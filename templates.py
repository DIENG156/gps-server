# ============================================================
#  templates.py — GPS Tracker v3 (SaaS Modern Redesign)
#  Toutes les pages HTML (Login, Admin, User, Reset)
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
<meta name="apple-mobile-web-app-title" content="GPS Tracker">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
:root{
  --bg:#F5F7FA; --surface:#FFFFFF; --border:#E2E8F0;
  --primary-light:#4FC3F7; --primary-dark:#0B3D91; --primary-hover:#29B6F6;
  --grad:linear-gradient(135deg, #0B3D91, #4FC3F7);
  --green:#10B981; --red:#F43F5E;
  --text:#1E293B; --text2:#64748B; --text3:#94A3B8;
  --shadow-sm: 0 4px 6px -1px rgba(11, 61, 145, 0.05), 0 2px 4px -1px rgba(11, 61, 145, 0.03);
  --shadow-lg: 0 20px 25px -5px rgba(11, 61, 145, 0.1), 0 10px 10px -5px rgba(11, 61, 145, 0.04);
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Poppins',sans-serif;min-height:100vh;display:flex;
  align-items:center;justify-content:center;position:relative;overflow:hidden;
  background:var(--bg); color:var(--text);}
.orb{position:fixed;border-radius:50%;pointer-events:none;z-index:0;filter:blur(60px);opacity:0.6;}
.o1{width:400px;height:400px;background:var(--primary-light);top:-100px;right:-100px;opacity:0.3;}
.o2{width:500px;height:500px;background:var(--primary-dark);bottom:-150px;left:-150px;opacity:0.15;}
.card{position:relative;z-index:1;background:rgba(255,255,255,0.85);
  backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.9);
  border-radius:24px;padding:50px 40px;width:100%;max-width:420px;
  box-shadow:var(--shadow-lg);}
@media(max-width:480px){.card{padding:36px 24px;margin:16px;border-radius:20px}}
.logo{text-align:center;margin-bottom:36px}
.logo-wrap{position:relative;width:64px;height:64px;margin:0 auto 16px}
.logo-bg{width:64px;height:64px;border-radius:18px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:28px;color:#fff;
  box-shadow:0 10px 25px rgba(79, 195, 247, 0.4);}
.logo h1{font-size:24px;font-weight:700;letter-spacing:-0.5px;color:var(--primary-dark);}
.logo p{color:var(--text2);font-size:13px;margin-top:4px;font-weight:400;}
.fg{margin-bottom:20px}
.fg label{display:block;font-size:12px;font-weight:600;color:var(--text2);
  margin-bottom:8px;letter-spacing:0.3px}
.iw{position:relative}
.ii{position:absolute;left:16px;top:50%;transform:translateY(-50%);font-size:16px;color:var(--text3);transition:color 0.3s;}
input{width:100%;height:48px;padding:0 16px 0 46px;
  background:#F8FAFC;border:1.5px solid var(--border);
  border-radius:14px;font-size:14px;font-family:'Poppins',sans-serif;
  color:var(--text);outline:none;transition:all 0.3s;box-shadow:inset 0 2px 4px rgba(0,0,0,0.01);}
input:hover{border-color:#CBD5E1;}
input:focus{border-color:var(--primary-light);background:#fff;box-shadow:0 0 0 4px rgba(79, 195, 247, 0.15);}
input:focus + .ii, .iw:focus-within .ii {color:var(--primary-dark);}
input::placeholder{color:var(--text3);font-weight:300;}
.btn{width:100%;height:48px;margin-top:8px;background:var(--grad);
  border:none;border-radius:14px;color:#fff;font-family:'Poppins',sans-serif;
  font-size:15px;font-weight:600;cursor:pointer;letter-spacing:0.3px;
  box-shadow:0 8px 20px rgba(11, 61, 145, 0.2);transition:all 0.3s;
  display:flex;align-items:center;justify-content:center;gap:10px;}
.btn:hover{transform:translateY(-2px);box-shadow:0 12px 25px rgba(11, 61, 145, 0.3);background:linear-gradient(135deg, #093070, #29B6F6);}
.btn:active{transform:translateY(0);}
.err{background:#FFF1F2;border:1px solid #FECDD3;color:var(--red);
  padding:12px 16px;border-radius:12px;font-size:13px;margin-bottom:20px;display:none;
  display:flex;align-items:center;gap:8px;font-weight:500;}
.trust{display:flex;justify-content:center;gap:20px;margin-top:28px;flex-wrap:wrap}
.trust-item{display:flex;align-items:center;gap:6px;font-size:12px;color:var(--text3);font-weight:500;}
.trust-item i {color:var(--primary-light);font-size:10px;}
</style></head><body>
<div class="orb o1"></div><div class="orb o2"></div>
<div class="card">
  <div class="logo">
    <div class="logo-wrap">
      <div class="logo-bg"><i class="fa-solid fa-satellite-dish"></i></div>
    </div>
    <h1>GPS Tracker</h1>
    <p>Système de suivi intelligent & sécurisé</p>
  </div>
  <div class="err" id="err"><i class="fa-solid fa-circle-exclamation"></i><span id="err-text"></span></div>
  <div class="fg">
    <label>Adresse email</label>
    <div class="iw"><i class="fa-solid fa-envelope ii"></i>
      <input type="email" id="email" placeholder="votre@email.com"/></div>
  </div>
  <div class="fg">
    <label>Mot de passe</label>
    <div class="iw"><i class="fa-solid fa-lock ii"></i>
      <input type="password" id="pwd" placeholder="••••••••"
             onkeydown="if(event.key==='Enter')doLogin()"/></div>
  </div>
  <button class="btn" onclick="doLogin()">Se connecter <i class="fa-solid fa-arrow-right"></i></button>
  <div style="text-align:center;margin-top:20px">
    <a href="#" onclick="showForgot()" style="font-size:13px;color:var(--text2);text-decoration:none;
      transition:color 0.3s;font-weight:500;" onmouseover="this.style.color='var(--primary-dark)'"
      onmouseout="this.style.color='var(--text2)'">Mot de passe oublié ?</a>
  </div>
  <div class="trust">
    <div class="trust-item"><i class="fa-solid fa-shield-halved"></i> Sécurisé</div>
    <div class="trust-item"><i class="fa-solid fa-bolt"></i> Temps réel</div>
    <div class="trust-item"><i class="fa-solid fa-cloud"></i> IoT Cloud</div>
  </div>
</div>

<div id="forgot-bg" style="display:none;position:fixed;inset:0;background:rgba(15, 23, 42, 0.6);
  backdrop-filter:blur(8px);z-index:200;align-items:center;justify-content:center;padding:16px">
  <div style="background:#fff;border-radius:24px;padding:36px;width:100%;max-width:420px;
    position:relative;box-shadow:var(--shadow-lg)">
    <div style="position:absolute;top:0;left:20%;right:20%;height:4px;
      background:var(--grad);border-radius:0 0 8px 8px"></div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px">
      <h3 style="font-size:18px;font-weight:700;color:var(--primary-dark)">Mot de passe oublié</h3>
      <button onclick="hideForgot()" style="width:32px;height:32px;border-radius:10px;
        border:1px solid var(--border);background:#F8FAFC;cursor:pointer;font-size:14px;color:var(--text2);
        transition:all 0.2s"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <p style="font-size:13px;color:var(--text2);margin-bottom:20px;line-height:1.6">
      Entrez votre adresse email. Vous recevrez un lien sécurisé pour réinitialiser votre mot de passe.
    </p>
    <div id="forgot-err" style="background:#FFF1F2;border:1px solid #FECDD3;color:#F43F5E;
      padding:12px 16px;border-radius:12px;font-size:13px;margin-bottom:16px;display:none;font-weight:500;"></div>
    <div id="forgot-ok" style="background:#ECFDF5;border:1px solid #A7F3D0;color:#059669;
      padding:12px 16px;border-radius:12px;font-size:13px;margin-bottom:16px;display:none;font-weight:500;"></div>
    <div style="margin-bottom:24px">
      <label style="display:block;font-size:12px;font-weight:600;color:var(--text2);
        margin-bottom:8px;">Email</label>
      <div class="iw">
        <i class="fa-solid fa-envelope ii"></i>
        <input type="email" id="forgot-email" placeholder="votre@email.com"
          onkeydown="if(event.key==='Enter')doForgot()"/>
      </div>
    </div>
    <button onclick="doForgot()" class="btn">Envoyer le lien <i class="fa-solid fa-paper-plane"></i></button>
  </div>
</div>
<script>
async function doLogin(){
  const email=document.getElementById("email").value.trim();
  const pwd=document.getElementById("pwd").value;
  const err=document.getElementById("err");
  const errText=document.getElementById("err-text");
  err.style.display="none";
  if(!email||!pwd){errText.textContent="Veuillez remplir tous les champs.";err.style.display="flex";return;}
  const res=await fetch("/api/login",{method:"POST",headers:{"Content-Type":"application/json"},
    body:JSON.stringify({email,mot_de_passe:pwd})});
  const data=await res.json();
  if(res.ok){window.location.href=data.role==="admin"?"/admin":"/dashboard";}
  else{errText.textContent=data.error||"Identifiants incorrects.";err.style.display="flex";}
}
if('serviceWorker' in navigator){
  navigator.serviceWorker.register('/sw.js', {scope:'/'})
    .then(()=>console.log('[PWA] Service Worker enregistré'))
    .catch(e=>console.log('[PWA] Erreur SW:', e));
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
  ok.innerHTML="<i class='fa-solid fa-circle-check'></i> Si cet email existe, vous recevrez un lien dans quelques minutes.";
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
<meta name="theme-color" content="#0B3D91">
<meta name="apple-mobile-web-app-capable" content="yes">
<link rel="manifest" href="/manifest.json">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
:root{
  --bg:#F5F7FA; --surface:#FFFFFF; --border:#E2E8F0;
  --primary-light:#4FC3F7; --primary-dark:#0B3D91; --primary-hover:#29B6F6;
  --grad:linear-gradient(135deg, #0B3D91, #4FC3F7);
  --green:#10B981; --red:#F43F5E;
  --text:#1E293B; --text2:#64748B; --text3:#94A3B8;
  --shadow-lg: 0 20px 25px -5px rgba(11, 61, 145, 0.1);
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Poppins',sans-serif;min-height:100vh;display:flex;align-items:center;
  justify-content:center;background:var(--bg);padding:16px;color:var(--text);}
.card{background:rgba(255,255,255,0.95);backdrop-filter:blur(20px);
  border:1px solid rgba(255,255,255,0.8);border-radius:24px;
  padding:48px 40px;width:100%;max-width:420px;
  box-shadow:var(--shadow-lg)}
@media(max-width:480px){.card{padding:32px 24px}}
.logo{text-align:center;margin-bottom:36px}
.logo-bg{width:64px;height:64px;border-radius:18px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:26px;color:#fff;
  margin:0 auto 16px;box-shadow:0 10px 25px rgba(79, 195, 247, 0.4);}
.logo h1{font-size:24px;font-weight:700;color:var(--primary-dark);}
.logo p{color:var(--text2);font-size:13px;margin-top:4px}
.fg{margin-bottom:20px}
.fg label{display:block;font-size:12px;font-weight:600;color:var(--text2);
  margin-bottom:8px;}
.iw{position:relative}
.ii{position:absolute;left:16px;top:50%;transform:translateY(-50%);font-size:15px;color:var(--text3);transition:color 0.3s;}
input{width:100%;height:48px;padding:0 16px 0 46px;background:#F8FAFC;
  border:1.5px solid var(--border);border-radius:14px;font-size:14px;
  font-family:'Poppins',sans-serif;color:var(--text);outline:none;transition:all 0.3s}
input:focus{border-color:var(--primary-light);background:#fff;box-shadow:0 0 0 4px rgba(79, 195, 247, 0.15);}
input:focus + .ii, .iw:focus-within .ii {color:var(--primary-dark);}
.btn{width:100%;height:48px;margin-top:8px;background:var(--grad);border:none;
  border-radius:14px;color:#fff;font-family:'Poppins',sans-serif;font-size:15px;
  font-weight:600;cursor:pointer;box-shadow:0 8px 20px rgba(11, 61, 145, 0.2);transition:all 0.3s;
  display:flex;align-items:center;justify-content:center;gap:10px;}
.btn:hover{transform:translateY(-2px);box-shadow:0 12px 25px rgba(11, 61, 145, 0.3);}
.err{background:#FFF1F2;border:1px solid #FECDD3;color:var(--red);
  padding:12px 16px;border-radius:12px;font-size:13px;margin-bottom:20px;display:none;font-weight:500;}
.ok{background:#ECFDF5;border:1px solid #A7F3D0;color:var(--green);
  padding:12px 16px;border-radius:12px;font-size:13px;margin-bottom:20px;display:none;font-weight:500;}
.exp{background:#FFFBEB;border:1px solid #FDE68A;color:#B45309;
  padding:24px;border-radius:16px;text-align:center;font-size:14px;display:none;font-weight:500;}
</style></head><body>
<div class="card">
  <div class="logo">
    <div class="logo-bg"><i class="fa-solid fa-shield-halved"></i></div>
    <h1>Nouveau mot de passe</h1>
    <p>Sécurisez l'accès à votre espace</p>
  </div>
  <div class="exp" id="exp">
    <div style="font-size:32px;margin-bottom:12px;color:#D97706;"><i class="fa-solid fa-clock-rotate-left"></i></div>
    <div style="font-weight:700;margin-bottom:8px;font-size:16px;">Lien expiré ou invalide</div>
    <div style="color:#92400E;font-size:13px;">Ce lien n'est plus valide. Veuillez faire une nouvelle demande de réinitialisation.</div>
  </div>
  <div id="form-wrap">
    <div class="err" id="err"></div>
    <div class="ok" id="ok"></div>
    <div class="fg">
      <label>Nouveau mot de passe</label>
      <div class="iw"><i class="fa-solid fa-lock ii"></i>
        <input type="password" id="pwd1" placeholder="Minimum 6 caractères"/></div>
    </div>
    <div class="fg">
      <label>Confirmer le mot de passe</label>
      <div class="iw"><i class="fa-solid fa-lock-open ii"></i>
        <input type="password" id="pwd2" placeholder="Répétez le mot de passe"
          onkeydown="if(event.key==='Enter')doReset()"/></div>
    </div>
    <button class="btn" onclick="doReset()">Enregistrer <i class="fa-solid fa-check"></i></button>
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
  if(!pwd1||!pwd2){err.innerHTML="<i class='fa-solid fa-circle-exclamation'></i> Veuillez remplir les deux champs.";err.style.display="block";return;}
  if(pwd1.length<6){err.innerHTML="<i class='fa-solid fa-circle-exclamation'></i> Le mot de passe doit faire au moins 6 caractères.";err.style.display="block";return;}
  if(pwd1!==pwd2){err.innerHTML="<i class='fa-solid fa-circle-exclamation'></i> Les mots de passe ne correspondent pas.";err.style.display="block";return;}
  const res=await fetch("/api/reset-password",{method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({token,mot_de_passe:pwd1})});
  const data=await res.json();
  if(res.ok){
    ok.innerHTML="<i class='fa-solid fa-circle-check'></i> Mot de passe modifié ! Redirection...";ok.style.display="block";
    document.getElementById("pwd1").value="";document.getElementById("pwd2").value="";
    setTimeout(()=>window.location.href="/",2500);
  }else{err.innerHTML="<i class='fa-solid fa-circle-exclamation'></i> "+(data.error||"Erreur.");err.style.display="block";}
}
init();
</script></body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE ADMIN
# ═════════════════════════════════════════════════════════════

ADMIN_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Admin Dashboard</title>
<meta name="theme-color" content="#0B3D91">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="GPS Tracker">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
:root{
  --bg:#F5F7FA; --surface:#FFFFFF; --surface2:#F8FAFC; --border:#E2E8F0;
  --primary:#4FC3F7; --primary-dark:#0B3D91; --primary-hover:#29B6F6;
  --grad:linear-gradient(135deg, #0B3D91, #4FC3F7);
  --grad-light:linear-gradient(135deg, rgba(79, 195, 247, 0.1), rgba(11, 61, 145, 0.05));
  --green:#10B981; --green-bg:rgba(16,185,129,0.1); --green-bd:rgba(16,185,129,0.2);
  --red:#EF4444; --red-bg:rgba(239,68,68,0.1); --red-bd:rgba(239,68,68,0.2);
  --amber:#F59E0B; --text:#1E293B; --text2:#475569; --text3:#94A3B8;
  --sidebar-w:260px;
  --radius-lg:16px; --radius-md:12px;
  --shadow-sm: 0 2px 4px rgba(11, 61, 145, 0.04);
  --shadow-md: 0 8px 16px rgba(11, 61, 145, 0.06);
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Poppins',sans-serif;background:var(--bg);color:var(--text);font-size:14px;display:flex;min-height:100vh}

/* ══ SIDEBAR ══ */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:var(--surface);border-right:1px solid var(--border);
  display:flex;flex-direction:column;z-index:100;overflow:hidden;
  transition:left 0.3s ease; box-shadow:var(--shadow-md);
}
.s-logo{padding:24px 20px;border-bottom:1px solid var(--border);position:relative}
.s-logo-row{display:flex;align-items:center;gap:14px}
.s-logo-icon{width:42px;height:42px;border-radius:12px;background:var(--grad);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:20px;
  box-shadow:0 4px 14px rgba(79, 195, 247, 0.3);flex-shrink:0}
.s-logo-name{font-size:16px;font-weight:700;color:var(--primary-dark);letter-spacing:-0.3px}
.s-logo-sub{font-size:11px;color:var(--text3);margin-top:2px;font-weight:500;}

.s-admin{margin:20px 16px;padding:14px;
  background:var(--surface2); border:1px solid var(--border); border-radius:var(--radius-md)}
.s-admin-row{display:flex;align-items:center;gap:12px}
.s-avatar{width:40px;height:40px;border-radius:10px;background:var(--grad-light);color:var(--primary-dark);
  display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0}
.s-admin-name{font-size:14px;font-weight:600;color:var(--text)}
.s-admin-role{font-size:11px;font-weight:600;color:var(--primary);text-transform:uppercase;letter-spacing:0.5px;}

.s-nav{flex:1;padding:0 16px;overflow-y:auto}
.nav-item{display:flex;align-items:center;gap:12px;padding:12px 16px;
  border-radius:var(--radius-md);cursor:pointer;color:var(--text2);font-size:14px;
  font-weight:500;transition:all 0.2s;margin-bottom:6px;position:relative}
.nav-item:hover{background:var(--surface2);color:var(--primary-dark)}
.nav-item.active{background:var(--primary-dark);color:#fff;font-weight:600;box-shadow:0 4px 12px rgba(11, 61, 145, 0.2);}
.nav-ico{font-size:16px;width:24px;text-align:center;flex-shrink:0;transition:all 0.2s;}

.s-bottom{padding:20px 16px;border-top:1px solid var(--border);background:var(--surface);flex-shrink:0}
.btn-logout{width:100%;padding:12px;background:var(--surface);color:var(--text2);
  border:1px solid var(--border);border-radius:var(--radius-md);cursor:pointer;font-size:14px;font-weight:600;
  font-family:'Poppins',sans-serif;transition:all 0.2s;
  display:flex;align-items:center;justify-content:center;gap:8px}
.btn-logout:hover{background:var(--red-bg);color:var(--red);border-color:var(--red-bd);}

/* ══ MAIN ══ */
.main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;min-width:0}
.topbar{position:sticky;top:0;z-index:50;height:70px;padding:0 32px;
  background:rgba(255,255,255,0.85);backdrop-filter:blur(16px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;}
.tb-left{display:flex;align-items:center;gap:12px}
.menu-btn{display:none;background:none;border:none;cursor:pointer;
  font-size:20px;color:var(--text);padding:8px;border-radius:8px;transition:background 0.2s;}
.menu-btn:hover{background:var(--surface2);}
.tb-crumb{font-size:13px;color:var(--text3);font-weight:500}
.tb-page-title{font-size:20px;font-weight:700;color:var(--primary-dark);letter-spacing:-0.5px}
.tb-right{display:flex;align-items:center;gap:16px}
.clock{padding:8px 16px;background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius-md);font-size:13px;color:var(--primary-dark);font-weight:600;
  box-shadow:var(--shadow-sm); display:flex; align-items:center; gap:8px;}

.content{padding:32px;flex:1}
.section{display:none}
.section.active{display:block;animation:fadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1)}
@keyframes fadeInUp{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}

/* ── Stats Modernes ── */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-bottom:32px}
.stat{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);
  padding:28px;position:relative;overflow:hidden;transition:all 0.3s;box-shadow:var(--shadow-sm);}
.stat:hover{border-color:var(--primary-light);box-shadow:var(--shadow-md);transform:translateY(-3px)}
.stat-top{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:20px}
.stat-icon{width:52px;height:52px;border-radius:14px;background:var(--grad-light);color:var(--primary-dark);
  display:flex;align-items:center;justify-content:center;font-size:24px;}
.stat-trend{font-size:12px;font-weight:600;padding:4px 12px;border-radius:20px;
  background:var(--green-bg);color:var(--green);}
.stat-val{font-size:38px;font-weight:700;color:var(--primary-dark);letter-spacing:-1px;line-height:1}
.stat-lbl{font-size:14px;color:var(--text2);margin-top:8px;font-weight:500}

/* ── Section header ── */
.sh{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px;flex-wrap:wrap;gap:16px}
.sh h2{font-size:22px;font-weight:700;color:var(--primary-dark);}
.sh-sub{font-size:14px;color:var(--text3);margin-top:4px}

/* ── Boutons ── */
.btn{height:44px;padding:0 20px;border:none;border-radius:var(--radius-md);cursor:pointer;
  font-size:14px;font-weight:600;font-family:'Poppins',sans-serif;
  transition:all 0.3s;display:inline-flex;align-items:center;gap:8px;}
.btn-primary{background:var(--grad);color:#fff;box-shadow:0 4px 12px rgba(79, 195, 247, 0.3)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 6px 16px rgba(79, 195, 247, 0.4)}
.btn-danger{background:var(--surface);color:var(--red);border:1px solid var(--border);}
.btn-danger:hover{background:var(--red-bg); border-color:var(--red-bd);}
.btn-success{background:var(--surface);color:var(--green);border:1px solid var(--border);}
.btn-success:hover{background:var(--green-bg); border-color:var(--green-bd);}
.btn-sm{height:34px;padding:0 14px;font-size:12px;border-radius:8px}

/* ── Table SaaS ── */
.table-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);overflow:hidden;
  box-shadow:var(--shadow-sm);}
.table-wrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;min-width:700px}
thead{background:var(--surface2); border-bottom:2px solid var(--border);}
th{padding:16px 24px;text-align:left;font-size:12px;color:var(--text2);
  font-weight:600;text-transform:uppercase;letter-spacing:0.5px;}
tbody tr{transition:background 0.2s; border-bottom:1px solid var(--border);}
tbody tr:hover{background:var(--surface2);}
td{padding:18px 24px;font-size:14px;color:var(--text);}
tbody tr:last-child{border-bottom:none}
.td-main{font-weight:600;color:var(--primary-dark);}
.device{font-size:12px;background:var(--grad-light);color:var(--primary-dark);
  padding:4px 10px;border-radius:6px;font-weight:600;font-family:monospace; border:1px solid var(--border);}
.badge{padding:6px 14px;border-radius:20px;font-size:12px;font-weight:600;
  display:inline-flex;align-items:center;gap:6px}
.badge::before{content:'\\f111'; font-family:'Font Awesome 6 Free'; font-weight:900; font-size:8px;}
.badge-on{background:var(--green-bg);color:var(--green);}
.badge-off{background:var(--red-bg);color:var(--red);}

/* ── Empty ── */
.empty{padding:60px 20px;text-align:center}
.empty-ico{font-size:50px;margin-bottom:16px;color:var(--border)}
.empty-img{width:140px;height:140px;object-fit:cover;border-radius:50%;margin:0 auto 20px;
  display:block;box-shadow:var(--shadow-md);border:4px solid var(--surface);}
.empty-txt{font-size:16px;font-weight:600;color:var(--text2)}
.empty-sub{font-size:13px;color:var(--text3);margin-top:6px}
.veh-thumb{width:44px;height:44px;border-radius:12px;object-fit:cover;flex-shrink:0;
  box-shadow:var(--shadow-sm);border:1px solid var(--border);}

/* ── Véhicules regroupés par propriétaire (accordéon) ── */
.veh-search{margin-bottom:20px}
.owner-group{border:1px solid var(--border);border-radius:var(--radius-lg);background:var(--surface);
  margin-bottom:14px;overflow:hidden;box-shadow:var(--shadow-sm);transition:box-shadow 0.2s;}
.owner-group.hl{border-color:var(--primary-light);box-shadow:0 0 0 3px rgba(79,195,247,0.15)}
.owner-header{display:flex;align-items:center;justify-content:space-between;padding:18px 24px;
  cursor:pointer;transition:background 0.2s;user-select:none}
.owner-header:hover{background:var(--surface2)}
.owner-header-left{display:flex;align-items:center;gap:14px}
.owner-avatar{width:44px;height:44px;border-radius:12px;background:var(--grad-light);color:var(--primary-dark);
  display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0}
.owner-name{font-size:15px;font-weight:700;color:var(--text)}
.owner-count{font-size:12px;color:var(--text3);margin-top:2px;font-weight:500}
.owner-chevron{font-size:14px;color:var(--text3);transition:transform 0.25s}
.owner-group.open .owner-chevron{transform:rotate(180deg)}
.owner-body{max-height:0;overflow:hidden;transition:max-height 0.35s ease}
.owner-group.open .owner-body{max-height:3000px}
.owner-body-inner{padding:4px 24px 22px;display:grid;
  grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:14px;border-top:1px solid var(--border);padding-top:18px}
.veh-mini-card{background:var(--surface2);border:1px solid var(--border);border-radius:14px;padding:16px;transition:all 0.2s}
.veh-mini-card:hover{border-color:var(--primary-light);box-shadow:var(--shadow-sm)}
.veh-mini-top{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}
.veh-mini-immat{font-size:14px;font-weight:700;color:var(--primary-dark)}
.veh-mini-model{font-size:12px;color:var(--text2);margin-top:2px}
.veh-mini-driver{font-size:12px;color:var(--text2);margin-top:10px;display:flex;align-items:center;gap:6px}
.veh-mini-driver i{color:var(--text3);width:12px}
.veh-mini-device{font-size:11px;color:var(--text3);margin-top:6px;font-family:monospace}
.veh-mini-actions{display:flex;gap:6px;margin-top:12px}
.veh-mini-actions .btn-sm{flex:1;justify-content:center}

/* ── Historique & Params ── */
.h-filters{display:flex;gap:12px;margin-bottom:24px;align-items:center;flex-wrap:wrap}
.h-select{height:44px;padding:0 16px;background:var(--surface);border:1px solid var(--border);
  border-radius:var(--radius-md);font-size:14px;font-family:'Poppins',sans-serif;color:var(--text);
  outline:none;transition:all 0.3s; box-shadow:var(--shadow-sm);}
.h-select:focus{border-color:var(--primary-light);box-shadow:0 0 0 3px rgba(79, 195, 247, 0.15)}

.param-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-lg);
  padding:28px;margin-bottom:24px; box-shadow:var(--shadow-sm);}
