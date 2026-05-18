/**
 * TasGloss — THE ALIEN SCHOOL Archive Glossary System
 * Mobile-first layered insight tool for the Synthesis Archive.
 *
 * HOW TO USE ON ANY PAGE:
 *   1. Link <link rel="stylesheet" href="tas-glossary.css"> in <head>
 *   2. Add the sheet HTML before </body> (see index.html for reference)
 *   3. Add <script src="tas-glossary.js" defer></script> before </body>
 *   4. Mark terms in the text:
 *
 *   <span class="tas-term"
 *     tabindex="0"
 *     role="button"
 *     data-term="Display Name"
 *     data-short="Entry definition — Layer 1 of the glossary."
 *     data-category="CONCEPT"
 *     data-href="/glossary#slug">   ← optional: add when glossary exists
 *   >Term text</span>
 *
 * DEPTH LAYERS:
 *   data-short    → Layer 1: entry definition (shown in sheet)
 *   data-href     → Layer 2: link to full glossary article
 *   (Layer 3 lives inside the glossary article, linking to reports)
 */

const TasGloss = (() => {
  // DOM refs — populated on DOMContentLoaded
  let sheet, overlay, elTermName, elCat, elDef, elMore, elDepth;
  let activeTermEl = null;

  const isFinePointer = () =>
    window.matchMedia('(hover: hover) and (pointer: fine) and (min-width: 769px)').matches;

  // ── Init ────────────────────────────────────────────────────────
  function init() {
    sheet      = document.getElementById('tas-gloss-sheet');
    overlay    = document.getElementById('tas-gloss-overlay');
    elTermName = document.getElementById('tas-gloss-term-name');
    elCat      = document.getElementById('tas-gloss-category');
    elDef      = document.getElementById('tas-gloss-def');
    elMore     = document.getElementById('tas-gloss-more');
    elDepth    = document.getElementById('tas-gloss-depth');

    if (!sheet) return;

    // Delegated click/tap: any .tas-term anywhere on the page
    document.addEventListener('click', e => {
      const term = e.target.closest('.tas-term');
      if (term) {
        e.preventDefault();
        e.stopPropagation();
        // Toggle: tap the same open term to close
        if (activeTermEl === term && sheet.classList.contains('is-open')) {
          close();
        } else {
          open(term);
        }
        return;
      }
      // Tap outside the sheet to close
      if (sheet.classList.contains('is-open') && !sheet.contains(e.target)) {
        close();
      }
    });

    // Keyboard: Enter or Space on focused term, Escape to close
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') { close(); return; }
      const focused = document.activeElement;
      if (focused && focused.classList.contains('tas-term')) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          if (activeTermEl === focused && sheet.classList.contains('is-open')) {
            close();
          } else {
            open(focused);
          }
        }
      }
    });

    // Swipe down to close on touch (gesture feel)
    let touchStartY = 0;
    let isSwiping = false;
    sheet.addEventListener('touchstart', e => {
      touchStartY = e.touches[0].clientY;
      isSwiping = false;
    }, { passive: true });
    sheet.addEventListener('touchmove', e => {
      const dy = e.touches[0].clientY - touchStartY;
      if (dy > 12) isSwiping = true;
      if (dy > 72) close();
    }, { passive: true });
    sheet.addEventListener('touchend', () => { isSwiping = false; }, { passive: true });
  }

  // ── Open ────────────────────────────────────────────────────────
  function open(termEl) {
    if (!sheet) return;

    // Populate content from data attributes
    const termText = termEl.dataset.term
      || termEl.textContent.replace(/∴\s*$/, '').trim();
    const shortDef  = termEl.dataset.short    || '';
    const category  = termEl.dataset.category || 'CONCEPT';
    const href      = termEl.dataset.href     || null;

    elTermName.textContent = termText;
    elDef.textContent      = shortDef;
    elCat.textContent      = category;

    if (href) {
      elMore.href         = href;
      elMore.style.display = '';
      if (elDepth) elDepth.textContent = '∴ LAYER 1 · ENTRY DEFINITION — GLOSSARY AVAILABLE';
    } else {
      elMore.style.display = 'none';
      if (elDepth) elDepth.textContent = '∴ LAYER 1 · ENTRY DEFINITION — FULL GLOSSARY COMING';
    }

    // Track active term (for toggle, focus restoration on close)
    if (activeTermEl) activeTermEl.removeAttribute('aria-expanded');
    activeTermEl = termEl;
    termEl.setAttribute('aria-expanded', 'true');

    // Desktop: position the floating panel near the term
    if (isFinePointer()) positionNear(termEl);

    // Open with animation tick for position to apply first
    requestAnimationFrame(() => {
      sheet.classList.add('is-open');
      sheet.removeAttribute('aria-hidden');
      if (overlay) overlay.classList.add('is-open');
    });
  }

  // ── Position (desktop) ──────────────────────────────────────────
  function positionNear(termEl) {
    const r          = termEl.getBoundingClientRect();
    const panelW     = 340;
    const panelH     = 240; // approximate — sheet is max-height 50vh
    const margin     = 16;

    let left = r.left + window.scrollX;
    let top  = r.bottom + window.scrollY + 10;

    // Don't bleed off right edge
    if (left + panelW > window.innerWidth - margin) {
      left = Math.max(margin, window.innerWidth - panelW - margin);
    }

    // Flip above term if not enough room below
    if (r.bottom + panelH + 10 > window.innerHeight) {
      top = Math.max(
        window.scrollY + margin,
        r.top + window.scrollY - panelH - 10
      );
    }

    Object.assign(sheet.style, {
      left:        left + 'px',
      top:         top + 'px',
      bottom:      'auto',
      right:       'auto',
      maxWidth:    panelW + 'px',
      borderRadius: '6px',
      transform:   'none',
    });
  }

  // ── Close ───────────────────────────────────────────────────────
  function close() {
    if (!sheet) return;
    sheet.classList.remove('is-open');
    sheet.setAttribute('aria-hidden', 'true');
    if (overlay) overlay.classList.remove('is-open');

    if (activeTermEl) {
      activeTermEl.removeAttribute('aria-expanded');
      // Return focus to the term that opened the sheet
      activeTermEl.focus({ preventScroll: true });
      activeTermEl = null;
    }

    // Reset inline styles added for desktop positioning
    if (isFinePointer()) {
      ['left', 'top', 'bottom', 'right', 'maxWidth', 'borderRadius', 'transform']
        .forEach(p => sheet.style.removeProperty(p));
    }
  }

  document.addEventListener('DOMContentLoaded', init);
  return { open, close };
})();
