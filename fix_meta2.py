#!/usr/bin/env python3
"""
Direct string-based fix for meta-tag-generator.html
Uses find/replace on exact text (not regex) — more reliable.
"""
from pathlib import Path

ROOT = Path.cwd()
FILE = ROOT / "meta-tag-generator.html"

if not FILE.exists():
    print("❌ meta-tag-generator.html not found")
    input("Press Enter...")
    exit(1)

text = FILE.read_text(encoding="utf-8")
original = text

# ============================================================
# The broken text starts at "paste it inside the <head>"
# and ends at "</head> section of your webpage code."
# We replace everything in between with clean text.
# ============================================================

# Find start position
start_marker = '"text": "Copy the generated HTML snippet and paste it inside the <head>'
end_marker = '</head> section of your webpage code."'

start_pos = text.find(start_marker)
if start_pos == -1:
    print("❌ Could not find start marker")
    input("Press Enter...")
    exit(1)

end_pos = text.find(end_marker, start_pos)
if end_pos == -1:
    print("❌ Could not find end marker")
    input("Press Enter...")
    exit(1)

# Include the end marker in the replacement range
end_pos += len(end_marker)

# The clean replacement
clean_text = '"text": "Copy the generated HTML snippet and paste it inside the head section of your webpage code."'

# Perform the replacement
new_text = text[:start_pos] + clean_text + text[end_pos:]

# Also check for any remaining WebApplication scripts (should still be one at the end of head)
# But since we removed the embedded one, we need to make sure there's a standalone WebApplication schema
# Check if WebApplication exists outside the FAQ
if '"@type": "WebApplication"' not in new_text:
    # Add it back after the FAQPage script
    faq_end = new_text.find('</script>', new_text.find('"@type": "FAQPage"'))
    if faq_end != -1:
        faq_end += len('</script>')
        webapp_schema = '''

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "ToolCrate Meta Tag Generator",
    "url": "https://site.toolcrate-tools.workers.dev/meta-tag-generator.html",
    "applicationCategory": "DeveloperApplication",
    "operatingSystem": "Any (runs in browser)",
    "offers": { "@type": "Offer", "price": "0", "priceCurrency": "USD" },
    "description": "Free SEO meta tag generator. Generate title, description, Open Graph and Twitter Card tags with a live preview.",
    "featureList": ["SEO title and description tags","Open Graph tags for Facebook/WhatsApp","Twitter Card tags","Meta robots tag","Live preview of Google SERP snippet"]
  }
  </script>'''
        new_text = new_text[:faq_end] + webapp_schema + new_text[faq_end:]
        print("✅ Also added standalone WebApplication schema")
else:
    print("✅ WebApplication schema already present")

# Save
if new_text != original:
    FILE.write_text(new_text, encoding="utf-8")
    print(f"✅ Fixed {end_pos - start_pos} chars replaced")
    print("💾 File saved successfully")
else:
    print("⏭️  No changes made")

print()
print("=" * 60)
print("Verify:")
print("  1. python -m http.server 8000")
print("  2. Open http://localhost:8000/meta-tag-generator.html")
print("  3. Ctrl+U → search 'paste it inside'")
print("  4. Should see: 'paste it inside the head section'")
print("=" * 60)
input("Press Enter to close...")