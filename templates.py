# ============================================================
#  templates.py — GPS Tracker v4
#  Design : Glassmorphism Premium Aurora
#  Fonts  : Syne (display) + DM Sans (body)
# ============================================================

# ═══════════════════════════════════════════════════════════════
#  STYLES COMMUNS (injectés dans chaque page)
# ═══════════════════════════════════════════════════════════════

_COMMON_HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap" rel="stylesheet">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="https://cdn.jsdelivr.net/npm/twemoji@14/assets/72x72/1f6f0.png">
<meta name="theme-color" content="#0a0a1a">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="GPS Tracker">
<style>
/* ── RESET & BASE ── */
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --glass:#ffffff0d;
  --glass-border:#ffffff1a;
  --glass-hover:#ffffff18;
  --glass-active:#ffffff22;
  --blur:saturate(180%) blur(20px);

  --aurora-1:#6c3bff;
  --aurora-2:#00d4ff;
  --aurora-3:#ff3cac;
  --aurora-4:#00ffa3;

  --primary:#7c5cfc;
  --primary-glow:rgba(124,92,252,0.4);
  --cyan:#00d4ff;
  --cyan-glow:rgba(0,212,255,0.35);
  --emerald:#00ffa3;
  --rose:#ff3cac;

  --bg:#08081a;
  --surface:rgba(255,255,255,0.06);
  --surface-2:rgba(255,255,255,0.09);
  --border:rgba(255,255,255,0.10);
  --border-2:rgba(255,255,255,0.16);

  --text:#f0f0ff;
  --text-2:#a0a0c0;
  --text-3:#606080;

  --green:#00ffa3;
  --green-bg:rgba(0,255,163,0.08);
  --green-bd:rgba(0,255,163,0.2);
  --red:#ff3cac;
  --red-bg:rgba(255,60,172,0.08);
  --red-bd:rgba(255,60,172,0.2);
  --amber:#ffca28;

  --r-sm:10px;
  --r-md:16px;
  --r-lg:22px;
  --r-xl:28px;

  --shadow-sm:0 2px 12px rgba(0,0,0,0.3);
  --shadow-md:0 8px 32px rgba(0,0,0,0.4);
  --shadow-lg:0 20px 60px rgba(0,0,0,0.5);
  --shadow-primary:0 8px 32px rgba(124,92,252,0.35);
  --shadow-cyan:0 8px 32px rgba(0,212,255,0.25);

  --sidebar-w:260px;
  --topbar-h:60px;
}

body{
  font-family:'DM Sans',sans-serif;
  background:var(--bg);
  color:var(--text);
  font-size:14px;
  min-height:100vh;
  overflow-x:hidden;
}

/* ── AURORA BACKGROUND ── */
.aurora-bg{
  position:fixed;inset:0;z-index:0;overflow:hidden;pointer-events:none;
}
.aurora-orb{
  position:absolute;border-radius:50%;filter:blur(80px);
  opacity:0.18;animation:drift 20s ease-in-out infinite alternate;
}
.ao1{width:700px;height:700px;background:var(--aurora-1);top:-200px;left:-200px;animation-delay:0s}
.ao2{width:600px;height:600px;background:var(--aurora-2);top:20%;right:-150px;animation-delay:-7s}
.ao3{width:500px;height:500px;background:var(--aurora-3);bottom:-100px;left:30%;animation-delay:-14s}
.ao4{width:400px;height:400px;background:var(--aurora-4);bottom:10%;right:20%;animation-delay:-5s}
@keyframes drift{
  0%{transform:translate(0,0) scale(1)}
  33%{transform:translate(40px,-30px) scale(1.05)}
  66%{transform:translate(-20px,40px) scale(0.95)}
  100%{transform:translate(30px,20px) scale(1.03)}
}

/* ── NOISE TEXTURE ── */
.aurora-bg::after{
  content:'';position:absolute;inset:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  background-size:200px 200px;opacity:0.4;
}

/* ── GLASS CARDS ── */
.glass{
  background:var(--glass);
  backdrop-filter:var(--blur);
  -webkit-backdrop-filter:var(--blur);
  border:1px solid var(--glass-border);
}
.glass:hover{
  background:var(--glass-hover);
  border-color:var(--border-2);
}

/* ── GRADIENT TEXT ── */
.grad-text{
  background:linear-gradient(135deg,var(--primary) 0%,var(--cyan) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.grad-text-warm{
  background:linear-gradient(135deg,var(--rose) 0%,var(--amber) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}

/* ── BUTTONS ── */
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:8px;
  height:40px;padding:0 20px;border:none;border-radius:var(--r-sm);
  font-family:'DM Sans',sans-serif;font-size:13px;font-weight:600;
  cursor:pointer;transition:all 0.2s cubic-bezier(0.4,0,0.2,1);
  letter-spacing:0.2px;position:relative;overflow:hidden;
}
.btn::after{
  content:'';position:absolute;inset:0;
  background:linear-gradient(rgba(255,255,255,0.1),rgba(255,255,255,0));
  opacity:0;transition:opacity 0.2s;
}
.btn:hover::after{opacity:1}
.btn:active{transform:scale(0.97)}

.btn-primary{
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  color:#fff;box-shadow:var(--shadow-primary);
}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 12px 40px rgba(124,92,252,0.5)}

.btn-ghost{
  background:var(--glass);border:1px solid var(--border);color:var(--text-2);
  backdrop-filter:blur(10px);
}
.btn-ghost:hover{background:var(--glass-hover);color:var(--text);border-color:var(--border-2)}

.btn-danger{
  background:var(--red-bg);border:1px solid var(--red-bd);color:var(--red);
}
.btn-danger:hover{background:rgba(255,60,172,0.14)}

.btn-success{
  background:var(--green-bg);border:1px solid var(--green-bd);color:var(--green);
}
.btn-success:hover{background:rgba(0,255,163,0.14)}

.btn-sm{height:32px;padding:0 14px;font-size:12px;border-radius:8px}
.btn-xs{height:26px;padding:0 10px;font-size:11px;border-radius:6px}

/* ── INPUTS ── */
.input{
  width:100%;height:44px;padding:0 14px;
  background:rgba(255,255,255,0.05);
  border:1px solid var(--border);border-radius:var(--r-sm);
  font-family:'DM Sans',sans-serif;font-size:14px;color:var(--text);
  outline:none;transition:all 0.2s;
  backdrop-filter:blur(10px);
}
.input:hover{border-color:var(--border-2);background:rgba(255,255,255,0.07)}
.input:focus{
  border-color:var(--primary);
  background:rgba(124,92,252,0.08);
  box-shadow:0 0 0 3px rgba(124,92,252,0.15);
}
.input::placeholder{color:var(--text-3)}

select.input{cursor:pointer}
select.input option{background:#1a1a3a;color:var(--text)}

/* ── BADGES ── */
.badge{
  display:inline-flex;align-items:center;gap:5px;
  padding:4px 12px;border-radius:99px;
  font-size:11px;font-weight:600;letter-spacing:0.3px;
}
.badge::before{content:'';width:5px;height:5px;border-radius:50%}
.badge-on{background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd)}
.badge-on::before{background:var(--green)}
.badge-off{background:var(--red-bg);color:var(--red);border:1px solid var(--red-bd)}
.badge-off::before{background:var(--red)}
.badge-info{background:rgba(124,92,252,0.1);color:var(--primary);border:1px solid rgba(124,92,252,0.2)}
.badge-info::before{background:var(--primary)}

/* ── ALERT BANNERS ── */
.alert{padding:12px 16px;border-radius:var(--r-sm);font-size:13px;font-weight:500;display:none}
.alert-err{background:var(--red-bg);border:1px solid var(--red-bd);color:var(--red)}
.alert-ok{background:var(--green-bg);border:1px solid var(--green-bd);color:var(--green)}

/* ── TABLES ── */
.table-card{
  background:var(--glass);backdrop-filter:var(--blur);
  border:1px solid var(--border);border-radius:var(--r-lg);overflow:hidden;
}
.table-wrap{overflow-x:auto}
table{width:100%;border-collapse:separate;border-spacing:0;min-width:580px}
thead{background:rgba(255,255,255,0.04)}
th{
  padding:12px 18px;font-size:10px;font-weight:700;
  color:var(--text-3);text-transform:uppercase;letter-spacing:1.2px;
  border-bottom:1px solid var(--border);font-family:'Syne',sans-serif;
}
td{
  padding:14px 18px;font-size:13px;color:var(--text-2);
  border-bottom:1px solid rgba(255,255,255,0.04);transition:background 0.15s;
}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(255,255,255,0.03)}
.td-main{font-weight:600;color:var(--text)}
.device-tag{
  font-size:11px;font-family:monospace;
  background:rgba(0,212,255,0.08);color:var(--cyan);
  padding:3px 10px;border-radius:6px;border:1px solid rgba(0,212,255,0.15);
  font-weight:600;
}

/* ── SIDEBAR ── */
.sidebar{
  position:fixed;top:0;left:0;bottom:0;width:var(--sidebar-w);
  background:rgba(8,8,26,0.7);backdrop-filter:saturate(180%) blur(24px);
  -webkit-backdrop-filter:saturate(180%) blur(24px);
  border-right:1px solid var(--border);
  display:flex;flex-direction:column;z-index:200;
  transition:left 0.3s cubic-bezier(0.4,0,0.2,1);
}
.s-logo{padding:24px 20px;border-bottom:1px solid var(--border)}
.s-logo-row{display:flex;align-items:center;gap:12px}
.s-logo-icon{
  width:40px;height:40px;border-radius:12px;flex-shrink:0;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  display:flex;align-items:center;justify-content:center;font-size:18px;
  box-shadow:var(--shadow-primary);
}
.s-logo-name{font-family:'Syne',sans-serif;font-size:16px;font-weight:700;color:var(--text)}
.s-logo-sub{font-size:10px;color:var(--text-3);margin-top:1px;font-weight:500}

.s-user{
  margin:12px;padding:12px 14px;
  background:var(--glass);border:1px solid var(--border);
  border-radius:var(--r-md);
}
.s-user-row{display:flex;align-items:center;gap:10px}
.s-avatar{
  width:34px;height:34px;border-radius:10px;flex-shrink:0;
  background:linear-gradient(135deg,var(--rose),var(--primary));
  display:flex;align-items:center;justify-content:center;font-size:15px;
}
.s-user-name{font-size:13px;font-weight:600;color:var(--text);font-family:'Syne',sans-serif}
.s-user-role{font-size:10px;color:var(--text-3);margin-top:2px;font-weight:500}

.s-nav-section{
  padding:14px 20px 6px;
  font-family:'Syne',sans-serif;font-size:9px;font-weight:700;
  color:var(--text-3);text-transform:uppercase;letter-spacing:1.8px;
}
.s-nav{flex:1;padding:4px 10px;overflow-y:auto}
.nav-item{
  display:flex;align-items:center;gap:10px;padding:10px 14px;
  border-radius:var(--r-sm);cursor:pointer;color:var(--text-2);
  font-size:13px;font-weight:500;transition:all 0.15s;
  margin-bottom:2px;border:1px solid transparent;
  font-family:'DM Sans',sans-serif;
}
.nav-item:hover{background:var(--glass);color:var(--text);border-color:var(--border)}
.nav-item.active{
  background:linear-gradient(135deg,rgba(124,92,252,0.15),rgba(0,212,255,0.08));
  color:var(--text);border-color:rgba(124,92,252,0.25);
  box-shadow:inset 0 0 20px rgba(124,92,252,0.08);
}
.nav-item.active .nav-ico{filter:drop-shadow(0 0 6px var(--primary))}
.nav-ico{font-size:16px;width:22px;text-align:center;flex-shrink:0}
.nav-label{flex:1}
.nav-badge{
  font-size:10px;font-weight:700;padding:2px 8px;border-radius:99px;
  background:linear-gradient(135deg,var(--primary),var(--cyan));color:#fff;
}

