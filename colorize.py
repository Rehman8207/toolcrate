import re
from pathlib import Path

ROOT = Path.cwd()

# ============ 1. NEW STYLE.CSS (adds colorful classes) ============
NEW_CSS = r""":root{
  --bg:#070B10;--surface:rgba(255,255,255,0.04);--surface-2:rgba(255,255,255,0.07);
  --surface-3:rgba(255,255,255,0.10);--border:rgba(255,255,255,0.09);--border-2:rgba(255,255,255,0.16);
  --ink:#EAF2F8;--ink-2:#B8C6D1;--ink-3:#6E7E8C;
  --emerald:#10B981;--mint:#34D399;--cyan:#22D3EE;--violet:#A78BFA;--lime:#A3E635;--pink:#FF4ECD;--amber:#FBBF24;--coral:#FB7185;
  --grad-a:linear-gradient(135deg,#10B981 0%,#22D3EE 100%);
  --grad-1:linear-gradient(135deg,#FF4ECD 0%,#A855F7 50%,#6366F1 100%);
  --grad-2:linear-gradient(135deg,#22D3EE 0%,#6366F1 100%);
  --grad-3:linear-gradient(135deg,#A3E635 0%,#34D399 100%);
  --grad-4:linear-gradient(135deg,#FBBF24 0%,#FB7185 100%);
  --radius-sm:10px;--radius-md:14px;--radius:16px;--radius-lg:20px;--radius-full:9999px;
  --maxw:1120px;--t:0.22s cubic-bezier(0.4,0,0.2,1);
  --font-body:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  --font-display:'Space Grotesk','Inter',sans-serif;
  --font-mono:'JetBrains Mono','SF Mono',monospace;
}
[data-theme="light"]{--bg:#F6F8FA;--surface:rgba(255,255,255,0.85);--surface-2:#FFF;--surface-3:#FFF;
  --border:rgba(15,23,42,0.08);--border-2:rgba(15,23,42,0.15);
  --ink:#0B1117;--ink-2:#334155;--ink-3:#64748B;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:var(--font-body);font-size:15px;line-height:1.6;color:var(--ink);
  background:var(--bg);
  background-image:
    radial-gradient(at 10% 0%,rgba(255,78,205,0.15) 0%,transparent 45%),
    radial-gradient(at 90% 5%,rgba(99,102,241,0.18) 0%,transparent 45%),
    radial-gradient(at 50% 100%,rgba(34,211,238,0.12) 0%,transparent 55%),
    radial-gradient(at 15% 85%,rgba(168,85,247,0.12) 0%,transparent 50%);
  background-attachment:fixed;-webkit-font-smoothing:antialiased;
  min-height:100vh;overflow-x:hidden}
img,svg,video{display:block;max-width:100%;height:auto}
button,input,select,textarea{font:inherit;color:inherit}
a{color:var(--emerald);text-decoration:none;transition:color var(--t)}
a:hover{color:var(--cyan)}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}

/* ============ COLORFUL HERO ============ */
.masthead{padding:24px 0 20px;margin-bottom:20px}
.masthead .row{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap}
.brand-block{display:flex;align-items:center;gap:14px}
.hero-illus{width:52px;height:52px;flex-shrink:0}
.brand h1{font-family:var(--font-display);font-size:1.75rem;font-weight:700;letter-spacing:-0.03em;
  background:var(--grad-a);-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;line-height:1.1}
.brand a{color:inherit;-webkit-text-fill-color:inherit}
.tagline{font-size:0.86rem;color:var(--ink-2);margin-top:3px;max-width:560px;line-height:1.5}
.theme-toggle{background:var(--surface);backdrop-filter:blur(20px);
  border:1px solid var(--border-2);border-radius:var(--radius-full);padding:9px 18px;
  font-size:0.82rem;font-weight:500;color:var(--ink);cursor:pointer;transition:all var(--t);
  display:inline-flex;align-items:center;gap:6px}
.theme-toggle:hover{border-color:var(--emerald);background:var(--surface-2);transform:translateY(-1px)}

/* Colorful badges */
.badge-row{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 12px}
.badge{font-family:var(--font-mono);font-size:0.72rem;padding:6px 12px;border-radius:999px;
  display:inline-flex;align-items:center;gap:6px;backdrop-filter:blur(10px);transition:all 0.25s}
.badge svg{width:13px;height:13px;flex:none}
.badge:hover{transform:translateY(-1px)}
.badge.pink{color:#FFC7EE;border:1px solid rgba(255,78,205,0.4);
  background:linear-gradient(135deg,rgba(255,78,205,0.18),rgba(255,78,205,0.06));
  box-shadow:0 0 20px rgba(255,78,205,0.15)}
.badge.violet{color:#D8B4FE;border:1px solid rgba(168,85,247,0.4);
  background:linear-gradient(135deg,rgba(168,85,247,0.18),rgba(168,85,247,0.06));
  box-shadow:0 0 20px rgba(168,85,247,0.15)}
.badge.cyan{color:#A5F3FC;border:1px solid rgba(34,211,238,0.4);
  background:linear-gradient(135deg,rgba(34,211,238,0.18),rgba(34,211,238,0.06));
  box-shadow:0 0 20px rgba(34,211,238,0.15)}
.badge.lime{color:#D9F99D;border:1px solid rgba(163,230,53,0.4);
  background:linear-gradient(135deg,rgba(163,230,53,0.18),rgba(163,230,53,0.06));
  box-shadow:0 0 20px rgba(163,230,53,0.15)}
.badge.amber{color:#FDE68A;border:1px solid rgba(251,191,36,0.4);
  background:linear-gradient(135deg,rgba(251,191,36,0.18),rgba(251,191,36,0.06));
  box-shadow:0 0 20px rgba(251,191,36,0.15)}

/* Big gradient page title */
.hero-title{font-family:var(--font-display);font-weight:700;font-size:clamp(1.8rem,4vw,2.6rem);
  line-height:1.08;letter-spacing:-0.02em;margin:10px 0 12px;max-width:16ch}
.hero-title .grad-word{background:var(--grad-1);-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;font-style:italic}
.hero-sub{color:var(--ink-2);font-size:0.98rem;line-height:1.55;max-width:62ch;margin-bottom:4px}

/* Section title with gradient */
.section-title{font-family:var(--font-display);font-size:1.5rem;font-weight:700;
  letter-spacing:-0.02em;margin:0 0 6px;
  background:linear-gradient(135deg,#F3F0FF 0%,#A9A3D0 100%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;
  display:inline-block}
[data-theme="light"] .section-title{background:linear-gradient(135deg,#0B1117 0%,#64748B 100%);
  -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.section-lead{color:var(--ink-2);font-size:0.94rem;margin:0 0 20px;line-height:1.6}

/* ============ SEARCH & CHIPS ============ */
.search-row{margin-top:20px}
#toolSearch{width:100%;padding:16px 24px;border:1px solid var(--border-2);border-radius:var(--radius-lg);
  background:var(--surface);backdrop-filter:blur(20px);font-size:0.95rem;color:var(--ink);transition:all var(--t)}
#toolSearch:focus{outline:none;border-color:var(--pink);background:var(--surface-2);
  box-shadow:0 0 0 4px rgba(255,78,205,0.12),0 0 30px rgba(255,78,205,0.15)}
#toolSearch::placeholder{color:var(--ink-3)}
.category-rail{display:flex;gap:8px;margin-bottom:24px;overflow-x:auto;padding-bottom:4px;scrollbar-width:none}
.category-rail::-webkit-scrollbar{display:none}
.chip{padding:9px 20px;border:1px solid var(--border-2);border-radius:var(--radius-full);
  background:var(--surface);backdrop-filter:blur(20px);font-size:0.82rem;font-weight:500;
  color:var(--ink-2);cursor:pointer;transition:all var(--t);white-space:nowrap}
.chip:hover{border-color:var(--pink);color:var(--pink);background:var(--surface-2)}
.chip.active{background:var(--grad-1);color:#fff;border-color:transparent;box-shadow:0 4px 20px rgba(168,85,247,0.4)}

/* ============ COLORFUL FEATURE CARDS ============ */
.feature-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin-top:20px}
.feature-card{background:var(--surface);backdrop-filter:blur(20px);border:1px solid var(--border);
  border-radius:var(--radius-md);padding:18px;position:relative;overflow:hidden;transition:all 0.3s}
.feature-card::before{content:'';position:absolute;inset:0;opacity:0.08;transition:opacity 0.3s;pointer-events:none}
.feature-card:hover{transform:translateY(-3px);border-color:rgba(255,255,255,0.25)}
.feature-card:hover::before{opacity:0.16}
.feature-card svg{width:22px;height:22px;margin-bottom:10px;padding:8px;box-sizing:content-box;
  border-radius:10px;position:relative;z-index:1}
.feature-card h3{font-family:var(--font-display);font-size:0.95rem;font-weight:600;margin:0 0 6px;
  position:relative;z-index:1}
.feature-card p{font-size:0.82rem;color:var(--ink-2);line-height:1.55;margin:0;position:relative;z-index:1}
.feature-card.pink::before{background:linear-gradient(135deg,#FF4ECD,#A855F7)}
.feature-card.pink svg{background:rgba(255,78,205,0.18);color:#FF9EE4}
.feature-card.violet::before{background:linear-gradient(135deg,#A855F7,#6366F1)}
.feature-card.violet svg{background:rgba(168,85,247,0.18);color:#D8B4FE}
.feature-card.cyan::before{background:linear-gradient(135deg,#22D3EE,#6366F1)}
.feature-card.cyan svg{background:rgba(34,211,238,0.18);color:#A5F3FC}
.feature-card.lime::before{background:linear-gradient(135deg,#A3E635,#34D399)}
.feature-card.lime svg{background:rgba(163,230,53,0.18);color:#D9F99D}
.feature-card.amber::before{background:linear-gradient(135deg,#FBBF24,#FB7185)}
.feature-card.amber svg{background:rgba(251,191,36,0.18);color:#FDE68A}
.feature-card.coral::before{background:linear-gradient(135deg,#FB7185,#A855F7)}
.feature-card.coral svg{background:rgba(251,113,133,0.18);color:#FECDD3}

/* ============ TOOL LIST (colorful) ============ */
.tool-list{display:flex;flex-direction:column;gap:10px}
.tool-row{display:grid;grid-template-columns:40px 48px 1fr auto 32px;gap:16px;align-items:center;
  padding:18px 22px;background:var(--surface);backdrop-filter:blur(20px);
  border:1px solid var(--border);border-radius:var(--radius-lg);color:inherit;transition:all var(--t);
  animation:fadeUp 0.4s ease both;position:relative;overflow:hidden;text-decoration:none}
@keyframes fadeUp{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.tool-row::before{content:'';position:absolute;top:0;left:0;width:3px;height:100%;
  background:var(--grad-1);transform:scaleY(0);transform-origin:top;transition:transform var(--t)}
.tool-row:hover::before{transform:scaleY(1)}
.tool-row:hover{border-color:rgba(168,85,247,0.4);background:var(--surface-2);transform:translateX(4px);
  box-shadow:0 8px 30px rgba(0,0,0,0.3),0 0 30px rgba(168,85,247,0.1)}
.tool-row .idx{font-family:var(--font-mono);font-size:0.72rem;font-weight:600;color:var(--ink-3);opacity:0.7}
.tool-row .icon{width:44px;height:44px;display:flex;align-items:center;justify-content:center;
  background:linear-gradient(135deg,rgba(255,78,205,0.12),rgba(168,85,247,0.08));
  border:1px solid var(--border);border-radius:var(--radius-md);color:var(--pink);transition:all var(--t)}
.tool-row:hover .icon{background:var(--grad-1);border-color:transparent;color:#fff;
  box-shadow:0 0 20px rgba(255,78,205,0.5)}
.tool-row .icon svg{width:20px;height:20px}
.tool-row .info h3{font-family:var(--font-display);font-size:1rem;font-weight:600;margin-bottom:3px;color:var(--ink)}
.tool-row .info p{font-size:0.82rem;color:var(--ink-3);line-height:1.5;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.tool-row .tag{font-family:var(--font-mono);font-size:0.68rem;font-weight:600;text-transform:uppercase;
  letter-spacing:0.06em;padding:5px 12px;border-radius:var(--radius-full);
  background:rgba(34,211,238,0.12);color:var(--cyan);border:1px solid rgba(34,211,238,0.2);white-space:nowrap}
.tool-row .arrow{font-size:1.1rem;color:var(--ink-3);transition:all var(--t)}
.tool-row:hover .arrow{color:var(--pink);transform:translateX(4px)}
.empty-note{text-align:center;padding:60px 20px;color:var(--ink-3)}

/* ============ TOOL PANEL ============ */
.tool-panel{background:var(--surface);backdrop-filter:blur(24px);border:1px solid var(--border);
  border-radius:var(--radius-lg);padding:32px;box-shadow:0 12px 40px rgba(0,0,0,0.3);
  margin-bottom:40px;position:relative;overflow:hidden}
.tool-panel::before{content:'';position:absolute;top:0;left:24px;right:24px;height:2px;
  background:var(--grad-1);border-radius:2px;opacity:0.85;transform:scaleX(0);transform-origin:left;
  transition:transform 0.4s ease}
.tool-panel:hover::before{transform:scaleX(1)}
.back-btn{display:inline-flex;align-items:center;gap:6px;font-size:0.82rem;font-weight:500;
  color:var(--ink-2);padding:8px 14px;border-radius:var(--radius-full);background:var(--surface-2);
  border:1px solid var(--border);transition:all var(--t);margin-bottom:22px;position:relative;z-index:1}
.back-btn:hover{color:var(--pink);border-color:var(--pink);transform:translateX(-2px)}
.panel-art{position:absolute;top:24px;right:28px;width:110px;height:110px;opacity:0.08;
  pointer-events:none;color:var(--pink)}
.panel-head{display:flex;gap:18px;align-items:flex-start;margin-bottom:28px;position:relative;z-index:1}
.panel-icon{width:52px;height:52px;display:flex;align-items:center;justify-content:center;
  background:var(--grad-1);border-radius:var(--radius-md);color:#fff;flex-shrink:0;
  box-shadow:0 0 30px rgba(168,85,247,0.4)}
.panel-icon svg{width:26px;height:26px}
.panel-head h2{font-family:var(--font-display);font-size:1.55rem;font-weight:700;
  letter-spacing:-0.02em;margin-bottom:4px;line-height:1.2}
.panel-head p{font-size:0.88rem;color:var(--ink-2);line-height:1.55}
.panel-body{position:relative;z-index:1}

/* ============ FIELDS / BUTTONS / MISC ============ */
.field{margin-bottom:20px}
.field label{display:block;font-family:var(--font-display);font-size:0.82rem;font-weight:600;
  color:var(--ink-2);margin-bottom:8px}
.field input[type="text"],.field input[type="number"],.field input[type="date"],
.field select,.field textarea{width:100%;padding:13px 18px;border:1px solid var(--border-2);
  border-radius:var(--radius-md);background:var(--surface-2);font-size:0.9rem;color:var(--ink);
  transition:all var(--t);-webkit-appearance:none;appearance:none}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--pink);
  background:var(--surface-3);box-shadow:0 0 0 4px rgba(255,78,205,0.12),0 0 20px rgba(255,78,205,0.15)}
.field textarea{min-height:150px;resize:vertical;line-height:1.65;font-family:inherit}
.row3{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.row2{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
.btn-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:6px;padding:12px 24px;
  border:none;border-radius:var(--radius-md);background:var(--grad-1);color:#fff;
  font-family:var(--font-display);font-size:0.86rem;font-weight:600;cursor:pointer;
  transition:all var(--t);box-shadow:0 4px 20px rgba(168,85,247,0.4);white-space:nowrap;
  position:relative;overflow:hidden}
.btn:hover{transform:translateY(-2px);box-shadow:0 8px 30px rgba(168,85,247,0.55);filter:brightness(1.1)}
.btn.secondary{background:var(--surface-2);color:var(--ink);border:1px solid var(--border-2);box-shadow:none}
.btn.secondary:hover{background:var(--surface-3);border-color:var(--pink);color:var(--pink)}
.btn:disabled{opacity:0.4;cursor:not-allowed;transform:none;box-shadow:none}
.stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-top:20px}
.stat{background:var(--surface-2);border:1px solid var(--border);border-radius:var(--radius-md);
  padding:20px 16px;text-align:center;transition:all var(--t)}
.stat:hover{border-color:rgba(255,78,205,0.4);transform:translateY(-2px)}
.stat .n{font-family:var(--font-display);font-size:1.75rem;font-weight:700;
  background:var(--grad-1);-webkit-background-clip:text;background-clip:text;
  -webkit-text-fill-color:transparent;line-height:1.1;margin-bottom:6px}
.stat .l{font-size:0.72rem;font-weight:500;color:var(--ink-3);text-transform:uppercase;letter-spacing:0.06em}
.result-box{background:var(--surface-2);border:1px solid rgba(168,85,247,0.35);
  border-radius:var(--radius-md);padding:20px 24px;margin-top:20px;font-size:0.9rem;
  color:var(--ink-2);line-height:1.55;position:relative;overflow:hidden}
.result-box::before{content:'';position:absolute;top:0;left:0;width:100%;height:2px;background:var(--grad-1)}
.result-box .big{font-family:var(--font-display);font-size:1.6rem;font-weight:700;
  background:var(--grad-1);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.mono-out{background:var(--surface-2);border:1px solid var(--border);border-radius:var(--radius-md);
  padding:18px;font-family:var(--font-mono);font-size:0.82rem;line-height:1.65;color:var(--ink-2);
  white-space:pre-wrap;word-break:break-word;overflow-x:auto;max-height:420px;overflow-y:auto;margin-top:16px}
.slider-row{display:flex;align-items:center;gap:14px}
.slider-row input[type="range"]{flex:1;height:6px;border-radius:3px;background:var(--surface-3);
  accent-color:var(--pink);cursor:pointer}
.slider-row .val{font-family:var(--font-mono);font-size:0.85rem;font-weight:600;color:var(--pink);min-width:44px;text-align:right}
.checks{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.checks label{display:flex;align-items:center;gap:8px;font-size:0.82rem;color:var(--ink-2);
  cursor:pointer;padding:9px 16px;border:1px solid var(--border-2);border-radius:var(--radius-full);
  background:var(--surface-2);transition:all var(--t)}
.checks label:hover{border-color:var(--lime);color:var(--lime)}
.checks input[type="checkbox"]{accent-color:var(--lime);width:16px;height:16px}
.drop-zone{border:2px dashed var(--border-2);border-radius:var(--radius-lg);padding:52px 24px;
  text-align:center;font-size:0.9rem;color:var(--ink-3);cursor:pointer;transition:all var(--t);
  background:var(--surface);margin-bottom:18px}
.drop-zone:hover,.drop-zone.drag{border-color:var(--pink);background:var(--surface-2);color:var(--pink);
  box-shadow:0 0 40px rgba(255,78,205,0.15)}
.drop-zone svg{width:42px;height:42px;margin:0 auto 14px;color:var(--pink);opacity:0.8}
.subject-rows{display:flex;flex-direction:column;gap:10px}
.subject-row{display:grid;grid-template-columns:1.5fr 1fr 1fr auto;gap:10px;align-items:center}
.subject-row input{padding:11px 14px;border:1px solid var(--border-2);border-radius:var(--radius-sm);
  background:var(--surface-2);font-size:0.85rem;transition:all var(--t)}
.subject-row input:focus{outline:none;border-color:var(--pink);box-shadow:0 0 0 4px rgba(255,78,205,0.12)}
.remove-row{background:none;border:1px solid var(--border-2);color:var(--ink-3);
  border-radius:var(--radius-sm);padding:9px 14px;font-size:0.75rem;cursor:pointer;transition:all var(--t)}
.remove-row:hover{border-color:#dc2626;color:#dc2626}
.img-compare{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:18px}
.img-compare figure{margin:0;border-radius:var(--radius-md);overflow:hidden;
  border:1px solid var(--border);background:var(--surface-2)}
.img-compare img{width:100%;height:auto}
.img-compare figcaption{padding:12px 16px;font-size:0.78rem;color:var(--ink-3);
  text-align:center;border-top:1px solid var(--border)}

/* ============ PROSE / SEO / FAQ ============ */
.prose{max-width:760px;margin:0 auto}
.prose h2{font-family:var(--font-display);font-size:1.9rem;font-weight:700;letter-spacing:-0.02em;
  margin-bottom:10px;line-height:1.15}
.prose h3{font-family:var(--font-display);font-size:1.15rem;font-weight:600;margin:32px 0 12px}
.prose h4{font-family:var(--font-display);font-size:0.98rem;font-weight:600;margin:24px 0 10px;color:var(--pink)}
.prose p{font-size:0.92rem;color:var(--ink-2);line-height:1.75;margin-bottom:14px}
.prose ul,.prose ol{padding-left:22px;margin-bottom:16px}
.prose li{font-size:0.9rem;color:var(--ink-2);line-height:1.7;margin-bottom:8px}
.prose code{font-family:var(--font-mono);font-size:0.82em;background:rgba(255,78,205,0.12);
  color:var(--pink);padding:2px 7px;border-radius:6px}
.updated{font-size:0.82rem;color:var(--ink-3);margin-bottom:26px;font-style:italic}
.how-to{margin-top:26px;padding:20px 24px;background:var(--surface-2);border:1px solid var(--border);
  border-radius:var(--radius-md);border-left:3px solid var(--pink)}
.how-to h3{font-family:var(--font-display);font-size:0.92rem;font-weight:600;margin-bottom:8px}
.how-to p{font-size:0.84rem;color:var(--ink-3);line-height:1.65;margin:0}
.seo-guide-content{margin-top:56px;padding-top:36px;border-top:1px solid var(--border)}
.seo-guide-content h2{font-family:var(--font-display);font-size:1.5rem;font-weight:700;
  letter-spacing:-0.02em;margin-bottom:14px}
.seo-guide-content h3{font-family:var(--font-display);font-size:1.05rem;font-weight:600;margin:28px 0 12px}
.seo-guide-content p,.seo-guide-content li{font-size:0.9rem;color:var(--ink-2);line-height:1.75}
.seo-guide-content ul{padding-left:22px;margin:12px 0}
.seo-guide-content blockquote{background:var(--surface-2);border-left:3px solid var(--pink);
  padding:18px 22px;margin:18px 0;border-radius:0 var(--radius-md) var(--radius-md) 0;
  font-size:0.9rem;color:var(--ink-2);line-height:1.65}
.seo-guide-content details{margin-bottom:10px;border:1px solid var(--border);
  border-radius:var(--radius-md);background:var(--surface);overflow:hidden;transition:all var(--t)}
.seo-guide-content details[open]{border-color:rgba(255,78,205,0.35);background:var(--surface-2)}
.seo-guide-content summary{padding:16px 20px;font-family:var(--font-display);font-size:0.88rem;
  font-weight:600;color:var(--ink);cursor:pointer;list-style:none;display:flex;
  align-items:center;justify-content:space-between;transition:background var(--t)}
.seo-guide-content summary::-webkit-details-marker{display:none}
.seo-guide-content summary::after{content:'+';font-size:1.3rem;color:var(--pink);font-weight:400;
  width:28px;height:28px;display:flex;align-items:center;justify-content:center;
  border-radius:50%;background:rgba(255,78,205,0.12);transition:all 0.25s}
.seo-guide-content details[open] summary::after{content:'−';background:var(--grad-1);color:#fff;
  transform:rotate(180deg)}
.seo-guide-content details p{padding:0 20px 16px;font-size:0.86rem;color:var(--ink-3);line-height:1.7;margin:0}
.seo-guide-content table{width:100%;border-collapse:collapse;margin:18px 0;font-size:0.86rem;
  border-radius:var(--radius-md);overflow:hidden;border:1px solid var(--border)}
.seo-guide-content th{background:var(--surface-2);color:var(--pink);font-family:var(--font-display);
  font-weight:600;text-align:left;padding:12px 16px;border-bottom:1px solid var(--border)}
.seo-guide-content td{padding:11px 16px;border-bottom:1px solid var(--border);color:var(--ink-2)}
footer{margin-top:64px;padding:32px 0;border-top:1px solid var(--border);display:flex;
  flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;
  font-size:0.82rem;color:var(--ink-3)}
.footer-links{display:flex;flex-wrap:wrap;gap:20px}
.footer-links a{color:var(--ink-3);font-weight:500;transition:color var(--t)}
.footer-links a:hover{color:var(--pink)}
.ok{color:var(--mint);font-weight:600}
.err{color:#FB7185;font-weight:600}
.char-left{font-weight:400;color:var(--ink-3);font-size:0.75rem}
@media (max-width:768px){
  .wrap{padding:0 16px}.tool-panel{padding:22px}.panel-head h2{font-size:1.25rem}
  .row3,.row2{grid-template-columns:1fr}.img-compare{grid-template-columns:1fr}
  .tool-row{grid-template-columns:32px 40px 1fr 28px;gap:10px;padding:14px}
  .tool-row .tag{display:none}.tool-row .info p{-webkit-line-clamp:1}
  .stat-grid{grid-template-columns:repeat(2,1fr)}.brand h1{font-size:1.45rem}
  .hero-illus{width:44px;height:44px}.hero-title{font-size:1.5rem}}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:0.01ms !important;transition-duration:0.01ms !important}}
"""
(ROOT / "assets" / "style.css").write_text(NEW_CSS, encoding="utf-8")
print("✅ assets/style.css updated")

