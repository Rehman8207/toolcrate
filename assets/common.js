(function(){
  "use strict";
  var themeBtn = document.getElementById('themeToggle');
  if(!themeBtn) return;
  function applyTheme(t){
    if(t){ document.documentElement.setAttribute('data-theme', t); }
    else { document.documentElement.removeAttribute('data-theme'); }
    themeBtn.textContent = (t === 'dark') ? 'Light mode' : 'Dark mode';
  }
  var savedTheme = null;
  try { savedTheme = localStorage.getItem('toolcrate-theme'); } catch(e){}
  applyTheme(savedTheme);
  themeBtn.addEventListener('click', function(){
    var current = document.documentElement.getAttribute('data-theme');
    var next = current === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    try { localStorage.setItem('toolcrate-theme', next); } catch(e){}
  });
})();