.param-title{font-size:16px;font-weight:700;color:var(--primary-dark);margin-bottom:4px}
.param-sub{font-size:13px;color:var(--text3);margin-bottom:20px}
.param-row{display:flex;justify-content:space-between;align-items:center;
  padding:16px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:12px}
.param-row:last-child{border-bottom:none;padding-bottom:0}
.p-lbl{font-size:14px;font-weight:600;color:var(--text)}
.p-desc{font-size:12px;color:var(--text3);margin-top:4px}
.p-badge{font-size:12px;font-weight:600;padding:6px 14px;border-radius:20px; background:var(--surface2); color:var(--text2); border:1px solid var(--border);}

/* ── Modal Glassmorphism ── */
.mbg{display:none;position:fixed;inset:0;background:rgba(15, 23, 42, 0.5);
  backdrop-filter:blur(6px);z-index:200;align-items:center;justify-content:center;padding:16px}
.mbg.open{display:flex;animation:fadeIn 0.2s ease}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
.modal{background:var(--surface);border:1px solid rgba(255,255,255,0.8);border-radius:24px;
  padding:36px;width:100%;max-width:550px;max-height:90vh;overflow-y:auto;
  box-shadow:var(--shadow-lg);animation:slideUp 0.3s cubic-bezier(0.16, 1, 0.3, 1);position:relative}
@keyframes slideUp{from{opacity:0;transform:translateY(20px) scale(0.98)}to{opacity:1;transform:translateY(0) scale(1)}}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:28px}
.mh h3{font-size:20px;font-weight:700;color:var(--primary-dark);}
.mc{width:36px;height:36px;border-radius:10px;border:1px solid var(--border);
  background:var(--surface2);cursor:pointer;font-size:16px;color:var(--text2);
  display:flex;align-items:center;justify-content:center;transition:all 0.2s}
.mc:hover{background:var(--border); color:var(--text);}
.fg{margin-bottom:20px}
.fg label{display:block;font-size:12px;font-weight:600;color:var(--text2);margin-bottom:8px;}
.fg input,.fg select{width:100%;height:46px;padding:0 16px;
  background:#F8FAFC;border:1px solid var(--border);
  border-radius:12px;font-size:14px;font-family:'Poppins',sans-serif;
  color:var(--text);outline:none;transition:all 0.3s;}
.fg input:focus,.fg select:focus{border-color:var(--primary-light);background:#fff;
  box-shadow:0 0 0 3px rgba(79, 195, 247, 0.15)}
.fg2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.ma{display:flex;gap:12px;margin-top:32px;padding-top:24px;border-top:1px solid var(--border)}
.ma .btn{flex:1;justify-content:center;}
.al{padding:14px 16px;border-radius:12px;font-size:13px;font-weight:500;margin-bottom:20px;display:none; align-items:center; gap:8px;}
.al-e{background:var(--red-bg);border:1px solid var(--red-bd);color:var(--red)}
.al-o{background:var(--green-bg);border:1px solid var(--green-bd);color:var(--green)}

/* Overlay mobile */
.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.4);z-index:99; backdrop-filter:blur(4px);}
.overlay.open{display:block}

/* ══ RESPONSIVE MOBILE ══ */
@media(max-width:768px){
  .sidebar{left:calc(-1 * var(--sidebar-w));}
  .sidebar.open{left:0;}
  .main{margin-left:0!important}
  .menu-btn{display:inline-flex;}
  .topbar{padding:0 16px; height:60px;}
  .tb-page-title{font-size:18px}
  .content{padding:16px}
  .stats{grid-template-columns:1fr!important; gap:16px;}
  .fg2{grid-template-columns:1fr!important}
  .h-filters{flex-direction:column;align-items:stretch}
  .modal{padding:24px 20px}
}
</style></head><body>

<div class="overlay" id="overlay" onclick="closeMenu()"></div>

<div class="sidebar" id="sidebar">
  <div class="s-logo">
    <div class="s-logo-row">
      <div class="s-logo-icon"><i class="fa-solid fa-earth-americas"></i></div>
      <div>
        <div class="s-logo-name">GPS Tracker</div>
        <div class="s-logo-sub">Command Center</div>
      </div>
    </div>
  </div>
  <div class="s-admin">
    <div class="s-admin-row">
      <div class="s-avatar"><i class="fa-solid fa-user-shield"></i></div>
      <div>
        <div class="s-admin-name">Administrateur</div>
        <div class="s-admin-role">Accès total</div>
      </div>
    </div>
  </div>
  <div class="s-nav">
    <div class="nav-item active" onclick="show('dashboard',this)">
      <i class="fa-solid fa-chart-pie nav-ico"></i> Tableau de bord
    </div>
    <div class="nav-item" onclick="show('proprietaires',this)">
      <i class="fa-solid fa-users nav-ico"></i> Propriétaires
    </div>
    <div class="nav-item" onclick="show('vehicules',this)">
      <i class="fa-solid fa-car nav-ico"></i> Véhicules
    </div>
    <div class="nav-item" onclick="show('historique',this)">
      <i class="fa-solid fa-map-location-dot nav-ico"></i> Historique GPS
    </div>
    <div class="nav-item" onclick="show('alertes',this)" style="justify-content:space-between">
      <span><i class="fa-solid fa-triangle-exclamation nav-ico"></i> Alertes Système</span>
      <span id="nav-alert-badge" style="display:none;background:var(--red);color:#fff;font-size:11px;
        font-weight:700;padding:2px 8px;border-radius:20px;">0</span>
    </div>
    <div class="nav-item" onclick="show('parametres',this)">
      <i class="fa-solid fa-sliders nav-ico"></i> Paramètres
    </div>
  </div>
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()"><i class="fa-solid fa-arrow-right-from-bracket"></i> Déconnexion</button>
  </div>
</div>

