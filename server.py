# ============================================================
#  server.py — GPS Tracker v3
#  Design : Ocean Blue + Violet — Style Stripe Premium
# ============================================================

from flask import Flask, jsonify, request, session, redirect
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3, os
from functools import wraps

app = Flask(__name__)
app.secret_key = "gps_tracker_secret_key_2026"
CORS(app)
DATABASE = "gps_data.db"

# ─────────────────────────────────────────────────────────────
#  BASE DE DONNÉES
# ─────────────────────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS utilisateurs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL, prenom TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE, mot_de_passe TEXT NOT NULL,
        telephone TEXT, role TEXT NOT NULL DEFAULT 'user',
        actif INTEGER NOT NULL DEFAULT 1,
        date_creation TEXT DEFAULT (datetime('now')),
        derniere_connexion TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS vehicules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        proprietaire_id INTEGER NOT NULL,
        marque TEXT NOT NULL, modele TEXT NOT NULL,
        immatriculation TEXT NOT NULL UNIQUE,
        type_vehicule TEXT NOT NULL,
        couleur TEXT, annee INTEGER,
        device_id TEXT NOT NULL UNIQUE,
        actif INTEGER NOT NULL DEFAULT 1,
        date_ajout TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (proprietaire_id) REFERENCES utilisateurs(id))""")
    c.execute("""CREATE TABLE IF NOT EXISTS positions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicule_id INTEGER NOT NULL,
        latitude REAL NOT NULL, longitude REAL NOT NULL,
        vitesse REAL DEFAULT 0, altitude REAL DEFAULT 0,
        satellites INTEGER DEFAULT 0, timestamp TEXT,
        created_at TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (vehicule_id) REFERENCES vehicules(id))""")
    if not c.execute("SELECT id FROM utilisateurs WHERE role='admin'").fetchone():
        c.execute("INSERT INTO utilisateurs (nom,prenom,email,mot_de_passe,role) VALUES (?,?,?,?,?)",
            ("Admin","GPS","admin@gps.com",generate_password_hash("admin123"),"admin"))
        print("[DB] Admin créé → admin@gps.com / admin123")
    conn.commit(); conn.close()
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
    conn = get_db()
    user = conn.execute("SELECT * FROM utilisateurs WHERE email=?", (data["email"],)).fetchone()
    if not user or not user["actif"]:
        conn.close()
        return jsonify({"error": "Compte introuvable ou désactivé"}), 401
    if not check_password_hash(user["mot_de_passe"], data["mot_de_passe"]):
        conn.close()
        return jsonify({"error": "Email ou mot de passe incorrect"}), 401
    conn.execute("UPDATE utilisateurs SET derniere_connexion=datetime('now') WHERE id=?", (user["id"],))
    conn.commit(); conn.close()
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
    conn = get_db()
    user = conn.execute(
        "SELECT id,nom,prenom,email,telephone,role,date_creation,derniere_connexion FROM utilisateurs WHERE id=?",
        (session["user_id"],)).fetchone()
    conn.close()
    return jsonify(dict(user)), 200

# ─────────────────────────────────────────────────────────────
#  API ADMIN
# ─────────────────────────────────────────────────────────────

@app.route("/api/admin/proprietaires", methods=["GET"])
@admin_required
def get_proprietaires():
    conn = get_db()
    rows = conn.execute("""
        SELECT u.id,u.nom,u.prenom,u.email,u.telephone,u.actif,u.date_creation,
               COUNT(v.id) as nb_vehicules
        FROM utilisateurs u
        LEFT JOIN vehicules v ON v.proprietaire_id=u.id
        WHERE u.role='user' GROUP BY u.id ORDER BY u.date_creation DESC""").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows]), 200

@app.route("/api/admin/proprietaires", methods=["POST"])
@admin_required
def creer_proprietaire():
    data = request.get_json()
    for c in ["nom","prenom","email","mot_de_passe","telephone"]:
        if not data.get(c): return jsonify({"error":f"Champ manquant : {c}"}), 400
    conn = get_db()
    if conn.execute("SELECT id FROM utilisateurs WHERE email=?", (data["email"],)).fetchone():
        conn.close(); return jsonify({"error":"Email déjà utilisé"}), 409
    conn.execute("INSERT INTO utilisateurs (nom,prenom,email,mot_de_passe,telephone,role) VALUES (?,?,?,?,?,'user')",
        (data["nom"],data["prenom"],data["email"],generate_password_hash(data["mot_de_passe"]),data["telephone"]))
    conn.commit()
    new_id = conn.execute("SELECT last_insert_rowid() as id").fetchone()["id"]
    conn.close()
    return jsonify({"status":"ok","id":new_id}), 201

@app.route("/api/admin/proprietaires/<int:uid>/toggle", methods=["POST"])
@admin_required
def toggle_proprietaire(uid):
    conn = get_db()
    user = conn.execute("SELECT actif FROM utilisateurs WHERE id=? AND role='user'", (uid,)).fetchone()
    if not user: conn.close(); return jsonify({"error":"Introuvable"}), 404
    nouvel = 0 if user["actif"] else 1
    conn.execute("UPDATE utilisateurs SET actif=? WHERE id=?", (nouvel, uid))
    conn.commit(); conn.close()
    return jsonify({"status":"ok","actif":nouvel}), 200

@app.route("/api/admin/vehicules", methods=["GET"])
@admin_required
def get_all_vehicules():
    conn = get_db()
    rows = conn.execute("""
        SELECT v.*,u.nom||' '||u.prenom as proprietaire_nom
        FROM vehicules v JOIN utilisateurs u ON u.id=v.proprietaire_id
        ORDER BY v.date_ajout DESC""").fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows]), 200

@app.route("/api/admin/vehicules", methods=["POST"])
@admin_required
def creer_vehicule():
    data = request.get_json()
    for c in ["proprietaire_id","marque","modele","immatriculation","type_vehicule","device_id"]:
        if not data.get(c): return jsonify({"error":f"Champ manquant : {c}"}), 400
    conn = get_db()
    try:
        conn.execute("""INSERT INTO vehicules
            (proprietaire_id,marque,modele,immatriculation,type_vehicule,couleur,annee,device_id)
            VALUES (?,?,?,?,?,?,?,?)""",
            (data["proprietaire_id"],data["marque"],data["modele"],data["immatriculation"],
             data["type_vehicule"],data.get("couleur",""),data.get("annee",2024),data["device_id"]))
        conn.commit()
        new_id = conn.execute("SELECT last_insert_rowid() as id").fetchone()["id"]
        conn.close()
        return jsonify({"status":"ok","id":new_id}), 201
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"error":"Immatriculation ou device_id déjà utilisé"}), 409

@app.route("/api/admin/vehicules/<int:vid>/toggle", methods=["POST"])
@admin_required
def toggle_vehicule(vid):
    conn = get_db()
    v = conn.execute("SELECT actif FROM vehicules WHERE id=?", (vid,)).fetchone()
    if not v: conn.close(); return jsonify({"error":"Introuvable"}), 404
    nouvel = 0 if v["actif"] else 1
    conn.execute("UPDATE vehicules SET actif=? WHERE id=?", (nouvel, vid))
    conn.commit(); conn.close()
    return jsonify({"status":"ok","actif":nouvel}), 200

@app.route("/api/user/vehicules", methods=["GET"])
@login_required
def get_user_vehicules():
    conn = get_db()
    rows = conn.execute("""
        SELECT * FROM vehicules WHERE proprietaire_id=? AND actif=1
        ORDER BY date_ajout DESC""", (session["user_id"],)).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows]), 200

@app.route("/api/position", methods=["POST"])
def receive_position():
    data = request.get_json()
    if not data or not data.get("device_id"):
        return jsonify({"error":"device_id manquant"}), 400
    conn = get_db()
    v = conn.execute("SELECT id FROM vehicules WHERE device_id=? AND actif=1", (data["device_id"],)).fetchone()
    if not v: conn.close(); return jsonify({"error":"Véhicule inconnu"}), 404
    conn.execute("""INSERT INTO positions (vehicule_id,latitude,longitude,vitesse,altitude,satellites,timestamp)
        VALUES (?,?,?,?,?,?,?)""",
        (v["id"],data["lat"],data["lng"],data.get("speed",0),
         data.get("altitude",0),data.get("satellites",0),data.get("timestamp","")))
    conn.commit(); conn.close()
    return jsonify({"status":"ok"}), 200

@app.route("/api/positions/<int:vid>", methods=["GET"])
@login_required
def get_positions(vid):
    limit = request.args.get("limit", 200, type=int)
    conn = get_db()
    if session.get("role") != "admin":
        v = conn.execute("SELECT id FROM vehicules WHERE id=? AND proprietaire_id=?",
            (vid, session["user_id"])).fetchone()
        if not v: conn.close(); return jsonify({"error":"Accès refusé"}), 403
    rows = conn.execute("SELECT * FROM positions WHERE vehicule_id=? ORDER BY id DESC LIMIT ?", (vid, limit)).fetchall()
    conn.close()
    result = [dict(r) for r in rows]
    result.reverse()
    return jsonify(result), 200

@app.route("/api/positions/<int:vid>/last", methods=["GET"])
@login_required
def get_last_position(vid):
    conn = get_db()
    row = conn.execute("SELECT * FROM positions WHERE vehicule_id=? ORDER BY id DESC LIMIT 1", (vid,)).fetchone()
    conn.close()
    if not row: return jsonify({"error":"Aucune position"}), 404
    return jsonify(dict(row)), 200

# ─────────────────────────────────────────────────────────────
#  ROUTES HTML
# ─────────────────────────────────────────────────────────────

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
#  PAGE LOGIN — Ocean Blue + Violet
# ═════════════════════════════════════════════════════════════

LOGIN_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Connexion</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#F5F3FF;
  --surface:#FFFFFF;
  --border:#E5E7EB;
  --primary:#6366F1;
  --primary2:#4F46E5;
  --cyan:#06B6D4;
  --violet:#7C3AED;
  --grad:linear-gradient(135deg,#6366F1,#06B6D4);
  --grad2:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
  --green:#10B981;
  --red:#F43F5E;
  --text:#111827;
  --text2:#6B7280;
  --text3:#9CA3AF;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;min-height:100vh;display:flex;
  align-items:center;justify-content:center;position:relative;overflow:hidden;
  background:linear-gradient(160deg,#EDE9FE 0%,#E0F2FE 55%,#F0FDF4 100%)}

.orb{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
.o1{width:500px;height:500px;background:radial-gradient(circle,rgba(99,102,241,0.15),transparent);
  top:-120px;right:-80px}
.o2{width:400px;height:400px;background:radial-gradient(circle,rgba(6,182,212,0.12),transparent);
  bottom:-80px;left:-60px}
.o3{width:250px;height:250px;background:radial-gradient(circle,rgba(124,58,237,0.1),transparent);
  top:50%;left:30%}

.card{position:relative;z-index:1;background:rgba(255,255,255,0.85);
  backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.9);
  border-radius:24px;padding:52px 44px;width:100%;max-width:430px;
  box-shadow:0 8px 40px rgba(99,102,241,0.12),0 2px 8px rgba(0,0,0,0.04)}

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

.divider{display:flex;align-items:center;gap:10px;margin:20px 0}
.divider-line{flex:1;height:1px;background:var(--border)}
.divider-txt{font-size:11px;color:var(--text3);font-weight:500}

.fg{margin-bottom:18px}
.fg label{display:block;font-size:11px;font-weight:700;color:var(--text2);
  margin-bottom:7px;text-transform:uppercase;letter-spacing:0.7px}
.iw{position:relative}
.ii{position:absolute;left:13px;top:50%;transform:translateY(-50%);
  font-size:15px;opacity:0.35;pointer-events:none}
input{width:100%;height:44px;padding:0 14px 0 42px;
  background:#FAFAFA;border:1.5px solid #E5E7EB;
  border-radius:12px;font-size:14px;font-family:'Inter',sans-serif;
  color:var(--text);outline:none;transition:all 0.2s}
input:hover{border-color:#D1D5DB;background:#fff}
input:focus{border-color:var(--primary);background:#fff;
  box-shadow:0 0 0 4px rgba(99,102,241,0.1)}
input::placeholder{color:var(--text3)}

.btn{width:100%;height:46px;margin-top:6px;background:var(--grad2);
  border:none;border-radius:12px;color:#fff;font-family:'Inter',sans-serif;
  font-size:14px;font-weight:600;cursor:pointer;letter-spacing:0.2px;
  box-shadow:0 4px 16px rgba(99,102,241,0.4);transition:all 0.2s}
.btn:hover{transform:translateY(-1px);box-shadow:0 8px 24px rgba(99,102,241,0.45)}
.btn:active{transform:translateY(0)}

.err{background:#FFF1F2;border:1px solid #FECDD3;color:var(--red);
  padding:11px 14px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}

.trust{display:flex;justify-content:center;gap:20px;margin-top:22px}
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
  <div class="trust">
    <div class="trust-item"><div class="trust-dot"></div>Sécurisé</div>
    <div class="trust-item"><div class="trust-dot"></div>Temps réel</div>
    <div class="trust-item"><div class="trust-dot"></div>GPS IoT</div>
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
</script></body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE ADMIN — Ocean Blue + Violet Premium
# ═════════════════════════════════════════════════════════════

ADMIN_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Admin</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#F8F7FF;
  --surface:#FFFFFF;
  --surface2:#F9FAFB;
  --border:#E5E7EB;
  --border2:#D1D5DB;
  --primary:#6366F1;
  --primary2:#4F46E5;
  --violet:#7C3AED;
  --cyan:#06B6D4;
  --grad:linear-gradient(135deg,#7C3AED,#6366F1,#06B6D4);
  --grad2:linear-gradient(135deg,#6366F1,#06B6D4);
  --green:#10B981;
  --green-bg:rgba(16,185,129,0.08);
  --green-bd:rgba(16,185,129,0.2);
  --red:#F43F5E;
  --red-bg:rgba(244,63,94,0.08);
  --red-bd:rgba(244,63,94,0.2);
  --amber:#F59E0B;
  --text:#111827;
  --text2:#6B7280;
  --text3:#9CA3AF;
  --sidebar-w:256px;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);
  font-size:14px;display:flex;min-height:100vh}

/* ══ SIDEBAR FIXE ══ */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;
  width:var(--sidebar-w);
  background:var(--surface);
  border-right:1px solid var(--border);
  display:flex;flex-direction:column;
  z-index:100;overflow:hidden
}

/* Dégradé décoratif haut sidebar */
.sidebar::before{
  content:'';position:absolute;top:0;left:0;right:0;height:180px;
  background:linear-gradient(180deg,rgba(99,102,241,0.06),transparent);
  pointer-events:none
}

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

/* Nav items */
.s-nav{flex:1;padding:10px 10px 0;overflow-y:auto}
.nav-item{display:flex;align-items:center;gap:10px;padding:10px 14px;
  border-radius:10px;cursor:pointer;color:var(--text2);font-size:13px;
  font-weight:500;transition:all 0.15s;margin-bottom:2px;
  border-left:3px solid transparent;position:relative}
.nav-item:hover{background:rgba(99,102,241,0.06);color:var(--primary)}
.nav-item.active{
  background:linear-gradient(135deg,rgba(124,58,237,0.09),rgba(99,102,241,0.07));
  color:var(--primary);font-weight:600;
  border-left-color:var(--violet)}
.nav-item.active .nav-ico{
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-ico{font-size:16px;width:22px;text-align:center;flex-shrink:0;transition:all 0.15s}
.nav-badge{margin-left:auto;background:var(--grad);color:#fff;
  font-size:10px;font-weight:700;padding:2px 7px;border-radius:99px}

/* Bouton déconnexion FIXE en bas */
.s-bottom{
  padding:14px 12px;
  border-top:1px solid var(--border);
  background:var(--surface);
  flex-shrink:0
}
.btn-logout{
  width:100%;padding:10px 16px;
  background:var(--red-bg);color:var(--red);
  border:1px solid var(--red-bd);border-radius:10px;
  cursor:pointer;font-size:13px;font-weight:600;
  font-family:'Inter',sans-serif;transition:all 0.15s;
  display:flex;align-items:center;justify-content:center;gap:8px
}
.btn-logout:hover{background:rgba(244,63,94,0.14);border-color:rgba(244,63,94,0.35)}

/* ══ MAIN ══ */
.main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;min-width:0}

.topbar{position:sticky;top:0;z-index:50;
  height:60px;padding:0 28px;background:rgba(255,255,255,0.9);
  backdrop-filter:blur(12px);border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
  box-shadow:0 1px 4px rgba(0,0,0,0.04)}
.tb-left{display:flex;align-items:center;gap:8px}
.tb-crumb{font-size:12px;color:var(--text3);font-weight:500}
.tb-title{font-size:18px;font-weight:700;color:var(--text);letter-spacing:-0.3px}
.tb-right{display:flex;align-items:center;gap:10px}
.clock{padding:5px 14px;background:var(--surface2);border:1px solid var(--border);
  border-radius:8px;font-size:12px;color:var(--text2);font-variant-numeric:tabular-nums;font-weight:500}

.content{padding:28px;flex:1}
.section{display:none}
.section.active{display:block;animation:fadeUp 0.2s ease}
@keyframes fadeUp{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:translateY(0)}}

/* ── Stats ── */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:28px}
.stat{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:22px;position:relative;overflow:hidden;transition:all 0.2s;cursor:default}
.stat:hover{border-color:rgba(99,102,241,0.25);
  box-shadow:0 4px 20px rgba(99,102,241,0.1);transform:translateY(-2px)}
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
.sh{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
.sh h2{font-size:17px;font-weight:700;color:var(--text);letter-spacing:-0.3px}
.sh-sub{font-size:13px;color:var(--text3);margin-top:2px}

/* ── Boutons ── */
.btn{height:40px;padding:0 18px;border:none;border-radius:10px;cursor:pointer;
  font-size:13px;font-weight:600;font-family:'Inter',sans-serif;
  transition:all 0.2s;display:inline-flex;align-items:center;gap:7px}
.btn-primary{background:var(--grad);color:#fff;
  box-shadow:0 3px 12px rgba(99,102,241,0.35)}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 6px 20px rgba(99,102,241,0.45)}
.btn-danger{background:var(--red-bg);color:var(--red);border:1px solid var(--red-bd)}
.btn-danger:hover{background:rgba(244,63,94,0.14)}
.btn-success{background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
.btn-success:hover{background:rgba(16,185,129,0.14)}
.btn-sm{height:30px;padding:0 13px;font-size:12px;border-radius:8px}

/* ── Table Stripe ── */
.table-card{background:var(--surface);border:1px solid var(--border);
  border-radius:16px;overflow:hidden;
  box-shadow:0 1px 4px rgba(0,0,0,0.04)}
table{width:100%;border-collapse:separate;border-spacing:0}
thead{background:var(--surface2)}
th{padding:12px 18px;text-align:left;font-size:11px;color:var(--text3);
  font-weight:700;text-transform:uppercase;letter-spacing:0.8px;
  border-bottom:1px solid var(--border)}
tbody tr{transition:background 0.12s}
tbody tr:hover td{background:rgba(99,102,241,0.025)}
td{padding:14px 18px;font-size:13px;color:var(--text2);
  border-bottom:1px solid var(--border)}
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

/* ── Positions propriétaires en haut ── */
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
.hs-val{font-size:22px;font-weight:700;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hs-lbl{font-size:11px;color:var(--text3);font-weight:500;margin-top:3px}

/* ── Paramètres ── */
.param-card{background:var(--surface);border:1px solid var(--border);
  border-radius:14px;padding:24px;margin-bottom:14px}
.param-title{font-size:14px;font-weight:700;color:var(--text);margin-bottom:3px}
.param-sub{font-size:12px;color:var(--text3);margin-bottom:18px}
.param-row{display:flex;justify-content:space-between;align-items:center;
  padding:13px 0;border-bottom:1px solid var(--border)}
.param-row:last-child{border-bottom:none;padding-bottom:0}
.p-lbl{font-size:13px;font-weight:500;color:var(--text)}
.p-desc{font-size:11px;color:var(--text3);margin-top:2px}
.p-badge{font-size:11px;font-weight:600;padding:4px 12px;border-radius:99px}
.p-blue{background:rgba(99,102,241,0.08);color:var(--primary);border:1px solid rgba(99,102,241,0.2)}
.p-violet{background:rgba(124,58,237,0.08);color:var(--violet);border:1px solid rgba(124,58,237,0.2)}
.p-green{background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}

/* ── Modal ── */
.mbg{display:none;position:fixed;inset:0;background:rgba(17,24,39,0.45);
  backdrop-filter:blur(4px);z-index:200;align-items:center;justify-content:center}
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
.fg select option{background:#fff}
.fg2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ma{display:flex;gap:10px;margin-top:24px;padding-top:20px;border-top:1px solid var(--border)}
.ma .btn{flex:1;justify-content:center;height:42px}
.al{padding:10px 14px;border-radius:10px;font-size:12px;font-weight:500;
  margin-bottom:14px;display:none}
.al-e{background:#FFF1F2;border:1px solid #FECDD3;color:var(--red)}
.al-o{background:#F0FDF4;border:1px solid #BBF7D0;color:var(--green)}
</style></head><body>

<!-- ══ SIDEBAR ══ -->
<div class="sidebar">
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

  <!-- BOUTON DÉCONNEXION FIXE -->
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()">
      🚪 Déconnexion
    </button>
  </div>
</div>

<!-- ══ MAIN ══ -->
<div class="main">
  <div class="topbar">
    <div class="tb-left">
      <span class="tb-crumb">Admin /</span>
      <span class="tb-title" id="pt">Dashboard</span>
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

      <!-- Positions en haut — SANS altitude -->
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
      <div class="table-card"><table>
        <thead><tr>
          <th>Nom complet</th><th>Email</th><th>Téléphone</th>
          <th>Véhicules</th><th>Depuis</th><th>Statut</th><th>Action</th>
        </tr></thead>
        <tbody id="tbp">
          <tr><td colspan="7"><div class="empty"><div class="empty-ico">👥</div>
            <div class="empty-txt">Chargement...</div></div></td></tr>
        </tbody>
      </table></div>
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
      <div class="table-card"><table>
        <thead><tr>
          <th>Immatriculation</th><th>Marque / Modèle</th><th>Type</th>
          <th>Propriétaire</th><th>Device ID</th><th>Statut</th><th>Action</th>
        </tr></thead>
        <tbody id="tbv">
          <tr><td colspan="7"><div class="empty"><div class="empty-ico">🚗</div>
            <div class="empty-txt">Chargement...</div></div></td></tr>
        </tbody>
      </table></div>
    </div>

    <!-- HISTORIQUE GPS — sans altitude -->
    <div class="section" id="s-historique">
      <div class="sh"><div>
        <h2>Historique GPS</h2>
        <div class="sh-sub">Consultez l'historique des positions par véhicule</div>
      </div></div>
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
      <div class="table-card"><table>
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
      </table></div>
    </div>

    <!-- PARAMÈTRES -->
    <div class="section" id="s-parametres">
      <div class="sh"><div>
        <h2>Paramètres</h2>
        <div class="sh-sub">Configuration du système GPS Tracker</div>
      </div></div>

      <div class="param-card">
        <div class="param-title">Compte administrateur</div>
        <div class="param-sub">Informations de votre compte</div>
        <div class="param-row">
          <div><div class="p-lbl">Email de connexion</div>
          <div class="p-desc">admin@gps.com</div></div>
          <span class="p-badge p-violet">Administrateur</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Niveau d'accès</div>
          <div class="p-desc">Contrôle total sur toutes les fonctionnalités</div></div>
          <span class="p-badge p-green">Actif</span>
        </div>
      </div>

      <div class="param-card">
        <div class="param-title">Système de suivi GPS</div>
        <div class="param-sub">État des services et configuration</div>
        <div class="param-row">
          <div><div class="p-lbl">API ESP32</div>
          <div class="p-desc">Endpoint : POST /api/position</div></div>
          <span class="p-badge p-green">En ligne</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Base de données</div>
          <div class="p-desc">SQLite — gps_data.db</div></div>
          <span class="p-badge p-green">Connectée</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Intervalle de mise à jour</div>
          <div class="p-desc">Fréquence de rafraîchissement de la carte</div></div>
          <select class="h-select" style="width:160px">
            <option>2 secondes</option>
            <option>5 secondes</option>
            <option>10 secondes</option>
          </select>
        </div>
      </div>

      <div class="param-card">
        <div class="param-title">À propos</div>
        <div class="param-sub">Informations sur l'application</div>
        <div class="param-row">
          <div><div class="p-lbl">GPS Tracker</div>
          <div class="p-desc">Version 3.0 — Ocean Blue + Violet</div></div>
          <span class="p-badge p-blue">Flask · SQLite</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Design</div>
          <div class="p-desc">Style Stripe Premium</div></div>
          <span class="p-badge p-violet">Inter · Gradient</span>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- MODAL PROPRIÉTAIRE -->
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
    <div class="fg"><label>Email *</label><input type="email" id="pe" placeholder="Saliou@email.com"/></div>
    <div class="fg"><label>Téléphone *</label><input id="pt" placeholder="+221 77 229 22 03"/></div>
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

function show(n,el){
  document.querySelectorAll(".section").forEach(s=>s.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  document.getElementById("s-"+n).classList.add("active");
  el.classList.add("active");
  document.getElementById("pt").textContent=T[n];
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
  // Stats en haut
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
    <td><button class="btn btn-sm ${p.actif?'btn-danger':'btn-success'}" onclick="toggleP(${p.id})">${p.actif?'Désactiver':'Activer'}</button></td>
  </tr>`).join("");
}

async function creerP(){
  const e=document.getElementById("ep"),o=document.getElementById("op");
  e.style.display=o.style.display="none";
  const body={nom:document.getElementById("pn").value.trim(),prenom:document.getElementById("pp").value.trim(),
    email:document.getElementById("pe").value.trim(),telephone:document.getElementById("pt").value.trim(),
    mot_de_passe:document.getElementById("pw").value};
  if(!body.nom||!body.prenom||!body.email||!body.telephone||!body.mot_de_passe){
    e.textContent="Tous les champs sont obligatoires.";e.style.display="block";return;}
  const res=await fetch("/api/admin/proprietaires",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){o.textContent="✓ Propriétaire créé avec succès !";o.style.display="block";
    ["pn","pp","pe","pt","pw"].forEach(id=>document.getElementById(id).value="");loadStats();}
  else{e.textContent=data.error;e.style.display="block";}
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
    <td><button class="btn btn-sm ${v.actif?'btn-danger':'btn-success'}" onclick="toggleV(${v.id})">${v.actif?'Désactiver':'Activer'}</button></td>
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
  const body={proprietaire_id:parseInt(document.getElementById("vp").value),
    marque:document.getElementById("vm").value.trim(),modele:document.getElementById("vmo").value.trim(),
    immatriculation:document.getElementById("vi").value.trim(),type_vehicule:document.getElementById("vt").value,
    couleur:document.getElementById("vc").value.trim(),annee:parseInt(document.getElementById("va").value)||2024,
    device_id:document.getElementById("vd").value.trim()};
  const res=await fetch("/api/admin/vehicules",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){o.textContent="✓ Véhicule créé avec succès !";o.style.display="block";loadStats();}
  else{e.textContent=data.error;e.style.display="block";}
}

async function toggleV(id){await fetch(`/api/admin/vehicules/${id}/toggle`,{method:"POST"});loadV();}

/* ── Historique — sans altitude ── */
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

function openMP(){document.getElementById("ep").style.display=document.getElementById("op").style.display="none";document.getElementById("mp").classList.add("open");}
function closeM(id){document.getElementById(id).classList.remove("open");}
async function doLogout(){await fetch("/api/logout",{method:"POST"});window.location.href="/";}
loadStats();
</script></body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE USER — Ocean Blue + Violet
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

/* SIDEBAR FIXE */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;
  width:var(--sidebar-w);
  background:var(--surface);
  border-right:1px solid var(--border);
  display:flex;flex-direction:column;
  z-index:100
}
.sidebar::before{content:'';position:absolute;top:0;left:0;right:0;height:160px;
  background:linear-gradient(180deg,rgba(124,58,237,0.05),transparent);pointer-events:none}

.s-logo{padding:20px;border-bottom:1px solid var(--border);position:relative}
.s-logo-row{display:flex;align-items:center;gap:10px}
.s-logo-icon{width:36px;height:36px;border-radius:10px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;
  box-shadow:0 3px 10px rgba(99,102,241,0.3)}
.s-logo-name{font-size:14px;font-weight:700;color:var(--text)}
.s-logo-sub{font-size:10px;background:var(--grad);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:600}

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
.tb-title{font-size:15px;font-weight:700;color:var(--text);letter-spacing:-0.2px}
.live-pill{display:flex;align-items:center;gap:6px;padding:5px 13px;
  background:var(--green-bg);border:1px solid var(--green-bd);
  border-radius:99px;font-size:11px;color:var(--green);font-weight:600}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.4}}
.live-blink{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.5s infinite}
.upd{font-size:11px;color:var(--text3);margin-left:8px}

/* INFOBAR — sans altitude */
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
.es-sub{font-size:13px;color:var(--text3)}

/* Sections utilisateur */
.usec{display:none;flex:1;overflow-y:auto;padding:24px}
.usec.active{display:block}

/* Historique user */
.h-filters{display:flex;gap:10px;margin-bottom:18px}
.h-select{height:38px;padding:0 13px;background:var(--surface);border:1px solid var(--border);
  border-radius:10px;font-size:13px;font-family:'Inter',sans-serif;color:var(--text);outline:none}
.h-select:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(99,102,241,0.1)}
.htable{background:var(--surface);border:1px solid var(--border);border-radius:14px;overflow:hidden}
.htable table{width:100%;border-collapse:collapse}
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
  padding:12px 0;border-bottom:1px solid var(--border)}
.prow:last-child{border-bottom:none;padding-bottom:0}
.plbl{font-size:13px;font-weight:500;color:var(--text)}
.pdesc{font-size:11px;color:var(--text3);margin-top:2px}
.pbadge{font-size:11px;font-weight:600;padding:4px 12px;border-radius:99px;
  background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
</style></head><body>

<div class="sidebar">
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
  <!-- BOUTON DÉCONNEXION FIXE -->
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()">🚪 Déconnexion</button>
  </div>
</div>

<div class="main">
  <div class="topbar">
    <div class="tb-title" id="ttl">Sélectionnez un véhicule</div>
    <div style="display:flex;align-items:center;gap:10px">
      <div class="live-pill"><div class="live-blink"></div>Temps réel</div>
      <span class="upd" id="tupd">—</span>
    </div>
  </div>

  <!-- CARTE — infobar sans altitude -->
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
      <div class="es-sub">Cliquez sur un véhicule dans le menu pour démarrer le suivi</div>
    </div>
  </div>

  <!-- HISTORIQUE — sans altitude -->
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
    <div class="htable"><table>
      <thead><tr>
        <th>#</th><th>Date / Heure</th><th>Latitude</th>
        <th>Longitude</th><th>Vitesse</th><th>Satellites</th>
      </tr></thead>
      <tbody id="uhtb">
        <tr><td colspan="6" style="text-align:center;padding:40px;color:var(--text3)">
          Sélectionnez un véhicule pour afficher l'historique
        </td></tr>
      </tbody>
    </table></div>
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
      <div class="ptitle">Système</div>
      <div class="psub">Informations sur l'application</div>
      <div class="prow"><div><div class="plbl">GPS Tracker v3.0</div><div class="pdesc">Ocean Blue + Violet · Style Stripe</div></div><span class="pbadge">Flask · SQLite</span></div>
    </div>
  </div>
</div>

<script>
let map=null,marker=null,poly=null,selId=null,interval=null,meD=null,vehD=[];

function showTab(n,el){
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  if(el)el.classList.add("active");
  document.getElementById("tab-carte").style.display=n==="carte"?"flex":"none";
  document.querySelectorAll(".usec").forEach(s=>s.classList.remove("active"));
  if(n!=="carte")document.getElementById("tab-"+n).classList.add("active");
  if(n==="historique")initUH();
  if(n==="parametres")loadParams();
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
  if(!vehs.length){list.innerHTML='<div style="padding:14px;color:var(--text3);font-size:12px">Aucun véhicule associé</div>';return;}
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
  initMap();
  if(poly)poly.setLatLngs([]);
  if(marker){map.removeLayer(marker);marker=null;}
  setTimeout(()=>map.invalidateSize(),100);
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
  if(!data.length){tb.innerHTML='<tr><td colspan="6" style="text-align:center;padding:40px;color:var(--text3)">Aucune position enregistrée</td></tr>';return;}
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
        padding:10px 0;border-bottom:1px solid var(--border)">
        <div>
          <div style="font-size:13px;font-weight:600;color:var(--text)">${v.immatriculation}</div>
          <div style="font-size:11px;color:var(--text3)">${v.marque} ${v.modele} · ${v.type_vehicule}</div>
        </div>
        <span class="pbadge">Actif</span>
      </div>`).join("")
    :'<div style="color:var(--text3);font-size:13px">Aucun véhicule associé</div>';
}

async function doLogout(){await fetch("/api/logout",{method:"POST"});window.location.href="/";}
loadVehicules();
</script></body></html>"""

# ─────────────────────────────────────────────────────────────
#  DÉMARRAGE
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)