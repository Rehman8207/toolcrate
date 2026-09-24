#!/usr/bin/env python3
"""
Add a visible 'Install App' button next to the theme toggle.
Uses beforeinstallprompt to trigger native install.
Hides button if already installed or not supported.
"""
from pathlib import Path
import re

ROOT = Path.cwd()
COMMON_JS = ROOT / "assets" / "common.js"
CSS = ROOT / "assets" / "style.css"

# ============================================================
# 1. Update common.js — Install button logic
# ============================================================
INSTALL_JS = """

/* ============================================================
   PWA INSTALL BUTTON
   ============================================================ */

(function() {
  'use strict';

  let deferredPrompt = null;
  const installBtn = document.getElementById('installAppBtn');

  if (!installBtn) return;

  // Hide button if already installed (standalone mode)
  if (window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true) {
    installBtn.style.display = 'none';
    return;
  }

  // Hide by default until browser fires the prompt event
  installBtn.style.display = 'none';

  // Browser ready to install
  window.addEventListener('beforeinstallprompt', function(e) {
    e.preventDefault();
    deferredPrompt = e;
    installBtn.style.display = 'inline-flex';
  });

  // User clicks install button
  installBtn.addEventListener('click', async function() {
    if (!deferredPrompt) {
      // Fallback: show manual instructions
      alert(
        'To install ToolCrate as an app:\\n\\n' +
        '• Chrome/Edge desktop: Click the install icon (⊕) in the address bar\\n' +
        '• Android Chrome: Menu (⋮) → "Add to Home screen"\\n' +
        '• iPhone Safari: Share → "Add to Home Screen"'
      );
      return;
    }

    deferredPrompt.prompt();
    const { outcome } = await deferredPrompt.userChoice;

    if (outcome === 'accepted') {
      installBtn.style.display = 'none';
    }

    deferredPrompt = null;
  });

  // Detect successful install
  window.addEventListener('appinstalled', function() {
    installBtn.style.display = 'none';
  });

  // iOS Safari — no beforeinstallprompt, so always show button
  const isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  if (isIOS && !window.navigator.standalone) {
    installBtn.style.display = 'inline-flex';
  }

  // Fallback for browsers that don't support beforeinstallprompt
  // Show button after 3 seconds if not fired
  setTimeout(function() {
    if (installBtn.style.display === 'none' && 'serviceWorker' in navigator) {
      // Only show if service worker is available but prompt didn't fire
      // This catches cases where install is possible but event didn't fire
      // We'll show but the click handler will show manual instructions
      installBtn.style.display = 'inline-flex';
    }
  }, 3000);

})();
"""

js_text = COMMON_JS.read_text(encoding="utf-8")

if "PWA INSTALL BUTTON" in js_text:
    print("SKIP — Install button code already exists in common.js")
else:
    js_text += INSTALL_JS
    COMMON_JS.write_text(js_text, encoding="utf-8")
    print("OK  common.js — install button logic added")

# ============================================================
# 2. Update CSS — Button styles
# ============================================================
INSTALL_CSS = """

/* ============================================================
   INSTALL APP BUTTON
   ============================================================ */

.install-app-btn {
  display: none; /* controlled by JS */
  align-items: center;
  gap: 6px;
  background: linear-gradient(135deg, rgba(16,185,129,0.15) 0%, rgba(59,130,246,0.10) 100%);
  border: 1px solid rgba(16,185,129,0.35);
  border-radius: var(--radius-full);
  padding: 9px 16px;
  font-family: var(--font-body);
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--emerald);
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  white-space: nowrap;
  margin-right: 10px;
}

.install-app-btn:hover {
  background: linear-gradient(135deg, rgba(16,185,129,0.25) 0%, rgba(59,130,246,0.18) 100%);
  border-color: var(--emerald);
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(16,185,129,0.25);
}

.install-app-btn:active {
  transform: translateY(0);
}

.install-app-btn svg {
  width: 15px;
  height: 15px;
  flex-shrink: 0;
}

@media (max-width: 640px) {
  .install-app-btn {
    padding: 8px 12px;
    font-size: 0.78rem;
    margin-right: 6px;
  }
  .install-app-btn span {
    display: none; /* icon only on mobile */
  }
  .install-app-btn {
    padding: 8px 10px;
  }
}
"""

css_text = CSS.read_text(encoding="utf-8")

if "INSTALL APP BUTTON" in css_text:
    print("SKIP — Install button CSS already exists")
else:
    css_text += INSTALL_CSS
    CSS.write_text(css_text, encoding="utf-8")
    print("OK  style.css — install button styles added")

# ============================================================
# 3. Add button HTML to all pages (before theme-toggle)
# ============================================================
print()
print("Adding install button to HTML pages...")
print()

INSTALL_BTN_HTML = '''<button class="install-app-btn" id="installAppBtn" type="button" aria-label="Install ToolCrate as app">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
<span>Install App</span>
</button>
'''

# Pattern to find the theme-toggle button in header
theme_btn_pattern = re.compile(
    r'(<button\s+class="theme-toggle"\s+id="themeToggle"\s+type="button">[^<]*</button>)',
    re.IGNORECASE
)

all_html = list(ROOT.glob("*.html")) + list((ROOT / "blog").glob("*.html"))
updated = 0
skipped = 0

for fp in all_html:
    text = fp.read_text(encoding="utf-8", errors="ignore")
    original = text

    # Skip if already has install button
    if 'installAppBtn' in text:
        skipped += 1
        continue

    # Insert install button BEFORE the theme toggle
    if theme_btn_pattern.search(text):
        text = theme_btn_pattern.sub(INSTALL_BTN_HTML + r'\1', text, count=1)
    else:
        print(f"  WARN — no theme-toggle found in {fp.name}")
        skipped += 1
        continue

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
print("Test locally:")
print("  python -m http.server 8000")
print("  Open http://localhost:8000/ in Chrome")
print("  Wait 3 seconds → Install App button should appear next to ☀️ Light")
print()
print("Push:")
print("  git add .")
print('  git commit -m "Add visible Install App button in header"')
print("  git push")
print()
input("Press Enter to close...")