<div class="main">
  <div class="topbar">
    <div class="tb-left">
      <button class="menu-btn" onclick="toggleMenu()"><i class="fa-solid fa-bars"></i></button>
      <div style="display:flex;flex-direction:column;">
        <span class="tb-crumb">Espace Admin</span>
        <span class="tb-page-title" id="page-title">Tableau de bord</span>
      </div>
    </div>
    <div class="tb-right">
      <div class="clock"><i class="fa-regular fa-clock"></i> <span id="clk">--:--:--</span></div>
    </div>
  </div>

  <div class="content">

    <div class="section active" id="s-dashboard">
      <div class="stats">
        <div class="stat">
          <div class="stat-top">
            <div class="stat-icon"><i class="fa-solid fa-users"></i></div>
            <span class="stat-trend"><i class="fa-solid fa-arrow-trend-up"></i> Total</span>
          </div>
          <div class="stat-val" id="stp">—</div>
          <div class="stat-lbl">Propriétaires enregistrés</div>
        </div>
        <div class="stat">
          <div class="stat-top">
            <div class="stat-icon"><i class="fa-solid fa-car-side"></i></div>
            <span class="stat-trend"><i class="fa-solid fa-signal"></i> Actifs</span>
          </div>
          <div class="stat-val" id="stv">—</div>
          <div class="stat-lbl">Véhicules suivis</div>
        </div>
        <div class="stat">
          <div class="stat-top">
            <div class="stat-icon"><i class="fa-solid fa-satellite-dish"></i></div>
            <span class="stat-trend"><i class="fa-solid fa-bolt"></i> Live</span>
          </div>
          <div class="stat-val">24/7</div>
          <div class="stat-lbl">Surveillance réseau</div>
        </div>
      </div>
      <div class="table-card" style="padding:0; overflow:hidden; position:relative; min-height:240px; display:flex; align-items:center;">
        <img src="https://images.unsplash.com/photo-1520594923568-1b5d82587f86?auto=format&fit=crop&w=1400&q=70" alt="Réseau routier"
          style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;"/>
        <div style="position:absolute;inset:0;background:linear-gradient(90deg, rgba(255,255,255,0.96) 0%, rgba(255,255,255,0.82) 42%, rgba(255,255,255,0.25) 100%);"></div>
        <div style="position:relative; padding:40px; max-width:560px;">
          <h3 style="font-size:22px; color:var(--primary-dark); margin-bottom:10px; font-weight:700;">Bienvenue sur le Centre de Contrôle</h3>
          <p style="font-size:14px;color:var(--text2);line-height:1.6;">
            Gérez votre flotte avec précision. Utilisez le menu latéral pour ajouter des clients, assigner des traceurs GPS, et analyser les données de déplacement.
          </p>
        </div>
      </div>
    </div>

    <div class="section" id="s-proprietaires">
      <div class="stats" id="prop-pos" style="margin-bottom:24px;">
        <div class="stat" style="padding:20px;">
          <div style="font-size:24px; color:var(--primary-dark); margin-bottom:10px;"><i class="fa-solid fa-users"></i></div>
          <div class="stat-val" id="pp-total" style="font-size:28px;">—</div>
          <div class="stat-lbl" style="margin-top:4px;">Total propriétaires</div>
        </div>
        <div class="stat" style="padding:20px;">
          <div style="font-size:24px; color:var(--green); margin-bottom:10px;"><i class="fa-solid fa-user-check"></i></div>
          <div class="stat-val" id="pp-actif" style="font-size:28px;">—</div>
          <div class="stat-lbl" style="margin-top:4px;">Comptes actifs</div>
        </div>
        <div class="stat" style="padding:20px;">
          <div style="font-size:24px; color:var(--primary-light); margin-bottom:10px;"><i class="fa-solid fa-car"></i></div>
          <div class="stat-val" id="pp-vehs" style="font-size:28px;">—</div>
          <div class="stat-lbl" style="margin-top:4px;">Véhicules associés</div>
        </div>
      </div>
      <div class="sh">
        <div>
          <h2>Propriétaires</h2>
          <div class="sh-sub">Gestion des comptes clients</div>
        </div>
        <button class="btn btn-primary" onclick="openMP()"><i class="fa-solid fa-plus"></i> Nouveau</button>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>Nom complet</th><th>Email</th><th>Téléphone</th>
              <th>Véhicules</th><th>Depuis</th><th>Statut</th><th style="min-width:260px">Actions</th>
            </tr></thead>
            <tbody id="tbp">
              <tr><td colspan="7"><div class="empty"><i class="fa-solid fa-users empty-ico"></i>
                <div class="empty-txt">Chargement des données...</div></div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="section" id="s-vehicules">
      <div class="sh">
        <div>
          <h2>Flotte de Véhicules</h2>
          <div class="sh-sub">Gérez les traceurs GPS et assignations, regroupés par propriétaire</div>
        </div>
        <button class="btn btn-primary" onclick="openMV()"><i class="fa-solid fa-plus"></i> Nouveau</button>
      </div>
      <div class="veh-search">
        <div class="iw" style="max-width:420px">
          <i class="fa-solid fa-magnifying-glass ii"></i>
          <input id="veh-search-input" placeholder="Rechercher (immatriculation, propriétaire, conducteur...)" oninput="renderVehiculesGroupes()"/>
        </div>
      </div>
      <div id="veh-groups">
        <div class="empty"><i class="fa-solid fa-car empty-ico"></i>
          <div class="empty-txt">Chargement des données...</div></div>
      </div>
    </div>

    <div class="section" id="s-historique">
      <div class="sh">
        <div>
          <h2>Historique de Tracking</h2>
          <div class="sh-sub">Analysez les trajets enregistrés</div>
        </div>
      </div>
      <div class="h-filters">
        <select class="h-select" id="hv" onchange="loadHist()" style="min-width:250px;">
          <option value="">Sélectionnez un véhicule...</option>
        </select>
        <select class="h-select" id="hl" onchange="loadHist()">
          <option value="50">50 dernières positions</option>
          <option value="100">100 dernières positions</option>
          <option value="200">200 dernières positions</option>
        </select>
      </div>
      <div class="stats" id="hstats" style="display:none; grid-template-columns:repeat(4,1fr); gap:16px;">
        <div class="stat" style="padding:16px;"><div class="stat-val" id="hs1" style="font-size:24px;">0</div><div class="stat-lbl" style="font-size:12px;margin-top:2px;">Points</div></div>
        <div class="stat" style="padding:16px;"><div class="stat-val" id="hs2" style="font-size:24px;">0</div><div class="stat-lbl" style="font-size:12px;margin-top:2px;">Vmax (km/h)</div></div>
        <div class="stat" style="padding:16px;"><div class="stat-val" id="hs3" style="font-size:24px;">0</div><div class="stat-lbl" style="font-size:12px;margin-top:2px;">Vmoy (km/h)</div></div>
        <div class="stat" style="padding:16px;"><div class="stat-val" id="hs4" style="font-size:24px;">0</div><div class="stat-lbl" style="font-size:12px;margin-top:2px;">Satellites moy.</div></div>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>#</th><th>Horodatage</th><th>Latitude</th>
              <th>Longitude</th><th>Vitesse</th><th>Signal</th>
            </tr></thead>
            <tbody id="tbh">
              <tr><td colspan="6"><div class="empty">
                <i class="fa-solid fa-map-location-dot empty-ico"></i>
                <div class="empty-txt">Sélectionnez un véhicule</div>
                <div class="empty-sub">pour afficher l'historique des trajets</div>
              </div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="section" id="s-alertes">
      <div class="sh">
        <div>
          <h2>Alertes Système</h2>
          <div class="sh-sub">Supervision de la connectivité et de l'infrastructure IoT</div>
        </div>
        <button class="btn btn-danger" onclick="loadAlertes()"><i class="fa-solid fa-arrows-rotate"></i> Actualiser</button>
      </div>

      <div class="stats" style="grid-template-columns:repeat(2,1fr);margin-bottom:32px">
        <div class="stat" style="border-top:4px solid var(--red)">
          <div class="stat-top">
            <div class="stat-icon" style="background:var(--red-bg);color:var(--red)"><i class="fa-solid fa-satellite-dish"></i></div>
            <span class="stat-trend" style="background:var(--red-bg);color:var(--red)"><i class="fa-solid fa-triangle-exclamation"></i> Actif</span>
          </div>
          <div class="stat-val" id="al-signal-count" style="color:var(--red)">—</div>
          <div class="stat-lbl">Véhicules hors ligne / panne technique</div>
        </div>
        <div class="stat" style="border-top:4px solid var(--amber)">
          <div class="stat-top">
            <div class="stat-icon" style="background:rgba(245,158,11,0.1);color:var(--amber)"><i class="fa-solid fa-sim-card"></i></div>
            <span class="stat-trend" style="background:rgba(245,158,11,0.1);color:var(--amber)"><i class="fa-solid fa-triangle-exclamation"></i> Actif</span>
          </div>
          <div class="stat-val" id="al-sim-count" style="color:var(--amber)">—</div>
          <div class="stat-lbl">Puces SIM800L sous 100 Mo</div>
        </div>
      </div>

      <div class="sh">
        <div>
          <h2 style="font-size:18px">Perte de signal &amp; pannes techniques</h2>
          <div class="sh-sub">Véhicules dont le traceur n'a plus émis de position récente</div>
        </div>
      </div>
      <div class="table-card" style="margin-bottom:32px">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>Immatriculation</th><th>Device ID</th><th>Propriétaire</th>
              <th>Dernière position</th><th>Hors ligne depuis</th><th>Statut</th>
            </tr></thead>
            <tbody id="tb-al-signal">
              <tr><td colspan="6"><div class="empty"><i class="fa-solid fa-satellite-dish empty-ico"></i>
                <div class="empty-txt">Chargement...</div></div></td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="sh">
        <div>
          <h2 style="font-size:18px">Recharge de données — Puces SIM800L</h2>
          <div class="sh-sub">Traceurs dont le forfait data descend sous le seuil critique (100 Mo)</div>
        </div>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>Device ID</th><th>Véhicule</th><th>Propriétaire</th>
              <th>Data restante</th><th>Seuil</th><th>Action</th>
            </tr></thead>
            <tbody id="tb-al-sim">
              <tr><td colspan="6"><div class="empty"><i class="fa-solid fa-sim-card empty-ico"></i>
                <div class="empty-txt">Chargement...</div></div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <div class="section" id="s-parametres">
      <div class="sh">
        <div>
          <h2>Paramètres Système</h2>
          <div class="sh-sub">Configuration globale du GPS Tracker</div>
        </div>
      </div>
      <div class="param-card">
        <div class="param-title">Compte Super Administrateur</div>
        <div class="param-sub">Identité de gestion</div>
        <div class="param-row">
          <div><div class="p-lbl">Email principal</div><div class="p-desc">admin@gps.com</div></div>
          <span class="p-badge" style="background:var(--grad-light); color:var(--primary-dark);"><i class="fa-solid fa-shield-halved"></i> Root Access</span>
        </div>
      </div>
      <div class="param-card">
        <div class="param-title">Infrastructure IoT</div>
        <div class="param-sub">État des connexions serveurs</div>
        <div class="param-row">
          <div><div class="p-lbl">Endpoint ESP32</div><div class="p-desc">POST /api/position</div></div>
          <span class="p-badge" style="background:var(--green-bg);color:var(--green);"><i class="fa-solid fa-circle-check"></i> Actif</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Stockage Data</div><div class="p-desc">SQLite Relational DB</div></div>
          <span class="p-badge" style="background:var(--green-bg);color:var(--green);"><i class="fa-solid fa-database"></i> Connecté</span>
        </div>
      </div>
    </div>

  </div>
</div>

<div class="mbg" id="mp">
  <div class="modal">
    <div class="mh">
      <h3>Ajouter un client</h3>
      <button class="mc" onclick="closeM('mp')"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <div class="al al-e" id="ep"><i class="fa-solid fa-circle-exclamation"></i> <span id="ep-t"></span></div>
    <div class="al al-o" id="op"><i class="fa-solid fa-circle-check"></i> <span id="op-t"></span></div>
    <div class="fg2">
      <div class="fg"><label>Nom *</label><input id="pn" placeholder="Nom"/></div>
      <div class="fg"><label>Prénom *</label><input id="pp" placeholder="Prénom"/></div>
    </div>
    <div class="fg"><label>Email *</label><input type="email" id="pe" placeholder="client@email.com"/></div>
    <div class="fg"><label>Téléphone *</label><input id="p-tel" placeholder="+33 6 ..."/></div>
    <div class="fg"><label>Mot de passe *</label><input type="password" id="pw" placeholder="Minimum 6 caractères"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('mp')">Annuler</button>
      <button class="btn btn-primary" onclick="creerP()"><i class="fa-solid fa-check"></i> Créer le compte</button>
    </div>
  </div>
</div>

<div class="mbg" id="mv">
  <div class="modal">
    <div class="mh">
      <h3>Assigner un véhicule</h3>
      <button class="mc" onclick="closeM('mv')"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <div class="al al-e" id="ev"><i class="fa-solid fa-circle-exclamation"></i> <span id="ev-t"></span></div>
    <div class="al al-o" id="ov"><i class="fa-solid fa-circle-check"></i> <span id="ov-t"></span></div>
    <div class="fg"><label>Propriétaire *</label><select id="vp"></select></div>
    <div class="fg2">
      <div class="fg"><label>Marque *</label><input id="vm" placeholder="Peugeot"/></div>
      <div class="fg"><label>Modèle *</label><input id="vmo" placeholder="3008"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Type *</label>
        <select id="vt">
          <option value="voiture">Voiture</option>
          <option value="moto">Moto</option>
          <option value="camion">Camion</option>
          <option value="bus">Bus</option>
          <option value="autre">Autre</option>
        </select>
      </div>
      <div class="fg"><label>Couleur</label><input id="vc" placeholder="Noir"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Immatriculation *</label><input id="vi" placeholder="AB-123-CD"/></div>
      <div class="fg"><label>Année</label><input type="number" id="va" placeholder="2023"/></div>
    </div>
    <div class="fg"><label>Device ID (Tracker ESP32) *</label><input id="vd" placeholder="Identifiant unique"/>
    </div>
    <div class="fg"><label>Nom complet du conducteur <span style="font-weight:400;color:var(--text3)">(optionnel)</span></label>
      <input id="v-conducteur" placeholder="Ousmane Ndiaye"/>
    </div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('mv')">Annuler</button>
      <button class="btn btn-primary" onclick="creerV()"><i class="fa-solid fa-check"></i> Assigner</button>
    </div>
  </div>
</div>

<script>
const T={dashboard:"Tableau de bord",proprietaires:"Propriétaires",vehicules:"Flotte de Véhicules",
  historique:"Historique de Tracking",alertes:"Alertes Système",parametres:"Paramètres Système"};

/* Vraies photos par type de véhicule (au lieu d'icônes génériques) */
const VEH_IMAGES={
  voiture:"https://images.unsplash.com/photo-1492967396498-f79507b65e89?auto=format&fit=crop&w=120&h=120&q=70",
  moto:"https://images.unsplash.com/photo-1591637333184-19aa84b3e01f?auto=format&fit=crop&w=120&h=120&q=70",
  camion:"https://images.unsplash.com/photo-1616432043562-3671ea2e5242?auto=format&fit=crop&w=120&h=120&q=70",
  bus:"https://images.unsplash.com/photo-1514355453671-d0164a278218?auto=format&fit=crop&w=120&h=120&q=70",
  autre:"https://images.unsplash.com/photo-1492967396498-f79507b65e89?auto=format&fit=crop&w=120&h=120&q=70"
};
function vehiculeImage(type){return VEH_IMAGES[type]||VEH_IMAGES.autre;}

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
  if(n==="alertes")loadAlertes();
}

async function loadStats(){
  const[p,v]=await Promise.all([
    fetch("/api/admin/proprietaires").then(r=>r.json()),
    fetch("/api/admin/vehicules").then(r=>r.json())]);
  document.getElementById("stp").textContent=p.length||0;
  document.getElementById("stv").textContent=v.filter(x=>x.actif).length||0;
}

/* ── Alertes Système : perte de signal / panne technique + quota SIM800L ── */
async function loadAlertes(){
  await Promise.all([loadAlertesSignal(), loadAlertesSim()]);
  refreshNavAlertBadge();
}

