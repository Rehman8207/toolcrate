#!/usr/bin/env python3
"""Create new blog post: compress-jpg-to-50kb.html"""
from pathlib import Path
import re

ROOT = Path.cwd()
BLOG = ROOT / "blog"
BLOG_INDEX = BLOG / "index.html"
SITEMAP = ROOT / "sitemap.xml"

TITLE = "Compress JPG to 50KB Online — Free, No Upload | ToolCrate"
DESC = "Compress any JPG image to under 50KB without losing quality. Free browser-based tool, no signup, works on mobile and desktop."

CONTENT = '''
<p>Many online forms, university portals, and government websites require photos to be under <strong>50KB</strong>. Modern phone cameras produce images of 3-5MB — 100 times larger than allowed. Here's how to fix it in 30 seconds.</p>

<h2>Why 50KB?</h2>
<p>File size limits exist because uploading servers need to process thousands of applications. Common requirements in Pakistan and India:</p>
<ul>
  <li><strong>University admissions:</strong> 20KB-50KB photos</li>
  <li><strong>Government jobs (NTS, PPSC, FPSC):</strong> 30KB-50KB</li>
  <li><strong>Online visa forms:</strong> 50KB-100KB</li>
  <li><strong>Bank KYC updates:</strong> 20KB-50KB</li>
  <li><strong>Examination registrations:</strong> 50KB</li>
</ul>

<h2>How to Compress JPG to 50KB</h2>

<h3>Step 1: Open the ToolCrate Image Compressor</h3>
<p>Go to <a href="../image-compressor.html">ToolCrate's Image Compressor</a>. No signup needed.</p>

<h3>Step 2: Upload Your JPG</h3>
<p>Drag your file into the browser or click to select.</p>

<h3>Step 3: Adjust Quality to Hit 50KB</h3>
<p>Slide quality down. Watch the live size indicator. Typically 40-60% quality hits 50KB for standard passport photos.</p>

<h3>Step 4: Preview and Download</h3>
<p>Check the side-by-side preview. If quality is acceptable, download.</p>

<div class="cta-box">
<h3>Try the Free Image Compressor</h3>
<p>Reduce any image to any size — free, private, browser-based.</p>
<a class="cta-btn" href="../image-compressor.html">Open Image Compressor →</a>
</div>

<h2>Recommended Photo Dimensions</h2>
<table>
<thead>
<tr><th>Use Case</th><th>Dimensions</th><th>File Size</th></tr>
</thead>
<tbody>
<tr><td>Passport photo</td><td>200×230 px</td><td>50KB</td></tr>
<tr><td>Signature</td><td>140×60 px</td><td>20KB</td></tr>
<tr><td>Profile picture</td><td>300×300 px</td><td>50KB</td></tr>
<tr><td>CNIC photo</td><td>350×450 px</td><td>50KB</td></tr>
</tbody>
</table>

<h2>Tips for Best Results</h2>
<ul>
  <li><strong>Resize first, then compress</strong> — reducing dimensions helps size too</li>
  <li><strong>Use JPEG</strong> — 5-10× smaller than PNG for photos</li>
  <li><strong>Don't compress twice</strong> — always start from original</li>
  <li><strong>Check the form requirements</strong> — some portals need exact dimensions</li>
</ul>

<h2>Frequently Asked Questions</h2>
<div class="faq">
  <details><summary>Can I compress JPG to 50KB without losing quality?</summary>
  <p>Yes. At 50-60% quality for standard photos, most people can't tell the difference visually. The key is not to over-compress.</p></details>

  <details><summary>Does this tool upload my image to a server?</summary>
  <p>No. All processing happens locally in your browser. Your images never leave your device.</p></details>

  <details><summary>What if 50KB is too small?</summary>
  <p>For most passport photos, 50KB is more than enough for sharp quality. Only high-resolution prints need larger files.</p></details>

  <details><summary>Can I use this for job applications?</summary>
  <p>Absolutely. Most Pakistani job portals (NTS, PPSC, FPSC) accept compressed photos under 50KB.</p></details>

  <details><summary>Which format is best for forms?</summary>
  <p>JPEG. It compresses 5-10× better than PNG for photos and is universally supported.</p></details>
</div>

<h2>Conclusion</h2>
<p>Compressing JPGs to 50KB doesn't require Photoshop or any paid software. ToolCrate's free tool does it in seconds, entirely in your browser.</p>
<p><a href="../image-compressor.html">→ Try the free Image Compressor now</a></p>
'''

