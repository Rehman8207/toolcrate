#!/usr/bin/env python3
"""
Append a complete Green + Blue gradient theme override to style.css.
Since CSS cascade uses last rule, this overrides everything safely.
No regex matching needed — 100% reliable.
"""
from pathlib import Path

ROOT = Path.cwd()
CSS = ROOT / "assets" / "style.css"

if not CSS.exists():
    print("❌ assets/style.css not found")
    input("Press Enter...")
    exit(1)

OVERRIDE_CSS = """

/* ============================================================
   GREEN + BLUE GRADIENT THEME — 2026
   Appended override (CSS cascade: last rule wins)
   ============================================================ */

/* ---------- NEW DARK PALETTE ---------- */
:root{
  --bg:#0A1410;
  --bg-2:#0F1A17;
  --surface:rgba(230,255,245,0.035);
  --surface-2:rgba(230,255,245,0.065);
  --surface-3:rgba(230,255,245,0.10);
  --border:rgba(129,230,180,0.10);
  --border-2:rgba(129,230,180,0.18);
  --border-strong:rgba(129,230,180,0.28);
  --ink:#E8F5EE;
  --ink-2:#A8C4B8;
  --ink-3:#6E8A7E;
  --emerald:#10B981;
  --mint:#34D399;
  --teal:#14B8A6;
  --cyan:#06B6D4;
  --sky:#38BDF8;
  --blue:#3B82F6;
  --lime:#84CC16;
  --amber:#F59E0B;
  --orange:#F97316;
  --rose:#F43F5E;
  --pink:#F43F5E;
  --violet:#3B82F6;
  --coral:#F97316;
  --grad-a:linear-gradient(135deg,#10B981 0%,#14B8A6 50%,#3B82F6 100%);
  --grad-1:linear-gradient(135deg,#10B981 0%,#06B6D4 50%,#3B82F6 100%);
  --grad-2:linear-gradient(135deg,#14B8A6 0%,#06B6D4 100%);
  --grad-3:linear-gradient(135deg,#84CC16 0%,#10B981 100%);
  --grad-4:linear-gradient(135deg,#F59E0B 0%,#F97316 100%);
  --grad-5:linear-gradient(135deg,#3B82F6 0%,#06B6D4 100%);
  --grad-hero:linear-gradient(135deg,#10B981 0%,#14B8A6 25%,#06B6D4 65%,#3B82F6 100%);
}

[data-theme="light"]{
  --bg:#F5FAF7;
  --bg-2:#FFFFFF;
  --surface:rgba(255,255,255,0.85);
  --surface-2:#FFFFFF;
  --surface-3:#F0F7F4;
  --border:rgba(15,42,32,0.10);
  --border-2:rgba(15,42,32,0.18);
  --border-strong:rgba(15,42,32,0.28);
  --ink:#0A1410;
  --ink-2:#3D5A50;
  --ink-3:#6E8A7E;
  --emerald:#059669;
  --mint:#10B981;
  --teal:#0D9488;
  --cyan:#0891B2;
  --sky:#0284C7;
  --blue:#2563EB;
  --lime:#65A30D;
  --amber:#D97706;
  --orange:#EA580C;
  --rose:#E11D48;
  --pink:#E11D48;
  --violet:#2563EB;
  --coral:#EA580C;
  --grad-a:linear-gradient(135deg,#059669 0%,#0D9488 50%,#2563EB 100%);
  --grad-1:linear-gradient(135deg,#059669 0%,#0891B2 50%,#2563EB 100%);
  --grad-2:linear-gradient(135deg,#0D9488 0%,#0891B2 100%);
  --grad-3:linear-gradient(135deg,#65A30D 0%,#059669 100%);
  --grad-4:linear-gradient(135deg,#D97706 0%,#EA580C 100%);
  --grad-5:linear-gradient(135deg,#2563EB 0%,#0891B2 100%);
  --grad-hero:linear-gradient(135deg,#059669 0%,#0D9488 25%,#0891B2 65%,#2563EB 100%);
}

/* ---------- BODY ---------- */
body{
  background:var(--bg) !important;
  background-image:
    radial-gradient(at 8% 0%,rgba(16,185,129,0.14) 0%,transparent 42%),
    radial-gradient(at 92% 8%,rgba(59,130,246,0.12) 0%,transparent 45%),
    radial-gradient(at 50% 100%,rgba(20,184,166,0.10) 0%,transparent 55%),
    radial-gradient(at 100% 60%,rgba(6,182,212,0.08) 0%,transparent 50%) !important;
  background-attachment:fixed !important;
  color:var(--ink) !important;
}
[data-theme="light"] body{
  background:#F5FAF7 !important;
  background-image:none !important;
}

/* ---------- BRAND ---------- */
.brand h1,.brand h2,.brand-h1{
  background:var(--grad-hero) !important;
  -webkit-background-clip:text !important;
  background-clip:text !important;
  -webkit-text-fill-color:transparent !important;
  transition:filter 0.3s ease !important;
}
.brand a:hover h1,.brand a:hover h2{
  filter:brightness(1.15) drop-shadow(0 0 20px rgba(16,185,129,0.4)) !important;
}

/* ---------- BADGES ---------- */
.badge{
  transition:all 0.25s ease !important;
  backdrop-filter:blur(12px) !important;
}
.badge:hover{transform:translateY(-2px) !important;box-shadow:0 8px 20px rgba(0,0,0,0.15) !important}
.badge.pink{
  color:#A8E6CF !important;
  border-color:rgba(16,185,129,0.45) !important;
  background:linear-gradient(135deg,rgba(16,185,129,0.20) 0%,rgba(20,184,166,0.10) 100%) !important;
  box-shadow:0 0 22px rgba(16,185,129,0.14) !important;
}
.badge.pink:hover{border-color:rgba(16,185,129,0.75) !important;box-shadow:0 8px 24px rgba(16,185,129,0.28) !important}
.badge.violet{
  color:#A8D5FF !important;
  border-color:rgba(59,130,246,0.45) !important;
  background:linear-gradient(135deg,rgba(59,130,246,0.20) 0%,rgba(6,182,212,0.10) 100%) !important;
  box-shadow:0 0 22px rgba(59,130,246,0.14) !important;
}
.badge.violet:hover{border-color:rgba(59,130,246,0.75) !important;box-shadow:0 8px 24px rgba(59,130,246,0.28) !important}
.badge.cyan{
  color:#9AE6F0 !important;
  border-color:rgba(6,182,212,0.45) !important;
  background:linear-gradient(135deg,rgba(6,182,212,0.20) 0%,rgba(20,184,166,0.10) 100%) !important;
  box-shadow:0 0 22px rgba(6,182,212,0.14) !important;
}
.badge.cyan:hover{border-color:rgba(6,182,212,0.75) !important;box-shadow:0 8px 24px rgba(6,182,212,0.28) !important}
.badge.lime{
  color:#D4F0A0 !important;
  border-color:rgba(132,204,22,0.45) !important;
  background:linear-gradient(135deg,rgba(132,204,22,0.20) 0%,rgba(16,185,129,0.10) 100%) !important;
  box-shadow:0 0 22px rgba(132,204,22,0.14) !important;
}
.badge.lime:hover{border-color:rgba(132,204,22,0.75) !important;box-shadow:0 8px 24px rgba(132,204,22,0.28) !important}
.badge.amber{
  color:#FFE0A8 !important;
  border-color:rgba(245,158,11,0.45) !important;
  background:linear-gradient(135deg,rgba(245,158,11,0.20) 0%,rgba(249,115,22,0.10) 100%) !important;
  box-shadow:0 0 22px rgba(245,158,11,0.14) !important;
}
.badge.amber:hover{border-color:rgba(245,158,11,0.75) !important;box-shadow:0 8px 24px rgba(245,158,11,0.28) !important}

/* ---------- CHIPS ---------- */
.chip{
  transition:all 0.25s ease !important;
}
.chip:hover{
  border-color:var(--emerald) !important;
  color:var(--emerald) !important;
  background:var(--surface-2) !important;
  transform:translateY(-1px) !important;
  box-shadow:0 4px 14px rgba(16,185,129,0.12) !important;
}
.chip.active{
  background:var(--grad-a) !important;
  color:#FFFFFF !important;
  border-color:transparent !important;
  box-shadow:0 6px 24px rgba(16,185,129,0.35),0 0 0 1px rgba(16,185,129,0.2) !important;
  transform:translateY(-1px) !important;
}
.chip-blog{
  display:inline-flex !important;
  align-items:center !important;
  gap:6px !important;
  background:linear-gradient(135deg,rgba(20,184,166,0.16) 0%,rgba(59,130,246,0.10) 100%) !important;
  border-color:rgba(20,184,166,0.40) !important;
  color:#7EE7D5 !important;
  font-weight:600 !important;
  margin-left:8px !important;
  padding:9px 20px !important;
  border-radius:999px !important;
  text-decoration:none !important;
  font-size:0.82rem !important;
  transition:all 0.25s ease !important;
}
.chip-blog:hover{
  background:linear-gradient(135deg,rgba(20,184,166,0.28) 0%,rgba(59,130,246,0.18) 100%) !important;
  border-color:var(--teal) !important;
  color:#A8F0E0 !important;
  box-shadow:0 6px 24px rgba(20,184,166,0.28) !important;
  transform:translateY(-1px) !important;
}

/* ---------- TOOL CARDS ---------- */
.tool-row{
  transition:all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
  position:relative !important;
}
.tool-row:hover{
  border-color:transparent !important;
  background:var(--surface-2) !important;
  transform:translateY(-4px) !important;
  box-shadow:0 20px 40px rgba(0,0,0,0.35),0 0 40px rgba(16,185,129,0.10) !important;
}
.tool-row .icon-wrap .icon{
  transition:all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
}
.tool-row:hover .icon-wrap .icon{
  background:var(--grad-a) !important;
  border-color:transparent !important;
  color:#FFFFFF !important;
  box-shadow:0 8px 20px rgba(16,185,129,0.35) !important;
  transform:scale(1.06) !important;
}
.tool-row:hover .icon-label{
  transform:scale(1.08) translateY(-1px) !important;
}
.tool-row:hover .info h3{
  background:var(--grad-a) !important;
  -webkit-background-clip:text !important;
  background-clip:text !important;
  -webkit-text-fill-color:transparent !important;
}
.tool-row:hover .arrow{
  color:var(--emerald) !important;
  transform:translateX(5px) !important;
}

/* ---------- ICON LABEL GRADIENTS ---------- */
.icon-label--pdf  {background:linear-gradient(135deg,#F43F5E 0%,#DC2626 100%) !important;}
.icon-label--img  {background:linear-gradient(135deg,#3B82F6 0%,#0284C7 100%) !important;}
.icon-label--text {background:linear-gradient(135deg,#14B8A6 0%,#0D9488 100%) !important;}
.icon-label--dev  {background:linear-gradient(135deg,#10B981 0%,#059669 100%) !important;}
.icon-label--num  {background:linear-gradient(135deg,#F59E0B 0%,#EA580C 100%) !important;}
.icon-label--seo  {background:linear-gradient(135deg,#06B6D4 0%,#3B82F6 100%) !important;}

/* ---------- BUTTONS ---------- */
.btn{
  background:var(--grad-a) !important;
  transition:all 0.25s ease !important;
  position:relative !important;
  overflow:hidden !important;
  box-shadow:0 4px 18px rgba(16,185,129,0.32),inset 0 1px 0 rgba(255,255,255,0.15) !important;
}
.btn::before{
  content:'' !important;
  position:absolute !important;
  top:0 !important;left:-100% !important;
  width:100% !important;height:100% !important;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.28),transparent) !important;
  transition:left 0.55s ease !important;
}
.btn:hover{
  transform:translateY(-2px) !important;
  box-shadow:0 12px 32px rgba(16,185,129,0.45),inset 0 1px 0 rgba(255,255,255,0.15) !important;
  filter:brightness(1.08) !important;
}
.btn:hover::before{left:100% !important}
.btn.secondary{
  background:var(--surface-2) !important;
  color:var(--ink) !important;
  border:1px solid var(--border-2) !important;
  box-shadow:none !important;
}
.btn.secondary:hover{
  background:var(--surface-3) !important;
  border-color:var(--teal) !important;
  color:var(--teal) !important;
  box-shadow:0 6px 20px rgba(20,184,166,0.18) !important;
}
.btn.secondary::before{display:none !important}

/* ---------- THEME TOGGLE ---------- */
.theme-toggle{
  transition:all 0.25s ease !important;
}
.theme-toggle:hover{
  border-color:var(--emerald) !important;
  color:var(--emerald) !important;
  transform:translateY(-1px) !important;
  box-shadow:0 6px 20px rgba(16,185,129,0.22) !important;
}

/* ---------- SEARCH ---------- */
#toolSearch:focus{
  border-color:var(--emerald) !important;
  background:var(--surface-2) !important;
  box-shadow:0 0 0 4px rgba(16,185,129,0.14),0 8px 30px rgba(16,185,129,0.15) !important;
}

/* ---------- HERO TITLE ---------- */
.hero-title .grad-word{
  background:var(--grad-hero) !important;
  -webkit-background-clip:text !important;
  background-clip:text !important;
  -webkit-text-fill-color:transparent !important;
}

/* ---------- PANEL ICON ---------- */
.panel-icon{
  background:var(--grad-a) !important;
  box-shadow:0 10px 30px rgba(16,185,129,0.35) !important;
  transition:transform 0.3s ease !important;
}
.panel-icon:hover{transform:scale(1.06) rotate(-3deg) !important}

/* ---------- BACK BUTTON ---------- */
.back-btn{
  transition:all 0.25s ease !important;
}
.back-btn:hover{
  color:var(--emerald) !important;
  border-color:var(--emerald) !important;
  background:var(--surface-3) !important;
  transform:translateX(-3px) !important;
  box-shadow:0 4px 14px rgba(16,185,129,0.15) !important;
}

/* ---------- STATS ---------- */
.stat{
  transition:all 0.25s ease !important;
}
.stat:hover{
  border-color:rgba(16,185,129,0.40) !important;
  background:var(--surface-3) !important;
  transform:translateY(-3px) !important;
  box-shadow:0 12px 30px rgba(0,0,0,0.25),0 0 30px rgba(16,185,129,0.10) !important;
}
.stat .n{
  background:var(--grad-a) !important;
  -webkit-background-clip:text !important;
  background-clip:text !important;
  -webkit-text-fill-color:transparent !important;
}

/* ---------- FEATURE ITEMS ---------- */
.feature-item{
  transition:all 0.25s ease !important;
}
.feature-item:hover{
  border-color:rgba(16,185,129,0.40) !important;
  background:var(--surface-2) !important;
  transform:translateY(-3px) !important;
  box-shadow:0 12px 30px rgba(0,0,0,0.25),0 0 30px rgba(16,185,129,0.10) !important;
}
.feature-item:hover svg{transform:scale(1.12) !important}
.feature-item svg{transition:transform 0.25s ease !important}

/* ---------- FOOTER LINKS ---------- */
.footer-links a{
  position:relative !important;
  transition:color 0.25s ease !important;
}
.footer-links a::after{
  content:'' !important;
  position:absolute !important;
  left:0 !important;bottom:-3px !important;
  width:100% !important;height:1px !important;
  background:var(--grad-a) !important;
  transform:scaleX(0) !important;
  transform-origin:left !important;
  transition:transform 0.25s ease !important;
}
.footer-links a:hover{color:var(--emerald) !important}
.footer-links a:hover::after{transform:scaleX(1) !important}

/* ---------- SCROLLBAR ---------- */
::-webkit-scrollbar{width:10px;height:10px}
::-webkit-scrollbar-track{background:var(--bg-2)}
::-webkit-scrollbar-thumb{
  background:linear-gradient(135deg,rgba(16,185,129,0.5),rgba(59,130,246,0.5));
  border-radius:5px;
}
::-webkit-scrollbar-thumb:hover{
  background:linear-gradient(135deg,rgba(16,185,129,0.8),rgba(59,130,246,0.8));
}

/* ---------- SELECTION ---------- */
::selection{background:rgba(16,185,129,0.35);color:#FFFFFF}
"""

css = CSS.read_text(encoding="utf-8")

if "GREEN + BLUE GRADIENT THEME — 2026" in css:
    print("⚠️  Theme already applied. Skipping.")
else:
    css += OVERRIDE_CSS
    CSS.write_text(css, encoding="utf-8")
    print("✅ assets/style.css — green + blue theme appended")
    print()
    print("=" * 60)
    print("🎉 DONE! Green + Blue gradient theme applied.")
    print("=" * 60)
    print()
    print("Test:")
    print("  1. python -m http.server 8000")
    print("  2. Open http://localhost:8000/")
    print("  3. Ctrl + Shift + R (hard refresh)")
    print("  4. Toggle dark/light mode")
    print("  5. Hover over cards, buttons, chips")
    print()
    print("  If you like it:")
    print("    git add .")
    print("    git commit -m 'Apply green + blue gradient theme'")
    print("    git push")
    print()
    print("  If not:")
    print("    git reset --hard HEAD")

input("Press Enter to close...")