async function loadAlertesSignal(){
  const tb=document.getElementById("tb-al-signal");
  try{
    const data=await fetch("/api/admin/alertes/signal").then(r=>{
      if(!r.ok)throw new Error("indisponible");
      return r.json();
    });
    document.getElementById("al-signal-count").textContent=data.length;
    if(!data.length){
      tb.innerHTML='<tr><td colspan="6"><div class="empty"><img class="empty-img" src="https://images.unsplash.com/photo-1520594923568-1b5d82587f86?auto=format&fit=crop&w=300&h=300&q=70" alt=""><div class="empty-txt">Aucune alerte — tous les traceurs émettent normalement</div></div></td></tr>';
      return;
    }
    tb.innerHTML=data.map(v=>`<tr>
      <td class="td-main">${v.immatriculation}</td>
      <td><span class="device"><i class="fa-solid fa-microchip" style="margin-right:4px;"></i>${v.device_id}</span></td>
      <td><i class="fa-regular fa-user" style="color:var(--text3);margin-right:6px"></i>${v.proprietaire_nom||"—"}</td>
      <td style="font-size:13px;color:var(--text2)">${v.derniere_position||"Aucune donnée"}</td>
      <td><span style="font-weight:600;color:var(--red)">${v.minutes_hors_ligne!=null?Math.round(v.minutes_hors_ligne)+" min":"—"}</span></td>
      <td><span class="badge badge-off"><i class="fa-solid fa-satellite-dish"></i> Hors ligne</span></td>
    </tr>`).join("");
  }catch(e){
    document.getElementById("al-signal-count").textContent="0";
    tb.innerHTML='<tr><td colspan="6"><div class="empty"><i class="fa-solid fa-satellite-dish empty-ico"></i><div class="empty-txt">Aucune donnée disponible</div><div class="empty-sub">Ce module nécessite l\\'endpoint /api/admin/alertes/signal côté serveur</div></div></td></tr>';
  }
}

async function loadAlertesSim(){
  const tb=document.getElementById("tb-al-sim");
  try{
    const data=await fetch("/api/admin/alertes/sim-data").then(r=>{
      if(!r.ok)throw new Error("indisponible");
      return r.json();
    });
    document.getElementById("al-sim-count").textContent=data.length;
    if(!data.length){
      tb.innerHTML='<tr><td colspan="6"><div class="empty"><img class="empty-img" src="https://images.unsplash.com/photo-1520594923568-1b5d82587f86?auto=format&fit=crop&w=300&h=300&q=70" alt=""><div class="empty-txt">Toutes les puces ont un quota data suffisant</div></div></td></tr>';
      return;
    }
    tb.innerHTML=data.map(v=>`<tr>
      <td><span class="device"><i class="fa-solid fa-microchip" style="margin-right:4px;"></i>${v.device_id}</span></td>
      <td class="td-main">${v.immatriculation}</td>
      <td><i class="fa-regular fa-user" style="color:var(--text3);margin-right:6px"></i>${v.proprietaire_nom||"—"}</td>
      <td><span style="font-weight:700;color:${v.data_restante_mo<20?'var(--red)':'var(--amber)'}">${v.data_restante_mo} Mo</span></td>
      <td style="color:var(--text3);font-size:13px">${v.seuil_mo||100} Mo</td>
      <td><button class="btn btn-sm btn-primary" onclick="rechargerSim(${v.id})"><i class="fa-solid fa-bolt"></i> Recharger</button></td>
    </tr>`).join("");
  }catch(e){
    document.getElementById("al-sim-count").textContent="0";
    tb.innerHTML='<tr><td colspan="6"><div class="empty"><i class="fa-solid fa-sim-card empty-ico"></i><div class="empty-txt">Aucune donnée disponible</div><div class="empty-sub">Ce module nécessite l\\'endpoint /api/admin/alertes/sim-data côté serveur</div></div></td></tr>';
  }
}

async function rechargerSim(vehiculeId){
  try{
    const res=await fetch(`/api/admin/vehicules/${vehiculeId}/recharger-sim`,{method:"POST"});
    if(!res.ok)throw new Error();
    loadAlertes();
  }catch(e){
    alert("Impossible de confirmer la recharge — endpoint serveur non disponible pour le moment.");
  }
}

async function refreshNavAlertBadge(){
  const s=parseInt(document.getElementById("al-signal-count").textContent)||0;
  const d=parseInt(document.getElementById("al-sim-count").textContent)||0;
  const total=s+d;
  const badge=document.getElementById("nav-alert-badge");
  if(!badge)return;
  if(total>0){badge.style.display="inline-block";badge.textContent=total;}
  else badge.style.display="none";
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
    tb.innerHTML='<tr><td colspan="7"><div class="empty"><img class="empty-img" src="https://images.unsplash.com/photo-1520594923568-1b5d82587f86?auto=format&fit=crop&w=300&h=300&q=70" alt=""><div class="empty-txt">Aucun client trouvé</div></div></td></tr>';
    return;
  }
  tb.innerHTML=data.map(p=>`<tr>
    <td class="td-main">${p.prenom} ${p.nom}</td>
    <td><i class="fa-regular fa-envelope" style="color:var(--text3);margin-right:6px"></i>${p.email}</td>
    <td>${p.telephone||"—"}</td>
    <td><span onclick="ouvrirVehiculesDe(${p.id},'${p.prenom} ${p.nom}')" style="cursor:pointer;font-weight:600; padding:4px 12px; border-radius:20px; background:var(--surface2); border:1px solid var(--border); transition:all 0.2s;" onmouseover="this.style.borderColor='var(--primary-light)'" onmouseout="this.style.borderColor='var(--border)'">${p.nb_vehicules} <i class="fa-solid fa-car" style="color:var(--primary);margin-left:4px;"></i></span></td>
    <td style="font-size:12px;color:var(--text3)">${(p.date_creation||"").slice(0,10)}</td>
    <td><span class="badge ${p.actif?'badge-on':'badge-off'}">${p.actif?'Actif':'Inactif'}</span></td>
    <td style="white-space:nowrap"><div style="display:flex;gap:8px;align-items:center">
    <button class="btn btn-sm" style="background:var(--surface); color:var(--primary-dark); border:1px solid var(--border);" onclick="ouvrirVehiculesDe(${p.id},'${p.prenom} ${p.nom}')" title="Voir ses véhicules"><i class="fa-solid fa-car"></i></button>
    <button class="btn btn-sm ${p.actif?'btn-danger':'btn-success'}" onclick="toggleP(${p.id})"><i class="fa-solid fa-power-off"></i></button>
    <button class="btn btn-sm btn-primary" style="background:var(--surface2); color:var(--primary-dark); border:1px solid var(--border); box-shadow:none;" onclick="ouvrirModifP(${p.id})"><i class="fa-solid fa-pen"></i></button>
    <button class="btn btn-sm btn-danger" onclick="confirmerSuppressionP(${p.id},'${p.prenom} ${p.nom}')"><i class="fa-solid fa-trash"></i></button>
    </div></td>
  </tr>`).join("");
}

