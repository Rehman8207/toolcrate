#!/usr/bin/env python3
"""
Remove the broken install button completely from all HTML files.
Also removes the related CSS and JS.
"""
from pathlib import Path
import re

ROOT = Path.cwd()
CSS = ROOT / "assets" / "style.css"
JS = ROOT / "assets" / "common.js"

print("=" * 60)
print("Removing broken install button")
print("=" * 60)
print()

# ============================================================
# 1. Remove button from all HTML files
# ============================================================
print("Step 1: Removing from HTML files...")
print()

# Match the install button HTML (any variant)
BUTTON_PATTERNS = [
    # Standard pattern
    re.compile(
        r'<button\s+class="install-app-btn"[^>]*>[\s\S]*?</button>\s*',
        re.IGNORECASE
    ),
    # If nested SVG with multiline
    re.compile(
        r'<button[^>]*id="installAppBtn"[^>]*>[\s\S]*?</button>\s*',
        re.IGNORECASE
    ),
]

all_html = list(ROOT.glob("*.html")) + list((ROOT / "blog").glob("*.html"))
updated = 0
skipped = 0

for fp in all_html:
    text = fp.read_text(encoding="utf-8", errors="ignore")
    original = text

    # Remove button
    for pattern in BUTTON_PATTERNS:
        text = pattern.sub('', text)

    # Also remove install modal if present
    text = re.sub(
        r'<!--\s*Install Modal\s*-->[\s\S]*?<div class="install-modal"[^>]*>[\s\S]*?</div>\s*</div>\s*',
        '',
        text,
        flags=re.IGNORECASE
    )

    if text != original:
        fp.write_text(text, encoding="utf-8")
        print(f"  OK  {fp.relative_to(ROOT)}")
        updated += 1
    else:
        skipped += 1

print(f"\n  {updated} updated, {skipped} skipped\n")

# ============================================================
# 2. Remove JS from common.js
# ============================================================
print("Step 2: Removing JS from common.js...")

if JS.exists():
    js_text = JS.read_text(encoding="utf-8")
    original_js = js_text

    # Remove PWA INSTALL blocks
    js_text = re.sub(
        r'/\* =+\s*PWA INSTALL[^*]*=+ \*/[\s\S]*?\}\)\(\);',
        '',
        js_text
    )

    if js_text != original_js:
        JS.write_text(js_text, encoding="utf-8")
        print("  OK  common.js — install JS removed")
    else:
        print("  SKIP  common.js — no install JS found")

# ============================================================
# 3. Add hide CSS as safety net
# ============================================================
print("\nStep 3: Adding hide CSS as safety net...")

if CSS.exists():
    css_text = CSS.read_text(encoding="utf-8")
    
    SAFETY_CSS = """

/* ============================================================
   SAFETY: Hide any remaining install button
   ============================================================ */

.install-app-btn,
#installAppBtn,
.install-modal,
#installModal {
  display: none !important;
  visibility: hidden !important;
  width: 0 !important;
  height: 0 !important;
  overflow: hidden !important;
}
"""
    
    if "SAFETY: Hide any remaining install button" not in css_text:
        css_text += SAFETY_CSS
        CSS.write_text(css_text, encoding="utf-8")
        print("  OK  style.css — safety hide CSS added")
    else:
        print("  SKIP  style.css — already has safety CSS")

print()
print("=" * 60)
print("DONE! Install button removed completely")
print("=" * 60)
print()
print("Now push:")
print("  git add .")
print('  git commit -m "Remove broken install button"')
print("  git push")
print()
print("Then:")
print("  1. Wait 1 minute for Cloudflare deploy")
print("  2. Hard refresh browser: Ctrl + Shift + R")
print("  3. White box should be gone!")
print()
input("Press Enter to close...")