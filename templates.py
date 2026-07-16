# ============================================================
#  templates.py — GPS Tracker v3 (SaaS Modern Redesign)
#  Toutes les pages HTML (Login, Admin, User, Reset)
# ============================================================

# ═════════════════════════════════════════════════════════════
#  PAGE LOGIN (Apple / Stripe Premium Style)
# ═════════════════════════════════════════════════════════════

LOGIN_PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>GPS Tracker — Connexion</title>
  <meta name="theme-color" content="#0B3D91">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="GPS Tracker">
  <link rel="manifest" href="/manifest.json">
  <link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg: #F5F7FA;
      --surface: #FFFFFF;
      --border: #E2E8F0;
      --primary-light: #4FC3F7;
      --primary-dark: #0B3D91;
      --primary-hover: #072a66;
      --grad: linear-gradient(135deg, #0B3D91, #4FC3F7);
      --green: #10B981;
      --red: #F43F5E;
      --text: #0F172A;
      --text-muted: #64748B;
      --text-light: #94A3B8;
      --shadow-sm: 0 1px 3px rgba(11, 61, 145, 0.05);
      --shadow-lg: 0 25px 50px -12px rgba(11, 61, 145, 0.12);
      --radius-lg: 24px;
      --radius-md: 14px;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Inter', sans-serif;
      min-height: 100vh;
      display: flex;
      background: var(--bg);
      color: var(--text);
      overflow-x: hidden;
    }
    
    /* Split Layout */
    .login-container {
      display: flex;
      width: 100%;
      min-height: 100vh;
    }
    
    /* Left Side: Premium Modern Art Vector Illustration & Tech specs */
    .brand-side {
      flex: 1.2;
      background: linear-gradient(145deg, #051b40 0%, #0B3D91 100%);
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 60px;
      color: #FFFFFF;
      overflow: hidden;
    }
    .brand-side::before {
      content: '';
      position: absolute;
      inset: 0;
      background-image: radial-gradient(circle at 80% 20%, rgba(79, 195, 247, 0.15) 0%, transparent 50%),
                        radial-gradient(circle at 20% 80%, rgba(11, 61, 145, 0.4) 0%, transparent 60%);
      pointer-events: none;
    }
    .brand-header {
      display: flex;
      align-items: center;
      gap: 12px;
      z-index: 2;
    }
    .brand-logo-icon {
      width: 44px;
      height: 44px;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      backdrop-filter: blur(8px);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      color: var(--primary-light);
    }
    .brand-title {
      font-size: 20px;
      font-weight: 700;
      letter-spacing: -0.5px;
    }
    
    .brand-visual {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      z-index: 2;
    }
    /* Vector IoT / GPS Modern Illustration */
    .vector-art {
      width: 80%;
      max-width: 450px;
      height: auto;
      filter: drop-shadow(0 20px 30px rgba(0,0,0,0.3));
      animation: float 6s ease-in-out infinite;
    }
    @keyframes float {
      0%, 100% { transform: translateY(0px) rotate(0deg); }
      50% { transform: translateY(-15px) rotate(1deg); }
    }

    .brand-footer {
      z-index: 2;
    }
    .brand-tagline {
      font-size: 32px;
      font-weight: 700;
      line-height: 1.25;
      margin-bottom: 16px;
      letter-spacing: -1px;
    }
    .brand-desc {
      font-size: 15px;
      color: rgba(255, 255, 255, 0.7);
      max-width: 480px;
      line-height: 1.6;
    }

    /* Right Side: Clean Form */
    .form-side {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 40px;
      background: var(--bg);
      position: relative;
    }
    
    .form-card {
      width: 100%;
      max-width: 440px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 48px 40px;
      box-shadow: var(--shadow-lg);
      position: relative;
    }
    
    .form-header {
      margin-bottom: 36px;
    }
    .form-header h2 {
      font-size: 26px;
      font-weight: 700;
      color: var(--primary-dark);
      letter-spacing: -0.5px;
    }
    .form-header p {
      color: var(--text-muted);
      font-size: 14px;
      margin-top: 6px;
    }
    
    .fg { margin-bottom: 24px; position: relative; }
    .fg label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      color: var(--text);
      margin-bottom: 8px;
    }
    .iw { position: relative; }
    .ii {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 16px;
      color: var(--text-light);
      transition: color 0.25s ease;
    }
    input {
      width: 100%;
      height: 48px;
      padding: 0 16px 0 46px;
      background: var(--bg);
      border: 1.5px solid var(--border);
      border-radius: var(--radius-md);
      font-size: 14px;
      font-family: 'Inter', sans-serif;
      color: var(--text);
      outline: none;
      transition: all 0.25s ease;
    }
    input:hover { border-color: #CBD5E1; }
    input:focus {
      border-color: var(--primary-light);
      background: #FFFFFF;
      box-shadow: 0 0 0 4px rgba(79, 195, 247, 0.15);
    }
    input:focus + .ii, .iw:focus-within .ii { color: var(--primary-dark); }
    
    .btn {
      width: 100%;
      height: 50px;
      background: var(--primary-dark);
      border: none;
      border-radius: var(--radius-md);
      color: #FFFFFF;
      font-family: 'Inter', sans-serif;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(11, 61, 145, 0.15);
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }
    .btn:hover {
      background: var(--primary-hover);
      transform: translateY(-1px);
      box-shadow: 0 8px 20px rgba(11, 61, 145, 0.25);
    }
    .btn:active { transform: translateY(0); }
    
    .err {
      background: #FFF1F2;
      border: 1px solid #FECDD3;
      color: var(--red);
      padding: 12px 16px;
      border-radius: var(--radius-md);
      font-size: 13px;
      margin-bottom: 24px;
      display: none;
      align-items: center;
      gap: 10px;
      font-weight: 500;
      animation: shake 0.4s ease;
    }
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      25% { transform: translateX(-4px); }
      75% { transform: translateX(4px); }
    }
    
    .forgot-link {
      display: inline-block;
      margin-top: 16px;
      font-size: 13px;
      color: var(--text-muted);
      text-decoration: none;
      font-weight: 500;
      transition: color 0.2s ease;
    }
    .forgot-link:hover { color: var(--primary-dark); }
    
    .trust-badge-row {
      display: flex;
      justify-content: space-between;
      margin-top: 40px;
      padding-top: 24px;
      border-top: 1px solid var(--border);
    }
    .trust-badge {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .trust-badge i { color: var(--primary-light); font-size: 12px; }

    /* Modal Backdrop Blur */
    .modal-backdrop {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.4);
      backdrop-filter: blur(12px);
      z-index: 200;
      align-items: center;
      justify-content: center;
      padding: 16px;
      animation: fadeIn 0.3s ease;
    }
    @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

    .modal-box {
      background: var(--surface);
      border-radius: var(--radius-lg);
      padding: 40px;
      width: 100%;
      max-width: 440px;
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--border);
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .brand-side { display: none; }
    }
    @media (max-width: 480px) {
      .form-side { padding: 16px; }
      .form-card { padding: 32px 20px; border-radius: 20px; }
    }
  </style>
</head>
<body>

<div class="login-container">
  <!-- Left Side Visual Section -->
  <div class="brand-side">
    <div class="brand-header">
      <div class="brand-logo-icon"><i class="fa-solid fa-satellite-dish"></i></div>
      <span class="brand-title">FleetTracker Enterprise</span>
    </div>
    
    <div class="brand-visual">
      <!-- Modern vector graphic mapping representation -->
      <svg class="vector-art" viewBox="0 0 500 500" fill="none" xmlns="http://www.w3.org/2000/svg">
        <circle cx="250" cy="250" r="180" stroke="#4FC3F7" stroke-width="1.5" stroke-dasharray="8 8" opacity="0.4"/>
        <circle cx="250" cy="250" r="120" stroke="#4FC3F7" stroke-width="2" opacity="0.6"/>
        <!-- Central Globe -->
        <circle cx="250" cy="250" r="60" fill="url(#globeGrad)"/>
        <!-- Orbits and Nodes -->
        <circle cx="160" cy="180" r="8" fill="#4FC3F7" filter="drop-shadow(0 0 8px #4FC3F7)"/>
        <line x1="250" y1="250" x2="160" y2="180" stroke="#4FC3F7" stroke-width="2" opacity="0.5"/>
        <circle cx="340" cy="210" r="10" fill="#FFFFFF" filter="drop-shadow(0 0 10px #FFFFFF)"/>
        <line x1="250" y1="250" x2="340" y2="210" stroke="#FFFFFF" stroke-width="2" opacity="0.5"/>
        <circle cx="220" cy="330" r="6" fill="#4FC3F7" opacity="0.8"/>
        <line x1="250" y1="250" x2="220" y2="330" stroke="#4FC3F7" stroke-width="1.5" opacity="0.4"/>
        <!-- Satellite icon -->
        <g transform="translate(350, 90)">
          <path d="M10 30 L30 10 M20 20 L40 40" stroke="#4FC3F7" stroke-width="3"/>
          <rect x="5" y="5" width="16" height="16" rx="4" fill="#FFFFFF"/>
        </g>
        <defs>
          <linearGradient id="globeGrad" x1="190" y1="190" x2="310" y2="310" gradientUnits="userSpaceOnUse">
            <stop stop-color="#4FC3F7"/>
            <stop offset="1" stop-color="#0B3D91"/>
          </linearGradient>
        </defs>
      </svg>
    </div>
    
    <div class="brand-footer">
      <h3 class="brand-tagline">Géolocalisation intelligente de flotte en temps réel</h3>
      <p class="brand-desc">Optimisez la gestion de vos véhicules, analysez les trajets et sécurisez vos équipements via une infrastructure IoT cloud hautement disponible.</p>
    </div>
  </div>

  <!-- Right Side Form Section -->
  <div class="form-side">
    <div class="form-card">
      <div class="form-header">
        <h2>Se connecter</h2>
        <p>Ravi de vous revoir. Entrez vos identifiants.</p>
      </div>
      
      <div class="err" id="err">
        <i class="fa-solid fa-circle-exclamation"></i>
        <span id="err-text"></span>
      </div>
      
      <div class="fg">
        <label>Adresse email</label>
        <div class="iw">
          <i class="fa-solid fa-envelope ii"></i>
          <input type="email" id="email" placeholder="nom@entreprise.com" autocomplete="email"/>
        </div>
      </div>
      
      <div class="fg">
        <label>Mot de passe</label>
        <div class="iw">
          <i class="fa-solid fa-lock ii"></i>
          <input type="password" id="pwd" placeholder="••••••••" onkeydown="if(event.key==='Enter')doLogin()"/>
        </div>
      </div>
      
      <button class="btn" onclick="doLogin()">
        Se connecter <i class="fa-solid fa-arrow-right"></i>
      </button>
      
      <div style="text-align: center;">
        <a href="#" onclick="showForgot()" class="forgot-link">Mot de passe oublié ?</a>
      </div>
      
      <div class="trust-badge-row">
        <div class="trust-badge"><i class="fa-solid fa-shield-halved"></i> Cloud Secure</div>
        <div class="trust-badge"><i class="fa-solid fa-bolt"></i> Temps Réel</div>
      </div>
    </div>
  </div>