.s-bottom{
  padding:14px;border-top:1px solid var(--border);
  background:rgba(8,8,26,0.5);flex-shrink:0;
}
.btn-logout{
  width:100%;padding:10px 16px;
  background:var(--red-bg);border:1px solid var(--red-bd);color:var(--red);
  border-radius:var(--r-sm);cursor:pointer;font-size:13px;font-weight:600;
  font-family:'DM Sans',sans-serif;transition:all 0.15s;
  display:flex;align-items:center;justify-content:center;gap:8px;
}
.btn-logout:hover{background:rgba(255,60,172,0.14);transform:translateY(-1px)}

/* ── TOPBAR ── */
.topbar{
  position:sticky;top:0;z-index:100;height:var(--topbar-h);
  padding:0 28px;
  background:rgba(8,8,26,0.7);backdrop-filter:saturate(180%) blur(20px);
  -webkit-backdrop-filter:saturate(180%) blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;justify-content:space-between;
}
.menu-btn{
  display:none;background:none;border:none;cursor:pointer;
  font-size:20px;color:var(--text-2);padding:6px;margin-right:8px;
  border-radius:8px;transition:all 0.15s;
}
.menu-btn:hover{background:var(--glass);color:var(--text)}
.tb-crumb{font-size:11px;color:var(--text-3)}
.tb-title{font-family:'Syne',sans-serif;font-size:17px;font-weight:700;color:var(--text)}
.tb-actions{display:flex;align-items:center;gap:10px}

/* ── LIVE PILL ── */
.live-pill{
  display:flex;align-items:center;gap:6px;padding:6px 14px;
  background:var(--green-bg);border:1px solid var(--green-bd);
  border-radius:99px;font-size:11px;color:var(--green);font-weight:700;
  font-family:'Syne',sans-serif;letter-spacing:0.5px;
}
@keyframes pulse-dot{0%,100%{opacity:1;transform:scale(1)}50%{opacity:0.5;transform:scale(0.7)}}
.live-dot{width:6px;height:6px;border-radius:50%;background:var(--green);animation:pulse-dot 1.5s infinite}
.clock-pill{
  padding:6px 14px;background:var(--glass);border:1px solid var(--border);
  border-radius:99px;font-size:12px;color:var(--text-2);font-weight:500;
  font-variant-numeric:tabular-nums;
}

/* ── MODAL ── */
.modal-bg{
  display:none;position:fixed;inset:0;z-index:300;
  background:rgba(0,0,10,0.65);backdrop-filter:blur(8px);
  align-items:center;justify-content:center;padding:20px;
}
.modal-bg.open{display:flex;animation:fade-in 0.2s ease}
@keyframes fade-in{from{opacity:0}to{opacity:1}}
.modal{
  background:rgba(12,12,32,0.9);backdrop-filter:saturate(200%) blur(30px);
  -webkit-backdrop-filter:saturate(200%) blur(30px);
  border:1px solid var(--border-2);border-radius:var(--r-xl);
  padding:32px;width:100%;max-width:520px;
  max-height:90vh;overflow-y:auto;
  box-shadow:var(--shadow-lg),0 0 0 1px rgba(124,92,252,0.1);
  animation:modal-up 0.25s cubic-bezier(0.4,0,0.2,1);
  position:relative;
}
@keyframes modal-up{from{opacity:0;transform:translateY(20px) scale(0.97)}to{opacity:1;transform:translateY(0) scale(1)}}
.modal::before{
  content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);
  width:60%;height:2px;border-radius:0 0 4px 4px;
  background:linear-gradient(90deg,transparent,var(--primary),var(--cyan),transparent);
}
.modal-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:26px}
.modal-title{font-family:'Syne',sans-serif;font-size:18px;font-weight:700;color:var(--text)}
.modal-close{
  width:30px;height:30px;border-radius:8px;border:1px solid var(--border);
  background:var(--glass);cursor:pointer;font-size:14px;color:var(--text-3);
  display:flex;align-items:center;justify-content:center;transition:all 0.15s;
}
.modal-close:hover{background:var(--red-bg);color:var(--red);border-color:var(--red-bd)}
.modal-actions{
  display:flex;gap:10px;margin-top:26px;padding-top:22px;
  border-top:1px solid var(--border);
}
.modal-actions .btn{flex:1;height:44px}

/* ── FORM GROUPS ── */
.fg{margin-bottom:16px}
.fg label{
  display:block;font-size:10px;font-weight:700;color:var(--text-3);
  margin-bottom:8px;text-transform:uppercase;letter-spacing:1.2px;
  font-family:'Syne',sans-serif;
}
.fg .input{height:44px}
.fg-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}

/* ── EMPTY STATE ── */
.empty-state{
  padding:60px;text-align:center;
}
.empty-ico{font-size:48px;opacity:0.2;margin-bottom:12px}
.empty-title{font-family:'Syne',sans-serif;font-size:15px;font-weight:600;color:var(--text-2)}
.empty-sub{font-size:12px;color:var(--text-3);margin-top:4px}

/* ── OVERLAY MOBILE ── */
.overlay{
  display:none;position:fixed;inset:0;
  background:rgba(0,0,10,0.5);z-index:199;
  backdrop-filter:blur(4px);
}
.overlay.open{display:block;animation:fade-in 0.2s}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:4px;height:4px}
::-webkit-scrollbar-track{background:transparent}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:var(--border-2)}

/* ── SECTION ANIMATION ── */
.section{display:none}
.section.active{display:block;animation:section-in 0.25s ease}
@keyframes section-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .sidebar{left:calc(-1 * var(--sidebar-w));box-shadow:none}
  .sidebar.open{left:0;box-shadow:4px 0 30px rgba(0,0,0,0.5)}
  .menu-btn{display:flex}
  .topbar{padding:0 16px}
  .fg-row{grid-template-columns:1fr}
  .modal{padding:24px 18px;border-radius:var(--r-lg)}
}
</style>
"""

# ═══════════════════════════════════════════════════════════════
#  PAGE LOGIN
# ═══════════════════════════════════════════════════════════════

LOGIN_PAGE = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Connexion</title>
{_COMMON_HEAD}
<style>
body{{
  display:flex;align-items:center;justify-content:center;
  min-height:100vh;padding:20px;
  background:linear-gradient(135deg,#06061a 0%,#0d0a1f 50%,#06061a 100%);
}}
.login-wrap{{position:relative;z-index:1;width:100%;max-width:420px}}
.login-card{{
  background:rgba(14,14,36,0.8);
  backdrop-filter:saturate(200%) blur(30px);
  -webkit-backdrop-filter:saturate(200%) blur(30px);
  border:1px solid var(--border-2);border-radius:var(--r-xl);
  padding:48px 40px;
  box-shadow:var(--shadow-lg),
    0 0 0 1px rgba(124,92,252,0.08),
    inset 0 1px 0 rgba(255,255,255,0.06);
  position:relative;overflow:hidden;
}}
.login-card::before{{
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(124,92,252,0.6),rgba(0,212,255,0.6),transparent);
}}
.login-card::after{{
  content:'';position:absolute;top:-40%;right:-20%;
  width:300px;height:300px;border-radius:50%;
  background:radial-gradient(circle,rgba(124,92,252,0.08),transparent);
  pointer-events:none;
}}
.logo-section{{text-align:center;margin-bottom:40px}}
.logo-ring{{
  position:relative;width:72px;height:72px;margin:0 auto 18px;
}}
.logo-ring-outer{{
  position:absolute;inset:-4px;border-radius:20px;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  padding:2px;
}}
.logo-ring-outer-inner{{
  width:100%;height:100%;border-radius:18px;background:var(--bg);
}}
.logo-icon-wrap{{
  position:absolute;inset:0;border-radius:18px;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  display:flex;align-items:center;justify-content:center;font-size:28px;
  box-shadow:var(--shadow-primary);
}}
.login-title{{
  font-family:'Syne',sans-serif;font-size:26px;font-weight:800;
  background:linear-gradient(135deg,#fff 0%,rgba(255,255,255,0.7) 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  letter-spacing:-0.5px;
}}
.login-sub{{font-size:13px;color:var(--text-3);margin-top:6px;font-weight:400}}
.input-group{{margin-bottom:18px}}
.input-group label{{
  display:block;font-family:'Syne',sans-serif;font-size:10px;font-weight:700;
  color:var(--text-3);text-transform:uppercase;letter-spacing:1.4px;margin-bottom:9px;
}}
.input-wrap{{position:relative}}
.input-icon{{
  position:absolute;left:14px;top:50%;transform:translateY(-50%);
  font-size:15px;opacity:0.4;pointer-events:none;z-index:1;
}}
.input-wrap .input{{padding-left:44px;height:48px}}
.btn-login{{
  width:100%;height:50px;margin-top:8px;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  border:none;border-radius:var(--r-md);color:#fff;
  font-family:'Syne',sans-serif;font-size:15px;font-weight:700;
  cursor:pointer;letter-spacing:0.3px;position:relative;overflow:hidden;
  box-shadow:var(--shadow-primary);transition:all 0.25s;
}}
.btn-login::after{{
  content:'';position:absolute;inset:0;
  background:linear-gradient(rgba(255,255,255,0.15),rgba(255,255,255,0));
  opacity:0;transition:opacity 0.2s;
}}
.btn-login:hover{{transform:translateY(-2px);box-shadow:0 16px 48px rgba(124,92,252,0.5)}}
.btn-login:hover::after{{opacity:1}}
.btn-login:active{{transform:scale(0.98)}}
.forgot-link{{
  display:block;text-align:center;margin-top:16px;
  font-size:12px;color:var(--text-3);text-decoration:none;
  transition:color 0.2s;cursor:pointer;background:none;border:none;
  font-family:'DM Sans',sans-serif;width:100%;
}}
.forgot-link:hover{{color:var(--primary)}}
.trust-row{{
  display:flex;justify-content:center;gap:18px;margin-top:28px;
  padding-top:20px;border-top:1px solid var(--border);
}}
.trust-item{{
  display:flex;align-items:center;gap:5px;
  font-size:11px;color:var(--text-3);font-weight:500;
}}
.trust-dot{{
  width:5px;height:5px;border-radius:50%;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
}}
/* Modal forgot */
.forgot-modal{{
  background:rgba(12,12,32,0.95);
  backdrop-filter:saturate(200%) blur(30px);
  -webkit-backdrop-filter:saturate(200%) blur(30px);
  border:1px solid var(--border-2);border-radius:var(--r-xl);
  padding:32px;width:100%;max-width:420px;
  box-shadow:var(--shadow-lg);animation:modal-up 0.25s cubic-bezier(0.4,0,0.2,1);
  position:relative;
}}
.forgot-modal::before{{
  content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);
  width:60%;height:2px;border-radius:0 0 4px 4px;
  background:linear-gradient(90deg,transparent,var(--primary),var(--cyan),transparent);
}}
@media(max-width:480px){{
  .login-card{{padding:32px 22px;border-radius:var(--r-lg)}}
}}
</style>
</head><body>
<div class="aurora-bg">
  <div class="aurora-orb ao1"></div>
  <div class="aurora-orb ao2"></div>
  <div class="aurora-orb ao3"></div>
  <div class="aurora-orb ao4"></div>
</div>

<div class="login-wrap">
  <div class="login-card">
    <div class="logo-section">
      <div class="logo-ring">
        <div class="logo-icon-wrap">🛰️</div>
      </div>
      <div class="login-title">GPS Tracker</div>
      <div class="login-sub">Suivi de véhicules en temps réel</div>
    </div>

    <div class="alert alert-err" id="err" style="margin-bottom:18px"></div>

    <div class="input-group">
      <label>Adresse email</label>
      <div class="input-wrap">
        <span class="input-icon">✉️</span>
        <input class="input" type="email" id="email" placeholder="vous@email.com" autocomplete="email"/>
      </div>
    </div>
    <div class="input-group">
      <label>Mot de passe</label>
      <div class="input-wrap">
        <span class="input-icon">🔑</span>
        <input class="input" type="password" id="pwd" placeholder="••••••••"
          autocomplete="current-password"
          onkeydown="if(event.key==='Enter')doLogin()"/>
      </div>
    </div>

    <button class="btn-login" onclick="doLogin()">Connexion →</button>
    <button class="forgot-link" onclick="showForgot()">Mot de passe oublié ?</button>

    <div class="trust-row">
      <div class="trust-item"><div class="trust-dot"></div>Chiffré</div>
      <div class="trust-item"><div class="trust-dot"></div>Temps réel</div>
      <div class="trust-item"><div class="trust-dot"></div>GPS IoT</div>
    </div>
  </div>
</div>

<!-- Modal mot de passe oublié -->
<div class="modal-bg" id="forgot-bg">
  <div class="forgot-modal">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:22px">
      <div>
        <div style="font-family:'Syne',sans-serif;font-size:17px;font-weight:700;color:var(--text)">Mot de passe oublié</div>
        <div style="font-size:12px;color:var(--text-3);margin-top:4px">Recevez un lien de réinitialisation</div>
      </div>
      <button class="modal-close" onclick="hideForgot()">✕</button>
    </div>
    <div class="alert alert-err" id="forgot-err" style="margin-bottom:14px"></div>
    <div class="alert alert-ok" id="forgot-ok" style="margin-bottom:14px"></div>
    <div class="fg">
      <label>Email</label>
      <input class="input" type="email" id="forgot-email" placeholder="vous@email.com"
        onkeydown="if(event.key==='Enter')doForgot()"/>
    </div>
    <button class="btn btn-primary" style="width:100%;height:44px;margin-top:6px" onclick="doForgot()">
      Envoyer le lien →
    </button>
  </div>
</div>

<script>
async function doLogin(){{
  const email=document.getElementById("email").value.trim();
  const pwd=document.getElementById("pwd").value;
  const err=document.getElementById("err");
  err.style.display="none";
  if(!email||!pwd){{err.textContent="Veuillez remplir tous les champs.";err.style.display="block";return;}}
  const res=await fetch("/api/login",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{email,mot_de_passe:pwd}})}});
  const data=await res.json();
  if(res.ok){{window.location.href=data.role==="admin"?"/admin":"/dashboard";}}
  else{{err.textContent=data.error||"Identifiants incorrects.";err.style.display="block";}}
}}
if('serviceWorker' in navigator){{
  navigator.serviceWorker.register('/sw.js',{{scope:'/'}})
    .then(()=>console.log('[PWA] SW enregistré')).catch(e=>console.log('[PWA]',e));
}}
function showForgot(){{
  document.getElementById("forgot-bg").classList.add("open");
  document.getElementById("forgot-err").style.display="none";
  document.getElementById("forgot-ok").style.display="none";
  document.getElementById("forgot-email").value="";
}}
function hideForgot(){{document.getElementById("forgot-bg").classList.remove("open");}}
async function doForgot(){{
  const email=document.getElementById("forgot-email").value.trim();
  const err=document.getElementById("forgot-err"),ok=document.getElementById("forgot-ok");
  err.style.display=ok.style.display="none";
  if(!email){{err.textContent="Veuillez entrer votre email.";err.style.display="block";return;}}
  await fetch("/api/forgot-password",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{email}})}});
  ok.textContent="Si cet email existe, un lien vous a été envoyé.";ok.style.display="block";
}}
</script>
</body></html>"""

