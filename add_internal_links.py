#!/usr/bin/env python3
"""
Add internal links from existing blog posts to tools and other posts.
"""
from pathlib import Path
import re

ROOT = Path.cwd()
BLOG = ROOT / "blog"

# Map of blog post -> related content suggestions
LINK_MAP = {
    "compress-image-for-whatsapp.html": [
        ('<h2>Conclusion</h2>', '''<h2>Related Tools</h2>
<ul>
<li><a href="../image-compressor.html">Image Compressor</a> - Compress any image</li>
<li><a href="../image-to-pdf.html">Image to PDF</a> - Convert photos to PDF</li>
<li><a href="compress-jpg-to-50kb.html">Compress JPG to 50KB</a> - For online forms</li>
<li><a href="compress-jpg-to-100kb.html">Compress JPG to 100KB</a> - For job applications</li>
</ul>

<h2>Conclusion</h2>''')
    ],
    "compress-jpg-to-100kb.html": [
        ('<h2>Frequently Asked Questions</h2>', '''<h2>Related Guides</h2>
<ul>
<li><a href="compress-jpg-to-50kb.html">Compress JPG to 50KB</a> - Smaller requirement</li>
<li><a href="compress-image-for-whatsapp.html">Compress Images for WhatsApp</a> - Messaging</li>
<li><a href="../image-compressor.html">Image Compressor Tool</a> - Open tool</li>
</ul>

<h2>Frequently Asked Questions</h2>''')
    ],
}

print("=" * 60)
print("Adding internal links to blog posts")
print("=" * 60)
print()

for fname, insertions in LINK_MAP.items():
    fp = BLOG / fname
    if not fp.exists():
        print(f"SKIP: {fname} not found")
        continue

    text = fp.read_text(encoding="utf-8")
    original = text

    for target, replacement in insertions:
        if target in text and "Related Guides" not in text and "Related Tools" not in text.split(target)[0][-500:]:
            text = text.replace(target, replacement, 1)

    if text != original:
        fp.write_text(text, encoding="utf-8")
        print(f"OK  {fname} - internal links added")
    else:
        print(f"SKIP {fname} - no changes")

print()
print("DONE!")
print()
print("Next:")
print("  git add .")
print('  git commit -m "Add 3 days tasks: expand QR blog, new post, internal links"')
print("  git push")
print()
input("Press Enter to close...")