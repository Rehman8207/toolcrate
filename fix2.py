import re
from pathlib import Path

ROOT = Path.cwd()

HERO_TEMPLATE = '''<header class="masthead">
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
<h1 class="hero-title">{TITLE} <span class="grad-word">right in your browser</span></h1>
<p class="hero-sub">{SUB}</p>
</header>'''

FILES = {
    "cgpa-calculator.html": (
        "Calculate CGPA",
        "Extract semester GPA from your result card, plan target CGPA, or calculate course-wise GPA."
    ),
    "currency-converter.html": (
        "Convert currencies",
        "Convert real-time exchange rates for 150+ world currencies instantly."
    ),
    "image-to-pdf.html": (
        "Convert images to PDF",
        "Convert JPG, PNG and WebP images into a single PDF. Folder upload, no page limit."
    ),
}

for name, (title, sub) in FILES.items():
    fp = ROOT / name
    if not fp.exists():
        print(f"⚠️  {name} — not found")
        continue

    text = fp.read_text(encoding="utf-8")

    # Replace the first <header>...</header> block (any attributes) with colorful hero
    pattern = re.compile(r'<header[^>]*>.*?</header>', re.DOTALL)
    hero = HERO_TEMPLATE.replace("{TITLE}", title).replace("{SUB}", sub)
    new_text, count = pattern.subn(hero, text, count=1)

    if count:
        fp.write_text(new_text, encoding="utf-8")
        print(f"✅ {name}")
    else:
        print(f"⚠️  {name} — no <header> tag found")

print()
print("=" * 55)
print("🎉 DONE! All pages now have the colorful hero.")
print("=" * 55)
print()
print("Next:")
print("  git add .")
print("  git commit -m 'Fix remaining pages with colorful hero'")
print("  git push")
print()
input("Press Enter to close...")