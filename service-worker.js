/* ============================================================
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
