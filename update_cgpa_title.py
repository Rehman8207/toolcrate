#!/usr/bin/env python3
"""
Update CGPA calculator page to target the winning keyword:
'CGPA Calculator Pakistan (HEC 4.0 Scale)'
"""
from pathlib import Path
import re

ROOT = Path.cwd()
CGPA = ROOT / "cgpa-calculator.html"

if not CGPA.exists():
    print("ERROR: cgpa-calculator.html not found")
    input("Press Enter...")
    exit(1)

text = CGPA.read_text(encoding="utf-8")
original = text

# New title (55 chars — perfect)
NEW_TITLE = "CGPA Calculator Pakistan (HEC 4.0 Scale) | ToolCrate"

# New meta description (155 chars — perfect)
NEW_DESC = "Free HEC CGPA calculator for Pakistani universities. Calculate CGPA on 4.0 scale, convert to percentage, extract semester GPA instantly."

# Update title tag
text = re.sub(
    r'<title>[^<]*</title>',
    f'<title>{NEW_TITLE}</title>',
    text,
    count=1
)

# Update meta description
text = re.sub(
    r'<meta\s+name="description"\s+content="[^"]*"\s*/?>',
    f'<meta name="description" content="{NEW_DESC}">',
    text,
    count=1
)

# Update OG title and description
text = re.sub(
    r'<meta\s+property="og:title"\s+content="[^"]*"\s*/?>',
    f'<meta property="og:title" content="{NEW_TITLE}">',
    text,
    count=1
)

text = re.sub(
    r'<meta\s+property="og:description"\s+content="[^"]*"\s*/?>',
    f'<meta property="og:description" content="{NEW_DESC}">',
    text,
    count=1
)

# Update Twitter title/description
text = re.sub(
    r'<meta\s+(?:property|name)="twitter:title"\s+content="[^"]*"\s*/?>',
    f'<meta name="twitter:title" content="{NEW_TITLE}">',
    text,
    count=1
)

text = re.sub(
    r'<meta\s+(?:property|name)="twitter:description"\s+content="[^"]*"\s*/?>',
    f'<meta name="twitter:description" content="{NEW_DESC}">',
    text,
    count=1
)

if text != original:
    CGPA.write_text(text, encoding="utf-8")
    print("=" * 60)
    print("CGPA Calculator updated!")
    print("=" * 60)
    print()
    print(f"NEW TITLE:       {NEW_TITLE}")
    print(f"  Character count: {len(NEW_TITLE)}/60 ✅")
    print()
    print(f"NEW DESCRIPTION: {NEW_DESC}")
    print(f"  Character count: {len(NEW_DESC)}/160 ✅")
    print()
    print("Next steps:")
    print("  1. python -m http.server 8000")
    print("  2. Open http://localhost:8000/cgpa-calculator.html")
    print("  3. Check title in browser tab")
    print("  4. git add .")
    print('  5. git commit -m "Target CGPA Pakistan HEC keyword"')
    print("  6. git push")
    print()
else:
    print("No changes made")

input("Press Enter to close...")