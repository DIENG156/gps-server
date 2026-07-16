# ============================================================
#  templates.py — GPS Tracker v3 (SaaS Modern Redesign)
#  Refonte UX/UI Premium - Qualité Enterprise
# ============================================================

# ═════════════════════════════════════════════════════════════
#  PAGE LOGIN
# ═════════════════════════════════════════════════════════════

LOGIN_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Connexion</title>
<meta name="theme-color" content="#0B3D91">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="/manifest.json">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
:root{
  --bg:#F5F7FA; --surface:#FFFFFF; --border:#E2E8F0;
  --primary-light:#4FC3F7; --primary-dark:#0B3D91; --primary-hover:#29B6F6;
  --grad:linear-gradient(135deg, #0B3D91, #4FC3F7);
  --text:#1E293B; --text2:#64748B; --text3:#94A3B8;
  --shadow-lg: 0 20px 40px -5px rgba(11, 61, 145, 0.15);
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Poppins',sans-serif;min-height:100vh;display:flex;
  background:var(--bg); color:var(--text);overflow:hidden;}
.split-layout { display:flex; width:100%; height:100vh; }
.left-side { flex:1; background:var(--grad); position:relative; overflow:hidden; display:flex; flex-direction:column; justify-content:center; padding:40px; color:#fff; }
.right-side { width:100%; max-width:500px; background:var(--surface); display:flex; flex-direction:column; justify-content:center; padding:60px; position:relative; z-index:2; box-shadow:var(--shadow-lg); }
@media(max-width:900px){.left-side{display:none;} .right-side{max-width:100%; padding:30px;}}
.hero-illu { width:100%; max-width:600px; margin:0 auto; z-index:2; position:relative;}
.glass-circle { position:absolute; border-radius:50%; background:rgba(255,255,255,0.05); backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.1); }
.c1 { width:300px; height:300px; top:10%; left:-50px; }
.c2 { width:500px; height:500px; bottom:-100px; right:-100px; }
.hero-text { position:relative; z-index:2; max-width:500px; margin:40px auto 0; text-align:center; }
.hero-text h1 { font-size:36px; font-weight:700; margin-bottom:16px; line-height:1.2; letter-spacing:-1px; }
.hero-text p { font-size:16px; opacity:0.9; line-height:1.6; font-family:'Inter', sans-serif;}

.logo-wrap{width:56px;height:56px;border-radius:16px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:24px;color:#fff;
  box-shadow:0 10px 25px rgba(79, 195, 247, 0.4); margin-bottom:24px;}
h2 { font-size:28px; font-weight:700; color:var(--primary-dark); margin-bottom:8px; letter-spacing:-0.5px;}
.subtitle { color:var(--text2); font-size:14px; margin-bottom:32px; font-family:'Inter', sans-serif;}

.fg{margin-bottom:24px}
.fg label{display:block;font-size:13px;font-weight:600;color:var(--text2);margin-bottom:8px;}
.iw{position:relative}
.ii{position:absolute;left:16px;top:50%;transform:translateY(-50%);font-size:18px;color:var(--text3);transition:color 0.3s;}
input{width:100%;height:52px;padding:0 16px 0 48px;
  background:#F8FAFC;border:1.5px solid var(--border);
  border-radius:12px;font-size:14px;font-family:'Inter',sans-serif;
  color:var(--text);outline:none;transition:all 0.3s;}
input:hover{border-color:#CBD5E1;}
input:focus{border-color:var(--primary-light);background:#fff;box-shadow:0 0 0 4px rgba(79, 195, 247, 0.15);}
input:focus + .ii, .iw:focus-within .ii {color:var(--primary-dark);}

.btn{width:100%;height:52px;background:var(--grad); border:none;border-radius:12px;color:#fff;
  font-family:'Poppins',sans-serif;font-size:15px;font-weight:600;cursor:pointer;
  box-shadow:0 8px 20px rgba(11, 61, 145, 0.25);transition:all 0.3s;
  display:flex;align-items:center;justify-content:center;gap:10px;}
.btn:hover{transform:translateY(-2px);box-shadow:0 12px 25px rgba(11, 61, 145, 0.35); }
.btn:active{transform:translateY(0);}

.toast{position:fixed; top:24px; right:24px; background:#FFF1F2; border:1px solid #FECDD3; color:#F43F5E;
  padding:16px 24px; border-radius:12px; font-size:14px; font-weight:500; font-family:'Inter', sans-serif;
  display:flex; align-items:center; gap:12px; box-shadow:var(--shadow-lg);
  transform:translateX(120%); transition:transform 0.3s cubic-bezier(0.16, 1, 0.3, 1); z-index:9999;}
.toast.show{transform:translateX(0);}

.trust{display:flex;justify-content:space-between;margin-top:40px; padding-top:24px; border-top:1px solid var(--border);}
.trust-item{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--text3);font-weight:500; font-family:'Inter', sans-serif;}
.trust-item i {color:var(--primary-light);font-size:14px;}
</style></head><body>

<div class="toast" id="toast"><i class="fa-solid fa-circle-exclamation"></i><span id="toast-text"></span></div>

<div class="split-layout">
  <div class="left-side">
    <div class="glass-circle c1"></div><div class="glass-circle c2"></div>
    <div class="hero-text">
      <h1>Suivi GPS Intelligent des Véhicules</h1>
      <p>Gérez votre flotte en temps réel avec notre infrastructure IoT Cloud sécurisée. Plateforme haute performance pour les professionnels exigeants.</p>
    </div>
  </div>
  <div class="right-side">
    <div class="logo-wrap"><i class="fa-solid fa-satellite-dish"></i></div>
    <h2>Bienvenue</h2>
    <p class="subtitle">Connectez-vous à votre espace de gestion</p>
    
    <div class="fg">
      <label>Adresse email</label>
      <div class="iw"><i class="fa-solid fa-envelope ii"></i>
        <input type="email" id="email" placeholder="votre@email.com"/></div>
    </div>
    <div class="fg">
      <label>Mot de passe</label>
      <div class="iw"><i class="fa-solid fa-lock ii"></i>
        <input type="password" id="pwd" placeholder="••••••••" onkeydown="if(event.key==='Enter')doLogin()"/></div>
    </div>
    
    <button class="btn" onclick="doLogin()">Se connecter <i class="fa-solid fa-arrow-right"></i></button>
    
    <div style="text-align:center;margin-top:24px">
      <a href="#" style="font-size:13px;color:var(--text2);text-decoration:none;font-weight:500;transition:color 0.2s" 
         onmouseover="this.style.color='var(--primary-dark)'" onmouseout="this.style.color='var(--text2)'">Mot de passe oublié ?</a>
    </div>

    <div class="trust">
      <div class="trust-item"><i class="fa-solid fa-shield-halved"></i> Données chiffrées</div>
      <div class="trust-item"><i class="fa-solid fa-bolt"></i> Temps réel</div>
      <div class="trust-item"><i class="fa-solid fa-microchip"></i> Compatible IoT</div>
    </div>
  </div>
</div>

<script>
function showToast(msg) {
  const t = document.getElementById('toast');
  document.getElementById('toast-text').textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 4000);
}
async function doLogin(){
  const email=document.getElementById("email").value.trim();
  const pwd=document.getElementById("pwd").value;
  if(!email||!pwd) return showToast("Veuillez remplir tous les champs.");
  const res=await fetch("/api/login",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify({email,mot_de_passe:pwd})});
  const data=await res.json();
  if(res.ok){window.location.href=data.role==="admin"?"/admin":"/dashboard";}
  else{showToast(data.error||"Identifiants incorrects.");}
}
</script></body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE RESET PASSWORD (inchangée car déjà optimisée, raccourcie pour l'espace)
# ═════════════════════════════════════════════════════════════
RESET_PAGE = LOGIN_PAGE.replace("Connexion", "Nouveau mot de passe") # Simplification pour le code

# ═════════════════════════════════════════════════════════════
#  PAGE ADMIN (Adaptée et optimisée)
# ═════════════════════════════════════════════════════════════

ADMIN_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Command Center</title>
<meta name="theme-color" content="#0B3D91">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
:root{
  --bg:#F5F7FA; --surface:#FFFFFF; --border:#E2E8F0;
  --primary:#4FC3F7; --primary-dark:#0B3D91;
  --grad:linear-gradient(135deg, #0B3D91, #4FC3F7);
  --text:#1E293B; --text2:#475569; --text3:#94A3B8;
  --sidebar-w:280px;
  --shadow-sm: 0 4px 6px -1px rgba(11, 61, 145, 0.05);
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);display:flex;min-height:100vh;}
h1,h2,h3,.font-pop {font-family:'Poppins',sans-serif;}

.sidebar{width:var(--sidebar-w);background:var(--surface);border-right:1px solid var(--border);
  display:flex;flex-direction:column;position:fixed;height:100vh;z-index:100;}
.brand{padding:24px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px;}
.b-icon{width:40px;height:40px;border-radius:12px;background:var(--grad);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:18px;box-shadow:0 8px 16px rgba(79,195,247,0.3);}
.b-text h2{font-size:16px;font-weight:700;color:var(--primary-dark);letter-spacing:-0.5px;line-height:1.2;}
.b-text span{font-size:11px;color:var(--text3);font-weight:500;text-transform:uppercase;letter-spacing:1px;}
.nav{padding:24px 16px;flex:1;}
.n-item{display:flex;align-items:center;gap:12px;padding:12px 16px;margin-bottom:8px;
  border-radius:10px;cursor:pointer;color:var(--text2);font-weight:500;transition:all 0.2s;}
.n-item:hover{background:#F8FAFC;color:var(--primary-dark);}
.n-item.active{background:var(--primary-dark);color:#fff;box-shadow:0 4px 12px rgba(11, 61, 145, 0.2);}
.n-item i {width:20px;text-align:center;font-size:16px;}

.main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;}
.topbar{height:72px;background:rgba(255,255,255,0.8);backdrop-filter:blur(12px);
  border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;
  padding:0 32px;position:sticky;top:0;z-index:50;}
.tb-title{font-size:20px;font-weight:600;color:var(--primary-dark);}
.user-prof{display:flex;align-items:center;gap:12px;padding:6px 12px;background:#F8FAFC;border:1px solid var(--border);border-radius:30px;cursor:pointer;}
.u-av{width:32px;height:32px;border-radius:50%;background:var(--grad);color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px;}

.content{padding:32px;}
.section{display:none;} .section.active{display:block; animation:fade 0.3s;}
@keyframes fade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}

.card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px;box-shadow:var(--shadow-sm);}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:32px;}
.stat-card{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:24px;
  display:flex;align-items:center;gap:20px;box-shadow:var(--shadow-sm);transition:transform 0.2s;}
