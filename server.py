# ============================================================
#  server.py — GPS Tracker v3
#  Design : Ocean Blue + Violet — Style Stripe Premium
#  DB      : PostgreSQL (psycopg2)
# ============================================================

from flask import Flask, jsonify, request, session, redirect
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2, psycopg2.extras, os, json, threading, time, secrets
from functools import wraps
from pywebpush import webpush, WebPushException
import urllib.request, urllib.error

app = Flask(__name__)
app.secret_key = "gps_tracker_secret_key_2026"
app.config["SESSION_COOKIE_SECURE"] = os.environ.get("RENDER") is not None
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_HTTPONLY"] = True
CORS(app)

DATABASE_URL = os.environ.get("DATABASE_URL", "")

# ── VAPID Push Notifications ──
VAPID_PRIVATE_KEY   = os.environ.get("VAPID_PRIVATE_KEY", "")
VAPID_PUBLIC_KEY    = os.environ.get("VAPID_PUBLIC_KEY", "")
VAPID_CLAIMS_EMAIL  = os.environ.get("VAPID_CLAIMS_EMAIL", "admin@gps.com")
ALERTE_MINUTES      = 5   # minutes sans position → alerte

# ── Resend Email ──
RESEND_API_KEY   = os.environ.get("RESEND_API_KEY", "")
RESEND_FROM      = os.environ.get("RESEND_FROM_EMAIL", "onboarding@resend.dev")
APP_URL          = os.environ.get("APP_URL", "http://localhost:5000")

# ─────────────────────────────────────────────────────────────
#  BASE DE DONNÉES — PostgreSQL
# ─────────────────────────────────────────────────────────────

def get_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS utilisateurs (
        id SERIAL PRIMARY KEY,
        nom TEXT NOT NULL, prenom TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE, mot_de_passe TEXT NOT NULL,
        telephone TEXT, role TEXT NOT NULL DEFAULT 'user',
        actif INTEGER NOT NULL DEFAULT 1,
        date_creation TEXT DEFAULT (NOW()::text),
        derniere_connexion TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS vehicules (
        id SERIAL PRIMARY KEY,
        proprietaire_id INTEGER NOT NULL,
        marque TEXT NOT NULL, modele TEXT NOT NULL,
        immatriculation TEXT NOT NULL UNIQUE,
        type_vehicule TEXT NOT NULL,
        couleur TEXT, annee INTEGER,
        device_id TEXT NOT NULL UNIQUE,
        actif INTEGER NOT NULL DEFAULT 1,
        date_ajout TEXT DEFAULT (NOW()::text),
        FOREIGN KEY (proprietaire_id) REFERENCES utilisateurs(id))""")
    c.execute("""CREATE TABLE IF NOT EXISTS positions (
        id SERIAL PRIMARY KEY,
        vehicule_id INTEGER NOT NULL,
        latitude REAL NOT NULL, longitude REAL NOT NULL,
        vitesse REAL DEFAULT 0, altitude REAL DEFAULT 0,
        satellites INTEGER DEFAULT 0, timestamp TEXT,
        created_at TEXT DEFAULT (NOW()::text),
        FOREIGN KEY (vehicule_id) REFERENCES vehicules(id))""")
    c.execute("SELECT id FROM utilisateurs WHERE role='admin'")
    if not c.fetchone():
        c.execute(
            "INSERT INTO utilisateurs (nom,prenom,email,mot_de_passe,role) VALUES (%s,%s,%s,%s,%s)",
            ("Admin","GPS","admin@gps.com",generate_password_hash("admin123"),"admin"))
        print("[DB] Admin créé → admin@gps.com / admin123")
    # Table abonnements push
    c.execute("""CREATE TABLE IF NOT EXISTS push_subscriptions (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES utilisateurs(id) ON DELETE CASCADE,
        subscription TEXT NOT NULL,
        created_at TEXT DEFAULT (NOW()::text))""")
    # Table alertes envoyées (évite le spam)
    c.execute("""CREATE TABLE IF NOT EXISTS alertes_envoyees (
        vehicule_id INTEGER PRIMARY KEY,
        derniere_alerte TEXT)""")
    # Table tokens réinitialisation mot de passe
    c.execute("""CREATE TABLE IF NOT EXISTS reset_tokens (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL REFERENCES utilisateurs(id) ON DELETE CASCADE,
        token TEXT NOT NULL UNIQUE,
        expire_at TEXT NOT NULL,
        utilise INTEGER NOT NULL DEFAULT 0)""")
    conn.commit(); c.close(); conn.close()
    print("[DB] Base initialisée ✅")

# ─────────────────────────────────────────────────────────────
#  DÉCORATEURS
# ─────────────────────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Connexion requise"}), 401
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return jsonify({"error": "Connexion requise"}), 401
        if session.get("role") != "admin":
            return jsonify({"error": "Accès admin uniquement"}), 403
        return f(*args, **kwargs)
    return decorated

# ─────────────────────────────────────────────────────────────
#  AUTH
# ─────────────────────────────────────────────────────────────

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or not data.get("email") or not data.get("mot_de_passe"):
        return jsonify({"error": "Email et mot de passe requis"}), 400
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT * FROM utilisateurs WHERE email=%s", (data["email"],))
    user = c.fetchone()
    if not user or not user["actif"]:
        c.close(); conn.close()
        return jsonify({"error": "Compte introuvable ou désactivé"}), 401
    if not check_password_hash(user["mot_de_passe"], data["mot_de_passe"]):
        c.close(); conn.close()
        return jsonify({"error": "Email ou mot de passe incorrect"}), 401
    c.execute("UPDATE utilisateurs SET derniere_connexion=NOW()::text WHERE id=%s", (user["id"],))
    conn.commit(); c.close(); conn.close()
    session["user_id"] = user["id"]
    session["role"]    = user["role"]
    session["nom"]     = user["nom"]
    session["prenom"]  = user["prenom"]
    return jsonify({"status":"ok","role":user["role"],"user_id":user["id"],"prenom":user["prenom"]}), 200

@app.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"status":"ok"}), 200

@app.route("/api/me", methods=["GET"])
@login_required
def me():
    conn = get_db(); c = conn.cursor()
    c.execute(
        "SELECT id,nom,prenom,email,telephone,role,date_creation,derniere_connexion FROM utilisateurs WHERE id=%s",
        (session["user_id"],))
    user = c.fetchone()
    c.close(); conn.close()
    return jsonify(dict(user)), 200

# ─────────────────────────────────────────────────────────────
#  API ADMIN
# ─────────────────────────────────────────────────────────────

@app.route("/api/admin/proprietaires", methods=["GET"])
@admin_required
def get_proprietaires():
    conn = get_db(); c = conn.cursor()
    c.execute("""
        SELECT u.id,u.nom,u.prenom,u.email,u.telephone,u.actif,u.date_creation,
               COUNT(v.id) as nb_vehicules
        FROM utilisateurs u
        LEFT JOIN vehicules v ON v.proprietaire_id=u.id
        WHERE u.role='user' GROUP BY u.id ORDER BY u.date_creation DESC""")
    rows = c.fetchall()
    c.close(); conn.close()
    return jsonify([dict(r) for r in rows]), 200

@app.route("/api/admin/proprietaires", methods=["POST"])
@admin_required
def creer_proprietaire():
    data = request.get_json()
    for ch in ["nom","prenom","email","mot_de_passe","telephone"]:
        if not data.get(ch): return jsonify({"error":f"Champ manquant : {ch}"}), 400
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id FROM utilisateurs WHERE email=%s", (data["email"],))
    if c.fetchone():
        c.close(); conn.close(); return jsonify({"error":"Email déjà utilisé"}), 409
    c.execute(
        "INSERT INTO utilisateurs (nom,prenom,email,mot_de_passe,telephone,role) VALUES (%s,%s,%s,%s,%s,'user') RETURNING id",
        (data["nom"],data["prenom"],data["email"],generate_password_hash(data["mot_de_passe"]),data["telephone"]))
    new_id = c.fetchone()["id"]
    conn.commit(); c.close(); conn.close()
    return jsonify({"status":"ok","id":new_id}), 201

@app.route("/api/admin/proprietaires/<int:uid>/toggle", methods=["POST"])
@admin_required
def toggle_proprietaire(uid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT actif FROM utilisateurs WHERE id=%s AND role='user'", (uid,))
    user = c.fetchone()
    if not user: c.close(); conn.close(); return jsonify({"error":"Introuvable"}), 404
    nouvel = 0 if user["actif"] else 1
    c.execute("UPDATE utilisateurs SET actif=%s WHERE id=%s", (nouvel, uid))
    conn.commit(); c.close(); conn.close()
    return jsonify({"status":"ok","actif":nouvel}), 200

@app.route("/api/admin/vehicules", methods=["GET"])
@admin_required
def get_all_vehicules():
    conn = get_db(); c = conn.cursor()
    c.execute("""
        SELECT v.*,u.nom||' '||u.prenom as proprietaire_nom
        FROM vehicules v JOIN utilisateurs u ON u.id=v.proprietaire_id
        ORDER BY v.date_ajout DESC""")
    rows = c.fetchall()
    c.close(); conn.close()
    return jsonify([dict(r) for r in rows]), 200

@app.route("/api/admin/vehicules", methods=["POST"])
@admin_required
def creer_vehicule():
    data = request.get_json()
    for ch in ["proprietaire_id","marque","modele","immatriculation","type_vehicule","device_id"]:
        if not data.get(ch): return jsonify({"error":f"Champ manquant : {ch}"}), 400
    conn = get_db(); c = conn.cursor()
    try:
        c.execute("""INSERT INTO vehicules
            (proprietaire_id,marque,modele,immatriculation,type_vehicule,couleur,annee,device_id)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id""",
            (data["proprietaire_id"],data["marque"],data["modele"],data["immatriculation"],
             data["type_vehicule"],data.get("couleur",""),data.get("annee",2024),data["device_id"]))
        new_id = c.fetchone()["id"]
        conn.commit(); c.close(); conn.close()
        return jsonify({"status":"ok","id":new_id}), 201
    except Exception:
        conn.rollback(); c.close(); conn.close()
        return jsonify({"error":"Immatriculation ou device_id déjà utilisé"}), 409

@app.route("/api/admin/vehicules/<int:vid>/toggle", methods=["POST"])
@admin_required
def toggle_vehicule(vid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT actif FROM vehicules WHERE id=%s", (vid,))
    v = c.fetchone()
    if not v: c.close(); conn.close(); return jsonify({"error":"Introuvable"}), 404
    nouvel = 0 if v["actif"] else 1
    c.execute("UPDATE vehicules SET actif=%s WHERE id=%s", (nouvel, vid))
    conn.commit(); c.close(); conn.close()
    return jsonify({"status":"ok","actif":nouvel}), 200

@app.route("/api/user/vehicules", methods=["GET"])
@login_required
def get_user_vehicules():
    conn = get_db(); c = conn.cursor()
    c.execute("""
        SELECT * FROM vehicules WHERE proprietaire_id=%s AND actif=1
        ORDER BY date_ajout DESC""", (session["user_id"],))
    rows = c.fetchall()
    c.close(); conn.close()
    return jsonify([dict(r) for r in rows]), 200

@app.route("/api/position", methods=["POST"])
def receive_position():
    data = request.get_json()
    if not data or not data.get("device_id"):
        return jsonify({"error":"device_id manquant"}), 400
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id FROM vehicules WHERE device_id=%s AND actif=1", (data["device_id"],))
    v = c.fetchone()
    if not v: c.close(); conn.close(); return jsonify({"error":"Véhicule inconnu"}), 404
    c.execute("""INSERT INTO positions (vehicule_id,latitude,longitude,vitesse,altitude,satellites,timestamp)
        VALUES (%s,%s,%s,%s,%s,%s,%s)""",
        (v["id"],data["lat"],data["lng"],data.get("speed",0),
         data.get("altitude",0),data.get("satellites",0),data.get("timestamp","")))
    conn.commit(); c.close(); conn.close()
    return jsonify({"status":"ok"}), 200

@app.route("/api/positions/<int:vid>", methods=["GET"])
@login_required
def get_positions(vid):
    limit = request.args.get("limit", 200, type=int)
    conn = get_db(); c = conn.cursor()
    if session.get("role") != "admin":
        c.execute("SELECT id FROM vehicules WHERE id=%s AND proprietaire_id=%s",
            (vid, session["user_id"]))
        if not c.fetchone():
            c.close(); conn.close(); return jsonify({"error":"Accès refusé"}), 403
    c.execute("SELECT * FROM positions WHERE vehicule_id=%s ORDER BY id DESC LIMIT %s", (vid, limit))
    rows = c.fetchall()
    c.close(); conn.close()
    result = [dict(r) for r in rows]
    result.reverse()
    return jsonify(result), 200

@app.route("/api/positions/<int:vid>/last", methods=["GET"])
@login_required
def get_last_position(vid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT * FROM positions WHERE vehicule_id=%s ORDER BY id DESC LIMIT 1", (vid,))
    row = c.fetchone()
    c.close(); conn.close()
    if not row: return jsonify({"error":"Aucune position"}), 404
    return jsonify(dict(row)), 200

# ─────────────────────────────────────────────────────────────
#  MODIFICATION PROPRIÉTAIRE & VÉHICULE
# ─────────────────────────────────────────────────────────────

@app.route("/api/admin/proprietaires/<int:uid>", methods=["PUT"])
@admin_required
def modifier_proprietaire(uid):
    data = request.get_json()
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id FROM utilisateurs WHERE id=%s AND role='user'", (uid,))
    if not c.fetchone():
        c.close(); conn.close(); return jsonify({"error":"Introuvable"}), 404
    # Vérif email unique si changé
    if data.get("email"):
        c.execute("SELECT id FROM utilisateurs WHERE email=%s AND id!=%s", (data["email"], uid))
        if c.fetchone():
            c.close(); conn.close(); return jsonify({"error":"Email déjà utilisé"}), 409
    # Construction dynamique de la requête
    champs = []
    valeurs = []
    for col in ["nom","prenom","email","telephone"]:
        if data.get(col):
            champs.append(f"{col}=%s")
            valeurs.append(data[col])
    if data.get("mot_de_passe"):
        champs.append("mot_de_passe=%s")
        valeurs.append(generate_password_hash(data["mot_de_passe"]))
    if not champs:
        c.close(); conn.close(); return jsonify({"error":"Rien à modifier"}), 400
    valeurs.append(uid)
    c.execute(f"UPDATE utilisateurs SET {','.join(champs)} WHERE id=%s", valeurs)
    conn.commit(); c.close(); conn.close()
    return jsonify({"status":"ok"}), 200

@app.route("/api/admin/proprietaires/<int:uid>", methods=["GET"])
@admin_required
def get_proprietaire(uid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id,nom,prenom,email,telephone FROM utilisateurs WHERE id=%s AND role='user'", (uid,))
    row = c.fetchone()
    c.close(); conn.close()
    if not row: return jsonify({"error":"Introuvable"}), 404
    return jsonify(dict(row)), 200

@app.route("/api/admin/vehicules/<int:vid>", methods=["PUT"])
@admin_required
def modifier_vehicule(vid):
    data = request.get_json()
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id FROM vehicules WHERE id=%s", (vid,))
    if not c.fetchone():
        c.close(); conn.close(); return jsonify({"error":"Introuvable"}), 404
    champs = []
    valeurs = []
    for col in ["marque","modele","immatriculation","type_vehicule","couleur","device_id"]:
        if data.get(col):
            champs.append(f"{col}=%s")
            valeurs.append(data[col])
    if data.get("annee"):
        champs.append("annee=%s")
        valeurs.append(int(data["annee"]))
    if not champs:
        c.close(); conn.close(); return jsonify({"error":"Rien à modifier"}), 400
    valeurs.append(vid)
    try:
        c.execute(f"UPDATE vehicules SET {','.join(champs)} WHERE id=%s", valeurs)
        conn.commit(); c.close(); conn.close()
        return jsonify({"status":"ok"}), 200
    except Exception:
        conn.rollback(); c.close(); conn.close()
        return jsonify({"error":"Immatriculation ou device_id déjà utilisé"}), 409

@app.route("/api/admin/vehicules/<int:vid>", methods=["GET"])
@admin_required
def get_vehicule(vid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT * FROM vehicules WHERE id=%s", (vid,))
    row = c.fetchone()
    c.close(); conn.close()
    if not row: return jsonify({"error":"Introuvable"}), 404
    return jsonify(dict(row)), 200

# ─────────────────────────────────────────────────────────────
#  MOT DE PASSE OUBLIÉ
# ─────────────────────────────────────────────────────────────

def envoyer_email_reset(email, prenom, lien):
    """Envoie l'email de réinitialisation via Resend API."""
    try:
        payload = json.dumps({
            "from": RESEND_FROM,
            "to": [email],
            "subject": "Réinitialisation de votre mot de passe — GPS Tracker",
            "html": f"""
            <div style="font-family:Inter,sans-serif;max-width:480px;margin:0 auto;padding:32px">
              <div style="text-align:center;margin-bottom:28px">
                <div style="width:56px;height:56px;border-radius:16px;
                  background:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
                  display:inline-flex;align-items:center;justify-content:center;
                  font-size:24px">🛰️</div>
                <h1 style="font-size:20px;font-weight:700;color:#111827;margin-top:12px">GPS Tracker</h1>
              </div>
              <h2 style="font-size:18px;font-weight:700;color:#111827;margin-bottom:8px">
                Bonjour {prenom},
              </h2>
              <p style="color:#6B7280;font-size:14px;line-height:1.7;margin-bottom:24px">
                Vous avez demandé la réinitialisation de votre mot de passe.<br>
                Cliquez sur le bouton ci-dessous. Ce lien est valable <strong>30 minutes</strong>.
              </p>
              <a href="{lien}" style="display:block;text-align:center;padding:14px 24px;
                background:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
                color:#fff;border-radius:12px;text-decoration:none;
                font-weight:600;font-size:15px;margin-bottom:24px">
                Réinitialiser mon mot de passe →
              </a>
              <p style="color:#9CA3AF;font-size:12px;text-align:center">
                Si vous n'avez pas demandé cette réinitialisation, ignorez cet email.
              </p>
            </div>"""
        }).encode("utf-8")
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=payload,
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type": "application/json"
            }
        )
        urllib.request.urlopen(req)
        return True
    except Exception as e:
        print(f"[EMAIL] Erreur envoi : {e}")
        return False

