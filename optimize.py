import re
from pathlib import Path

ROOT = Path.cwd()

# ============ 1. FIX GTAG — Use defer + fast inline loading ============
OLD_GTAG_PATTERN = re.compile(
    r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-H20HJWJQWV"></script>\s*'
    r'<script>\s*window\.dataLayer=window\.dataLayer\|\|\[\];\s*function gtag\(\)\{dataLayer\.push\(arguments\);\}\s*'
    r'gtag\([\'"]js[\'"],\s*new Date\(\)\);\s*gtag\([\'"]config[\'"],\s*[\'"]G-H20HJWJQWV[\'"]\);\s*</script>',
    re.DOTALL
)

NEW_GTAG = '''<!-- Google tag (gtag.js) — deferred for performance -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-H20HJWJQWV');
  // Load gtag.js after page is interactive
  window.addEventListener('load', function(){
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=G-H20HJWJQWV';
    document.head.appendChild(s);
  });
</script>'''

# Also handle simpler variant (some pages have slight variation)
OLD_GTAG_SIMPLE = re.compile(
    r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=G-H20HJWJQWV"></script>\s*'
    r'<script>[^<]*window\.dataLayer[^<]*</script>',
    re.DOTALL
)

# ============ 2. FIX FONT LINK — Add display=swap + media print trick ============
OLD_FONT_LINK = re.compile(
    r'<link href="https://fonts\.googleapis\.com/css2\?family=Inter[^"]*" rel="stylesheet">'
)

NEW_FONT_LINK = '''<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">'''

# ============ 3. Fix heading order — add hidden h2 in index.html ============
HIDDEN_H2 = '''<h2 style="position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden;">Available Tools</h2>'''

# ============ Process all HTML files ============
files = list(ROOT.glob("*.html"))
total = len(files)
print(f"Processing {total} HTML files...\n")

updated_gtag = 0
updated_font = 0
updated_heading = 0

for f in files:
    text = f.read_text(encoding="utf-8")
    original = text

    # 1. Fix GTM
    if OLD_GTAG_PATTERN.search(text):
        text = OLD_GTAG_PATTERN.sub(NEW_GTAG, text)
        updated_gtag += 1
    elif OLD_GTAG_SIMPLE.search(text):
        text = OLD_GTAG_SIMPLE.sub(NEW_GTAG, text)
        updated_gtag += 1

    # 2. Fix font preload
    if OLD_FONT_LINK.search(text):
        text = OLD_FONT_LINK.sub(NEW_FONT_LINK, text)
        updated_font += 1

    # 3. Fix heading order on index.html only
    if f.name == "index.html" and '<h2 style="position:absolute' not in text:
        # Insert hidden h2 right before the tool-list section
        if '<section class="tool-list"' in text:
            text = text.replace(
                '<section class="tool-list"',
                HIDDEN_H2 + '\n<section class="tool-list"',
                1
            )
            updated_heading += 1

    if text != original:
        f.write_text(text, encoding="utf-8")

print(f"✅ GTM deferred: {updated_gtag} files")
print(f"✅ Fonts preloaded: {updated_font} files")
print(f"✅ Heading hierarchy fixed: {updated_heading} files")
print()
print("=" * 55)
print("🎉 Optimization complete!")
print("=" * 55)
print()
print("Now push:")
print("  git add .")
print("  git commit -m 'Performance optimization: defer GTM, preload fonts, fix headings'")
print("  git push")
print()
input("Press Enter to close...")