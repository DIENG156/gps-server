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

@app.route("/api/admin/vehicules/<int:vid>", methods=["DELETE"])
@admin_required
def supprimer_vehicule(vid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id FROM vehicules WHERE id=%s", (vid,))
    if not c.fetchone():
        c.close(); conn.close()
        return jsonify({"error":"Véhicule introuvable"}), 404
    # Supprimer d'abord les positions GPS
    c.execute("DELETE FROM positions WHERE vehicule_id=%s", (vid,))
    # Supprimer les alertes envoyées
    c.execute("DELETE FROM alertes_envoyees WHERE vehicule_id=%s", (vid,))
    # Supprimer le véhicule
    c.execute("DELETE FROM vehicules WHERE id=%s", (vid,))
    conn.commit(); c.close(); conn.close()
    return jsonify({"status":"ok"}), 200

@app.route("/api/admin/proprietaires/<int:uid>", methods=["DELETE"])
@admin_required
def supprimer_proprietaire(uid):
    conn = get_db(); c = conn.cursor()
    c.execute("SELECT id FROM utilisateurs WHERE id=%s AND role='user'", (uid,))
    if not c.fetchone():
        c.close(); conn.close()
        return jsonify({"error":"Propriétaire introuvable"}), 404
    # Récupérer tous les véhicules du propriétaire
    c.execute("SELECT id FROM vehicules WHERE proprietaire_id=%s", (uid,))
    vehicules = c.fetchall()
    for v in vehicules:
        # Supprimer positions et alertes de chaque véhicule
        c.execute("DELETE FROM positions WHERE vehicule_id=%s", (v["id"],))
        c.execute("DELETE FROM alertes_envoyees WHERE vehicule_id=%s", (v["id"],))
    # Supprimer les véhicules
    c.execute("DELETE FROM vehicules WHERE proprietaire_id=%s", (uid,))
    # Supprimer les abonnements push et tokens reset
    c.execute("DELETE FROM push_subscriptions WHERE user_id=%s", (uid,))
    c.execute("DELETE FROM reset_tokens WHERE user_id=%s", (uid,))
    # Supprimer le propriétaire
    c.execute("DELETE FROM utilisateurs WHERE id=%s", (uid,))
    conn.commit(); c.close(); conn.close()
    return jsonify({"status":"ok"}), 200

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

@app.route("/api/user/vehicules/statut", methods=["GET"])
@login_required
def get_user_vehicules_statut():
    """Retourne les véhicules avec leur statut : mouvement, immobile, sans_signal"""
    conn = get_db(); c = conn.cursor()
    c.execute("""
        SELECT v.id, v.immatriculation, v.marque, v.modele, v.type_vehicule,
               v.couleur, v.annee, v.device_id,
               p.latitude, p.longitude, p.vitesse, p.satellites,
               p.created_at as derniere_pos
        FROM vehicules v
        LEFT JOIN positions p ON p.id = (
            SELECT id FROM positions
            WHERE vehicule_id = v.id
            ORDER BY id DESC LIMIT 1
        )
        WHERE v.proprietaire_id=%s AND v.actif=1
        ORDER BY v.date_ajout DESC""", (session["user_id"],))
    rows = c.fetchall()

    resultat = []
    for v in rows:
        item = dict(v)
        if not v["derniere_pos"]:
            item["statut"] = "sans_signal"
            item["minutes_sans_signal"] = None
        else:
            c.execute("""SELECT EXTRACT(EPOCH FROM
                (NOW() - %s::timestamp))/60 as minutes""",
                (v["derniere_pos"],))
            minutes = c.fetchone()["minutes"] or 0
            item["minutes_sans_signal"] = round(minutes, 1)

            if minutes >= ALERTE_MINUTES:
                item["statut"] = "sans_signal"
            elif (v["vitesse"] or 0) == 0:
                item["statut"] = "immobile"
            else:
                item["statut"] = "mouvement"
        resultat.append(item)

    c.close(); conn.close()
    return jsonify(resultat), 200

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
const CACHE_NAME = 'gps-tracker-v1';
const URLS_TO_CACHE = ['/', '/dashboard', '/admin'];

// Installation - mise en cache
self.addEventListener('install', function(e){
  e.waitUntil(
    caches.open(CACHE_NAME).then(function(cache){
      return cache.addAll(URLS_TO_CACHE);
    })
  );
  self.skipWaiting();
});

// Activation - nettoyage anciens caches
self.addEventListener('activate', function(e){
  e.waitUntil(
    caches.keys().then(function(keys){
      return Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      );
    })
  );
  self.clients.claim();
});

// Fetch - réseau d'abord, cache en fallback
self.addEventListener('fetch', function(e){
  if(e.request.method !== 'GET') return;
  if(e.request.url.includes('/api/')) return; // API toujours en réseau
  e.respondWith(
    fetch(e.request)
      .then(function(res){
        const clone = res.clone();
        caches.open(CACHE_NAME).then(c => c.put(e.request, clone));
        return res;
      })
      .catch(function(){
        return caches.match(e.request);
      })
  );
});

// Push notifications
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

// Clic notification
self.addEventListener('notificationclick', function(e){
  e.notification.close();
  e.waitUntil(clients.openWindow('/dashboard'));
});
"""
    from flask import Response
    return Response(sw_code, mimetype="application/javascript",
                   headers={"Service-Worker-Allowed": "/"})

@app.route("/manifest.json")
def manifest():
    data = {
        "name": "GPS Tracker",
        "short_name": "GPS Tracker",
        "description": "Suivi de véhicules en temps réel",
        "start_url": "/dashboard",
        "display": "standalone",
        "background_color": "#F8F7FF",
        "theme_color": "#6366F1",
        "orientation": "portrait",
        "icons": [
            {
                "src": "https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png",
                "sizes": "72x72",
                "type": "image/png"
            },
            {
                "src": "https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            }
        ]
    }
    from flask import Response
    return Response(json.dumps(data), mimetype="application/manifest+json")

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


# ─────────────────────────────────────────────────────────────
#  IMPORT PAGES HTML
# ─────────────────────────────────────────────────────────────
from templates import LOGIN_PAGE, ADMIN_PAGE, USER_PAGE, RESET_PAGE

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