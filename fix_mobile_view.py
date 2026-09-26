#!/usr/bin/env python3
"""
Fix mobile layout:
1. Tool cards: proper vertical stack on mobile
2. Install button: compact icon-only on mobile
3. Category chips: proper wrapping
"""
from pathlib import Path

ROOT = Path.cwd()
CSS = ROOT / "assets" / "style.css"

if not CSS.exists():
    print("ERROR: assets/style.css not found")
    input("Press Enter...")
    exit(1)

MOBILE_FIX = """

/* ============================================================
   MOBILE VIEW FIX — Tool cards, install button, chips
   ============================================================ */

/* ---------- INSTALL BUTTON — compact on mobile ---------- */
@media (max-width: 768px) {
  .install-app-btn {
    width: 40px !important;
    height: 40px !important;
    padding: 0 !important;
    margin-right: 6px !important;
    border-radius: 50% !important;
    flex-shrink: 0 !important;
  }
  .install-app-btn .install-text {
    display: none !important;
  }
  .install-app-btn svg {
    width: 18px !important;
    height: 18px !important;
    margin: 0 !important;
  }
}

/* On very small screens, even smaller */
@media (max-width: 380px) {
  .install-app-btn {
    width: 36px !important;
    height: 36px !important;
  }
}

/* ---------- HEADER ROW — proper flex on mobile ---------- */
@media (max-width: 768px) {
  .masthead .row {
    flex-wrap: nowrap !important;
    align-items: center !important;
    justify-content: space-between !important;
    gap: 8px !important;
  }
  .brand-block {
    flex: 1 1 auto !important;
    min-width: 0 !important;
  }
  .brand h1 {
    font-size: 1.35rem !important;
  }
  .theme-toggle {
    padding: 8px 12px !important;
    font-size: 0.75rem !important;
    flex-shrink: 0 !important;
  }
}

/* ---------- TOOL CARDS — proper vertical layout on mobile ---------- */
@media (max-width: 768px) {
  .tool-row {
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
    gap: 14px !important;
    padding: 18px !important;
    grid-template-columns: none !important;
  }

  /* Icon row at top */
  .tool-row .icon-wrap {
    display: inline-flex !important;
    align-items: center !important;
    gap: 10px !important;
    margin-bottom: 0 !important;
  }

  /* Info block below icon */
  .tool-row .info {
    width: 100% !important;
    grid-column: unset !important;
  }

  /* Title full width, no wrapping mid-word */
  .tool-row .info h3 {
    font-size: 1.05rem !important;
    line-height: 1.3 !important;
    margin-bottom: 6px !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
    hyphens: none !important;
  }

  /* Description full width */
  .tool-row .info p {
    font-size: 0.85rem !important;
    line-height: 1.5 !important;
    -webkit-line-clamp: 2 !important;
    line-clamp: 2 !important;
    margin: 0 !important;
  }

  /* Hide the tag pill inside icon-wrap on mobile (already on icon-label) */
  .tool-row > .tag {
    display: none !important;
  }

  /* Icon label positioning */
  .tool-row .icon-label {
    font-size: 0.55rem !important;
    padding: 2px 5px !important;
    top: -5px !important;
    right: -8px !important;
  }
}

/* ---------- TOOL LIST — single column on mobile ---------- */
@media (max-width: 768px) {
  .tool-list {
    grid-template-columns: 1fr !important;
    gap: 12px !important;
    padding: 14px !important;
    border-radius: 16px !important;
  }
}

/* ---------- CATEGORY CHIPS — proper horizontal scroll ---------- */
@media (max-width: 768px) {
  .category-rail {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    gap: 8px !important;
    padding: 12px !important;
    margin-bottom: 16px !important;
    -webkit-overflow-scrolling: touch !important;
    scrollbar-width: none !important;
    scroll-snap-type: x proximity !important;
  }
  .category-rail::-webkit-scrollbar {
    display: none !important;
  }
  .chip {
    padding: 8px 16px !important;
    font-size: 0.78rem !important;
    flex-shrink: 0 !important;
    scroll-snap-align: start !important;
  }
  .chip-blog {
    margin-left: 0 !important;
    padding: 8px 16px !important;
  }
  .chip-blog::before {
    display: none !important;
  }
}

/* ---------- SEARCH BAR ---------- */
@media (max-width: 768px) {
  #toolSearch {
    padding: 14px 18px !important;
    font-size: 0.88rem !important;
  }
}

/* ---------- FEATURE STRIP ---------- */
@media (max-width: 768px) {
  .feature-strip {
    grid-template-columns: 1fr !important;
    gap: 10px !important;
  }
}

/* ---------- HERO / TAGLINE ---------- */
@media (max-width: 768px) {
  .tagline {
    font-size: 0.85rem !important;
    line-height: 1.5 !important;
  }
}
"""

print("=" * 60)
print("Fixing mobile layout")
print("=" * 60)
print()

css = CSS.read_text(encoding="utf-8")

if "MOBILE VIEW FIX" in css:
    print("SKIP: Mobile fix already applied")
else:
    css += MOBILE_FIX
    CSS.write_text(css, encoding="utf-8")
    print("OK  assets/style.css — mobile fix appended")

print()
print("=" * 60)
print("DONE!")
print("=" * 60)
print()
print("Test:")
print("  1. python -m http.server 8000")
print("  2. Mobile Chrome → http://192.168.1.XXX:8000")
print("  3. Ya live site → hard refresh")
print()
print("Push:")
print("  git add .")
print("  git commit -m 'Fix mobile layout - tool cards, install button, chips'")
print("  git push")
print()
input("Press Enter to close...")