# ============ 2. NEW INDEX.HTML ============
NEW_INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="google-site-verification" content="Ly7kZPsyUOovYPRZgQrzFI62Y_VjLqnDi1i1h6cpHR0" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ToolCrate — 15+ Free Browser Tools. No Signup. Nothing Leaves Your Device.</title>
<meta name="description" content="Free online tools that run entirely in your browser — word counter, QR generator, image compressor, JSON formatter, PDF tools, watermark, CGPA calculator and more. No signup, no uploads, no file limits.">
<link rel="canonical" href="https://site.toolcrate-tools.workers.dev/">
<meta name="theme-color" content="#070B10">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H20HJWJQWV"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-H20HJWJQWV');</script>
</head>
<body>
<div class="wrap">
<header class="masthead">
<div class="row">
<div class="brand-block">
<div class="hero-illus" aria-hidden="true">
<svg viewBox="0 0 120 120" fill="none"><defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FF4ECD"/><stop offset="50%" stop-color="#A855F7"/><stop offset="100%" stop-color="#22D3EE"/></linearGradient></defs>
<circle cx="60" cy="60" r="58" stroke="url(#g1)" stroke-width="1" opacity="0.35"/>
<g stroke="url(#g1)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
<path d="M40 78 L74 44a8 8 0 0 0 0-11.3l-1.7-1.7a8 8 0 0 0-11.3 0L27 65"/><circle cx="33" cy="72" r="7"/></g></svg>
</div>
<div>
<div class="brand"><h1>ToolCrate</h1></div>
<p class="tagline">15+ free tools that run entirely in your browser. Nothing leaves your device.</p>
</div>
</div>
<button class="theme-toggle" id="themeToggle" type="button">☀️ Light</button>
</div>

