import re
from pathlib import Path

ROOT = Path.cwd()
css = ROOT / "assets" / "style.css"

if not css.exists():
    print("❌ style.css not found")
    input("Press Enter...")
    exit(1)

text = css.read_text(encoding="utf-8")

# Add standard line-clamp right after every -webkit-line-clamp
pattern = re.compile(r'(-webkit-line-clamp:\s*([^;]+);)')
def repl(m):
    full = m.group(1)
    val = m.group(2).strip()
    return full + f'\n  line-clamp: {val};'

new_text = pattern.sub(repl, text)

if new_text == text:
    print("⚠️  No changes — line-clamp maybe already added")
else:
    css.write_text(new_text, encoding="utf-8")
    print(f"✅ Fixed {len(pattern.findall(text))} line-clamp rules in style.css")

# Also fix style.pretty.css if it exists
pretty = ROOT / "assets" / "style.pretty.css"
if pretty.exists():
    pt = pretty.read_text(encoding="utf-8")
    pt2 = pattern.sub(repl, pt)
    if pt2 != pt:
        pretty.write_text(pt2, encoding="utf-8")
        print(f"✅ Fixed style.pretty.css too")
    else:
        print("⏭️  style.pretty.css already clean")

print()
input("Press Enter to close...")