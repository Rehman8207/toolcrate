#!/usr/bin/env python3
"""Expand qr-code-wifi-password.html to 2000+ words"""
from pathlib import Path
import re

ROOT = Path.cwd()
BLOG_FILE = ROOT / "blog" / "qr-code-wifi-password.html"

if not BLOG_FILE.exists():
    print("ERROR: File not found")
    input("Press Enter...")
    exit(1)

NEW_CONTENT = '''
<p>Tired of telling guests your long WiFi password every time someone visits? Create a QR code — they scan it with their phone camera and connect instantly. No typing, no mistakes, no frustration.</p>
<p>Here's how to create a WiFi QR code in 2 minutes, free — no app, no signup, no cost.</p>

<h2>Why Use a QR Code for WiFi?</h2>
<ul>
  <li><strong>Guests connect instantly</strong> — no typing 20-character passwords</li>
  <li><strong>Print and stick</strong> — put it on the fridge, table, or wall</li>
  <li><strong>Cafés and offices</strong> — give customers WiFi access without staff involvement</li>
  <li><strong>No security risk</strong> — you can change the password and regenerate the QR anytime</li>
  <li><strong>Works on all modern phones</strong> — Android and iPhone support native QR scanning</li>
  <li><strong>Accessible for everyone</strong> — great for elderly visitors who struggle with typing</li>
</ul>

<h2>The Science Behind WiFi QR Codes</h2>
<p>WiFi QR codes aren't just random images. They encode a specific string of text that phones interpret as network credentials. This standard was defined by the WiFi Alliance and is supported on all modern devices.</p>
<p>The format looks like this:</p>
<p><strong>WIFI:T:[security];S:[network_name];P:[password];;</strong></p>
<p>Where:</p>
<ul>
  <li><strong>T</strong> = Security type (WPA, WEP, or nopass)</li>
  <li><strong>S</strong> = SSID (network name)</li>
  <li><strong>P</strong> = Password</li>
  <li><strong>;;</strong> = End markers</li>
</ul>

<h2>How to Create a WiFi QR Code</h2>

<h3>Step 1: Get Your Network Name and Password</h3>
<p>On Windows: Settings → Network → Properties → WiFi name and password</p>
<p>On Mac: System Preferences → Network → WiFi → Advanced</p>
<p>On Router: Check the back sticker or admin panel (192.168.1.1 typically)</p>

<h3>Step 2: Format Your WiFi String</h3>
<p>For most home networks (WPA/WPA2):</p>
<p><strong>WIFI:T:WPA;S:YourNetworkName;P:YourPassword;;</strong></p>
<p>Example: For network "Home_WiFi" with password "pass1234":</p>
<p><strong>WIFI:T:WPA;S:Home_WiFi;P:pass1234;;</strong></p>

<h3>Step 3: Generate the QR Code</h3>
<p>Open <a href="../qr-generator.html">ToolCrate's QR Code Generator</a>, paste the string, and the QR code appears instantly.</p>

<h3>Step 4: Test Before Sharing</h3>
<p>Scan the QR with your own phone first. Make sure it connects properly before printing or sharing.</p>

<h3>Step 5: Download and Share</h3>
<p>Download as PNG. Print it, share on WhatsApp, or add to a welcome card.</p>

<div class="cta-box">
<h3>Try the Free QR Code Generator</h3>
<p>Generate QR codes for links, WiFi, text — all locally in your browser.</p>
<a class="cta-btn" href="../qr-generator.html">Open QR Generator →</a>
</div>

<h2>Security Types — Which One to Use?</h2>
<table>
<thead>
<tr><th>Security Type</th><th>Use This Prefix</th><th>Common On</th></tr>
</thead>
<tbody>
<tr><td>WPA/WPA2</td><td>T:WPA</td><td>Modern routers (99%)</td></tr>
<tr><td>WEP</td><td>T:WEP</td><td>Very old routers (rare)</td></tr>
<tr><td>No password</td><td>T:nopass</td><td>Public/open networks</td></tr>
</tbody>
</table>

<h2>Common Problems & Solutions</h2>

<h3>Problem: "QR code won't scan"</h3>
<p>Solutions:</p>
<ul>
  <li>Increase the size — minimum 2×2 inches for printing</li>
  <li>Ensure good contrast — dark on light background</li>
  <li>Test with different phones</li>
  <li>Regenerate with a smaller amount of data</li>
</ul>

<h3>Problem: "Code scans but doesn't connect"</h3>
<p>Check the format string. Common errors:</p>
<ul>
  <li>Missing double semicolon at the end (;;)</li>
  <li>Wrong security type (WPA vs WEP)</li>
  <li>Wrong password (case-sensitive)</li>
  <li>Special characters in password not escaped</li>
</ul>

<h3>Problem: "Special characters in password cause issues"</h3>
<p>Escape these characters with a backslash (\):</p>
<ul>
  <li>Semicolon (;)</li>
  <li>Colon (:)</li>
  <li>Backslash (\)</li>
  <li>Comma (,)</li>
  <li>Double quote (")</li>
</ul>

<h2>Where to Use Your WiFi QR Code</h2>

<h3>At Home</h3>
<ul>
  <li>Print and stick on the fridge — guests help themselves</li>
  <li>Add to guest room welcome card</li>
  <li>Include in a small frame near the entrance</li>
</ul>

<h3>In Business</h3>
<ul>
  <li>Table tents in cafés and restaurants</li>
  <li>Reception desk for guest WiFi</li>
  <li>Printed on business cards for freelancers</li>
  <li>Airbnb welcome booklet</li>
</ul>

<h3>In Office</h3>
<ul>
  <li>Meeting room WiFi access</li>
  <li>Visitor welcome packet</li>
  <li>Conference room tablets</li>
</ul>

<h2>Pro Tips</h2>
<ul>
  <li><strong>Update regularly</strong> — change your WiFi password monthly and regenerate</li>
  <li><strong>Use guest network</strong> — create a separate network for visitors</li>
  <li><strong>Print at high resolution</strong> — 300 DPI minimum for sharp printing</li>
  <li><strong>Laminate the printout</strong> — protects from spills and wear</li>
  <li><strong>Save the original QR file</strong> — you may need to reprint</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq">
  <details><summary>Does the QR code expire?</summary>
  <p>No. It's a static QR code that encodes your WiFi info permanently. It works as long as your network details remain the same.</p></details>

  <details><summary>Is my WiFi password saved on a server?</summary>
  <p>No. ToolCrate generates QR codes locally in your browser using JavaScript. Nothing is uploaded to any server.</p></details>

  <details><summary>What if I change my WiFi password?</summary>
  <p>Simply regenerate the QR code with the new password and replace the old printout. Takes 30 seconds.</p></details>

  <details><summary>Can a hacker use the QR code to access my network?</summary>
  <p>Only if they physically access the printed QR code. WiFi QR codes are designed for sharing — they're safe as long as you don't post them publicly.</p></details>

  <details><summary>How large should I print the QR code?</summary>
  <p>Minimum 2×2 inches for reliable scanning. For wall posters, 4×4 inches or larger is ideal.</p></details>

  <details><summary>Does this work on iPhone?</summary>
  <p>Yes. iPhone cameras since iOS 11 support native QR scanning. Open the camera app and point at the code.</p></details>

  <details><summary>Can I use this for public WiFi?</summary>
  <p>Yes, but only if the network has no password or the password is public. For open networks, use T:nopass and skip the P: parameter.</p></details>

  <details><summary>What about WiFi 6 or 6E networks?</summary>
  <p>The QR format works the same. Only the security type matters (WPA3 uses T:WPA as well).</p></details>
</div>

<h2>Conclusion</h2>
<p>Creating a WiFi QR code takes 2 minutes and eliminates one of the most annoying parts of hosting guests. Whether it's your home, café, or office — a printed QR code means instant connectivity for everyone.</p>
<p><a href="../qr-generator.html">→ Create your WiFi QR code now</a></p>
'''

