#!/usr/bin/env python3
"""
Convert ToolCrate into installable PWA (Progressive Web App).
- Creates manifest.json
- Creates service-worker.js
- Adds manifest link + SW registration to all HTML pages
- All tools already client-side, so offline works perfectly
"""
from pathlib import Path
import json
import re

ROOT = Path.cwd()

# ============================================================
# 1. manifest.json
# ============================================================
MANIFEST = {
    "name": "ToolCrate — 18+ Free Browser Tools",
    "short_name": "ToolCrate",
    "description": "18+ free browser tools that run entirely in your browser. No signup, no uploads, offline-ready.",
    "start_url": "/",
    "scope": "/",
    "display": "standalone",
    "orientation": "portrait-primary",
    "background_color": "#0A1410",
    "theme_color": "#0A1410",
    "categories": ["utilities", "productivity", "tools"],
    "lang": "en",
    "dir": "ltr",
    "icons": [
        {
            "src": "/assets/favicon.svg",
            "sizes": "any",
            "type": "image/svg+xml",
            "purpose": "any"
        },
        {
            "src": "/assets/favicon.svg",
            "sizes": "192x192",
            "type": "image/svg+xml",
            "purpose": "maskable"
        }
    ],
    "shortcuts": [
        {
            "name": "Word Counter",
            "url": "/word-counter.html",
            "description": "Count words, characters, and reading time"
        },
        {
            "name": "Image Compressor",
            "url": "/image-compressor.html",
            "description": "Compress images without uploading"
        },
        {
            "name": "PDF Merger",
            "url": "/pdf-merge.html",
            "description": "Merge PDFs with page control"
        },
        {
            "name": "QR Generator",
            "url": "/qr-generator.html",
            "description": "Create QR codes locally"
        }
    ]
}

# ============================================================
# 2. Service Worker
# ============================================================
SERVICE_WORKER = '''/* ============================================================
   ToolCrate Service Worker
   Provides offline support for all browser tools.
   ============================================================ */

const CACHE_NAME = 'toolcrate-v1';
const RUNTIME_CACHE = 'toolcrate-runtime-v1';

// Files to pre-cache on install (core pages + assets)
const PRECACHE_URLS = [
  '/',
  '/index.html',
  '/about.html',
  '/contact.html',
  '/privacy.html',
  '/blog/',
  '/blog/index.html',
  '/word-counter.html',
  '/case-converter.html',
  '/unit-converter.html',
  '/qr-generator.html',
  '/password-generator.html',
  '/image-compressor.html',
  '/json-formatter.html',
  '/age-calculator.html',
  '/discount-calculator.html',
  '/aggregate-calculator.html',
  '/meta-tag-generator.html',
  '/cgpa-calculator.html',
  '/currency-converter.html',
  '/image-to-pdf.html',
  '/watermark-tool.html',
  '/pdf-merge.html',
  '/pdf-to-text.html',
  '/text-to-pdf.html',
  '/assets/style.css',
  '/assets/common.js',
  '/assets/favicon.svg',
  '/manifest.json'
];

// Install — pre-cache everything
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(PRECACHE_URLS).catch(err => {
        console.warn('Pre-cache warning:', err);
      }))
      .then(() => self.skipWaiting())
  );
});

// Activate — clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME && name !== RUNTIME_CACHE)
          .map((name) => caches.delete(name))
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch — smart caching strategy
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Skip non-GET requests
  if (request.method !== 'GET') return;

  // Skip external domains (Google Analytics, fonts, CDNs)
  if (url.origin !== self.location.origin) return;

  // Skip Google Analytics and external APIs
  if (url.pathname.startsWith('/gtag/') ||
      url.pathname.startsWith('/collect') ||
      url.hostname.includes('google') ||
      url.hostname.includes('cloudflareinsights')) {
    return;
  }

  // HTML pages: Network-first (always get latest)
  if (request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const clone = response.clone();
          caches.open(RUNTIME_CACHE).then((cache) => cache.put(request, clone));
          return response;
        })
        .catch(() => caches.match(request).then(r => r || caches.match('/index.html')))
    );
    return;
  }

  // Assets (CSS, JS, images): Cache-first (fast, offline-ready)
  event.respondWith(
    caches.match(request).then((cached) => {
      if (cached) return cached;
      return fetch(request).then((response) => {
        // Cache successful responses
        if (response && response.status === 200) {
          const clone = response.clone();
          caches.open(RUNTIME_CACHE).then((cache) => cache.put(request, clone));
        }
        return response;
      }).catch(() => cached);
    })
  );
});
'''

# ============================================================
# 3. Add manifest + SW registration to HTML pages
# ============================================================
MANIFEST_LINK = '<link rel="manifest" href="/manifest.json">\n'
APPLE_META = '''<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="ToolCrate">
<meta name="mobile-web-app-capable" content="yes">
<meta name="application-name" content="ToolCrate">
'''

SW_REGISTER = '''<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/service-worker.js')
      .then(function(reg) { console.log('SW registered'); })
      .catch(function(err) { console.log('SW failed:', err); });
  });
}
</script>
'''

# ============================================================
# Process
# ============================================================
print("=" * 70)
print("Setting up PWA (Progressive Web App)")
print("=" * 70)
print()

# Write manifest.json
manifest_path = ROOT / "manifest.json"
manifest_path.write_text(json.dumps(MANIFEST, indent=2), encoding="utf-8")
print(f"OK  Created: manifest.json")

# Write service-worker.js
sw_path = ROOT / "service-worker.js"
sw_path.write_text(SERVICE_WORKER, encoding="utf-8")
print(f"OK  Created: service-worker.js")

# Update all HTML files
print()
print("Updating HTML pages...")
print()

all_html = list(ROOT.glob("*.html")) + list((ROOT / "blog").glob("*.html"))
updated = 0
skipped = 0

for fp in all_html:
    text = fp.read_text(encoding="utf-8", errors="ignore")
    original = text

    # Skip if already has manifest
    if 'rel="manifest"' in text:
        skipped += 1
        continue

    # Add manifest link + apple meta before </head>
    manifest_block = MANIFEST_LINK + APPLE_META

    if "</head>" in text:
        text = text.replace("</head>", manifest_block + "</head>", 1)

    # Add SW registration before </body>
    if "</body>" in text:
        text = text.replace("</body>", SW_REGISTER + "</body>", 1)

    if text != original:
        fp.write_text(text, encoding="utf-8")
        print(f"  OK  {fp.relative_to(ROOT)}")
        updated += 1
    else:
        skipped += 1

print()
print("=" * 70)
print(f"DONE! {updated} pages updated, {skipped} skipped")
print("=" * 70)
print()
print("What was added:")
print("  + manifest.json              (app info, icons, shortcuts)")
print("  + service-worker.js          (offline support)")
print(f"  + manifest + SW in {updated} HTML pages")
print()
print("Test locally:")
print("  python -m http.server 8000")
print("  Open Chrome → http://localhost:8000/")
print("  Should see install icon in address bar (⊕ or monitor icon)")
print()
print("Push:")
print("  git add .")
print('  git commit -m "Add PWA support — installable as app"')
print("  git push")
print()
input("Press Enter to close...")