NEW_POST = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="https://site.toolcrate-tools.workers.dev/blog/compress-jpg-to-50kb.html">
<meta name="theme-color" content="#0A1410">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:type" content="article">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../assets/style.css">
<link rel="stylesheet" href="../assets/mobile.css?v=2">
<link rel="stylesheet" href="../assets/responsive.css?v=1">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H20HJWJQWV"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-H20HJWJQWV');</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","headline":"{TITLE}","author":{{"@type":"Person","name":"Abdul Rehman"}},"publisher":{{"@type":"Organization","name":"ToolCrate"}},"datePublished":"2026-09-27"}}
</script>
<style>
  .article{{max-width:760px;margin:0 auto;padding:0 24px 60px}}
  .article .back-btn{{display:inline-flex;align-items:center;gap:6px;font-size:0.82rem;color:var(--ink-2);padding:8px 14px;border-radius:999px;background:var(--surface-2);border:1px solid var(--border);text-decoration:none;margin-bottom:24px;transition:all 0.2s}}
  .article .back-btn:hover{{color:var(--emerald);border-color:var(--emerald)}}
  .article .post-tag{{font-family:var(--font-mono);font-size:0.7rem;font-weight:600;text-transform:uppercase;letter-spacing:0.06em;color:var(--emerald);padding:5px 12px;border-radius:999px;background:rgba(16,185,129,0.12);border:1px solid rgba(16,185,129,0.25);display:inline-block}}
  .article h1{{font-family:var(--font-display);font-size:clamp(1.8rem,4vw,2.4rem);font-weight:700;letter-spacing:-0.03em;line-height:1.15;margin:16px 0 12px;color:var(--ink)}}
  .article .meta{{font-family:var(--font-mono);font-size:0.78rem;color:var(--ink-3);margin-bottom:32px;padding-bottom:20px;border-bottom:1px solid var(--border)}}
  .article h2{{font-family:var(--font-display);font-size:1.5rem;font-weight:700;margin:40px 0 12px;color:var(--ink)}}
  .article h3{{font-family:var(--font-display);font-size:1.15rem;font-weight:600;margin:28px 0 10px;color:var(--ink)}}
  .article p{{font-size:1rem;color:var(--ink-2);line-height:1.75;margin-bottom:16px}}
  .article ul,.article ol{{padding-left:22px;margin-bottom:20px}}
  .article li{{font-size:1rem;color:var(--ink-2);line-height:1.75;margin-bottom:8px}}
  .article strong{{color:var(--ink);font-weight:600}}
  .article a{{color:var(--emerald);text-decoration:underline;text-underline-offset:3px;font-weight:500}}
  .article table{{width:100%;border-collapse:collapse;margin:20px 0;font-size:0.9rem;border:1px solid var(--border);border-radius:10px;overflow:hidden}}
  .article th{{background:var(--surface-2);color:var(--emerald);font-weight:600;text-align:left;padding:12px 16px}}
  .article td{{padding:10px 16px;border-bottom:1px solid var(--border);color:var(--ink-2)}}
  .article .cta-box{{background:var(--surface-2);border:1px solid rgba(16,185,129,0.3);border-radius:14px;padding:24px;margin:28px 0;text-align:center;position:relative;overflow:hidden}}
  .article .cta-box::before{{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:var(--grad-a)}}
  .article .cta-box h3{{margin:0 0 8px}}
  .article .cta-btn{{display:inline-block;background:var(--grad-a);color:#fff;padding:12px 26px;border-radius:10px;font-weight:600;text-decoration:none;font-family:var(--font-display);font-size:0.9rem}}
  .article .related{{margin-top:48px;padding-top:28px;border-top:1px solid var(--border)}}
  .article .faq details{{background:var(--surface-2);border:1px solid var(--border);border-radius:10px;margin-bottom:10px;padding:14px 18px}}
  .article .faq summary{{font-weight:600;cursor:pointer;color:var(--ink)}}
  .article .faq p{{margin-top:8px;font-size:0.9rem}}
</style>
</head>
<body>
<div class="wrap">
<header class="masthead">
<div class="row">
<div class="brand-block"><div><div class="brand"><h1><a href="../index.html">ToolCrate</a></h1></div></div></div>
<button class="theme-toggle" id="themeToggle" type="button">Light</button>
</div>
</header>
<main>
<article class="article">
<a class="back-btn" href="index.html">Back to blog</a>
<span class="post-tag">Image Tools</span>
<h1>Compress JPG to 50KB Online</h1>
<p class="meta">Published Sep 27, 2026 - 4 min read</p>
{CONTENT}
<div class="related">
<h3>Related tools</h3>
<ul>
<li><a href="../image-compressor.html">Image Compressor</a></li>
<li><a href="compress-jpg-to-100kb.html">Compress JPG to 100KB</a></li>
<li><a href="index.html">View all blog posts</a></li>
</ul>
</div>
</article>
</main>
<footer>
<span>ToolCrate</span>
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

print("=" * 60)
print("Creating new blog post")
print("=" * 60)
print()

# Write new post
post_path = BLOG / "compress-jpg-to-50kb.html"
if post_path.exists():
    print("SKIP: Post already exists")
else:
    post_path.write_text(NEW_POST, encoding="utf-8")
    print("OK  Created: blog/compress-jpg-to-50kb.html")

# Update blog/index.html
index_text = BLOG_INDEX.read_text(encoding="utf-8")
if "compress-jpg-to-50kb" in index_text:
    print("SKIP: Card already exists")
else:
    new_card = '''
  <a class="post-card" href="compress-jpg-to-50kb.html">
    <span class="post-tag">Image Tools</span>
    <h2>Compress JPG to 50KB Online</h2>
    <p>Reduce any JPG image to under 50KB for online forms, job applications, and university portals.</p>
    <div class="post-meta">
      <span>Sep 27, 2026</span>
      <span class="read-more">Read</span>
    </div>
  </a>
'''
    grid_match = re.search(r'(<section class="blog-grid">)(.*?)(</section>)', index_text, re.DOTALL)
    if grid_match:
        insertion = grid_match.group(2).rstrip() + "\n" + new_card
        index_text = index_text[:grid_match.start(2)] + insertion + index_text[grid_match.end(2):]
        BLOG_INDEX.write_text(index_text, encoding="utf-8")
        print("OK  Card added to blog/index.html")

# Update sitemap
sitemap_text = SITEMAP.read_text(encoding="utf-8")
new_url = 'https://site.toolcrate-tools.workers.dev/blog/compress-jpg-to-50kb.html'
if new_url in sitemap_text:
    print("SKIP: URL already in sitemap")
else:
    url_entry = f'  <url>\n    <loc>{new_url}</loc>\n    <lastmod>2026-09-27</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    sitemap_text = sitemap_text.replace('</urlset>', url_entry + '</urlset>')
    SITEMAP.write_text(sitemap_text, encoding="utf-8")
    print("OK  URL added to sitemap.xml")

print()
print("DONE!")
input("Press Enter to close...")