</div>

<!-- Password Recovery Modal -->
<div id="forgot-bg" class="modal-backdrop">
  <div class="modal-box">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
      <h3 style="font-size: 18px; font-weight: 700; color: var(--primary-dark);">Réinitialisation</h3>
      <button onclick="hideForgot()" style="width: 32px; height: 32px; border-radius: 8px; border: 1px solid var(--border); background: var(--bg); cursor: pointer;"><i class="fa-solid fa-xmark"></i></button>
    </div>
    
    <p style="font-size: 13.5px; color: var(--text-muted); margin-bottom: 24px; line-height: 1.5;">
      Entrez votre adresse email de connexion pour recevoir un lien sécurisé de réinitialisation.
    </p>
    
    <div id="forgot-err" class="err" style="margin-bottom: 16px;"></div>
    <div id="forgot-ok" style="background: #ECFDF5; border: 1px solid #A7F3D0; color: #059669; padding: 12px 16px; border-radius: var(--radius-md); font-size: 13px; margin-bottom: 16px; display: none; font-weight: 500;"></div>
    
    <div class="fg" style="margin-bottom: 24px;">
      <label>Email professionnel</label>
      <div class="iw">
        <i class="fa-solid fa-envelope ii"></i>
        <input type="email" id="forgot-email" placeholder="nom@entreprise.com" onkeydown="if(event.key==='Enter')doForgot()"/>
      </div>
    </div>
    
    <button onclick="doForgot()" class="btn">
      Envoyer le lien <i class="fa-solid fa-paper-plane"></i>
    </button>
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
  try {
    const res=await fetch("/api/login",{method:"POST",headers:{"Content-Type":"application/json"},
      body:JSON.stringify({email,mot_de_passe:pwd})});
    const data=await res.json();
    if(res.ok){window.location.href=data.role==="admin"?"/admin":"/dashboard";}
    else{errText.textContent=data.error||"Identifiants incorrects.";err.style.display="flex";}
  } catch(e) {
    errText.textContent="Erreur de connexion serveur.";err.style.display="flex";
  }
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
  if(!email){err.textContent="Veuillez entrer votre email.";err.style.display="flex";return;}
  try {
    await fetch("/api/forgot-password",{method:"POST",
      headers:{"Content-Type":"application/json"},body:JSON.stringify({email})});
    ok.innerHTML="<i class='fa-solid fa-circle-check'></i> Si cet email existe, un lien vient de vous être envoyé.";
    ok.style.display="block";
  } catch(e) {
    err.textContent="Erreur lors de la demande.";err.style.display="flex";
  }
}
</script>
</body>
</html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE RESET PASSWORD (Premium Stripe Style)
# ═════════════════════════════════════════════════════════════

RESET_PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>GPS Tracker — Nouveau mot de passe</title>
  <meta name="theme-color" content="#0B3D91">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <link rel="manifest" href="/manifest.json">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg: #F5F7FA;
      --surface: #FFFFFF;
      --border: #E2E8F0;
      --primary-light: #4FC3F7;
      --primary-dark: #0B3D91;
      --grad: linear-gradient(135deg, #0B3D91, #4FC3F7);
      --green: #10B981;
      --red: #F43F5E;
      --text: #0F172A;
      --text-muted: #64748B;
      --text-light: #94A3B8;
      --shadow-lg: 0 25px 50px -12px rgba(11, 61, 145, 0.1);
      --radius-lg: 24px;
      --radius-md: 14px;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Inter', sans-serif;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--bg);
      padding: 16px;
      color: var(--text);
    }
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 48px 40px;
      width: 100%;
      max-width: 440px;
      box-shadow: var(--shadow-lg);
    }
    .logo { text-align: center; margin-bottom: 36px; }
    .logo-bg {
      width: 60px;
      height: 60px;
      border-radius: 16px;
      background: var(--grad);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      color: #FFFFFF;
      margin: 0 auto 16px;
      box-shadow: 0 10px 20px rgba(79, 195, 247, 0.3);
    }
    .logo h1 { font-size: 22px; font-weight: 700; color: var(--primary-dark); letter-spacing: -0.5px; }
    .logo p { color: var(--text-muted); font-size: 14px; margin-top: 6px; }
    
    .fg { margin-bottom: 24px; }
    .fg label { display: block; font-size: 13px; font-weight: 600; color: var(--text); margin-bottom: 8px; }
    .iw { position: relative; }
    .ii {
      position: absolute;
      left: 16px;
      top: 50%;
      transform: translateY(-50%);
      font-size: 16px;
      color: var(--text-light);
      transition: color 0.25s ease;
    }
    input {
      width: 100%;
      height: 48px;
      padding: 0 16px 0 46px;
      background: var(--bg);
      border: 1.5px solid var(--border);
      border-radius: var(--radius-md);
      font-size: 14px;
      font-family: 'Inter', sans-serif;
      color: var(--text);
      outline: none;
      transition: all 0.25s ease;
    }
    input:focus {
      border-color: var(--primary-light);
      background: #FFFFFF;
      box-shadow: 0 0 0 4px rgba(79, 195, 247, 0.15);
    }
    input:focus + .ii, .iw:focus-within .ii { color: var(--primary-dark); }
    
    .btn {
      width: 100%;
      height: 48px;
      background: var(--primary-dark);
      border: none;
      border-radius: var(--radius-md);
      color: #FFFFFF;
      font-family: 'Inter', sans-serif;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(11, 61, 145, 0.15);
      transition: all 0.25s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }
    .btn:hover {
      background: var(--primary-hover);
      transform: translateY(-1px);
      box-shadow: 0 8px 20px rgba(11, 61, 145, 0.25);
    }
    
    .err {
      background: #FFF1F2;
      border: 1px solid #FECDD3;
      color: var(--red);
      padding: 12px 16px;
      border-radius: var(--radius-md);
      font-size: 13px;
      margin-bottom: 24px;
      display: none;
      font-weight: 500;
    }
    .ok {
      background: #ECFDF5;
      border: 1px solid #A7F3D0;
      color: var(--green);
      padding: 12px 16px;
      border-radius: var(--radius-md);
      font-size: 13px;
      margin-bottom: 24px;
      display: none;
      font-weight: 500;
    }
    .exp {
      background: #FFFBEB;
      border: 1px solid #FDE68A;
      color: #B45309;
      padding: 24px;
      border-radius: var(--radius-lg);
      text-align: center;
      font-size: 14px;
      display: none;
      font-weight: 500;
    }
    @media (max-width: 480px) {
      .card { padding: 32px 20px; }
    }
  </style>
</head>
<body>
<div class="card">
  <div class="logo">
    <div class="logo-bg"><i class="fa-solid fa-shield-halved"></i></div>
    <h1>Nouveau mot de passe</h1>
    <p>Sécurisez l'accès à votre espace client</p>
  </div>
  
  <div class="exp" id="exp">
    <div style="font-size: 36px; margin-bottom: 12px; color: #D97706;"><i class="fa-solid fa-clock-rotate-left"></i></div>
    <div style="font-weight: 700; margin-bottom: 8px; font-size: 16px;">Lien expiré ou invalide</div>
    <div style="color: #92400E; font-size: 13px;">Cette demande n'est plus valide. Veuillez relancer une réinitialisation de mot de passe.</div>
  </div>
  
  <div id="form-wrap">
    <div class="err" id="err"></div>
    <div class="ok" id="ok"></div>
    
    <div class="fg">
      <label>Nouveau mot de passe</label>
      <div class="iw">
        <i class="fa-solid fa-lock ii"></i>
        <input type="password" id="pwd1" placeholder="Minimum 6 caractères"/>
      </div>
    </div>
    
    <div class="fg">
      <label>Confirmer le mot de passe</label>
      <div class="iw">
        <i class="fa-solid fa-lock-open ii"></i>
        <input type="password" id="pwd2" placeholder="Saisir à nouveau" onkeydown="if(event.key==='Enter')doReset()"/>
      </div>
    </div>
    
    <button class="btn" onclick="doReset()">
      Enregistrer le mot de passe <i class="fa-solid fa-check"></i>
    </button>
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
  if(!pwd1||!pwd2){err.innerHTML="<i class='fa-solid fa-circle-exclamation'></i> Veuillez remplir tous les champs.";err.style.display="block";return;}
  if(pwd1.length<6){err.innerHTML="<i class='fa-solid fa-circle-exclamation'></i> Doit comporter au moins 6 caractères.";err.style.display="block";return;}
  if(pwd1!==pwd2){err.innerHTML="<i class='fa-solid fa-circle-exclamation'></i> Les mots de passe ne correspondent pas.";err.style.display="block";return;}
  const res=await fetch("/api/reset-password",{method:"POST",
    headers:{"Content-Type":"application/json"},
    body:JSON.stringify({token,mot_de_passe:pwd1})});
  const data=await res.json();
  if(res.ok){
    ok.innerHTML="<i class='fa-solid fa-circle-check'></i> Enregistrement réussi ! Redirection...";ok.style.display="block";
    document.getElementById("pwd1").value="";document.getElementById("pwd2").value="";
    setTimeout(()=>window.location.href="/",2000);
  }else{err.innerHTML="<i class='fa-solid fa-circle-exclamation'></i> "+(data.error||"Erreur.");err.style.display="block";}
}
init();
</script>
</body>
</html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE ADMIN (Vercel & Stripe Dashboard Quality UI)
# ═════════════════════════════════════════════════════════════

