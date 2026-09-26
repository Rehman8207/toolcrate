#!/usr/bin/env python3
"""
Update titles on image-compressor.html and qr-generator.html
to target competitor keywords directly.
"""
from pathlib import Path
import re

ROOT = Path.cwd()

UPDATES = {
    "image-compressor.html": {
        "title": "Image Compressor for WhatsApp — Free, No Upload | ToolCrate",
        "desc": "Compress images for WhatsApp without uploading. Free browser-based tool, no signup, no file limits. Works on mobile and desktop.",
    },
    "qr-generator.html": {
        "title": "WiFi QR Code Generator — Free, No Signup | ToolCrate",
        "desc": "Create a WiFi QR code for your network — guests scan and connect instantly. Free, no signup, no upload. Works on any phone.",
    },
}

print("=" * 60)
print("Updating titles for competitor keywords")
print("=" * 60)
print()

for fname, data in UPDATES.items():
    fp = ROOT / fname
    if not fp.exists():
        print(f"SKIP: {fname} not found")
        continue

    text = fp.read_text(encoding="utf-8")
    original = text

    # Update title
    text = re.sub(r'<title>[^<]*</title>', f'<title>{data["title"]}</title>', text, count=1)

    # Update meta description
    text = re.sub(
        r'<meta\s+name="description"\s+content="[^"]*"\s*/?>',
        f'<meta name="description" content="{data["desc"]}">',
        text,
        count=1
    )

    # Update og:title
    text = re.sub(
        r'<meta\s+property="og:title"\s+content="[^"]*"\s*/?>',
        f'<meta property="og:title" content="{data["title"]}">',
        text,
        count=1
    )

    # Update og:description
    text = re.sub(
        r'<meta\s+property="og:description"\s+content="[^"]*"\s*/?>',
        f'<meta property="og:description" content="{data["desc"]}">',
        text,
        count=1
    )

    # Update twitter:title
    text = re.sub(
        r'<meta\s+name="twitter:title"\s+content="[^"]*"\s*/?>',
        f'<meta name="twitter:title" content="{data["title"]}">',
        text,
        count=1
    )

    # Update twitter:description
    text = re.sub(
        r'<meta\s+name="twitter:description"\s+content="[^"]*"\s*/?>',
        f'<meta name="twitter:description" content="{data["desc"]}">',
        text,
        count=1
    )

    if text != original:
        fp.write_text(text, encoding="utf-8")
        print(f"OK  {fname}")
        print(f"     New title: {data['title']}")
        print(f"     Chars: {len(data['title'])}/60 {'OK' if len(data['title']) <= 60 else 'TOO LONG'}")
        print()
    else:
        print(f"SKIP {fname} - no changes made")
        print()

print("=" * 60)
print("DONE!")
print("=" * 60)
print()
print("Next:")
print("  git add .")
print('  git commit -m "Target competitor keywords: image compressor, wifi qr"')
print("  git push")
print()
input("Press Enter to close...")