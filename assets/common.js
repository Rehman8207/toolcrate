(function(){
  "use strict";
  var STORAGE_KEY='toolcrate-theme';
  var html=document.documentElement;
  var toggle=document.getElementById('themeToggle');
  function applyTheme(theme){
    if(theme==='light'){html.setAttribute('data-theme','light');if(toggle)toggle.textContent='🌙 Dark';}
    else{html.removeAttribute('data-theme');if(toggle)toggle.textContent='☀️ Light';}
  }
  var saved=localStorage.getItem(STORAGE_KEY);
  applyTheme(saved||'dark');
  if(toggle){
    toggle.addEventListener('click',function(){
      var isLight=html.getAttribute('data-theme')==='light';
      var next=isLight?'dark':'light';
      applyTheme(next);
      localStorage.setItem(STORAGE_KEY,next);
    });
  }
})();

/* ============================================================
   GA4 CUSTOM EVENT TRACKING
   ============================================================ */

(function() {
  'use strict';

  // Wait for gtag to load
  function trackEvent(eventName, params) {
    if (typeof gtag === 'function') {
      gtag('event', eventName, params || {});
    }
  }

  // ---------- Track theme toggle ----------
  var themeBtn = document.getElementById('themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', function() {
      trackEvent('theme_toggle', {
        'new_theme': document.documentElement.getAttribute('data-theme') === 'light' ? 'dark' : 'light'
      });
    });
  }

  // ---------- Track homepage search ----------
  var searchInput = document.getElementById('toolSearch');
  if (searchInput) {
    var searchTimeout = null;
    var searchFired = false;
    searchInput.addEventListener('input', function() {
      clearTimeout(searchTimeout);
      searchFired = false;
      searchTimeout = setTimeout(function() {
        if (!searchFired && searchInput.value.length >= 3) {
          searchFired = true;
          trackEvent('search_used', {
            'search_term': searchInput.value.trim().substring(0, 50)
          });
        }
      }, 1500);
    });
  }

  // ---------- Track category filter clicks ----------
  var categoryRail = document.getElementById('categoryRail');
  if (categoryRail) {
    categoryRail.addEventListener('click', function(e) {
      var chip = e.target.closest('[data-cat]');
      if (chip && chip.tagName !== 'A') {
        trackEvent('category_filter', {
          'category': chip.getAttribute('data-cat')
        });
      }
    });
  }

  // ---------- Track tool usage (page-specific) ----------
  // Detect which tool page we're on
  var path = window.location.pathname;
  var toolMatch = path.match(/([a-z-]+)\.html$/);
  if (toolMatch && toolMatch[1] !== 'index' && toolMatch[1] !== 'about' && toolMatch[1] !== 'contact' && toolMatch[1] !== 'privacy') {
    var toolName = toolMatch[1];
    // Fire on first meaningful interaction (input or click in the tool panel)
    var panel = document.querySelector('.tool-panel');
    if (panel) {
      var fired = false;
      function fireToolUsed() {
        if (fired) return;
        fired = true;
        trackEvent('tool_used', { 'tool_name': toolName });
      }
      panel.addEventListener('input', fireToolUsed, { once: true });
      panel.addEventListener('change', fireToolUsed, { once: true });
      panel.addEventListener('click', function(e) {
        // Only if clicked inside panel-body (not back button)
        if (e.target.closest('.panel-body')) fireToolUsed();
      }, { once: true });
    }
  }

  // ---------- Track blog post reading (75% scroll) ----------
  if (path.indexOf('/blog/') === 0 && path !== '/blog/index.html' && path !== '/blog/') {
    var scrolled = false;
    function checkScroll() {
      if (scrolled) return;
      var scrollPercent = (window.scrollY + window.innerHeight) / document.documentElement.scrollHeight;
      if (scrollPercent >= 0.75) {
        scrolled = true;
        var slug = path.split('/').pop().replace('.html', '');
        trackEvent('blog_read', {
          'blog_post': slug,
          'engagement': 'deep_read'
        });
        window.removeEventListener('scroll', checkScroll);
      }
    }
    window.addEventListener('scroll', checkScroll, { passive: true });
  }

})();


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
        'To install ToolCrate as an app:\n\n' +
        '• Chrome/Edge desktop: Click the install icon (⊕) in the address bar\n' +
        '• Android Chrome: Menu (⋮) → "Add to Home screen"\n' +
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