# ═══════════════════════════════════════════════════════════════
#  PAGE RESET PASSWORD
# ═══════════════════════════════════════════════════════════════

RESET_PAGE = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Nouveau mot de passe</title>
{_COMMON_HEAD}
<style>
body{{
  display:flex;align-items:center;justify-content:center;min-height:100vh;padding:20px;
  background:linear-gradient(135deg,#06061a,#0d0a1f,#06061a);
}}
.reset-card{{
  position:relative;z-index:1;
  background:rgba(14,14,36,0.85);
  backdrop-filter:saturate(200%) blur(30px);
  border:1px solid var(--border-2);border-radius:var(--r-xl);
  padding:48px 40px;width:100%;max-width:420px;
  box-shadow:var(--shadow-lg),0 0 0 1px rgba(124,92,252,0.08);
}}
.reset-card::before{{
  content:'';position:absolute;top:0;left:50%;transform:translateX(-50%);
  width:60%;height:2px;border-radius:0 0 4px 4px;
  background:linear-gradient(90deg,transparent,var(--primary),var(--cyan),transparent);
}}
.expired-state{{
  text-align:center;padding:20px 0;
}}
@media(max-width:480px){{.reset-card{{padding:32px 22px}}}}
</style>
</head><body>
<div class="aurora-bg">
  <div class="aurora-orb ao1"></div><div class="aurora-orb ao2"></div>
  <div class="aurora-orb ao3"></div><div class="aurora-orb ao4"></div>
</div>

<div class="reset-card">
  <div style="text-align:center;margin-bottom:36px">
    <div style="width:60px;height:60px;border-radius:16px;margin:0 auto 16px;
      background:linear-gradient(135deg,var(--primary),var(--cyan));
      display:flex;align-items:center;justify-content:center;font-size:26px;
      box-shadow:var(--shadow-primary)">🔑</div>
    <div style="font-family:'Syne',sans-serif;font-size:22px;font-weight:800;
      background:linear-gradient(135deg,#fff,rgba(255,255,255,0.7));
      -webkit-background-clip:text;-webkit-text-fill-color:transparent">Nouveau mot de passe</div>
    <div style="font-size:13px;color:var(--text-3);margin-top:6px">Choisissez un mot de passe sécurisé</div>
  </div>

  <div class="expired-state" id="expired" style="display:none">
    <div style="font-size:44px;margin-bottom:12px">⏰</div>
    <div style="font-family:'Syne',sans-serif;font-size:16px;font-weight:700;color:var(--text);margin-bottom:8px">Lien expiré</div>
    <div style="font-size:13px;color:var(--text-3);line-height:1.7">Ce lien n'est plus valide.<br>Faites une nouvelle demande sur la page de connexion.</div>
    <a href="/" style="display:inline-block;margin-top:20px;padding:10px 24px;
      background:linear-gradient(135deg,var(--primary),var(--cyan));
      color:#fff;border-radius:var(--r-sm);text-decoration:none;
      font-weight:600;font-size:13px">← Retour connexion</a>
  </div>

  <div id="form-wrap">
    <div class="alert alert-err" id="err" style="margin-bottom:16px"></div>
    <div class="alert alert-ok" id="ok" style="margin-bottom:16px"></div>
    <div class="fg">
      <label>Nouveau mot de passe</label>
      <input class="input" type="password" id="pwd1" placeholder="Minimum 6 caractères"/>
    </div>
    <div class="fg">
      <label>Confirmer le mot de passe</label>
      <input class="input" type="password" id="pwd2" placeholder="Répétez le mot de passe"
        onkeydown="if(event.key==='Enter')doReset()"/>
    </div>
    <button class="btn btn-primary" style="width:100%;height:48px;margin-top:8px;font-size:14px" onclick="doReset()">
      Enregistrer →
    </button>
  </div>
</div>

<script>
const token=new URLSearchParams(window.location.search).get("token");
async function init(){{
  if(!token){{showExpired();return;}}
  const r=await fetch(`/api/reset-password/check?token=${{token}}`).then(x=>x.json());
  if(!r.valid)showExpired();
}}
function showExpired(){{
  document.getElementById("expired").style.display="block";
  document.getElementById("form-wrap").style.display="none";
}}
async function doReset(){{
  const pwd1=document.getElementById("pwd1").value;
  const pwd2=document.getElementById("pwd2").value;
  const err=document.getElementById("err"),ok=document.getElementById("ok");
  err.style.display=ok.style.display="none";
  if(!pwd1||!pwd2){{err.textContent="Veuillez remplir les deux champs.";err.style.display="block";return;}}
  if(pwd1.length<6){{err.textContent="Minimum 6 caractères.";err.style.display="block";return;}}
  if(pwd1!==pwd2){{err.textContent="Les mots de passe ne correspondent pas.";err.style.display="block";return;}}
  const res=await fetch("/api/reset-password",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{token,mot_de_passe:pwd1}})}});
  const data=await res.json();
  if(res.ok){{ok.textContent="✓ Mot de passe modifié ! Redirection...";ok.style.display="block";setTimeout(()=>window.location.href="/",2500);}}
  else{{err.textContent=data.error||"Erreur.";err.style.display="block";}}
}}
init();
</script>
</body></html>"""

# ═══════════════════════════════════════════════════════════════
#  PAGE ADMIN
# ═══════════════════════════════════════════════════════════════

ADMIN_PAGE = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Admin</title>
{_COMMON_HEAD}
<style>
body{{display:flex;min-height:100vh;background:var(--bg)}}
.main{{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;min-width:0}}
.content{{padding:28px;flex:1}}

/* Stat cards */
.stats-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-bottom:28px;
}}
@media(max-width:900px){{.stats-grid{{grid-template-columns:1fr 1fr}}}}
@media(max-width:500px){{.stats-grid{{grid-template-columns:1fr}}}}
.stat-card{{
  background:var(--glass);backdrop-filter:var(--blur);
  border:1px solid var(--border);border-radius:var(--r-lg);
  padding:22px;position:relative;overflow:hidden;
  transition:all 0.25s cubic-bezier(0.4,0,0.2,1);cursor:default;
}}
.stat-card:hover{{
  border-color:var(--border-2);
  transform:translateY(-3px);
  box-shadow:var(--shadow-md);
}}
.stat-card::after{{
  content:'';position:absolute;bottom:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,var(--primary),var(--cyan));
}}
.stat-glow{{
  position:absolute;top:-20px;right:-20px;width:100px;height:100px;
  border-radius:50%;background:radial-gradient(circle,rgba(124,92,252,0.12),transparent);
  pointer-events:none;
}}
.stat-icon{{
  width:44px;height:44px;border-radius:12px;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  display:flex;align-items:center;justify-content:center;font-size:20px;
  box-shadow:var(--shadow-primary);margin-bottom:16px;
}}
.stat-val{{
  font-family:'Syne',sans-serif;font-size:36px;font-weight:800;
  color:var(--text);letter-spacing:-2px;line-height:1;
}}
.stat-label{{font-size:12px;color:var(--text-3);margin-top:6px;font-weight:500}}
.stat-trend{{
  position:absolute;top:20px;right:20px;
  font-size:10px;font-weight:700;padding:4px 10px;border-radius:99px;
  background:var(--green-bg);color:var(--green);border:1px solid var(--green-bd);
  font-family:'Syne',sans-serif;
}}

/* Section header */
.section-header{{
  display:flex;justify-content:space-between;align-items:center;
  margin-bottom:20px;flex-wrap:wrap;gap:12px;
}}
.section-title{{font-family:'Syne',sans-serif;font-size:18px;font-weight:700;color:var(--text)}}
.section-sub{{font-size:12px;color:var(--text-3);margin-top:3px}}

/* Mini stat row (propriétaires) */
.mini-stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:22px}}
@media(max-width:600px){{.mini-stats{{grid-template-columns:1fr 1fr}}}}
.mini-card{{
  background:var(--glass);backdrop-filter:var(--blur);border:1px solid var(--border);
  border-radius:var(--r-md);padding:14px 16px;position:relative;overflow:hidden;
  transition:all 0.2s;
}}
.mini-card::after{{content:'';position:absolute;bottom:0;left:0;right:0;height:1.5px;
  background:linear-gradient(90deg,var(--primary),var(--cyan));}}
.mini-ico{{font-size:20px;margin-bottom:6px}}
.mini-val{{
  font-family:'Syne',sans-serif;font-size:24px;font-weight:800;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.mini-lbl{{font-size:11px;color:var(--text-3);margin-top:3px;font-weight:500}}

/* Historique filters & stats */
.h-filters{{display:flex;gap:10px;margin-bottom:20px;flex-wrap:wrap}}
.h-select{{
  height:40px;padding:0 14px;
  background:var(--glass);backdrop-filter:blur(10px);
  border:1px solid var(--border);border-radius:var(--r-sm);
  font-size:13px;font-family:'DM Sans',sans-serif;color:var(--text);outline:none;
  transition:all 0.2s;
}}
.h-select:focus{{border-color:var(--primary);box-shadow:0 0 0 3px rgba(124,92,252,0.12)}}
.h-select option{{background:#1a1a3a}}
.hist-stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}}
@media(max-width:700px){{.hist-stats{{grid-template-columns:1fr 1fr}}}}
.hs-card{{
  background:var(--glass);backdrop-filter:var(--blur);border:1px solid var(--border);
  border-radius:var(--r-md);padding:14px 16px;
}}
.hs-val{{
  font-family:'Syne',sans-serif;font-size:22px;font-weight:800;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
}}
.hs-lbl{{font-size:11px;color:var(--text-3);margin-top:3px;font-weight:500}}

/* Settings cards */
.param-card{{
  background:var(--glass);backdrop-filter:var(--blur);border:1px solid var(--border);
  border-radius:var(--r-lg);padding:24px;margin-bottom:14px;
}}
.param-title{{font-family:'Syne',sans-serif;font-size:15px;font-weight:700;color:var(--text);margin-bottom:3px}}
.param-sub{{font-size:12px;color:var(--text-3);margin-bottom:20px}}
.param-row{{
  display:flex;justify-content:space-between;align-items:center;
  padding:14px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:10px;
}}
.param-row:last-child{{border-bottom:none;padding-bottom:0}}
.param-lbl{{font-size:13px;font-weight:600;color:var(--text)}}
.param-desc{{font-size:11px;color:var(--text-3);margin-top:3px}}

/* Responsive */
@media(max-width:768px){{
  .main{{margin-left:0!important}}
  .content{{padding:14px}}
  .topbar{{padding:0 14px}}
  .h-filters{{flex-direction:column}}
  .h-select{{width:100%}}
}}
</style>
</head><body>

<div class="aurora-bg" style="opacity:0.5">
  <div class="aurora-orb ao1"></div><div class="aurora-orb ao2"></div>
  <div class="aurora-orb ao3"></div>
</div>

<div class="overlay" id="overlay" onclick="closeMenu()"></div>

<!-- SIDEBAR -->
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
  <div class="s-user">
    <div class="s-user-row">
      <div class="s-avatar">⚙️</div>
      <div>
        <div class="s-user-name">Administrateur</div>
        <div class="s-user-role">Accès total</div>
      </div>
    </div>
  </div>
  <div class="s-nav-section">Navigation</div>
  <div class="s-nav">
    <div class="nav-item active" onclick="show('dashboard',this)">
      <span class="nav-ico">📊</span><span class="nav-label">Dashboard</span>
    </div>
    <div class="nav-item" onclick="show('proprietaires',this)">
      <span class="nav-ico">👥</span><span class="nav-label">Propriétaires</span>
    </div>
    <div class="nav-item" onclick="show('vehicules',this)">
      <span class="nav-ico">🚗</span><span class="nav-label">Véhicules</span>
    </div>
    <div class="nav-item" onclick="show('historique',this)">
      <span class="nav-ico">📍</span><span class="nav-label">Historique GPS</span>
    </div>
    <div class="nav-item" onclick="show('parametres',this)">
      <span class="nav-ico">⚙️</span><span class="nav-label">Paramètres</span>
    </div>
  </div>
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()">🚪 Déconnexion</button>
  </div>
</div>

<!-- MAIN -->
<div class="main">
  <div class="topbar">
    <div style="display:flex;align-items:center;gap:6px">
      <button class="menu-btn" onclick="toggleMenu()">☰</button>
      <span class="tb-crumb">Admin /&nbsp;</span>
      <span class="tb-title" id="page-title">Dashboard</span>
    </div>
    <div class="tb-actions">
      <div class="clock-pill" id="clk">--:--:--</div>
    </div>
  </div>

  <div class="content">

    <!-- DASHBOARD -->
    <div class="section active" id="s-dashboard">
      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-glow"></div>
          <div class="stat-trend">Total</div>
          <div class="stat-icon">👥</div>
          <div class="stat-val" id="stp">—</div>
          <div class="stat-label">Propriétaires enregistrés</div>
        </div>
        <div class="stat-card">
          <div class="stat-glow" style="background:radial-gradient(circle,rgba(0,212,255,0.12),transparent)"></div>
          <div class="stat-trend">Actifs</div>
          <div class="stat-icon" style="background:linear-gradient(135deg,var(--cyan),var(--emerald))">🚗</div>
          <div class="stat-val" id="stv">—</div>
          <div class="stat-label">Véhicules suivis</div>
        </div>
        <div class="stat-card">
          <div class="stat-glow" style="background:radial-gradient(circle,rgba(0,255,163,0.1),transparent)"></div>
          <div class="stat-trend" style="background:rgba(0,212,255,0.1);color:var(--cyan);border-color:rgba(0,212,255,0.2)">Live</div>
          <div class="stat-icon" style="background:linear-gradient(135deg,var(--emerald),var(--cyan))">📡</div>
          <div class="stat-val" style="font-size:28px;letter-spacing:-1px">24/7</div>
          <div class="stat-label">Surveillance active</div>
        </div>
      </div>
      <div class="table-card" style="padding:32px">
        <div style="font-family:'Syne',sans-serif;font-size:18px;font-weight:700;margin-bottom:12px">
          Bienvenue dans le <span class="grad-text">Centre de Contrôle</span>
        </div>
        <div style="font-size:14px;color:var(--text-2);line-height:1.8">
          Utilisez la navigation à gauche pour gérer les propriétaires, les véhicules et consulter l'historique GPS en temps réel.
        </div>
        <div style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap">
          <button class="btn btn-primary btn-sm" onclick="show('proprietaires',document.querySelectorAll('.nav-item')[1])">
            👥 Gérer les propriétaires
          </button>
          <button class="btn btn-ghost btn-sm" onclick="show('vehicules',document.querySelectorAll('.nav-item')[2])">
            🚗 Voir les véhicules
          </button>
        </div>
      </div>
    </div>

    <!-- PROPRIÉTAIRES -->
    <div class="section" id="s-proprietaires">
      <div class="mini-stats">
        <div class="mini-card"><div class="mini-ico">👥</div><div class="mini-val" id="pp-total">—</div><div class="mini-lbl">Total propriétaires</div></div>
        <div class="mini-card"><div class="mini-ico">✅</div><div class="mini-val" id="pp-actif">—</div><div class="mini-lbl">Comptes actifs</div></div>
        <div class="mini-card"><div class="mini-ico">🚗</div><div class="mini-val" id="pp-vehs">—</div><div class="mini-lbl">Véhicules associés</div></div>
      </div>
      <div class="section-header">
        <div>
          <div class="section-title">Propriétaires</div>
          <div class="section-sub">Gestion des comptes propriétaires</div>
        </div>
        <button class="btn btn-primary" onclick="openMP()">+ Nouveau propriétaire</button>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>Nom complet</th><th>Email</th><th>Téléphone</th>
              <th>Véhicules</th><th>Depuis</th><th>Statut</th><th>Actions</th>
            </tr></thead>
            <tbody id="tbp">
              <tr><td colspan="7"><div class="empty-state">
                <div class="empty-ico">👥</div><div class="empty-title">Chargement...</div>
              </div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- VÉHICULES -->
    <div class="section" id="s-vehicules">
      <div class="section-header">
        <div>
          <div class="section-title">Véhicules</div>
          <div class="section-sub">Flotte de véhicules enregistrés</div>
        </div>
        <button class="btn btn-primary" onclick="openMV()">+ Nouveau véhicule</button>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr>
              <th>Immatriculation</th><th>Marque / Modèle</th><th>Type</th>
              <th>Propriétaire</th><th>Device ID</th><th>Statut</th><th>Actions</th>
            </tr></thead>
            <tbody id="tbv">
              <tr><td colspan="7"><div class="empty-state">
                <div class="empty-ico">🚗</div><div class="empty-title">Chargement...</div>
              </div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- HISTORIQUE GPS -->
    <div class="section" id="s-historique">
      <div class="section-header">
        <div>
          <div class="section-title">Historique GPS</div>
          <div class="section-sub">Positions enregistrées par véhicule</div>
        </div>
      </div>
      <div class="h-filters">
        <select class="h-select" id="hv" onchange="loadHist()" style="flex:1;min-width:200px">
          <option value="">Sélectionnez un véhicule...</option>
        </select>
        <select class="h-select" id="hl" onchange="loadHist()">
          <option value="50">50 positions</option>
          <option value="100">100 positions</option>
          <option value="200">200 positions</option>
        </select>
      </div>
      <div class="hist-stats" id="hstats" style="display:none">
        <div class="hs-card"><div class="hs-val" id="hs1">0</div><div class="hs-lbl">Positions totales</div></div>
        <div class="hs-card"><div class="hs-val" id="hs2">0</div><div class="hs-lbl">Vitesse max km/h</div></div>
        <div class="hs-card"><div class="hs-val" id="hs3">0</div><div class="hs-lbl">Vitesse moy km/h</div></div>
        <div class="hs-card"><div class="hs-val" id="hs4">0</div><div class="hs-lbl">Satellites moy</div></div>
      </div>
      <div class="table-card">
        <div class="table-wrap">
          <table>
            <thead><tr><th>#</th><th>Date / Heure</th><th>Latitude</th><th>Longitude</th><th>Vitesse</th><th>Satellites</th></tr></thead>
            <tbody id="tbh">
              <tr><td colspan="6"><div class="empty-state">
                <div class="empty-ico">📍</div>
                <div class="empty-title">Sélectionnez un véhicule</div>
                <div class="empty-sub">pour afficher son historique GPS</div>
              </div></td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- PARAMÈTRES -->
    <div class="section" id="s-parametres">
      <div class="section-header">
        <div><div class="section-title">Paramètres</div><div class="section-sub">Configuration du système GPS Tracker</div></div>
      </div>
      <div class="param-card">
        <div class="param-title">Compte administrateur</div>
        <div class="param-sub">Informations de votre compte</div>
        <div class="param-row">
          <div><div class="param-lbl">Email de connexion</div><div class="param-desc">admin@gps.com</div></div>
          <span class="badge badge-info">Administrateur</span>
        </div>
        <div class="param-row">
          <div><div class="param-lbl">Niveau d'accès</div><div class="param-desc">Contrôle total sur toutes les fonctionnalités</div></div>
          <span class="badge badge-on">Actif</span>
        </div>
      </div>
      <div class="param-card">
        <div class="param-title">Système de suivi GPS</div>
        <div class="param-sub">État des services et configuration</div>
        <div class="param-row">
          <div><div class="param-lbl">API ESP32</div><div class="param-desc">Endpoint : POST /api/position</div></div>
          <span class="badge badge-on">En ligne</span>
        </div>
        <div class="param-row">
          <div><div class="param-lbl">Base de données</div><div class="param-desc">PostgreSQL</div></div>
          <span class="badge badge-on">Connectée</span>
        </div>
        <div class="param-row">
          <div><div class="param-lbl">Surveillance véhicules</div><div class="param-desc">Alerte après 5 min sans signal</div></div>
          <span class="badge badge-on">Active</span>
        </div>
      </div>
      <div class="param-card">
        <div class="param-title">À propos</div>
        <div class="param-sub">GPS Tracker v4 — Glassmorphism Aurora</div>
        <div class="param-row">
          <div><div class="param-lbl">Stack technique</div><div class="param-desc">Flask · PostgreSQL · Leaflet · PWA</div></div>
          <span class="badge badge-info">v4.0</span>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- MODAL NOUVEAU PROPRIÉTAIRE -->
<div class="modal-bg" id="mp">
  <div class="modal">
    <div class="modal-header">
      <div class="modal-title">Nouveau propriétaire</div>
      <button class="modal-close" onclick="closeM('mp')">✕</button>
    </div>
    <div class="alert alert-err" id="ep" style="margin-bottom:14px"></div>
    <div class="alert alert-ok" id="op" style="margin-bottom:14px"></div>
    <div class="fg-row">
      <div class="fg"><label>Nom *</label><input class="input" id="pn" placeholder="Dieng"/></div>
      <div class="fg"><label>Prénom *</label><input class="input" id="pp" placeholder="Saliou"/></div>
    </div>
    <div class="fg"><label>Email *</label><input class="input" type="email" id="pe" placeholder="saliou@email.com"/></div>
    <div class="fg"><label>Téléphone *</label><input class="input" id="p-tel" placeholder="+221 77 000 00 00"/></div>
    <div class="fg"><label>Mot de passe *</label><input class="input" type="password" id="pw" placeholder="Minimum 6 caractères"/></div>
    <div class="modal-actions">
      <button class="btn btn-ghost" onclick="closeM('mp')">Annuler</button>
      <button class="btn btn-primary" onclick="creerP()">Créer le compte</button>
    </div>
  </div>
</div>

<!-- MODAL MODIFIER PROPRIÉTAIRE -->
<div class="modal-bg" id="m-modif-p">
  <div class="modal">
    <div class="modal-header">
      <div class="modal-title">✏️ Modifier le propriétaire</div>
      <button class="modal-close" onclick="closeM('m-modif-p')">✕</button>
    </div>
    <input type="hidden" id="mp-id"/>
    <div class="alert alert-err" id="emp" style="margin-bottom:14px"></div>
    <div class="alert alert-ok" id="omp" style="margin-bottom:14px"></div>
    <div class="fg-row">
      <div class="fg"><label>Nom *</label><input class="input" id="mp-nom"/></div>
      <div class="fg"><label>Prénom *</label><input class="input" id="mp-prenom"/></div>
    </div>
    <div class="fg"><label>Email *</label><input class="input" type="email" id="mp-email"/></div>
    <div class="fg"><label>Téléphone</label><input class="input" id="mp-tel"/></div>
    <div class="fg">
      <label>Nouveau mot de passe <span style="color:var(--text-3);font-weight:400;text-transform:none">(laisser vide = inchangé)</span></label>
      <input class="input" type="password" id="mp-pw" placeholder="Laisser vide pour ne pas modifier"/>
    </div>
    <div class="modal-actions">
      <button class="btn btn-ghost" onclick="closeM('m-modif-p')">Annuler</button>
      <button class="btn btn-primary" onclick="sauvegarderP()">💾 Sauvegarder</button>
    </div>
  </div>
</div>

<!-- MODAL NOUVEAU VÉHICULE -->
<div class="modal-bg" id="mv">
  <div class="modal">
    <div class="modal-header">
      <div class="modal-title">Nouveau véhicule</div>
      <button class="modal-close" onclick="closeM('mv')">✕</button>
    </div>
    <div class="alert alert-err" id="ev" style="margin-bottom:14px"></div>
    <div class="alert alert-ok" id="ov" style="margin-bottom:14px"></div>
    <div class="fg"><label>Propriétaire *</label><select class="input" id="vp"></select></div>
    <div class="fg-row">
      <div class="fg"><label>Marque *</label><input class="input" id="vm" placeholder="Toyota"/></div>
      <div class="fg"><label>Modèle *</label><input class="input" id="vmo" placeholder="Corolla"/></div>
    </div>
    <div class="fg-row">
      <div class="fg"><label>Type *</label>
        <select class="input" id="vt">
          <option value="voiture">🚗 Voiture</option>
          <option value="moto">🏍️ Moto</option>
          <option value="camion">🚛 Camion</option>
          <option value="bus">🚌 Bus</option>
          <option value="autre">🚙 Autre</option>
        </select>
      </div>
      <div class="fg"><label>Couleur</label><input class="input" id="vc" placeholder="Blanc"/></div>
    </div>
    <div class="fg-row">
      <div class="fg"><label>Immatriculation *</label><input class="input" id="vi" placeholder="DK-1234-AB"/></div>
      <div class="fg"><label>Année</label><input class="input" type="number" id="va" placeholder="2022"/></div>
    </div>
    <div class="fg"><label>Device ID (ESP32) *</label><input class="input" id="vd" placeholder="vehicule_01"/></div>
    <div class="modal-actions">
      <button class="btn btn-ghost" onclick="closeM('mv')">Annuler</button>
      <button class="btn btn-primary" onclick="creerV()">Créer le véhicule</button>
    </div>
  </div>
</div>

<!-- MODAL MODIFIER VÉHICULE -->
<div class="modal-bg" id="m-modif-v">
  <div class="modal">
    <div class="modal-header">
      <div class="modal-title">✏️ Modifier le véhicule</div>
      <button class="modal-close" onclick="closeM('m-modif-v')">✕</button>
    </div>
    <input type="hidden" id="mv-id"/>
    <div class="alert alert-err" id="emv" style="margin-bottom:14px"></div>
    <div class="alert alert-ok" id="omv" style="margin-bottom:14px"></div>
    <div class="fg-row">
      <div class="fg"><label>Marque *</label><input class="input" id="mv-marque"/></div>
      <div class="fg"><label>Modèle *</label><input class="input" id="mv-modele"/></div>
    </div>
    <div class="fg-row">
      <div class="fg"><label>Type *</label>
        <select class="input" id="mv-type">
          <option value="voiture">🚗 Voiture</option>
          <option value="moto">🏍️ Moto</option>
          <option value="camion">🚛 Camion</option>
          <option value="bus">🚌 Bus</option>
          <option value="autre">🚙 Autre</option>
        </select>
      </div>
      <div class="fg"><label>Couleur</label><input class="input" id="mv-couleur"/></div>
    </div>
    <div class="fg-row">
      <div class="fg"><label>Immatriculation *</label><input class="input" id="mv-immat"/></div>
      <div class="fg"><label>Année</label><input class="input" type="number" id="mv-annee"/></div>
    </div>
    <div class="fg"><label>Device ID (ESP32) *</label><input class="input" id="mv-device"/></div>
    <div class="modal-actions">
      <button class="btn btn-ghost" onclick="closeM('m-modif-v')">Annuler</button>
      <button class="btn btn-primary" onclick="sauvegarderV()">💾 Sauvegarder</button>
    </div>
  </div>
</div>

<script>
const PAGE_NAMES={{dashboard:"Dashboard",proprietaires:"Propriétaires",vehicules:"Véhicules",historique:"Historique GPS",parametres:"Paramètres"}};
setInterval(()=>document.getElementById("clk").textContent=new Date().toLocaleTimeString('fr-FR'),1000);

function toggleMenu(){{document.getElementById("sidebar").classList.toggle("open");document.getElementById("overlay").classList.toggle("open");}}
function closeMenu(){{document.getElementById("sidebar").classList.remove("open");document.getElementById("overlay").classList.remove("open");}}

function show(n,el){{
  document.querySelectorAll(".section").forEach(s=>s.classList.remove("active"));
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  document.getElementById("s-"+n).classList.add("active");
  el.classList.add("active");
  document.getElementById("page-title").textContent=PAGE_NAMES[n];
  closeMenu();
  if(n==="proprietaires")loadP();
  if(n==="vehicules")loadV();
  if(n==="historique")initHist();
}}

async function loadStats(){{
  const[p,v]=await Promise.all([
    fetch("/api/admin/proprietaires").then(r=>r.json()),
    fetch("/api/admin/vehicules").then(r=>r.json())
  ]);
  document.getElementById("stp").textContent=p.length||0;
  document.getElementById("stv").textContent=v.filter(x=>x.actif).length||0;
}}

/* ── Propriétaires ── */
async function loadP(){{
  const data=await fetch("/api/admin/proprietaires").then(r=>r.json());
  const actifs=data.filter(p=>p.actif).length;
  const totalVehs=data.reduce((s,p)=>s+p.nb_vehicules,0);
  document.getElementById("pp-total").textContent=data.length;
  document.getElementById("pp-actif").textContent=actifs;
  document.getElementById("pp-vehs").textContent=totalVehs;
  const tb=document.getElementById("tbp");
  if(!data.length){{tb.innerHTML='<tr><td colspan="7"><div class="empty-state"><div class="empty-ico">👥</div><div class="empty-title">Aucun propriétaire enregistré</div><div class="empty-sub">Créez votre premier propriétaire</div></div></td></tr>';return;}}
  tb.innerHTML=data.map(p=>`<tr>
    <td class="td-main">${{p.prenom}} ${{p.nom}}</td>
    <td>${{p.email}}</td>
    <td>${{p.telephone||"—"}}</td>
    <td><span class="badge badge-info">${{p.nb_vehicules}} veh.</span></td>
    <td style="font-size:12px;color:var(--text-3)">${{(p.date_creation||"").slice(0,10)}}</td>
    <td><span class="badge ${{p.actif?'badge-on':'badge-off'}}">${{p.actif?'Actif':'Inactif'}}</span></td>
    <td><div style="display:flex;gap:6px;flex-wrap:wrap">
      <button class="btn btn-sm ${{p.actif?'btn-danger':'btn-success'}}" onclick="toggleP(${{p.id}})">${{p.actif?'Désactiver':'Activer'}}</button>
      <button class="btn btn-sm btn-ghost" onclick="ouvrirModifP(${{p.id}})">✏️</button>
    </div></td>
  </tr>`).join("");
}}

async function creerP(){{
  const e=document.getElementById("ep"),o=document.getElementById("op");
  e.style.display=o.style.display="none";
  const body={{nom:document.getElementById("pn").value.trim(),prenom:document.getElementById("pp").value.trim(),email:document.getElementById("pe").value.trim(),telephone:document.getElementById("p-tel").value.trim(),mot_de_passe:document.getElementById("pw").value}};
  if(!body.nom||!body.prenom||!body.email||!body.telephone||!body.mot_de_passe){{e.textContent="Tous les champs sont obligatoires.";e.style.display="block";return;}}
  const res=await fetch("/api/admin/proprietaires",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify(body)}});
  const data=await res.json();
  if(res.ok){{o.textContent="✓ Propriétaire créé avec succès !";o.style.display="block";["pn","pp","pe","p-tel","pw"].forEach(id=>document.getElementById(id).value="");loadStats();loadP();}}
  else{{e.textContent=data.error;e.style.display="block";}}
}}
async function toggleP(id){{await fetch(`/api/admin/proprietaires/${{id}}/toggle`,{{method:"POST"}});loadP();}}
async function ouvrirModifP(id){{
  const data=await fetch(`/api/admin/proprietaires/${{id}}`).then(r=>r.json());
  document.getElementById("mp-id").value=id;
  document.getElementById("mp-nom").value=data.nom||"";
  document.getElementById("mp-prenom").value=data.prenom||"";
  document.getElementById("mp-email").value=data.email||"";
  document.getElementById("mp-tel").value=data.telephone||"";
  document.getElementById("mp-pw").value="";
  document.getElementById("emp").style.display=document.getElementById("omp").style.display="none";
  document.getElementById("m-modif-p").classList.add("open");
}}
async function sauvegarderP(){{
  const id=document.getElementById("mp-id").value;
  const e=document.getElementById("emp"),o=document.getElementById("omp");
  e.style.display=o.style.display="none";
  const body={{nom:document.getElementById("mp-nom").value.trim(),prenom:document.getElementById("mp-prenom").value.trim(),email:document.getElementById("mp-email").value.trim(),telephone:document.getElementById("mp-tel").value.trim()}};
  const pw=document.getElementById("mp-pw").value;
  if(pw)body.mot_de_passe=pw;
  const res=await fetch(`/api/admin/proprietaires/${{id}}`,{{method:"PUT",headers:{{"Content-Type":"application/json"}},body:JSON.stringify(body)}});
  const data=await res.json();
  if(res.ok){{o.textContent="✓ Propriétaire modifié !";o.style.display="block";setTimeout(()=>closeM("m-modif-p"),1200);loadP();}}
  else{{e.textContent=data.error;e.style.display="block";}}
}}

/* ── Véhicules ── */
async function loadV(){{
  const data=await fetch("/api/admin/vehicules").then(r=>r.json());
  const tb=document.getElementById("tbv");
  if(!data.length){{tb.innerHTML='<tr><td colspan="7"><div class="empty-state"><div class="empty-ico">🚗</div><div class="empty-title">Aucun véhicule enregistré</div></div></td></tr>';return;}}
  tb.innerHTML=data.map(v=>`<tr>
    <td class="td-main">${{v.immatriculation}}</td>
    <td>${{v.marque}} ${{v.modele}}</td>
    <td style="color:var(--text-3)">${{v.type_vehicule}}</td>
    <td>${{v.proprietaire_nom}}</td>
    <td><span class="device-tag">${{v.device_id}}</span></td>
    <td><span class="badge ${{v.actif?'badge-on':'badge-off'}}">${{v.actif?'Actif':'Inactif'}}</span></td>
    <td><div style="display:flex;gap:6px;flex-wrap:wrap">
      <button class="btn btn-sm ${{v.actif?'btn-danger':'btn-success'}}" onclick="toggleV(${{v.id}})">${{v.actif?'Désactiver':'Activer'}}</button>
      <button class="btn btn-sm btn-ghost" onclick="ouvrirModifV(${{v.id}})">✏️</button>
    </div></td>
  </tr>`).join("");
}}
async function openMV(){{
  const data=await fetch("/api/admin/proprietaires").then(r=>r.json());
  document.getElementById("vp").innerHTML=data.map(p=>`<option value="${{p.id}}">${{p.prenom}} ${{p.nom}}</option>`).join("");
  document.getElementById("mv").classList.add("open");
}}
async function creerV(){{
  const e=document.getElementById("ev"),o=document.getElementById("ov");
  e.style.display=o.style.display="none";
  const body={{proprietaire_id:parseInt(document.getElementById("vp").value),marque:document.getElementById("vm").value.trim(),modele:document.getElementById("vmo").value.trim(),immatriculation:document.getElementById("vi").value.trim(),type_vehicule:document.getElementById("vt").value,couleur:document.getElementById("vc").value.trim(),annee:parseInt(document.getElementById("va").value)||2024,device_id:document.getElementById("vd").value.trim()}};
  const res=await fetch("/api/admin/vehicules",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify(body)}});
  const data=await res.json();
  if(res.ok){{o.textContent="✓ Véhicule créé !";o.style.display="block";loadStats();loadV();}}
  else{{e.textContent=data.error;e.style.display="block";}}
}}
async function toggleV(id){{await fetch(`/api/admin/vehicules/${{id}}/toggle`,{{method:"POST"}});loadV();}}
async function ouvrirModifV(id){{
  const data=await fetch(`/api/admin/vehicules/${{id}}`).then(r=>r.json());
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
}}
async function sauvegarderV(){{
  const id=document.getElementById("mv-id").value;
  const e=document.getElementById("emv"),o=document.getElementById("omv");
  e.style.display=o.style.display="none";
  const body={{marque:document.getElementById("mv-marque").value.trim(),modele:document.getElementById("mv-modele").value.trim(),immatriculation:document.getElementById("mv-immat").value.trim(),type_vehicule:document.getElementById("mv-type").value,couleur:document.getElementById("mv-couleur").value.trim(),annee:document.getElementById("mv-annee").value,device_id:document.getElementById("mv-device").value.trim()}};
  const res=await fetch(`/api/admin/vehicules/${{id}}`,{{method:"PUT",headers:{{"Content-Type":"application/json"}},body:JSON.stringify(body)}});
  const data=await res.json();
  if(res.ok){{o.textContent="✓ Véhicule modifié !";o.style.display="block";setTimeout(()=>closeM("m-modif-v"),1200);loadV();}}
  else{{e.textContent=data.error;e.style.display="block";}}
}}

/* ── Historique ── */
async function initHist(){{
  const vehs=await fetch("/api/admin/vehicules").then(r=>r.json());
  const sel=document.getElementById("hv");
  const cur=sel.value;
  sel.innerHTML='<option value="">Sélectionnez un véhicule...</option>'+
    vehs.filter(v=>v.actif).map(v=>`<option value="${{v.id}}">${{v.immatriculation}} — ${{v.marque}} ${{v.modele}}</option>`).join("");
  if(cur)sel.value=cur;
}}
async function loadHist(){{
  const vid=document.getElementById("hv").value,lim=document.getElementById("hl").value;
  if(!vid)return;
  const data=await fetch(`/api/positions/${{vid}}?limit=${{lim}}`).then(r=>r.json());
  const hs=document.getElementById("hstats"),tb=document.getElementById("tbh");
  if(!data.length){{hs.style.display="none";tb.innerHTML='<tr><td colspan="6"><div class="empty-state"><div class="empty-ico">📍</div><div class="empty-title">Aucune position enregistrée</div></div></td></tr>';return;}}
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
    <td style="color:var(--text-3);font-size:12px">#${{data.length-i}}</td>
    <td style="font-size:12px;color:var(--text-2)">${{p.created_at||p.timestamp||"—"}}</td>
    <td style="font-family:monospace;font-size:12px" class="grad-text">${{(p.latitude||0).toFixed(6)}}</td>
    <td style="font-family:monospace;font-size:12px" class="grad-text">${{(p.longitude||0).toFixed(6)}}</td>
    <td style="font-weight:700;color:${{(p.vitesse||0)>80?'var(--red)':'var(--text)'}}">${{(p.vitesse||0).toFixed(1)}} <span style="font-weight:400;color:var(--text-3);font-size:11px">km/h</span></td>
    <td style="color:var(--text-2)">${{p.satellites||"—"}}</td>
  </tr>`).join("");
}}

function openMP(){{document.getElementById("ep").style.display=document.getElementById("op").style.display="none";document.getElementById("mp").classList.add("open");}}
function closeM(id){{document.getElementById(id).classList.remove("open");}}
async function doLogout(){{await fetch("/api/logout",{{method:"POST"}});window.location.href="/";}}
loadStats();
</script>
</body></html>"""