async function creerP(){
  const e=document.getElementById("ep"),o=document.getElementById("op");
  const et=document.getElementById("ep-t"),ot=document.getElementById("op-t");
  e.style.display=o.style.display="none";
  const body={
    nom:document.getElementById("pn").value.trim(),
    prenom:document.getElementById("pp").value.trim(),
    email:document.getElementById("pe").value.trim(),
    telephone:document.getElementById("p-tel").value.trim(),
    mot_de_passe:document.getElementById("pw").value
  };
  if(!body.nom||!body.prenom||!body.email||!body.telephone||!body.mot_de_passe){
    et.textContent="Champs obligatoires manquants.";e.style.display="flex";return;}
  const res=await fetch("/api/admin/proprietaires",{method:"POST",
    headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){
    ot.textContent="Compte client créé avec succès.";o.style.display="flex";
    ["pn","pp","pe","p-tel","pw"].forEach(id=>document.getElementById(id).value="");
    loadStats();
  }else{et.textContent=data.error;e.style.display="flex";}
}

async function toggleP(id){await fetch(`/api/admin/proprietaires/${id}/toggle`,{method:"POST"});loadP();}

/* ── Véhicules — regroupés par propriétaire (accordéon) ── */
let vehiculesData=[], openOwnerGroups=new Set(), focusOwnerId=null;

async function loadV(){
  vehiculesData=await fetch("/api/admin/vehicules").then(r=>r.json());
  renderVehiculesGroupes();
}

function toggleOwnerGroup(pid){
  if(openOwnerGroups.has(pid))openOwnerGroups.delete(pid);
  else openOwnerGroups.add(pid);
  renderVehiculesGroupes();
}

function ouvrirVehiculesDe(proprietaireId,proprietaireLabel){
  focusOwnerId=proprietaireId;
  openOwnerGroups.add(proprietaireId);
  show("vehicules", document.querySelectorAll(".nav-item")[2]);
  setTimeout(()=>{
    const el=document.getElementById("owner-"+proprietaireId);
    if(el)el.scrollIntoView({behavior:"smooth",block:"start"});
  },80);
}

function renderVehiculesGroupes(){
  const wrap=document.getElementById("veh-groups");
  if(!wrap)return;
  if(!vehiculesData.length){
    wrap.innerHTML='<div class="empty"><img class="empty-img" src="https://images.unsplash.com/photo-1520594923568-1b5d82587f86?auto=format&fit=crop&w=300&h=300&q=70" alt=""><div class="empty-txt">Flotte vide</div></div>';
    return;
  }
  const term=(document.getElementById("veh-search-input")?.value||"").toLowerCase().trim();

  // Regroupement par propriétaire
  const groupes={};
  vehiculesData.forEach(v=>{
    const key=v.proprietaire_id;
    if(!groupes[key])groupes[key]={id:key,nom:v.proprietaire_nom,vehicules:[]};
    groupes[key].vehicules.push(v);
  });
  let liste=Object.values(groupes).sort((a,b)=>a.nom.localeCompare(b.nom));

  if(term){
    liste=liste.map(g=>{
      const ownerMatch=g.nom.toLowerCase().includes(term);
      const vehsFiltres=ownerMatch?g.vehicules:g.vehicules.filter(v=>
        `${v.immatriculation} ${v.marque} ${v.modele} ${v.conducteur_nom||""}`.toLowerCase().includes(term));
      return {...g,vehicules:vehsFiltres};
    }).filter(g=>g.vehicules.length>0);
    // Auto-ouvre les groupes qui matchent une recherche
    liste.forEach(g=>openOwnerGroups.add(g.id));
  }

  if(!liste.length){
    wrap.innerHTML='<div class="empty"><img class="empty-img" src="https://images.unsplash.com/photo-1619468129361-605ebea04b44?auto=format&fit=crop&w=300&h=300&q=70" alt=""><div class="empty-txt">Aucun résultat</div></div>';
    return;
  }

  wrap.innerHTML=liste.map(g=>{
    const isOpen=openOwnerGroups.has(g.id);
    const initiales=g.nom.split(" ").map(s=>s[0]).join("").slice(0,2).toUpperCase();
    return `<div class="owner-group ${isOpen?'open':''} ${focusOwnerId===g.id?'hl':''}" id="owner-${g.id}">
      <div class="owner-header" onclick="toggleOwnerGroup(${g.id})">
        <div class="owner-header-left">
          <div class="owner-avatar">${initiales}</div>
          <div>
            <div class="owner-name">${g.nom}</div>
            <div class="owner-count">${g.vehicules.length} véhicule${g.vehicules.length>1?'s':''}</div>
          </div>
        </div>
        <i class="fa-solid fa-chevron-down owner-chevron"></i>
      </div>
      <div class="owner-body"><div class="owner-body-inner">
        ${g.vehicules.map(v=>`
          <div class="veh-mini-card">
            <div class="veh-mini-top">
              <img class="veh-thumb" src="${vehiculeImage(v.type_vehicule)}" alt="${v.type_vehicule}"/>
              <div style="flex:1">
                <div class="veh-mini-immat">${v.immatriculation}</div>
                <div class="veh-mini-model">${v.marque} ${v.modele} · <span style="text-transform:capitalize">${v.type_vehicule}</span></div>
              </div>
              <span class="badge ${v.actif?'badge-on':'badge-off'}" style="flex-shrink:0">${v.actif?'Actif':'Inactif'}</span>
            </div>
            ${v.conducteur_nom?`<div class="veh-mini-driver"><i class="fa-solid fa-id-card"></i> ${v.conducteur_nom}</div>`:''}
            <div class="veh-mini-device"><i class="fa-solid fa-microchip"></i> ${v.device_id}</div>
            <div class="veh-mini-actions">
              <button class="btn btn-sm ${v.actif?'btn-danger':'btn-success'}" onclick="toggleV(${v.id})"><i class="fa-solid fa-power-off"></i></button>
              <button class="btn btn-sm" style="background:var(--surface); color:var(--primary-dark); border:1px solid var(--border);" onclick="ouvrirModifV(${v.id})"><i class="fa-solid fa-pen"></i></button>
              <button class="btn btn-sm btn-danger" onclick="confirmerSuppressionV(${v.id},'${v.immatriculation}')"><i class="fa-solid fa-trash"></i></button>
            </div>
          </div>`).join("")}
      </div></div>
    </div>`;
  }).join("");
  focusOwnerId=null;
}

async function openMV(){
  const data=await fetch("/api/admin/proprietaires").then(r=>r.json());
  document.getElementById("vp").innerHTML=data.map(p=>`<option value="${p.id}">${p.prenom} ${p.nom}</option>`).join("");
  document.getElementById("ev").style.display=document.getElementById("ov").style.display="none";
  document.getElementById("mv").classList.add("open");
}

async function creerV(){
  const e=document.getElementById("ev"),o=document.getElementById("ov");
  const et=document.getElementById("ev-t"),ot=document.getElementById("ov-t");
  e.style.display=o.style.display="none";
  const body={
    proprietaire_id:parseInt(document.getElementById("vp").value),
    marque:document.getElementById("vm").value.trim(),
    modele:document.getElementById("vmo").value.trim(),
    immatriculation:document.getElementById("vi").value.trim(),
    type_vehicule:document.getElementById("vt").value,
    couleur:document.getElementById("vc").value.trim(),
    annee:parseInt(document.getElementById("va").value)||2024,
    device_id:document.getElementById("vd").value.trim(),
    conducteur_nom:document.getElementById("v-conducteur").value.trim()
  };
  const res=await fetch("/api/admin/vehicules",{method:"POST",
    headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){ot.textContent="Traceur assigné au véhicule.";o.style.display="flex";loadStats();loadV();}
  else{et.textContent=data.error;e.style.display="flex";}
}

async function toggleV(id){await fetch(`/api/admin/vehicules/${id}/toggle`,{method:"POST"});loadV();}

/* ── Historique ── */
async function initHist(){
  const vehs=await fetch("/api/admin/vehicules").then(r=>r.json());
  const sel=document.getElementById("hv");
  const cur=sel.value;
  sel.innerHTML='<option value="">Sélectionner un véhicule...</option>'+
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
    tb.innerHTML='<tr><td colspan="6"><div class="empty"><img class="empty-img" src="https://images.unsplash.com/photo-1619468129361-605ebea04b44?auto=format&fit=crop&w=300&h=300&q=70" alt=""><div class="empty-txt">Aucune donnée GPS trouvée</div></div></td></tr>';
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
    <td style="color:var(--text3);font-size:12px;font-weight:600">#${data.length-i}</td>
    <td style="font-size:13px;color:var(--text2)"><i class="fa-regular fa-clock" style="margin-right:6px"></i>${p.created_at||p.timestamp||"—"}</td>
    <td style="font-family:monospace;font-size:13px;font-weight:600;color:var(--primary-dark)">${(p.latitude||0).toFixed(6)}</td>
    <td style="font-family:monospace;font-size:13px;font-weight:600;color:var(--primary-dark)">${(p.longitude||0).toFixed(6)}</td>
    <td><span style="font-weight:600; padding:4px 10px; border-radius:8px; background:${(p.vitesse||0)>80?'var(--red-bg)':'var(--surface2)'}; color:${(p.vitesse||0)>80?'var(--red)':'var(--text)'}">${(p.vitesse||0).toFixed(1)} km/h</span></td>
    <td><i class="fa-solid fa-satellite" style="color:var(--text3);margin-right:6px"></i>${p.satellites||"—"}</td>
  </tr>`).join("");
}

function openMP(){
  document.getElementById("ep").style.display=document.getElementById("op").style.display="none";
  document.getElementById("mp").classList.add("open");
}
function closeM(id){document.getElementById(id).classList.remove("open");}

/* ── Confirmation Suppression ── */
let _supprId=null, _supprType=null;

function confirmerSuppressionV(id, label){
  _supprId=id; _supprType='vehicule';
  document.getElementById("suppr-msg").innerHTML=
    `Supprimer le véhicule <strong style="color:var(--text)">${label}</strong> et tout son historique GPS ?`;
  document.getElementById("m-suppr").classList.add("open");
}

function confirmerSuppressionP(id, label){
  _supprId=id; _supprType='proprietaire';
  document.getElementById("suppr-msg").innerHTML=
    `Supprimer le client <strong style="color:var(--text)">${label}</strong>, ses véhicules et historiques ?`;
  document.getElementById("m-suppr").classList.add("open");
}

async function executerSuppression(){
  if(!_supprId||!_supprType)return;
  const url = _supprType==='vehicule'
    ? `/api/admin/vehicules/${_supprId}`
    : `/api/admin/proprietaires/${_supprId}`;
  const res = await fetch(url,{method:"DELETE"});
  const data = await res.json();
  closeM("m-suppr");
  if(res.ok){
    if(_supprType==='vehicule') loadV();
    else loadP();
    loadStats();
  } else {
    alert(data.error||"Erreur");
  }
  _supprId=null; _supprType=null;
}

/* ── Modification ── */
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
  const et=document.getElementById("emp-t"),ot=document.getElementById("omp-t");
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
  if(res.ok){ot.textContent="Client mis à jour !";o.style.display="flex";
    setTimeout(()=>closeM("m-modif-p"),1200);loadP();}
  else{et.textContent=data.error;e.style.display="flex";}
}

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
  document.getElementById("mv-conducteur").value=data.conducteur_nom||"";
  document.getElementById("emv").style.display=document.getElementById("omv").style.display="none";
  document.getElementById("m-modif-v").classList.add("open");
}
async function sauvegarderV(){
  const id=document.getElementById("mv-id").value;
  const e=document.getElementById("emv"),o=document.getElementById("omv");
  const et=document.getElementById("emv-t"),ot=document.getElementById("omv-t");
  e.style.display=o.style.display="none";
  const body={
    marque:document.getElementById("mv-marque").value.trim(),
    modele:document.getElementById("mv-modele").value.trim(),
    immatriculation:document.getElementById("mv-immat").value.trim(),
    type_vehicule:document.getElementById("mv-type").value,
    couleur:document.getElementById("mv-couleur").value.trim(),
    annee:document.getElementById("mv-annee").value,
    device_id:document.getElementById("mv-device").value.trim(),
    conducteur_nom:document.getElementById("mv-conducteur").value.trim()
  };
  const res=await fetch(`/api/admin/vehicules/${id}`,{method:"PUT",
    headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
  const data=await res.json();
  if(res.ok){ot.textContent="Véhicule mis à jour !";o.style.display="flex";
    setTimeout(()=>closeM("m-modif-v"),1200);loadV();}
  else{et.textContent=data.error;e.style.display="flex";}
}

async function doLogout(){await fetch("/api/logout",{method:"POST"});window.location.href="/";}
loadStats();
loadAlertes();
</script>

<div class="mbg" id="m-suppr">
  <div class="modal" style="max-width:420px; text-align:center;">
    <div style="font-size:48px; color:var(--red); margin-bottom:16px;"><i class="fa-solid fa-triangle-exclamation"></i></div>
    <h3 style="color:var(--text); font-size:20px; font-weight:700; margin-bottom:12px;">Action irréversible</h3>
    <p id="suppr-msg" style="font-size:14px;color:var(--text2);line-height:1.6;margin-bottom:24px"></p>
    <div class="ma" style="margin-top:0; border-top:none; padding-top:0;">
      <button class="btn btn-success" onclick="closeM('m-suppr')" style="flex:1;">Annuler</button>
      <button class="btn btn-danger" onclick="executerSuppression()" style="flex:1; background:var(--red); color:#fff;"><i class="fa-solid fa-trash"></i> Confirmer</button>
    </div>
  </div>
</div>

<div class="mbg" id="m-modif-p">
  <div class="modal">
    <div class="mh">
      <h3>Modifier le client</h3>
      <button class="mc" onclick="closeM('m-modif-p')"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <input type="hidden" id="mp-id"/>
    <div class="al al-e" id="emp"><i class="fa-solid fa-circle-exclamation"></i> <span id="emp-t"></span></div>
    <div class="al al-o" id="omp"><i class="fa-solid fa-circle-check"></i> <span id="omp-t"></span></div>
    <div class="fg2">
      <div class="fg"><label>Nom *</label><input id="mp-nom"/></div>
      <div class="fg"><label>Prénom *</label><input id="mp-prenom"/></div>
    </div>
    <div class="fg"><label>Email *</label><input type="email" id="mp-email"/></div>
    <div class="fg"><label>Téléphone *</label><input id="mp-tel"/></div>
    <div class="fg"><label>Nouveau mot de passe <span style="font-weight:400;color:var(--text3)">(laisser vide si inchangé)</span></label>
      <input type="password" id="mp-pw"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('m-modif-p')">Annuler</button>
      <button class="btn btn-primary" onclick="sauvegarderP()"><i class="fa-solid fa-floppy-disk"></i> Enregistrer</button>
    </div>
  </div>
</div>

<div class="mbg" id="m-modif-v">
  <div class="modal">
    <div class="mh">
      <h3>Modifier le véhicule</h3>
      <button class="mc" onclick="closeM('m-modif-v')"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <input type="hidden" id="mv-id"/>
    <div class="al al-e" id="emv"><i class="fa-solid fa-circle-exclamation"></i> <span id="emv-t"></span></div>
    <div class="al al-o" id="omv"><i class="fa-solid fa-circle-check"></i> <span id="omv-t"></span></div>
    <div class="fg2">
      <div class="fg"><label>Marque *</label><input id="mv-marque"/></div>
      <div class="fg"><label>Modèle *</label><input id="mv-modele"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Type *</label>
        <select id="mv-type">
          <option value="voiture">Voiture</option>
          <option value="moto">Moto</option>
          <option value="camion">Camion</option>
          <option value="bus">Bus</option>
          <option value="autre">Autre</option>
        </select>
      </div>
      <div class="fg"><label>Couleur</label><input id="mv-couleur"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Immatriculation *</label><input id="mv-immat"/></div>
      <div class="fg"><label>Année</label><input type="number" id="mv-annee"/></div>
    </div>
    <div class="fg"><label>Device ID (ESP32) *</label><input id="mv-device"/></div>
    <div class="fg"><label>Nom complet du conducteur <span style="font-weight:400;color:var(--text3)">(optionnel)</span></label>
      <input id="mv-conducteur" placeholder="Ousmane Ndiaye"/>
    </div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('m-modif-v')">Annuler</button>
      <button class="btn btn-primary" onclick="sauvegarderV()"><i class="fa-solid fa-floppy-disk"></i> Enregistrer</button>
    </div>
  </div>
</div>
</body></html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE USER
# ═════════════════════════════════════════════════════════════

USER_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Mon Suivi</title>
<meta name="theme-color" content="#0B3D91">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="GPS Tracker">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
:root{
  --bg:#F5F7FA; --surface:#FFFFFF; --surface2:#F8FAFC; --border:#E2E8F0;
  --primary:#4FC3F7; --primary-dark:#0B3D91;
  --grad:linear-gradient(135deg, #0B3D91, #4FC3F7);
  --green:#10B981; --red:#EF4444; --amber:#F59E0B;
  --text:#1E293B; --text2:#475569; --text3:#94A3B8;
  --sidebar-w:260px;
  --shadow-sm: 0 4px 6px -1px rgba(11,61,145,0.05);
  --shadow-md: 0 10px 15px -3px rgba(11,61,145,0.08);
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Poppins',sans-serif;background:var(--bg);color:var(--text);
  height:100vh;display:flex;overflow:hidden;font-size:14px}

/* SIDEBAR */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:var(--surface);border-right:1px solid var(--border);
  display:flex;flex-direction:column;z-index:2000;
  transition:left 0.3s ease;overflow-y:auto; box-shadow:var(--shadow-md);
}
.s-logo{padding:24px 20px;border-bottom:1px solid var(--border);}
.s-logo-row{display:flex;align-items:center;gap:12px}
.s-logo-icon{width:38px;height:38px;border-radius:10px;background:var(--grad);color:#fff;
  display:flex;align-items:center;justify-content:center;font-size:18px;flex-shrink:0;
  box-shadow:0 4px 12px rgba(79,195,247,0.3)}
.s-logo-name{font-size:16px;font-weight:700;color:var(--primary-dark)}
.s-logo-sub{font-size:11px;color:var(--primary);font-weight:600}

.s-user{margin:16px;padding:14px;background:var(--surface2);border:1px solid var(--border);border-radius:12px}
.s-user-name{font-size:14px;font-weight:600;color:var(--text)}
.s-user-role{font-size:11px;font-weight:600;color:var(--primary-dark);margin-top:2px}

.s-section{padding:16px 20px 8px;font-size:11px;font-weight:700;
  color:var(--text3);text-transform:uppercase;letter-spacing:1px}
.nav-item{display:flex;align-items:center;gap:12px;padding:12px 16px;
  margin:2px 12px;border-radius:12px;cursor:pointer;color:var(--text2);
  font-size:14px;font-weight:500;transition:all 0.2s;}
.nav-item:hover{background:var(--surface2);color:var(--primary-dark)}
.nav-item.active{background:var(--primary-dark);color:#fff;font-weight:600;box-shadow:0 4px 12px rgba(11,61,145,0.2)}
.nav-ico{font-size:16px;width:24px;text-align:center;flex-shrink:0}

.veh-list{flex:1;overflow-y:auto;padding:8px 12px}
.veh-card{padding:14px;border-radius:12px;cursor:pointer;position:relative;
  border:1px solid var(--border);background:var(--surface);margin-bottom:8px;transition:all 0.2s}
.veh-card:hover{border-color:var(--primary-light);box-shadow:var(--shadow-sm);transform:translateX(2px)}
.veh-card.sel{background:var(--surface2);border-color:var(--primary-dark);border-width:2px;box-shadow:0 4px 12px rgba(11,61,145,0.12);}
.veh-card.sel::before{content:'';position:absolute;left:-1px;top:14px;bottom:14px;width:3px;
  background:var(--grad);border-radius:0 4px 4px 0;}
.veh-top{display:flex;align-items:center;justify-content:space-between;gap:8px}
.veh-immat{font-size:14px;font-weight:700;color:var(--primary-dark)}
.veh-info{font-size:12px;color:var(--text2);margin-top:4px}
.veh-status-badge{font-size:10px;font-weight:700;padding:3px 9px;border-radius:20px;
  text-transform:uppercase;letter-spacing:0.3px;white-space:nowrap;flex-shrink:0;
  background:var(--surface2);color:var(--text3);border:1px solid var(--border);}
.veh-status-badge.st-mouvement{background:rgba(16,185,129,0.1);color:var(--green);border-color:rgba(16,185,129,0.2)}
.veh-status-badge.st-immobile{background:rgba(245,158,11,0.1);color:var(--amber);border-color:rgba(245,158,11,0.2)}
.veh-status-badge.st-sans_signal{background:rgba(239,68,68,0.1);color:var(--red);border-color:rgba(239,68,68,0.2)}
.veh-live{display:flex;align-items:center;gap:6px;margin-top:8px}
.dot{width:8px;height:8px;border-radius:50%;background:var(--text3);transition:all 0.3s;flex-shrink:0}
@keyframes blink{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.6;transform:scale(0.8)}}
.dot.live{background:var(--green);animation:blink 1.5s infinite;box-shadow:0 0 8px rgba(16,185,129,0.4)}
.dot-lbl{font-size:11px;color:var(--text2);font-weight:600}
.veh-mini-stats{display:flex;gap:12px;margin-top:8px;padding-top:8px;border-top:1px solid var(--border)}
.veh-mini-stat{font-size:11px;color:var(--text2);font-weight:600;display:flex;align-items:center;gap:4px}
.veh-mini-stat i{color:var(--text3);font-size:10px}

.s-bottom{padding:16px;border-top:1px solid var(--border);background:var(--surface);flex-shrink:0}
.btn-logout{width:100%;padding:12px;background:var(--surface);color:var(--text2);
  border:1px solid var(--border);border-radius:12px;cursor:pointer;
  font-size:14px;font-weight:600;font-family:'Poppins',sans-serif;
  display:flex;align-items:center;justify-content:center;gap:8px;transition:all 0.2s}
.btn-logout:hover{background:rgba(239,68,68,0.1);color:var(--red);border-color:rgba(239,68,68,0.2)}

/* ══ FLEET PANEL (Carte GPS — style Wialon/Samsara) ══ */
.fleet-panel{width:320px;flex-shrink:0;background:var(--surface);border-right:1px solid var(--border);
  display:flex;flex-direction:column;height:100%;z-index:20;}
.fleet-search{padding:16px 16px 12px;border-bottom:1px solid var(--border)}
.fleet-search .iw input{background:var(--surface2)}
.fleet-filters{display:flex;gap:6px;padding:12px 16px;flex-wrap:wrap;border-bottom:1px solid var(--border)}
.filter-pill{padding:6px 12px;border-radius:20px;border:1px solid var(--border);background:var(--surface);
  color:var(--text2);font-size:11px;font-weight:600;cursor:pointer;font-family:'Poppins',sans-serif;
  display:flex;align-items:center;gap:6px;transition:all 0.2s;}
.filter-pill:hover{border-color:var(--primary-light)}
.filter-pill.active{background:var(--primary-dark);color:#fff;border-color:var(--primary-dark)}
.fleet-count{padding:10px 16px;font-size:11px;font-weight:700;color:var(--text3);
  text-transform:uppercase;letter-spacing:0.5px}
.fleet-cards{flex:1;overflow-y:auto;padding:4px 12px 12px}
.fleet-toggle-btn{display:none;position:absolute;top:20px;left:20px;z-index:1000;width:44px;height:44px;
  border-radius:12px;background:var(--surface);border:1px solid var(--border);box-shadow:var(--shadow-md);
  align-items:center;justify-content:center;cursor:pointer;color:var(--primary-dark);font-size:16px;}

/* ── Sélecteur de fenêtre de tracking (durée de la trace) ── */
.track-window{display:flex;gap:6px;padding:12px 16px;flex-wrap:wrap;border-bottom:1px solid var(--border)}
.track-window .filter-pill.active{background:var(--primary);border-color:var(--primary);color:#fff}

/* ── Detail card (fiche véhicule flottante sur la carte) ── */
.detail-card{position:absolute;bottom:24px;left:24px;z-index:1000;width:320px;max-width:calc(100% - 48px);
  background:rgba(255,255,255,0.97);backdrop-filter:blur(12px);border:1px solid var(--border);
  border-radius:18px;box-shadow:var(--shadow-lg);overflow:hidden;animation:fadeInUp 0.3s ease;}
.dc-head{display:flex;align-items:center;justify-content:space-between;padding:16px 18px;
  background:var(--grad);color:#fff;}
.dc-head-info{display:flex;align-items:center;gap:12px}
.dc-ico{width:38px;height:38px;border-radius:10px;background:rgba(255,255,255,0.2);
  display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0}
.dc-immat{font-size:15px;font-weight:700}
.dc-model{font-size:11px;opacity:0.85;margin-top:1px}
.dc-close{width:26px;height:26px;border-radius:8px;border:none;background:rgba(255,255,255,0.2);
  color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0}
.dc-close:hover{background:rgba(255,255,255,0.35)}
.dc-body{padding:16px 18px}
.dc-status-row{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px}
.dc-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.dc-item{background:var(--surface2);border:1px solid var(--border);border-radius:12px;padding:10px 12px}
.dc-item-lbl{font-size:10px;font-weight:600;color:var(--text3);text-transform:uppercase;letter-spacing:0.4px}
.dc-item-val{font-size:15px;font-weight:700;color:var(--text);margin-top:3px}
.dc-foot{padding:12px 18px;border-top:1px solid var(--border);display:flex;gap:8px;background:var(--surface2)}
.dc-foot button{flex:1;height:36px;border-radius:10px;border:1px solid var(--border);background:var(--surface);
  color:var(--text2);font-size:12px;font-weight:600;font-family:'Poppins',sans-serif;cursor:pointer;
  display:flex;align-items:center;justify-content:center;gap:6px;transition:all 0.2s;}
.dc-foot button:hover{border-color:var(--primary-light);color:var(--primary-dark)}

/* ══ TRAJETS DU JOUR (panneau droit) ══ */
.trajets-panel{width:320px;flex-shrink:0;background:var(--surface);border-left:1px solid var(--border);
  display:none;flex-direction:column;height:100%;z-index:20;}
.trajets-panel.visible{display:flex}
.tp-header{padding:18px 18px 14px;border-bottom:1px solid var(--border);display:flex;
  justify-content:space-between;align-items:flex-start;gap:10px}
.tp-title{font-size:15px;font-weight:700;color:var(--primary-dark)}
.tp-sub{font-size:11px;color:var(--text3);margin-top:3px;font-weight:500}
.tp-refresh{width:32px;height:32px;border-radius:9px;border:1px solid var(--border);
  background:var(--surface2);color:var(--text2);cursor:pointer;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;transition:all 0.2s}
.tp-refresh:hover{background:var(--border)}
.tp-refresh.loading i{animation:spin 1s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.tp-summary{display:flex;gap:10px;padding:14px 18px;border-bottom:1px solid var(--border)}
.tp-sum-item{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:12px;
  padding:10px 12px;text-align:center}
.tp-sum-val{font-size:16px;font-weight:700;color:var(--primary-dark)}
.tp-sum-lbl{font-size:10px;color:var(--text3);font-weight:600;margin-top:2px;text-transform:uppercase}
.tp-list{flex:1;overflow-y:auto;padding:10px 14px}
.tp-card{border:1px solid var(--border);border-radius:14px;padding:14px;margin-bottom:10px;
  cursor:pointer;transition:all 0.2s;background:var(--surface)}
.tp-card:hover{border-color:var(--primary-light);box-shadow:var(--shadow-sm)}
.tp-card.active{border-color:var(--primary-dark);border-width:2px;background:var(--surface2)}
.tp-card-num{font-size:11px;font-weight:700;color:var(--primary);text-transform:uppercase;margin-bottom:8px}
.tp-row{display:flex;align-items:flex-start;gap:8px;margin-bottom:6px}
.tp-dot{width:10px;height:10px;border-radius:50%;margin-top:3px;flex-shrink:0}
.tp-dot.a{background:var(--green)}
.tp-dot.b{background:var(--red)}
.tp-txt{flex:1;min-width:0}
.tp-heure{font-size:13px;font-weight:700;color:var(--text)}
.tp-lieu{font-size:12px;color:var(--text2);margin-top:1px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.tp-duree{font-size:11px;color:var(--text3);margin-top:8px;padding-top:8px;border-top:1px dashed var(--border)}
.tp-stationnement{font-size:11px;color:var(--amber);margin-top:6px;display:flex;align-items:center;gap:6px}
.tp-empty{padding:30px 16px;text-align:center;color:var(--text3);font-size:13px}
.tp-toggle-btn{display:none;position:absolute;top:20px;right:20px;z-index:1000;width:44px;height:44px;
  border-radius:12px;background:var(--surface);border:1px solid var(--border);box-shadow:var(--shadow-md);
  align-items:center;justify-content:center;cursor:pointer;color:var(--primary-dark);font-size:16px;}


.main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}
.topbar{height:70px;padding:0 24px;background:rgba(255,255,255,0.9);
  backdrop-filter:blur(16px);border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;flex-shrink:0; z-index:10;}
.menu-btn{display:none;background:none;border:none;cursor:pointer;
  font-size:20px;color:var(--text);padding:8px;border-radius:8px;}
.menu-btn:hover{background:var(--surface2);}
.tb-title{font-size:18px;font-weight:700;color:var(--primary-dark);}
.live-pill{display:flex;align-items:center;gap:8px;padding:6px 14px;
  background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);
  border-radius:20px;font-size:12px;color:var(--green);font-weight:600}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.4}}
.live-blink{width:8px;height:8px;border-radius:50%;background:var(--green);animation:pulse 1.5s infinite}
.upd{font-size:12px;color:var(--text3);margin-left:12px;font-weight:500;}

#map{flex:1; width:100%; height:100%; z-index:1;}
.empty-state{flex:1;display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:16px; background:var(--bg);}
.es-ico{font-size:64px;color:var(--border)}
.es-img{width:160px;height:160px;object-fit:cover;border-radius:50%;margin-bottom:8px;
  box-shadow:var(--shadow-md);border:4px solid var(--surface);}
.es-title{font-size:20px;font-weight:700;color:var(--primary-dark)}
.es-sub{font-size:14px;color:var(--text2);text-align:center;padding:0 24px; max-width:400px;}
.empty-img{width:120px;height:120px;object-fit:cover;border-radius:50%;margin:0 auto 16px;
  display:block;box-shadow:var(--shadow-md);border:4px solid var(--surface);}
.veh-thumb{width:40px;height:40px;border-radius:10px;object-fit:cover;flex-shrink:0;
  box-shadow:var(--shadow-sm);border:1px solid var(--border);}

.usec{display:none;flex:1;overflow-y:auto;padding:32px; background:var(--bg);}
.usec.active{display:block; animation:fadeInUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);}
@keyframes fadeInUp{from{opacity:0;transform:translateY(15px)}to{opacity:1;transform:translateY(0)}}

/* Dash / Hist / Params */
.stat-cards-container { display:grid; grid-template-columns:repeat(3,1fr); gap:20px; margin-bottom:32px; }
.card-modern { background:var(--surface); border:1px solid var(--border); border-radius:16px; padding:24px; position:relative; overflow:hidden; box-shadow:var(--shadow-sm); transition:transform 0.2s;}
.card-modern:hover { transform:translateY(-2px); box-shadow:var(--shadow-md); }

.h-filters{display:flex;gap:12px;margin-bottom:24px;flex-wrap:wrap}
.h-select{height:44px;padding:0 16px;background:var(--surface);border:1px solid var(--border);
  border-radius:12px;font-size:14px;font-family:'Poppins',sans-serif;color:var(--text);outline:none; box-shadow:var(--shadow-sm);}
.htable{background:var(--surface);border:1px solid var(--border);border-radius:16px;overflow:hidden;box-shadow:var(--shadow-sm);}
.htable-wrap{overflow-x:auto}
.htable table{width:100%;border-collapse:collapse;min-width:600px}
.htable th{padding:16px 20px;font-size:12px;font-weight:600;color:var(--text2);
  text-transform:uppercase;letter-spacing:0.5px;background:var(--surface2); border-bottom:2px solid var(--border)}
.htable td{padding:16px 20px;font-size:14px;color:var(--text);border-bottom:1px solid var(--border)}
.htable tr:hover td{background:var(--surface2)}

.pcard{background:var(--surface);border:1px solid var(--border);border-radius:16px;padding:28px;margin-bottom:20px;box-shadow:var(--shadow-sm);}
.ptitle{font-size:18px;font-weight:700;color:var(--primary-dark);margin-bottom:4px}
.psub{font-size:13px;color:var(--text2);margin-bottom:24px}
.prow{display:flex;justify-content:space-between;align-items:center;
  padding:16px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:12px}
.prow:last-child{border-bottom:none;padding-bottom:0}
.plbl{font-size:14px;font-weight:600;color:var(--text)}
.pdesc{font-size:12px;color:var(--text3);margin-top:4px}
.pbadge{font-size:12px;font-weight:600;padding:6px 14px;border-radius:20px;
  background:rgba(16,185,129,0.1);color:var(--green);border:1px solid rgba(16,185,129,0.2)}

.overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.5);z-index:99;backdrop-filter:blur(3px);}
.overlay.open{display:block}

/* MOBILE */
@media(max-width:768px){
  body{overflow:auto;height:auto;display:block}
  .sidebar{left:calc(-1 * var(--sidebar-w));box-shadow:none;bottom:0;height:100vh}
  .sidebar.open{left:0;box-shadow:4px 0 20px rgba(0,0,0,0.15)}
  .main{margin-left:0!important;height:100vh;display:flex;flex-direction:column}
  .menu-btn{display:inline-flex;align-items:center;justify-content:center}
  .topbar{padding:0 16px;flex-shrink:0;z-index:50;position:relative; height:60px;}
  .tb-title{font-size:16px}
  .upd{display:none}

  #tab-carte{height:calc(100vh - 60px);flex-direction:row;overflow:hidden;position:relative}
  #map-wrap{flex:1;min-height:0;overflow:hidden;position:relative}

  .fleet-panel{position:fixed;top:60px;left:0;bottom:0;width:85%;max-width:320px;
    transform:translateX(-100%);transition:transform 0.3s ease;box-shadow:none;z-index:1500;}
  .fleet-panel.open{transform:translateX(0);box-shadow:8px 0 24px rgba(0,0,0,0.15)}
  .fleet-toggle-btn{display:flex}
  .detail-card{left:12px;right:12px;bottom:16px;width:auto;max-width:none}
  .dc-grid{grid-template-columns:1fr 1fr}

  .infobar{display:none}

  #btn-retour-carte{
    display:none; position:absolute; bottom:24px; left:50%; transform:translateX(-50%);
    z-index:1000; background:var(--primary-dark); color:#fff; border:none; border-radius:24px;
    padding:12px 24px; font-size:14px; font-weight:600; cursor:pointer;
    box-shadow:0 8px 16px rgba(11,61,145,0.3); align-items:center; gap:8px; font-family:'Poppins',sans-serif;
  }
  #btn-retour-carte[data-active="true"]{display:flex}

  .trajets-panel.visible{display:flex;position:fixed;top:60px;right:0;bottom:0;width:85%;max-width:320px;
    transform:translateX(100%);transition:transform 0.3s ease;z-index:1500;}
  .trajets-panel.visible.open{transform:translateX(0);box-shadow:-8px 0 24px rgba(0,0,0,0.15)}
  .tp-toggle-btn{display:flex}

  .usec{padding:20px;height:calc(100vh - 60px);overflow-y:auto}
  .stat-cards-container{grid-template-columns:1fr; gap:16px;}
  .h-filters{flex-direction:column}
  .h-select{width:100%}
}
</style></head><body>

<div class="overlay" id="overlay" onclick="closeMenu()"></div>

<div class="sidebar" id="sidebar">
  <div class="s-logo">
    <div class="s-logo-row">
      <div class="s-logo-icon"><i class="fa-solid fa-location-arrow"></i></div>
      <div><div class="s-logo-name">GPS Tracker</div><div class="s-logo-sub">Espace Client</div></div>
    </div>
  </div>
  <div class="s-user">
    <div class="s-user-name" id="uname">—</div>
    <div class="s-user-role">Propriétaire</div>
  </div>
  <div class="s-section">Navigation</div>
  <div class="nav-item active" onclick="showTab('dashboard',this)">
    <i class="fa-solid fa-chart-line nav-ico"></i> Tableau de bord
  </div>
  <div class="nav-item" onclick="showTab('carte',this)">
    <i class="fa-solid fa-map-location-dot nav-ico"></i> Carte GPS
  </div>
  <div class="nav-item" onclick="showTab('historique',this)">
    <i class="fa-solid fa-route nav-ico"></i> Historique
  </div>
  <div class="nav-item" onclick="showTab('parametres',this)">
    <i class="fa-solid fa-sliders nav-ico"></i> Paramètres
  </div>
  <div style="flex:1"></div>
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()"><i class="fa-solid fa-power-off"></i> Déconnexion</button>
  </div>
</div>

<div class="main">
  <div class="topbar">
    <div style="display:flex;align-items:center;gap:12px">
      <button class="menu-btn" onclick="toggleMenu()"><i class="fa-solid fa-bars"></i></button>
      <div class="tb-title" id="ttl">Sélectionnez un véhicule</div>
    </div>
    <div style="display:flex;align-items:center;gap:12px">
      <div class="live-pill"><div class="live-blink"></div>Temps réel</div>
      <span class="upd" id="tupd"><i class="fa-regular fa-clock"></i> —</span>
    </div>
  </div>

  <div id="tab-dashboard" class="usec active">
    <div style="position:relative; border-radius:16px; overflow:hidden; min-height:150px; margin-bottom:24px; display:flex; align-items:center; box-shadow:var(--shadow-sm);">
      <img src="https://images.unsplash.com/photo-1520594923568-1b5d82587f86?auto=format&fit=crop&w=1400&q=70" alt="Réseau routier"
        style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;"/>
      <div style="position:absolute;inset:0;background:linear-gradient(90deg, rgba(255,255,255,0.96) 0%, rgba(255,255,255,0.8) 45%, rgba(255,255,255,0.25) 100%);"></div>
      <div style="position:relative; padding:28px 32px;">
        <h2 style="font-size:22px;font-weight:700;color:var(--primary-dark);">Vue d'ensemble</h2>
        <p style="font-size:13px;color:var(--text2);margin-top:6px;max-width:420px;">Suivez l'état de votre flotte en un coup d'œil.</p>
      </div>
    </div>

    <div class="stat-cards-container" id="stat-cards">
      <div class="card-modern" style="border-top:4px solid var(--green);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <div style="width:40px;height:40px;border-radius:10px;background:var(--green-bg);color:var(--green);display:flex;align-items:center;justify-content:center;font-size:18px;"><i class="fa-solid fa-truck-fast"></i></div>
        </div>
        <div style="font-size:36px;font-weight:700;color:var(--green);line-height:1;" id="cnt-mouvement">0</div>
        <div style="font-size:14px;color:var(--text2);font-weight:600;margin-top:8px;">En mouvement</div>
      </div>
      <div class="card-modern" style="border-top:4px solid var(--amber);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <div style="width:40px;height:40px;border-radius:10px;background:rgba(245,158,11,0.1);color:var(--amber);display:flex;align-items:center;justify-content:center;font-size:18px;"><i class="fa-solid fa-square-parking"></i></div>
        </div>
        <div style="font-size:36px;font-weight:700;color:var(--amber);line-height:1;" id="cnt-immobile">0</div>
        <div style="font-size:14px;color:var(--text2);font-weight:600;margin-top:8px;">Immobile</div>
      </div>
      <div class="card-modern" style="border-top:4px solid var(--red);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
          <div style="width:40px;height:40px;border-radius:10px;background:rgba(239,68,68,0.1);color:var(--red);display:flex;align-items:center;justify-content:center;font-size:18px;"><i class="fa-solid fa-location-crosshairs" style="opacity:0.5"></i></div>
        </div>
        <div style="font-size:36px;font-weight:700;color:var(--red);line-height:1;" id="cnt-signal">0</div>
        <div style="font-size:14px;color:var(--text2);font-weight:600;margin-top:8px;">Hors ligne</div>
      </div>
    </div>

    <h3 style="font-size:16px; font-weight:700; color:var(--text); margin-bottom:16px;">État de la flotte</h3>
    <div id="dash-list" style="display:flex;flex-direction:column;gap:12px">
      <div style="text-align:center;padding:40px;color:var(--text3);font-size:14px"><i class="fa-solid fa-spinner fa-spin"></i> Analyse en cours...</div>
    </div>
  </div>

  <div id="tab-carte" style="flex:1;display:none;overflow:hidden; position:relative;">

    <div class="fleet-panel" id="fleet-panel">
      <div class="fleet-search">
        <div class="iw"><i class="fa-solid fa-magnifying-glass ii"></i>
          <input id="fleet-search-input" placeholder="Rechercher (immat, marque...)" oninput="renderFleetPanel()"/></div>
      </div>
      <div class="fleet-filters">
        <button class="filter-pill active" data-f="all" onclick="setFleetFilter('all',this)">Tous</button>
        <button class="filter-pill" data-f="mouvement" onclick="setFleetFilter('mouvement',this)">
          <i class="fa-solid fa-circle" style="color:var(--green);font-size:6px"></i> En route</button>
        <button class="filter-pill" data-f="immobile" onclick="setFleetFilter('immobile',this)">
          <i class="fa-solid fa-circle" style="color:var(--amber);font-size:6px"></i> Immobile</button>
        <button class="filter-pill" data-f="sans_signal" onclick="setFleetFilter('sans_signal',this)">
          <i class="fa-solid fa-circle" style="color:var(--red);font-size:6px"></i> Hors ligne</button>
      </div>
      <div class="track-window" id="track-window">
        <button class="filter-pill active" data-w="" onclick="setTrackWindow('',this)" title="Comportement standard (200 dernières positions)">Standard</button>
        <button class="filter-pill" data-w="15" onclick="setTrackWindow('15',this)">15 mn</button>
        <button class="filter-pill" data-w="30" onclick="setTrackWindow('30',this)">30 mn</button>
        <button class="filter-pill" data-w="60" onclick="setTrackWindow('60',this)">1h</button>
        <button class="filter-pill" data-w="120" onclick="setTrackWindow('120',this)">2h</button>
      </div>
      <div class="fleet-count" id="fleet-count">Chargement...</div>
      <div class="fleet-cards" id="fleet-cards">
        <div style="padding:14px;color:var(--text3);font-size:13px;text-align:center;"><i class="fa-solid fa-spinner fa-spin"></i> Chargement...</div>
      </div>
    </div>

    <div id="map-column" style="flex:1;display:flex;flex-direction:column;position:relative;min-width:0;">
      <div id="map-wrap" style="flex:1;display:none;position:relative">
        <div id="map"></div>
        <button class="fleet-toggle-btn" id="fleet-toggle-btn" onclick="toggleFleetPanel()"><i class="fa-solid fa-list"></i></button>
        <button class="tp-toggle-btn" id="tp-toggle-btn" onclick="toggleTrajetsPanel()" style="display:none"><i class="fa-solid fa-route"></i></button>
        <div class="detail-card" id="detail-card" style="display:none">
          <div class="dc-head">
            <div class="dc-head-info">
              <img id="dc-vico" class="dc-ico" src="https://images.unsplash.com/photo-1492967396498-f79507b65e89?auto=format&fit=crop&w=100&h=100&q=70" alt="" style="object-fit:cover;"/>
              <div>
                <div class="dc-immat" id="dc-immat">—</div>
                <div class="dc-model" id="dc-model">—</div>
              </div>
            </div>
            <button class="dc-close" onclick="closeDetailCard()"><i class="fa-solid fa-xmark"></i></button>
          </div>
          <div class="dc-body">
            <div class="dc-status-row">
              <span class="veh-status-badge" id="dc-badge">—</span>
              <span style="font-size:11px;color:var(--text3);font-weight:500" id="dc-updated">—</span>
            </div>
            <div class="dc-grid">
              <div class="dc-item"><div class="dc-item-lbl">Vitesse</div><div class="dc-item-val" id="dc-speed">—</div></div>
              <div class="dc-item"><div class="dc-item-lbl">Latitude</div><div class="dc-item-val" id="dc-lat" style="font-size:12px;font-family:monospace">—</div></div>
              <div class="dc-item" style="grid-column:span 2"><div class="dc-item-lbl">Longitude</div><div class="dc-item-val" id="dc-lng" style="font-size:12px;font-family:monospace">—</div></div>
            </div>
          </div>
          <div class="dc-foot">
            <button onclick="goToHistorique()"><i class="fa-solid fa-route"></i> Historique</button>
            <button onclick="recenterMap()"><i class="fa-solid fa-crosshairs"></i> Recentrer</button>
          </div>
        </div>
        <button id="btn-retour-carte" onclick="toggleMenu()">
          <i class="fa-solid fa-bars"></i> Menu
        </button>
      </div>

      <div class="empty-state" id="empty">
        <img class="es-img" src="https://images.unsplash.com/photo-1619468129361-605ebea04b44?auto=format&fit=crop&w=320&h=320&q=70" alt=""/>
        <div class="es-title">Aucun véhicule sélectionné</div>
        <div class="es-sub">Choisissez un véhicule dans le panneau flotte pour démarrer le suivi en temps réel.</div>
      </div>
    </div>

    <div class="trajets-panel" id="trajets-panel">
      <div class="tp-header">
        <div>
          <div class="tp-title"><i class="fa-solid fa-route"></i> Trajets du jour</div>
          <div class="tp-sub" id="tp-sub">—</div>
        </div>
        <button class="tp-refresh" id="tp-refresh-btn" onclick="chargerTrajetsJour()"><i class="fa-solid fa-arrows-rotate"></i></button>
      </div>
      <div class="tp-summary" id="tp-summary" style="display:none">
        <div class="tp-sum-item"><div class="tp-sum-val" id="tp-mobilite">—</div><div class="tp-sum-lbl">En route</div></div>
        <div class="tp-sum-item"><div class="tp-sum-val" id="tp-stationnement">—</div><div class="tp-sum-lbl">À l'arrêt</div></div>
      </div>
      <div class="tp-list" id="tp-list">
        <div class="tp-empty">Sélectionnez un véhicule</div>
      </div>
    </div>
  </div>

  <div id="tab-historique" class="usec">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:24px">
      <h2 style="font-size:22px;font-weight:700;color:var(--primary-dark)">Historique des trajets</h2>
    </div>
    <div class="h-filters">
      <select class="h-select" id="uhv" onchange="loadUH()" style="min-width:250px;">
        <option value="">Sélectionnez un véhicule...</option>
      </select>
      <select class="h-select" id="uhl" onchange="loadUH()">
        <option value="50">50 dernières positions</option>
        <option value="100">100 dernières positions</option>
        <option value="200">200 dernières positions</option>
      </select>
    </div>
    <div class="htable">
      <div class="htable-wrap">
        <table>
          <thead><tr>
            <th>#</th><th>Date / Heure</th><th>Latitude</th>
            <th>Longitude</th><th>Vitesse</th>
          </tr></thead>
          <tbody id="uhtb">
            <tr><td colspan="5" style="text-align:center;padding:50px;color:var(--text3)">
              <i class="fa-solid fa-list" style="font-size:24px; margin-bottom:12px; display:block;"></i>
              Sélectionnez un véhicule pour afficher l'historique
            </td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <div id="tab-parametres" class="usec">
    <h2 style="font-size:22px;font-weight:700;color:var(--primary-dark);margin-bottom:24px">Paramètres</h2>
    
    <div class="pcard">
      <div class="ptitle">Mon profil</div>
      <div class="psub">Informations associées à votre compte</div>
      <div class="prow"><div><div class="plbl">Nom complet</div><div class="pdesc" id="pcn">—</div></div><span class="pbadge"><i class="fa-solid fa-check"></i> Actif</span></div>
      <div class="prow"><div><div class="plbl">Email</div><div class="pdesc" id="pce">—</div></div></div>
      <div class="prow"><div><div class="plbl">Téléphone</div><div class="pdesc" id="pct">—</div></div></div>
      <div class="prow"><div><div class="plbl">Membre depuis</div><div class="pdesc" id="pcd">—</div></div></div>
    </div>

    <div class="pcard">
      <div class="ptitle">Mes véhicules</div>
      <div class="psub">Flotte active sous surveillance</div>
      <div id="pcv"><i class="fa-solid fa-spinner fa-spin"></i> Chargement...</div>
    </div>

    <div class="pcard">
      <div class="ptitle">Notifications & Alertes</div>
      <div class="psub">Soyez prévenu en cas de perte de signal prolongée</div>
      <div id="notif-wrap">
        <div style="font-size:13px;color:var(--text3)"><i class="fa-solid fa-spinner fa-spin"></i> Vérification...</div>
      </div>
    </div>

    <div class="pcard">
      <div class="ptitle">À propos du système</div>
      <div class="psub">Détails de l'application</div>
      <div class="prow">
        <div><div class="plbl">GPS Tracker SaaS</div><div class="pdesc">Version 3.1 — Modern UI</div></div>
        <span class="pbadge" style="background:var(--surface2); color:var(--text2); border-color:var(--border);"><i class="fa-solid fa-code"></i> Python / Flask</span>
      </div>
    </div>
  </div>
</div>

<script>
let map=null,marker=null,poly=null,startMarker=null,selId=null,interval=null,meD=null,vehD=[];
let vehStatusMap={}, fleetFilter="all";
let trajetsData=[], trajetLayer=null, trajetActifNumero=null, intervalTrajets=null;

/* Vraies photos par type de véhicule (au lieu d'icônes génériques) */
const VEH_IMAGES={
  voiture:"https://images.unsplash.com/photo-1492967396498-f79507b65e89?auto=format&fit=crop&w=120&h=120&q=70",
  moto:"https://images.unsplash.com/photo-1591637333184-19aa84b3e01f?auto=format&fit=crop&w=120&h=120&q=70",
  camion:"https://images.unsplash.com/photo-1616432043562-3671ea2e5242?auto=format&fit=crop&w=120&h=120&q=70",
  bus:"https://images.unsplash.com/photo-1514355453671-d0164a278218?auto=format&fit=crop&w=120&h=120&q=70",
  autre:"https://images.unsplash.com/photo-1492967396498-f79507b65e89?auto=format&fit=crop&w=120&h=120&q=70"
};
function vehiculeImage(type){return VEH_IMAGES[type]||VEH_IMAGES.autre;}

/* ── Fenêtre de tracking (durée de la trace affichée) ──
   "" = comportement standard (200 dernières positions, comme avant l'ajout de cette fonctionnalité)
   "15"/"30"/"60"/"120" = fenêtre glissante en minutes, mémorisée dans localStorage */
let trackWindowMinutes = localStorage.getItem("gps_track_window") || "";
let tracePoints = []; // {lat,lng,ts} utilisés uniquement en mode fenêtre glissante

function toggleMenu(){
  document.getElementById("sidebar").classList.toggle("open");
  document.getElementById("overlay").classList.toggle("open");
}
function closeMenu(){
  document.getElementById("sidebar").classList.remove("open");
  document.getElementById("overlay").classList.remove("open");
}
function toggleFleetPanel(){
  document.getElementById("fleet-panel").classList.toggle("open");
}
function closeFleetPanel(){
  document.getElementById("fleet-panel").classList.remove("open");
}

function showTab(n,el){
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  if(el)el.classList.add("active");
  document.getElementById("tab-carte").style.display=n==="carte"?"flex":"none";
  document.querySelectorAll(".usec").forEach(s=>s.classList.remove("active"));
  if(n!=="carte")document.getElementById("tab-"+n).classList.add("active");
  const btnRetour=document.getElementById("btn-retour-carte");
  if(btnRetour)delete btnRetour.dataset.active;
  if(n==="dashboard")loadDashboard();
  if(n==="carte")renderFleetPanel();
  if(n==="historique")initUH();
  if(n==="parametres")loadParams();
  closeMenu();
}

/* ── Tableau de bord ── */
async function loadDashboard(){
  try{
    const data = await fetch("/api/user/vehicules/statut").then(r=>r.json());
    data.forEach(v=>vehStatusMap[v.id]=v);
    updateFleetCardsStatus();
    updateDetailCardLive();

    const nbMouvement = data.filter(v=>v.statut==='mouvement').length;
    const nbImmobile  = data.filter(v=>v.statut==='immobile').length;
    const nbSignal    = data.filter(v=>v.statut==='sans_signal').length;

    document.getElementById("cnt-mouvement").textContent = nbMouvement;
    document.getElementById("cnt-immobile").textContent  = nbImmobile;
    document.getElementById("cnt-signal").textContent    = nbSignal;

    const list = document.getElementById("dash-list");
    if(!data.length){
      list.innerHTML = '<div style="text-align:center;padding:40px;color:var(--text3);font-size:14px;background:var(--surface);border-radius:16px;"><img class="empty-img" src="https://images.unsplash.com/photo-1520594923568-1b5d82587f86?auto=format&fit=crop&w=300&h=300&q=70" alt="">Aucun véhicule n\\'est actuellement assigné à votre compte.</div>';
      return;
    }

    const config = {
      mouvement:  {icone:'<i class="fa-solid fa-truck-fast"></i>', label:'En mouvement', couleur:'var(--green)', bg:'rgba(16,185,129,0.1)', bd:'rgba(16,185,129,0.2)'},
      immobile:   {icone:'<i class="fa-solid fa-square-parking"></i>', label:'Immobile',      couleur:'var(--amber)',     bg:'rgba(245,158,11,0.1)', bd:'rgba(245,158,11,0.2)'},
      sans_signal:{icone:'<i class="fa-solid fa-location-crosshairs" style="opacity:0.5"></i>', label:'Hors ligne',   couleur:'var(--red)',  bg:'rgba(239,68,68,0.1)', bd:'rgba(239,68,68,0.2)'}
    };

    list.innerHTML = data.map(v=>{
      const cfg = config[v.statut];
      const infoSignal = v.statut==='sans_signal'
        ? (v.minutes_sans_signal!==null
            ? `Hors ligne depuis ${Math.round(v.minutes_sans_signal)} min · Nous surveillons la situation`
            : 'Aucune donnée enregistrée pour le moment')
        : `<i class="fa-solid fa-gauge-high"></i> ${(v.vitesse||0).toFixed(0)} km/h`;

      return `<div onclick="showTab('carte',document.querySelectorAll('.nav-item')[1]); selV(${v.id},'${v.marque} ${v.modele}','${v.immatriculation}')"
        style="display:flex;align-items:center;justify-content:space-between;cursor:pointer;
          background:var(--surface);border:1px solid var(--border);border-radius:16px;
          padding:20px;transition:all 0.2s; box-shadow:var(--shadow-sm);"
        onmouseover="this.style.borderColor='${cfg.couleur}'; this.style.transform='translateY(-2px)';"
        onmouseout="this.style.borderColor='var(--border)'; this.style.transform='translateY(0)';">
        <div style="display:flex;align-items:center;gap:16px">
          <div style="width:48px;height:48px;border-radius:12px;background:${cfg.bg};color:${cfg.couleur};
            display:flex;align-items:center;justify-content:center;font-size:20px">${cfg.icone}</div>
          <div>
            <div style="font-size:16px;font-weight:700;color:var(--text)">${v.immatriculation}</div>
            <div style="font-size:13px;color:var(--text2)">${v.marque} ${v.modele}</div>
          </div>
        </div>
        <div style="text-align:right">
          <div style="font-size:12px;font-weight:600;padding:4px 12px;border-radius:20px;
            background:${cfg.bg};color:${cfg.couleur};border:1px solid ${cfg.bd};display:inline-block">
            ${cfg.label}
          </div>
          <div style="font-size:12px;color:var(--text3);margin-top:8px;font-weight:500;">${infoSignal}</div>
        </div>
      </div>`;
    }).join("");
  }catch(e){
    console.log("Erreur dashboard:",e);
  }
}

function initMap(){
  if(map)return;
  map=L.map("map",{zoomControl:false}).setView([14.8500,-15.8833],15);
  L.control.zoom({position: 'bottomright'}).addTo(map);
  L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",{
    attribution:"© Esri",
    maxZoom:20,
    maxNativeZoom:17,
    minZoom:3
  }).addTo(map);
  poly=L.polyline([],{color:"#4FC3F7",weight:5,opacity:0.9,lineCap:"round",lineJoin:"round"}).addTo(map);
}

async function loadVehicules(){
  const[vehs,m]=await Promise.all([
    fetch("/api/user/vehicules").then(r=>r.json()),
    fetch("/api/me").then(r=>r.json())]);
  meD=m; vehD=vehs;
  document.getElementById("uname").textContent=m.prenom+" "+m.nom;
  renderFleetPanel();
}

/* ── Panneau flotte (Carte GPS) — style Wialon/Samsara ── */
function setFleetFilter(f,btn){
  fleetFilter=f;
  document.querySelectorAll(".filter-pill").forEach(b=>{ if(b.dataset.f!==undefined) b.classList.remove("active"); });
  if(btn)btn.classList.add("active");
  renderFleetPanel();
}

/* ── Sélecteur de fenêtre de tracking (durée de la trace) ── */
function setTrackWindow(minutes, btn){
  trackWindowMinutes = minutes;
  localStorage.setItem("gps_track_window", minutes);
  document.querySelectorAll("#track-window .filter-pill").forEach(b=>b.classList.remove("active"));
  if(btn)btn.classList.add("active");
  // Recharge immédiatement la trace du véhicule actuellement suivi, si un véhicule est sélectionné
  if(selId){
    chargerHistoriqueTrace(selId);
  }
}

function syncTrackWindowUI(){
  document.querySelectorAll("#track-window .filter-pill").forEach(b=>{
    b.classList.toggle("active", (b.dataset.w||"")===trackWindowMinutes);
  });
}

function renderFleetPanel(){
  const cards=document.getElementById("fleet-cards");
  const countEl=document.getElementById("fleet-count");
  if(!cards)return;
  syncTrackWindowUI();
  if(!vehD.length){
    cards.innerHTML='<div style="padding:20px;color:var(--text3);font-size:13px;text-align:center;">Aucun véhicule assigné</div>';
    if(countEl)countEl.textContent="0 véhicule";
    return;
  }
  const term=(document.getElementById("fleet-search-input")?.value||"").toLowerCase().trim();
  let filtered=vehD.filter(v=>{
    const st=vehStatusMap[v.id]?.statut;
    if(fleetFilter!=="all" && st!==fleetFilter)return false;
    if(term && !(`${v.immatriculation} ${v.marque} ${v.modele}`.toLowerCase().includes(term)))return false;
    return true;
  });
  if(countEl)countEl.textContent=`${filtered.length} véhicule${filtered.length>1?'s':''} sur ${vehD.length}`;
  if(!filtered.length){
    cards.innerHTML='<div style="padding:20px;color:var(--text3);font-size:13px;text-align:center;">Aucun résultat</div>';
    return;
  }
  cards.innerHTML=filtered.map(v=>`
    <div class="veh-card ${v.id===selId?'sel':''}" id="vc${v.id}" onclick="selV(${v.id},'${v.marque} ${v.modele}','${v.immatriculation}')">
      <div class="veh-top">
        <img class="veh-thumb" src="${vehiculeImage(v.type_vehicule)}" alt=""/>
        <div style="flex:1">
          <div class="veh-immat">${v.immatriculation}</div>
          <div class="veh-info">${v.marque} ${v.modele}</div>
        </div>
        <span class="veh-status-badge" id="badge${v.id}">—</span>
      </div>
      <div class="veh-live">
        <div class="dot" id="dot${v.id}"></div>
        <span class="dot-lbl" id="dlbl${v.id}">En attente</span>
      </div>
      <div class="veh-mini-stats" id="mstats${v.id}" style="display:none">
        <span class="veh-mini-stat"><i class="fa-solid fa-gauge-high"></i> <span id="mspd${v.id}">—</span> km/h</span>
      </div>
    </div>`).join("");
  updateFleetCardsStatus();
}

function updateFleetCardsStatus(){
  const cfgLbl={mouvement:"En mouvement",immobile:"Immobile",sans_signal:"Hors ligne"};
  Object.values(vehStatusMap).forEach(v=>{
    const badge=document.getElementById("badge"+v.id);
    const mstats=document.getElementById("mstats"+v.id);
    const mspd=document.getElementById("mspd"+v.id);
    if(badge){
      badge.className="veh-status-badge st-"+v.statut;
      badge.textContent=cfgLbl[v.statut]||"—";
    }
    if(v.statut!=="sans_signal" && mstats){
      mstats.style.display="flex";
      if(mspd)mspd.textContent=(v.vitesse||0).toFixed(0);
    }else if(mstats){
      mstats.style.display="none";
    }
  });
}

function updateDetailCardLive(){
  if(!selId)return;
  const v=vehStatusMap[selId];
  if(!v)return;
  const cfgLbl={mouvement:"En mouvement",immobile:"Immobile",sans_signal:"Hors ligne"};
  const badge=document.getElementById("dc-badge");
  if(badge){
    badge.className="veh-status-badge st-"+v.statut;
    badge.textContent=cfgLbl[v.statut]||"—";
  }
}

function closeDetailCard(){
  document.getElementById("detail-card").style.display="none";
}
function recenterMap(){
  if(marker && map)map.setView(marker.getLatLng(),17);
}
function goToHistorique(){
  showTab("historique", document.querySelectorAll(".nav-item")[2]);
  const sel=document.getElementById("uhv");
  if(sel && selId){sel.value=selId; loadUH();}
}

/* Charge (ou recharge) le tracé affiché sur la carte pour le véhicule vid,
   selon le réglage de fenêtre actif (trackWindowMinutes). */
async function chargerHistoriqueTrace(vid){
  const url = trackWindowMinutes
    ? `/api/positions/${vid}?minutes=${trackWindowMinutes}`
    : `/api/positions/${vid}?limit=200`;
  const hist = await fetch(url).then(r=>r.json());
  if(poly)poly.setLatLngs([]);
  if(startMarker){map.removeLayer(startMarker);startMarker=null;}
  tracePoints = hist.map(p=>({lat:p.latitude,lng:p.longitude,ts:Date.parse(p.created_at)||Date.now()}));
  if(hist.length){
    poly.setLatLngs(tracePoints.map(p=>[p.lat,p.lng]));
    const first=hist[0];
    startMarker=L.circleMarker([first.latitude,first.longitude],{
      radius:6,color:"#fff",weight:2,fillColor:"#10B981",fillOpacity:1
    }).addTo(map).bindTooltip("Départ du trajet",{direction:"top"});
  }
}

async function selV(id,label,immat){
  selId=id;
  document.getElementById("ttl").textContent=immat+" — "+label;
  document.getElementById("empty").style.display="none";
  document.getElementById("map-wrap").style.display="block";
  const btnRetour = document.getElementById("btn-retour-carte");
  if(btnRetour) btnRetour.dataset.active="true";
  document.getElementById("tab-carte").style.display="flex";
  document.querySelectorAll(".usec").forEach(s=>s.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  const navItems = document.querySelectorAll(".nav-item");
  if(navItems[1]) navItems[1].classList.add("active");
  closeFleetPanel();

  const v=vehD.find(x=>x.id===id);
  document.getElementById("dc-immat").textContent=immat;
  document.getElementById("dc-model").textContent=v?`${v.marque} ${v.modele}`:label;
  document.getElementById("dc-vico").src=vehiculeImage(v?v.type_vehicule:"autre");
  document.getElementById("detail-card").style.display="block";
  updateDetailCardLive();

  renderFleetPanel();

  initMap();
  if(marker){map.removeLayer(marker);marker=null;}
  setTimeout(()=>map.invalidateSize(),150);
  setTimeout(()=>map.invalidateSize(),400);
  await chargerHistoriqueTrace(id);
  if(trajetLayer){map.removeLayer(trajetLayer);trajetLayer=null;}
  trajetActifNumero=null;
  if(interval)clearInterval(interval);
  if(intervalTrajets)clearInterval(intervalTrajets);
  refresh(); interval=setInterval(refresh,2000);
  chargerTrajetsJour(); intervalTrajets=setInterval(chargerTrajetsJour, 5*60*1000);
}

/* ── Trajets du jour ── */
function toggleTrajetsPanel(){document.getElementById("trajets-panel").classList.toggle("open");}

async function chargerTrajetsJour(){
  if(!selId)return;
  const btn=document.getElementById("tp-refresh-btn");
  if(btn)btn.classList.add("loading");
  try{
    const res=await fetch(`/api/positions/${selId}/trajets-jour`);
    if(!res.ok)throw new Error("http "+res.status);
    const data=await res.json();
    trajetsData=data.trajets||[];
    renderTrajetsJour(data);
  }catch(e){
    console.log("Erreur trajets du jour:",e);
    document.getElementById("trajets-panel").classList.add("visible");
    document.getElementById("tp-list").innerHTML='<div class="tp-empty">Impossible de charger les trajets pour le moment.</div>';
    document.getElementById("tp-summary").style.display="none";
  }
  if(btn)btn.classList.remove("loading");
}

function formatDuree(minutes){
  minutes=Math.max(0,Math.round(minutes||0));
  const h=Math.floor(minutes/60), m=minutes%60;
  return h>0 ? `${h}h${m.toString().padStart(2,'0')}` : `${m} min`;
}

function renderTrajetsJour(data){
  const panel=document.getElementById("trajets-panel");
  const list=document.getElementById("tp-list");
  const sub=document.getElementById("tp-sub");
  const summary=document.getElementById("tp-summary");
  panel.classList.add("visible");
  const tpBtn=document.getElementById("tp-toggle-btn");
  if(tpBtn)tpBtn.style.display="flex";

  if(!data.trajets||!data.trajets.length){
    sub.textContent="Aucun déplacement aujourd'hui";
    summary.style.display="none";
    list.innerHTML='<div class="tp-empty"><i class="fa-solid fa-moon" style="font-size:20px;margin-bottom:8px;display:block;color:var(--text3)"></i>Ce véhicule n\\'a pas encore bougé aujourd\\'hui.</div>';
    return;
  }
  sub.textContent=`${data.trajets.length} trajet${data.trajets.length>1?'s':''} aujourd'hui`;
  summary.style.display="flex";
  document.getElementById("tp-mobilite").textContent=formatDuree(data.duree_mobilite_minutes||0);
  document.getElementById("tp-stationnement").textContent=formatDuree(data.duree_stationnement_minutes||0);

  list.innerHTML=data.trajets.map(t=>`
    <div class="tp-card ${t.numero===trajetActifNumero?'active':''}" onclick="afficherTrajetSurCarte(${t.numero})">
      <div class="tp-card-num">Trajet ${t.numero}</div>
      <div class="tp-row"><div class="tp-dot a"></div><div class="tp-txt">
        <div class="tp-heure">${t.depart.heure}</div><div class="tp-lieu">${t.depart.adresse}</div>
      </div></div>
      <div class="tp-row"><div class="tp-dot b"></div><div class="tp-txt">
        <div class="tp-heure">${t.arrivee.heure} ${t.arrivee.en_cours?'<span style="color:var(--green);font-weight:600">· En cours</span>':''}</div>
        <div class="tp-lieu">${t.arrivee.adresse}</div>
      </div></div>
      <div class="tp-duree"><i class="fa-solid fa-clock"></i> ${formatDuree(t.duree_minutes)} de route</div>
      ${t.stationnement_suivant?`<div class="tp-stationnement"><i class="fa-solid fa-square-parking"></i> ${formatDuree(t.stationnement_suivant.duree_minutes)} à ${t.stationnement_suivant.adresse}</div>`:''}
    </div>`).join("");
}

function afficherTrajetSurCarte(numero){
  const t=trajetsData.find(x=>x.numero===numero);
  if(!t||!map)return;
  trajetActifNumero=numero;
  const cards=document.querySelectorAll("#tp-list .tp-card");
  cards.forEach(c=>c.classList.remove("active"));
  const idx=trajetsData.findIndex(x=>x.numero===numero);
  if(cards[idx])cards[idx].classList.add("active");

  if(trajetLayer)map.removeLayer(trajetLayer);
  const latlngs=(t.trace||[]).map(p=>[p[0],p[1]]);
  if(!latlngs.length)return;
  trajetLayer=L.layerGroup().addTo(map);
  L.polyline(latlngs,{color:"#7C3AED",weight:5,opacity:0.85,lineCap:"round"}).addTo(trajetLayer);
  L.marker([t.depart.lat,t.depart.lng],{icon:L.divIcon({
      html:'<div style="background:#10B981;color:#fff;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,0.3)">A</div>',
      iconSize:[26,26],iconAnchor:[13,13]})})
    .addTo(trajetLayer).bindTooltip(`Départ ${t.depart.heure} — ${t.depart.adresse}`);
  L.marker([t.arrivee.lat,t.arrivee.lng],{icon:L.divIcon({
      html:`<div style="background:${t.arrivee.en_cours?'#4FC3F7':'#EF4444'};color:#fff;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:12px;border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,0.3)">${t.arrivee.en_cours?'●':'B'}</div>`,
      iconSize:[26,26],iconAnchor:[13,13]})})
    .addTo(trajetLayer).bindTooltip(`${t.arrivee.en_cours?'Position actuelle':'Arrivée'} ${t.arrivee.heure} — ${t.arrivee.adresse}`);
  map.fitBounds(L.latLngBounds(latlngs), {padding:[40,40]});
  closeFleetPanel();
}

async function refresh(){
  if(!selId)return;
  try{
    const res=await fetch(`/api/positions/${selId}/last`);
    if(!res.ok)return;
    const p=await res.json();
    const ll=[p.latitude,p.longitude];
    const icon=L.divIcon({
      html:`<div style="position:relative;width:28px;height:28px">
        <div style="position:absolute;top:0;left:0;width:28px;height:28px;
          background:rgba(79, 195, 247, 0.4);border-radius:50%;
          animation:pulseMarker 2s infinite"></div>
        <div style="position:absolute;top:6px;left:6px;width:16px;height:16px;
          background:linear-gradient(135deg, #0B3D91, #4FC3F7);
          border:3px solid #fff;border-radius:50%;
          box-shadow:0 4px 10px rgba(0,0,0,0.3)"></div>
      </div>
      <style>
        @keyframes pulseMarker{
          0%{transform:scale(0.6);opacity:1}
          100%{transform:scale(2);opacity:0}
        }
      </style>`,
      iconSize:[28,28],iconAnchor:[14,14]});
    if(!marker){marker=L.marker(ll,{icon}).addTo(map);map.setView(ll,17);}
    else marker.setLatLng(ll);

    // Ajoute le nouveau point à la trace, puis, si une fenêtre de temps est active,
    // purge les points devenus plus vieux que la fenêtre pour faire "glisser" le tracé.
    const nowTs=Date.parse(p.created_at)||Date.now();
    const dernierPoint=tracePoints[tracePoints.length-1];
    if(!dernierPoint || dernierPoint.lat!==p.latitude || dernierPoint.lng!==p.longitude){
      tracePoints.push({lat:p.latitude,lng:p.longitude,ts:nowTs});
    }
    if(trackWindowMinutes){
      const seuil=Date.now()-(parseInt(trackWindowMinutes)*60*1000);
      tracePoints=tracePoints.filter(pt=>pt.ts>=seuil);
    }
    poly.setLatLngs(tracePoints.map(pt=>[pt.lat,pt.lng]));

    document.getElementById("dc-lat").textContent=p.latitude.toFixed(6)+"°";
    document.getElementById("dc-lng").textContent=p.longitude.toFixed(6)+"°";
    document.getElementById("dc-speed").textContent=(p.vitesse||0).toFixed(1)+" km/h";
    document.getElementById("dc-updated").innerHTML=`<i class="fa-regular fa-clock"></i> `+new Date().toLocaleTimeString();
    document.getElementById("tupd").innerHTML= `<i class="fa-solid fa-rotate"></i> ` + new Date().toLocaleTimeString();
    const dot=document.getElementById("dot"+selId);
    const lbl=document.getElementById("dlbl"+selId);
    if(dot)dot.className="dot live";
    if(lbl)lbl.innerHTML="Live Tracker";
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
    tb.innerHTML='<tr><td colspan="5" style="text-align:center;padding:50px;color:var(--text3)"><img class="empty-img" src="https://images.unsplash.com/photo-1619468129361-605ebea04b44?auto=format&fit=crop&w=300&h=300&q=70" alt="">Aucune donnée pour ce véhicule</td></tr>';
    return;
  }
  const rev=[...data].reverse();
  tb.innerHTML=rev.map((p,i)=>`<tr>
    <td style="color:var(--text3);font-weight:600">#${data.length-i}</td>
    <td style="color:var(--text2);font-size:13px"><i class="fa-regular fa-clock" style="margin-right:6px"></i>${p.created_at||"—"}</td>
    <td style="font-family:monospace;font-weight:600;color:var(--primary-dark)">${(p.latitude||0).toFixed(6)}</td>
    <td style="font-family:monospace;font-weight:600;color:var(--primary-dark)">${(p.longitude||0).toFixed(6)}</td>
    <td style="font-weight:600; color:${(p.vitesse||0)>80?'var(--red)':'var(--text)'}">${(p.vitesse||0).toFixed(1)} km/h</td>
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
        padding:16px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:12px">
        <div style="display:flex; align-items:center; gap:16px;">
          <div style="width:40px; height:40px; border-radius:10px; background:var(--surface2); border:1px solid var(--border); display:flex; align-items:center; justify-content:center; font-size:16px; color:var(--primary-dark)"><i class="fa-solid fa-car"></i></div>
          <div>
            <div style="font-size:15px;font-weight:700;color:var(--text)">${v.immatriculation}</div>
            <div style="font-size:13px;color:var(--text2)">${v.marque} ${v.modele}</div>
          </div>
        </div>
        <span class="pbadge"><i class="fa-solid fa-satellite-dish"></i> Actif</span>
      </div>`).join("")
    :'<div style="color:var(--text3);font-size:14px">Aucun véhicule assigné à votre compte.</div>';
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
    wrap.innerHTML='<div style="font-size:13px;color:var(--text3)"><i class="fa-solid fa-triangle-exclamation"></i> Notifications non supportées par ce navigateur.</div>';
    return;
  }
  const res=await fetch("/api/push/status").then(r=>r.json());
  const abonne=res.subscribed;
  wrap.innerHTML=`
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px">
      <div>
        <div style="font-size:15px;font-weight:600;color:var(--text)"><i class="fa-solid fa-bell" style="color:var(--primary); margin-right:8px;"></i>Alertes de disponibilité</div>
        <div style="font-size:13px;color:var(--text2);margin-top:4px">
          Recevez une notification si le suivi d'un véhicule devient indisponible.
        </div>
      </div>
      <button onclick="${abonne?'desactiverNotifs':'activerNotifs'}()"
        style="padding:10px 24px;border-radius:12px;border:none;cursor:pointer;
          font-size:14px;font-weight:600;font-family:'Poppins',sans-serif;
          background:${abonne?'var(--surface2)':'var(--primary-dark)'};
          color:${abonne?'var(--red)':'#fff'};
          border:1px solid ${abonne?'var(--border)':'transparent'}; transition:all 0.2s; box-shadow:${abonne?'none':'0 4px 12px rgba(11,61,145,0.2)'};">
        ${abonne?'<i class="fa-solid fa-bell-slash"></i> Désactiver':'<i class="fa-solid fa-bell"></i> Activer'}
      </button>
    </div>
    <div id="notif-msg" style="margin-top:16px;font-size:13px;font-weight:500;">
      Statut : ${abonne?'<span style="color:var(--green)"><i class="fa-solid fa-check-double"></i> Alertes activées</span>':'<span style="color:var(--text3)"><i class="fa-solid fa-minus"></i> Alertes désactivées</span>'}
    </div>`;
}

async function activerNotifs(){
  const msg=document.getElementById("notif-msg");
  try{
    const perm=await Notification.requestPermission();
    if(perm!=="granted"){
      if(msg)msg.innerHTML='<span style="color:var(--red)"><i class="fa-solid fa-circle-xmark"></i> Permission refusée par le navigateur.</span>';
      return;
    }
    const{publicKey}=await fetch("/api/push/vapid-public-key").then(r=>r.json());
    const reg=await navigator.serviceWorker.register("/sw.js");
    await navigator.serviceWorker.ready;
    const sub=await reg.pushManager.subscribe({
      userVisibleOnly:true,
      applicationServerKey:urlBase64ToUint8Array(publicKey)
    });
    await fetch("/api/push/subscribe",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body:JSON.stringify({subscription:sub.toJSON()})
    });
    await refreshNotifStatus();
  }catch(e){
    if(msg)msg.innerHTML=`<span style="color:var(--red)"><i class="fa-solid fa-circle-exclamation"></i> Erreur : ${e.message}</span>`;
  }
}

async function desactiverNotifs(){
  await fetch("/api/push/unsubscribe",{method:"POST"});
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
loadDashboard();
setInterval(loadDashboard, 30000);
</script></body></html>"""