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