# ═══════════════════════════════════════════════════════════════
#  PAGE USER
# ═══════════════════════════════════════════════════════════════

USER_PAGE = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>GPS Tracker — Mon suivi</title>
{_COMMON_HEAD}
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"><\/script>
<style>
body{{display:flex;height:100vh;overflow:hidden;background:var(--bg)}}
.main{{margin-left:var(--sidebar-w);flex:1;display:flex;flex-direction:column;overflow:hidden;min-width:0}}

/* ── Sidebar véhicules ── */
.veh-list{{flex:1;padding:6px 10px;overflow-y:auto}}
.veh-card{{
  padding:12px 14px;border-radius:var(--r-md);cursor:pointer;
  border:1px solid transparent;margin-bottom:6px;
  transition:all 0.2s cubic-bezier(0.4,0,0.2,1);
  position:relative;overflow:hidden;
}}
.veh-card:hover{{background:var(--glass);border-color:var(--border)}}
.veh-card.sel{{
  background:linear-gradient(135deg,rgba(124,92,252,0.12),rgba(0,212,255,0.06));
  border-color:rgba(124,92,252,0.3);
  box-shadow:0 0 20px rgba(124,92,252,0.1);
}}
.veh-card.sel::before{{
  content:'';position:absolute;left:0;top:0;bottom:0;width:3px;
  background:linear-gradient(180deg,var(--primary),var(--cyan));
  border-radius:4px 0 0 4px;
}}
.veh-immat{{font-family:'Syne',sans-serif;font-size:13px;font-weight:700;color:var(--text)}}
.veh-info{{font-size:11px;color:var(--text-3);margin-top:2px}}
.veh-live{{display:flex;align-items:center;gap:6px;margin-top:8px}}
@keyframes blink{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:0.5;transform:scale(0.7)}}}}
.live-dot-sm{{width:6px;height:6px;border-radius:50%;background:var(--text-3);flex-shrink:0;transition:all 0.4s}}
.live-dot-sm.on{{background:var(--green);animation:blink 1.5s infinite;box-shadow:0 0 6px var(--green)}}
.live-lbl{{font-size:10px;color:var(--text-3);font-weight:500}}

