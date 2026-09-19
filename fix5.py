import re
from pathlib import Path

ROOT = Path.cwd()

# ============ FIX 1: Shorten index.html title ============
print("=" * 60)
print("FIX 1: Shorten index.html title (77 → 55 chars)")
print("=" * 60)

index_file = ROOT / "index.html"
if index_file.exists():
    text = index_file.read_text(encoding="utf-8")
    new_title = "ToolCrate — 15+ Free Browser Tools | No Signup"
    text = re.sub(
        r'<title>[^<]*</title>',
        f'<title>{new_title}</title>',
        text,
        count=1
    )
    index_file.write_text(text, encoding="utf-8")
    print(f"   ✅ index.html → {new_title}")

# ============ FIX 2: Also check other pages > 70 chars ============
print()
print("=" * 60)
print("FIX 2: Verify all titles are under 70 chars")
print("=" * 60)

TITLE_RE = re.compile(r'<title>([^<]*)</title>')
over_limit = []

for fp in sorted(ROOT.glob("*.html")):
    text = fp.read_text(encoding="utf-8")
    m = TITLE_RE.search(text)
    if m:
        title = m.group(1).strip()
        length = len(title)
        if length > 70:
            over_limit.append((fp.name, title, length))
            print(f"   ⚠️  {fp.name}: {length} chars — {title}")
        else:
            print(f"   ✅ {fp.name}: {length} chars")

if not over_limit:
    print()
    print("   🎉 All titles under 70 characters!")

# ============ FIX 3: Update CSS for .brand h2 ============
print()
print("=" * 60)
print("FIX 3: Update CSS for .brand h2 styling")
print("=" * 60)

css_file = ROOT / "assets" / "style.css"
if css_file.exists():
    text = css_file.read_text(encoding="utf-8")
    original = text

    # Replace .brand h1 with combined rule (h1, h2, .brand-h1)
    text = re.sub(
        r'\.brand h1\{',
        '.brand h1,.brand h2,.brand-h1{',
        text
    )

    # Replace .brand a with combined rule
    text = re.sub(
        r'\.brand a\{',
        '.brand a,.brand h2 a{',
        text
    )

    if text != original:
        css_file.write_text(text, encoding="utf-8")
        print("   ✅ style.css — brand h1/h2 CSS updated")
    else:
        print("   ⏭️  style.css — already updated or pattern not found")

print()
print("=" * 60)
print("🎉 DONE!")
print("=" * 60)
print()
print("Next:")
print("  git add .")
print("  git commit -m 'Fix title length and brand h2 styling'")
print("  git push")
print()
input("Press Enter to close...")