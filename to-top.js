/* Shared "Back to top" button for DirtSprintCars.com. Adds one small round button
   (bottom right) that appears after scrolling. Pages that already include their own
   #to-top button (index.html, results.html) are skipped so there is never a duplicate. */
(function () {
  if (document.getElementById('to-top')) return;
  var css = '.to-top{position:fixed;right:20px;bottom:20px;z-index:40;width:48px;height:48px;border:0;border-radius:50%;background:#d6262b;color:#fff;font-size:22px;line-height:1;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.5);opacity:0;visibility:hidden;transition:opacity .2s,visibility .2s;padding:0}' +
    '.to-top.show{opacity:1;visibility:visible}.to-top:hover{background:#ff4d4f}' +
    '.to-top:focus-visible{outline:2px solid #fff;outline-offset:2px}' +
    '.to-top.up{bottom:70px}' +
    '@media (max-width:640px){.to-top{right:14px;bottom:14px;width:44px;height:44px}.to-top.up{bottom:64px}}' +
    '@media print{.to-top{display:none}}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);
  var b = document.createElement('button');
  b.type = 'button';
  b.id = 'to-top';
  b.className = 'to-top';
  b.setAttribute('aria-label', 'Back to top');
  b.title = 'Back to top';
  b.innerHTML = '&uarr;';
  /* Sit above the "Jump to today" button on This Day in History. */
  if (document.getElementById('jt')) b.className += ' up';
  document.body.appendChild(b);
  function u() { b.classList.toggle('show', window.scrollY > 400); }
  window.addEventListener('scroll', u, { passive: true });
  u();
  b.addEventListener('click', function () {
    var rm = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    window.scrollTo({ top: 0, behavior: rm ? 'auto' : 'smooth' });
  });
})();
