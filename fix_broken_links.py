#!/usr/bin/env python3
"""
Fix broken links from Bing report:
- Creates 4 missing blog posts
- Fixes _template.html placeholder
"""
from pathlib import Path

ROOT = Path.cwd()
BLOG = ROOT / "blog"

def make_blog_post(title, description, category, tool_name, tool_file, content_html):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | ToolCrate</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://site.toolcrate-tools.workers.dev/blog/{tool_file}.html">
<meta name="theme-color" content="#0A1410">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="article">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/style.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H20HJWJQWV"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-H20HJWJQWV');</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{title}","author":{{"@type":"Person","name":"Abdul Rehman"}},"publisher":{{"@type":"Organization","name":"ToolCrate"}},"datePublished":"2026-09-21"}}
</script>
<style>
  .article{{max-width:760px;margin:0 auto;padding:0 24px 60px}}
  .article .back-btn{{display:inline-flex;align-items:center;gap:6px;font-size:0.82rem;color:var(--ink-2);padding:8px 14px;border-radius:999px;background:var(--surface-2);border:1px solid var(--border);text-decoration:none;margin-bottom:24px;transition:all 0.2s}}
  .article .back-btn:hover{{color:var(--emerald);border-color:var(--emerald)}}
  .article .post-tag{{font-family:var(--font-mono);font-size:0.7rem;font-weight:600;text-transform:uppercase;letter-spacing:0.06em;color:var(--emerald);padding:5px 12px;border-radius:999px;background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.25);display:inline-block}}
  .article h1{{font-family:var(--font-display);font-size:clamp(1.8rem,4vw,2.4rem);font-weight:700;letter-spacing:-0.03em;line-height:1.15;margin:16px 0 12px;color:var(--ink)}}
  .article .meta{{font-family:var(--font-mono);font-size:0.78rem;color:var(--ink-3);margin-bottom:32px;padding-bottom:20px;border-bottom:1px solid var(--border)}}
  .article h2{{font-family:var(--font-display);font-size:1.5rem;font-weight:700;letter-spacing:-0.02em;margin:40px 0 12px;color:var(--ink)}}
  .article h3{{font-family:var(--font-display);font-size:1.15rem;font-weight:600;margin:28px 0 10px;color:var(--ink)}}
  .article p{{font-size:1rem;color:var(--ink-2);line-height:1.75;margin-bottom:16px}}
  .article ul,.article ol{{padding-left:22px;margin-bottom:20px}}
  .article li{{font-size:1rem;color:var(--ink-2);line-height:1.75;margin-bottom:8px}}
  .article strong{{color:var(--ink);font-weight:600}}
  .article a{{color:var(--emerald);text-decoration:underline;text-underline-offset:3px;font-weight:500}}
  .article .cta-box{{background:var(--surface-2);border:1px solid rgba(16,185,129,0.3);border-radius:14px;padding:24px;margin:28px 0;text-align:center;position:relative;overflow:hidden}}
  .article .cta-box::before{{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--grad-a)}}
  .article .cta-box h3{{margin:0 0 8px}}
  .article .cta-btn{{display:inline-block;background:var(--grad-a);color:#fff;padding:12px 26px;border-radius:10px;font-weight:600;text-decoration:none;font-family:var(--font-display);font-size:0.9rem}}
  .article .related{{margin-top:48px;padding-top:28px;border-top:1px solid var(--border)}}
</style>
</head>
<body>
<div class="wrap">
<header class="masthead">
<div class="row">
<div class="brand-block"><div><div class="brand"><h1><a href="../index.html">ToolCrate</a></h1></div></div></div>
<button class="theme-toggle" id="themeToggle" type="button">☀️ Light</button>
</div>
</header>
<main>
<article class="article">
<a class="back-btn" href="index.html">← Back to blog</a>
<span class="post-tag">{category}</span>
<h1>{title}</h1>
<p class="meta">Published Sep 21, 2026 · 5 min read</p>
{content_html}
<div class="related">
<h3>Related tools</h3>
<ul>
<li><a href="../{tool_file}.html">{tool_name}</a></li>
<li><a href="index.html">View all blog posts →</a></li>
</ul>
</div>
</article>
</main>
<footer>
<span>ToolCrate — built for people, not ads.</span>
<nav class="footer-links">
<a href="../index.html">All tools</a>
<a href="index.html">Blog</a>
<a href="../about.html">About</a>
<a href="../contact.html">Contact</a>
<a href="../privacy.html">Privacy Policy</a>
</nav>
</footer>
</div>
<script src="../assets/common.js"></script>
</body>
</html>'''

post1_content = '''
<p>Most job portals require passport-size photos or documents to be under <strong>100KB</strong>. If your photo is 2-5MB (typical from modern phones), you can't upload it without compressing first.</p>
<p>Here's how to compress a JPG file to under 100KB — free, without signing up.</p>
<h2>Why 100KB?</h2>
<p>Government job portals, online application forms, and university admission sites enforce strict file size limits — usually 20KB-100KB for photos. This is because they process thousands of applications with limited storage.</p>
<h2>How to Compress JPG to 100KB</h2>
<h3>Step 1: Open ToolCrate Image Compressor</h3>
<p>Visit <a href="../image-compressor.html">ToolCrate's Image Compressor</a>. No signup, no ads.</p>
<h3>Step 2: Upload Your JPG</h3>
<p>Click the drop zone or drag your file in. JPG, PNG, and WebP formats supported.</p>
<h3>Step 3: Adjust Quality</h3>
<p>Slide quality down until the compressed file size drops below 100KB. The size updates live.</p>
<h3>Step 4: Download</h3>
<p>Click "Download compressed image" and use it for your application.</p>
<div class="cta-box">
<h3>Try the Free Image Compressor</h3>
<p>Compress any image to any size — free, private, browser-based.</p>
<a class="cta-btn" href="../image-compressor.html">Open Image Compressor →</a>
</div>
<h2>Tips for Job Applications</h2>
<ul>
<li><strong>Passport photo:</strong> Aim for 50KB-100KB, size 200x230 pixels</li>
<li><strong>Signature:</strong> 10KB-20KB, size 140x60 pixels</li>
<li><strong>Use JPEG format</strong> — compresses better than PNG for photos</li>
<li><strong>Don't compress multiple times</strong> — always from the original</li>
</ul>
<h2>Frequently Asked Questions</h2>
<h3>Does compression reduce photo quality?</h3>
<p>Not if done correctly. At 70-80% quality, most people can't tell the difference, and file sizes drop by 80-90%.</p>
<h3>Is this tool free?</h3>
<p>Yes, completely free. No signup, no hidden limits.</p>
'''

post2_content = '''
<p>Need to combine multiple PDF files into one? Maybe you have 5 separate invoices, scanned documents, or certificates that need to be submitted as a single PDF.</p>
<p>Here's how to merge PDFs free, without uploading your files to any server.</p>
<h2>Why Merge PDFs?</h2>
<ul>
<li><strong>Job applications:</strong> Combine degree, experience letter, and CNIC into one PDF</li>
<li><strong>Invoices:</strong> Send multiple invoices as one document</li>
<li><strong>Personal records:</strong> Keep related documents in one file</li>
<li><strong>Students:</strong> Submit assignments with all attachments together</li>
</ul>
<h2>How to Merge PDFs Free</h2>
<h3>Step 1: Open ToolCrate PDF Merger</h3>
<p>Go to <a href="../pdf-merge.html">ToolCrate's PDF Merger</a>. Runs 100% in your browser.</p>
<h3>Step 2: Upload Your PDFs</h3>
<p>Drag files in, select from your computer, or upload an entire folder.</p>
<h3>Step 3: Reorder Pages</h3>
<p>Unlike other tools, ToolCrate lets you drag individual pages to reorder them exactly as you want.</p>
<h3>Step 4: Merge and Download</h3>
<p>Click "Merge PDFs" and your combined document downloads instantly.</p>
<div class="cta-box">
<h3>Try the Free PDF Merger</h3>
<p>No signup, no uploads, no page limit.</p>
<a class="cta-btn" href="../pdf-merge.html">Open PDF Merger →</a>
</div>
<h2>Why Use ToolCrate's PDF Merger?</h2>
<ul>
<li><strong>No file uploads</strong> — your PDFs never leave your device</li>
<li><strong>Page reordering</strong> — drag to rearrange, delete, or rotate pages</li>
<li><strong>No page limit</strong> — merge 5 pages or 5000, no cap</li>
<li><strong>Free forever</strong> — no ads, no premium upsell</li>
</ul>
<h2>Frequently Asked Questions</h2>
<h3>Are my PDFs uploaded to a server?</h3>
<p>No. All merging happens client-side in your browser.</p>
<h3>Can I combine different-sized PDFs?</h3>
<p>Yes. Page sizes can vary, and each page keeps its original dimensions.</p>
'''

post3_content = '''
<p>Pakistani universities like NUST, FAST, LUMS, UET, and Punjab University use the 4.0 GPA scale. Understanding your CGPA is essential for job applications, higher studies, and scholarships.</p>
<p>Here's how to calculate your CGPA and how to extract your individual semester GPA from your result card.</p>
<h2>What is CGPA vs GPA?</h2>
<ul>
<li><strong>GPA</strong> = Grade Point Average for ONE semester</li>
<li><strong>CGPA</strong> = Cumulative Grade Point Average across ALL semesters</li>
</ul>
<p>Example: If you get 3.5 GPA in semester 1 and 3.7 GPA in semester 2, your CGPA after 2 semesters would be approximately 3.6.</p>
<h2>How to Calculate CGPA from Result Card</h2>
<h3>The Standard Formula</h3>
<p><strong>CGPA = (Sum of all quality points) ÷ (Sum of all credit hours)</strong></p>
<p>Quality points = Grade point × Credit hours for that course</p>
<h2>Extract Semester GPA from Result CGPA</h2>
<p>If your result card shows a new overall CGPA but not your individual semester GPA, use this formula:</p>
<p><strong>Semester GPA = [(New CGPA × Total Credits) − (Old CGPA × Old Credits)] ÷ Semester Credits</strong></p>
<div class="cta-box">
<h3>Try the CGPA & GPA Calculator</h3>
<p>Automatic calculation with multiple tools: extract semester GPA, plan target CGPA, calculate course-wise GPA.</p>
<a class="cta-btn" href="../cgpa-calculator.html">Open CGPA Calculator →</a>
</div>
<h2>4.0 GPA Scale in Pakistani Universities</h2>
<ul>
<li><strong>A / A+</strong> = 4.0 (90-100%)</li>
<li><strong>A-</strong> = 3.7 (85-89%)</li>
<li><strong>B+</strong> = 3.3 (80-84%)</li>
<li><strong>B</strong> = 3.0 (75-79%)</li>
<li><strong>B-</strong> = 2.7 (70-74%)</li>
<li><strong>C+</strong> = 2.3 (65-69%)</li>
<li><strong>C</strong> = 2.0 (60-64%)</li>
<li><strong>F</strong> = 0.0 (below 60%)</li>
</ul>
<h2>Frequently Asked Questions</h2>
<h3>Is CGPA 3.0 good in Pakistan?</h3>
<p>CGPA 3.0+ is considered good for most employers. For scholarships and top companies, aim for 3.5+.</p>
<h3>How can I raise my CGPA?</h3>
<p>Use our <a href="../cgpa-calculator.html">Target CGPA Planner</a> to calculate exactly what GPA you need in upcoming semesters.</p>
'''

post4_content = '''
<p>Tired of telling guests your long WiFi password every time someone visits? Create a QR code — they scan it with their phone camera and connect instantly.</p>
<p>Here's how, in 2 minutes, free.</p>
<h2>Why Use a QR Code for WiFi?</h2>
<ul>
<li><strong>Guests connect instantly</strong> — no typing 20-character passwords</li>
<li><strong>Print and stick</strong> — put it on the fridge or coffee table</li>
<li><strong>Cafés and offices</strong> — give customers WiFi access without staff involvement</li>
<li><strong>No security risk</strong> — you can change the password and QR anytime</li>
</ul>
<h2>How to Create a WiFi QR Code</h2>
<h3>Step 1: Format Your WiFi String</h3>
<p>WiFi QR codes need a specific format:</p>
<p><strong>WIFI:T:WPA;S:YourNetworkName;P:YourPassword;;</strong></p>
<p>Example: For network "Home_WiFi" with password "pass1234":<br>
WIFI:T:WPA;S:Home_WiFi;P:pass1234;;</p>
<h3>Step 2: Generate the QR Code</h3>
<p>Open <a href="../qr-generator.html">ToolCrate's QR Code Generator</a>, paste the string, and the QR code appears instantly.</p>
<h3>Step 3: Download and Share</h3>
<p>Download as PNG. Print it, share on WhatsApp, or add to a welcome card.</p>
<div class="cta-box">
<h3>Try the Free QR Code Generator</h3>
<p>Generate QR codes for links, WiFi, text — all locally.</p>
<a class="cta-btn" href="../qr-generator.html">Open QR Generator →</a>
</div>
<h2>Notes for Different Security Types</h2>
<ul>
<li><strong>WPA/WPA2:</strong> Use "T:WPA" (most common)</li>
<li><strong>WEP:</strong> Use "T:WEP" (older routers)</li>
<li><strong>No password:</strong> Use "T:nopass" and skip the P: part</li>
</ul>
<h2>Frequently Asked Questions</h2>
<h3>Does the QR code expire?</h3>
<p>No. It's a static QR code that encodes your WiFi info permanently.</p>
<h3>Is my WiFi password saved on a server?</h3>
<p>No. ToolCrate generates QR codes locally in your browser — nothing is uploaded.</p>
'''

print("=" * 70)
print("CREATING MISSING BLOG POSTS")
print("=" * 70)
print()

posts = [
    ("compress-jpg-to-100kb.html",
     "Compress JPG to 100KB for Job Applications",
     "How to compress a JPG file to under 100KB for job applications, university admissions, and government forms. Free browser-based tool, no signup.",
     "Image Tools", "Image Compressor", "image-compressor", post1_content),

    ("merge-pdf-free-online.html",
     "Merge PDF Files Free Online — No Upload, No Signup",
     "Combine multiple PDF files into one document with drag-to-reorder pages. 100% client-side, no signup, no uploads, no file limits.",
     "PDF Tools", "PDF Merger", "pdf-merge", post2_content),

    ("cgpa-calculator-pakistan.html",
     "CGPA Calculator for Pakistani Universities — Step by Step",
     "Calculate your CGPA and extract individual semester GPA from result card CGPA. Free online tool for Pakistani university students.",
     "Calculators", "CGPA & GPA Calculator", "cgpa-calculator", post3_content),

    ("qr-code-wifi-password.html",
     "How to Create a QR Code for Your WiFi Password (Free)",
     "Let guests connect to your WiFi instantly by scanning a QR code. Complete guide with the correct WiFi QR format and free generator.",
     "Developer Tools", "QR Code Generator", "qr-generator", post4_content),
]

for filename, title, desc, cat, tool_name, tool_file, content in posts:
    fp = BLOG / filename
    if fp.exists():
        print(f"   SKIP {filename} — already exists")
        continue
    html = make_blog_post(title, desc, cat, tool_name, tool_file, content)
    fp.write_text(html, encoding="utf-8")
    print(f"   OK   {filename}")
    print(f"        {title}")

print()
print("=" * 70)
print("FIXING _template.html")
print("=" * 70)
print()

template_fp = BLOG / "_template.html"
if template_fp.exists():
    text = template_fp.read_text(encoding="utf-8")
    original = text
    text = text.replace('../[TOOL].html', '#TOOL_LINK_GOES_HERE')
    text = text.replace('[TOOL NAME]', 'TOOL NAME')
    text = text.replace('[TOOL].html', '#TOOL_LINK_GOES_HERE')
    if text != original:
        template_fp.write_text(text, encoding="utf-8")
        print("   OK   _template.html — placeholders fixed")
    else:
        print("   SKIP _template.html — no changes needed")
else:
    print("   SKIP _template.html not found")

print()
print("=" * 70)
print("DONE!")
print("=" * 70)
print()
print("Files created:")
print("  blog/compress-jpg-to-100kb.html")
print("  blog/merge-pdf-free-online.html")
print("  blog/cgpa-calculator-pakistan.html")
print("  blog/qr-code-wifi-password.html")
print()
print("Verify:")
print("  python -m http.server 8000")
print("  Open: http://localhost:8000/blog/")
print()
input("Press Enter to close...")