<div class="badge-row">
<span class="badge pink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 4 6v6c0 5 3.5 8.5 8 10 4.5-1.5 8-5 8-10V6z"/></svg>Nothing uploaded</span>
<span class="badge violet"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>Private by design</span>
<span class="badge cyan"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg>No signup, no waiting</span>
<span class="badge lime"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3 2 8l10 5 10-5-10-5Z"/></svg>No file-size traps</span>
</div>

<h1 class="hero-title">15+ free tools that run <span class="grad-word">entirely in your browser</span></h1>
<p class="hero-sub">Word counter, QR generator, PDF tools, image compressor, JSON formatter, watermark, CGPA calculator and more — all local, fast, and completely private.</p>

<div class="search-row">
<input id="toolSearch" type="text" placeholder="🔍  Search a tool — word counter, QR code, PDF, watermark…" autocomplete="off">
</div>
</header>

<main>
<nav class="category-rail" id="categoryRail">
<button class="chip active" data-cat="all">✨ All tools</button>
<button class="chip" data-cat="text">📝 Text</button>
<button class="chip" data-cat="image">🖼️ Image</button>
<button class="chip" data-cat="numbers">🔢 Numbers</button>
<button class="chip" data-cat="dev">⚙️ Dev</button>
<button class="chip" data-cat="seo">🔎 SEO</button>
</nav>

