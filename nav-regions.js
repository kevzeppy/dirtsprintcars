/* Regions nav dropdown and schedule country-filter helpers for DirtSprintCars.com.
   The dropdown uses the same details/summary pattern as the legends "jump to a series" list.
   Exports DSCRegions for the homepage schedule filter and for node tests. */
(function (root) {
  var SLUGS = {
    usa: 'USA',
    australia: 'Australia',
    'new-zealand': 'New Zealand',
    newzealand: 'New Zealand',
    nz: 'New Zealand'
  };

  function countryFromHash(hash) {
    var h = String(hash || '');
    if (h.charAt(0) === '#') h = h.slice(1);
    var m = h.match(/^schedule(?:-([a-z0-9-]+))?$/i);
    if (!m) return null;
    if (!m[1]) return 'All';
    return SLUGS[m[1].toLowerCase()] || null;
  }

  function countryMatch(eventCountry, filter) {
    if (!filter || filter === 'All') return true;
    return String(eventCountry || '').split(/\s*\/\s*/).indexOf(filter) !== -1;
  }

  function slugForCountry(country) {
    if (!country || country === 'All') return 'schedule';
    return 'schedule-' + String(country).toLowerCase().replace(/\s+/g, '-');
  }

  function wireDropdowns() {
    function closeAll(except) {
      var open = document.querySelectorAll('nav details.nav-drop[open]');
      for (var i = 0; i < open.length; i++) {
        if (open[i] !== except) open[i].removeAttribute('open');
      }
    }

    document.addEventListener('click', function (ev) {
      var drop = ev.target.closest && ev.target.closest('nav details.nav-drop');
      closeAll(drop || null);
      if (ev.target.closest && ev.target.closest('nav .nav-menu a')) closeAll();
    });

    document.addEventListener('keydown', function (ev) {
      if (ev.key !== 'Escape' && ev.key !== 'Esc') return;
      var open = document.querySelector('nav details.nav-drop[open]');
      if (!open) return;
      open.removeAttribute('open');
      var summary = open.querySelector('summary');
      if (summary) summary.focus();
    });
  }

  var api = {
    countryFromHash: countryFromHash,
    countryMatch: countryMatch,
    slugForCountry: slugForCountry
  };

  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  root.DSCRegions = api;

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', wireDropdowns);
    } else {
      wireDropdowns();
    }
  }
})(typeof window !== 'undefined' ? window : global);
