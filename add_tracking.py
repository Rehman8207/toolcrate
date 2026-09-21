#!/usr/bin/env python3
"""
Add GA4 custom event tracking to track user actions:
- tool_used: when a user actually uses a tool
- blog_scroll: when a user scrolls 75% of a blog post
- search_used: when a user searches on homepage
- theme_toggle: when a user switches theme
"""
from pathlib import Path

ROOT = Path.cwd()
COMMON_JS = ROOT / "assets" / "common.js"

if not COMMON_JS.exists():
    print("❌ assets/common.js not found")
    input("Press Enter...")
    exit(1)

TRACKING_CODE = """

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
  var toolMatch = path.match(/([a-z-]+)\\.html$/);
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
"""

# Append to common.js
text = COMMON_JS.read_text(encoding="utf-8")

if "GA4 CUSTOM EVENT TRACKING" in text:
    print("⏭️  Tracking code already exists in common.js")
else:
    text += TRACKING_CODE
    COMMON_JS.write_text(text, encoding="utf-8")
    print("✅ assets/common.js — tracking code added")
    print()
    print("Events being tracked:")
    print("  • theme_toggle    — light/dark switch")
    print("  • search_used     — homepage search (>=3 chars)")
    print("  • category_filter — chip clicks")
    print("  • tool_used       — first input/click in tool panel")
    print("  • blog_read       — 75% scroll on blog posts")

print()
print("=" * 60)
print("DONE!")
print("=" * 60)
print()
print("Next steps:")
print("  1. python -m http.server 8000")
print("  2. Open site and use a tool")
print("  3. GA4 → Reports → Realtime → should show events")
print("  4. Wait 24 hours for events to show in Engagement tab")
print()
input("Press Enter to close...")