ADMIN_PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>GPS Tracker — Centre d'administration</title>
  <meta name="theme-color" content="#0B3D91">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="GPS Tracker">
  <link rel="manifest" href="/manifest.json">
  <link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --bg: #F8FAFC;
      --surface: #FFFFFF;
      --surface2: #F1F5F9;
      --border: #E2E8F0;
      --primary: #4FC3F7;
      --primary-dark: #0B3D91;
      --primary-hover: #082d6b;
      --grad: linear-gradient(135deg, #0B3D91, #4FC3F7);
      --grad-light: linear-gradient(135deg, rgba(79, 195, 247, 0.08), rgba(11, 61, 145, 0.04));
      --green: #10B981;
      --green-bg: #ECFDF5;
      --green-bd: #A7F3D0;
      --red: #EF4444;
      --red-bg: #FEF2F2;
      --red-bd: #FEE2E2;
      --amber: #F59E0B;
      --text: #0F172A;
      --text-muted: #475569;
      --text-light: #94A3B8;
      --sidebar-w: 270px;
      --radius-lg: 16px;
      --radius-md: 10px;
      --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05);
      --shadow-md: 0 4px 12px -2px rgba(15, 23, 42, 0.05), 0 2px 4px -1px rgba(15, 23, 42, 0.03);
      --shadow-lg: 0 20px 25px -5px rgba(15, 23, 42, 0.1);
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text);
      font-size: 14px;
      display: flex;
      min-height: 100vh;
    }

    /* ══ SIDEBAR ══ */
    .sidebar {
      position: fixed; top: 0; left: 0; bottom: 0; width: var(--sidebar-w);
      background: var(--surface); border-right: 1px solid var(--border);
      display: flex; flex-direction: column; z-index: 100;
      transition: left 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .s-logo { padding: 24px; border-bottom: 1px solid var(--border); }
    .s-logo-row { display: flex; align-items: center; gap: 12px; }
    .s-logo-icon {
      width: 38px; height: 38px; border-radius: 10px; background: var(--grad); color: #FFF;
      display: flex; align-items: center; justify-content: center; font-size: 18px;
      box-shadow: 0 4px 12px rgba(79, 195, 247, 0.25); flex-shrink: 0;
    }
    .s-logo-name { font-size: 16px; font-weight: 700; color: var(--primary-dark); letter-spacing: -0.5px; }
    .s-logo-sub { font-size: 11px; color: var(--text-light); margin-top: 1px; font-weight: 600; text-transform: uppercase; }

    .s-admin { margin: 20px 16px; padding: 14px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius-md); }
    .s-admin-row { display: flex; align-items: center; gap: 12px; }
    .s-avatar {
      width: 36px; height: 36px; border-radius: 8px; background: var(--grad-light); color: var(--primary-dark);
      display: flex; align-items: center; justify-content: center; font-size: 16px; flex-shrink: 0;
    }
    .s-admin-name { font-size: 13.5px; font-weight: 600; color: var(--text); }
    .s-admin-role { font-size: 10px; font-weight: 700; color: var(--primary-dark); text-transform: uppercase; opacity: 0.8; }

    .s-nav { flex: 1; padding: 0 16px; overflow-y: auto; }
    .nav-item {
      display: flex; align-items: center; gap: 12px; padding: 10px 14px;
      border-radius: var(--radius-md); cursor: pointer; color: var(--text-muted); font-size: 13.5px;
      font-weight: 500; transition: all 0.2s ease; margin-bottom: 4px;
    }
    .nav-item:hover { background: var(--surface2); color: var(--text); }
    .nav-item.active { background: var(--primary-dark); color: #FFFFFF; font-weight: 600; box-shadow: var(--shadow-sm); }
    .nav-ico { font-size: 15px; width: 20px; text-align: center; flex-shrink: 0; }

    .s-bottom { padding: 20px 16px; border-top: 1px solid var(--border); }
    .btn-logout {
      width: 100%; padding: 10px; background: var(--surface); color: var(--text-muted);
      border: 1px solid var(--border); border-radius: var(--radius-md); cursor: pointer; font-size: 13px; font-weight: 600;
      font-family: 'Inter', sans-serif; transition: all 0.2s ease;
      display: flex; align-items: center; justify-content: center; gap: 8px;
    }
    .btn-logout:hover { background: var(--red-bg); color: var(--red); border-color: var(--red-bd); }

    /* ══ MAIN CONTENT ══ */
    .main { margin-left: var(--sidebar-w); flex: 1; display: flex; flex-direction: column; min-width: 0; }
    .topbar {
      position: sticky; top: 0; z-index: 50; height: 64px; padding: 0 32px;
      background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border); display: flex; align-items: center; justify-content: space-between;
    }
    .tb-left { display: flex; align-items: center; gap: 12px; }
    .menu-btn {
      display: none; background: none; border: none; cursor: pointer;
      font-size: 18px; color: var(--text); padding: 6px; border-radius: 6px;
    }
    .tb-crumb { font-size: 11px; color: var(--text-light); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
    .tb-page-title { font-size: 18px; font-weight: 700; color: var(--primary-dark); letter-spacing: -0.3px; }
    .clock {
      padding: 6px 12px; background: var(--surface); border: 1px solid var(--border);
      border-radius: var(--radius-md); font-size: 12.5px; color: var(--primary-dark); font-weight: 600;
      box-shadow: var(--shadow-sm); display: flex; align-items: center; gap: 6px;
    }

    .content { padding: 32px; flex: 1; max-width: 1400px; width: 100%; margin: 0 auto; }
    .section { display: none; }
    .section.active { display: block; animation: fadeInUp 0.35s cubic-bezier(0.16, 1, 0.3, 1); }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

    /* Stats Grid */
    .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-bottom: 32px; }
    .stat {
      background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
      padding: 24px; transition: all 0.25s ease; box-shadow: var(--shadow-sm);
    }
    .stat:hover { border-color: var(--primary-light); transform: translateY(-2px); box-shadow: var(--shadow-md); }
    .stat-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
    .stat-icon {
      width: 44px; height: 44px; border-radius: 10px; background: var(--grad-light); color: var(--primary-dark);
      display: flex; align-items: center; justify-content: center; font-size: 18px;
    }
    .stat-trend { font-size: 11px; font-weight: 600; padding: 4px 8px; border-radius: 12px; background: var(--green-bg); color: var(--green); }
    .stat-val { font-size: 32px; font-weight: 700; color: var(--text); letter-spacing: -1px; line-height: 1.1; }
    .stat-lbl { font-size: 13px; color: var(--text-muted); margin-top: 6px; font-weight: 500; }

    /* Section Header */
    .sh { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; flex-wrap: wrap; gap: 16px; }
    .sh h2 { font-size: 20px; font-weight: 700; color: var(--text); letter-spacing: -0.5px; }
    .sh-sub { font-size: 13px; color: var(--text-muted); margin-top: 2px; }

    /* Buttons */
    .btn {
      height: 38px; padding: 0 16px; border: none; border-radius: var(--radius-md); cursor: pointer;
      font-size: 13.5px; font-weight: 600; font-family: 'Inter', sans-serif;
      transition: all 0.2s ease; display: inline-flex; align-items: center; gap: 6px;
    }
    .btn-primary { background: var(--primary-dark); color: #FFFFFF; box-shadow: var(--shadow-sm); }
    .btn-primary:hover { background: var(--primary-hover); transform: translateY(-1px); }
    .btn-danger { background: var(--surface); color: var(--red); border: 1px solid var(--border); }
    .btn-danger:hover { background: var(--red-bg); border-color: var(--red-bd); }
    .btn-success { background: var(--surface); color: var(--green); border: 1px solid var(--border); }
    .btn-success:hover { background: var(--green-bg); border-color: var(--green-bd); }
    .btn-sm { height: 32px; padding: 0 12px; font-size: 12px; border-radius: 6px; }

    /* Modern Table UI */
    .table-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-sm); }
    .table-wrap { overflow-x: auto; }
    table { width: 100%; border-collapse: collapse; min-width: 800px; }
    thead { background: #FAFAFA; border-bottom: 1px solid var(--border); }
    th { padding: 14px 24px; text-align: left; font-size: 11px; color: var(--text-muted); font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }
    tbody tr { transition: background 0.15s ease; border-bottom: 1px solid var(--border); }
    tbody tr:hover { background: #FAFAFA; }
    td { padding: 16px 24px; font-size: 13.5px; color: var(--text); }
    tbody tr:last-child { border-bottom: none; }
    .td-main { font-weight: 600; color: var(--primary-dark); }
    .device {
      font-size: 11.5px; background: var(--bg); color: var(--text);
      padding: 4px 8px; border-radius: 6px; font-weight: 600; font-family: monospace; border: 1px solid var(--border);
    }
    .badge { padding: 4px 10px; border-radius: 12px; font-size: 11.5px; font-weight: 600; display: inline-flex; align-items: center; gap: 5px; }
    .badge::before { content: '●'; font-size: 8px; }
    .badge-on { background: var(--green-bg); color: var(--green); }
    .badge-off { background: var(--red-bg); color: var(--red); }

    /* Empty state */
    .empty { padding: 50px 20px; text-align: center; }
    .empty-ico { font-size: 40px; margin-bottom: 12px; color: var(--text-light); }
    .empty-txt { font-size: 15px; font-weight: 600; color: var(--text-muted); }
    .empty-sub { font-size: 12.5px; color: var(--text-light); margin-top: 4px; }

    /* Filters / Forms */
    .h-filters { display: flex; gap: 12px; margin-bottom: 24px; align-items: center; flex-wrap: wrap; }
    .h-select {
      height: 38px; padding: 0 12px; background: var(--surface); border: 1px solid var(--border);
      border-radius: var(--radius-md); font-size: 13.5px; font-family: 'Inter', sans-serif; color: var(--text);
      outline: none; transition: border-color 0.2s;
    }
    .h-select:focus { border-color: var(--primary-light); }

    .param-card { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 24px; margin-bottom: 24px; box-shadow: var(--shadow-sm); }
    .param-title { font-size: 15px; font-weight: 700; color: var(--text); margin-bottom: 4px; }
    .param-sub { font-size: 12.5px; color: var(--text-muted); margin-bottom: 16px; }
    .param-row { display: flex; justify-content: space-between; align-items: center; padding: 14px 0; border-bottom: 1px solid var(--border); flex-wrap: wrap; gap: 12px; }
    .param-row:last-child { border-bottom: none; padding-bottom: 0; }
    .p-lbl { font-size: 13.5px; font-weight: 600; color: var(--text); }
    .p-desc { font-size: 12px; color: var(--text-muted); margin-top: 2px; }
    .p-badge { font-size: 11.5px; font-weight: 600; padding: 4px 10px; border-radius: 12px; background: var(--bg); color: var(--text-muted); border: 1px solid var(--border); }

    /* Modals & Dialogs */
    .mbg {
      display: none; position: fixed; inset: 0; background: rgba(15, 23, 42, 0.4);
      backdrop-filter: blur(8px); z-index: 200; align-items: center; justify-content: center; padding: 16px;
    }
    .mbg.open { display: flex; animation: fadeIn 0.2s ease; }
    .modal {
      background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
      padding: 32px; width: 100%; max-width: 500px; max-height: 90vh; overflow-y: auto;
      box-shadow: var(--shadow-lg); animation: slideUp 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes slideUp { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
    .mh { display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px; }
    .mh h3 { font-size: 18px; font-weight: 700; color: var(--text); }
    .mc {
      width: 28px; height: 28px; border-radius: 6px; border: 1px solid var(--border);
      background: var(--surface); cursor: pointer; font-size: 14px; color: var(--text-muted);
      display: flex; align-items: center; justify-content: center;
    }
    .fg { margin-bottom: 16px; }
    .fg label { display: block; font-size: 12.5px; font-weight: 600; color: var(--text); margin-bottom: 6px; }
    .fg input, .fg select {
      width: 100%; height: 40px; padding: 0 12px; background: var(--bg); border: 1px solid var(--border);
      border-radius: var(--radius-md); font-size: 13.5px; font-family: 'Inter', sans-serif; color: var(--text); outline: none;
    }
    .fg input:focus, .fg select:focus { border-color: var(--primary-light); background: #FFF; }
    .fg2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
    .ma { display: flex; gap: 10px; margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--border); }
    .ma .btn { flex: 1; justify-content: center; }
    .al { padding: 10px 14px; border-radius: 8px; font-size: 12.5px; font-weight: 500; margin-bottom: 16px; display: none; align-items: center; gap: 8px; }
    .al-e { background: var(--red-bg); border: 1px solid var(--red-bd); color: var(--red); }
    .al-o { background: var(--green-bg); border: 1px solid var(--green-bd); color: var(--green); }

    .overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.3); z-index: 99; backdrop-filter: blur(2px); }
    .overlay.open { display: block; }

    /* RESPONSIVE */
    @media (max-width: 768px) {
      .sidebar { left: calc(-1 * var(--sidebar-w)); }
      .sidebar.open { left: 0; }
      .main { margin-left: 0 !important; }
      .menu-btn { display: inline-flex; }
      .topbar { padding: 0 16px; }
      .content { padding: 16px; }
      .stats { grid-template-columns: 1fr !important; gap: 16px; }
      .fg2 { grid-template-columns: 1fr !important; }
    }
  </style>
</head>
<body>

<div class="overlay" id="overlay" onclick="closeMenu()"></div>

<!-- Sidebar -->
<div class="sidebar" id="sidebar">
  <div class="s-logo">
    <div class="s-logo-row">
      <div class="s-logo-icon"><i class="fa-solid fa-earth-americas"></i></div>
      <div>
        <div class="s-logo-name">FleetTracker</div>
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
    <div class="nav-item" onclick="show('parametres',this)">
      <i class="fa-solid fa-sliders nav-ico"></i> Paramètres
    </div>
  </div>
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()"><i class="fa-solid fa-arrow-right-from-bracket"></i> Déconnexion</button>
  </div>
</div>

<!-- Main Section -->
<div class="main">
  <div class="topbar">
    <div class="tb-left">
      <button class="menu-btn" onclick="toggleMenu()"><i class="fa-solid fa-bars"></i></button>
      <div style="display: flex; flex-direction: column;">
        <span class="tb-crumb">Espace Admin</span>
        <span class="tb-page-title" id="page-title">Tableau de bord</span>
      </div>
    </div>
    <div class="tb-right">
      <div class="clock"><i class="fa-regular fa-clock"></i> <span id="clk">--:--:--</span></div>
    </div>
  </div>

  <div class="content">

    <!-- Dashboard -->
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
          <div class="stat-lbl">Infrastructure IoT Cloud</div>
        </div>
      </div>
      
      <div class="table-card" style="padding: 48px; text-align: center;">
        <i class="fa-solid fa-circle-check" style="font-size: 44px; color: var(--primary); margin-bottom: 16px;"></i>
        <h3 style="font-size: 18px; color: var(--text); margin-bottom: 8px;">Centre de Contrôle Opérationnel</h3>
        <p style="font-size: 14px; color: var(--text-muted); line-height: 1.5; max-width: 500px; margin: 0 auto;">
          Bienvenue dans votre gestionnaire de flotte global. Utilisez le panneau d'accès pour administrer vos comptes clients, l'inventaire des traceurs GPS et le diagnostic du réseau Sénégalais.
        </p>
      </div>
    </div>

    <!-- Propriétaires -->
    <div class="section" id="s-proprietaires">
      <div class="stats" id="prop-pos" style="margin-bottom: 24px;">
        <div class="stat" style="padding: 20px;">
          <div style="font-size: 20px; color: var(--primary-dark); margin-bottom: 8px;"><i class="fa-solid fa-users"></i></div>
          <div class="stat-val" id="pp-total" style="font-size: 24px;">—</div>
          <div class="stat-lbl" style="margin-top: 2px;">Total propriétaires</div>
        </div>
        <div class="stat" style="padding: 20px;">
          <div style="font-size: 20px; color: var(--green); margin-bottom: 8px;"><i class="fa-solid fa-user-check"></i></div>
          <div class="stat-val" id="pp-actif" style="font-size: 24px;">—</div>
          <div class="stat-lbl" style="margin-top: 2px;">Comptes actifs</div>
        </div>
        <div class="stat" style="padding: 20px;">
          <div style="font-size: 20px; color: var(--primary-light); margin-bottom: 8px;"><i class="fa-solid fa-car"></i></div>
          <div class="stat-val" id="pp-vehs" style="font-size: 24px;">—</div>
          <div class="stat-lbl" style="margin-top: 2px;">Véhicules associés</div>
        </div>
      </div>
      
      <div class="sh">
        <div>
          <h2>Propriétaires</h2>
          <div class="sh-sub">Comptes d'accès client et facturation</div>
        </div>
        <button class="btn btn-primary" onclick="openMP()"><i class="fa-solid fa-plus"></i> Nouveau client</button>
      </div>
      
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Nom complet</th><th>Email</th><th>Téléphone</th>
                <th>Véhicules</th><th>Depuis</th><th>Statut</th><th>Actions</th>
              </tr>
            </thead>
            <tbody id="tbp">
              <tr>
                <td colspan="7">
                  <div class="empty"><i class="fa-solid fa-circle-notch fa-spin empty-ico"></i><div class="empty-txt">Chargement...</div></div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Véhicules -->
    <div class="section" id="s-vehicules">
      <div class="sh">
        <div>
          <h2>Flotte de Véhicules</h2>
          <div class="sh-sub">Gérez l'assignation des traceurs ESP32</div>
        </div>
        <button class="btn btn-primary" onclick="openMV()"><i class="fa-solid fa-plus"></i> Assigner un véhicule</button>
      </div>
      
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Immatriculation</th><th>Modèle</th><th>Type</th>
                <th>Propriétaire</th><th>Device ID</th><th>Statut</th><th>Actions</th>
              </tr>
            </thead>
            <tbody id="tbv">
              <tr>
                <td colspan="7">
                  <div class="empty"><i class="fa-solid fa-circle-notch fa-spin empty-ico"></i><div class="empty-txt">Chargement...</div></div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Historique -->
    <div class="section" id="s-historique">
      <div class="sh">
        <div>
          <h2>Historique de Tracking</h2>
          <div class="sh-sub">Données télémétriques de positionnement</div>
        </div>
      </div>
      
      <div class="h-filters">
        <select class="h-select" id="hv" onchange="loadHist()" style="min-width: 260px;">
          <option value="">Sélectionnez un véhicule...</option>
        </select>
        <select class="h-select" id="hl" onchange="loadHist()">
          <option value="50">50 derniers points</option>
          <option value="100">100 derniers points</option>
          <option value="200">200 derniers points</option>
        </select>
      </div>
      
      <div class="stats" id="hstats" style="display: none; grid-template-columns: repeat(4,1fr); gap: 16px; margin-bottom: 24px;">
        <div class="stat" style="padding: 16px;"><div class="stat-val" id="hs1" style="font-size: 22px;">0</div><div class="stat-lbl" style="font-size: 11.5px; margin-top: 2px;">Points</div></div>
        <div class="stat" style="padding: 16px;"><div class="stat-val" id="hs2" style="font-size: 22px;">0</div><div class="stat-lbl" style="font-size: 11.5px; margin-top: 2px;">Vmax (km/h)</div></div>
        <div class="stat" style="padding: 16px;"><div class="stat-val" id="hs3" style="font-size: 22px;">0</div><div class="stat-lbl" style="font-size: 11.5px; margin-top: 2px;">Vmoy (km/h)</div></div>
        <div class="stat" style="padding: 16px;"><div class="stat-val" id="hs4" style="font-size: 22px;">0</div><div class="stat-lbl" style="font-size: 11.5px; margin-top: 2px;">Sats moy.</div></div>
      </div>
      
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th>#</th><th>Horodatage</th><th>Latitude</th><th>Longitude</th><th>Vitesse</th><th>Signal</th>
              </tr>
            </thead>
            <tbody id="tbh">
              <tr>
                <td colspan="6">
                  <div class="empty">
                    <i class="fa-solid fa-map-location-dot empty-ico"></i>
                    <div class="empty-txt">Sélectionnez un véhicule</div>
                    <div class="empty-sub">pour afficher l'historique des positions</div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Paramètres -->
    <div class="section" id="s-parametres">
      <div class="sh">
        <div>
          <h2>Paramètres Système</h2>
          <div class="sh-sub">Infrastructure Cloud de géolocalisation</div>
        </div>
      </div>
      
      <div class="param-card">
        <div class="param-title">Compte Administrateur Principal</div>
        <div class="param-sub">Identité système racine</div>
        <div class="param-row">
          <div><div class="p-lbl">Email d'administration</div><div class="p-desc">admin@gps.com</div></div>
          <span class="p-badge" style="background: var(--grad-light); color: var(--primary-dark);"><i class="fa-solid fa-shield-halved"></i> Accès total</span>
        </div>
      </div>
      
      <div class="param-card">
        <div class="param-title">IoT Network & Stockage</div>
        <div class="param-sub">Diagnostic de la connexion des microcontrôleurs</div>
        <div class="param-row">
          <div><div class="p-lbl">Réception Télémétrie (ESP32)</div><div class="p-desc">POST /api/position</div></div>
          <span class="p-badge" style="background: var(--green-bg); color: var(--green);"><i class="fa-solid fa-circle-check"></i> Actif (200 OK)</span>
        </div>
        <div class="param-row">
          <div><div class="p-lbl">Base de données</div><div class="p-desc">PostgreSQL Cloud DB Engine</div></div>
          <span class="p-badge" style="background: var(--green-bg); color: var(--green);"><i class="fa-solid fa-database"></i> Connecté</span>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- Modal: Ajouter Client -->
<div class="mbg" id="mp">
  <div class="modal">
    <div class="mh">
      <h3>Ajouter un nouveau client</h3>
      <button class="mc" onclick="closeM('mp')"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <div class="al al-e" id="ep"><i class="fa-solid fa-circle-exclamation"></i> <span id="ep-t"></span></div>
    <div class="al al-o" id="op"><i class="fa-solid fa-circle-check"></i> <span id="op-t"></span></div>
    <div class="fg2">
      <div class="fg"><label>Nom *</label><input id="pn" placeholder="Nom"/></div>
      <div class="fg"><label>Prénom *</label><input id="pp" placeholder="Prénom"/></div>
    </div>
    <div class="fg"><label>Email *</label><input type="email" id="pe" placeholder="client@entreprise.com"/></div>
    <div class="fg"><label>Téléphone *</label><input id="p-tel" placeholder="+221 77 ..."/></div>
    <div class="fg"><label>Mot de passe *</label><input type="password" id="pw" placeholder="Minimum 6 caractères"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('mp')">Annuler</button>
      <button class="btn btn-primary" onclick="creerP()"><i class="fa-solid fa-check"></i> Créer le compte</button>
    </div>
  </div>
</div>

<!-- Modal: Assigner Véhicule -->
<div class="mbg" id="mv">
  <div class="modal">
    <div class="mh">
      <h3>Assigner un traceur</h3>
      <button class="mc" onclick="closeM('mv')"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <div class="al al-e" id="ev"><i class="fa-solid fa-circle-exclamation"></i> <span id="ev-t"></span></div>
    <div class="al al-o" id="ov"><i class="fa-solid fa-circle-check"></i> <span id="ov-t"></span></div>
    <div class="fg"><label>Propriétaire du véhicule *</label><select id="vp"></select></div>
    <div class="fg2">
      <div class="fg"><label>Marque *</label><input id="vm" placeholder="Toyota"/></div>
      <div class="fg"><label>Modèle *</label><input id="vmo" placeholder="Hilux"/></div>
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
      <div class="fg"><label>Couleur</label><input id="vc" placeholder="Blanc"/></div>
    </div>
    <div class="fg2">
      <div class="fg"><label>Immatriculation *</label><input id="vi" placeholder="DK-1234-A"/></div>
      <div class="fg"><label>Année</label><input type="number" id="va" placeholder="2025"/></div>
    </div>
    <div class="fg"><label>Device ID (Adresse MAC ESP32) *</label><input id="vd" placeholder="Ex: esp32_fleet_01"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('mv')">Annuler</button>
      <button class="btn btn-primary" onclick="creerV()"><i class="fa-solid fa-check"></i> Enregistrer l'assignation</button>
    </div>
  </div>
</div>

<!-- Modal: Modification Client -->
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
    <div class="fg"><label>Nouveau mot de passe <span style="font-weight: 400; color: var(--text-light)">(laisser vide si inchangé)</span></label>
      <input type="password" id="mp-pw"/></div>
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('m-modif-p')">Annuler</button>
      <button class="btn btn-primary" onclick="sauvegarderP()"><i class="fa-solid fa-floppy-disk"></i> Enregistrer</button>
    </div>
  </div>
</div>

<!-- Modal: Modification Véhicule -->
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
    <div class="ma">
      <button class="btn btn-danger" onclick="closeM('m-modif-v')">Annuler</button>
      <button class="btn btn-primary" onclick="sauvegarderV()"><i class="fa-solid fa-floppy-disk"></i> Enregistrer</button>
    </div>
  </div>
</div>

<!-- Modal: Supprimer (Irreversible) -->
<div class="mbg" id="m-suppr">
  <div class="modal" style="max-width: 420px; text-align: center;">
    <div style="font-size: 40px; color: var(--red); margin-bottom: 16px;"><i class="fa-solid fa-triangle-exclamation"></i></div>
    <h3 style="color: var(--text); font-size: 18px; font-weight: 700; margin-bottom: 8px;">Action irréversible</h3>
    <p id="suppr-msg" style="font-size: 13.5px; color: var(--text-muted); line-height: 1.5; margin-bottom: 24px;"></p>
    <div class="ma" style="border-top: none; padding-top: 0;">
      <button class="btn btn-success" onclick="closeM('m-suppr')">Annuler</button>
      <button class="btn btn-danger" onclick="executerSuppression()" style="background: var(--red); color: #FFF;"><i class="fa-solid fa-trash"></i> Confirmer</button>
    </div>
  </div>
</div>

<script>
const T={dashboard:"Tableau de bord",proprietaires:"Propriétaires",vehicules:"Flotte de Véhicules",
  historique:"Historique de Tracking",parametres:"Paramètres Système"};

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
  try {
    const[p,v]=await Promise.all([
      fetch("/api/admin/proprietaires").then(r=>r.json()),
      fetch("/api/admin/vehicules").then(r=>r.json())]);
    document.getElementById("stp").textContent=p.length||0;
    document.getElementById("stv").textContent=v.filter(x=>x.actif).length||0;
  } catch(e) {}
}

/* ── Propriétaires ── */
async function loadP(){
  try {
    const data=await fetch("/api/admin/proprietaires").then(r=>r.json());
    const actifs=data.filter(p=>p.actif).length;
    const totalVehs=data.reduce((s,p)=>s+p.nb_vehicules,0);
    document.getElementById("pp-total").textContent=data.length;
    document.getElementById("pp-actif").textContent=actifs;
    document.getElementById("pp-vehs").textContent=totalVehs;
    const tb=document.getElementById("tbp");
    if(!data.length){
      tb.innerHTML='<tr><td colspan="7"><div class="empty"><i class="fa-solid fa-users empty-ico"></i><div class="empty-txt">Aucun client trouvé</div></div></td></tr>';
      return;
    }
    tb.innerHTML=data.map(p=>`<tr>
      <td class="td-main">${p.prenom} ${p.nom}</td>
      <td><i class="fa-regular fa-envelope" style="color:var(--text-light);margin-right:6px"></i>${p.email}</td>
      <td>${p.telephone||"—"}</td>
      <td><span style="font-weight:600; padding:4px 8px; border-radius:12px; background:var(--bg); border:1px solid var(--border);">${p.nb_vehicules} &nbsp;<i class="fa-solid fa-car" style="color:var(--primary-dark); font-size:11px;"></i></span></td>
      <td style="font-size:12px;color:var(--text-muted)">${(p.date_creation||"").slice(0,10)}</td>
      <td><span class="badge ${p.actif?'badge-on':'badge-off'}">${p.actif?'Actif':'Inactif'}</span></td>
      <td><div style="display:flex;gap:6px;">
        <button class="btn btn-sm ${p.actif?'btn-danger':'btn-success'}" onclick="toggleP(${p.id})"><i class="fa-solid fa-power-off"></i></button>
        <button class="btn btn-sm btn-primary" style="background:var(--bg); color:var(--primary-dark); border:1px solid var(--border); box-shadow:none;" onclick="ouvrirModifP(${p.id})"><i class="fa-solid fa-pen"></i></button>
        <button class="btn btn-sm btn-danger" onclick="confirmerSuppressionP(${p.id},'${p.prenom} ${p.nom}')"><i class="fa-solid fa-trash"></i></button>
      </div></td>
    </tr>`).join("");
  } catch(e) {}
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
    et.textContent="Veuillez remplir tous les champs obligatoires.";e.style.display="flex";return;}
  try {
    const res=await fetch("/api/admin/proprietaires",{method:"POST",
      headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
    const data=await res.json();
    if(res.ok){
      ot.textContent="Client créé avec succès.";o.style.display="flex";
      ["pn","pp","pe","p-tel","pw"].forEach(id=>document.getElementById(id).value="");
      loadStats();
    }else{et.textContent=data.error;e.style.display="flex";}
  } catch(err) { et.textContent="Erreur d'envoi.";e.style.display="flex"; }
}

async function toggleP(id){await fetch(`/api/admin/proprietaires/${id}/toggle`,{method:"POST"});loadP();loadStats();}

/* ── Véhicules ── */
async function loadV(){
  try {
    const data=await fetch("/api/admin/vehicules").then(r=>r.json());
    const tb=document.getElementById("tbv");
    if(!data.length){tb.innerHTML='<tr><td colspan="7"><div class="empty"><i class="fa-solid fa-car empty-ico"></i><div class="empty-txt">Flotte vide</div></div></td></tr>';return;}
    tb.innerHTML=data.map(v=>`<tr>
      <td class="td-main">${v.immatriculation}</td>
      <td>${v.marque} <span style="color:var(--text-muted);font-weight:400">${v.modele}</span></td>
      <td style="text-transform:capitalize"><i class="fa-solid fa-car" style="color:var(--text-light);margin-right:6px"></i>${v.type_vehicule}</td>
      <td><i class="fa-regular fa-user" style="color:var(--text-light);margin-right:6px"></i>${v.proprietaire_nom}</td>
      <td><span class="device"><i class="fa-solid fa-microchip" style="margin-right:4px;"></i>${v.device_id}</span></td>
      <td><span class="badge ${v.actif?'badge-on':'badge-off'}">${v.actif?'Actif':'Inactif'}</span></td>
      <td><div style="display:flex;gap:6px;">
        <button class="btn btn-sm ${v.actif?'btn-danger':'btn-success'}" onclick="toggleV(${v.id})"><i class="fa-solid fa-power-off"></i></button>
        <button class="btn btn-sm btn-primary" style="background:var(--bg); color:var(--primary-dark); border:1px solid var(--border); box-shadow:none;" onclick="ouvrirModifV(${v.id})"><i class="fa-solid fa-pen"></i></button>
        <button class="btn btn-sm btn-danger" onclick="confirmerSuppressionV(${v.id},'${v.immatriculation}')"><i class="fa-solid fa-trash"></i></button>
      </div></td>
    </tr>`).join("");
  } catch(e) {}
}

async function openMV(){
  try {
    const data=await fetch("/api/admin/proprietaires").then(r=>r.json());
    document.getElementById("vp").innerHTML=data.map(p=>`<option value="${p.id}">${p.prenom} ${p.nom}</option>`).join("");
    document.getElementById("ev").style.display=document.getElementById("ov").style.display="none";
    document.getElementById("mv").classList.add("open");
  } catch(e) {}
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
    annee:parseInt(document.getElementById("va").value)||2025,
    device_id:document.getElementById("vd").value.trim()
  };
  try {
    const res=await fetch("/api/admin/vehicules",{method:"POST",
      headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
    const data=await res.json();
    if(res.ok){ot.textContent="Traceur assigné au véhicule avec succès.";o.style.display="flex";loadStats();}
    else{et.textContent=data.error;e.style.display="flex";}
  } catch(err) { et.textContent="Erreur d'envoi.";e.style.display="flex"; }
}

async function toggleV(id){await fetch(`/api/admin/vehicules/${id}/toggle`,{method:"POST"});loadV();loadStats();}

/* ── Historique ── */
async function initHist(){
  try {
    const vehs=await fetch("/api/admin/vehicules").then(r=>r.json());
    const sel=document.getElementById("hv");
    const cur=sel.value;
    sel.innerHTML='<option value="">Sélectionner un véhicule...</option>'+
      vehs.filter(v=>v.actif).map(v=>`<option value="${v.id}">${v.immatriculation} — ${v.marque} ${v.modele}</option>`).join("");
    if(cur)sel.value=cur;
  } catch(e) {}
}

async function loadHist(){
  const vid=document.getElementById("hv").value;
  const lim=document.getElementById("hl").value;
  if(!vid)return;
  try {
    const data=await fetch(`/api/positions/${vid}?limit=${lim}`).then(r=>r.json());
    const hs=document.getElementById("hstats");
    const tb=document.getElementById("tbh");
    if(!data.length){
      hs.style.display="none";
      tb.innerHTML='<tr><td colspan="6"><div class="empty"><i class="fa-solid fa-route empty-ico"></i><div class="empty-txt">Aucune coordonnée GPS enregistrée</div></div></td></tr>';
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
      <td style="color:var(--text-light);font-size:12px;font-weight:600">#${data.length-i}</td>
      <td style="font-size:13px;color:var(--text-muted)"><i class="fa-regular fa-clock" style="margin-right:6px"></i>${p.created_at||p.timestamp||"—"}</td>
      <td style="font-family:monospace;font-size:13px;font-weight:600;color:var(--primary-dark)">${(p.latitude||0).toFixed(6)}</td>
      <td style="font-family:monospace;font-size:13px;font-weight:600;color:var(--primary-dark)">${(p.longitude||0).toFixed(6)}</td>
      <td><span style="font-weight:600; padding:4px 8px; border-radius:6px; background:${(p.vitesse||0)>80?'var(--red-bg)':'var(--bg)'}; color:${(p.vitesse||0)>80?'var(--red)':'var(--text)'}">${(p.vitesse||0).toFixed(1)} km/h</span></td>
      <td><i class="fa-solid fa-satellite" style="color:var(--text-light);margin-right:6px"></i>${p.satellites||"—"}</td>
    </tr>`).join("");
  } catch(e) {}
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
    `Supprimer définitivement le véhicule <strong style="color:var(--text)">${label}</strong> et ses coordonnées ?`;
  document.getElementById("m-suppr").classList.add("open");
}

function confirmerSuppressionP(id, label){
  _supprId=id; _supprType='proprietaire';
  document.getElementById("suppr-msg").innerHTML=
    `Supprimer le compte client de <strong style="color:var(--text)">${label}</strong>, incluant ses véhicules et historiques ?`;
  document.getElementById("m-suppr").classList.add("open");
}

async function executerSuppression(){
  if(!_supprId||!_supprType)return;
  const url = _supprType==='vehicule'
    ? `/api/admin/vehicules/${_supprId}`
    : `/api/admin/proprietaires/${_supprId}`;
  try {
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
  } catch(e) {}
  _supprId=null; _supprType=null;
}

/* ── Modification ── */
async function ouvrirModifP(id){
  try {
    const data=await fetch(`/api/admin/proprietaires/${id}`).then(r=>r.json());
    document.getElementById("mp-id").value=id;
    document.getElementById("mp-nom").value=data.nom||"";
    document.getElementById("mp-prenom").value=data.prenom||"";
    document.getElementById("mp-email").value=data.email||"";
    document.getElementById("mp-tel").value=data.telephone||"";
    document.getElementById("mp-pw").value="";
    document.getElementById("emp").style.display=document.getElementById("omp").style.display="none";
    document.getElementById("m-modif-p").classList.add("open");
  } catch(e) {}
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
  try {
    const res=await fetch(`/api/admin/proprietaires/${id}`,{method:"PUT",
      headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
    const data=await res.json();
    if(res.ok){ot.textContent="Enregistré !";o.style.display="flex";
      setTimeout(()=>closeM("m-modif-p"),1000);loadP();}
    else{et.textContent=data.error;e.style.display="flex";}
  } catch(err) {}
}

async function ouvrirModifV(id){
  try {
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
  } catch(e) {}
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
    device_id:document.getElementById("mv-device").value.trim()
  };
  try {
    const res=await fetch(`/api/admin/vehicules/${id}`,{method:"PUT",
      headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
    const data=await res.json();
    if(res.ok){ot.textContent="Enregistré !";o.style.display="flex";
      setTimeout(()=>closeM("m-modif-v"),1000);loadV();}
    else{et.textContent=data.error;e.style.display="flex";}
  } catch(err) {}
}

async function doLogout(){await fetch("/api/logout",{method:"POST"});window.location.href="/";}
loadStats();
</script>
</body>
</html>"""

# ═════════════════════════════════════════════════════════════
#  PAGE USER (Samsara / Geotab Premium Map Centric UI)
# ═════════════════════════════════════════════════════════════

USER_PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>GPS Tracker — Mon Suivi de Flotte</title>
  <meta name="theme-color" content="#0B3D91">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="GPS Tracker">
  <link rel="manifest" href="/manifest.json">
  <link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
  <style>
    :root {
      --bg: #F8FAFC;
      --surface: #FFFFFF;
      --surface2: #F1F5F9;
      --border: #E2E8F0;
      --primary: #4FC3F7;
      --primary-dark: #0B3D91;
      --grad: linear-gradient(135deg, #0B3D91, #4FC3F7);
      --green: #10B981;
      --green-bg: #ECFDF5;
      --red: #EF4444;
      --red-bg: #FEF2F2;
      --amber: #F59E0B;
      --amber-bg: #FFFBEB;
      --text: #0F172A;
      --text-muted: #475569;
      --text-light: #94A3B8;
      --sidebar-w: 280px;
      --radius-lg: 16px;
      --radius-md: 10px;
      --shadow-sm: 0 1px 3px rgba(15, 23, 42, 0.05);
      --shadow-md: 0 4px 12px -2px rgba(15, 23, 42, 0.05), 0 2px 4px -1px rgba(15, 23, 42, 0.03);
      --shadow-lg: 0 20px 25px -5px rgba(15, 23, 42, 0.1);
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Inter', sans-serif;
      background: var(--bg);
      color: var(--text);
      height: 100vh;
      display: flex;
      overflow: hidden;
      font-size: 14px;
    }

    /* SIDEBAR */
    .sidebar {
      position: fixed; top: 0; left: 0; bottom: 0; width: var(--sidebar-w);
      background: var(--surface); border-right: 1px solid var(--border);
      display: flex; flex-direction: column; z-index: 2000;
      transition: left 0.3s ease; box-shadow: var(--shadow-md);
    }
    .s-logo { padding: 24px 20px; border-bottom: 1px solid var(--border); }
    .s-logo-row { display: flex; align-items: center; gap: 12px; }
    .s-logo-icon {
      width: 38px; height: 38px; border-radius: 10px; background: var(--grad); color: #FFF;
      display: flex; align-items: center; justify-content: center; font-size: 18px; flex-shrink: 0;
    }
    .s-logo-name { font-size: 16px; font-weight: 700; color: var(--primary-dark); letter-spacing: -0.5px; }
    .s-logo-sub { font-size: 11px; color: var(--primary); font-weight: 700; text-transform: uppercase; }

    .s-user { margin: 16px; padding: 14px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius-md); }
    .s-user-name { font-size: 13.5px; font-weight: 600; color: var(--text); }
    .s-user-role { font-size: 11px; font-weight: 700; color: var(--primary-dark); text-transform: uppercase; margin-top: 2px; }

    .s-section { padding: 16px 20px 8px; font-size: 11px; font-weight: 700; color: var(--text-light); text-transform: uppercase; letter-spacing: 1px; }
    .nav-item {
      display: flex; align-items: center; gap: 12px; padding: 10px 16px;
      margin: 2px 12px; border-radius: var(--radius-md); cursor: pointer; color: var(--text-muted);
      font-size: 13.5px; font-weight: 500; transition: all 0.2s;
    }
    .nav-item:hover { background: var(--bg); color: var(--text); }
    .nav-item.active { background: var(--primary-dark); color: #FFF; font-weight: 600; box-shadow: var(--shadow-sm); }
    .nav-ico { font-size: 15px; width: 20px; text-align: center; flex-shrink: 0; }

    /* VEHICLE CARD SYNC LIST[cite: 1] */
    .veh-list { flex: 1; overflow-y: auto; padding: 8px 12px; }
    .veh-card {
      padding: 14px; border-radius: var(--radius-md); cursor: pointer;
      border: 1px solid var(--border); background: var(--surface); margin-bottom: 8px;
      transition: all 0.2s ease;
    }
    .veh-card:hover { border-color: var(--primary-light); transform: translateY(-1px); box-shadow: var(--shadow-sm); }
    .veh-card.sel { background: var(--bg); border-color: var(--primary-dark); border-width: 2.5px; }
    .veh-immat { font-size: 13.5px; font-weight: 700; color: var(--primary-dark); letter-spacing: -0.3px; }
    .veh-info { font-size: 12.5px; color: var(--text-muted); margin-top: 4px; }
    .veh-live { display: flex; align-items: center; gap: 6px; margin-top: 8px; }
    .dot { width: 8px; height: 8px; border-radius: 50%; background: var(--text-light); flex-shrink: 0; }
    @keyframes blink { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.5; transform: scale(0.9); } }
    .dot.live { background: var(--green); animation: blink 1.5s infinite; box-shadow: 0 0 6px var(--green); }
    .dot-lbl { font-size: 11px; color: var(--text-muted); font-weight: 600; text-transform: uppercase; }

    .s-bottom { padding: 16px; border-top: 1px solid var(--border); }
    .btn-logout {
      width: 100%; padding: 10px; background: var(--surface); color: var(--text-muted);
      border: 1px solid var(--border); border-radius: var(--radius-md); cursor: pointer;
      font-size: 13px; font-weight: 600; font-family: 'Inter', sans-serif;
      display: flex; align-items: center; justify-content: center; gap: 8px;
    }
    .btn-logout:hover { background: var(--red-bg); color: var(--red); border-color: rgba(239, 68, 68, 0.2); }

    /* MAIN PANEL */
    .main { margin-left: var(--sidebar-w); flex: 1; display: flex; flex-direction: column; overflow: hidden; min-width: 0; }
    .topbar {
      height: 64px; padding: 0 24px; background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(12px); border-bottom: 1px solid var(--border);
      display: flex; align-items: center; justify-content: space-between; flex-shrink: 0; z-index: 10;
    }
    .menu-btn { display: none; background: none; border: none; cursor: pointer; font-size: 18px; color: var(--text); padding: 6px; border-radius: 6px; }
    .tb-title { font-size: 16px; font-weight: 700; color: var(--primary-dark); }
    .live-pill {
      display: flex; align-items: center; gap: 6px; padding: 4px 10px;
      background: var(--green-bg); border: 1px solid rgba(16,185,129,0.2);
      border-radius: 12px; font-size: 11.5px; color: var(--green); font-weight: 600;
    }
    .live-blink { width: 6px; height: 6px; border-radius: 50%; background: var(--green); animation: blink 1.5s infinite; }
    .upd { font-size: 12px; color: var(--text-light); margin-left: 12px; font-weight: 500; }

    /* Floating Panel on Central Map[cite: 1] */
    .infobar {
      position: absolute; top: 20px; left: 50%; transform: translateX(-50%); z-index: 1000;
      background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(12px); border: 1px solid var(--border);
      border-radius: var(--radius-lg); padding: 12px 24px; display: flex; align-items: center; gap: 20px;
      box-shadow: var(--shadow-lg); transition: all 0.3s ease;
    }
    .isep { width: 1px; height: 28px; background: var(--border); }
    .iitem { display: flex; flex-direction: column; align-items: center; }
    .ilbl { font-size: 9px; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; }
    .ival { font-size: 15px; font-weight: 700; color: var(--text); margin-top: 2px; }
    .ival.grad { color: var(--primary-dark); }

    #map { flex: 1; width: 100%; height: 100%; z-index: 1; }
    
    /* Empty View / Error states */
    .empty-state { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; background: var(--bg); }
    .es-ico { font-size: 50px; color: var(--text-light); }
    .es-title { font-size: 18px; font-weight: 700; color: var(--primary-dark); }
    .es-sub { font-size: 13.5px; color: var(--text-muted); text-align: center; padding: 0 24px; max-width: 380px; line-height: 1.5; }

    .usec { display: none; flex: 1; overflow-y: auto; padding: 32px; background: var(--bg); }
    .usec.active { display: block; animation: fadeInUp 0.35s cubic-bezier(0.16, 1, 0.3, 1); }

    /* Stats Grid */
    .stat-cards-container { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-bottom: 32px; }
    .card-modern {
      background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
      padding: 20px; position: relative; overflow: hidden; box-shadow: var(--shadow-sm); transition: transform 0.2s;
    }
    .card-modern:hover { transform: translateY(-1px); box-shadow: var(--shadow-md); }

    .h-filters { display: flex; gap: 12px; margin-bottom: 24px; flex-wrap: wrap; }
    .h-select {
      height: 38px; padding: 0 12px; background: var(--surface); border: 1px solid var(--border);
      border-radius: var(--radius-md); font-size: 13.5px; font-family: 'Inter', sans-serif; color: var(--text); outline: none;
    }
    
    /* Tables */
    .htable { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg); overflow: hidden; box-shadow: var(--shadow-sm); }
    .htable-wrap { overflow-x: auto; }
    .htable table { width: 100%; border-collapse: collapse; min-width: 600px; }
    .htable th { padding: 14px 20px; font-size: 11px; font-weight: 600; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; background: #FAFAFA; border-bottom: 1px solid var(--border); }
    .htable td { padding: 14px 20px; font-size: 13.5px; color: var(--text); border-bottom: 1px solid var(--border); }
    .htable tr:hover td { background: #FAFAFA; }

    /* Params */
    .pcard { background: var(--surface); border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 24px; margin-bottom: 20px; box-shadow: var(--shadow-sm); }
    .ptitle { font-size: 16px; font-weight: 700; color: var(--text); margin-bottom: 4px; }
    .psub { font-size: 12.5px; color: var(--text-muted); margin-bottom: 20px; }
    .prow { display: flex; justify-content: space-between; align-items: center; padding: 14px 0; border-bottom: 1px solid var(--border); flex-wrap: wrap; gap: 12px; }
    .prow:last-child { border-bottom: none; padding-bottom: 0; }
    .plbl { font-size: 13.5px; font-weight: 600; color: var(--text); }
    .pdesc { font-size: 12px; color: var(--text-light); margin-top: 2px; }
    .pbadge { font-size: 11.5px; font-weight: 600; padding: 4px 10px; border-radius: 12px; background: var(--green-bg); color: var(--green); border: 1px solid rgba(16,185,129,0.2); }

    .overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.3); z-index: 99; backdrop-filter: blur(2px); }
    .overlay.open { display: block; }

    /* RESPONSIVE */
    @media (max-width: 768px) {
      body { overflow: auto; height: auto; display: block; }
      .sidebar { left: calc(-1 * var(--sidebar-w)); bottom: 0; height: 100vh; }
      .sidebar.open { left: 0; }
      .main { margin-left: 0 !important; height: 100vh; display: flex; flex-direction: column; }
      .menu-btn { display: inline-flex; }
      .topbar { padding: 0 16px; height: 60px; }
      .tb-title { font-size: 14.5px; }
      .upd { display: none; }

      #tab-carte { height: calc(100vh - 60px); position: relative; }
      #map-wrap { flex: 1; min-height: 0; overflow: hidden; position: relative; }
      
      .infobar { width: 90%; border-radius: 12px; padding: 10px 16px; gap: 10px; justify-content: space-between; }
      .isep { display: none; }
      .iitem { align-items: flex-start; }
      .ilbl { font-size: 8px; }
      .ival { font-size: 12px; }

      #btn-retour-carte {
        display: none; position: absolute; bottom: 24px; left: 50%; transform: translateX(-50%);
        z-index: 1000; background: var(--primary-dark); color: #FFF; border: none; border-radius: 20px;
        padding: 10px 20px; font-size: 13px; font-weight: 600; cursor: pointer;
        box-shadow: 0 8px 16px rgba(11,61,145,0.25); align-items: center; gap: 6px; font-family: 'Inter', sans-serif;
      }
      #btn-retour-carte[data-active="true"] { display: flex; }

      .usec { padding: 16px; height: calc(100vh - 60px); overflow-y: auto; }
      .stat-cards-container { grid-template-columns: 1fr; gap: 16px; }
    }
  </style>
</head>
<body>

<div class="overlay" id="overlay" onclick="closeMenu()"></div>

<!-- Dynamic Fleet Manager Map-Centric Sidebar[cite: 1] -->
<div class="sidebar" id="sidebar">
  <div class="s-logo">
    <div class="s-logo-row">
      <div class="s-logo-icon"><i class="fa-solid fa-location-arrow"></i></div>
      <div><div class="s-logo-name">FleetTracker</div><div class="s-logo-sub">Espace Client</div></div>
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
    <i class="fa-solid fa-map-location-dot nav-ico"></i> Carte GPS Live
  </div>
  <div class="nav-item" onclick="showTab('historique',this)">
    <i class="fa-solid fa-route nav-ico"></i> Historique
  </div>
  <div class="nav-item" onclick="showTab('parametres',this)">
    <i class="fa-solid fa-sliders nav-ico"></i> Paramètres
  </div>
  
  <div class="s-section" style="margin-top: 10px;">Ma Flotte de véhicules[cite: 1]</div>
  <div class="veh-list" id="veh-list">
    <div style="padding: 14px; color: var(--text-light); font-size: 13px; text-align: center;"><i class="fa-solid fa-spinner fa-spin"></i> Chargement...</div>
  </div>
  
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()"><i class="fa-solid fa-power-off"></i> Déconnexion</button>
  </div>
</div>

<div class="main">
  <div class="topbar">
    <div style="display: flex; align-items: center; gap: 12px;">
      <button class="menu-btn" onclick="toggleMenu()"><i class="fa-solid fa-bars"></i></button>
      <div class="tb-title" id="ttl">Aucun véhicule sélectionné[cite: 1]</div>
    </div>
    <div style="display: flex; align-items: center; gap: 12px;">
      <div class="live-pill"><div class="live-blink"></div>Temps réel</div>
      <span class="upd" id="tupd"><i class="fa-regular fa-clock"></i> Synchronisé</span>
    </div>
  </div>

  <!-- Dashboard Overview Tab -->
  <div id="tab-dashboard" class="usec active">
    <h2 style="font-size: 20px; font-weight: 700; color: var(--text); margin-bottom: 24px; letter-spacing: -0.5px;">Vue d'ensemble de l'activité</h2>

    <div class="stat-cards-container" id="stat-cards">
      <div class="card-modern" style="border-top: 3px solid var(--green);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: var(--green-bg); color: var(--green); display: flex; align-items: center; justify-content: center; font-size: 16px;"><i class="fa-solid fa-truck-fast"></i></div>
        </div>
        <div style="font-size: 32px; font-weight: 700; color: var(--green); line-height: 1.1;" id="cnt-mouvement">0</div>
        <div style="font-size: 13px; color: var(--text-muted); font-weight: 600; margin-top: 6px;">En déplacement</div>
      </div>
      
      <div class="card-modern" style="border-top: 3px solid var(--amber);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: var(--amber-bg); color: var(--amber); display: flex; align-items: center; justify-content: center; font-size: 16px;"><i class="fa-solid fa-square-parking"></i></div>
        </div>
        <div style="font-size: 32px; font-weight: 700; color: var(--amber); line-height: 1.1;" id="cnt-immobile">0</div>
        <div style="font-size: 13px; color: var(--text-muted); font-weight: 600; margin-top: 6px;">À l'arrêt</div>
      </div>
      
      <div class="card-modern" style="border-top: 3px solid var(--red);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <div style="width: 36px; height: 36px; border-radius: 8px; background: var(--red-bg); color: var(--red); display: flex; align-items: center; justify-content: center; font-size: 16px;"><i class="fa-solid fa-satellite-dish"></i></div>
        </div>
        <div style="font-size: 32px; font-weight: 700; color: var(--red); line-height: 1.1;" id="cnt-signal">0</div>
        <div style="font-size: 13px; color: var(--text-muted); font-weight: 600; margin-top: 6px;">Traceur inactif</div>
      </div>
    </div>

    <h3 style="font-size: 15px; font-weight: 700; color: var(--text); margin-bottom: 16px;">Télémétrie opérationnelle</h3>
    <div id="dash-list" style="display: flex; flex-direction: column; gap: 10px;">
      <div style="text-align: center; padding: 40px; color: var(--text-light); font-size: 14px;"><i class="fa-solid fa-spinner fa-spin"></i> Analyse télémétrique...</div>
    </div>
  </div>

  <!-- GPS Interactive Central Map Tab[cite: 1] -->
  <div id="tab-carte" style="flex: 1; display: none; flex-direction: column; overflow: hidden; position: relative;">
    
    <div id="map-wrap" style="flex: 1; display: none; position: relative;">
      <!-- Floating glassmorphism stats panel[cite: 1] -->
      <div class="infobar" id="infobar">
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
          <span class="ilbl">Vitesse GPS</span>
          <span class="ival" id="ispd">—</span>
        </div>
        <div class="isep"></div>
        <div class="iitem">
          <span class="ilbl">Satellites</span>
          <span class="ival" id="isat">—</span>
        </div>
      </div>
      
      <div id="map"></div>
      <button id="btn-retour-carte" onclick="toggleMenu()">
        <i class="fa-solid fa-bars"></i> Menu Flotte
      </button>
    </div>
    
    <!-- Beautiful Empty state illustrated[cite: 1] -->
    <div class="empty-state" id="empty">
      <div class="es-ico"><i class="fa-solid fa-map-location-dot"></i></div>
      <div class="es-title">Aucun véhicule sélectionné[cite: 1]</div>
      <div class="es-sub">Sélectionnez un véhicule dans la barre latérale pour centrer la carte et lancer le suivi télématique en direct.[cite: 1]</div>
    </div>
  </div>

  <!-- Historical Telemetry Tab -->
  <div id="tab-historique" class="usec">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
      <h2 style="font-size: 20px; font-weight: 700; color: var(--text); letter-spacing: -0.5px;">Historique des trajets</h2>
    </div>
    
    <div class="h-filters">
      <select class="h-select" id="uhv" onchange="loadUH()" style="min-width: 260px;">
        <option value="">Sélectionnez un véhicule...</option>
      </select>
      <select class="h-select" id="uhl" onchange="loadUH()">
        <option value="50">50 derniers points</option>
        <option value="100">100 derniers points</option>
        <option value="200">200 derniers points</option>
      </select>
    </div>
    
    <div class="htable">
      <div class="htable-wrap">
        <table>
          <thead>
            <tr>
              <th>#</th><th>Date / Heure</th><th>Latitude</th><th>Longitude</th><th>Vitesse</th><th>Signal</th>
            </tr>
          </thead>
          <tbody id="uhtb">
            <tr>
              <td colspan="6" style="text-align: center; padding: 48px; color: var(--text-light);">
                <i class="fa-solid fa-circle-notch fa-spin" style="font-size: 24px; margin-bottom: 8px;"></i>
                <div>Saisie requise</div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- Customer Settings Tab -->
  <div id="tab-parametres" class="usec">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
      <h2 style="font-size: 20px; font-weight: 700; color: var(--text); letter-spacing: -0.5px;">Paramètres de compte</h2>
    </div>
    
    <div class="pcard">
      <div class="ptitle">Informations du Profil</div>
      <div class="psub">Données de sécurité & email</div>
      <div class="prow">
        <div><div class="plbl">Compte Client</div><div class="pdesc" id="p-client-name">—</div></div>
      </div>
      <div class="prow">
        <div><div class="plbl">Email d'accès</div><div class="pdesc" id="p-client-email">—</div></div>
      </div>
    </div>
    
    <div class="pcard">
      <div class="ptitle">Statut Traceurs GPS</div>
      <div class="psub">Communication des terminaux IoT</div>
      <div class="prow">
        <div><div class="plbl">Fréquence de rafraîchissement</div><div class="pdesc">Mise à jour instantanée (temps réel)</div></div>
        <span class="pbadge"><i class="fa-solid fa-wifi"></i> 10s Interval</span>
      </div>
    </div>
  </div>
</div>

<script>
let M=null, currMarker=null, pathLine=null, selectedVehId=null, loop=null, liveData=[];

function toggleMenu(){
  document.getElementById("sidebar").classList.toggle("open");
  document.getElementById("overlay").classList.toggle("open");
}
function closeMenu(){
  document.getElementById("sidebar").classList.remove("open");
  document.getElementById("overlay").classList.remove("open");
}

function showTab(t,el){
  document.querySelectorAll(".usec").forEach(x=>x.style.display="none");
  document.getElementById("tab-carte").style.display="none";
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  
  if(t==="carte"){
    document.getElementById("tab-carte").style.display="flex";
    setTimeout(()=>{ if(M) M.invalidateSize(); },200);
  } else {
    document.getElementById("tab-"+t).style.display="block";
  }
  el.classList.add("active");
  closeMenu();
}

async function loadInit(){
  try {
    const me=await fetch("/api/me").then(r=>r.json());
    document.getElementById("uname").textContent=me.prenom+" "+me.nom;
    document.getElementById("p-client-name").textContent=me.prenom+" "+me.nom;
    document.getElementById("p-client-email").textContent=me.email;
    
    const vehs=await fetch("/api/vehicules").then(r=>r.json());
    initFleet(vehs);
  } catch(e) {}
}

function initFleet(list){
  const vl=document.getElementById("veh-list");
  const dsel=document.getElementById("uhv");
  
  if(!list.length){
    vl.innerHTML='<div style="padding:14px;color:var(--text-light);font-size:13px">Aucun véhicule actif</div>';
    dsel.innerHTML='<option value="">Aucun véhicule disponible</option>';
    return;
  }
  
  vl.innerHTML=list.map(v=>`
    <div class="veh-card" id="vc-${v.id}" onclick="selectVeh(${v.id},'${v.immatriculation}')">
      <div class="veh-immat"><i class="fa-solid fa-car-side" style="margin-right:6px;color:var(--primary-dark)"></i>${v.immatriculation}</div>
      <div class="veh-info">${v.marque} ${v.modele}</div>
      <div class="veh-live">
        <div class="dot ${v.actif?'live':''}" id="dot-${v.id}"></div>
        <div class="dot-lbl" id="lbl-${v.id}">${v.actif?'En ligne':'Hors-ligne'}</div>
      </div>
    </div>
  `).join("");
  
  dsel.innerHTML='<option value="">Sélectionnez un véhicule...</option>'+
    list.map(v=>`<option value="${v.id}">${v.immatriculation} (${v.marque})</option>`).join("");
    
  runTelemetryLoop();
}

/* Loop & State Management */
async function runTelemetryLoop(){
  if(loop) clearInterval(loop);
  await fetchAndRefreshTelemetry();
  loop = setInterval(fetchAndRefreshTelemetry, 10000);
}

async function fetchAndRefreshTelemetry(){
  try {
    const stats = await fetch("/api/telemetry").then(r=>r.json());
    liveData = stats;
    
    let mvt=0, rst=0, off=0;
    stats.forEach(s=>{
      const dot=document.getElementById("dot-"+s.vehicule_id);
      const lbl=document.getElementById("lbl-"+s.vehicule_id);
      if(s.actif){
        if(dot){ dot.className="dot live"; lbl.textContent="En ligne"; }
        if(s.vitesse > 2) mvt++; else rst++;
      } else {
        if(dot){ dot.className="dot"; lbl.textContent="Hors-ligne"; }
        off++;
      }
    });
    
    document.getElementById("cnt-mouvement").textContent=mvt;
    document.getElementById("cnt-immobile").textContent=rst;
    document.getElementById("cnt-signal").textContent=off;
    
    updateDashboardGrid(stats);
    if(selectedVehId) updateLivePointer(stats.find(x=>x.vehicule_id===selectedVehId));
  } catch(e) {}
}

function updateDashboardGrid(stats){
  const dl=document.getElementById("dash-list");
  if(!stats.length){
    dl.innerHTML='<div style="text-align:center;padding:24px;color:var(--text-light)">Aucun traceur détecté</div>';
    return;
  }
  dl.innerHTML=stats.map(s=>`
    <div class="card-modern" style="padding:16px; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <div style="font-weight:700;color:var(--primary-dark)">${s.immatriculation}</div>
        <div style="font-size:12px;color:var(--text-muted);margin-top:2px;">Dernière émission : ${s.timestamp||'Non disponible'}</div>
      </div>
      <div style="display:flex; gap:16px; align-items:center;">
        <span style="font-size:13px;font-weight:600;"><i class="fa-solid fa-gauge-high" style="color:var(--text-light);margin-right:4px"></i>${(s.vitesse||0).toFixed(1)} km/h</span>
        <span class="live-pill" style="background:${s.actif?'var(--green-bg)':'var(--red-bg)'}; color:${s.actif?'var(--green)':'var(--red)'}; border:none;">
          <div class="live-blink" style="background:${s.actif?'var(--green)':'var(--red)'}; animation:none;"></div>${s.actif?'Connecté':'Inactif'}
        </span>
      </div>
    </div>
  `).join("");
}

/* Map centric view selection[cite: 1] */
function selectVeh(id, immat){
  selectedVehId=id;
  document.querySelectorAll(".veh-card").forEach(x=>x.classList.remove("sel"));
  const card = document.getElementById("vc-"+id);
  if(card) card.classList.add("sel");
  
  document.getElementById("ttl").textContent=immat;
  document.getElementById("empty").style.display="none";
  document.getElementById("map-wrap").style.display="block";
  document.getElementById("btn-retour-carte").setAttribute("data-active", "true");
  
  if(!M){
    // Utilisation d'un style de carte professionnel type Esri World Imagery ou style clair épuré standard
    M = L.map('map', {zoomControl: false}).setView([14.6937, -17.4441], 13);
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
      maxZoom: 19,
      attribution: '&copy; CARTO'
    }).addTo(M);
    L.control.zoom({ position: 'bottomright' }).addTo(M);
  }
  
  showTab("carte", document.querySelector('[onclick*="carte"]'));
  const point = liveData.find(x=>x.vehicule_id===id);
  if(point) updateLivePointer(point, true);
}

/* Centers map automatically & updates path line dynamically[cite: 1] */
function updateLivePointer(p, forceRecenter=false){
  if(!p||!M||!p.latitude||!p.longitude) return;
  const pos=[p.latitude, p.longitude];
  
  document.getElementById("ilat").textContent=p.latitude.toFixed(6);
  document.getElementById("ilng").textContent=p.longitude.toFixed(6);
  document.getElementById("ispd").textContent=p.vitesse.toFixed(1)+" km/h";
  document.getElementById("isat").textContent=p.satellites||"—";
  document.getElementById("tupd").innerHTML=`<i class="fa-regular fa-clock"></i> MàJ: ${new Date().toLocaleTimeString('fr-FR')}`;
  
  if(!currMarker){
    const icon = L.divIcon({
      html: '<div style="background:var(--primary-dark);width:16px;height:16px;border:3px style solid #FFF;border-radius:50%;box-shadow:0 0 8px var(--primary-dark)"></div>',
      className: ''
    });
    currMarker=L.marker(pos, {icon}).addTo(M);
  } else {
    currMarker.setLatLng(pos);
  }
  
  if(forceRecenter) M.setView(pos, 15);
  fetchHistoricalTrackForLine(p.vehicule_id);
}

/* Dynamically query positions and render interactive track[cite: 1] */
async function fetchHistoricalTrackForLine(vid){
  try {
    const points = await fetch(`/api/positions/${vid}?limit=30`).then(r=>r.json());
    if(!points.length) return;
    const latlngs = points.map(x=>[x.latitude, x.longitude]);
    
    if(pathLine) M.removeLayer(pathLine);
    pathLine = L.polyline(latlngs, {color: '#0B3D91', weight: 4, opacity: 0.85}).addTo(M);
  } catch(e){}
}

/* Historical Tab management */
async function loadUH(){
  const vid=document.getElementById("uhv").value;
  const lim=document.getElementById("uhl").value;
  const tb=document.getElementById("uhtb");
  if(!vid) return;
  tb.innerHTML='<tr><td colspan="6" style="text-align:center;padding:48px;color:var(--text-light)"><i class="fa-solid fa-spinner fa-spin"></i> Traitement...</td></tr>';
  try {
    const data=await fetch(`/api/positions/${vid}?limit=${lim}`).then(r=>r.json());
    if(!data.length){
      tb.innerHTML='<tr><td colspan="6" style="text-align:center;padding:48px;color:var(--text-light)"><i class="fa-solid fa-route"></i> Aucune coordonnée enregistrée</td></tr>';
      return;
    }
    const rev=[...data].reverse();
    tb.innerHTML=rev.map((p,i)=>`
      <tr>
        <td style="color:var(--text-light);font-size:12px;font-weight:600">#${data.length-i}</td>
        <td style="font-size:13px;color:var(--text-muted)"><i class="fa-regular fa-clock" style="margin-right:6px"></i>${p.created_at||p.timestamp||"—"}</td>
        <td style="font-family:monospace;font-size:13px;font-weight:600;color:var(--primary-dark)">${(p.latitude||0).toFixed(6)}</td>
        <td style="font-family:monospace;font-size:13px;font-weight:600;color:var(--primary-dark)">${(p.longitude||0).toFixed(6)}</td>
        <td><span style="font-weight:600; padding:4px 8px; border-radius:6px; background:${(p.vitesse||0)>80?'var(--red-bg)':'var(--bg)'}; color:${(p.vitesse||0)>80?'var(--red)':'var(--text)'}">${(p.vitesse||0).toFixed(1)} km/h</span></td>
        <td><i class="fa-solid fa-satellite" style="color:var(--text-light);margin-right:6px"></i>${p.satellites||"—"}</td>
      </tr>
    `).join("");
  } catch(e) {}
}

async function doLogout(){await fetch("/api/logout",{method:"POST"});window.location.href="/";}
loadInit();
</script>
</body>
</html>"""