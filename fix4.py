import re
from pathlib import Path

ROOT = Path.cwd()

# ============ FIX 1: Shorten long titles ============
TITLE_FIXES = {
    # Original (truncated) -> Shortened title
    "word-counter.html": "Free Word & Character Counter Online | ToolCrate",
    "case-converter.html": "Free Case Converter — UPPERCASE, Title Case | ToolCrate",
    "unit-converter.html": "Free Unit Converter — Length, Weight, Temperature | ToolCrate",
    "qr-generator.html": "Free QR Code Generator Online — No Signup | ToolCrate",
    "password-generator.html": "Free Strong Password Generator | ToolCrate",
    "image-compressor.html": "Free Image Compressor — Reduce Photo Size | ToolCrate",
    "json-formatter.html": "Free JSON Formatter & Validator | ToolCrate",
    "age-calculator.html": "Free Age Calculator — Years, Months, Days | ToolCrate",
    "discount-calculator.html": "Free Discount & Tax Calculator | ToolCrate",
    "aggregate-calculator.html": "Free Percentage Calculator | ToolCrate",
    "meta-tag-generator.html": "Free Meta Tag Generator — SEO Tags | ToolCrate",
    "cgpa-calculator.html": "CGPA & GPA Calculator — Extract Semester GPA | ToolCrate",
    "currency-converter.html": "Live Currency Converter — 150+ Currencies | ToolCrate",
    "image-to-pdf.html": "Image to PDF Converter — Batch & Folder | ToolCrate",
    "watermark-tool.html": "Free Watermark Tool — Images & PDFs | ToolCrate",
    "about.html": "About ToolCrate — Free Browser Tools | ToolCrate",
    "contact.html": "Contact ToolCrate — Get in Touch | ToolCrate",
    "privacy.html": "Privacy Policy — ToolCrate",
}

print("=" * 60)
print("FIX 1: Shortening titles")
print("=" * 60)

TITLE_RE = re.compile(r'<title>[^<]*</title>')

for fname, new_title in TITLE_FIXES.items():
    fp = ROOT / fname
    if not fp.exists():
        print(f"   ⚠️  {fname} — not found")
        continue
    text = fp.read_text(encoding="utf-8")
    old = text
    text = TITLE_RE.sub(f'<title>{new_title}</title>', text, count=1)
    if text != old:
        fp.write_text(text, encoding="utf-8")
        print(f"   ✅ {fname} → {new_title}")
    else:
        print(f"   ⏭️  {fname}")

# ============ FIX 2: Remove duplicate h1 tags ============
print()
print("=" * 60)
print("FIX 2: Removing duplicate h1 tags")
print("=" * 60)

H1_RE = re.compile(r'<h1[^>]*>(.*?)</h1>', re.DOTALL)

for fp in sorted(ROOT.glob("*.html")):
    text = fp.read_text(encoding="utf-8")
    original = text

    # Find all h1s
    matches = list(H1_RE.finditer(text))

    if len(matches) <= 1:
        continue

    # Keep the last one (hero-title), convert others to h2 or h3
    # Reverse order to avoid offset issues
    for match in reversed(matches[:-1]):
        # Convert duplicate h1 to div (keep styling via class)
        full_match = match.group(0)
        inner = match.group(1)

        # Check if it's the brand h1
        if 'brand' in full_match or 'ToolCrate' in inner:
            # Replace with h2 styled same way
            replacement = f'<h2 class="brand-h1">{inner}</h2>'
        else:
            replacement = f'<h2>{inner}</h2>'

        text = text[:match.start()] + replacement + text[match.end():]

    if text != original:
        fp.write_text(text, encoding="utf-8")
        print(f"   ✅ {fp.name}")

print()
print("=" * 60)
print("🎉 DONE!")
print("=" * 60)
print()
print("Next:")
print("  git add .")
print("  git commit -m 'Fix title length and duplicate h1 tags'")
print("  git push")
print()
input("Press Enter to close...")