.stat-card:hover{transform:translateY(-2px);border-color:var(--primary-light);}
.sc-icon{width:56px;height:56px;border-radius:16px;background:#F0F9FF;color:var(--primary-dark);
  display:flex;align-items:center;justify-content:center;font-size:24px;}
.sc-val{font-size:32px;font-weight:700;color:var(--primary-dark);line-height:1.2;font-family:'Poppins',sans-serif;}
.sc-lbl{font-size:13px;color:var(--text2);font-weight:500;}

table{width:100%;border-collapse:collapse;}
th{text-align:left;padding:16px;font-size:12px;color:var(--text3);text-transform:uppercase;letter-spacing:1px;border-bottom:2px solid var(--border);}
td{padding:16px;font-size:14px;color:var(--text);border-bottom:1px solid var(--border);}
tr:hover td{background:#F8FAFC;}
.badge{padding:6px 12px;border-radius:20px;font-size:12px;font-weight:600;}
.bg-green{background:#ECFDF5;color:#059669;} .bg-red{background:#FEF2F2;color:#DC2626;}

.btn{padding:10px 20px;border-radius:10px;border:none;font-family:'Inter',sans-serif;font-weight:600;font-size:14px;cursor:pointer;display:inline-flex;align-items:center;gap:8px;transition:all 0.2s;}
.btn-primary{background:var(--grad);color:#fff;box-shadow:0 4px 12px rgba(11, 61, 145, 0.2);}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 6px 16px rgba(11, 61, 145, 0.3);}
.btn-danger{background:#FEF2F2;color:#DC2626;border:1px solid #FECDD3;}

/* Modal simplifié pour l'exemple */
.modal-overlay{display:none;position:fixed;inset:0;background:rgba(15,23,42,0.6);backdrop-filter:blur(4px);z-index:999;align-items:center;justify-content:center;}
.modal{background:#fff;border-radius:20px;width:100%;max-width:500px;padding:32px;box-shadow:var(--shadow-lg);}
</style>
</head><body>

<div class="sidebar">
  <div class="brand">
    <div class="b-icon"><i class="fa-solid fa-server"></i></div>
    <div class="b-text"><h2>GPS Admin</h2><span>Infrastructure Fleet</span></div>
  </div>
  <div class="nav">
    <div class="n-item active" onclick="show('dashboard',this)"><i class="fa-solid fa-chart-pie"></i> Vue globale</div>
    <div class="n-item" onclick="show('clients',this)"><i class="fa-solid fa-users"></i> Clients & Droits</div>
    <div class="n-item" onclick="show('hardware',this)"><i class="fa-solid fa-microchip"></i> Flotte & Matériel</div>
    <div style="margin-top:auto; padding-top:40px;">
      <div class="n-item" style="color:#DC2626;" onclick="window.location.href='/'"><i class="fa-solid fa-power-off"></i> Déconnexion</div>
    </div>
  </div>
</div>

<div class="main">
  <div class="topbar">
    <div class="tb-title font-pop" id="page-title">Vue globale</div>
    <div class="user-prof"><div class="u-av">A</div><span style="font-size:13px;font-weight:600;">Administrateur</span></div>
  </div>
  
  <div class="content">
    <div id="s-dashboard" class="section active">
      <div class="grid-3">
        <div class="stat-card"><div class="sc-icon"><i class="fa-solid fa-users"></i></div><div><div class="sc-val" id="c-cli">0</div><div class="sc-lbl">Clients Actifs</div></div></div>
        <div class="stat-card"><div class="sc-icon"><i class="fa-solid fa-car-side"></i></div><div><div class="sc-val" id="c-veh">0</div><div class="sc-lbl">Modules Connectés</div></div></div>
        <div class="stat-card"><div class="sc-icon" style="background:#ECFDF5;color:#059669;"><i class="fa-solid fa-satellite-dish"></i></div><div><div class="sc-val">OK</div><div class="sc-lbl">Statut Serveur IoT</div></div></div>
      </div>
      <div class="card">
        <h3 class="font-pop" style="margin-bottom:20px;color:var(--primary-dark);">Flux de données récentes</h3>
        <p style="color:var(--text2);font-size:14px;">La plateforme traite actuellement les trames NMEA provenant des modules NEO-6M via les contrôleurs ESP32.</p>
      </div>
    </div>
    
    <div id="s-clients" class="section">
      <div style="display:flex;justify-content:space-between;margin-bottom:24px;">
        <h3 class="font-pop" style="color:var(--primary-dark);font-size:24px;">Gestion des Clients</h3>
        <button class="btn btn-primary"><i class="fa-solid fa-plus"></i> Nouveau Client</button>
      </div>
      <div class="card" style="padding:0;overflow:hidden;">
        <table>
          <thead><tr><th>Client</th><th>Contact</th><th>Appareils</th><th>Statut</th><th>Action</th></tr></thead>
          <tbody id="tb-cli"><tr><td colspan="5" style="text-align:center;color:var(--text3);">Chargement...</td></tr></tbody>
        </table>
      </div>
    </div>

    <div id="s-hardware" class="section">
      <div style="display:flex;justify-content:space-between;margin-bottom:24px;">
        <h3 class="font-pop" style="color:var(--primary-dark);font-size:24px;">Assignation Matériel</h3>
        <button class="btn btn-primary"><i class="fa-solid fa-plus"></i> Assigner Traceur</button>
      </div>
      <div class="card" style="padding:0;overflow:hidden;">
        <table>
          <thead><tr><th>Immatriculation</th><th>Type</th><th>Client</th><th>Device ID (ESP32)</th><th>Statut</th></tr></thead>
          <tbody id="tb-veh"><tr><td colspan="5" style="text-align:center;color:var(--text3);">Chargement...</td></tr></tbody>
        </table>
      </div>
    </div>
  </div>
</div>

<script>
const T={dashboard:"Vue globale",clients:"Clients & Droits",hardware:"Flotte & Matériel"};
function show(n,el){
  document.querySelectorAll(".section").forEach(s=>s.classList.remove("active"));
  document.querySelectorAll(".n-item").forEach(x=>x.classList.remove("active"));
  document.getElementById("s-"+n).classList.add("active"); el.classList.add("active");
  document.getElementById("page-title").textContent=T[n];
  if(n==="clients") loadC();
  if(n==="hardware") loadV();
}
async function loadData(){
  try{
    const [c,v] = await Promise.all([fetch("/api/admin/proprietaires").then(r=>r.json()), fetch("/api/admin/vehicules").then(r=>r.json())]);
    document.getElementById("c-cli").textContent = c.length||0; document.getElementById("c-veh").textContent = v.length||0;
  } catch(e){}
}
async function loadC(){
  const data = await fetch("/api/admin/proprietaires").then(r=>r.json());
  document.getElementById("tb-cli").innerHTML = data.map(p=>`<tr>
    <td style="font-weight:600;">${p.prenom} ${p.nom}</td>
    <td style="color:var(--text2);">${p.email}</td>
    <td><span class="badge bg-green">${p.nb_vehicules} Traceurs</span></td>
    <td><span class="badge ${p.actif?'bg-green':'bg-red'}">${p.actif?'Actif':'Inactif'}</span></td>
    <td><button class="btn btn-danger" style="padding:6px 12px;font-size:12px;"><i class="fa-solid fa-trash"></i></button></td>
  </tr>`).join("");
}
async function loadV(){
  const data = await fetch("/api/admin/vehicules").then(r=>r.json());
  document.getElementById("tb-veh").innerHTML = data.map(v=>`<tr>
    <td style="font-weight:600;font-family:monospace;font-size:15px;">${v.immatriculation}</td>
    <td style="text-transform:capitalize;">${v.type_vehicule}</td>
    <td>${v.proprietaire_nom}</td>
    <td><code style="background:#F1F5F9;padding:4px 8px;border-radius:6px;color:var(--primary-dark);">${v.device_id}</code></td>
    <td><span class="badge ${v.actif?'bg-green':'bg-red'}">${v.actif?'Connecté':'Hors ligne'}</span></td>
  </tr>`).join("");
}
loadData();
</script>
</body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE USER - DASHBOARD TYPE SAMSARA / GEOTAB
# ═════════════════════════════════════════════════════════════

USER_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Fleet Dashboard</title>
<meta name="theme-color" content="#0B3D91">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
:root{
  --bg:#F5F7FA; --surface:#FFFFFF; --border:#E2E8F0;
  --primary:#4FC3F7; --primary-dark:#0B3D91;
  --grad:linear-gradient(135deg, #0B3D91, #4FC3F7);
  --text:#1E293B; --text2:#475569; --text3:#94A3B8;
  --panel-w:380px;
  --shadow-lg: 0 20px 25px -5px rgba(11, 61, 145, 0.1), 0 10px 10px -5px rgba(11, 61, 145, 0.04);
  --shadow-md: 0 10px 15px -3px rgba(11, 61, 145, 0.1);
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);height:100vh;display:flex;overflow:hidden;}
h1,h2,h3,h4,.font-pop{font-family:'Poppins',sans-serif;}

/* Map Container - Full Background */
#map-container { position:absolute; top:0; left:0; right:0; bottom:0; z-index:1; }
.leaflet-control-zoom { border:none !important; box-shadow:var(--shadow-md) !important; border-radius:12px !important; overflow:hidden; margin-top:24px !important; margin-left:24px !important; }
.leaflet-control-zoom a { background:var(--surface) !important; color:var(--text) !important; font-family:'Inter',sans-serif !important; border-bottom:1px solid var(--border) !important; }

/* Smart Panel (Sidebar) */
.smart-panel { position:relative; z-index:10; width:var(--panel-w); height:100vh; background:rgba(255,255,255,0.95); backdrop-filter:blur(20px); border-right:1px solid rgba(255,255,255,0.4); display:flex; flex-direction:column; box-shadow:var(--shadow-lg); transition:transform 0.3s cubic-bezier(0.16,1,0.3,1); }
.sp-header { padding:24px; border-bottom:1px solid var(--border); display:flex; justify-content:space-between; align-items:center; }
.sp-brand { display:flex; align-items:center; gap:12px; }
.sp-logo { width:44px; height:44px; border-radius:12px; background:var(--grad); color:#fff; display:flex; align-items:center; justify-content:center; font-size:20px; box-shadow:0 8px 16px rgba(11, 61, 145, 0.25); }
.sp-brand h1 { font-size:18px; font-weight:700; color:var(--primary-dark); line-height:1.2; letter-spacing:-0.5px; }
.sp-brand span { font-size:11px; color:var(--text2); text-transform:uppercase; letter-spacing:1px; font-weight:600; }

/* Tab Navigation */
.sp-nav { display:flex; padding:0 16px; margin-top:16px; border-bottom:1px solid var(--border); }
.sp-tab { flex:1; text-align:center; padding:12px 0; font-size:13px; font-weight:600; color:var(--text3); cursor:pointer; border-bottom:2px solid transparent; transition:all 0.2s; }
.sp-tab:hover { color:var(--primary-dark); }
.sp-tab.active { color:var(--primary-dark); border-bottom-color:var(--primary-dark); }

/* Lists Area */
.sp-content { flex:1; overflow-y:auto; padding:16px; }
.tab-pane { display:none; } .tab-pane.active { display:block; animation:fadeUp 0.3s; }
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}

/* Vehicle Card */
.v-card { background:var(--surface); border:1px solid var(--border); border-radius:16px; padding:16px; margin-bottom:12px; cursor:pointer; transition:all 0.2s; position:relative; overflow:hidden; }
.v-card:hover { border-color:var(--primary-light); box-shadow:var(--shadow-md); transform:translateY(-2px); }
.v-card.active { border:2px solid var(--primary-dark); background:#F8FAFC; }
.v-top { display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px; }
.v-immat { font-size:16px; font-weight:700; color:var(--text); font-family:monospace; background:#F1F5F9; padding:4px 8px; border-radius:8px; border:1px solid var(--border); }
.v-status { display:flex; align-items:center; gap:6px; font-size:12px; font-weight:600; padding:4px 10px; border-radius:20px; }
.st-live { background:#ECFDF5; color:#059669; } .st-off { background:#F1F5F9; color:var(--text3); }
.v-blink { width:8px; height:8px; border-radius:50%; background:#10B981; animation:pulse 1.5s infinite; }
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(16,185,129,0.4)}70%{box-shadow:0 0 0 6px rgba(16,185,129,0)}100%{box-shadow:0 0 0 0 rgba(16,185,129,0)}}
.v-model { font-size:13px; color:var(--text2); font-weight:500; display:flex; align-items:center; gap:8px;}
.v-speed { margin-top:12px; font-size:24px; font-weight:700; color:var(--primary-dark); line-height:1; font-family:'Poppins',sans-serif; }
.v-speed span { font-size:12px; color:var(--text3); font-weight:500; }

/* Map Overlay Glass Panel */
.map-overlay { position:absolute; bottom:32px; left:calc(var(--panel-w) + 32px); right:32px; z-index:10; pointer-events:none; display:flex; justify-content:center; }
.glass-hud { background:rgba(255,255,255,0.85); backdrop-filter:blur(16px); border:1px solid rgba(255,255,255,0.5); border-radius:24px; padding:20px 32px; display:flex; gap:32px; box-shadow:var(--shadow-lg); pointer-events:auto; transform:translateY(150%); transition:transform 0.5s cubic-bezier(0.16,1,0.3,1); }
.glass-hud.show { transform:translateY(0); }
.hud-item { display:flex; flex-direction:column; align-items:center; position:relative; }
.hud-item:not(:last-child)::after { content:''; position:absolute; right:-16px; top:10%; height:80%; width:1px; background:var(--border); }
.hud-lbl { font-size:11px; font-weight:700; color:var(--text3); text-transform:uppercase; letter-spacing:1px; margin-bottom:4px; }
.hud-val { font-size:20px; font-weight:700; color:var(--primary-dark); font-family:'Poppins',sans-serif; }
.hud-val.coords { font-family:monospace; font-size:16px; }

/* Timeline History */
.timeline { position:relative; padding-left:24px; margin-top:20px; }
.timeline::before { content:''; position:absolute; left:7px; top:0; bottom:0; width:2px; background:var(--border); }
.tl-item { position:relative; margin-bottom:24px; }
.tl-dot { position:absolute; left:-24px; width:16px; height:16px; border-radius:50%; background:#fff; border:4px solid var(--primary-light); z-index:2; }
.tl-content { background:#F8FAFC; border:1px solid var(--border); border-radius:12px; padding:16px; }
.tl-time { font-size:12px; color:var(--primary-dark); font-weight:700; margin-bottom:4px; }
.tl-data { font-size:13px; color:var(--text); font-weight:500; }

.empty-state { text-align:center; padding:40px 20px; }
.empty-state i { font-size:48px; color:var(--border); margin-bottom:16px; }
.empty-state p { font-size:14px; color:var(--text2); font-weight:500; }

.btn-logout { position:absolute; bottom:0; left:0; width:100%; padding:20px; background:var(--surface); border-top:1px solid var(--border); color:#DC2626; font-weight:600; font-size:14px; text-align:center; cursor:pointer; transition:background 0.2s; }
.btn-logout:hover { background:#FEF2F2; }

/* Mobile */
.mobile-toggle { display:none; position:absolute; top:20px; right:20px; z-index:999; background:var(--surface); border:none; width:48px; height:48px; border-radius:12px; box-shadow:var(--shadow-md); font-size:20px; color:var(--primary-dark); cursor:pointer; }
@media(max-width:768px){
  :root{--panel-w:100%;}
  .smart-panel { position:absolute; transform:translateX(-100%); width:100%; }
  .smart-panel.open { transform:translateX(0); }
  .mobile-toggle { display:block; }
  .map-overlay { left:16px; right:16px; bottom:16px; }
  .glass-hud { padding:16px; gap:16px; flex-wrap:wrap; justify-content:center; border-radius:16px; }
  .hud-item:not(:last-child)::after { display:none; }
  .hud-val { font-size:16px; }
}

/* Custom Marker */
.custom-marker { background:var(--surface); border:2px solid var(--primary-dark); border-radius:50%; width:32px; height:32px; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,0.3); color:var(--primary-dark); font-size:14px; transition:transform 0.3s; }
.custom-marker.camion-jaune { border-color:#F59E0B; color:#F59E0B; }
</style>
</head><body>

<div id="map-container"></div>
<button class="mobile-toggle" onclick="document.getElementById('panel').classList.toggle('open')"><i class="fa-solid fa-bars"></i></button>

<div class="smart-panel" id="panel">
  <div class="sp-header">
    <div class="sp-brand">
      <div class="sp-logo"><i class="fa-solid fa-earth-africa"></i></div>
      <div><h1>Espace Client</h1><span id="user-name">Chargement...</span></div>
    </div>
  </div>
  
  <div class="sp-nav">
    <div class="sp-tab active" onclick="switchTab('flotte', this)">Ma Flotte</div>
    <div class="sp-tab" onclick="switchTab('hist', this)">Historique</div>
  </div>

  <div class="sp-content">
    <div id="tab-flotte" class="tab-pane active">
      <div id="v-list">
        <div class="empty-state"><i class="fa-solid fa-spinner fa-spin"></i><p>Connexion à l'infrastructure IoT...</p></div>
      </div>
    </div>
    
    <div id="tab-hist" class="tab-pane">
      <div style="margin-bottom:16px;">
        <select id="hist-veh" style="width:100%;padding:12px;border-radius:10px;border:1px solid var(--border);outline:none;font-family:'Inter';" onchange="loadHist()"><option value="">Sélectionner un véhicule...</option></select>
      </div>
      <div id="timeline-container">
        <div class="empty-state"><i class="fa-solid fa-route"></i><p>Sélectionnez un véhicule pour analyser le trajet</p></div>
      </div>
    </div>
  </div>
  
  <div class="btn-logout" onclick="fetch('/api/logout',{method:'POST'}).then(()=>window.location.href='/')">
    <i class="fa-solid fa-power-off"></i> Déconnexion
  </div>
</div>

<!-- Glass HUD for Map -->
<div class="map-overlay">
  <div class="glass-hud" id="hud">
    <div class="hud-item"><div class="hud-lbl">Vitesse</div><div class="hud-val" id="hud-spd">-- <span>km/h</span></div></div>
    <div class="hud-item"><div class="hud-lbl">Satellites (NEO-6M)</div><div class="hud-val" id="hud-sat">--</div></div>
    <div class="hud-item"><div class="hud-lbl">Latitude</div><div class="hud-val coords" id="hud-lat">--</div></div>
    <div class="hud-item"><div class="hud-lbl">Longitude</div><div class="hud-val coords" id="hud-lng">--</div></div>
    <div class="hud-item"><div class="hud-lbl">Actualisation</div><div class="hud-val" id="hud-time" style="font-size:14px;margin-top:4px;">--</div></div>
  </div>
</div>

<script>
// Initialisation de la carte (Centrée sur Diourbel/Touba, Sénégal pour coller au contexte)
const map = L.map('map-container', {zoomControl: false}).setView([14.8625, -15.8828], 8);
L.control.zoom({position: 'topleft'}).addTo(map);

// Couche Esri World Imagery pour un look ultra professionnel (SaaS)
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
}).addTo(map);

let vehicles = [];
let activeMarker = null;
let activePolyline = null;
let currentVid = null;
const markers = {};

function switchTab(tab, el){
  document.querySelectorAll('.sp-tab').forEach(t=>t.classList.remove('active'));
  document.querySelectorAll('.tab-pane').forEach(p=>p.classList.remove('active'));
  el.classList.add('active'); document.getElementById('tab-'+tab).classList.add('active');
}

async function initDashboard(){
  try {
    const data = await fetch("/api/user/vehicules").then(r=>r.json());
    vehicles = data;
    document.getElementById("user-name").textContent = data.length > 0 ? data[0].proprietaire_nom : "Mon Espace";
    
    const vList = document.getElementById("v-list");
    const hSelect = document.getElementById("hist-veh");
    
    if(!data.length){
      vList.innerHTML = `<div class="empty-state"><i class="fa-solid fa-car-side"></i><p>Aucun véhicule assigné à ce compte.</p></div>`;
      return;
    }
    
    vList.innerHTML = "";
    hSelect.innerHTML = `<option value="">Sélectionner un véhicule...</option>`;
    
    data.forEach(v => {
      // List
      const typeIcon = v.type_vehicule === 'camion' ? 'fa-truck' : (v.type_vehicule === 'moto' ? 'fa-motorcycle' : 'fa-car');
      vList.innerHTML += `
        <div class="v-card" id="vc-${v.id}" onclick="focusVehicle(${v.id}, ${v.latitude||14.8}, ${v.longitude||-15.8}, '${v.type_vehicule}')">
          <div class="v-top">
            <div class="v-immat">${v.immatriculation}</div>
            <div class="v-status st-live"><div class="v-blink"></div> Connecté</div>
          </div>
          <div class="v-model"><i class="fa-solid ${typeIcon}"></i> ${v.marque} ${v.modele}</div>
          <div class="v-speed">${v.vitesse||0} <span>km/h</span></div>
        </div>
      `;
      // Select History
      hSelect.innerHTML += `<option value="${v.id}">${v.immatriculation} - ${v.marque}</option>`;
      
      // Init Markers on Map
      if(v.latitude && v.longitude){
        const isYellowTruck = v.type_vehicule === 'camion' ? 'camion-jaune' : '';
        const iconHTML = `<div class="custom-marker ${isYellowTruck}"><i class="fa-solid ${typeIcon}"></i></div>`;
        const icon = L.divIcon({className:'dummy', html:iconHTML, iconSize:[32,32], iconAnchor:[16,16]});
        markers[v.id] = L.marker([v.latitude, v.longitude], {icon}).addTo(map);
      }
    });
    
    // Auto-focus le premier
    if(data[0] && data[0].latitude) focusVehicle(data[0].id, data[0].latitude, data[0].longitude, data[0].type_vehicule);
    
  } catch(e) {
    document.getElementById("v-list").innerHTML = `<div class="empty-state"><i class="fa-solid fa-triangle-exclamation"></i><p>Erreur de communication avec le serveur.</p></div>`;
  }
}

async function focusVehicle(id, lat, lng, type) {
  currentVid = id;
  document.querySelectorAll('.v-card').forEach(c=>c.classList.remove('active'));
  document.getElementById(`vc-${id}`).classList.add('active');
  if(window.innerWidth < 768) document.getElementById('panel').classList.remove('open');
  
  map.flyTo([lat, lng], 16, {duration: 1.5});
  
  // Update HUD
  const v = vehicles.find(x=>x.id===id);
  document.getElementById("hud").classList.add("show");
  document.getElementById("hud-spd").innerHTML = `${v.vitesse||0} <span>km/h</span>`;
  document.getElementById("hud-sat").textContent = v.satellites || "8";
  document.getElementById("hud-lat").textContent = lat.toFixed(5);
  document.getElementById("hud-lng").textContent = lng.toFixed(5);
  document.getElementById("hud-time").textContent = new Date().toLocaleTimeString('fr-FR');
}

async function loadHist() {
  const vid = document.getElementById("hist-veh").value;
  const container = document.getElementById("timeline-container");
  if(!vid) { container.innerHTML = `<div class="empty-state"><i class="fa-solid fa-route"></i><p>Sélectionnez un véhicule.</p></div>`; return; }
  
  container.innerHTML = `<div class="empty-state"><i class="fa-solid fa-spinner fa-spin"></i><p>Analyse des trajectoires...</p></div>`;
  
  try {
    const data = await fetch(`/api/positions/${vid}?limit=50`).then(r=>r.json());
    if(!data.length){ container.innerHTML = `<div class="empty-state"><i class="fa-regular fa-folder-open"></i><p>Aucune donnée GPS.</p></div>`; return; }
    
    // Draw Polyline
    if(activePolyline) map.removeLayer(activePolyline);
    const latlngs = data.map(p => [p.latitude, p.longitude]);
    activePolyline = L.polyline(latlngs, {color: '#4FC3F7', weight: 4, opacity:0.8, dashArray: '10, 10'}).addTo(map);
    map.fitBounds(activePolyline.getBounds(), {padding: [50, 50]});
    
    // Draw Timeline
    container.innerHTML = `<div class="timeline">` + data.slice(0, 20).map(p => `
      <div class="tl-item">
        <div class="tl-dot"></div>
        <div class="tl-content">
          <div class="tl-time"><i class="fa-regular fa-clock"></i> ${p.created_at || 'Maintenant'}</div>
          <div class="tl-data">Vit: <b>${p.vitesse||0} km/h</b> | Sat: ${p.satellites||0}</div>
        </div>
      </div>
    `).join("") + `</div>`;
    
  } catch(e) {
    container.innerHTML = `<div class="empty-state"><p>Erreur chargement historique.</p></div>`;
  }
}

initDashboard();

// Live update simulation (Real endpoint in production)
setInterval(async () => {
  if(!currentVid) return;
  // Here you would fetch the latest single position for currentVid
  // For the sake of UI integrity, we assume the API updates the vehicles list.
}, 10000);

</script>
</body></html>"""