# ============================================================
#  templates.py — GPS Tracker v3
#  Toutes les pages HTML (Login, Admin, User, Reset)
# ============================================================
 
# ═════════════════════════════════════════════════════════════
#  PAGE LOGIN
# ═════════════════════════════════════════════════════════════
 
LOGIN_PAGE = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Connexion</title>
<meta name="theme-color" content="#5B6EF5">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="GPS Tracker">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#F3F6FF;--surface:#FFFFFF;--border:#E5E9F7;
  --primary:#5B6EF5;--primary2:#4353E0;--cyan:#14B8A6;--violet:#8B5CF6;
  --grad:linear-gradient(135deg,#6D5DF6,#4F8EF7 55%,#14B8A6);
  --grad2:linear-gradient(120deg,#8B5CF6,#5B6EF5 50%,#14B8A6);
  --green:#10B981;--red:#F43F5E;
  --text:#111827;--text2:#6B7280;--text3:#9CA3AF;
  --font-display:'Poppins',sans-serif;--font-mono:'JetBrains Mono',monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;min-height:100vh;display:flex;
  align-items:center;justify-content:center;position:relative;overflow:hidden;
  background:
    radial-gradient(circle at 15% 15%,rgba(139,92,246,0.10),transparent 40%),
    radial-gradient(circle at 85% 20%,rgba(20,184,166,0.10),transparent 42%),
    linear-gradient(160deg,#EEF1FF 0%,#E7F3FF 55%,#EFFCF7 100%)}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;opacity:0.5;
  background-image:radial-gradient(rgba(91,110,245,0.14) 1px,transparent 1px);
  background-size:26px 26px;
  -webkit-mask-image:radial-gradient(circle at 50% 40%,#000 0%,transparent 72%);
  mask-image:radial-gradient(circle at 50% 40%,#000 0%,transparent 72%)}
.orb{position:fixed;border-radius:50%;pointer-events:none;z-index:0}
.o1{width:500px;height:500px;background:radial-gradient(circle,rgba(91,110,245,0.16),transparent);top:-120px;right:-80px}
.o2{width:400px;height:400px;background:radial-gradient(circle,rgba(20,184,166,0.14),transparent);bottom:-80px;left:-60px}
.o3{width:250px;height:250px;background:radial-gradient(circle,rgba(139,92,246,0.12),transparent);top:50%;left:30%}
.geo-tag{position:fixed;z-index:0;font-family:var(--font-mono);font-size:11px;letter-spacing:1px;
  color:rgba(91,110,245,0.35);font-weight:600;pointer-events:none;user-select:none}
.geo-tag.g1{top:26px;left:32px}
.geo-tag.g2{bottom:26px;right:34px;text-align:right}
@media(max-width:600px){.geo-tag{display:none}}
.card{position:relative;z-index:1;background:rgba(255,255,255,0.86);
  backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.9);
  border-radius:24px;padding:52px 44px;width:100%;max-width:430px;
  box-shadow:0 8px 40px rgba(91,110,245,0.14),0 2px 8px rgba(0,0,0,0.04)}
@media(max-width:480px){.card{padding:36px 24px;margin:16px;border-radius:20px}}
.logo{text-align:center;margin-bottom:38px}
.logo-wrap{position:relative;width:76px;height:76px;margin:0 auto 16px}
.logo-sweep{position:absolute;inset:-14px;border-radius:50%;
  background:conic-gradient(from 0deg,transparent 0%,rgba(91,110,245,0.35) 12%,transparent 24%);
  animation:sweep 3.2s linear infinite}
@keyframes sweep{to{transform:rotate(360deg)}}
.logo-bg{position:relative;width:72px;height:72px;border-radius:20px;background:var(--grad2);
  display:flex;align-items:center;justify-content:center;font-size:30px;
  box-shadow:0 8px 28px rgba(91,110,245,0.38)}
.logo-ring{position:absolute;inset:-5px;border-radius:25px;
  border:2px solid transparent;
  background:linear-gradient(135deg,rgba(91,110,245,0.4),rgba(20,184,166,0.4)) border-box;
  -webkit-mask:linear-gradient(#fff 0 0) padding-box,linear-gradient(#fff 0 0);
  -webkit-mask-composite:destination-out;mask-composite:exclude}
.logo h1{font-family:var(--font-display);font-size:23px;font-weight:700;letter-spacing:-0.3px;
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
input:focus{border-color:var(--primary);background:#fff;box-shadow:0 0 0 4px rgba(91,110,245,0.1)}
input::placeholder{color:var(--text3)}
.btn{width:100%;height:46px;margin-top:6px;background:var(--grad2);
  border:none;border-radius:12px;color:#fff;font-family:'Inter',sans-serif;
  font-size:14px;font-weight:600;cursor:pointer;letter-spacing:0.2px;
  box-shadow:0 4px 16px rgba(91,110,245,0.4);transition:all 0.2s}
.btn:hover{transform:translateY(-1px);box-shadow:0 8px 24px rgba(91,110,245,0.45)}
.btn:active{transform:translateY(0)}
.err{background:#FFF1F2;border:1px solid #FECDD3;color:var(--red);
  padding:11px 14px;border-radius:10px;font-size:13px;margin-bottom:16px;display:none}
.trust{display:flex;justify-content:center;gap:20px;margin-top:22px;flex-wrap:wrap}
.trust-item{display:flex;align-items:center;gap:5px;font-size:11px;color:var(--text3)}
.trust-dot{width:6px;height:6px;border-radius:50%;background:var(--grad)}
</style></head><body>
<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div>
<div class="geo-tag g1">14.6928°N<br>−17.4467°W</div>
<div class="geo-tag g2">DAKAR · SN<br>SIGNAL ACTIF</div>
<div class="card">
  <div class="logo">
    <div class="logo-wrap">
      <div class="logo-sweep"></div>
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
      background:linear-gradient(135deg,#8B5CF6,#5B6EF5,#14B8A6);border-radius:0 0 4px 4px"></div>
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
    <button onclick="doForgot()" style="width:100%;height:42px;background:linear-gradient(135deg,#8B5CF6,#5B6EF5,#14B8A6);
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
// Enregistrement Service Worker PWA
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
<meta name="theme-color" content="#5B6EF5">
<meta name="apple-mobile-web-app-capable" content="yes">
<link rel="manifest" href="/manifest.json">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --grad2:linear-gradient(120deg,#8B5CF6,#5B6EF5 50%,#14B8A6);
  --green:#10B981;--red:#F43F5E;--text:#111827;--text2:#6B7280;--text3:#9CA3AF;
  --font-display:'Poppins',sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',sans-serif;min-height:100vh;display:flex;align-items:center;
  justify-content:center;position:relative;overflow:hidden;
  background:
    radial-gradient(circle at 12% 20%,rgba(139,92,246,0.10),transparent 40%),
    radial-gradient(circle at 88% 75%,rgba(20,184,166,0.10),transparent 42%),
    linear-gradient(160deg,#EEF1FF 0%,#E7F3FF 55%,#EFFCF7 100%);
  padding:16px}
.card{position:relative;z-index:1;background:rgba(255,255,255,0.9);backdrop-filter:blur(20px);
  border:1px solid rgba(255,255,255,0.9);border-radius:24px;
  padding:48px 40px;width:100%;max-width:420px;
  box-shadow:0 8px 40px rgba(91,110,245,0.14)}
@media(max-width:480px){.card{padding:32px 22px}}
.logo{text-align:center;margin-bottom:32px}
.logo-bg{width:64px;height:64px;border-radius:18px;background:var(--grad2);
  display:flex;align-items:center;justify-content:center;font-size:26px;
  margin:0 auto 14px;box-shadow:0 6px 22px rgba(91,110,245,0.38)}
.logo h1{font-family:var(--font-display);font-size:21px;font-weight:700;
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
input:focus{border-color:#5B6EF5;background:#fff;box-shadow:0 0 0 4px rgba(91,110,245,0.1)}
.btn{width:100%;height:46px;margin-top:6px;background:var(--grad2);border:none;
  border-radius:12px;color:#fff;font-family:'Inter',sans-serif;font-size:14px;
  font-weight:600;cursor:pointer;box-shadow:0 4px 16px rgba(91,110,245,0.4);transition:all 0.2s}
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
<meta name="theme-color" content="#5B6EF5">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="GPS Tracker">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#F3F6FE;--surface:#FFFFFF;--surface2:#F7F9FF;--border:#E5E9F7;--border2:#D3DAEF;
  --primary:#5B6EF5;--primary2:#4353E0;--violet:#8B5CF6;--cyan:#14B8A6;
  --grad:linear-gradient(120deg,#8B5CF6,#5B6EF5 55%,#14B8A6);
  --grad2:linear-gradient(120deg,#5B6EF5,#14B8A6);
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-bd:rgba(16,185,129,0.2);
  --red:#F43F5E;--red-bg:rgba(244,63,94,0.08);--red-bd:rgba(244,63,94,0.2);
  --amber:#F59E0B;--text:#111827;--text2:#6B7280;--text3:#9CA3AF;
  --sidebar-w:256px;--font-display:'Poppins',sans-serif;--font-mono:'JetBrains Mono',monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scrollbar-width:thin;scrollbar-color:#C7D0F0 transparent}
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#C7D0F0;border-radius:99px}
::-webkit-scrollbar-thumb:hover{background:#A9B6EA}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);font-size:14px;display:flex;min-height:100vh;position:relative}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(circle at 8% 8%,rgba(139,92,246,0.07),transparent 32%),
    radial-gradient(circle at 96% 12%,rgba(20,184,166,0.07),transparent 32%),
    radial-gradient(circle at 50% 100%,rgba(91,110,245,0.05),transparent 40%)}
 
/* ══ SIDEBAR ══ */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:var(--surface);border-right:1px solid var(--border);
  display:flex;flex-direction:column;z-index:100;overflow:hidden;
  transition:left 0.25s ease
}
.sidebar::before{content:'';position:absolute;top:0;left:0;right:0;height:180px;
  background:linear-gradient(180deg,rgba(91,110,245,0.07),transparent);pointer-events:none}
.sidebar::after{content:'';position:absolute;inset:0;z-index:-1;opacity:0.6;pointer-events:none;
  background-image:radial-gradient(rgba(91,110,245,0.07) 1px,transparent 1px);
  background-size:20px 20px;
  -webkit-mask-image:linear-gradient(180deg,#000,transparent 55%);
  mask-image:linear-gradient(180deg,#000,transparent 55%)}
.s-logo{padding:22px 20px 18px;border-bottom:1px solid var(--border);position:relative}
.s-logo-row{display:flex;align-items:center;gap:12px}
.s-logo-icon{width:40px;height:40px;border-radius:12px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:19px;
  box-shadow:0 4px 14px rgba(91,110,245,0.38);flex-shrink:0}
.s-logo-name{font-family:var(--font-display);font-size:15px;font-weight:700;color:var(--text);letter-spacing:-0.2px}
.s-logo-sub{font-size:10px;color:var(--text3);margin-top:2px;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:600}
.s-admin{margin:14px 12px;padding:12px 14px;
  background:linear-gradient(135deg,rgba(139,92,246,0.08),rgba(91,110,245,0.05));
  border:1px solid rgba(139,92,246,0.16);border-radius:12px}
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
.nav-item:hover{background:rgba(91,110,245,0.07);color:var(--primary)}
.nav-item.active{background:linear-gradient(135deg,rgba(139,92,246,0.10),rgba(91,110,245,0.08));
  color:var(--primary);font-weight:600;border-left-color:var(--violet);
  box-shadow:inset 0 0 0 1px rgba(91,110,245,0.08)}
.nav-item.active .nav-ico{background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.nav-ico{font-size:16px;width:22px;text-align:center;flex-shrink:0;transition:all 0.15s}
.s-bottom{padding:14px 12px;border-top:1px solid var(--border);background:var(--surface);flex-shrink:0}
.btn-logout{width:100%;padding:10px 16px;background:var(--red-bg);color:var(--red);
  border:1px solid var(--red-bd);border-radius:10px;cursor:pointer;font-size:13px;font-weight:600;
  font-family:'Inter',sans-serif;transition:all 0.15s;
  display:flex;align-items:center;justify-content:center;gap:8px}
.btn-logout:hover{background:rgba(244,63,94,0.14);border-color:rgba(244,63,94,0.35)}
 
/* ══ MAIN ══ */
.main{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;min-width:0;position:relative;z-index:1}
.topbar{position:sticky;top:0;z-index:50;height:60px;padding:0 28px;
  background:rgba(255,255,255,0.75);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
  box-shadow:0 1px 4px rgba(0,0,0,0.03)}
.tb-left{display:flex;align-items:center;gap:8px}
.tb-crumb{font-size:12px;color:var(--text3);font-weight:500}
.tb-page-title{font-family:var(--font-display);font-size:18px;font-weight:700;color:var(--text);letter-spacing:-0.2px}
.tb-right{display:flex;align-items:center;gap:10px}
.clock{padding:5px 14px;background:var(--surface2);border:1px solid var(--border);
  border-radius:8px;font-size:12px;color:var(--text2);font-variant-numeric:tabular-nums;font-weight:500;
  font-family:var(--font-mono)}
.menu-btn{display:none;background:none;border:none;cursor:pointer;
  font-size:22px;color:var(--text);padding:4px 8px;margin-right:4px}
 
.content{padding:28px;flex:1}
.section{display:none}
.section.active{display:block;animation:fadeUp 0.35s cubic-bezier(.22,1,.36,1)}
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
 
/* ── Stats ── */
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:28px}
.stat{background:var(--surface);border:1px solid var(--border);border-radius:16px;
  padding:22px;position:relative;overflow:hidden;transition:all 0.25s cubic-bezier(.22,1,.36,1)}
.stat:hover{border-color:rgba(91,110,245,0.28);box-shadow:0 10px 30px rgba(91,110,245,0.14);transform:translateY(-3px)}
.stat-top{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:14px}
.stat-icon{width:44px;height:44px;border-radius:12px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:20px;position:relative;
  box-shadow:0 4px 14px rgba(91,110,245,0.32)}
.stat-icon::after{content:'';position:absolute;inset:-4px;border-radius:14px;
  border:1.5px solid rgba(91,110,245,0.25);pointer-events:none}
.stat-trend{font-size:11px;font-weight:600;padding:3px 10px;border-radius:99px;
  background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
.stat-val{font-family:var(--font-display);font-size:34px;font-weight:700;color:var(--text);letter-spacing:-1.2px;line-height:1}
.stat-lbl{font-size:12px;color:var(--text3);margin-top:5px;font-weight:500}
.stat::after{content:'';position:absolute;bottom:0;left:0;right:0;height:3px;background:var(--grad)}
.stat::before{content:'';position:absolute;top:0;right:0;width:80px;height:80px;
  background:radial-gradient(circle,rgba(91,110,245,0.07),transparent);pointer-events:none}
 
/* ── Section header ── */
.sh{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;flex-wrap:wrap;gap:10px}
.sh h2{font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--text);letter-spacing:-0.2px}
.sh-sub{font-size:13px;color:var(--text3);margin-top:2px}
 
/* ── Boutons ── */
.btn{height:40px;padding:0 18px;border:none;border-radius:10px;cursor:pointer;
  font-size:13px;font-weight:600;font-family:'Inter',sans-serif;position:relative;overflow:hidden;
  transition:all 0.2s;display:inline-flex;align-items:center;gap:7px}
.btn-primary{background:var(--grad);color:#fff;box-shadow:0 3px 12px rgba(91,110,245,0.38)}
.btn-primary:hover{transform:translateY(-1px);box-shadow:0 8px 22px rgba(91,110,245,0.48)}
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
thead{background:var(--surface2);position:relative}
thead::after{content:'';position:absolute;left:0;right:0;bottom:0;height:2px;background:var(--grad);opacity:0.5}
th{padding:12px 18px;text-align:left;font-size:11px;color:var(--text3);
  font-weight:700;text-transform:uppercase;letter-spacing:0.8px;border-bottom:1px solid var(--border)}
tbody tr{transition:all 0.15s;border-left:3px solid transparent}
tbody tr:hover{border-left-color:var(--primary)}
tbody tr:hover td{background:rgba(91,110,245,0.03)}
td{padding:14px 18px;font-size:13px;color:var(--text2);border-bottom:1px solid var(--border)}
tbody tr:last-child td{border-bottom:none}
.td-main{font-weight:600;color:var(--text)}
.device{font-size:11px;background:rgba(91,110,245,0.08);color:var(--primary);
  padding:3px 9px;border-radius:6px;font-weight:600;
  border:1px solid rgba(91,110,245,0.18);font-family:'JetBrains Mono',monospace}
.badge{padding:4px 12px;border-radius:99px;font-size:11px;font-weight:600;
  display:inline-flex;align-items:center;gap:5px}
.badge::before{content:'';width:5px;height:5px;border-radius:50%}
.badge-on{background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
.badge-on::before{background:var(--green);box-shadow:0 0 0 3px rgba(16,185,129,0.18)}
.badge-off{background:var(--red-bg);color:var(--red);border:1px solid var(--red-bd)}
.badge-off::before{background:var(--red)}
 
/* ── Positions propriétaires ── */
.prop-positions{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:20px}
.pp-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;
  padding:16px 18px;position:relative;overflow:hidden;transition:all 0.22s cubic-bezier(.22,1,.36,1)}
.pp-card:hover{border-color:rgba(91,110,245,0.22);box-shadow:0 8px 22px rgba(91,110,245,0.1);transform:translateY(-2px)}
.pp-card::after{content:'';position:absolute;bottom:0;left:0;right:0;height:2px;background:var(--grad)}
.pp-icon{font-size:22px;margin-bottom:8px}
.pp-val{font-family:var(--font-display);font-size:28px;font-weight:700;color:var(--text);letter-spacing:-1px;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.pp-lbl{font-size:12px;color:var(--text3);font-weight:500;margin-top:3px}
 
/* ── Empty ── */
.empty{padding:52px;text-align:center}
.empty-ico{font-size:44px;margin-bottom:12px;opacity:0.3}
.empty-txt{font-size:14px;font-weight:600;color:var(--text2)}
.empty-sub{font-size:12px;color:var(--text3);margin-top:4px}
 
/* ── Historique ── */
.h-filters{display:flex;gap:10px;margin-bottom:20px;align-items:center;flex-wrap:wrap}
.h-select{height:38px;padding:0 13px;background:var(--surface);border:1px solid var(--border);
  border-radius:10px;font-size:13px;font-family:'Inter',sans-serif;color:var(--text);outline:none;transition:all 0.15s}
.h-select:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(91,110,245,0.12)}
.h-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
.hs{background:var(--surface);border:1px solid var(--border);border-radius:12px;padding:14px 16px;
  border-bottom:2px solid transparent;transition:all 0.2s}
.hs:hover{border-bottom-color:var(--primary);transform:translateY(-1px)}
.hs-val{font-family:var(--font-mono);font-size:22px;font-weight:700;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hs-lbl{font-size:11px;color:var(--text3);font-weight:500;margin-top:3px}
 
/* ── Paramètres ── */
.param-card{background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:24px;margin-bottom:14px;
  transition:box-shadow 0.2s}
.param-card:hover{box-shadow:0 6px 20px rgba(91,110,245,0.06)}
.param-title{font-family:var(--font-display);font-size:14px;font-weight:700;color:var(--text);margin-bottom:3px}
.param-sub{font-size:12px;color:var(--text3);margin-bottom:18px}
.param-row{display:flex;justify-content:space-between;align-items:center;
  padding:13px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:8px}
.param-row:last-child{border-bottom:none;padding-bottom:0}
.p-lbl{font-size:13px;font-weight:500;color:var(--text)}
.p-desc{font-size:11px;color:var(--text3);margin-top:2px}
.p-badge{font-size:11px;font-weight:600;padding:4px 12px;border-radius:99px}
.p-blue{background:rgba(91,110,245,0.08);color:var(--primary);border:1px solid rgba(91,110,245,0.2)}
.p-violet{background:rgba(139,92,246,0.08);color:var(--violet);border:1px solid rgba(139,92,246,0.2)}
.p-green{background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
 
/* ── Modal ── */
.mbg{display:none;position:fixed;inset:0;background:rgba(30,38,64,0.35);
  backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);z-index:200;align-items:center;justify-content:center;padding:16px}
.mbg.open{display:flex;animation:fi 0.2s ease}
@keyframes fi{from{opacity:0}to{opacity:1}}
.modal{background:var(--surface);border:1px solid var(--border);border-radius:20px;
  padding:32px;width:100%;max-width:500px;max-height:90vh;overflow-y:auto;
  box-shadow:0 24px 70px rgba(30,38,64,0.18);animation:su 0.25s cubic-bezier(.22,1,.36,1);position:relative}
@keyframes su{from{opacity:0;transform:translateY(14px) scale(0.98)}to{opacity:1;transform:translateY(0) scale(1)}}
.modal::before{content:'';position:absolute;top:0;left:20%;right:20%;height:3px;
  background:var(--grad);border-radius:0 0 4px 4px}
.mh{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.mh h3{font-family:var(--font-display);font-size:17px;font-weight:700;color:var(--text);letter-spacing:-0.2px}
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
  box-shadow:0 0 0 3px rgba(91,110,245,0.1)}
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
              <th>Véhicules</th><th>Depuis</th><th>Statut</th><th style="min-width:200px">Action</th>
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
              <th>Propriétaire</th><th>Device ID</th><th>Statut</th><th style="min-width:200px">Action</th>
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
    <div class="fg"><label>Device ID (ESP32) *</label><input id="vd" placeholder="DK-1234-AB"/>
      <div style="font-size:11px;color:var(--text3);margin-top:4px">Utilisez l'immatriculation du véhicule comme identifiant</div>
    </div>
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
    <td style="white-space:nowrap"><div style="display:flex;gap:6px;align-items:center">
    <button class="btn btn-sm ${p.actif?'btn-danger':'btn-success'}" onclick="toggleP(${p.id})">${p.actif?'Désactiver':'Activer'}</button>
    <button class="btn btn-sm" onclick="confirmerSuppressionP(${p.id},'${p.prenom} ${p.nom}')" style="background:rgba(244,63,94,0.15);color:var(--red);border:1px solid var(--red-bd)">🗑️ Supprimer</button>
    <button class="btn btn-sm" onclick="ouvrirModifP(${p.id})" style="background:rgba(91,110,245,0.08);color:var(--primary);border:1px solid rgba(91,110,245,0.2)">✏️ Modifier</button>
    </div></td>
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
    <td style="white-space:nowrap"><div style="display:flex;gap:6px;align-items:center">
    <button class="btn btn-sm ${v.actif?'btn-danger':'btn-success'}" onclick="toggleV(${v.id})">${v.actif?'Désactiver':'Activer'}</button>
    <button class="btn btn-sm" onclick="confirmerSuppressionV(${v.id},'${v.immatriculation}')" style="background:rgba(244,63,94,0.15);color:var(--red);border:1px solid var(--red-bd)">🗑️ Supprimer</button>
    <button class="btn btn-sm" onclick="ouvrirModifV(${v.id})" style="background:rgba(91,110,245,0.08);color:var(--primary);border:1px solid rgba(91,110,245,0.2)">✏️ Modifier</button>
    </div></td>
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
    <td style="font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;
      background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent">${(p.latitude||0).toFixed(6)}</td>
    <td style="font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;
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
 
/* ── Confirmation Suppression ── */
let _supprId=null, _supprType=null;
 
function confirmerSuppressionV(id, label){
  _supprId=id; _supprType='vehicule';
  document.getElementById("suppr-msg").textContent=
    `Voulez-vous supprimer définitivement le véhicule "${label}" et toutes ses positions GPS ?`;
  document.getElementById("m-suppr").classList.add("open");
}
 
function confirmerSuppressionP(id, label){
  _supprId=id; _supprType='proprietaire';
  document.getElementById("suppr-msg").textContent=
    `Voulez-vous supprimer définitivement le propriétaire "${label}", tous ses véhicules et toutes ses positions GPS ?`;
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
    alert(data.error||"Erreur lors de la suppression");
  }
  _supprId=null; _supprType=null;
}
 
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
 
<!-- MODAL CONFIRMATION SUPPRESSION -->
<div class="mbg" id="m-suppr">
  <div class="modal" style="max-width:420px">
    <div class="mh">
      <h3 style="color:var(--red)">⚠️ Confirmation de suppression</h3>
      <button class="mc" onclick="closeM('m-suppr')">✕</button>
    </div>
    <p id="suppr-msg" style="font-size:13px;color:var(--text2);line-height:1.7;margin-bottom:20px"></p>
    <div style="background:var(--red-bg);border:1px solid var(--red-bd);border-radius:10px;
      padding:11px 14px;font-size:12px;color:var(--red);margin-bottom:20px">
      ⚠️ Cette action est irréversible. Toutes les données seront perdues définitivement.
    </div>
    <div class="ma">
      <button class="btn btn-success" onclick="closeM('m-suppr')" style="flex:1;justify-content:center">
        Annuler
      </button>
      <button class="btn btn-danger" onclick="executerSuppression()" style="flex:1;justify-content:center">
        🗑️ Supprimer définitivement
      </button>
    </div>
  </div>
</div>
 
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
<meta name="theme-color" content="#5B6EF5">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="GPS Tracker">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
:root{
  --bg:#F8F7FF;--surface:#FFFFFF;--surface2:#F9FAFB;--border:#E5E7EB;
  --primary:#5B6EF5;--violet:#8B5CF6;--cyan:#14B8A6;
  --grad:linear-gradient(135deg,#8B5CF6,#5B6EF5,#14B8A6);
  --grad2:linear-gradient(135deg,#5B6EF5,#14B8A6);
  --green:#10B981;--green-bg:rgba(16,185,129,0.08);--green-bd:rgba(16,185,129,0.2);
  --red:#F43F5E;--red-bg:rgba(244,63,94,0.08);--red-bd:rgba(244,63,94,0.2);
  --text:#111827;--text2:#6B7280;--text3:#9CA3AF;
  --sidebar-w:240px;--font-display:'Poppins',sans-serif;--font-mono:'JetBrains Mono',monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scrollbar-width:thin;scrollbar-color:#C7D0F0 transparent}
::-webkit-scrollbar{width:8px;height:8px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:#C7D0F0;border-radius:99px}
::-webkit-scrollbar-thumb:hover{background:#A9B6EA}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--text);
  height:100vh;display:flex;overflow:hidden;font-size:14px;position:relative}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(circle at 6% 10%,rgba(139,92,246,0.06),transparent 32%),
    radial-gradient(circle at 96% 90%,rgba(20,184,166,0.06),transparent 32%)}
 
/* SIDEBAR */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:var(--surface);border-right:1px solid var(--border);
  display:flex;flex-direction:column;z-index:2000;
  transition:left 0.25s ease;overflow-y:auto
}
.sidebar::before{content:'';position:absolute;top:0;left:0;right:0;height:160px;
  background:linear-gradient(180deg,rgba(139,92,246,0.05),transparent);pointer-events:none}
.sidebar::after{content:'';position:absolute;inset:0;z-index:-1;opacity:0.55;pointer-events:none;
  background-image:radial-gradient(rgba(91,110,245,0.07) 1px,transparent 1px);
  background-size:20px 20px;
  -webkit-mask-image:linear-gradient(180deg,#000,transparent 50%);
  mask-image:linear-gradient(180deg,#000,transparent 50%)}
.s-logo{padding:20px;border-bottom:1px solid var(--border);position:relative}
.s-logo-row{display:flex;align-items:center;gap:10px}
.s-logo-icon{width:36px;height:36px;border-radius:10px;background:var(--grad);
  display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;
  box-shadow:0 3px 10px rgba(91,110,245,0.3)}
.s-logo-name{font-family:var(--font-display);font-size:14px;font-weight:700;color:var(--text)}
.s-logo-sub{font-size:10px;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:600}
.s-user{margin:12px;padding:11px 13px;
  background:linear-gradient(135deg,rgba(139,92,246,0.06),rgba(91,110,245,0.04));
  border:1px solid rgba(139,92,246,0.14);border-radius:12px}
.s-user-name{font-size:13px;font-weight:600;color:var(--text)}
.s-user-role{font-size:10px;font-weight:600;margin-top:2px;
  background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.s-section{padding:14px 20px 5px;font-size:10px;font-weight:700;
  color:var(--text3);text-transform:uppercase;letter-spacing:1.5px}
.nav-item{display:flex;align-items:center;gap:10px;padding:9px 14px;
  margin:2px 8px;border-radius:10px;cursor:pointer;color:var(--text2);
  font-size:13px;font-weight:500;transition:all 0.15s;border-left:3px solid transparent}
.nav-item:hover{background:rgba(91,110,245,0.06);color:var(--primary)}
.nav-item.active{background:linear-gradient(135deg,rgba(139,92,246,0.08),rgba(91,110,245,0.06));
  color:var(--primary);font-weight:600;border-left-color:var(--violet)}
.nav-ico{font-size:15px;width:20px;text-align:center;flex-shrink:0}
.s-section2{padding:10px 20px 5px;font-size:10px;font-weight:700;
  color:var(--text3);text-transform:uppercase;letter-spacing:1.5px}
.veh-list{flex:1;overflow-y:auto;padding:4px 8px}
.veh-card{padding:11px 13px;border-radius:10px;cursor:pointer;
  border:1px solid transparent;margin-bottom:4px;transition:all 0.15s}
.veh-card:hover{background:var(--surface2);border-color:var(--border)}
.veh-card.sel{background:linear-gradient(135deg,rgba(139,92,246,0.07),rgba(91,110,245,0.05));
  border-color:rgba(91,110,245,0.2)}
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
.topbar{height:56px;padding:0 20px;background:rgba(255,255,255,0.78);
  backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;flex-shrink:0;position:relative;z-index:5}
.menu-btn{display:none;background:none;border:none;cursor:pointer;
  font-size:22px;color:var(--text);padding:4px 8px;margin-right:4px}
.tb-title{font-family:var(--font-display);font-size:15px;font-weight:700;color:var(--text);letter-spacing:-0.1px}
.live-pill{display:flex;align-items:center;gap:7px;padding:5px 13px 5px 10px;
  background:var(--green-bg);border:1px solid var(--green-bd);
  border-radius:99px;font-size:11px;color:var(--green);font-weight:600}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:0.4}}
.live-blink{position:relative;width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse 1.5s infinite}
.live-blink::after{content:'';position:absolute;inset:-5px;border-radius:50%;border:1.5px solid var(--green);
  opacity:0.6;animation:radarping 1.8s ease-out infinite}
@keyframes radarping{0%{transform:scale(0.4);opacity:0.7}100%{transform:scale(2.4);opacity:0}}
.upd{font-size:11px;color:var(--text3);margin-left:8px;font-family:var(--font-mono)}
 
.infobar{height:52px;padding:0 20px;background:var(--surface2);
  border-bottom:1px solid var(--border);display:flex;align-items:center;flex-shrink:0;position:relative}
.infobar::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--grad);opacity:0.5}
.isep{width:1px;height:24px;background:var(--border);margin:0 16px}
.iitem{display:flex;flex-direction:column}
.ilbl{font-size:9px;font-weight:700;color:var(--text3);text-transform:uppercase;letter-spacing:1px}
.ival{font-family:var(--font-mono);font-size:14px;font-weight:700;color:var(--text);margin-top:1px}
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
.h-select:focus{border-color:var(--primary);box-shadow:0 0 0 3px rgba(91,110,245,0.1)}
.htable{background:var(--surface);border:1px solid var(--border);border-radius:14px;overflow:hidden}
.htable-wrap{overflow-x:auto}
.htable table{width:100%;border-collapse:collapse;min-width:480px}
.htable th{padding:10px 14px;font-size:11px;font-weight:700;color:var(--text3);
  text-transform:uppercase;letter-spacing:0.8px;background:var(--surface2);
  border-bottom:1px solid var(--border)}
.htable td{padding:11px 14px;font-size:12px;color:var(--text2);border-bottom:1px solid var(--border)}
.htable tr:last-child td{border-bottom:none}
.htable tr:hover td{background:rgba(91,110,245,0.02)}
 
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
  .topbar{padding:0 12px;flex-shrink:0;z-index:50;position:relative}
  .tb-title{font-size:13px}
  .upd{display:none}
 
  /* Carte : hauteur limitée, topbar toujours visible */
  #tab-carte{
    height:calc(100vh - 56px);
    flex-direction:column;
    overflow:hidden;
    position:relative
  }
  #map-wrap{
    flex:1;
    min-height:0;
    overflow:hidden;
    position:relative
  }
  #map{height:100%!important}
 
  /* Bouton retour flottant sur la carte */
  #btn-retour-carte{
    display:none;
    position:absolute;
    bottom:20px;
    left:50%;
    transform:translateX(-50%);
    z-index:1000;
    background:linear-gradient(135deg,#8B5CF6,#5B6EF5);
    color:#fff;
    border:none;
    border-radius:99px;
    padding:10px 22px;
    font-size:13px;
    font-weight:600;
    font-family:Inter,sans-serif;
    cursor:pointer;
    box-shadow:0 4px 16px rgba(91,110,245,0.45);
    align-items:center;
    gap:7px;
    white-space:nowrap
  }
  #btn-retour-carte[data-active="true"]{display:flex}
 
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
  <div class="nav-item active" onclick="showTab('dashboard',this)">
    <span class="nav-ico">📊</span>Tableau de bord
  </div>
  <div class="nav-item" onclick="showTab('carte',this)">
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
 
  <!-- TABLEAU DE BORD -->
  <div id="tab-dashboard" class="usec active">
    <h2 style="font-family:var(--font-display);font-size:16px;font-weight:700;color:var(--text);margin-bottom:18px">Vue d'ensemble de la flotte</h2>
 
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:24px" id="stat-cards">
      <div style="background:var(--surface);border:1px solid var(--green-bd);border-radius:14px;padding:18px;position:relative;overflow:hidden;transition:transform .2s,box-shadow .2s" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 10px 26px rgba(16,185,129,0.14)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
        <div style="font-size:22px;margin-bottom:6px">🟢</div>
        <div style="font-family:var(--font-display);font-size:30px;font-weight:700;color:var(--green)" id="cnt-mouvement">0</div>
        <div style="font-size:12px;color:var(--text3);font-weight:500">En mouvement</div>
        <div style="position:absolute;bottom:0;left:0;right:0;height:3px;background:var(--green)"></div>
      </div>
      <div style="background:var(--surface);border:1px solid #FDE68A;border-radius:14px;padding:18px;position:relative;overflow:hidden;transition:transform .2s,box-shadow .2s" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 10px 26px rgba(245,158,11,0.14)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
        <div style="font-size:22px;margin-bottom:6px">🟡</div>
        <div style="font-family:var(--font-display);font-size:30px;font-weight:700;color:#D97706" id="cnt-immobile">0</div>
        <div style="font-size:12px;color:var(--text3);font-weight:500">Immobile</div>
        <div style="position:absolute;bottom:0;left:0;right:0;height:3px;background:#F59E0B"></div>
      </div>
      <div style="background:var(--surface);border:1px solid var(--red-bd);border-radius:14px;padding:18px;position:relative;overflow:hidden;transition:transform .2s,box-shadow .2s" onmouseover="this.style.transform='translateY(-3px)';this.style.boxShadow='0 10px 26px rgba(244,63,94,0.14)'" onmouseout="this.style.transform='none';this.style.boxShadow='none'">
        <div style="font-size:22px;margin-bottom:6px">🔴</div>
        <div style="font-family:var(--font-display);font-size:30px;font-weight:700;color:var(--red)" id="cnt-signal">0</div>
        <div style="font-size:12px;color:var(--text3);font-weight:500">Sans signal</div>
        <div style="position:absolute;bottom:0;left:0;right:0;height:3px;background:var(--red)"></div>
      </div>
    </div>
 
    <div id="dash-list" style="display:flex;flex-direction:column;gap:10px">
      <div style="text-align:center;padding:30px;color:var(--text3);font-size:13px">Chargement...</div>
    </div>
  </div>
 
  <!-- CARTE -->
  <div id="tab-carte" style="flex:1;display:none;flex-direction:column;overflow:hidden">
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
    <div id="map-wrap" style="flex:1;display:none;position:relative">
      <div id="map" style="height:100%"></div>
      <button id="btn-retour-carte" onclick="toggleMenu()">
        ☰ Menu
      </button>
    </div>
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
  // Cacher bouton retour si on quitte la carte
  const btnRetour=document.getElementById("btn-retour-carte");
  if(btnRetour)delete btnRetour.dataset.active;
  if(n==="dashboard")loadDashboard();
  if(n==="historique")initUH();
  if(n==="parametres")loadParams();
  closeMenu();
}
 
/* ── Tableau de bord : mouvement / immobile / sans signal ── */
let _dashInterval=null;
 
async function loadDashboard(){
  try{
    const data = await fetch("/api/user/vehicules/statut").then(r=>r.json());
 
    const nbMouvement = data.filter(v=>v.statut==='mouvement').length;
    const nbImmobile  = data.filter(v=>v.statut==='immobile').length;
    const nbSignal    = data.filter(v=>v.statut==='sans_signal').length;
 
    document.getElementById("cnt-mouvement").textContent = nbMouvement;
    document.getElementById("cnt-immobile").textContent  = nbImmobile;
    document.getElementById("cnt-signal").textContent    = nbSignal;
 
    const list = document.getElementById("dash-list");
    if(!data.length){
      list.innerHTML = '<div style="text-align:center;padding:30px;color:var(--text3);font-size:13px">Aucun véhicule associé</div>';
      return;
    }
 
    const config = {
      mouvement:  {icone:'🟢', label:'En mouvement', couleur:'var(--green)', bg:'var(--green-bg)', bd:'var(--green-bd)'},
      immobile:   {icone:'🟡', label:'Immobile',      couleur:'#D97706',     bg:'rgba(245,158,11,0.08)', bd:'#FDE68A'},
      sans_signal:{icone:'🔴', label:'Sans signal',   couleur:'var(--red)',  bg:'var(--red-bg)', bd:'var(--red-bd)'}
    };
 
    list.innerHTML = data.map(v=>{
      const cfg = config[v.statut];
      const infoSignal = v.statut==='sans_signal'
        ? (v.minutes_sans_signal!==null
            ? `Aucun signal depuis ${Math.round(v.minutes_sans_signal)} min`
            : 'Aucune position enregistrée')
        : `${(v.vitesse||0).toFixed(0)} km/h · ${v.satellites||0} satellites`;
 
      return `<div onclick="selV(${v.id},'${v.marque} ${v.modele}','${v.immatriculation}')"
        style="display:flex;align-items:center;justify-content:space-between;cursor:pointer;
          background:var(--surface);border:1px solid var(--border);border-radius:12px;
          padding:14px 16px;transition:all 0.15s"
        onmouseover="this.style.borderColor='${cfg.couleur}'"
        onmouseout="this.style.borderColor='var(--border)'">
        <div style="display:flex;align-items:center;gap:12px">
          <div style="width:38px;height:38px;border-radius:10px;background:${cfg.bg};
            display:flex;align-items:center;justify-content:center;font-size:17px">${cfg.icone}</div>
          <div>
            <div style="font-size:13px;font-weight:700;color:var(--text)">${v.immatriculation}</div>
            <div style="font-size:11px;color:var(--text3)">${v.marque} ${v.modele}</div>
          </div>
        </div>
        <div style="text-align:right">
          <div style="font-size:11px;font-weight:600;padding:3px 10px;border-radius:99px;
            background:${cfg.bg};color:${cfg.couleur};border:1px solid ${cfg.bd};display:inline-block">
            ${cfg.label}
          </div>
          <div style="font-size:11px;color:var(--text3);margin-top:4px">${infoSignal}</div>
        </div>
      </div>`;
    }).join("");
  }catch(e){
    console.log("Erreur dashboard:",e);
  }
}
 
function initMap(){
  if(map)return;
  map=L.map("map",{zoomControl:true}).setView([14.8500,-15.8833],15);
  L.tileLayer("https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",{
    attribution:"© Esri, Maxar, Earthstar Geographics",
    maxZoom:20,
        maxNativeZoom:17,
    minZoom:3
  }).addTo(map);
  poly=L.polyline([],{color:"#5B6EF5",weight:4,opacity:0.85}).addTo(map);
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
  // Affiche bouton retour sur mobile (géré par CSS media query, juste on l'active)
  const btnRetour = document.getElementById("btn-retour-carte");
  if(btnRetour) btnRetour.dataset.active="true";
  /* Ferme le menu sur mobile après sélection */
  closeMenu();
  /* Bascule vers l'onglet carte */
  document.getElementById("tab-carte").style.display="flex";
  document.querySelectorAll(".usec").forEach(s=>s.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  const navItems = document.querySelectorAll(".nav-item");
  if(navItems[1]) navItems[1].classList.add("active"); // "Carte GPS" est en 2e position
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
      html:`<div style="position:relative;width:24px;height:24px">
        <div style="position:absolute;top:0;left:0;width:24px;height:24px;
          background:rgba(244,63,94,0.35);border-radius:50%;
          animation:pulseMarker 1.5s infinite"></div>
        <div style="position:absolute;top:5px;left:5px;width:14px;height:14px;
          background:linear-gradient(135deg,#F43F5E,#DC2626);
          border:3px solid #fff;border-radius:50%;
          box-shadow:0 2px 8px rgba(0,0,0,0.5)"></div>
      </div>
      <style>
        @keyframes pulseMarker{
          0%{transform:scale(0.6);opacity:0.8}
          100%{transform:scale(1.8);opacity:0}
        }
      </style>`,
      iconSize:[24,24],iconAnchor:[12,12]});
    if(!marker){marker=L.marker(ll,{icon}).addTo(map);map.setView(ll,17);}
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
    <td style="font-family:'JetBrains Mono',monospace;font-weight:600;font-size:12px;
      background:var(--grad2);-webkit-background-clip:text;-webkit-text-fill-color:transparent">${(p.latitude||0).toFixed(6)}</td>
    <td style="font-family:'JetBrains Mono',monospace;font-weight:600;font-size:12px;
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
          background:${abonne?'rgba(244,63,94,0.08)':'linear-gradient(135deg,#8B5CF6,#5B6EF5)'};
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
loadDashboard();
setInterval(loadDashboard, 30000);
</script></body></html>"""
