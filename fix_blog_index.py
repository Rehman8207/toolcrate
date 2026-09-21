#!/usr/bin/env python3
"""
Update blog/index.html to remove 'Coming soon' text and show real dates
for the 4 new posts that now exist.
"""
from pathlib import Path
import re

ROOT = Path.cwd()
BLOG_INDEX = ROOT / "blog" / "index.html"

if not BLOG_INDEX.exists():
    print("❌ blog/index.html not found")
    input("Press Enter...")
    exit(1)

text = BLOG_INDEX.read_text(encoding="utf-8")
original = text

# Replace "Coming soon" spans with real publish dates
text = text.replace(
    '<span>Coming soon</span>',
    '<span>Sep 21, 2026</span>'
)

# Also handle if it's written differently
text = text.replace(
    'Coming soon',
    'Sep 21, 2026'
)

if text != original:
    BLOG_INDEX.write_text(text, encoding="utf-8")
    # Count how many were fixed
    count = original.count('Coming soon')
    print(f"✅ blog/index.html — {count} 'Coming soon' replaced with real dates")
else:
    print("⏭️  blog/index.html — no 'Coming soon' found")

print()
print("=" * 60)
print("Now verify:")
print("  python -m http.server 8000")
print("  Open: http://localhost:8000/blog/")
print("  All 5 cards should now show dates")
print("=" * 60)
print()
input("Press Enter to close...")