/* ── Map tab ── */
#tab-carte{{flex:1;display:flex;flex-direction:column;overflow:hidden}}

/* ── Infobar ── */
.infobar{{
  height:56px;padding:0 22px;
  background:rgba(8,8,26,0.8);backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
  display:flex;align-items:center;gap:0;flex-shrink:0;flex-wrap:nowrap;overflow:hidden;
}}
.info-item{{display:flex;flex-direction:column;padding:0 18px;border-right:1px solid var(--border);flex-shrink:0}}
.info-item:first-child{{padding-left:0}}
.info-item:last-child{{border-right:none}}
.info-lbl{{font-size:9px;font-weight:700;color:var(--text-3);text-transform:uppercase;letter-spacing:1.2px;font-family:'Syne',sans-serif}}
.info-val{{font-size:15px;font-weight:700;color:var(--text);margin-top:2px;font-variant-numeric:tabular-nums}}
.info-val.grad{{background:linear-gradient(135deg,var(--primary),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent}}

/* ── Map ── */
#map-wrap{{flex:1;position:relative;overflow:hidden}}
#map{{width:100%;height:100%}}

/* Leaflet override — dark theme */
.leaflet-container{{background:#1a1a2e}}
.leaflet-tile{{filter:brightness(0.85) saturate(0.9) hue-rotate(15deg)}}
.leaflet-control-zoom a{{
  background:rgba(14,14,36,0.9)!important;
  backdrop-filter:blur(10px)!important;
  color:var(--text)!important;
  border-color:var(--border)!important;
}}
.leaflet-control-zoom a:hover{{background:rgba(124,92,252,0.2)!important}}
.leaflet-control-attribution{{
  background:rgba(8,8,26,0.75)!important;
  backdrop-filter:blur(8px)!important;
  color:var(--text-3)!important;font-size:10px!important;
}}

/* Map overlay stats (flottant) */
.map-overlay{{
  position:absolute;bottom:20px;left:50%;transform:translateX(-50%);
  z-index:1000;display:none;
  background:rgba(10,10,28,0.85);backdrop-filter:saturate(200%) blur(20px);
  border:1px solid var(--border-2);border-radius:var(--r-lg);
  padding:14px 22px;display:flex;gap:22px;align-items:center;
  box-shadow:var(--shadow-lg);
  white-space:nowrap;
}}
.map-overlay.visible{{display:flex;animation:section-in 0.3s ease}}
.mo-item{{display:flex;flex-direction:column;align-items:center}}
.mo-val{{font-family:'Syne',sans-serif;font-size:18px;font-weight:800;
  background:linear-gradient(135deg,var(--primary),var(--cyan));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;}}
.mo-lbl{{font-size:9px;color:var(--text-3);font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-top:2px}}
.mo-sep{{width:1px;height:32px;background:var(--border)}}
.mo-speed-alert{{color:var(--red)!important;-webkit-text-fill-color:var(--red)!important}}

/* Empty state */
.empty-map{{
  flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:14px;background:radial-gradient(ellipse at center,rgba(124,92,252,0.04) 0%,transparent 70%);
}}

/* Sections */
.usec{{display:none;flex:1;overflow-y:auto;padding:24px;background:var(--bg)}}
.usec.active{{display:block;animation:section-in 0.25s ease}}

/* Historique user */
.h-filters{{display:flex;gap:10px;margin-bottom:20px;flex-wrap:wrap}}
.h-select{{
  height:40px;padding:0 14px;
  background:var(--glass);backdrop-filter:blur(10px);
  border:1px solid var(--border);border-radius:var(--r-sm);
  font-size:13px;font-family:'DM Sans',sans-serif;color:var(--text);outline:none;
  transition:all 0.2s;
}}
.h-select:focus{{border-color:var(--primary)}}
.h-select option{{background:#1a1a3a}}

/* Paramètres user */
.pcard{{
  background:var(--glass);backdrop-filter:var(--blur);border:1px solid var(--border);
  border-radius:var(--r-lg);padding:22px;margin-bottom:14px;
}}
.ptitle{{font-family:'Syne',sans-serif;font-size:15px;font-weight:700;color:var(--text);margin-bottom:3px}}
.psub{{font-size:12px;color:var(--text-3);margin-bottom:18px}}
.prow{{
  display:flex;justify-content:space-between;align-items:center;
  padding:12px 0;border-bottom:1px solid var(--border);flex-wrap:wrap;gap:8px;
}}
.prow:last-child{{border-bottom:none;padding-bottom:0}}
.plbl{{font-size:13px;font-weight:600;color:var(--text)}}
.pdesc{{font-size:11px;color:var(--text-3);margin-top:3px}}

/* ── RESPONSIVE MOBILE ── */
@media(max-width:768px){{
  body{{overflow:auto;height:auto;display:block}}
  .sidebar{{left:calc(-1 * var(--sidebar-w));height:100%;position:fixed}}
  .sidebar.open{{left:0;box-shadow:4px 0 30px rgba(0,0,0,0.6)}}
  .main{{margin-left:0!important;height:100vh;display:flex;flex-direction:column}}
  .menu-btn{{display:flex}}
  .topbar{{padding:0 14px;flex-shrink:0}}

  /* Carte plein écran corrigée */
  #tab-carte{{height:calc(100vh - 60px);flex-shrink:0}}
  #map-wrap{{height:100%;min-height:0}}
  #map{{height:100%!important}}

  /* Infobar scrollable horizontalement */
  .infobar{{
    height:auto;padding:10px 14px;flex-shrink:0;
    overflow-x:auto;gap:0;-webkit-overflow-scrolling:touch;
  }}
  .info-item{{padding:0 14px;flex-shrink:0}}

  /* Overlay map sur mobile en bas */
  .map-overlay{{
    bottom:16px;left:16px;right:16px;transform:none;
    justify-content:space-around;border-radius:var(--r-lg);
  }}

  .usec{{height:calc(100vh - 60px);overflow-y:auto;padding:16px}}
  .h-filters{{flex-direction:column}}
  .h-select{{width:100%}}
}}
</style>
</head><body>

<div class="aurora-bg" style="opacity:0.35">
  <div class="aurora-orb ao1"></div><div class="aurora-orb ao2"></div>
  <div class="aurora-orb ao3"></div>
</div>

<div class="overlay" id="overlay" onclick="closeMenu()"></div>

<!-- SIDEBAR -->
<div class="sidebar" id="sidebar">
  <div class="s-logo">
    <div class="s-logo-row">
      <div class="s-logo-icon">🛰️</div>
      <div><div class="s-logo-name">GPS Tracker</div><div class="s-logo-sub">Suivi en direct</div></div>
    </div>
  </div>
  <div class="s-user">
    <div class="s-user-row">
      <div class="s-avatar">👤</div>
      <div>
        <div class="s-user-name" id="uname">—</div>
        <div class="s-user-role">Propriétaire</div>
      </div>
    </div>
  </div>
  <div class="s-nav-section">Navigation</div>
  <div class="s-nav" style="flex:0;padding:4px 10px">
    <div class="nav-item active" id="nav-carte" onclick="showTab('carte',this)">
      <span class="nav-ico">🗺️</span><span class="nav-label">Carte GPS</span>
    </div>
    <div class="nav-item" onclick="showTab('historique',this)">
      <span class="nav-ico">📍</span><span class="nav-label">Historique</span>
    </div>
    <div class="nav-item" onclick="showTab('parametres',this)">
      <span class="nav-ico">⚙️</span><span class="nav-label">Paramètres</span>
    </div>
  </div>
  <div class="s-nav-section" style="padding-top:16px">Mes véhicules</div>
  <div class="veh-list" id="veh-list">
    <div style="padding:14px 4px;color:var(--text-3);font-size:12px">Chargement...</div>
  </div>
  <div class="s-bottom">
    <button class="btn-logout" onclick="doLogout()">🚪 Déconnexion</button>
  </div>
</div>

<!-- MAIN -->
<div class="main">
  <div class="topbar">
    <div style="display:flex;align-items:center;gap:4px">
      <button class="menu-btn" onclick="toggleMenu()">☰</button>
      <span class="tb-title" id="ttl">Sélectionnez un véhicule</span>
    </div>
    <div class="tb-actions">
      <div class="live-pill"><div class="live-dot"></div>Temps réel</div>
      <div class="clock-pill" id="clk" style="display:none">—</div>
    </div>
  </div>

  <!-- TAB CARTE -->
  <div id="tab-carte" style="flex:1;display:flex;flex-direction:column;overflow:hidden">
    <div class="infobar" id="infobar" style="display:none">
      <div class="info-item">
        <span class="info-lbl">Latitude</span>
        <span class="info-val grad" id="ilat">—</span>
      </div>
      <div class="info-item">
        <span class="info-lbl">Longitude</span>
        <span class="info-val grad" id="ilng">—</span>
      </div>
      <div class="info-item">
        <span class="info-lbl">Vitesse</span>
        <span class="info-val" id="ispd">—</span>
      </div>
      <div class="info-item">
        <span class="info-lbl">Satellites</span>
        <span class="info-val" id="isat">—</span>
      </div>
      <div class="info-item" style="border-right:none;margin-left:auto">
        <span class="info-lbl">Mise à jour</span>
        <span class="info-val" id="iupd" style="font-size:12px;color:var(--text-3)">—</span>
      </div>
    </div>

    <div id="map-wrap" style="flex:1;position:relative;display:none">
      <div id="map"></div>
      <!-- Overlay stats flottant sur la carte -->
      <div class="map-overlay" id="map-overlay">
        <div class="mo-item">
          <div class="mo-val" id="mo-spd">0</div>
          <div class="mo-lbl">km/h</div>
        </div>
        <div class="mo-sep"></div>
        <div class="mo-item">
          <div class="mo-val" id="mo-sat">—</div>
          <div class="mo-lbl">Satellites</div>
        </div>
        <div class="mo-sep"></div>
        <div class="mo-item">
          <div class="mo-val" id="mo-alt" style="font-size:14px">—</div>
          <div class="mo-lbl">Altitude m</div>
        </div>
      </div>
    </div>

    <div class="empty-map" id="empty">
      <div style="font-size:64px;filter:drop-shadow(0 0 20px rgba(124,92,252,0.3))">🛰️</div>
      <div style="font-family:'Syne',sans-serif;font-size:17px;font-weight:700;color:var(--text-2)">Aucun véhicule sélectionné</div>
      <div style="font-size:13px;color:var(--text-3);text-align:center;max-width:260px;line-height:1.7">
        Appuyez sur <strong style="color:var(--text-2)">☰</strong> puis choisissez un véhicule dans la liste pour démarrer le suivi GPS
      </div>
    </div>
  </div>

  <!-- TAB HISTORIQUE -->
  <div id="tab-historique" class="usec">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:22px">
      <div>
        <div style="font-family:'Syne',sans-serif;font-size:18px;font-weight:700;color:var(--text)">Historique GPS</div>
        <div style="font-size:12px;color:var(--text-3);margin-top:4px">Positions enregistrées</div>
      </div>
    </div>
    <div class="h-filters">
      <select class="h-select" id="uhv" onchange="loadUH()" style="flex:1;min-width:180px">
        <option value="">Sélectionnez un véhicule...</option>
      </select>
      <select class="h-select" id="uhl" onchange="loadUH()">
        <option value="50">50 positions</option>
        <option value="100">100 positions</option>
        <option value="200">200 positions</option>
      </select>
    </div>
    <div class="table-card">
      <div class="table-wrap">
        <table>
          <thead><tr><th>#</th><th>Date / Heure</th><th>Latitude</th><th>Longitude</th><th>Vitesse</th><th>Satellites</th></tr></thead>
          <tbody id="uhtb">
            <tr><td colspan="6"><div class="empty-state">
              <div class="empty-ico">📍</div>
              <div class="empty-title">Sélectionnez un véhicule</div>
            </div></td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- TAB PARAMÈTRES -->
  <div id="tab-parametres" class="usec">
    <div style="font-family:'Syne',sans-serif;font-size:18px;font-weight:700;color:var(--text);margin-bottom:22px">Paramètres</div>
    <div class="pcard">
      <div class="ptitle">Mon compte</div>
      <div class="psub">Informations de votre compte propriétaire</div>
      <div class="prow"><div><div class="plbl">Nom complet</div><div class="pdesc" id="pcn">—</div></div><span class="badge badge-on">Actif</span></div>
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
      <div class="ptitle">Notifications push</div>
      <div class="psub">Alertes si un véhicule perd le signal GPS</div>
      <div id="notif-wrap"><div style="font-size:12px;color:var(--text-3)">Chargement...</div></div>
    </div>
    <div class="pcard">
      <div class="ptitle">Système</div>
      <div class="psub">Informations sur l'application</div>
      <div class="prow">
        <div><div class="plbl">GPS Tracker v4.0</div><div class="pdesc">Glassmorphism Aurora · Flask · PostgreSQL</div></div>
        <span class="badge badge-info">PWA</span>
      </div>
    </div>
  </div>
</div>

<script>
let map=null,marker=null,poly=null,selId=null,interval=null,meD=null,vehD=[];

setInterval(()=>{{
  const clk=document.getElementById("clk");
  if(clk)clk.textContent=new Date().toLocaleTimeString('fr-FR');
}},1000);
document.getElementById("clk").style.display="flex";

function toggleMenu(){{
  document.getElementById("sidebar").classList.toggle("open");
  document.getElementById("overlay").classList.toggle("open");
}}
function closeMenu(){{
  document.getElementById("sidebar").classList.remove("open");
  document.getElementById("overlay").classList.remove("open");
}}

function showTab(n,el){{
  document.querySelectorAll(".nav-item").forEach(x=>x.classList.remove("active"));
  if(el)el.classList.add("active");
  document.getElementById("tab-carte").style.display=n==="carte"?"flex":"none";
  ["historique","parametres"].forEach(t=>{{
    const s=document.getElementById("tab-"+t);
    if(s)s.classList[n===t?"add":"remove"]("active");
  }});
  if(n==="historique")initUH();
  if(n==="parametres")loadParams();
  if(n==="carte"&&map)setTimeout(()=>map.invalidateSize(),100);
  closeMenu();
}}

function initMap(){{
  if(map)return;
  map=L.map("map",{{zoomControl:true}}).setView([14.6928,-17.4467],13);
  L.tileLayer("https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png",{{
    attribution:"© OpenStreetMap",maxZoom:19
  }}).addTo(map);
  poly=L.polyline([],{{
    color:"#7c5cfc",weight:3,opacity:0.8,
    dashArray:null,
  }}).addTo(map);
  // Ajoute un halo sous la polyligne
  L.polyline([],{{color:"#00d4ff",weight:8,opacity:0.1}}).addTo(map);
}}

function makeMarkerIcon(speed){{
  const color=speed>80?"#ff3cac":speed>50?"#ffca28":"#00ffa3";
  return L.divIcon({{
    html:`<div style="position:relative">
      <div style="width:18px;height:18px;
        background:linear-gradient(135deg,#7c5cfc,#00d4ff);
        border:3px solid #fff;border-radius:50%;
        box-shadow:0 0 0 4px rgba(124,92,252,0.25),0 4px 14px rgba(0,0,0,0.4)"></div>
      <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
        width:32px;height:32px;border-radius:50%;
        background:radial-gradient(circle,rgba(124,92,252,0.2),transparent);
        animation:ping 2s cubic-bezier(0,0,0.2,1) infinite"></div>
    </div>
    <style>@keyframes ping{{0%{{transform:scale(1);opacity:0.8}}100%{{transform:scale(2.5);opacity:0}}}}</style>`,
    iconSize:[18,18],iconAnchor:[9,9],
  }});
}}

async function selV(id,label,immat){{
  document.querySelectorAll(".veh-card").forEach(c=>c.classList.remove("sel"));
  const card=document.getElementById("vc"+id);
  if(card)card.classList.add("sel");
  selId=id;
  document.getElementById("ttl").textContent=immat+" · "+label;
  document.getElementById("empty").style.display="none";
  document.getElementById("infobar").style.display="flex";
  document.getElementById("map-wrap").style.display="block";
  document.getElementById("map-overlay").classList.add("visible");

  // Bascule vers carte et ferme menu
  showTab("carte",document.getElementById("nav-carte"));

  initMap();
  if(poly)poly.setLatLngs([]);
  if(marker){{map.removeLayer(marker);marker=null;}}
  setTimeout(()=>map.invalidateSize(),200);

  // Charge l'historique récent pour le tracé
  const hist=await fetch(`/api/positions/${{id}}?limit=200`).then(r=>r.json());
  if(hist.length){{
    poly.setLatLngs(hist.map(p=>[p.latitude,p.longitude]));
  }}

  if(interval)clearInterval(interval);
  refresh();
  interval=setInterval(refresh,2000);
}}

async function refresh(){{
  if(!selId)return;
  try{{
    const res=await fetch(`/api/positions/${{selId}}/last`);
    if(!res.ok)return;
    const p=await res.json();
    const ll=[p.latitude,p.longitude];
    const spd=p.vitesse||0;

    if(!marker){{
      marker=L.marker(ll,{{icon:makeMarkerIcon(spd)}}).addTo(map);
      map.setView(ll,15);
    }}else{{
      marker.setLatLng(ll);
      marker.setIcon(makeMarkerIcon(spd));
    }}
    poly.addLatLng(ll);

    // Infobar
    document.getElementById("ilat").textContent=p.latitude.toFixed(6)+"°";
    document.getElementById("ilng").textContent=p.longitude.toFixed(6)+"°";
    document.getElementById("ispd").textContent=spd.toFixed(1)+" km/h";
    document.getElementById("ispd").style.color=spd>80?"var(--red)":spd>50?"var(--amber)":"var(--text)";
    document.getElementById("isat").textContent=p.satellites||"—";
    document.getElementById("iupd").textContent=new Date().toLocaleTimeString('fr-FR');

    // Overlay flottant
    document.getElementById("mo-spd").textContent=spd.toFixed(0);
    document.getElementById("mo-spd").className="mo-val"+(spd>80?" mo-speed-alert":"");
    document.getElementById("mo-sat").textContent=p.satellites||"—";
    document.getElementById("mo-alt").textContent=p.altitude!=null?Math.round(p.altitude)+"":"—";

    // Live dot sidebar
    const dot=document.getElementById("dot"+selId);
    const lbl=document.getElementById("dlbl"+selId);
    if(dot)dot.className="live-dot-sm on";
    if(lbl)lbl.textContent="En direct";
  }}catch(e){{}}
}}

async function loadVehicules(){{
  const[vehs,m]=await Promise.all([
    fetch("/api/user/vehicules").then(r=>r.json()),
    fetch("/api/me").then(r=>r.json())
  ]);
  meD=m;vehD=vehs;
  document.getElementById("uname").textContent=m.prenom+" "+m.nom;
  const list=document.getElementById("veh-list");
  if(!vehs.length){{
    list.innerHTML='<div style="padding:14px 4px;color:var(--text-3);font-size:12px">Aucun véhicule associé à votre compte.</div>';
    return;
  }}
  list.innerHTML=vehs.map(v=>`
    <div class="veh-card" id="vc${{v.id}}" onclick="selV(${{v.id}},'${{v.marque}} ${{v.modele}}','${{v.immatriculation}}')">
      <div class="veh-immat">${{v.immatriculation}}</div>
      <div class="veh-info">${{v.marque}} ${{v.modele}} · ${{v.type_vehicule}}</div>
      <div class="veh-info" style="margin-top:2px">${{v.couleur||""}} ${{v.annee||""}}</div>
      <div class="veh-live">
        <div class="live-dot-sm" id="dot${{v.id}}"></div>
        <span class="live-lbl" id="dlbl${{v.id}}">En attente</span>
      </div>
    </div>`).join("");
}}

function initUH(){{
  const sel=document.getElementById("uhv");
  sel.innerHTML='<option value="">Sélectionnez un véhicule...</option>'+
    vehD.map(v=>`<option value="${{v.id}}">${{v.immatriculation}} — ${{v.marque}} ${{v.modele}}</option>`).join("");
}}

async function loadUH(){{
  const vid=document.getElementById("uhv").value,lim=document.getElementById("uhl").value;
  if(!vid)return;
  const data=await fetch(`/api/positions/${{vid}}?limit=${{lim}}`).then(r=>r.json());
  const tb=document.getElementById("uhtb");
  if(!data.length){{tb.innerHTML='<tr><td colspan="6"><div class="empty-state"><div class="empty-ico">📍</div><div class="empty-title">Aucune position</div></div></td></tr>';return;}}
  const rev=[...data].reverse();
  tb.innerHTML=rev.map((p,i)=>`<tr>
    <td style="color:var(--text-3);font-size:12px">#${{data.length-i}}</td>
    <td style="font-size:12px;color:var(--text-2)">${{p.created_at||"—"}}</td>
    <td style="font-family:monospace;font-size:12px" class="grad-text">${{(p.latitude||0).toFixed(6)}}</td>
    <td style="font-family:monospace;font-size:12px" class="grad-text">${{(p.longitude||0).toFixed(6)}}</td>
    <td style="font-weight:700;color:${{(p.vitesse||0)>80?'var(--red)':'var(--text)'}}">${{(p.vitesse||0).toFixed(1)}} <span style="font-weight:400;color:var(--text-3);font-size:11px">km/h</span></td>
    <td>${{p.satellites||"—"}}</td>
  </tr>`).join("");
}}

async function loadParams(){{
  if(!meD)return;
  document.getElementById("pcn").textContent=meD.prenom+" "+meD.nom;
  document.getElementById("pce").textContent=meD.email;
  document.getElementById("pct").textContent=meD.telephone||"—";
  document.getElementById("pcd").textContent=(meD.date_creation||"").slice(0,10);
  document.getElementById("pcv").innerHTML=vehD.length
    ?vehD.map(v=>`<div class="prow">
        <div>
          <div class="plbl">${{v.immatriculation}}</div>
          <div class="pdesc">${{v.marque}} ${{v.modele}} · ${{v.type_vehicule}}</div>
        </div>
        <span class="badge badge-on">Actif</span>
      </div>`).join("")
    :'<div style="color:var(--text-3);font-size:13px">Aucun véhicule associé</div>';
  await refreshNotifStatus();
}}

/* ── PUSH NOTIFICATIONS ── */
function urlBase64ToUint8Array(b64){{
  const pad='='.repeat((4-b64.length%4)%4);
  const b=(b64+pad).replace(/-/g,'+').replace(/_/g,'/');
  const raw=window.atob(b);const arr=new Uint8Array(raw.length);
  for(let i=0;i<raw.length;i++)arr[i]=raw.charCodeAt(i);return arr;
}}
async function refreshNotifStatus(){{
  const wrap=document.getElementById("notif-wrap");if(!wrap)return;
  if(!("Notification" in window)||!("serviceWorker" in navigator)){{
    wrap.innerHTML='<div style="font-size:12px;color:var(--text-3)">Non supporté par ce navigateur.</div>';return;
  }}
  const res=await fetch("/api/push/status").then(r=>r.json());
  const on=res.subscribed;
  wrap.innerHTML=`<div class="prow">
    <div>
      <div class="plbl">Alertes push</div>
      <div class="pdesc">Notification si un véhicule perd le signal plus de 5 min</div>
    </div>
    <button onclick="${{on?'desactiverNotifs':'activerNotifs'}}()" class="btn btn-sm ${{on?'btn-danger':'btn-primary'}}">
      ${{on?'🔕 Désactiver':'🔔 Activer'}}
    </button>
  </div>
  <div style="margin-top:10px;font-size:12px;color:var(--text-3)">
    Statut : ${{on?'<span style="color:var(--green);font-weight:600">✅ Activées</span>':'<span style="color:var(--text-3)">❌ Désactivées</span>'}}
  </div>`;
}}
async function activerNotifs(){{
  try{{
    const perm=await Notification.requestPermission();
    if(perm!=="granted"){{document.getElementById("notif-wrap").innerHTML+='<div style="color:var(--red);font-size:12px;margin-top:8px">Permission refusée.</div>';return;}}
    const{{publicKey}}=await fetch("/api/push/vapid-public-key").then(r=>r.json());
    const reg=await navigator.serviceWorker.register("/sw.js");
    await navigator.serviceWorker.ready;
    const sub=await reg.pushManager.subscribe({{userVisibleOnly:true,applicationServerKey:urlBase64ToUint8Array(publicKey)}});
    await fetch("/api/push/subscribe",{{method:"POST",headers:{{"Content-Type":"application/json"}},body:JSON.stringify({{subscription:sub.toJSON()}})}});
    await refreshNotifStatus();
  }}catch(e){{console.error(e);}}
}}
async function desactiverNotifs(){{
  await fetch("/api/push/unsubscribe",{{method:"POST"}});
  try{{const reg=await navigator.serviceWorker.getRegistration("/sw.js");if(reg){{const sub=await reg.pushManager.getSubscription();if(sub)await sub.unsubscribe();}}}}catch(e){{}}
  await refreshNotifStatus();
}}

async function doLogout(){{await fetch("/api/logout",{{method:"POST"}});window.location.href="/";}}
loadVehicules();
</script>
</body></html>"""