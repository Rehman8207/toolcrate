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



