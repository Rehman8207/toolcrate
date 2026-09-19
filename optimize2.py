import re
from pathlib import Path

ROOT = Path.cwd()

# ============ 1. UPDATE style.css — System fonts ============
css = ROOT / "assets" / "style.css"
if css.exists():
    text = css.read_text(encoding="utf-8")
    original = text

    # Replace font variables with system font stack
    text = text.replace(
        "--font-body:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;",
        "--font-body:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;"
    )
    text = text.replace(
        "--font-display:'Space Grotesk','Inter',sans-serif;",
        "--font-display:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;"
    )
    text = text.replace(
        "--font-mono:'JetBrains Mono','SF Mono',monospace;",
        "--font-mono:'SF Mono',Menlo,Monaco,Consolas,'Liberation Mono','Courier New',monospace;"
    )

    # Also handle old Fraunces variant
    text = text.replace(
        "--font-body:'Inter','Fraunces',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;",
        "--font-body:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;"
    )
    text = text.replace(
        "--font-display:'Space Grotesk','Fraunces','Inter',sans-serif;",
        "--font-display:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;"
    )
    text = text.replace(
        "--font-mono:'JetBrains Mono','IBM Plex Mono','SF Mono',monospace;",
        "--font-mono:'SF Mono',Menlo,Monaco,Consolas,'Liberation Mono','Courier New',monospace;"
    )

    if text != original:
        css.write_text(text, encoding="utf-8")
        print("✅ style.css — system fonts updated")
    else:
        print("⚠️  style.css — no font variables found to replace")

# ============ 2. REMOVE Google Fonts from ALL HTML files ============
FONT_BLOCK_RE = re.compile(
    r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*'
    r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*'
    r'<link rel="preload" as="style" href="https://fonts\.googleapis\.com/css2\?[^"]*">\s*'
    r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">',
    re.DOTALL
)

# Fallback for older format (just in case)
FONT_BLOCK_RE_OLD = re.compile(
    r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*'
    r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*'
    r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">',
    re.DOTALL
)

updated = 0
for f in sorted(ROOT.glob("*.html")):
    text = f.read_text(encoding="utf-8")
    original = text

    text = FONT_BLOCK_RE.sub("<!-- Fonts: system fonts for maximum performance -->", text)
    text = FONT_BLOCK_RE_OLD.sub("<!-- Fonts: system fonts for maximum performance -->", text)

    # Also remove orphan preconnect lines
    text = re.sub(
        r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*',
        "",
        text
    )
    text = re.sub(
        r'<link rel="preload" as="style" href="https://fonts\.googleapis\.com/css2\?[^"]*">\s*',
        "",
        text
    )
    text = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">',
        "",
        text
    )

    if text != original:
        f.write_text(text, encoding="utf-8")
        print(f"   ✅ {f.name} — Google Fonts removed")
        updated += 1

print()
print("=" * 55)
print(f"🎉 DONE! System fonts applied. {updated} HTML files cleaned.")
print("=" * 55)
print()
print("Next:")
print("  git add .")
print("  git commit -m 'Switch to system fonts for maximum performance'")
print("  git push")
print()
input("Press Enter to close...")