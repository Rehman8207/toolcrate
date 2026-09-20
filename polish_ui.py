#!/usr/bin/env python3
"""
1. Replace emoji chips with real SVG icons in index.html
2. Smooth hover transitions
3. Boxing effect on tool-list, category-rail, blog-grid
"""
import re
from pathlib import Path

ROOT = Path.cwd()
INDEX = ROOT / "index.html"
BLOG = ROOT / "blog" / "index.html"
CSS = ROOT / "assets" / "style.css"

# ============================================================
# SVG ICONS (16x16, inline)
# ============================================================
SVG = {
    'all':    '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
    'text':   '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M4 12h10M4 17h14"/></svg>',
    'image':  '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-4 4-3-3-6 6"/></svg>',
    'numbers':'<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 7h8M8 12h2M14 12h2M8 17h2M14 17h2"/></svg>',
    'dev':    '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 8l-4 4 4 4M16 8l4 4-4 4"/></svg>',
    'seo':    '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="10" r="6"/><path d="M20 20l-5.5-5.5"/></svg>',
    'blog':   '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5a2 2 0 0 1 2-2h12v18H6a2 2 0 0 1-2-2V5z"/><path d="M8 7h8M8 11h6"/></svg>',
}

# ============================================================
# NEW CSS — boxing + smooth hover
# ============================================================
NEW_CSS = """

/* ============================================================
   POLISH: Boxing effect + smooth hover + real icon chips
   ============================================================ */

/* ---------- SMOOTH GLOBAL TRANSITIONS ---------- */
*,
*::before,
*::after {
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

/* ---------- BOXED CONTAINERS ---------- */
.tool-list,
.blog-grid,
.category-rail {
  background: linear-gradient(180deg, rgba(255,255,255,0.025) 0%, rgba(255,255,255,0.008) 100%);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 20px;
  position: relative;
  box-shadow:
    0 1px 0 rgba(255,255,255,0.05) inset,
    0 20px 50px rgba(0,0,0,0.20);
}

[data-theme="light"] .tool-list,
[data-theme="light"] .blog-grid,
[data-theme="light"] .category-rail {
  background: #FFFFFF;
  border-color: rgba(15,42,32,0.08);
  box-shadow:
    0 1px 0 rgba(255,255,255,1) inset,
    0 20px 50px rgba(10,20,16,0.06);
}

.category-rail {
  padding: 14px 16px;
  margin-bottom: 22px;
  border-radius: 16px;
}

.tool-list {
  padding: 18px;
}

/* ---------- CHIPS: REAL ICONS + SMOOTH HOVER ---------- */
.chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 9px 18px;
  font-size: 0.84rem;
  font-weight: 500;
  line-height: 1;
  transition:
    background-color 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    color 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    box-shadow 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.chip svg {
  width: 14px;
  height: 14px;
  flex-shrink: 0;
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.chip:hover svg {
  transform: scale(1.15) rotate(-4deg);
}

.chip:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(16,185,129,0.18);
}

.chip.active {
  transform: translateY(-1px);
}

.chip.active svg {
  transform: none;
}

/* ---------- BLOG CHIP: match new icon style ---------- */
.chip-blog {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 9px 18px;
  margin-left: 10px;
  font-size: 0.84rem;
  font-weight: 600;
  border-radius: 999px;
  text-decoration: none;
  position: relative;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.chip-blog::before {
  content: '';
  position: absolute;
  left: -11px;
  top: 50%;
  transform: translateY(-50%);
  width: 1px;
  height: 22px;
  background: linear-gradient(180deg, transparent 0%, var(--border-2) 20%, var(--border-2) 80%, transparent 100%);
}

.chip-blog svg {
  width: 14px;
  height: 14px;
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.chip-blog:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(20,184,166,0.28);
}

.chip-blog:hover svg {
  transform: scale(1.15) rotate(-4deg);
}

/* ---------- TOOL CARDS: SMOOTHER HOVER IN/OUT ---------- */
.tool-row {
  transition:
    transform 0.4s cubic-bezier(0.34, 1.4, 0.64, 1),
    box-shadow 0.4s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.tool-row .icon-wrap .icon {
  transition:
    background 0.4s cubic-bezier(0.4, 0, 0.2, 1),
    transform 0.4s cubic-bezier(0.34, 1.4, 0.64, 1),
    box-shadow 0.4s cubic-bezier(0.4, 0, 0.2, 1),
    color 0.3s ease;
}

.tool-row .info h3 {
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

.tool-row .arrow {
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ---------- BUTTONS: SMOOTHER SHINE + HOVER ---------- */
.btn {
  transition:
    transform 0.35s cubic-bezier(0.34, 1.4, 0.64, 1),
    box-shadow 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    filter 0.3s ease;
}

/* ---------- BADGES: SMOOTH HOVER ---------- */
.badge {
  transition:
    transform 0.35s cubic-bezier(0.34, 1.4, 0.64, 1),
    box-shadow 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    color 0.35s ease;
}

/* ---------- FEATURE ITEMS: SMOOTH ---------- */
.feature-item {
  transition:
    transform 0.4s cubic-bezier(0.34, 1.4, 0.64, 1),
    box-shadow 0.4s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.35s ease,
    background-color 0.35s ease;
}

/* ---------- STATS: SMOOTH ---------- */
.stat {
  transition:
    transform 0.4s cubic-bezier(0.34, 1.4, 0.64, 1),
    box-shadow 0.4s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.35s ease,
    background-color 0.35s ease;
}

/* ---------- THEME TOGGLE: SMOOTH ---------- */
.theme-toggle {
  transition:
    transform 0.35s cubic-bezier(0.34, 1.4, 0.64, 1),
    box-shadow 0.35s cubic-bezier(0.4, 0, 0.2, 1),
    border-color 0.35s ease,
    color 0.35s ease;
}

/* ---------- SEARCH BAR: SMOOTH FOCUS ---------- */
#toolSearch {
  transition:
    border-color 0.35s ease,
    box-shadow 0.4s cubic-bezier(0.4, 0, 0.2, 1),
    background-color 0.35s ease;
}

/* ---------- REDUCED MOTION ---------- */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    transition-duration: 0.01ms !important;
    animation-duration: 0.01ms !important;
  }
}

/* ---------- MOBILE: tighter boxing ---------- */
@media (max-width: 640px) {
  .tool-list,
  .blog-grid {
    padding: 14px;
    border-radius: 16px;
  }
  .category-rail {
    padding: 12px 14px;
    border-radius: 14px;
  }
  .chip-blog {
    margin-left: 0;
  }
  .chip-blog::before {
    display: none;
  }
}
"""

