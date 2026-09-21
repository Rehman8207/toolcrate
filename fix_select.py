#!/usr/bin/env python3
"""
Fix native <select> dropdown options that are invisible
(white text on white background) in dark theme.
Adds explicit option styling to style.css.
"""
from pathlib import Path

ROOT = Path.cwd()
CSS = ROOT / "assets" / "style.css"

if not CSS.exists():
    print("❌ assets/style.css not found")
    input("Press Enter...")
    exit(1)

SELECT_FIX = """

/* ============================================================
   FIX: Native select dropdown options
   Native <option> elements don't inherit theme colors well
   in dark mode — options end up white-on-white.
   This forces proper contrast in both themes.
   ============================================================ */

/* Default (dark theme): dark popup, light text */
select option,
.field select option,
.wm-field select option,
.input-group select option {
  background-color: #0F1A17 !important;
  color: #E8F5EE !important;
  padding: 8px 12px;
}

/* Selected/hovered option */
select option:checked,
select option:hover,
.field select option:checked,
.wm-field select option:checked {
  background-color: #10B981 !important;
  color: #FFFFFF !important;
}

/* Light theme: light popup, dark text */
[data-theme="light"] select option,
[data-theme="light"] .field select option,
[data-theme="light"] .wm-field select option,
[data-theme="light"] .input-group select option {
  background-color: #FFFFFF !important;
  color: #0A1410 !important;
}

[data-theme="light"] select option:checked,
[data-theme="light"] select option:hover {
  background-color: #059669 !important;
  color: #FFFFFF !important;
}

/* Also ensure the closed select shows readable text */
select,
.field select,
.wm-field select,
.input-group select {
  color: var(--ink) !important;
  background-color: var(--bg-2) !important;
}

[data-theme="light"] select,
[data-theme="light"] .field select {
  color: #0A1410 !important;
  background-color: #FFFFFF !important;
}

/* Disabled options */
select option:disabled {
  opacity: 0.5;
}

/* Firefox-specific: option styling */
@supports (-moz-appearance: none) {
  select option {
    background-color: #0F1A17;
    color: #E8F5EE;
  }
  [data-theme="light"] select option {
    background-color: #FFFFFF;
    color: #0A1410;
  }
}
"""

print("=" * 60)
print("Fixing native <select> dropdown option colors")
print("=" * 60)

css = CSS.read_text(encoding="utf-8")

if "FIX: Native select dropdown options" in css:
    print("⏭️  Fix already applied — skipping")
else:
    css += SELECT_FIX
    CSS.write_text(css, encoding="utf-8")
    print("✅ assets/style.css — select option fix added")

print()
print("=" * 60)
print("🎉 DONE!")
print("=" * 60)
print()
print("Test:")
print("  1. python -m http.server 8000")
print("  2. Open http://localhost:8000/meta-tag-generator.html")
print("  3. Click any dropdown (Language, Robots, etc.)")
print("  4. Options should now be visible")
print()
print("Also check other pages with dropdowns:")
print("  - age-calculator.html (uses date picker)")
print("  - unit-converter.html (category + from/to)")
print("  - currency-converter.html (from/to currencies)")
print("  - cgpa-calculator.html (grade select)")
print()
print("If everything looks good:")
print("    git add .")
print("    git commit -m 'Fix native select dropdown colors for dark theme'")
print("    git push")
print()
input("Press Enter to close...")