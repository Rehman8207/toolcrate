#!/usr/bin/env python3
"""
Add iLovePDF-style category labels on top of tool icons in index.html.
Colors match each category: PDF=red, IMG=blue, TEXT=violet, DEV=green, NUM=amber, SEO=pink.
"""
import re
from pathlib import Path

ROOT = Path.cwd()
INDEX = ROOT / "index.html"
CSS = ROOT / "assets" / "style.css"

# Sanity checks
if not INDEX.exists():
    print("❌ index.html not found in current folder")
    print("   Current folder:", ROOT)
    input("Press Enter to close...")
    exit(1)

if not CSS.exists():
    print("❌ assets/style.css not found")
    input("Press Enter to close...")
    exit(1)

print("=" * 60)
print("Adding category labels to tool icons")
print("=" * 60)

# ============================================================
# Category mapping (based on filename without .html)
# ============================================================
LABEL_MAP = {
    'word-counter':         ('TEXT', 'text'),
    'case-converter':       ('TEXT', 'text'),
    'image-compressor':     ('IMG',  'img'),
    'image-to-pdf':         ('IMG',  'img'),
    'watermark-tool':       ('IMG',  'img'),
    'pdf-merge':            ('PDF',  'pdf'),
    'pdf-to-text':          ('PDF',  'pdf'),
    'text-to-pdf':          ('PDF',  'pdf'),
    'qr-generator':         ('DEV',  'dev'),
    'password-generator':   ('DEV',  'dev'),
    'json-formatter':       ('DEV',  'dev'),
    'meta-tag-generator':   ('SEO',  'seo'),
    'age-calculator':       ('NUM',  'num'),
    'discount-calculator':  ('NUM',  'num'),
    'aggregate-calculator': ('NUM',  'num'),
    'cgpa-calculator':      ('NUM',  'num'),
    'currency-converter':   ('NUM',  'num'),
    'unit-converter':       ('NUM',  'num'),
}

def page_from_href(href):
    return href.replace('.html', '').split('/')[-1].strip()

# ============================================================
# STEP 1: Process index.html
# ============================================================
html = INDEX.read_text(encoding="utf-8")

# Find the <section class="tool-list">...</section>
section_re = re.compile(
    r'(<section\s+class="tool-list"[^>]*>)(.*?)(</section>)',
    re.DOTALL
)
section_match = section_re.search(html)

if not section_match:
    print("❌ Could not find <section class='tool-list'> in index.html")
    input("Press Enter to close...")
    exit(1)

section_open = section_match.group(1)
section_inner = section_match.group(2)
section_close = section_match.group(3)

# Match each <a class="tool-row" ...>...</a>
row_re = re.compile(
    r'(<a\s+class="tool-row"[^>]*?href="([^"]+)"[^>]*?>)(.*?)(</a>)',
    re.DOTALL
)

stats = {'processed': 0, 'skipped': 0, 'already': 0}

def process_row(m):
    opening = m.group(1)
    href = m.group(2)
    inner = m.group(3)
    closing = m.group(4)

    page = page_from_href(href)
    if page not in LABEL_MAP:
        stats['skipped'] += 1
        return m.group(0)

    # Skip if already wrapped
    if 'icon-wrap' in inner:
        stats['already'] += 1
        return m.group(0)

    label_text, label_class = LABEL_MAP[page]

    # Find the <div class="icon">...</div> block
    icon_re = re.compile(r'<div\s+class="icon"[^>]*>.*?</div>', re.DOTALL)
    icon_match = icon_re.search(inner)

    if not icon_match:
        print(f"   ⚠️  No icon found for {page} — skipping")
        stats['skipped'] += 1
        return m.group(0)

    icon_html = icon_match.group(0)
    label_html = (
        f'<span class="icon-label icon-label--{label_class}">{label_text}</span>'
    )
    wrapped = f'<div class="icon-wrap">{icon_html}{label_html}</div>'

    # Replace icon with wrapped version
    new_inner = inner[:icon_match.start()] + wrapped + inner[icon_match.end():]

    # Remove old <div class="tag">...</div>
    new_inner = re.sub(
        r'\s*<div\s+class="tag"[^>]*>.*?</div>',
        '',
        new_inner,
        flags=re.DOTALL
    )

    stats['processed'] += 1
    return opening + new_inner + closing

new_section_inner = row_re.sub(process_row, section_inner)

new_html = (
    html[:section_match.start()]
    + section_open
    + new_section_inner
    + section_close
    + html[section_match.end():]
)

INDEX.write_text(new_html, encoding="utf-8")
print(f"✅ index.html — {stats['processed']} tools updated")
if stats['already']:
    print(f"   ⏭️  {stats['already']} already had labels (skipped)")
if stats['skipped']:
    print(f"   ⚠️  {stats['skipped']} skipped (no icon or unknown tool)")

# ============================================================
# STEP 2: Append CSS
# ============================================================
css = CSS.read_text(encoding="utf-8")

CSS_BLOCK = """

/* ============================================
   TOOL ICON LABELS (iLovePDF style)
   ============================================ */

.tool-row {
  position: relative;
}

.icon-wrap {
  position: relative;
  display: inline-block;
  width: 40px;
  height: 40px;
  margin-bottom: 4px;
  flex-shrink: 0;
}

.icon-wrap .icon {
  width: 40px !important;
  height: 40px !important;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 10px;
  color: var(--accent);
  padding: 8px;
  box-sizing: border-box;
}

.icon-wrap .icon svg {
  width: 20px !important;
  height: 20px !important;
  max-width: 20px !important;
  max-height: 20px !important;
}

.icon-label {
  position: absolute;
  top: -6px;
  right: -10px;
  font-family: var(--font-mono, monospace);
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  padding: 2px 6px;
  border-radius: 4px;
  color: #FFFFFF;
  text-transform: uppercase;
  line-height: 1.3;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
  pointer-events: none;
  white-space: nowrap;
  z-index: 2;
}

.icon-label--pdf  { background: #EF4444; }
.icon-label--img  { background: #3B82F6; }
.icon-label--text { background: #8B5CF6; }
.icon-label--dev  { background: #10B981; }
.icon-label--num  { background: #F59E0B; }
.icon-label--seo  { background: #EC4899; }

/* Hide the old text pill tag */
.tool-row .tag {
  display: none !important;
}

/* Light mode polish */
[data-theme="light"] .icon-label {
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

[data-theme="light"] .icon-wrap .icon {
  background: #F1F5F9;
  border-color: #E2E8F0;
}

/* Mobile tweak */
@media (max-width: 640px) {
  .icon-label {
    font-size: 0.55rem;
    padding: 2px 5px;
    top: -5px;
    right: -8px;
  }
}
"""

if 'TOOL ICON LABELS' not in css:
    css += CSS_BLOCK
    CSS.write_text(css, encoding="utf-8")
    print("✅ assets/style.css — label styles added")
else:
    print("⏭️  assets/style.css — label styles already exist, skipping")

print()
print("=" * 60)
print("🎉 DONE!")
print("=" * 60)
print()
print("Next steps:")
print("  1. Start local server: python -m http.server 8000")
print("  2. Open http://localhost:8000 in browser")
print("  3. Ctrl + Shift + R (hard refresh)")
print("  4. Check that each tool icon has a small colored label")
print()
print("  If everything looks good:")
print("    git add .")
print("    git commit -m 'Add category labels to tool icons'")
print("    git push")
print()
input("Press Enter to close...")