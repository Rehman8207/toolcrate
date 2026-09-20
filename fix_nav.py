#!/usr/bin/env python3
"""
1. Remove top-nav from header (back to logo + toggle only)
2. Add Blog as a chip-style link at end of category rail on homepage
"""
import re
from pathlib import Path

ROOT = Path.cwd()

# ============================================================
# HEADER — Back to simple (logo + toggle only)
# ============================================================
CLEAN_HEADER = '''<header class="masthead">
<div class="row">
<div class="brand-block">
<div><div class="brand"><h1><a href="{home_path}">ToolCrate</a></h1></div></div>
</div>
<button class="theme-toggle" id="themeToggle" type="button">☀️ Light</button>
</div>
</header>'''

# ============================================================
# Blog chip to add on homepage
# ============================================================
BLOG_CHIP = '<a class="chip chip-blog" href="blog/index.html">📚 Blog</a>'

# ============================================================
# CSS to style blog chip + remove top-nav styles
# ============================================================
NEW_CSS = """

/* ============================================
   BLOG CHIP (in category rail)
   ============================================ */

.chip-blog {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(34,211,238,0.08) 100%);
  border: 1px solid rgba(16,185,129,0.35);
  color: var(--emerald);
  text-decoration: none;
  font-weight: 600;
  position: relative;
  margin-left: 8px;
}

.chip-blog::before {
  content: '';
  position: absolute;
  left: -8px;
  top: 50%;
  transform: translateY(-50%);
  width: 1px;
  height: 20px;
  background: var(--border-2);
}

.chip-blog:hover {
  background: linear-gradient(135deg, rgba(16,185,129,0.20) 0%, rgba(34,211,238,0.12) 100%);
  border-color: var(--emerald);
  color: var(--emerald);
  transform: translateY(-1px);
}

@media (max-width: 640px) {
  .chip-blog {
    margin-left: 0;
  }
  .chip-blog::before {
    display: none;
  }
}

/* Hide any leftover top-nav if exists */
.top-nav {
  display: none !important;
}
"""

def read_file_safe(path):
    try:
        return path.read_text(encoding="utf-8"), "utf-8"
    except UnicodeDecodeError:
        pass
    try:
        return path.read_text(encoding="cp1252"), "cp1252"
    except UnicodeDecodeError:
        pass
    return path.read_text(encoding="latin-1"), "latin-1"

# ============================================================
# Process files
# ============================================================
print("=" * 60)
print("Cleaning header + adding Blog chip to category rail")
print("=" * 60)

all_files = list(ROOT.glob("*.html")) + list((ROOT / "blog").glob("*.html"))

updated = 0
skipped = 0
errors = 0

for fp in sorted(all_files):
    try:
        text, _ = read_file_safe(fp)
    except Exception as e:
        print(f"   ❌ {fp.relative_to(ROOT)} — {e}")
        errors += 1
        continue

    original = text

    # Determine home path
    if fp.parent.name == "blog":
        home_path = "../index.html"
    else:
        home_path = "index.html"

    # -------- Clean HEADER (remove top-nav) --------
    header_pattern = re.compile(
        r'<header class="masthead">.*?</header>',
        re.DOTALL
    )
    clean_header = CLEAN_HEADER.format(home_path=home_path)
    text = header_pattern.sub(clean_header, text, count=1)

    # -------- Add Blog chip to category rail (index.html only) --------
    if fp.name == "index.html" and fp.parent.name != "blog":
        # Find the category rail and add Blog chip before closing </nav>
        rail_pattern = re.compile(
            r'(<nav class="category-rail"[^>]*>)(.*?)(</nav>)',
            re.DOTALL
        )

        def add_blog_chip(m):
            open_tag = m.group(1)
            inner = m.group(2)
            close_tag = m.group(3)
            # Remove any existing blog chip
            inner = re.sub(r'<a[^>]*chip-blog[^>]*>.*?</a>', '', inner, flags=re.DOTALL)
            # Add blog chip at the end
            return open_tag + inner.rstrip() + '\n' + BLOG_CHIP + '\n' + close_tag

        text = rail_pattern.sub(add_blog_chip, text, count=1)

    if text != original:
        fp.write_text(text, encoding="utf-8")
        print(f"   ✅ {fp.relative_to(ROOT)}")
        updated += 1
    else:
        print(f"   ⏭️  {fp.relative_to(ROOT)} — no change")
        skipped += 1

# -------- Append CSS --------
css_file = ROOT / "assets" / "style.css"
if css_file.exists():
    css, _ = read_file_safe(css_file)
    if "BLOG CHIP" not in css:
        css += NEW_CSS
        css_file.write_text(css, encoding="utf-8")
        print()
        print("✅ assets/style.css — blog chip styles added")
    else:
        print()
        print("⏭️  assets/style.css — already has blog chip styles")

print()
print("=" * 60)
print(f"🎉 DONE! {updated} updated, {skipped} skipped, {errors} errors")
print("=" * 60)
print()
print("Next:")
print("  1. python -m http.server 8000")
print("  2. Open http://localhost:8000/")
print("  3. Ctrl + Shift + R")
print("  4. Check header has only logo + toggle")
print("  5. Check category rail ends with '📚 Blog' chip")
print()
print("  If everything looks good:")
print("    git add .")
print("    git commit -m 'Clean header, add Blog chip to category rail'")
print("    git push")
print()
input("Press Enter to close...")