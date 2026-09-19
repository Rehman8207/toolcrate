import re
from pathlib import Path

ROOT = Path.cwd()
files_to_fix = [
    "word-counter.html", "case-converter.html", "unit-converter.html",
    "qr-generator.html", "password-generator.html", "image-compressor.html",
    "json-formatter.html", "age-calculator.html", "discount-calculator.html",
    "aggregate-calculator.html", "meta-tag-generator.html", "cgpa-calculator.html",
    "currency-converter.html", "image-to-pdf.html", "watermark-tool.html",
]

NEW_FONT = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap"
OLD_FONT_RE = re.compile(r'https://fonts\.googleapis\.com/css2\?family=Fraunces[^"]*')
THEME_RE = re.compile(r'(<button class="theme-toggle" id="themeToggle" type="button">)[^<]*(</button>)')

fixed = 0
for name in files_to_fix:
    f = ROOT / name
    if not f.exists():
        print(f"  ⚠️  {name} — not found, skipping")
        continue
    text = f.read_text(encoding="utf-8")
    original = text
    text = OLD_FONT_RE.sub(NEW_FONT, text)
    text = THEME_RE.sub(r'\1☀️ Light\2', text)
    if text != original:
        f.write_text(text, encoding="utf-8")
        print(f"  ✅ {name}")
        fixed += 1
    else:
        print(f"  ⏭️  {name} — already updated")

print()
print(f"🎉 Done! {fixed} files updated.")
input("Press Enter to close...")