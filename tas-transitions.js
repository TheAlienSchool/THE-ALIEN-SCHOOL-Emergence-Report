/* ============================================================
   tÅs PORTAL TRANSITION SYSTEM
   Handles cross-page navigation with:
     - Visual curtain (fade out / fade in)
     - Sonic fade-out (masterGain ramp) + departure chord
     - Automatic audio init bypass on portal entry
   All internal relative links are intercepted via capture phase.
   Pages expose window.audioCtx, window.masterGain, window.initializeSpace.
   ============================================================ */
(function () {
  'use strict';

  var PORTAL_KEY = 'tas_portal_entry';
  var FADE_MS    = 1200;

  // ── CURTAIN ───────────────────────────────────────────────────────────
  var curtain;

  function injectCurtain() {
    curtain = document.createElement('div');
    curtain.id = 'tas-curtain';
    curtain.style.cssText = [
      'position:fixed', 'inset:0', 'z-index:20000',
      'background:var(--h70-bg,#0c0c0c)',
      'opacity:0', 'pointer-events:none',
      'transition:opacity ' + FADE_MS + 'ms cubic-bezier(0.4,0,0.2,1)'
    ].join(';');
    document.body.appendChild(curtain);
  }

  // ── DEPARTURE CHORD ───────────────────────────────────────────────────
  // Three descending partials of 528Hz, staggered, dissolving.
  function playDepartureChord() {
    var ctx  = window.audioCtx;
    var gain = window.masterGain;
    if (!ctx || !gain || ctx.state !== 'running') return;

    [528, 396, 264].forEach(function (freq, i) {
      var osc = ctx.createOscillator();
      var vol = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.value = freq;
      var t = ctx.currentTime + i * 0.22;
      vol.gain.setValueAtTime(0, t);
      vol.gain.linearRampToValueAtTime(0.055, t + 0.08);
      vol.gain.exponentialRampToValueAtTime(0.001, t + 1.6);
      osc.connect(vol);
      vol.connect(gain);
      osc.start(t);
      osc.stop(t + 1.8);
    });
  }

  // ── NAVIGATION WITH TRANSITION ────────────────────────────────────────
  function navigateWithTransition(url) {
    var ctx  = window.audioCtx;
    var gain = window.masterGain;

    // Fade existing ambient soundscape to silence
    if (ctx && gain && ctx.state === 'running') {
      var now = ctx.currentTime;
      gain.gain.cancelScheduledValues(now);
      gain.gain.setValueAtTime(gain.gain.value, now);
      gain.gain.linearRampToValueAtTime(0, now + FADE_MS / 1000);
    }

    playDepartureChord();

    // Draw the curtain
    if (curtain) {
      curtain.style.pointerEvents = 'all';
      curtain.style.opacity       = '1';
    }

    sessionStorage.setItem(PORTAL_KEY, '1');
    setTimeout(function () { window.location.href = url; }, FADE_MS + 200);
  }

  window.tasNavigate = navigateWithTransition;

  // ── PORTAL ENTRY ──────────────────────────────────────────────────────
  // Called on the incoming page: curtain starts opaque then fades out,
  // audio initializes with a gain ramp from silence.
  function handlePortalEntry() {
    if (sessionStorage.getItem(PORTAL_KEY) !== '1') return;
    sessionStorage.removeItem(PORTAL_KEY);

    if (curtain) {
      curtain.style.transition    = 'none';
      curtain.style.opacity       = '1';
      curtain.style.pointerEvents = 'all';

      // Two rAF ticks ensure the opaque state paints before we transition
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          curtain.style.transition    = 'opacity ' + (FADE_MS + 200) + 'ms cubic-bezier(0.4,0,0.2,1)';
          curtain.style.opacity       = '0';
          curtain.style.pointerEvents = 'none';
        });
      });
    }

    // Auto-initialize audio; pass isPortalEntry=true so gain fades in from silence
    setTimeout(function () {
      if (typeof window.initializeSpace === 'function') {
        window.initializeSpace(true);
      }
    }, 120);
  }

  // ── INTERNAL LINK INTERCEPTOR ─────────────────────────────────────────
  // Capture phase fires before element handlers, so sonic feedback still plays.
  function interceptLinks() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest('a');
      if (!link) return;

      var href = link.getAttribute('href');
      if (!href) return;
      if (href.charAt(0) === '#') return;
      if (href.indexOf('http') === 0 || href.indexOf('//') === 0) return;
      if (href.indexOf('mailto:') === 0 || href.indexOf('tel:') === 0) return;
      if (link.target === '_blank') return;

      e.preventDefault();
      navigateWithTransition(href);
    }, true);
  }

  // ── BFCACHE RESTORE: reset curtain when browser navigates back/forward ──
  // Mobile browsers (Safari, Chrome iOS) aggressively cache pages. If the
  // curtain was opaque at the moment of departure, it will be restored that
  // way — producing a blank, unresponsive page on back navigation.
  window.addEventListener('pageshow', function (e) {
    if (e.persisted) {
      sessionStorage.removeItem(PORTAL_KEY);
      if (curtain) {
        curtain.style.transition    = 'none';
        curtain.style.opacity       = '0';
        curtain.style.pointerEvents = 'none';
      }
    }
  });

  // ── INIT ──────────────────────────────────────────────────────────────
  document.addEventListener('DOMContentLoaded', function () {
    injectCurtain();
    handlePortalEntry();
    interceptLinks();
  });

})();