@app.route("/api/forgot-password", methods=["POST"])
def forgot_password():
    data = request.get_json()
    if not data or not data.get("email"):
        return jsonify({"error":"Email requis"}), 400
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id,prenom FROM utilisateurs WHERE email=%s AND role='user' AND actif=1",
              (data["email"],))
    user = c.fetchone()
    if not user:
        # Sécurité : on répond OK même si l'email n'existe pas
        c.close(); conn.close()
        return jsonify({"status":"ok"}), 200
    token = secrets.token_urlsafe(32)
    # Supprime les anciens tokens de cet utilisateur
    c.execute("DELETE FROM reset_tokens WHERE user_id=%s", (user["id"],))
    c.execute("""INSERT INTO reset_tokens (user_id, token, expire_at)
        VALUES (%s, %s, (NOW() + INTERVAL '30 minutes')::text)""",
        (user["id"], token))
    conn.commit(); c.close(); conn.close()
    lien = f"{APP_URL}/reset-password?token={token}"
    envoyer_email_reset(data["email"], user["prenom"], lien)
    return jsonify({"status":"ok"}), 200

@app.route("/api/reset-password", methods=["POST"])
def reset_password():
    data = request.get_json()
    if not data or not data.get("token") or not data.get("mot_de_passe"):
        return jsonify({"error":"Données manquantes"}), 400
    conn = get_db(); c = conn.cursor()
    c.execute("""SELECT rt.user_id FROM reset_tokens rt
        WHERE rt.token=%s AND rt.utilise=0
        AND rt.expire_at::timestamp > NOW()""", (data["token"],))
    row = c.fetchone()
    if not row:
        c.close(); conn.close()
        return jsonify({"error":"Lien invalide ou expiré"}), 400
    c.execute("UPDATE utilisateurs SET mot_de_passe=%s WHERE id=%s",
              (generate_password_hash(data["mot_de_passe"]), row["user_id"]))
    c.execute("UPDATE reset_tokens SET utilise=1 WHERE token=%s", (data["token"],))
    conn.commit(); c.close(); conn.close()
    return jsonify({"status":"ok"}), 200

@app.route("/api/reset-password/check", methods=["GET"])
def check_reset_token():
    token = request.args.get("token","")
    conn = get_db(); c = conn.cursor()
    c.execute("""SELECT id FROM reset_tokens
        WHERE token=%s AND utilise=0 AND expire_at::timestamp > NOW()""", (token,))
    row = c.fetchone()
    c.close(); conn.close()
    return jsonify({"valid": row is not None}), 200

# ─────────────────────────────────────────────────────────────
#  PUSH NOTIFICATIONS
# ─────────────────────────────────────────────────────────────

@app.route("/api/push/vapid-public-key", methods=["GET"])
@login_required
def get_vapid_public_key():
    return jsonify({"publicKey": VAPID_PUBLIC_KEY}), 200

@app.route("/api/push/subscribe", methods=["POST"])
@login_required
def push_subscribe():
    data = request.get_json()
    if not data or not data.get("subscription"):
        return jsonify({"error": "Subscription manquante"}), 400
    sub_str = json.dumps(data["subscription"])
    conn = get_db(); c = conn.cursor()
    # Supprimer ancien abonnement du même user
    c.execute("DELETE FROM push_subscriptions WHERE user_id=%s", (session["user_id"],))
    c.execute("INSERT INTO push_subscriptions (user_id, subscription) VALUES (%s,%s)",
              (session["user_id"], sub_str))
    conn.commit(); c.close(); conn.close()
    return jsonify({"status": "ok"}), 200

@app.route("/api/push/unsubscribe", methods=["POST"])
@login_required
def push_unsubscribe():
    conn = get_db(); c = conn.cursor()
    c.execute("DELETE FROM push_subscriptions WHERE user_id=%s", (session["user_id"],))
    conn.commit(); c.close(); conn.close()
    return jsonify({"status": "ok"}), 200

@app.route("/api/push/status", methods=["GET"])
@login_required
def push_status():
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id FROM push_subscriptions WHERE user_id=%s", (session["user_id"],))
    row = c.fetchone()
    c.close(); conn.close()
    return jsonify({"subscribed": row is not None}), 200

def envoyer_push(subscription_str, titre, corps):
    """Envoie une notification push à un abonné."""
    try:
        sub = json.loads(subscription_str)
        webpush(
            subscription_info=sub,
            data=json.dumps({"title": titre, "body": corps}),
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims={"sub": f"mailto:{VAPID_CLAIMS_EMAIL}"}
        )
        return True
    except WebPushException as e:
        print(f"[PUSH] Erreur envoi : {e}")
        return False
    except Exception as e:
        print(f"[PUSH] Erreur inattendue : {e}")
        return False

def surveillance_vehicules():
    """Thread : vérifie toutes les 2 minutes si un véhicule est hors réseau."""
    print("[SURVEILLANCE] Thread démarré ✅")
    while True:
        time.sleep(120)  # vérifie toutes les 2 minutes
        try:
            conn = get_db(); c = conn.cursor()
            # Récupère tous les véhicules actifs avec leur dernière position
            c.execute("""
                SELECT v.id, v.immatriculation, v.marque, v.modele,
                       v.proprietaire_id,
                       p.created_at as derniere_pos
                FROM vehicules v
                LEFT JOIN positions p ON p.id = (
                    SELECT id FROM positions
                    WHERE vehicule_id = v.id
                    ORDER BY id DESC LIMIT 1
                )
                WHERE v.actif = 1
            """)
            vehicules = c.fetchall()
            for veh in vehicules:
                if not veh["derniere_pos"]:
                    continue  # jamais de position, on ignore
                # Calcul du temps depuis la dernière position
                c.execute("""
                    SELECT EXTRACT(EPOCH FROM (NOW() - %s::timestamp))/60 as minutes
                """, (veh["derniere_pos"],))
                res = c.fetchone()
                if not res: continue
                minutes_ecoulees = res["minutes"] or 0
                if minutes_ecoulees < ALERTE_MINUTES:
                    # Véhicule connecté → réinitialise l'alerte si elle existait
                    c.execute("DELETE FROM alertes_envoyees WHERE vehicule_id=%s", (veh["id"],))
                    conn.commit()
                    continue
                # Vérifie si une alerte a déjà été envoyée pour ce véhicule
                c.execute("SELECT derniere_alerte FROM alertes_envoyees WHERE vehicule_id=%s", (veh["id"],))
                alerte = c.fetchone()
                if alerte:
                    continue  # alerte déjà envoyée, on attend la reconnexion
                # Récupère l'abonnement push du propriétaire
                c.execute("SELECT subscription FROM push_subscriptions WHERE user_id=%s",
                          (veh["proprietaire_id"],))
                sub = c.fetchone()
                if not sub:
                    continue  # propriétaire pas abonné aux notifications
                # Envoie la notification
                titre = f"⚠️ Véhicule hors réseau"
                corps = (f"{veh['immatriculation']} — {veh['marque']} {veh['modele']}\n"
                         f"Aucun signal depuis {int(minutes_ecoulees)} minutes.")
                succes = envoyer_push(sub["subscription"], titre, corps)
                if succes:
                    # Marque l'alerte comme envoyée
                    c.execute("""
                        INSERT INTO alertes_envoyees (vehicule_id, derniere_alerte)
                        VALUES (%s, NOW()::text)
                        ON CONFLICT (vehicule_id) DO UPDATE SET derniere_alerte=NOW()::text
                    """, (veh["id"],))
                    conn.commit()
                    print(f"[PUSH] Alerte envoyée pour {veh['immatriculation']}")
            c.close(); conn.close()
        except Exception as e:
            print(f"[SURVEILLANCE] Erreur : {e}")

# ─────────────────────────────────────────────────────────────
#  ROUTES HTML
# ─────────────────────────────────────────────────────────────

@app.route("/sw.js")
def service_worker():
    sw_code = """
self.addEventListener('push', function(e){
  const data = e.data ? e.data.json() : {};
  const title = data.title || 'GPS Tracker';
  const options = {
    body: data.body || '',
    icon: 'https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png',
    badge: 'https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png',
    vibrate: [200, 100, 200],
    tag: 'gps-alerte',
    renotify: true
  };
  e.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', function(e){
  e.notification.close();
  e.waitUntil(clients.openWindow('/dashboard'));
});
"""
    from flask import Response
    return Response(sw_code, mimetype="application/javascript")

@app.route("/reset-password")
def reset_password_page():
    return RESET_PAGE

@app.route("/")
def index():
    return LOGIN_PAGE

@app.route("/admin")
def admin_page():
    if "user_id" not in session or session.get("role") != "admin":
        return redirect("/")
    return ADMIN_PAGE

@app.route("/dashboard")
def user_dashboard():
    if "user_id" not in session or session.get("role") != "user":
        return redirect("/")
    return USER_PAGE

