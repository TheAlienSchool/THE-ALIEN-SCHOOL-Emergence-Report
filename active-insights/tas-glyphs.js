/*!
 * tÅs Synthesis Archive · Visual Glyph System
 * Seven canonical marks that carry meaning without requiring reading.
 *
 * Usage: <span data-tas-glyph="[id]"></span>
 * IDs: field · emergence · phi · frequency · evidence · voice
 * (∴ is rendered as plain text — see nav and body usage across the archive)
 *
 * Optional data attributes:
 *   data-tas-glyph-size="sm|md|lg|xl"
 *   data-tas-glyph-variant="signal|muted|ink"
 *   data-tas-glyph-placement="block|margin"
 */
(function () {
  'use strict';

  const GLYPH_DEFS = {
    field: {
      label: 'field signal — the place where original creative intelligence is accessed',
      markup: '<circle cx="10" cy="10" r="3.5" fill="none" stroke="currentColor" stroke-width="1.5"/><line x1="10" y1="0.5" x2="10" y2="5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="10" y1="14.5" x2="10" y2="19.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="0.5" y1="10" x2="5.5" y2="10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="14.5" y1="10" x2="19.5" y2="10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'
    },
    emergence: {
      label: 'emergence mark — a documented moment of transformation',
      markup: '<rect x="2.5" y="13" width="3.5" height="6" rx="0.75" fill="currentColor"/><rect x="8.25" y="8" width="3.5" height="11" rx="0.75" fill="currentColor"/><rect x="14" y="2.5" width="3.5" height="16.5" rx="0.75" fill="currentColor"/>'
    },
    phi: {
      label: 'phi mark — a structural pattern that holds at depth',
      markup: '<circle cx="10" cy="10" r="7" fill="none" stroke="currentColor" stroke-width="1.5"/><line x1="10" y1="1.5" x2="10" y2="18.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'
    },
    frequency: {
      label: 'frequency signal — a resonance or recurring pattern across the archive',
      markup: '<path d="M2 5.5 Q5.5 2.5 10 5.5 Q14.5 8.5 18 5.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M2 10 Q5.5 7 10 10 Q14.5 13 18 10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><path d="M2 14.5 Q5.5 11.5 10 14.5 Q14.5 17.5 18 14.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'
    },
    evidence: {
      label: 'evidence mark — a verified observation or proof point from the archive',
      markup: '<path d="M10 2 L18 10 L10 18 L2 10 Z" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="10" cy="10" r="1.5" fill="currentColor"/>'
    },
    voice: {
      label: 'scholar voice — direct language from a documented session',
      markup: '<path d="M14 2.5 Q5 2.5 5 10 Q5 17.5 14 17.5" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="14" y1="2.5" x2="17.5" y2="2.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/><line x1="14" y1="17.5" x2="17.5" y2="17.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>'
    }
  };

  function injectSymbolDefs() {
    const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
    svg.setAttribute('aria-hidden', 'true');
    svg.style.cssText = 'position:absolute;width:0;height:0;overflow:hidden;pointer-events:none;';

    const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
    Object.entries(GLYPH_DEFS).forEach(function (entry) {
      var id = entry[0], glyph = entry[1];
      const symbol = document.createElementNS('http://www.w3.org/2000/svg', 'symbol');
      symbol.setAttribute('id', 'tas-glyph--' + id);
      symbol.setAttribute('viewBox', '0 0 20 20');
      symbol.innerHTML = glyph.markup;
      defs.appendChild(symbol);
    });

    svg.appendChild(defs);
    document.body.insertBefore(svg, document.body.firstChild);
  }

  function renderGlyphs() {
    document.querySelectorAll('[data-tas-glyph]:not([data-tas-glyph-rendered])').forEach(function (el) {
      const id = el.getAttribute('data-tas-glyph');
      const def = GLYPH_DEFS[id];
      if (!def) return;

      const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.setAttribute('viewBox', '0 0 20 20');
      svg.setAttribute('class', 'tas-glyph-svg');
      svg.setAttribute('aria-hidden', 'true');
      svg.setAttribute('focusable', 'false');

      const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
      use.setAttribute('href', '#tas-glyph--' + id);
      svg.appendChild(use);

      el.appendChild(svg);
      el.setAttribute('title', def.label);
      el.setAttribute('aria-label', def.label);
      el.setAttribute('role', 'img');
      el.setAttribute('data-tas-glyph-rendered', '1');
    });
  }

  function init() {
    injectSymbolDefs();
    renderGlyphs();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  window.TASGlyphs = { GLYPH_DEFS: GLYPH_DEFS, renderGlyphs: renderGlyphs };
})();