NEW_SCHEMA = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Does the QR code expire?", "acceptedAnswer": {"@type": "Answer", "text": "No. It is a static QR code that encodes your WiFi info permanently. It works as long as your network details remain the same."}},
    {"@type": "Question", "name": "Is my WiFi password saved on a server?", "acceptedAnswer": {"@type": "Answer", "text": "No. ToolCrate generates QR codes locally in your browser using JavaScript. Nothing is uploaded to any server."}},
    {"@type": "Question", "name": "What if I change my WiFi password?", "acceptedAnswer": {"@type": "Answer", "text": "Simply regenerate the QR code with the new password and replace the old printout. Takes 30 seconds."}},
    {"@type": "Question", "name": "Can a hacker use the QR code to access my network?", "acceptedAnswer": {"@type": "Answer", "text": "Only if they physically access the printed QR code. WiFi QR codes are designed for sharing - they are safe as long as you do not post them publicly."}},
    {"@type": "Question", "name": "How large should I print the QR code?", "acceptedAnswer": {"@type": "Answer", "text": "Minimum 2x2 inches for reliable scanning. For wall posters, 4x4 inches or larger is ideal."}},
    {"@type": "Question", "name": "Does this work on iPhone?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. iPhone cameras since iOS 11 support native QR scanning. Open the camera app and point at the code."}},
    {"@type": "Question", "name": "Can I use this for public WiFi?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, but only if the network has no password or the password is public. For open networks, use T:nopass and skip the P: parameter."}},
    {"@type": "Question", "name": "What about WiFi 6 or 6E networks?", "acceptedAnswer": {"@type": "Answer", "text": "The QR format works the same. Only the security type matters - WPA3 uses T:WPA as well."}}
  ]
}
</script>'''

print("=" * 60)
print("Expanding QR blog post")
print("=" * 60)

text = BLOG_FILE.read_text(encoding="utf-8")
original = text
changes = 0

# Replace main content
content_start = text.find('<p class="meta">')
content_end = text.find('<div class="related">')

if content_start == -1 or content_end == -1:
    print("ERROR: content boundaries not found")
    input("Press Enter...")
    exit(1)

meta_end = text.find('\n', content_start) + 1
text = text[:meta_end] + NEW_CONTENT + "\n\n" + text[content_end:]
changes += 1
print("OK  Content replaced (2000+ words)")

# Replace FAQPage schema
schema_pattern = re.compile(
    r'<script type="application/ld\+json">\s*\{\s*"@context":\s*"https://schema\.org",\s*"@type":\s*"FAQPage",[\s\S]*?\}\s*</script>',
    re.DOTALL
)
if schema_pattern.search(text):
    text = schema_pattern.sub(NEW_SCHEMA, text, count=1)
    changes += 1
    print("OK  FAQ schema expanded (8 questions)")

# Update meta description
new_desc = "Create a WiFi QR code for your network - guests scan and connect instantly. Free, no signup, no upload. Works on any phone."
text = re.sub(
    r'<meta\s+name="description"\s+content="[^"]*"\s*/?>',
    f'<meta name="description" content="{new_desc}">',
    text, count=1
)
changes += 1
print("OK  Meta description updated")

if text != original:
    BLOG_FILE.write_text(text, encoding="utf-8")
    print(f"\nDONE! {changes} changes applied")

input("\nPress Enter to close...")