# ═════════════════════════════════════════════════════════════
#  PAGE LOGIN
# ═════════════════════════════════════════════════════════════

LOGIN_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Connexion</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#F5F3FF;--surface:#FFFFFF;--border:#E5E7EB;
  --primary:#6366F1;--primary2:#4F46E5;--cyan:#06B6D4;--violet:#7C3AED;
  --grad:linear-gradient(135deg,#6366F1,#06B6D4);
  --grad2:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
  --green:#10B981;--red:#F43F5E;
  --text:#111827;--text2:#6B7280;--text3:#9CA3AF;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;min-height:100vh;display:flex;
  align-items:center;justify-content:center;position:relative;overflow:hidden;
  background:linear-gradient(160deg,#EDE9FE 0%,#E0F2FE 55%,#F0FDF4 100%)}
.orb{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
.o1{width:500px;height:500px;background:radial-gradient(circle,rgba(99,102,241,0.15),transparent);top:-120px;right:-80px}
.o2{width:400px;height:400px;background:radial-gradient(circle,rgba(6,182,212,0.12),transparent);bottom:-80px;left:-60px}
.o3{width:250px;height:250px;background:radial-gradient(circle,rgba(124,58,237,0.1),transparent);top:50%;left:30%}
.card{position:relative;z-index:1;background:rgba(255,255,255,0.85);
  backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.9);
  border-radius:24px;padding:52px 44px;width:100%;max-width:430px;
  box-shadow:0 8px 40px rgba(99,102,241,0.12),0 2px 8px rgba(0,0,0,0.04)}
@media(max-width:480px){.card{padding:36px 24px;margin:16px;border-radius:20px}}
.logo{text-align:center;margin-bottom:38px}
.logo-wrap{position:relative;width:72px;height:72px;margin:0 auto 16px}
.logo-bg{width:72px;height:72px;border-radius:20px;background:var(--grad2);
  display:flex;align-items:center;justify-content:center;font-size:30px;
  box-shadow:0 8px 28px rgba(99,102,241,0.35)}
.logo-ring{position:absolute;inset:-5px;border-radius:25px;
  border:2px solid transparent;
  background:linear-gradient(135deg,rgba(99,102,241,0.4),rgba(6,182,212,0.4)) border-box;
  -webkit-mask:linear-gradient(#fff 0 0) padding-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:destination-out;mask-composite:exclude}
.logo h1{font-size:24px;font-weight:700;letter-spacing:-0.5px;
  background:var(--grad2);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.logo p{color:var(--text3);font-size:13px;margin-top:5px}
.fg{margin-bottom:18px}
.fg label{display:block;font-size:11px;font-weight:700;color:var(--text2);
  margin-bottom:7px;text-transform:uppercase;letter-spacing:0.7px}
.iw{position:relative}
.ii{position:absolute;left:13px;top:50%;transform:translateY(-50%);font-size:15px;opacity:0.35;pointer-events:none}
input{width:100%;height:44px;padding:0 14px 0 42px;
  background:#FAFAFA;border:1.5px solid #E5E7EB;
  border-radius:12px;font-size:14px;font-family:'Inter',sans-serif;
  color:var(--text);outline:none;transition:all 0.2s}
input:hover{border-color:#D1D5DB;background:#fff}
input:focus{border-color:var(--primary);background:#fff;box-shadow:0 0 0 4px rgba(99,102,241,0.1)}
input::placeholder{color:var(--text3)}
.btn{width:100%;height:46px;margin-top:6px;background:var(--grad2);
  border:none;border-radius:12px;color:#fff;font-family:'Inter',sans-serif;
  font-size:14px;font-weight:600;cursor:pointer;letter-spacing:0.2px;
  box-shadow:0 4px 16px rgba(99,102,241,0.4);transition:all 0.2s}
.btn:hover{transform:translateY(-1px);box-shadow:0 8px 24px rgba(99,102,241,0.45)}
.btn:active{transform:translateY(0)}
.err{background:#FFF1F2;border:1px solid #FECDD3;color:var(--red);
  padding:11px 14px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}
.trust{display:flex;justify-content:center;gap:20px;margin-top:22px;flex-wrap:wrap}
.trust-item{display:flex;align-items:center;gap:5px;font-size:11px;color:var(--text3)}
.trust-dot{width:6px;height:6px;border-radius:50%;background:var(--grad)}
</style></head><body>
<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
<div class="card">
  <div class="logo">
    <div class="logo-wrap">
      <div class="logo-bg">🛰️</div>
      <div class="logo-ring"></div>
    </div>
    <h1>GPS Tracker</h1>
    <p>Système de suivi de véhicules en temps réel</p>
  </div>
  <div class="err" id="err"></div>
  <div class="fg">
    <label>Adresse email</label>
    <div class="iw"><span class="ii">✉️</span>
      <input type="email" id="email" placeholder="votre@email.com"/></div>
  </div>
  <div class="fg">
    <label>Mot de passe</label>
    <div class="iw"><span class="ii">🔑</span>
      <input type="password" id="pwd" placeholder="••••••••"
             onkeydown="if(event.key==='Enter')doLogin()"/></div>
  </div>
  <button class="btn" onclick="doLogin()">Se connecter →</button>
  <div style="text-align:center;margin-top:14px">
    <a href="#" onclick="showForgot()" style="font-size:12px;color:var(--text3);text-decoration:none;
      transition:color 0.2s" onmouseover="this.style.color='var(--primary)'"
      onmouseout="this.style.color='var(--text3)'">Mot de passe oublié ?</a>
  </div>
  <div class="trust">
    <div class="trust-item"><div class="trust-dot"></div>Sécurisé</div>
    <div class="trust-item"><div class="trust-dot"></div>Temps réel</div>
    <div class="trust-item"><div class="trust-dot"></div>GPS IoT</div>
  </div>
</div>

<!-- MODAL MOT DE PASSE OUBLIÉ -->
<div id="forgot-bg" style="display:none;position:fixed;inset:0;background:rgba(17,24,39,0.45);
  backdrop-filter:blur(4px);z-index:200;align-items:center;justify-content:center;padding:16px">
  <div style="background:#fff;border-radius:20px;padding:32px;width:100%;max-width:400px;
    position:relative;box-shadow:0 20px 60px rgba(0,0,0,0.12)">
    <div style="position:absolute;top:0;left:20%;right:20%;height:3px;
      background:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);border-radius:0 0 4px 4px"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px">
      <h3 style="font-size:16px;font-weight:700;color:#111827">Mot de passe oublié</h3>
      <button onclick="hideForgot()" style="width:28px;height:28px;border-radius:8px;
        border:1px solid #E5E7EB;background:transparent;cursor:pointer;font-size:14px;color:#9CA3AF">✕</button>
    </div>
    <p style="font-size:13px;color:#6B7280;margin-bottom:16px;line-height:1.6">
      Entrez votre email. Vous recevrez un lien pour réinitialiser votre mot de passe.
    </p>
    <div id="forgot-err" style="background:#FFF1F2;border:1px solid #FECDD3;color:#F43F5E;
      padding:10px 13px;border-radius:10px;font-size:12px;margin-bottom:12px;display:none"></div>
    <div id="forgot-ok" style="background:#F0FDF4;border:1px solid #BBF7D0;color:#10B981;
      padding:10px 13px;border-radius:10px;font-size:12px;margin-bottom:12px;display:none"></div>
    <div style="margin-bottom:16px">
      <label style="display:block;font-size:11px;font-weight:700;color:#6B7280;
        margin-bottom:7px;text-transform:uppercase;letter-spacing:0.7px">Email</label>
      <input type="email" id="forgot-email" placeholder="votre@email.com"
        style="width:100%;height:42px;padding:0 13px;background:#FAFAFA;
          border:1.5px solid #E5E7EB;border-radius:10px;font-size:13px;
          font-family:Inter,sans-serif;color:#111827;outline:none"
        onkeydown="if(event.key==='Enter')doForgot()"/>
    </div>
    <button onclick="doForgot()" style="width:100%;height:42px;background:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
      border:none;border-radius:10px;color:#fff;font-family:Inter,sans-serif;
      font-size:13px;font-weight:600;cursor:pointer">Envoyer le lien →</button>
  </div>
</div>
<script>
async function doLogin(){
  const email=document.getElementById("email").value.trim();
  const pwd=document.getElementById("pwd").value;
  const err=document.getElementById("err");
  err.style.display="none";
  if(!email||!pwd){err.textContent="Veuillez remplir tous les champs.";err.style.display="block";return;}
  const res=await fetch("/api/login",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify({email,mot_de_passe:pwd})});
  const data=await res.json();
  if(res.ok){window.location.href=data.role==="admin"?"/admin":"/dashboard";}
  else{err.textContent=data.error||"Identifiants incorrects.";err.style.display="block";}
}
function showForgot(){
  document.getElementById("forgot-bg").style.display="flex";
  document.getElementById("forgot-err").style.display="none";
  document.getElementById("forgot-ok").style.display="none";
  document.getElementById("forgot-email").value="";
}
function hideForgot(){document.getElementById("forgot-bg").style.display="none";}
async function doForgot(){
  const email=document.getElementById("forgot-email").value.trim();
  const err=document.getElementById("forgot-err");
  const ok=document.getElementById("forgot-ok");
  err.style.display=ok.style.display="none";
  if(!email){err.textContent="Veuillez entrer votre email.";err.style.display="block";return;}
  await fetch("/api/forgot-password",{method:"POST",
    headers:{"Content-Type":"application/json"},body:JSON.stringify({email})});
  ok.textContent="Si cet email existe, vous recevrez un lien dans quelques minutes.";
  ok.style.display="block";
}
</script></body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE RESET PASSWORD
# ═════════════════════════════════════════════════════════════

RESET_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Nouveau mot de passe</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --grad2:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
  --green:#10B981;--red:#F43F5E;--text:#111827;--text2:#6B7280;--text3:#9CA3AF;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;min-height:100vh;display:flex;align-items:center;
  justify-content:center;background:linear-gradient(160deg,#EDE9FE 0%,#E0F2FE 55%,#F0FDF4 100%);
  padding:16px}
.card{background:rgba(255,255,255,0.9);backdrop-filter:blur(20px);
  border:1px solid rgba(255,255,255,0.9);border-radius:24px;
  padding:48px 40px;width:100%;max-width:420px;
  box-shadow:0 8px 40px rgba(99,102,241,0.12)}
@media(max-width:480px){.card{padding:32px 22px}}
.logo{text-align:center;margin-bottom:32px}
.logo-bg{width:64px;height:64px;border-radius:18px;background:var(--grad2);
  display:flex;align-items:center;justify-content:center;font-size:26px;
  margin:0 auto 14px;box-shadow:0 6px 22px rgba(99,102,241,0.35)}
.logo h1{font-size:22px;font-weight:700;
  background:var(--grad2);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.logo p{color:var(--text3);font-size:13px;margin-top:4px}
.fg{margin-bottom:16px}
.fg label{display:block;font-size:11px;font-weight:700;color:var(--text2);
  margin-bottom:7px;text-transform:uppercase;letter-spacing:0.7px}
.iw{position:relative}
.ii{position:absolute;left:13px;top:50%;transform:translateY(-50%);font-size:15px;opacity:0.35;pointer-events:none}
input{width:100%;height:44px;padding:0 14px 0 42px;background:#FAFAFA;
  border:1.5px solid #E5E7EB;border-radius:12px;font-size:14px;
  font-family:'Inter',sans-serif;color:var(--text);outline:none;transition:all 0.2s}
input:focus{border-color:#6366F1;background:#fff;box-shadow:0 0 0 4px rgba(99,102,241,0.1)}
.btn{width:100%;height:46px;margin-top:6px;background:var(--grad2);border:none;
  border-radius:12px;color:#fff;font-family:'Inter',sans-serif;font-size:14px;
  font-weight:600;cursor:pointer;box-shadow:0 4px 16px rgba(99,102,241,0.4);transition:all 0.2s}
.btn:hover{transform:translateY(-1px)}
.err{background:#FFF1F2;border:1px solid #FECDD3;color:var(--red);
  padding:11px 14px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}
.ok{background:#F0FDF4;border:1px solid #BBF7D0;color:var(--green);
  padding:11px 14px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}
.exp{background:#FFF7ED;border:1px solid #FED7AA;color:#C2410C;
  padding:16px;border-radius:12px;text-align:center;font-size:13px;display:none}
</style></head><body>
<div class="card">
  <div class="logo">
    <div class="logo-bg">🔑</div>
    <h1>Nouveau mot de passe</h1>
    <p>Choisissez un nouveau mot de passe sécurisé</p>
  </div>
  <div class="exp" id="exp">
    <div style="font-size:24px;margin-bottom:8px">⏰</div>
    <div style="font-weight:700;margin-bottom:4px">Lien expiré</div>
    <div style="color:#9A3412">Ce lien n'est plus valide. Faites une nouvelle demande sur la page de connexion.</div>
  </div>
  <div id="form-wrap">
    <div class="err" id="err"></div>
    <div class="ok" id="ok"></div>
    <div class="fg">
      <label>Nouveau mot de passe</label>
      <div class="iw"><span class="ii">🔑</span>
        <input type="password" id="pwd1" placeholder="Minimum 6 caractères"/></div>
    </div>
    <div class="fg">
      <label>Confirmer le mot de passe</label>
      <div class="iw"><span class="ii">🔑</span>
        <input type="password" id="pwd2" placeholder="Répétez le mot de passe"
          onkeydown="if(event.key==='Enter')doReset()"/></div>
    </div>
    <button class="btn" onclick="doReset()">Enregistrer le mot de passe →</button>
  </div>
</div>
<script>
const token=new URLSearchParams(window.location.search).get("token");
async function init(){
  if(!token){showExpired();return;}
  const r=await fetch(`/api/reset-password/check?token=${token}`).then(x=>x.json());
  if(!r.valid)showExpired();
}
function showExpired(){
  document.getElementById("exp").style.display="block";
  document.getElementById("form-wrap").style.display="none";
}
async function doReset(){
  const pwd1=document.getElementById("pwd1").value;
  const pwd2=document.getElementById("pwd2").value;
  const err=document.getElementById("err");
  const ok=document.getElementById("ok");
  err.style.display=ok.style.display="none";
  if(!pwd1||!pwd2){err.textContent="Veuillez remplir les deux champs.";err.style.display="block";return;}
  if(pwd1.length<6){err.textContent="Le mot de passe doit faire au moins 6 caractères.";err.style.display="block";return;}
  if(pwd1!==pwd2){err.textContent="Les mots de passe ne correspondent pas.";err.style.display="block";return;}
  const res=await fetch("/api/reset-password",{method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({token,mot_de_passe:pwd1})});
  const data=await res.json();
  if(res.ok){
    ok.textContent="✓ Mot de passe modifié ! Redirection...";ok.style.display="block";
    document.getElementById("pwd1").value="";document.getElementById("pwd2").value="";
    setTimeout(()=>window.location.href="/",2500);
  }else{err.textContent=data.error||"Erreur.";err.style.display="block";}
}
init();
</script></body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE ADMIN — CORRIGÉE (id="pt" → id="p-tel", responsive mobile)
# ═════════════════════════════════════════════════════════════

ADMIN_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Admin</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#F8F7FF;--surface:#FFFFFF;--surface2:#F9FAFB;--border:#E5E7EB;--border2:#D1D5DB;
  --primary:#6366F1;--primary2:#4F46E5;--violet:#7C3AED;--cyan:#06B6D4;
  --grad:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
  --grad2:linear-gradient(135deg,#6366F1,#06B6D4);
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-bd:rgba(16,185,129,0.2);
  --red:#F43F5E;--red-bg:rgba(244,63,94,0.08);--red-bd:rgba(244,63,94,0.2);
  --amber:#F59E0B;--text:#111827;--text2:#6B7280;--text3:#9CA3AF;
  --sidebar-w:256px;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);font-size:14px;display:flex;min-height:100vh}

/* ══ SIDEBAR ══ */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:var(--surface);border-right:1px solid var(--border);
  display:flex;flex-direction:column;z-index:100;overflow:hidden;
  transition:left 0.25s ease
}
.sidebar::before{content:'';position:absolute;top:0;left:0;right:0;height:180px;
  background:linear-gradient(180deg,rgba(99,102,241,0.06),transparent);pointer-events:none}
.s-logo{padding:22px 20px 18px;border-bottom:1px solid var(--border);position:relative}
.s-logo-row{display:flex;align-items:center;gap:12px}
.s-logo-icon{width:40px;height:40px;border-radius:12px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:19px;
  box-shadow:0 4px 14px rgba(99,102,241,0.35);flex-shrink:0}
.s-logo-name{font-size:15px;font-weight:700;color:var(--text);letter-spacing:-0.3px}
.s-logo-sub{font-size:10px;color:var(--text3);margin-top:2px;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:600}
.s-admin{margin:14px 12px;padding:12px 14px;
  background:linear-gradient(135deg,rgba(124,58,237,0.07),rgba(99,102,241,0.05));
  border:1px solid rgba(124,58,237,0.15);border-radius:12px}
.s-admin-row{display:flex;align-items:center;gap:10px}
.s-avatar{width:36px;height:36px;border-radius:10px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.s-admin-name{font-size:13px;font-weight:600;color:var(--text)}
.s-admin-role{font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.8px;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.s-nav{flex:1;padding:10px 10px 0;overflow-y:auto}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 14px;
  border-radius:10px;cursor:pointer;color:var(--text2);font-size:13px;
  font-weight:500;transition:all 0.15s;margin-bottom:2px;
  border-left:3px solid transparent;position:relative}
.nav-item:hover{background:rgba(99,102,241,0.06);color:var(--primary)}
.nav-item.active{background:linear-gradient(135deg,rgba(124,58,237,0.09),rgba(99,102,241,0.07));
  color:var(--primary);font-weight:600;border-left-color:var(--violet)}
.nav-item.active .nav-ico{background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-ico{font-size:16px;width:22px;text-align:center;flex-shrink:0;transition:all 0.15s}
.s-bottom{padding:14px 12px;border-top:1px solid var(--border);background:var(--surface);flex-shrink:0}
.btn-logout{width:100%;padding:10px 16px;background:var(--red-bg);color:var(--red);
  border:1px solid var(--red-bd);border-radius:10px;cursor:pointer;font-size:13px;font-weight:600;
  font-family:'Inter',sans-serif;transition:all 0.15s;
  display:flex;align-items:center;justify-content:center;gap:8px}
.btn-logout:hover{background:rgba(244,63,94,0.14);border-color:rgba(244,63,94,0.35)}

/* ══ MAIN ══ */
.main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;min-width:0}
.topbar{position:sticky;top:0;z-index:50;height:60px;padding:0 28px;
  background:rgba(255,255,255,0.9);backdrop-filter:blur(12px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
  box-shadow:0 1px 4px rgba(0,0,0,0.04)}
.tb-left{display:flex;align-items:center;gap:8px}
.tb-crumb{font-size:12px;color:var(--text3);font-weight:500}
.tb-page-title{font-size:18px;font-weight:700;color:var(--text);letter-spacing:-0.3px}
.tb-right{display:flex;align-items:center;gap:10px}
.clock{padding:5px 14px;background:var(--surface2);border:1px solid var(--border);
  border-radius:8px;font-size:12px;color:var(--text2);font-variant-numeric:tabular-nums;font-weight:500}
.menu-btn{display:none;background:none;border:none;cursor:pointer;
  font-size:22px;color:var(--text);padding:4px 8px;margin-right:4px}

.content{padding:28px;flex:1}
.section{display:none}
.section.active{display:block;animation:fadeUp 0.2s ease}
@keyframes fadeUp{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}

/* ── Stats ── */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:28px}
.stat{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:22px;position:relative;overflow:hidden;transition:all 0.2s}
.stat:hover{border-color:rgba(99,102,241,0.25);box-shadow:0 4px 20px rgba(99,102,241,0.1);transform:translateY(-2px)}
.stat-top{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:14px}
.stat-icon{width:44px;height:44px;border-radius:12px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:20px;
  box-shadow:0 4px 14px rgba(99,102,241,0.3)}
.stat-trend{font-size:11px;font-weight:600;padding:3px 10px;border-radius:99px;
  background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
.stat-val{font-size:34px;font-weight:700;color:var(--text);letter-spacing:-1.5px;line-height:1}
.stat-lbl{font-size:12px;color:var(--text3);margin-top:5px;font-weight:500}
.stat::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px;background:var(--grad)}
.stat::before{content:'';position:absolute;top:0;right:0;width:80px;height:80px;
  background:radial-gradient(circle,rgba(99,102,241,0.06),transparent);pointer-events:none}

/* ── Section header ── */
.sh{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:10px}
.sh h2{font-size:17px;font-weight:700;color:var(--text);letter-spacing:-0.3px}
.sh-sub{font-size:13px;color:var(--text3);margin-top:2px}

/* ── Boutons ── */
.btn{height:40px;padding:0 18px;border:none;border-radius:10px;cursor:pointer;
  font-size:13px;font-weight:600;font-family:'Inter',sans-serif;
  transition:all 0.2s;display:inline-flex;align-items:center;gap:7px}
.btn-primary{background:var(--grad);color:#fff;box-shadow:0 3px 12px rgba(99,102,241,0.35)}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 6px 20px rgba(99,102,241,0.45)}
.btn-danger{background:var(--red-bg);color:var(--red);border:1px solid var(--red-bd)}
.btn-danger:hover{background:rgba(244,63,94,0.14)}
.btn-success{background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
.btn-success:hover{background:rgba(16,185,129,0.14)}
.btn-sm{height:30px;padding:0 13px;font-size:12px;border-radius:8px}

/* ── Table ── */
.table-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;overflow:hidden;
  box-shadow:0 1px 4px rgba(0,0,0,0.04)}
.table-wrap{overflow-x:auto}
table{width:100%;border-collapse:separate;border-spacing:0;min-width:600px}
thead{background:var(--surface2)}
th{padding:12px 18px;text-align:left;font-size:11px;color:var(--text3);
  font-weight:700;text-transform:uppercase;letter-spacing:0.8px;border-bottom:1px solid var(--border)}
tbody tr{transition:background 0.12s}
tbody tr:hover td{background:rgba(99,102,241,0.025)}
td{padding:14px 18px;font-size:13px;color:var(--text2);border-bottom:1px solid var(--border)}
tbody tr:last-child td{border-bottom:none}
.td-main{font-weight:600;color:var(--text)}
.device{font-size:11px;background:rgba(99,102,241,0.07);color:var(--primary);
  padding:3px 9px;border-radius:6px;font-weight:600;
  border:1px solid rgba(99,102,241,0.15);font-family:monospace}
.badge{padding:4px 12px;border-radius:99px;font-size:11px;font-weight:600;
  display:inline-flex;align-items:center;gap:5px}
.badge::before{content:'';width:5px;height:5px;border-radius:50%}
.badge-on{background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
.badge-on::before{background:var(--green)}
.badge-off{background:var(--red-bg);color:var(--red);border:1px solid var(--red-bd)}
.badge-off::before{background:var(--red)}

/* ── Positions propriétaires ── */
.prop-positions{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px}
.pp-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;
  padding:16px 18px;position:relative;overflow:hidden;transition:all 0.2s}
.pp-card:hover{border-color:rgba(99,102,241,0.2);box-shadow:0 3px 14px rgba(99,102,241,0.08)}
.pp-card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:var(--grad)}
.pp-icon{font-size:22px;margin-bottom:8px}
.pp-val{font-size:28px;font-weight:700;color:var(--text);letter-spacing:-1px;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.pp-lbl{font-size:12px;color:var(--text3);font-weight:500;margin-top:3px}

/* ── Empty ── */
.empty{padding:52px;text-align:center}
.empty-ico{font-size:44px;margin-bottom:12px;opacity:0.25}
.empty-txt{font-size:14px;font-weight:600;color:var(--text2)}
.empty-sub{font-size:12px;color:var(--text3);margin-top:4px}

/* ── Historique ── */
.h-filters{display:flex;gap:10px;margin-bottom:20px;align-items:center;flex-wrap:wrap}
.h-select{height:38px;padding:0 13px;background:var(--surface);border:1px solid var(--border);
  border-radius:10px;font-size:13px;font-family:'Inter',sans-serif;color:var(--text);outline:none;transition:all 0.15s}
.h-select:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(99,102,241,0.1)}
.h-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
.hs{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:14px 16px}
.hs-val{font-size:22px;font-weight:700;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hs-lbl{font-size:11px;color:var(--text3);font-weight:500;margin-top:3px}

/* ── Paramètres ── */
.param-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:24px;margin-bottom:14px}
.param-title{font-size:14px;font-weight:700;color:var(--text);margin-bottom:3px}
.param-sub{font-size:12px;color:var(--text3);margin-bottom:18px}
.param-row{display:flex;justify-content:space-between;align-items:center;
  padding:13px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:8px}
.param-row:last-child{border-bottom:none;padding-bottom:0}
.p-lbl{font-size:13px;font-weight:500;color:var(--text)}
.p-desc{font-size:11px;color:var(--text3);margin-top:2px}
.p-badge{font-size:11px;font-weight:600;padding:4px 12px;border-radius:99px}
.p-blue{background:rgba(99,102,241,0.08);color:var(--primary);border:1px solid rgba(99,102,241,0.2)}
.p-violet{background:rgba(124,58,237,0.08);color:var(--violet);border:1px solid rgba(124,58,237,0.2)}
.p-green{background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}

/* ── Modal ── */
.mbg{display:none;position:fixed;inset:0;background:rgba(17,24,39,0.45);
  backdrop-filter:blur(4px);z-index:200;align-items:center;justify-content:center;padding:16px}
.mbg.open{display:flex;animation:fi 0.2s ease}
@keyframes fi{from{opacity:0}to{opacity:1}}
.modal{background:var(--surface);border:1px solid var(--border);border-radius:20px;
  padding:32px;width:100%;max-width:500px;max-height:90vh;overflow-y:auto;
  box-shadow:0 20px 60px rgba(0,0,0,0.12);animation:su 0.22s ease;position:relative}
@keyframes su{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:translateY(0)}}
.modal::before{content:'';position:absolute;top:0;left:20%;right:20%;height:3px;
  background:var(--grad);border-radius:0 0 4px 4px}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.mh h3{font-size:17px;font-weight:700;color:var(--text);letter-spacing:-0.3px}
.mc{width:30px;height:30px;border-radius:8px;border:1px solid var(--border);
  background:transparent;cursor:pointer;font-size:16px;color:var(--text3);
  display:flex;align-items:center;justify-content:center;font-family:'Inter',sans-serif}
.mc:hover{background:var(--surface2)}
.fg{margin-bottom:15px}
.fg label{display:block;font-size:11px;font-weight:700;color:var(--text2);
  margin-bottom:7px;text-transform:uppercase;letter-spacing:0.7px}
.fg input,.fg select{width:100%;height:42px;padding:0 13px;
  background:#FAFAFA;border:1.5px solid var(--border);
  border-radius:10px;font-size:13px;font-family:'Inter',sans-serif;
  color:var(--text);outline:none;transition:all 0.2s}
.fg input:focus,.fg select:focus{border-color:var(--primary);background:#fff;
  box-shadow:0 0 0 3px rgba(99,102,241,0.1)}
.fg2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ma{display:flex;gap:10px;margin-top:24px;padding-top:20px;border-top:1px solid var(--border)}
.ma .btn{flex:1;justify-content:center;height:42px}
.al{padding:10px 14px;border-radius:10px;font-size:12px;font-weight:500;margin-bottom:14px;display:none}
.al-e{background:#FFF1F2;border:1px solid #FECDD3;color:var(--red)}
.al-o{background:#F0FDF4;border:1px solid #BBF7D0;color:var(--green)}

/* ── Overlay mobile ── */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.4);z-index:99}
.overlay.open{display:block}

/* ══ RESPONSIVE MOBILE ══ */
@media(max-width:768px){
  .sidebar{left:calc(-1 * var(--sidebar-w));box-shadow:none}
  .sidebar.open{left:0;box-shadow:4px 0 20px rgba(0,0,0,0.15)}
  .main{margin-left:0!important}
  .menu-btn{display:inline-flex;align-items:center;justify-content:center}
  .topbar{padding:0 14px}
  .tb-page-title{font-size:15px}
  .content{padding:14px}
  .stats{grid-template-columns:1fr!important}
  .prop-positions{grid-template-columns:1fr 1fr!important}
  .h-stats{grid-template-columns:1fr 1fr!important}
  .fg2{grid-template-columns:1fr!important}
  .h-filters{flex-direction:column;align-items:stretch}
  .h-select{width:100%}
  .modal{padding:24px 18px}
}
@media(max-width:400px){
  .prop-positions{grid-template-columns:1fr!important}
  .h-stats{grid-template-columns:1fr!important}
}
</style></head><body>

<div class="overlay" id="overlay" onclick="closeMenu()"></div>

<!-- ══ SIDEBAR ══ -->
<div class="sidebar" id="sidebar">
  <div class="s-logo">
    <div class="s-logo-row">
      <div class="s-logo-icon">🛰️</div>
      <div>
        <div class="s-logo-name">GPS Tracker</div>
        <div class="s-logo-sub">Control Center</div>
      </div>
    </div>
  </div>
  <div class="s-admin">
    <div class="s-admin-row">
      <div class="s-avatar">⚙️</div>
      <div>
        <div class="s-admin-name">Administrateur</div>
        <div class="s-admin-role">Accès total</div>
      </div>
    </div>
  </div>
  <div class="s-nav">
    <div class="nav-item active" onclick="show('dashboard',this)">
      <span class="nav-ico">📊</span>Dashboard
    </div>
    <div class="nav-item" onclick="show('proprietaires',this)">
      <span class="nav-ico">👥</span>Propriétaires
    </div>
    <div class="nav-item" onclick="show('vehicules',this)">
      <span class="nav-ico">🚗</span>Véhicules
    </div>
    <div class="nav-item" onclick="show('historique',this)">
      <span class="nav-ico">📍</span>Historique GPS
    </div>
    <div class="nav-item" onclick="show('parametres',this)">
      <span class="nav-ico">⚙️</span>Paramètres
    </div>
  </div>
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()">🚪 Déconnexion</button>
  </div>
</div>

<!-- ══ MAIN ══ -->
<div class="main">
  <div class="topbar">
    <div class="tb-left">
      <button class="menu-btn" onclick="toggleMenu()">☰</button>
      <span class="tb-crumb">Admin /</span>
      <span class="tb-page-title" id="page-title">Dashboard</span>
    </div>
    <div class="tb-right">
      <div class="clock" id="clk">--:--:--</div>
    </div>
  </div>

  <div class="content">

    <!-- DASHBOARD -->
    <div class="section active" id="s-dashboard">
      <div class="stats">
        <div class="stat">
          <div class="stat-top">
            <div class="stat-icon">👥</div>
            <span class="stat-trend">Total</span>
          </div>
          <div class="stat-val" id="stp">—</div>
          <div class="stat-lbl">Propriétaires enregistrés</div>
        </div>
        <div class="stat">
          <div class="stat-top">
            <div class="stat-icon">🚗</div>
            <span class="stat-trend">Actifs</span>
          </div>
          <div class="stat-val" id="stv">—</div>
          <div class="stat-lbl">Véhicules suivis</div>
        </div>
        <div class="stat">
          <div class="stat-top">
            <div class="stat-icon">📡</div>
            <span class="stat-trend">Live</span>
          </div>
          <div class="stat-val">24/7</div>
          <div class="stat-lbl">Surveillance active</div>
        </div>
      </div>
      <div class="table-card" style="padding:28px 32px">
        <p style="font-size:14px;color:var(--text2);line-height:1.9">
          Bienvenue dans le <strong style="background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent">Centre de Contrôle GPS</strong>.<br>
          Utilisez la navigation à gauche pour gérer les propriétaires, les véhicules et consulter l'historique GPS.
        </p>
      </div>
    </div>

    <!-- PROPRIÉTAIRES -->
    <div class="section" id="s-proprietaires">
      <div class="prop-positions" id="prop-pos">
        <div class="pp-card">
          <div class="pp-icon">👥</div>
          <div class="pp-val" id="pp-total">—</div>
          <div class="pp-lbl">Total propriétaires</div>
        </div>
        <div class="pp-card">
          <div class="pp-icon">✅</div>
          <div class="pp-val" id="pp-actif">—</div>
          <div class="pp-lbl">Comptes actifs</div>
        </div>
        <div class="pp-card">
          <div class="pp-icon">🚗</div>
          <div class="pp-val" id="pp-vehs">—</div>
          <div class="pp-lbl">Véhicules associés</div>
        </div>
      </div>
      <div class="sh">
        <div>
          <h2>Propriétaires</h2>
          <div class="sh-sub">Gestion des comptes propriétaires</div>
        </div>
        <button class="btn btn-primary" onclick="openMP()">+ Nouveau propriétaire</button>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>Nom complet</th><th>Email</th><th>Téléphone</th>
              <th>Véhicules</th><th>Depuis</th><th>Statut</th><th>Action</th>
            </tr></thead>
            <tbody id="tbp">
              <tr><td colspan="7"><div class="empty"><div class="empty-ico">👥</div>
                <div class="empty-txt">Chargement...</div></div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- VÉHICULES -->
    <div class="section" id="s-vehicules">
      <div class="sh">
        <div>
          <h2>Véhicules</h2>
          <div class="sh-sub">Flotte de véhicules enregistrés</div>
        </div>
        <button class="btn btn-primary" onclick="openMV()">+ Nouveau véhicule</button>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>Immatriculation</th><th>Marque / Modèle</th><th>Type</th>
              <th>Propriétaire</th><th>Device ID</th><th>Statut</th><th>Action</th>
            </tr></thead>
            <tbody id="tbv">
              <tr><td colspan="7"><div class="empty"><div class="empty-ico">🚗</div>
                <div class="empty-txt">Chargement...</div></div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- HISTORIQUE GPS -->
    <div class="section" id="s-historique">
      <div class="sh">
        <div>
          <h2>Historique GPS</h2>
          <div class="sh-sub">Consultez l'historique des positions par véhicule</div>
        </div>
      </div>
      <div class="h-filters">
        <select class="h-select" id="hv" onchange="loadHist()">
          <option value="">Sélectionnez un véhicule...</option>
        </select>
        <select class="h-select" id="hl" onchange="loadHist()">
          <option value="50">50 positions</option>
          <option value="100">100 positions</option>
          <option value="200">200 positions</option>
        </select>
      </div>
      <div class="h-stats" id="hstats" style="display:none">
        <div class="hs"><div class="hs-val" id="hs1">0</div><div class="hs-lbl">Positions totales</div></div>
        <div class="hs"><div class="hs-val" id="hs2">0</div><div class="hs-lbl">Vitesse max km/h</div></div>
        <div class="hs"><div class="hs-val" id="hs3">0</div><div class="hs-lbl">Vitesse moy km/h</div></div>
        <div class="hs"><div class="hs-val" id="hs4">0</div><div class="hs-lbl">Satellites moy</div></div>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>#</th><th>Date / Heure</th><th>Latitude</th>
              <th>Longitude</th><th>Vitesse</th><th>Satellites</th>
            </tr></thead>
            <tbody id="tbh">
              <tr><td colspan="6"><div class="empty">
                <div class="empty-ico">📍</div>
                <div class="empty-txt">Sélectionnez un véhicule</div>
                <div class="empty-sub">pour afficher son historique</div>
              </div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- PARAMÈTRES -->
    <div class="section" id="s-parametres">
      <div class="sh">
        <div>
          <h2>Paramètres</h2>
          <div class="sh-sub">Configuration du système GPS Tracker</div>
        </div>
      </div>
      <div class="param-card">
        <div class="param-title">Compte administrateur</div>
        <div class="param-sub">Informations de votre compte</div>
        <div class="param-row">
          <div><div class="p-lbl">Email de connexion</div><div class="p-desc">admin@gps.com</div></div>
          <span class="p-badge p-violet">Administrateur</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Niveau d'accès</div><div class="p-desc">Contrôle total sur toutes les fonctionnalités</div></div>
          <span class="p-badge p-green">Actif</span>
        </div>
      </div>
      <div class="param-card">
        <div class="param-title">Système de suivi GPS</div>
        <div class="param-sub">État des services et configuration</div>
        <div class="param-row">
          <div><div class="p-lbl">API ESP32</div><div class="p-desc">Endpoint : POST /api/position</div></div>
          <span class="p-badge p-green">En ligne</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Base de données</div><div class="p-desc">SQLite — gps_data.db</div></div>
          <span class="p-badge p-green">Connectée</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Intervalle de mise à jour</div><div class="p-desc">Fréquence de rafraîchissement</div></div>
          <select class="h-select" style="width:160px">
            <option>2 secondes</option><option>5 secondes</option><option>10 secondes</option>
          </select>
        </div>
      </div>
      <div class="param-card">
        <div class="param-title">À propos</div>
        <div class="param-sub">Informations sur l'application</div>
        <div class="param-row">
          <div><div class="p-lbl">GPS Tracker</div><div class="p-desc">Version 3.0 — Ocean Blue + Violet</div></div>
          <span class="p-badge p-blue">Flask · SQLite</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Design</div><div class="p-desc">Style Stripe Premium</div></div>
          <span class="p-badge p-violet">Inter · Gradient</span>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- MODAL PROPRIÉTAIRE — CORRIGÉ : id="p-tel" au lieu de id="pt" -->
<div class="mbg" id="mp">
  <div class="modal">
    <div class="mh">
      <h3>Nouveau propriétaire</h3>
      <button class="mc" onclick="closeM('mp')">✕</button>
    </div>
    <div class="al al-e" id="ep"></div>
    <div class="al al-o" id="op"></div>
    <div class="fg2">
      <div class="fg"><label>Nom *</label><input id="pn" placeholder="Dieng"/></div>
      <div class="fg"><label>Prénom *</label><input id="pp" placeholder="Saliou"/></div>
    </div>
    <div class="fg"><label>Email *</label><input type="email" id="pe" placeholder="saliou@email.com"/></div>
    <div class="fg"><label>Téléphone *</label><input id="p-tel" placeholder="+221 77 229 22 03"/></div>
    <div class="fg"><label>Mot de passe *</label><input type="password" id="pw" placeholder="Minimum 6 caractères"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('mp')">Annuler</button>
      <button class="btn btn-primary" onclick="creerP()">Créer le compte</button>
    </div>
  </div>
</div>

<!-- MODAL VÉHICULE -->
<div class="mbg" id="mv">
  <div class="modal">
    <div class="mh">
      <h3>Nouveau véhicule</h3>
      <button class="mc" onclick="closeM('mv')">✕</button>
    </div>
    <div class="al al-e" id="ev"></div>
    <div class="al al-o" id="ov"></div>
    <div class="fg"><label>Propriétaire *</label><select id="vp"></select></div>
    <div class="fg2">
      <div class="fg"><label>Marque *</label><input id="vm" placeholder="Toyota"/></div>
      <div class="fg"><label>Modèle *</label><input id="vmo" placeholder="Corolla"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Type *</label>
        <select id="vt">
          <option value="voiture">🚗 Voiture</option>
          <option value="moto">🏍️ Moto</option>
          <option value="camion">🚛 Camion</option>
          <option value="bus">🚌 Bus</option>
          <option value="autre">🚙 Autre</option>
        </select>
      </div>
      <div class="fg"><label>Couleur</label><input id="vc" placeholder="Blanc"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Immatriculation *</label><input id="vi" placeholder="DK-1234-AB"/></div>
      <div class="fg"><label>Année</label><input type="number" id="va" placeholder="2022"/></div>
    </div>
    <div class="fg"><label>Device ID (ESP32) *</label><input id="vd" placeholder="vehicule_01"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('mv')">Annuler</button>
      <button class="btn btn-primary" onclick="creerV()">Créer le véhicule</button>
    </div>
  </div>
</div>

<script>
const T={dashboard:"Dashboard",proprietaires:"Propriétaires",vehicules:"Véhicules",
  historique:"Historique GPS",parametres:"Paramètres"};

setInterval(()=>{document.getElementById("clk").textContent=new Date().toLocaleTimeString('fr-FR')},1000);

function toggleMenu(){
  document.getElementById("sidebar").classList.toggle("open");
  document.getElementById("overlay").classList.toggle("open");
}
function closeMenu(){
  document.getElementById("sidebar").classList.remove("open");
  document.getElementById("overlay").classList.remove("open");
}

function show(n,el){
  document.querySelectorAll(".section").forEach(s=>s.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  document.getElementById("s-"+n).classList.add("active");
  el.classList.add("active");
  document.getElementById("page-title").textContent=T[n];
  closeMenu();
  if(n==="proprietaires")loadP();
  if(n==="vehicules")loadV();
  if(n==="historique")initHist();
}

async function loadStats(){
  const[p,v]=await Promise.all([
    fetch("/api/admin/proprietaires").then(r=>r.json()),
    fetch("/api/admin/vehicules").then(r=>r.json())]);
  document.getElementById("stp").textContent=p.length||0;
  document.getElementById("stv").textContent=v.filter(x=>x.actif).length||0;
}

/* ── Propriétaires ── */
async function loadP(){
  const data=await fetch("/api/admin/proprietaires").then(r=>r.json());
  const actifs=data.filter(p=>p.actif).length;
  const totalVehs=data.reduce((s,p)=>s+p.nb_vehicules,0);
  document.getElementById("pp-total").textContent=data.length;
  document.getElementById("pp-actif").textContent=actifs;
  document.getElementById("pp-vehs").textContent=totalVehs;
  const tb=document.getElementById("tbp");
  if(!data.length){
    tb.innerHTML='<tr><td colspan="7"><div class="empty"><div class="empty-ico">👥</div><div class="empty-txt">Aucun propriétaire enregistré</div><div class="empty-sub">Créez votre premier propriétaire</div></div></td></tr>';
    return;
  }
  tb.innerHTML=data.map(p=>`<tr>
    <td class="td-main">${p.prenom} ${p.nom}</td>
    <td>${p.email}</td>
    <td>${p.telephone||"—"}</td>
    <td><span style="font-weight:700;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent">${p.nb_vehicules}</span></td>
    <td style="font-size:12px;color:var(--text3)">${(p.date_creation||"").slice(0,10)}</td>
    <td><span class="badge ${p.actif?'badge-on':'badge-off'}">${p.actif?'Actif':'Inactif'}</span></td>
    <td><button class="btn btn-sm ${p.actif?'btn-danger':'btn-success'}" onclick="toggleP(${p.id})">${p.actif?'Désactiver':'Activer'}</button>
    <button class="btn btn-sm" onclick="ouvrirModifP(${p.id})" style="background:rgba(99,102,241,0.08);color:var(--primary);border:1px solid rgba(99,102,241,0.2);margin-left:4px">✏️ Modifier</button></td>
  </tr>`).join("");
}

async function creerP(){
  const e=document.getElementById("ep"),o=document.getElementById("op");
  e.style.display=o.style.display="none";
  /* CORRIGÉ : id="p-tel" au lieu de "pt" */
  const body={
    nom:document.getElementById("pn").value.trim(),
    prenom:document.getElementById("pp").value.trim(),
    email:document.getElementById("pe").value.trim(),
    telephone:document.getElementById("p-tel").value.trim(),
    mot_de_passe:document.getElementById("pw").value
  };
  if(!body.nom||!body.prenom||!body.email||!body.telephone||!body.mot_de_passe){
    e.textContent="Tous les champs sont obligatoires.";e.style.display="block";return;}
  const res=await fetch("/api/admin/proprietaires",{method:"POST",
    headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){
    o.textContent="✓ Propriétaire créé avec succès !";o.style.display="block";
    /* CORRIGÉ : "p-tel" dans le reset */
    ["pn","pp","pe","p-tel","pw"].forEach(id=>document.getElementById(id).value="");
    loadStats();
  }else{e.textContent=data.error;e.style.display="block";}
}

async function toggleP(id){await fetch(`/api/admin/proprietaires/${id}/toggle`,{method:"POST"});loadP();}

/* ── Véhicules ── */
async function loadV(){
  const data=await fetch("/api/admin/vehicules").then(r=>r.json());
  const tb=document.getElementById("tbv");
  if(!data.length){tb.innerHTML='<tr><td colspan="7"><div class="empty"><div class="empty-ico">🚗</div><div class="empty-txt">Aucun véhicule enregistré</div></div></td></tr>';return;}
  tb.innerHTML=data.map(v=>`<tr>
    <td class="td-main">${v.immatriculation}</td>
    <td>${v.marque} ${v.modele}</td>
    <td>${v.type_vehicule}</td>
    <td>${v.proprietaire_nom}</td>
    <td><span class="device">${v.device_id}</span></td>
    <td><span class="badge ${v.actif?'badge-on':'badge-off'}">${v.actif?'Actif':'Inactif'}</span></td>
    <td><button class="btn btn-sm ${v.actif?'btn-danger':'btn-success'}" onclick="toggleV(${v.id})">${v.actif?'Désactiver':'Activer'}</button>
    <button class="btn btn-sm" onclick="ouvrirModifV(${v.id})" style="background:rgba(99,102,241,0.08);color:var(--primary);border:1px solid rgba(99,102,241,0.2);margin-left:4px">✏️ Modifier</button></td>
  </tr>`).join("");
}

async function openMV(){
  const data=await fetch("/api/admin/proprietaires").then(r=>r.json());
  document.getElementById("vp").innerHTML=data.map(p=>`<option value="${p.id}">${p.prenom} ${p.nom}</option>`).join("");
  document.getElementById("mv").classList.add("open");
}

async function creerV(){
  const e=document.getElementById("ev"),o=document.getElementById("ov");
  e.style.display=o.style.display="none";
  const body={
    proprietaire_id:parseInt(document.getElementById("vp").value),
    marque:document.getElementById("vm").value.trim(),
    modele:document.getElementById("vmo").value.trim(),
    immatriculation:document.getElementById("vi").value.trim(),
    type_vehicule:document.getElementById("vt").value,
    couleur:document.getElementById("vc").value.trim(),
    annee:parseInt(document.getElementById("va").value)||2024,
    device_id:document.getElementById("vd").value.trim()
  };
  const res=await fetch("/api/admin/vehicules",{method:"POST",
    headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){o.textContent="✓ Véhicule créé avec succès !";o.style.display="block";loadStats();}
  else{e.textContent=data.error;e.style.display="block";}
}

async function toggleV(id){await fetch(`/api/admin/vehicules/${id}/toggle`,{method:"POST"});loadV();}

/* ── Historique ── */
async function initHist(){
  const vehs=await fetch("/api/admin/vehicules").then(r=>r.json());
  const sel=document.getElementById("hv");
  const cur=sel.value;
  sel.innerHTML='<option value="">Sélectionnez un véhicule...</option>'+
    vehs.filter(v=>v.actif).map(v=>`<option value="${v.id}">${v.immatriculation} — ${v.marque} ${v.modele}</option>`).join("");
  if(cur)sel.value=cur;
}

async function loadHist(){
  const vid=document.getElementById("hv").value;
  const lim=document.getElementById("hl").value;
  if(!vid)return;
  const data=await fetch(`/api/positions/${vid}?limit=${lim}`).then(r=>r.json());
  const hs=document.getElementById("hstats");
  const tb=document.getElementById("tbh");
  if(!data.length){
    hs.style.display="none";
    tb.innerHTML='<tr><td colspan="6"><div class="empty"><div class="empty-ico">📍</div><div class="empty-txt">Aucune position enregistrée</div></div></td></tr>';
    return;
  }
  hs.style.display="grid";
  const vmax=Math.max(...data.map(p=>p.vitesse||0));
  const vmoy=data.reduce((s,p)=>s+(p.vitesse||0),0)/data.length;
  const smoy=data.reduce((s,p)=>s+(p.satellites||0),0)/data.length;
  document.getElementById("hs1").textContent=data.length;
  document.getElementById("hs2").textContent=vmax.toFixed(1);
  document.getElementById("hs3").textContent=vmoy.toFixed(1);
  document.getElementById("hs4").textContent=smoy.toFixed(1);
  const rev=[...data].reverse();
  tb.innerHTML=rev.map((p,i)=>`<tr>
    <td style="color:var(--text3);font-size:12px">#${data.length-i}</td>
    <td style="font-size:12px;color:var(--text2)">${p.created_at||p.timestamp||"—"}</td>
    <td style="font-family:monospace;font-size:12px;font-weight:600;
      background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent">${(p.latitude||0).toFixed(6)}</td>
    <td style="font-family:monospace;font-size:12px;font-weight:600;
      background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent">${(p.longitude||0).toFixed(6)}</td>
    <td><span style="font-weight:700;color:${(p.vitesse||0)>80?'var(--red)':'var(--text)'}">${(p.vitesse||0).toFixed(1)} km/h</span></td>
    <td>${p.satellites||"—"}</td>
  </tr>`).join("");
}

function openMP(){
  document.getElementById("ep").style.display=document.getElementById("op").style.display="none";
  document.getElementById("mp").classList.add("open");
}
function closeM(id){document.getElementById(id).classList.remove("open");}

/* ── Modification Propriétaire ── */
async function ouvrirModifP(id){
  const data=await fetch(`/api/admin/proprietaires/${id}`).then(r=>r.json());
  document.getElementById("mp-id").value=id;
  document.getElementById("mp-nom").value=data.nom||"";
  document.getElementById("mp-prenom").value=data.prenom||"";
  document.getElementById("mp-email").value=data.email||"";
  document.getElementById("mp-tel").value=data.telephone||"";
  document.getElementById("mp-pw").value="";
  document.getElementById("emp").style.display=document.getElementById("omp").style.display="none";
  document.getElementById("m-modif-p").classList.add("open");
}
async function sauvegarderP(){
  const id=document.getElementById("mp-id").value;
  const e=document.getElementById("emp"),o=document.getElementById("omp");
  e.style.display=o.style.display="none";
  const body={
    nom:document.getElementById("mp-nom").value.trim(),
    prenom:document.getElementById("mp-prenom").value.trim(),
    email:document.getElementById("mp-email").value.trim(),
    telephone:document.getElementById("mp-tel").value.trim(),
    mot_de_passe:document.getElementById("mp-pw").value||undefined
  };
  if(!body.mot_de_passe)delete body.mot_de_passe;
  const res=await fetch(`/api/admin/proprietaires/${id}`,{method:"PUT",
    headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){o.textContent="✓ Propriétaire modifié !";o.style.display="block";
    setTimeout(()=>closeM("m-modif-p"),1200);loadP();}
  else{e.textContent=data.error;e.style.display="block";}
}

/* ── Modification Véhicule ── */
async function ouvrirModifV(id){
  const data=await fetch(`/api/admin/vehicules/${id}`).then(r=>r.json());
  document.getElementById("mv-id").value=id;
  document.getElementById("mv-marque").value=data.marque||"";
  document.getElementById("mv-modele").value=data.modele||"";
  document.getElementById("mv-immat").value=data.immatriculation||"";
  document.getElementById("mv-type").value=data.type_vehicule||"voiture";
  document.getElementById("mv-couleur").value=data.couleur||"";
  document.getElementById("mv-annee").value=data.annee||"";
  document.getElementById("mv-device").value=data.device_id||"";
  document.getElementById("emv").style.display=document.getElementById("omv").style.display="none";
  document.getElementById("m-modif-v").classList.add("open");
}
async function sauvegarderV(){
  const id=document.getElementById("mv-id").value;
  const e=document.getElementById("emv"),o=document.getElementById("omv");
  e.style.display=o.style.display="none";
  const body={
    marque:document.getElementById("mv-marque").value.trim(),
    modele:document.getElementById("mv-modele").value.trim(),
    immatriculation:document.getElementById("mv-immat").value.trim(),
    type_vehicule:document.getElementById("mv-type").value,
    couleur:document.getElementById("mv-couleur").value.trim(),
    annee:document.getElementById("mv-annee").value,
    device_id:document.getElementById("mv-device").value.trim()
  };
  const res=await fetch(`/api/admin/vehicules/${id}`,{method:"PUT",
    headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){o.textContent="✓ Véhicule modifié !";o.style.display="block";
    setTimeout(()=>closeM("m-modif-v"),1200);loadV();}
  else{e.textContent=data.error;e.style.display="block";}
}

async function doLogout(){await fetch("/api/logout",{method:"POST"});window.location.href="/";}
loadStats();
</script>

<!-- MODAL MODIFICATION PROPRIÉTAIRE -->
<div class="mbg" id="m-modif-p">
  <div class="modal">
    <div class="mh">
      <h3>✏️ Modifier le propriétaire</h3>
      <button class="mc" onclick="closeM('m-modif-p')">✕</button>
    </div>
    <input type="hidden" id="mp-id"/>
    <div class="al al-e" id="emp"></div>
    <div class="al al-o" id="omp"></div>
    <div class="fg2">
      <div class="fg"><label>Nom *</label><input id="mp-nom"/></div>
      <div class="fg"><label>Prénom *</label><input id="mp-prenom"/></div>
    </div>
    <div class="fg"><label>Email *</label><input type="email" id="mp-email"/></div>
    <div class="fg"><label>Téléphone *</label><input id="mp-tel"/></div>
    <div class="fg"><label>Nouveau mot de passe <span style="color:var(--text3);font-weight:400">(laisser vide = inchangé)</span></label>
      <input type="password" id="mp-pw" placeholder="Laisser vide pour ne pas changer"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('m-modif-p')">Annuler</button>
      <button class="btn btn-primary" onclick="sauvegarderP()">💾 Sauvegarder</button>
    </div>
  </div>
</div>

<!-- MODAL MODIFICATION VÉHICULE -->
<div class="mbg" id="m-modif-v">
  <div class="modal">
    <div class="mh">
      <h3>✏️ Modifier le véhicule</h3>
      <button class="mc" onclick="closeM('m-modif-v')">✕</button>
    </div>
    <input type="hidden" id="mv-id"/>
    <div class="al al-e" id="emv"></div>
    <div class="al al-o" id="omv"></div>
    <div class="fg2">
      <div class="fg"><label>Marque *</label><input id="mv-marque"/></div>
      <div class="fg"><label>Modèle *</label><input id="mv-modele"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Type *</label>
        <select id="mv-type">
          <option value="voiture">🚗 Voiture</option>
          <option value="moto">🏍️ Moto</option>
          <option value="camion">🚛 Camion</option>
          <option value="bus">🚌 Bus</option>
          <option value="autre">🚙 Autre</option>
        </select>
      </div>
      <div class="fg"><label>Couleur</label><input id="mv-couleur"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Immatriculation *</label><input id="mv-immat"/></div>
      <div class="fg"><label>Année</label><input type="number" id="mv-annee"/></div>
    </div>
    <div class="fg"><label>Device ID (ESP32) *</label><input id="mv-device"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('m-modif-v')">Annuler</button>
      <button class="btn btn-primary" onclick="sauvegarderV()">💾 Sauvegarder</button>
    </div>
  </div>
</div>
</body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE USER — CORRIGÉE (responsive mobile)
# ═════════════════════════════════════════════════════════════

USER_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Mon suivi</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
:root{
  --bg:#F8F7FF;--surface:#FFFFFF;--surface2:#F9FAFB;--border:#E5E7EB;
  --primary:#6366F1;--violet:#7C3AED;--cyan:#06B6D4;
  --grad:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
  --grad2:linear-gradient(135deg,#6366F1,#06B6D4);
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-bd:rgba(16,185,129,0.2);
  --red:#F43F5E;--red-bg:rgba(244,63,94,0.08);--red-bd:rgba(244,63,94,0.2);
  --text:#111827;--text2:#6B7280;--text3:#9CA3AF;
  --sidebar-w:240px;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);
  height:100vh;display:flex;overflow:hidden;font-size:14px}

/* SIDEBAR */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:var(--surface);border-right:1px solid var(--border);
  display:flex;flex-direction:column;z-index:100;
  transition:left 0.25s ease;overflow-y:auto
}
.sidebar::before{content:'';position:absolute;top:0;left:0;right:0;height:160px;
  background:linear-gradient(180deg,rgba(124,58,237,0.05),transparent);pointer-events:none}
.s-logo{padding:20px;border-bottom:1px solid var(--border);position:relative}
.s-logo-row{display:flex;align-items:center;gap:10px}
.s-logo-icon{width:36px;height:36px;border-radius:10px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;
  box-shadow:0 3px 10px rgba(99,102,241,0.3)}
.s-logo-name{font-size:14px;font-weight:700;color:var(--text)}
.s-logo-sub{font-size:10px;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:600}
.s-user{margin:12px;padding:11px 13px;
  background:linear-gradient(135deg,rgba(124,58,237,0.06),rgba(99,102,241,0.04));
  border:1px solid rgba(124,58,237,0.14);border-radius:12px}
.s-user-name{font-size:13px;font-weight:600;color:var(--text)}
.s-user-role{font-size:10px;font-weight:600;margin-top:2px;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.s-section{padding:14px 20px 5px;font-size:10px;font-weight:700;
  color:var(--text3);text-transform:uppercase;letter-spacing:1.5px}
.nav-item{display:flex;align-items:center;gap:10px;padding:9px 14px;
  margin:2px 8px;border-radius:10px;cursor:pointer;color:var(--text2);
  font-size:13px;font-weight:500;transition:all 0.15s;border-left:3px solid transparent}
.nav-item:hover{background:rgba(99,102,241,0.06);color:var(--primary)}
.nav-item.active{background:linear-gradient(135deg,rgba(124,58,237,0.08),rgba(99,102,241,0.06));
  color:var(--primary);font-weight:600;border-left-color:var(--violet)}
.nav-ico{font-size:15px;width:20px;text-align:center;flex-shrink:0}
.s-section2{padding:10px 20px 5px;font-size:10px;font-weight:700;
  color:var(--text3);text-transform:uppercase;letter-spacing:1.5px}
.veh-list{flex:1;overflow-y:auto;padding:4px 8px}
.veh-card{padding:11px 13px;border-radius:10px;cursor:pointer;
  border:1px solid transparent;margin-bottom:4px;transition:all 0.15s}
.veh-card:hover{background:var(--surface2);border-color:var(--border)}
.veh-card.sel{background:linear-gradient(135deg,rgba(124,58,237,0.07),rgba(99,102,241,0.05));
  border-color:rgba(99,102,241,0.2)}
.veh-immat{font-size:13px;font-weight:700;color:var(--text)}
.veh-info{font-size:11px;color:var(--text3);margin-top:2px}
.veh-live{display:flex;align-items:center;gap:5px;margin-top:5px}
.dot{width:6px;height:6px;border-radius:50%;background:var(--text3);transition:all 0.3s;flex-shrink:0}
@keyframes blink{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.6;transform:scale(0.8)}}
.dot.live{background:var(--green);animation:blink 1.5s infinite}
.dot-lbl{font-size:10px;color:var(--text3);font-weight:500}
.s-bottom{padding:12px;border-top:1px solid var(--border);background:var(--surface);flex-shrink:0}
.btn-logout{width:100%;padding:10px;background:var(--red-bg);color:var(--red);
  border:1px solid var(--red-bd);border-radius:10px;cursor:pointer;
  font-size:13px;font-weight:600;font-family:'Inter',sans-serif;
  display:flex;align-items:center;justify-content:center;gap:7px;transition:all 0.15s}
.btn-logout:hover{background:rgba(244,63,94,0.14)}

/* MAIN */
.main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}
.topbar{height:56px;padding:0 20px;background:rgba(255,255,255,0.92);
  backdrop-filter:blur(12px);border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;flex-shrink:0}
.menu-btn{display:none;background:none;border:none;cursor:pointer;
  font-size:22px;color:var(--text);padding:4px 8px;margin-right:4px}
.tb-title{font-size:15px;font-weight:700;color:var(--text);letter-spacing:-0.2px}
.live-pill{display:flex;align-items:center;gap:6px;padding:5px 13px;
  background:var(--green-bg);border:1px solid var(--green-bd);
  border-radius:99px;font-size:11px;color:var(--green);font-weight:600}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.4}}
.live-blink{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.5s infinite}
.upd{font-size:11px;color:var(--text3);margin-left:8px}

.infobar{height:52px;padding:0 20px;background:var(--surface2);
  border-bottom:1px solid var(--border);display:flex;align-items:center;flex-shrink:0}
.isep{width:1px;height:24px;background:var(--border);margin:0 16px}
.iitem{display:flex;flex-direction:column}
.ilbl{font-size:9px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:1px}
.ival{font-size:14px;font-weight:700;color:var(--text);margin-top:1px}
.ival.grad{background:var(--grad2);-webkit-background-clip:text;-webkit-text-fill-color:transparent}

#map{flex:1}
.empty-state{flex:1;display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:12px}
.es-ico{font-size:60px;opacity:0.15}
.es-title{font-size:16px;font-weight:600;color:var(--text2)}
.es-sub{font-size:13px;color:var(--text3);text-align:center;padding:0 20px}

.usec{display:none;flex:1;overflow-y:auto;padding:24px}
.usec.active{display:block}

/* Historique user */
.h-filters{display:flex;gap:10px;margin-bottom:18px;flex-wrap:wrap}
.h-select{height:38px;padding:0 13px;background:var(--surface);border:1px solid var(--border);
  border-radius:10px;font-size:13px;font-family:'Inter',sans-serif;color:var(--text);outline:none}
.h-select:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(99,102,241,0.1)}
.htable{background:var(--surface);border:1px solid var(--border);border-radius:14px;overflow:hidden}
.htable-wrap{overflow-x:auto}
.htable table{width:100%;border-collapse:collapse;min-width:480px}
.htable th{padding:10px 14px;font-size:11px;font-weight:700;color:var(--text3);
  text-transform:uppercase;letter-spacing:0.8px;background:var(--surface2);
  border-bottom:1px solid var(--border)}
.htable td{padding:11px 14px;font-size:12px;color:var(--text2);border-bottom:1px solid var(--border)}
.htable tr:last-child td{border-bottom:none}
.htable tr:hover td{background:rgba(99,102,241,0.02)}

/* Paramètres user */
.pcard{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:22px;margin-bottom:14px}
.ptitle{font-size:14px;font-weight:700;color:var(--text);margin-bottom:3px}
.psub{font-size:12px;color:var(--text3);margin-bottom:18px}
.prow{display:flex;justify-content:space-between;align-items:center;
  padding:12px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:8px}
.prow:last-child{border-bottom:none;padding-bottom:0}
.plbl{font-size:13px;font-weight:500;color:var(--text)}
.pdesc{font-size:11px;color:var(--text3);margin-top:2px}
.pbadge{font-size:11px;font-weight:600;padding:4px 12px;border-radius:99px;
  background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}

/* Overlay mobile */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.4);z-index:99}
.overlay.open{display:block}

/* ══ RESPONSIVE MOBILE ══ */
@media(max-width:768px){
  body{overflow:auto;height:auto;display:block}
  .sidebar{left:calc(-1 * var(--sidebar-w));box-shadow:none;bottom:0;height:100vh}
  .sidebar.open{left:0;box-shadow:4px 0 20px rgba(0,0,0,0.15)}
  .main{margin-left:0!important;height:100vh;display:flex;flex-direction:column}
  .menu-btn{display:inline-flex;align-items:center;justify-content:center}
  .topbar{padding:0 12px;flex-shrink:0}
  .tb-title{font-size:13px}
  .upd{display:none}

  /* Carte : hauteur fixe, pas 100% */
  #tab-carte{height:calc(100vh - 56px);flex-direction:column;overflow:hidden}
  #map-wrap{flex:1;min-height:0;overflow:hidden}
  #map{height:100%!important}

  .infobar{height:auto!important;padding:6px 12px;flex-wrap:wrap;gap:6px;flex-shrink:0}
  .isep{display:none}
  .iitem{flex-direction:row;align-items:center;gap:5px}
  .ilbl{font-size:9px}
  .ival{font-size:12px}

  .usec{padding:14px;height:calc(100vh - 56px);overflow-y:auto}
  .h-filters{flex-direction:column}
  .h-select{width:100%}
}
</style></head><body>

<div class="overlay" id="overlay" onclick="closeMenu()"></div>

<div class="sidebar" id="sidebar">
  <div class="s-logo">
    <div class="s-logo-row">
      <div class="s-logo-icon">🛰️</div>
      <div><div class="s-logo-name">GPS Tracker</div><div class="s-logo-sub">Suivi en direct</div></div>
    </div>
  </div>
  <div class="s-user">
    <div class="s-user-name" id="uname">—</div>
    <div class="s-user-role">Propriétaire</div>
  </div>
  <div class="s-section">Navigation</div>
  <div class="nav-item active" onclick="showTab('carte',this)">
    <span class="nav-ico">🗺️</span>Carte GPS
  </div>
  <div class="nav-item" onclick="showTab('historique',this)">
    <span class="nav-ico">📍</span>Historique
  </div>
  <div class="nav-item" onclick="showTab('parametres',this)">
    <span class="nav-ico">⚙️</span>Paramètres
  </div>
  <div class="s-section2">Mes véhicules</div>
  <div class="veh-list" id="veh-list">
    <div style="padding:14px;color:var(--text3);font-size:12px">Chargement...</div>
  </div>
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()">🚪 Déconnexion</button>
  </div>
</div>

<div class="main">
  <div class="topbar">
    <div style="display:flex;align-items:center;gap:4px">
      <button class="menu-btn" onclick="toggleMenu()">☰</button>
      <div class="tb-title" id="ttl">Sélectionnez un véhicule</div>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <div class="live-pill"><div class="live-blink"></div>Temps réel</div>
      <span class="upd" id="tupd">—</span>
    </div>
  </div>

  <!-- CARTE -->
  <div id="tab-carte" style="flex:1;display:flex;flex-direction:column;overflow:hidden">
    <div class="infobar" id="infobar" style="display:none">
      <div class="iitem">
        <span class="ilbl">Latitude</span>
        <span class="ival grad" id="ilat">—</span>
      </div>
      <div class="isep"></div>
      <div class="iitem">
        <span class="ilbl">Longitude</span>
        <span class="ival grad" id="ilng">—</span>
      </div>
      <div class="isep"></div>
      <div class="iitem">
        <span class="ilbl">Vitesse</span>
        <span class="ival" id="ispd">—</span>
      </div>
      <div class="isep"></div>
      <div class="iitem">
        <span class="ilbl">Satellites</span>
        <span class="ival" id="isat">—</span>
      </div>
    </div>
    <div id="map-wrap" style="flex:1;display:none"><div id="map" style="height:100%"></div></div>
    <div class="empty-state" id="empty">
      <div class="es-ico">🗺️</div>
      <div class="es-title">Aucun véhicule sélectionné</div>
      <div class="es-sub">Appuyez sur ☰ puis choisissez un véhicule pour démarrer le suivi</div>
    </div>
  </div>

  <!-- HISTORIQUE -->
  <div id="tab-historique" class="usec">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">
      <h2 style="font-size:16px;font-weight:700;color:var(--text)">Historique GPS</h2>
    </div>
    <div class="h-filters">
      <select class="h-select" id="uhv" onchange="loadUH()">
        <option value="">Sélectionnez un véhicule...</option>
      </select>
      <select class="h-select" id="uhl" onchange="loadUH()">
        <option value="50">50 positions</option>
        <option value="100">100 positions</option>
        <option value="200">200 positions</option>
      </select>
    </div>
    <div class="htable">
      <div class="htable-wrap">
        <table>
          <thead><tr>
            <th>#</th><th>Date / Heure</th><th>Latitude</th>
            <th>Longitude</th><th>Vitesse</th><th>Satellites</th>
          </tr></thead>
          <tbody id="uhtb">
            <tr><td colspan="6" style="text-align:center;padding:40px;color:var(--text3)">
              Sélectionnez un véhicule pour afficher l'historique
            </td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- PARAMÈTRES -->
  <div id="tab-parametres" class="usec">
    <h2 style="font-size:16px;font-weight:700;color:var(--text);margin-bottom:18px">Paramètres</h2>
    <div class="pcard">
      <div class="ptitle">Mon compte</div>
      <div class="psub">Informations de votre compte propriétaire</div>
      <div class="prow"><div><div class="plbl">Nom complet</div><div class="pdesc" id="pcn">—</div></div><span class="pbadge">Actif</span></div>
      <div class="prow"><div><div class="plbl">Email</div><div class="pdesc" id="pce">—</div></div></div>
      <div class="prow"><div><div class="plbl">Téléphone</div><div class="pdesc" id="pct">—</div></div></div>
      <div class="prow"><div><div class="plbl">Membre depuis</div><div class="pdesc" id="pcd">—</div></div></div>
    </div>
    <div class="pcard">
      <div class="ptitle">Mes véhicules</div>
      <div class="psub">Véhicules associés à votre compte</div>
      <div id="pcv">Chargement...</div>
    </div>
    <div class="pcard">
      <div class="ptitle">Notifications</div>
      <div class="psub">Alertes en temps réel sur votre téléphone</div>
      <div id="notif-wrap">
        <div style="font-size:12px;color:var(--text3)">Chargement...</div>
      </div>
    </div>
    <div class="pcard">
      <div class="ptitle">Système</div>
      <div class="psub">Informations sur l'application</div>
      <div class="prow">
        <div><div class="plbl">GPS Tracker v3.0</div><div class="pdesc">Ocean Blue + Violet · Style Stripe</div></div>
        <span class="pbadge">Flask · SQLite</span>
      </div>
    </div>
  </div>
</div>

<script>
let map=null,marker=null,poly=null,selId=null,interval=null,meD=null,vehD=[];

function toggleMenu(){
  document.getElementById("sidebar").classList.toggle("open");
  document.getElementById("overlay").classList.toggle("open");
}
function closeMenu(){
  document.getElementById("sidebar").classList.remove("open");
  document.getElementById("overlay").classList.remove("open");
}

function showTab(n,el){
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  if(el)el.classList.add("active");
  document.getElementById("tab-carte").style.display=n==="carte"?"flex":"none";
  document.querySelectorAll(".usec").forEach(s=>s.classList.remove("active"));
  if(n!=="carte")document.getElementById("tab-"+n).classList.add("active");
  if(n==="historique")initUH();
  if(n==="parametres")loadParams();
  closeMenu();
}

function initMap(){
  if(map)return;
  map=L.map("map").setView([14.6928,-17.4467],13);
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",{attribution:"© OpenStreetMap"}).addTo(map);
  poly=L.polyline([],{color:"#6366F1",weight:3,opacity:0.75}).addTo(map);
}

async function loadVehicules(){
  const[vehs,m]=await Promise.all([
    fetch("/api/user/vehicules").then(r=>r.json()),
    fetch("/api/me").then(r=>r.json())]);
  meD=m; vehD=vehs;
  document.getElementById("uname").textContent=m.prenom+" "+m.nom;
  const list=document.getElementById("veh-list");
  if(!vehs.length){
    list.innerHTML='<div style="padding:14px;color:var(--text3);font-size:12px">Aucun véhicule associé</div>';
    return;
  }
  list.innerHTML=vehs.map(v=>`
    <div class="veh-card" id="vc${v.id}" onclick="selV(${v.id},'${v.marque} ${v.modele}','${v.immatriculation}')">
      <div class="veh-immat">${v.immatriculation}</div>
      <div class="veh-info">${v.marque} ${v.modele} · ${v.type_vehicule}</div>
      <div class="veh-info">${v.couleur||""} ${v.annee||""}</div>
      <div class="veh-live">
        <div class="dot" id="dot${v.id}"></div>
        <span class="dot-lbl" id="dlbl${v.id}">En attente</span>
      </div>
    </div>`).join("");
}

async function selV(id,label,immat){
  document.querySelectorAll(".veh-card").forEach(c=>c.classList.remove("sel"));
  document.getElementById("vc"+id).classList.add("sel");
  selId=id;
  document.getElementById("ttl").textContent=immat+" — "+label;
  document.getElementById("empty").style.display="none";
  document.getElementById("infobar").style.display="flex";
  document.getElementById("map-wrap").style.display="block";
  /* Ferme le menu sur mobile après sélection */
  closeMenu();
  /* Bascule vers l'onglet carte */
  document.getElementById("tab-carte").style.display="flex";
  document.querySelectorAll(".usec").forEach(s=>s.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  document.querySelector(".nav-item:first-of-type")&&document.querySelectorAll(".nav-item")[0].classList.add("active");
  initMap();
  if(poly)poly.setLatLngs([]);
  if(marker){map.removeLayer(marker);marker=null;}
  setTimeout(()=>map.invalidateSize(),150);
  setTimeout(()=>map.invalidateSize(),400);
  const hist=await fetch(`/api/positions/${id}?limit=200`).then(r=>r.json());
  if(hist.length)poly.setLatLngs(hist.map(p=>[p.latitude,p.longitude]));
  if(interval)clearInterval(interval);
  refresh(); interval=setInterval(refresh,2000);
}

async function refresh(){
  if(!selId)return;
  try{
    const res=await fetch(`/api/positions/${selId}/last`);
    if(!res.ok)return;
    const p=await res.json();
    const ll=[p.latitude,p.longitude];
    const icon=L.divIcon({
      html:`<div style="width:14px;height:14px;
        background:linear-gradient(135deg,#7C3AED,#6366F1);
        border:3px solid #fff;border-radius:50%;
        box-shadow:0 2px 10px rgba(99,102,241,0.5)"></div>`,
      iconSize:[14,14],iconAnchor:[7,7]});
    if(!marker){marker=L.marker(ll,{icon}).addTo(map);map.setView(ll,15);}
    else marker.setLatLng(ll);
    poly.addLatLng(ll);
    document.getElementById("ilat").textContent=p.latitude.toFixed(6)+"°";
    document.getElementById("ilng").textContent=p.longitude.toFixed(6)+"°";
    document.getElementById("ispd").textContent=(p.vitesse||0).toFixed(1)+" km/h";
    document.getElementById("isat").textContent=p.satellites||"—";
    document.getElementById("tupd").textContent="Mis à jour "+new Date().toLocaleTimeString();
    const dot=document.getElementById("dot"+selId);
    const lbl=document.getElementById("dlbl"+selId);
    if(dot)dot.className="dot live";
    if(lbl)lbl.textContent="En direct";
  }catch(e){}
}

function initUH(){
  const sel=document.getElementById("uhv");
  sel.innerHTML='<option value="">Sélectionnez un véhicule...</option>'+
    vehD.map(v=>`<option value="${v.id}">${v.immatriculation} — ${v.marque} ${v.modele}</option>`).join("");
}

async function loadUH(){
  const vid=document.getElementById("uhv").value;
  const lim=document.getElementById("uhl").value;
  if(!vid)return;
  const data=await fetch(`/api/positions/${vid}?limit=${lim}`).then(r=>r.json());
  const tb=document.getElementById("uhtb");
  if(!data.length){
    tb.innerHTML='<tr><td colspan="6" style="text-align:center;padding:40px;color:var(--text3)">Aucune position enregistrée</td></tr>';
    return;
  }
  const rev=[...data].reverse();
  tb.innerHTML=rev.map((p,i)=>`<tr>
    <td style="color:var(--text3)">#${data.length-i}</td>
    <td>${p.created_at||"—"}</td>
    <td style="font-family:monospace;font-weight:600;font-size:12px;
      background:var(--grad2);-webkit-background-clip:text;-webkit-text-fill-color:transparent">${(p.latitude||0).toFixed(6)}</td>
    <td style="font-family:monospace;font-weight:600;font-size:12px;
      background:var(--grad2);-webkit-background-clip:text;-webkit-text-fill-color:transparent">${(p.longitude||0).toFixed(6)}</td>
    <td style="font-weight:600">${(p.vitesse||0).toFixed(1)} km/h</td>
    <td>${p.satellites||"—"}</td>
  </tr>`).join("");
}

async function loadParams(){
  if(!meD)return;
  document.getElementById("pcn").textContent=meD.prenom+" "+meD.nom;
  document.getElementById("pce").textContent=meD.email;
  document.getElementById("pct").textContent=meD.telephone||"—";
  document.getElementById("pcd").textContent=(meD.date_creation||"").slice(0,10);
  document.getElementById("pcv").innerHTML=vehD.length
    ?vehD.map(v=>`<div style="display:flex;justify-content:space-between;align-items:center;
        padding:10px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:8px">
        <div>
          <div style="font-size:13px;font-weight:600;color:var(--text)">${v.immatriculation}</div>
          <div style="font-size:11px;color:var(--text3)">${v.marque} ${v.modele} · ${v.type_vehicule}</div>
        </div>
        <span class="pbadge">Actif</span>
      </div>`).join("")
    :'<div style="color:var(--text3);font-size:13px">Aucun véhicule associé</div>';
  // Affiche le statut des notifications
  await refreshNotifStatus();
}

/* ── PUSH NOTIFICATIONS ── */
function urlBase64ToUint8Array(base64String){
  const padding='='.repeat((4-base64String.length%4)%4);
  const base64=(base64String+padding).replace(/-/g,'+').replace(/_/g,'/');
  const raw=window.atob(base64);
  const arr=new Uint8Array(raw.length);
  for(let i=0;i<raw.length;i++)arr[i]=raw.charCodeAt(i);
  return arr;
}

async function refreshNotifStatus(){
  const wrap=document.getElementById("notif-wrap");
  if(!wrap)return;
  if(!("Notification" in window)||!("serviceWorker" in navigator)){
    wrap.innerHTML='<div style="font-size:12px;color:var(--text3)">Notifications non supportées par ce navigateur.</div>';
    return;
  }
  const res=await fetch("/api/push/status").then(r=>r.json());
  const abonne=res.subscribed;
  wrap.innerHTML=`
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
      <div>
        <div style="font-size:13px;font-weight:600;color:var(--text)">Notifications push</div>
        <div style="font-size:11px;color:var(--text3);margin-top:3px">
          Alertes si un véhicule perd le réseau depuis 5 min
        </div>
      </div>
      <button onclick="${abonne?'desactiverNotifs':'activerNotifs'}()"
        style="padding:8px 18px;border-radius:10px;border:none;cursor:pointer;
          font-size:13px;font-weight:600;font-family:Inter,sans-serif;
          background:${abonne?'rgba(244,63,94,0.08)':'linear-gradient(135deg,#7C3AED,#6366F1)'};
          color:${abonne?'#F43F5E':'#fff'};
          border:${abonne?'1px solid rgba(244,63,94,0.2)':'none'}">
        ${abonne?'🔕 Désactiver':'🔔 Activer'}
      </button>
    </div>
    <div id="notif-msg" style="margin-top:10px;font-size:12px;color:var(--text3)">
      Statut : ${abonne?'<span style="color:#10B981;font-weight:600">✅ Activées</span>':'<span style="color:#9CA3AF">❌ Désactivées</span>'}
    </div>`;
}

async function activerNotifs(){
  const msg=document.getElementById("notif-msg");
  try{
    // Demande permission
    const perm=await Notification.requestPermission();
    if(perm!=="granted"){
      if(msg)msg.innerHTML='<span style="color:#F43F5E">Permission refusée. Autorisez les notifications dans les paramètres du navigateur.</span>';
      return;
    }
    // Récupère la clé publique VAPID
    const{publicKey}=await fetch("/api/push/vapid-public-key").then(r=>r.json());
    // Enregistre le service worker
    const reg=await navigator.serviceWorker.register("/sw.js");
    await navigator.serviceWorker.ready;
    // S'abonne aux push
    const sub=await reg.pushManager.subscribe({
      userVisibleOnly:true,
      applicationServerKey:urlBase64ToUint8Array(publicKey)
    });
    // Envoie l'abonnement au serveur
    await fetch("/api/push/subscribe",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({subscription:sub.toJSON()})
    });
    await refreshNotifStatus();
  }catch(e){
    if(msg)msg.innerHTML=`<span style="color:#F43F5E">Erreur : ${e.message}</span>`;
  }
}

async function desactiverNotifs(){
  await fetch("/api/push/unsubscribe",{method:"POST"});
  // Désabonne aussi le navigateur
  try{
    const reg=await navigator.serviceWorker.getRegistration("/sw.js");
    if(reg){
      const sub=await reg.pushManager.getSubscription();
      if(sub)await sub.unsubscribe();
    }
  }catch(e){}
  await refreshNotifStatus();
}

async function doLogout(){await fetch("/api/logout",{method:"POST"});window.location.href="/";}
loadVehicules();
</script></body></html>"""

# ─────────────────────────────────────────────────────────────
#  DÉMARRAGE
# ─────────────────────────────────────────────────────────────
with app.app_context():
    init_db()

# Démarrage du thread de surveillance
_t = threading.Thread(target=surveillance_vehicules, daemon=True)
_t.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)