<section class="tool-list" id="toolList">
<a class="tool-row" data-cat="text" data-name="word character counter" data-desc="count words characters sentences" href="word-counter.html"><div class="idx">01</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h10M4 18h7"/></svg></div><div class="info"><h3>Word & Character Counter</h3><p>Count words, characters, sentences, paragraphs and reading time as you type.</p></div><div class="tag">text</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="text" data-name="case converter" data-desc="uppercase lowercase title" href="case-converter.html"><div class="idx">02</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 6h16M4 12h10M4 18h7"/></svg></div><div class="info"><h3>Case Converter</h3><p>Switch text between UPPERCASE, lowercase, Title Case and Sentence case.</p></div><div class="tag">text</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="numbers" data-name="unit converter" data-desc="length weight temperature" href="unit-converter.html"><div class="idx">03</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="1"/><path d="M8 9h8M8 13h5M8 17h8"/></svg></div><div class="info"><h3>Unit Converter</h3><p>Convert length, weight, temperature and volume between common units.</p></div><div class="tag">numbers</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="dev" data-name="qr code generator" data-desc="link text qr code" href="qr-generator.html"><div class="idx">04</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 8l-4 4 4 4M16 8l4 4-4 4"/></svg></div><div class="info"><h3>QR Code Generator</h3><p>Turn any link or text into a downloadable QR code. Generated locally.</p></div><div class="tag">dev</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="dev" data-name="password generator" data-desc="strong random password" href="password-generator.html"><div class="idx">05</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 8l-4 4 4 4M16 8l4 4-4 4"/></svg></div><div class="info"><h3>Password Generator</h3><p>Create strong random passwords. Generated on your device.</p></div><div class="tag">dev</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="image" data-name="image compressor" data-desc="shrink photo size" href="image-compressor.html"><div class="idx">06</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="1"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-4 4-3-3-6 6"/></svg></div><div class="info"><h3>Image Compressor</h3><p>Shrink photo file sizes. Batch and folder upload supported.</p></div><div class="tag">image</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="dev" data-name="json formatter validator" data-desc="pretty print json" href="json-formatter.html"><div class="idx">07</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 8l-4 4 4 4M16 8l4 4-4 4"/></svg></div><div class="info"><h3>JSON Formatter</h3><p>Paste JSON to pretty-print, validate or minify.</p></div><div class="tag">dev</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="numbers" data-name="age calculator" data-desc="exact age years months" href="age-calculator.html"><div class="idx">08</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="1"/><path d="M8 9h8M8 13h5M8 17h8"/></svg></div><div class="info"><h3>Age Calculator</h3><p>Find exact age in years, months and days from a date of birth.</p></div><div class="tag">numbers</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="numbers" data-name="discount tax calculator" data-desc="sale price savings" href="discount-calculator.html"><div class="idx">09</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="1"/><path d="M8 9h8M8 13h5M8 17h8"/></svg></div><div class="info"><h3>Discount & Tax Calculator</h3><p>Work out final price after a discount and tax.</p></div><div class="tag">numbers</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="numbers" data-name="percentage aggregate calculator" data-desc="marks percentage" href="aggregate-calculator.html"><div class="idx">10</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="1"/><path d="M8 9h8M8 13h5M8 17h8"/></svg></div><div class="info"><h3>Percentage Calculator</h3><p>Add each subject's marks to get your overall percentage.</p></div><div class="tag">numbers</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="seo" data-name="meta tag generator" data-desc="seo meta tags" href="meta-tag-generator.html"><div class="idx">11</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="10" cy="10" r="6"/><path d="M20 20l-5.5-5.5"/></svg></div><div class="info"><h3>Meta Tag Generator</h3><p>Generate SEO-ready meta tags with Open Graph support.</p></div><div class="tag">seo</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="numbers" data-name="cgpa gpa calculator" data-desc="semester gpa cgpa" href="cgpa-calculator.html"><div class="idx">12</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/></svg></div><div class="info"><h3>CGPA & GPA Calculator</h3><p>Extract semester GPA from result card, plan target CGPA.</p></div><div class="tag">numbers</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="numbers" data-name="currency converter" data-desc="live exchange rates" href="currency-converter.html"><div class="idx">13</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 1l4 4-4 4M3 11V9a4 4 0 0 1 4-4h14M7 23l-4-4 4-4M21 13v2a4 4 0 0 1-4 4H3"/></svg></div><div class="info"><h3>Currency Converter</h3><p>Convert real-time exchange rates across 150+ currencies.</p></div><div class="tag">numbers</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="image" data-name="image to pdf" data-desc="images to pdf folder" href="image-to-pdf.html"><div class="idx">14</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/></svg></div><div class="info"><h3>Image to PDF</h3><p>Convert images to a single PDF. Folder upload, no page limit.</p></div><div class="tag">image</div><div class="arrow">→</div></a>
<a class="tool-row" data-cat="image" data-name="watermark tool" data-desc="text logo watermark" href="watermark-tool.html"><div class="idx">15</div><div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg></div><div class="info"><h3>Watermark Tool</h3><p>Add text watermarks to images and PDFs. Batch with folder upload.</p></div><div class="tag">image</div><div class="arrow">→</div></a>
<div class="empty-note" id="emptyNote" style="display:none;">No tools match that search.</div>
</section>
</main>
<footer><span>ToolCrate — built for people, not ads.</span>
<nav class="footer-links"><a href="index.html">All tools</a><a href="about.html">About</a><a href="contact.html">Contact</a><a href="privacy.html">Privacy Policy</a></nav></footer>
</div>
<script src="assets/common.js"></script>
<script>
(function(){
  var rows=Array.prototype.slice.call(document.querySelectorAll('.tool-row'));
  var emptyNote=document.getElementById('emptyNote');
  var currentCat='all',currentQuery='';
  rows.forEach(function(r,i){r.style.animationDelay=(Math.min(i,12)*0.035)+'s';});
  function applyFilter(){
    var q=currentQuery.trim().toLowerCase();var anyVisible=false;
    rows.forEach(function(row){
      var cat=row.getAttribute('data-cat');var name=row.getAttribute('data-name');var desc=row.getAttribute('data-desc');
      var catOk=currentCat==='all'||cat===currentCat;
      var qOk=!q||name.indexOf(q)>-1||desc.indexOf(q)>-1;
      var show=catOk&&qOk;row.style.display=show?'':'none';if(show)anyVisible=true;
    });
    emptyNote.style.display=anyVisible?'none':'block';
  }
  document.getElementById('categoryRail').addEventListener('click',function(e){
    var btn=e.target.closest('.chip');if(!btn)return;
    document.querySelectorAll('.chip').forEach(function(c){c.classList.remove('active');});
    btn.classList.add('active');currentCat=btn.getAttribute('data-cat');applyFilter();
  });
  document.getElementById('toolSearch').addEventListener('input',function(e){currentQuery=e.target.value;applyFilter();});
})();
</script>
</body>
</html>
"""
(ROOT / "index.html").write_text(NEW_INDEX, encoding="utf-8")
print("✅ index.html updated")

# ============ 3. UPDATE ABOUT / CONTACT / PRIVACY WITH COLORFUL HERO ============
FONT_LINK = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">'

GTAG = '<script async src="https://www.googletagmanager.com/gtag/js?id=G-H20HJWJQWV"></script>\n<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-H20HJWJQWV");</script>'

FOOTER = '<footer><span>ToolCrate — built for people, not ads.</span>\n<nav class="footer-links"><a href="index.html">All tools</a><a href="about.html">About</a><a href="contact.html">Contact</a><a href="privacy.html">Privacy Policy</a></nav></footer>'

def build_page(title, desc, canonical, badges_html, hero_title, hero_sub, body):
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8">
<meta name="google-site-verification" content="Ly7kZPsyUOovYPRZgQrzFI62Y_VjLqnDi1i1h6cpHR0" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#070B10">
{FONT_LINK}
<link rel="stylesheet" href="assets/style.css">
{GTAG}
</head><body>
<div class="wrap">
<header class="masthead">
<div class="row">
<div class="brand-block">
<div><div class="brand"><h1><a href="index.html">ToolCrate</a></h1></div></div>
</div>
<button class="theme-toggle" id="themeToggle" type="button">☀️ Light</button>
</div>
<div class="badge-row">{badges_html}</div>
<h1 class="hero-title">{hero_title}</h1>
<p class="hero-sub">{hero_sub}</p>
</header>
<main>
{body}
</main>
{FOOTER}
</div>
<script src="assets/common.js"></script>
</body></html>
'''

# About
about_body = '''<div class="prose">
<a class="back-btn" href="index.html">← Back to all tools</a>
<h2>About ToolCrate</h2>
<p class="updated">Last updated: 2026</p>
<p>ToolCrate is a free collection of everyday tools — word counter, case converter, unit converter, QR code generator, password generator, image compressor, JSON formatter, age calculator, CGPA calculator, currency converter, PDF tools, watermark tool and more.</p>
<p>Most "free" tool sites make you wait through ads, create an account, or upload your file to a server. ToolCrate doesn't. Every tool runs entirely as JavaScript in your browser — nothing you type or upload is ever sent anywhere.</p>
<h3>Why we built it</h3>
<p>One place with the small utilities people reach for constantly — without friction. No login walls, no file-size limits, no PDF page caps.</p>
<h3>How it's funded</h3>
<p>ToolCrate is free with no ads. As the site grows we may run clearly-labelled advertising to cover hosting costs — we'll never sell or share what you type into a tool.</p>
<h3>Top SEO Resources We Recommend</h3>
<h4>Research & Competitor Analysis</h4>
<ul>
<li><strong><a href="https://ahrefs.com" target="_blank" rel="noopener">Ahrefs</a></strong> — Backlink analysis, keyword research, competitor gap analysis.</li>
<li><strong><a href="https://semrush.com" target="_blank" rel="noopener">SEMrush</a></strong> — All-in-one SEO toolkit with keyword magic and audits.</li>
<li><strong><a href="https://moz.com" target="_blank" rel="noopener">Moz Pro</a></strong> — Keyword research, link analysis, MozBar extension.</li>
<li><strong><a href="https://www.similarweb.com" target="_blank" rel="noopener">Similarweb</a></strong> — Competitive market intelligence and traffic analysis.</li>
</ul>
<h4>Google Visibility & Analytics</h4>
<ul>
<li><strong><a href="https://search.google.com/search-console" target="_blank" rel="noopener">Google Search Console</a></strong> — Rank tracking, index coverage, crawl diagnostics.</li>
<li><strong><a href="https://analytics.google.com" target="_blank" rel="noopener">Google Analytics 4</a></strong> — Track SEO performance and user behaviour.</li>
<li><strong><a href="https://pagespeed.web.dev" target="_blank" rel="noopener">PageSpeed Insights</a></strong> — Core Web Vitals and performance.</li>
</ul>
<h4>Technical SEO & Audits</h4>
<ul>
<li><strong><a href="https://www.screamingfrog.co.uk/seo-spider/" target="_blank" rel="noopener">Screaming Frog SEO Spider</a></strong> — Crawl your site to detect technical issues.</li>
<li><strong><a href="https://sitebulb.com" target="_blank" rel="noopener">Sitebulb</a></strong> — Visual technical SEO auditing.</li>
<li><strong><a href="https://www.clearscope.io" target="_blank" rel="noopener">Clearscope</a></strong> — Content optimization tool.</li>
</ul>
<h3>Get in touch</h3>
<p>Questions, bug reports, or a tool you'd like to see added? Visit the <a href="contact.html">Contact page</a>.</p>
</div>'''

about_badges = '<span class="badge pink">🌿 Built for people</span><span class="badge violet">🔒 Nothing uploaded</span><span class="badge cyan">🌍 Free forever</span>'
(ROOT / "about.html").write_text(build_page(
    "About ToolCrate — Free Browser Tools & Top SEO Resources",
    "ToolCrate is a free collection of browser-based tools. Plus curated top SEO resources: Ahrefs, SEMrush, Moz, Google Search Console, Screaming Frog.",
    "https://site.toolcrate-tools.workers.dev/about.html",
    about_badges,
    "A free toolbox for <span class='grad-word'>everyday work</span>",
    "Built for photographers, students, developers and anyone who needs a quick tool without the friction of uploads, logins or ads.",
    about_body
), encoding="utf-8")
print("✅ about.html updated")

# Contact
contact_body = '''<div class="prose">
<a class="back-btn" href="index.html">← Back to all tools</a>
<h2>Contact</h2>
<p class="updated">We read every message.</p>
<p>Have a question, found a bug, or want to suggest a tool for ToolCrate? Reach out any time.</p>
<h3>Email</h3>
<p>Email us at <a href="mailto:hello@toolcrate.netlify.app">hello@toolcrate.netlify.app</a> and we'll get back to you as soon as we can.</p>
<h3>GitHub</h3>
<p>ToolCrate is open on GitHub. Open an issue or see how it's built at <a href="https://github.com/Rehman8207/toolcrate" target="_blank" rel="noopener">github.com/Rehman8207/toolcrate</a>.</p>
</div>'''

contact_badges = '<span class="badge pink">💬 Fast replies</span><span class="badge violet">🐛 Bug reports welcome</span><span class="badge cyan">💡 Tool ideas</span>'
(ROOT / "contact.html").write_text(build_page(
    "Contact ToolCrate — Get in Touch",
    "Get in touch with the ToolCrate team — questions, bug reports, or suggestions for new tools.",
    "https://site.toolcrate-tools.workers.dev/contact.html",
    contact_badges,
    "Say hello — <span class='grad-word'>we reply</span>",
    "Questions, bug reports, or a tool idea? Reach out any time — we read every message.",
    contact_body
), encoding="utf-8")
print("✅ contact.html updated")

# Privacy
privacy_body = '''<div class="prose">
<a class="back-btn" href="index.html">← Back to all tools</a>
<h2>Privacy Policy</h2>
<p class="updated">Last updated: 2026</p>
<p>This Privacy Policy explains what information ToolCrate collects and how it is used. ToolCrate is designed around a simple principle: your content stays on your device.</p>
<h3>What we do NOT collect</h3>
<ul>
<li>Anything you type, paste, or upload into a tool is processed entirely in your browser using JavaScript. It is never uploaded to, or stored on, any ToolCrate server.</li>
<li>We do not require accounts, so we do not collect names, emails, or passwords to use any tool.</li>
</ul>
<h3>What we may collect</h3>
<ul>
<li><strong>Local storage:</strong> your light/dark theme preference is saved in your browser's local storage (key <code>toolcrate-theme</code>).</li>
<li><strong>Basic analytics/hosting logs:</strong> our hosting provider may log standard technical data such as IP address, browser type, and pages visited, used only in aggregate.</li>
<li><strong>Advertising:</strong> if ToolCrate displays ads through Google AdSense, Google may use cookies to serve relevant ads. You can opt out at <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">google.com/settings/ads</a>.</li>
</ul>
<h3>Third-party services</h3>
<p>ToolCrate loads fonts from Google Fonts and some tools load open-source libraries from public CDNs. These services may see that your browser requested a file, but do not receive the content you enter.</p>
<h3>Contact</h3>
<p>Questions? Reach out via the <a href="contact.html">Contact page</a>.</p>
</div>'''

privacy_badges = '<span class="badge pink">🔒 No tracking</span><span class="badge violet">🌿 Local processing</span><span class="badge cyan">📄 Transparent</span>'
(ROOT / "privacy.html").write_text(build_page(
    "Privacy Policy — ToolCrate",
    "ToolCrate privacy policy. Every tool runs locally in your browser — we do not collect, store, or transmit your content.",
    "https://site.toolcrate-tools.workers.dev/privacy.html",
    privacy_badges,
    "Your data <span class='grad-word'>stays yours</span>",
    "Every tool runs locally. Your files, text and images never leave your browser.",
    privacy_body
), encoding="utf-8")
print("✅ privacy.html updated")

# ============ 4. UPDATE ALL TOOL PAGES — add colorful hero ============
TOOL_PAGES = {
    "word-counter.html": ("Word & Character Counter", "Count words, characters and reading time as you type.", "Count words and characters", "text", "01"),
    "case-converter.html": ("Case Converter", "Switch between UPPERCASE, lowercase, Title Case and Sentence case.", "Convert text case", "text", "02"),
    "unit-converter.html": ("Unit Converter", "Convert length, weight, temperature and volume.", "Convert any unit", "numbers", "03"),
    "qr-generator.html": ("QR Code Generator", "Turn any link or text into a downloadable QR code.", "Generate QR codes", "dev", "04"),
    "password-generator.html": ("Password Generator", "Create strong random passwords on your device.", "Generate strong passwords", "dev", "05"),
    "image-compressor.html": ("Image Compressor", "Shrink photo sizes locally — nothing is uploaded.", "Compress images", "image", "06"),
    "json-formatter.html": ("JSON Formatter & Validator", "Pretty-print, validate or minify JSON.", "Format JSON", "dev", "07"),
    "age-calculator.html": ("Age Calculator", "Find exact age in years, months and days.", "Calculate exact age", "numbers", "08"),
    "discount-calculator.html": ("Discount & Tax Calculator", "Work out final price after discount and tax.", "Calculate discounts", "numbers", "09"),
    "aggregate-calculator.html": ("Percentage & Aggregate Calculator", "Add marks across subjects to get your overall percentage.", "Calculate percentage", "numbers", "10"),
    "meta-tag-generator.html": ("Meta Tag Generator", "Generate SEO meta tags with OG and Twitter Cards.", "Generate SEO tags", "seo", "11"),
    "cgpa-calculator.html": ("CGPA & GPA Calculator", "Extract semester GPA, plan target CGPA.", "Calculate CGPA", "numbers", "12"),
    "currency-converter.html": ("Live Currency Converter", "Convert real-time exchange rates for 150+ currencies.", "Convert currencies", "numbers", "13"),
    "image-to-pdf.html": ("Image to PDF Converter", "Convert images to PDF with folder upload, no page limit.", "Convert images to PDF", "image", "14"),
    "watermark-tool.html": ("Watermark Tool", "Add text watermarks to images and PDFs. Batch upload.", "Watermark your files", "image", "15"),
}

# regex to match the whole masthead block on tool pages (allows for whitespace)
MASTHEAD_RE = re.compile(r'<header class="masthead">.*?</header>', re.DOTALL)

for page, (title, sub, hero_t, cat, num) in TOOL_PAGES.items():
    fp = ROOT / page
    if not fp.exists():
        print(f"   ⚠️  {page} — not found, skipping")
        continue
    text = fp.read_text(encoding="utf-8")

    colorful_hero = f'''<header class="masthead">
<div class="row">
<div class="brand-block">
<div><div class="brand"><h1><a href="index.html">ToolCrate</a></h1></div></div>
</div>
<button class="theme-toggle" id="themeToggle" type="button">☀️ Light</button>
</div>
<div class="badge-row">
<span class="badge pink"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 4 6v6c0 5 3.5 8.5 8 10 4.5-1.5 8-5 8-10V6z"/></svg>Nothing uploaded</span>
<span class="badge violet"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>Private by design</span>
<span class="badge cyan"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M2 12h20"/></svg>100% free</span>
</div>
<h1 class="hero-title">{hero_t} <span class="grad-word">right in your browser</span></h1>
<p class="hero-sub">{sub}</p>
</header>'''

    new_text, n = MASTHEAD_RE.subn(colorful_hero, text, count=1)
    if n:
        fp.write_text(new_text, encoding="utf-8")
        print(f"   ✅ {page}")
    else:
        print(f"   ⚠️  {page} — masthead pattern not found (skipped)")

print()
print("=" * 55)
print("🎉 ALL DONE! Colorful design applied everywhere.")
print("=" * 55)
print()
print("Next steps:")
print("  1. Test locally: open index.html in browser")
print("  2. Push:")
print("     git add .")
print("     git commit -m 'Colorful aurora theme on all pages'")
print("     git push")
print()
input("Press Enter to close...")