# ============================================================
# Emoji → SVG replacement map
# ============================================================
EMOJI_REPLACE = {
    '✨': SVG['all'],
    '📝': SVG['text'],
    '🖼️': SVG['image'],
    '🔢': SVG['numbers'],
    '⚙️': SVG['dev'],
    '🔎': SVG['seo'],
    '📚': SVG['blog'],
}

# ============================================================
# Process index.html
# ============================================================
print("=" * 60)
print("Polishing UI: real icons + smooth hover + boxing")
print("=" * 60)

def process_file(fp):
    if not fp.exists():
        print(f"   [WARN] {fp.name} — not found")
        return False

    text = fp.read_text(encoding="utf-8")
    original = text

    # Replace emojis in category rail ONLY (between <nav class="category-rail"> and </nav>)
    rail_re = re.compile(
        r'(<nav class="category-rail"[^>]*>)(.*?)(</nav>)',
        re.DOTALL
    )

    def fix_rail(m):
        head = m.group(1)
        inner = m.group(2)
        tail = m.group(3)
        for emoji, svg in EMOJI_REPLACE.items():
            inner = inner.replace(emoji, svg)
        # Also handle emoji followed by space in Blog chip
        inner = inner.replace('  ', ' ')
        return head + inner + tail

    text = rail_re.sub(fix_rail, text, count=1)

    if text != original:
        fp.write_text(text, encoding="utf-8")
        print(f"   [OK] {fp.relative_to(ROOT)}")
        return True
    else:
        print(f"   [SKIP] {fp.relative_to(ROOT)} — no change")
        return False

process_file(INDEX)
process_file(BLOG)

# ============================================================
# Append CSS
# ============================================================
if CSS.exists():
    css = CSS.read_text(encoding="utf-8")
    if "POLISH: Boxing effect" not in css:
        css += NEW_CSS
        CSS.write_text(css, encoding="utf-8")
        print()
        print("[OK] assets/style.css — polish styles appended")
    else:
        print()
        print("[SKIP] assets/style.css — already polished")

print()
print("=" * 60)
print("[DONE] DONE!")
print("=" * 60)
print()
print("Test:")
print("  python -m http.server 8000")
print("  Open http://localhost:8000/")
print("  Ctrl + Shift + R")
print()
print("  If looks good:")
print("    git add .")
print("    git commit -m 'Real icons, smooth hover, boxing effect'")
print("    git push")
print()
input("Press Enter to close...")