(function () {
  'use strict';

  const DEFAULTS = {
    glossaryUrl: '/active-insights/active-insights-glossary.json',
    mode: 'manual', // 'manual' or 'auto'
    autoSelector: '[data-tas-auto-annotate]',
    manualSelector: '[data-tas-term]',
    maxAutoMatchesPerTerm: 1,
    openOn: 'click',
    showSourceLinks: true
  };

  let config = { ...DEFAULTS };
  let glossary = [];
  let byId = new Map();
  let byLookup = new Map();
  let tooltip;
  let overlay;
  let activeTerm = null;
  let hideTimeout = null;

  function slugify(value) {
    return String(value || '')
      .trim()
      .toLowerCase()
      .normalize('NFKD')
      .replace(/[̀-ͯ]/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/(^-|-$)/g, '');
  }

  // ── DOM helpers (safe, no innerHTML for user content) ─────────

  function el(tag, attrs = {}, ...children) {
    const node = document.createElement(tag);
    Object.entries(attrs).forEach(([k, v]) => {
      if (k === 'class') node.className = v;
      else if (k === 'text') node.textContent = v;
      else node.setAttribute(k, v);
    });
    children.forEach((c) => {
      if (c instanceof Node) node.appendChild(c);
      else if (c != null) node.appendChild(document.createTextNode(String(c)));
    });
    return node;
  }

  function text(str) { return document.createTextNode(String(str || '')); }

  // ── UI construction ────────────────────────────────────────────

  function createUi() {
    tooltip = el('div', {
      class: 'tas-ai-tooltip',
      role: 'tooltip',
      'aria-hidden': 'true'
    });
    document.body.appendChild(tooltip);

    // Modal overlay — static structure, no user content injected here
    const closeBtn = el('button', {
      class: 'tas-ai-close',
      type: 'button',
      'aria-label': 'Close insight'
    }, '×');

    const eyebrow  = el('div',  { class: 'tas-ai-modal__eyebrow' });
    const title    = el('h2',   { class: 'tas-ai-modal__title', id: 'tas-ai-modal-title' });
    const body     = el('p',    { class: 'tas-ai-modal__body' });
    const why      = el('p',    { class: 'tas-ai-modal__why' });
    const actions  = el('div',  { class: 'tas-ai-modal__actions' });

    const inner = el('div', { class: 'tas-ai-modal__inner' }, eyebrow, title, body, why, actions);
    const modal = el('section', {
      class: 'tas-ai-modal',
      role: 'dialog',
      'aria-modal': 'true',
      'aria-labelledby': 'tas-ai-modal-title'
    }, closeBtn, inner);

    overlay = el('div', { class: 'tas-ai-overlay', 'aria-hidden': 'true' }, modal);
    document.body.appendChild(overlay);

    overlay.addEventListener('click', (event) => {
      if (event.target === overlay || event.target.closest('.tas-ai-close')) closeModal();
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') { hideTooltip(); closeModal(); }
    });
  }

  // ── Glossary data ──────────────────────────────────────────────

  function normalizeTermData(data) {
    const terms = Array.isArray(data?.terms) ? data.terms : [];
    glossary = terms.map((term) => ({
      id: term.id || slugify(term.term),
      term: term.term,
      aliases: Array.isArray(term.aliases) ? term.aliases : [],
      category: term.category || 'insight',
      tooltip: term.tooltip || '',
      expanded_title: term.expanded_title || term.term,
      expanded: term.expanded || term.tooltip || '',
      why_it_matters: term.why_it_matters || '',
      source: term.source || '',
      maxMatches: term.maxMatches != null ? term.maxMatches : null
    }));

    byId = new Map();
    byLookup = new Map();

    glossary.forEach((term) => {
      byId.set(term.id, term);
      byLookup.set(slugify(term.term), term);
      term.aliases.forEach((alias) => byLookup.set(slugify(alias), term));
    });
  }

  function getTermFromElement(element) {
    const key = element.getAttribute('data-tas-term') || element.textContent;
    return byId.get(key) || byLookup.get(slugify(key));
  }

  // ── Tooltip positioning ────────────────────────────────────────

  function positionTooltip(anchor) {
    const rect = anchor.getBoundingClientRect();
    const tipRect = tooltip.getBoundingClientRect();
    const margin = 12;
    let top = rect.bottom + 10;
    let left = rect.left + rect.width / 2 - tipRect.width / 2;

    if (top + tipRect.height > window.innerHeight - margin) top = rect.top - tipRect.height - 10;
    if (left < margin) left = margin;
    if (left + tipRect.width > window.innerWidth - margin) left = window.innerWidth - tipRect.width - margin;

    tooltip.style.top = `${Math.max(margin, top)}px`;
    tooltip.style.left = `${Math.max(margin, left)}px`;
  }

  // ── Tooltip show/hide ──────────────────────────────────────────

  function showTooltip(anchor, term) {
    clearTimeout(hideTimeout);
    activeTerm = term;

    // Safe DOM construction — no innerHTML for term data
    while (tooltip.firstChild) tooltip.removeChild(tooltip.firstChild);
    const termLabel = el('span', { class: 'tas-ai-tooltip__term', 'aria-hidden': 'true' }, term.term);
    tooltip.appendChild(termLabel);
    tooltip.appendChild(text(term.tooltip));

    tooltip.setAttribute('aria-hidden', 'false');
    tooltip.dataset.visible = 'true';
    requestAnimationFrame(() => positionTooltip(anchor));
  }

  function hideTooltip() {
    clearTimeout(hideTimeout);
    hideTimeout = setTimeout(() => {
      tooltip.dataset.visible = 'false';
      tooltip.setAttribute('aria-hidden', 'true');
    }, 150);
  }

  // ── Modal open/close ───────────────────────────────────────────

  function openModal(term) {
    activeTerm = term;
    const eyebrow = overlay.querySelector('.tas-ai-modal__eyebrow');
    const title   = overlay.querySelector('.tas-ai-modal__title');
    const body    = overlay.querySelector('.tas-ai-modal__body');
    const why     = overlay.querySelector('.tas-ai-modal__why');
    const actions = overlay.querySelector('.tas-ai-modal__actions');

    eyebrow.textContent = term.category.replace(/-/g, ' ');
    title.textContent   = term.expanded_title;
    body.textContent    = term.expanded;

    // Safe "Why it matters" with one bold span — no innerHTML
    while (why.firstChild) why.removeChild(why.firstChild);
    if (term.why_it_matters) {
      const label = el('strong', { text: 'Why it matters: ' });
      why.appendChild(label);
      why.appendChild(text(term.why_it_matters));
    }

    // Rebuild action buttons
    while (actions.firstChild) actions.removeChild(actions.firstChild);

    const closeBtn = el('button', { type: 'button', class: 'tas-ai-button', text: 'Close' });
    closeBtn.addEventListener('click', closeModal);
    actions.appendChild(closeBtn);

    if (config.showSourceLinks && term.source) {
      const link = el('a', {
        class: 'tas-ai-source',
        href: term.source,
        target: '_blank',
        rel: 'noopener noreferrer',
        text: 'Continue reading'
      });
      actions.appendChild(link);
    }

    overlay.dataset.visible = 'true';
    overlay.setAttribute('aria-hidden', 'false');
    overlay.querySelector('.tas-ai-close').focus();
  }

  function closeModal() {
    overlay.dataset.visible = 'false';
    overlay.setAttribute('aria-hidden', 'true');
    activeTerm = null;
  }

  // ── Manual term binding ────────────────────────────────────────

  function bindManualTerms(root = document) {
    root.querySelectorAll(config.manualSelector).forEach((element) => {
      const term = getTermFromElement(element);
      if (!term) return;

      element.classList.add('tas-ai-term');
      element.setAttribute('tabindex', '0');
      element.setAttribute('role', 'button');
      element.setAttribute('aria-label', `${term.term}: ${term.tooltip}`);

      element.addEventListener('mouseenter', () => showTooltip(element, term));
      element.addEventListener('mouseleave', hideTooltip);
      element.addEventListener('focus', () => showTooltip(element, term));
      element.addEventListener('blur', hideTooltip);
      element.addEventListener('click', (event) => { event.preventDefault(); openModal(term); });
      element.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); openModal(term); }
      });
    });
  }

  // ── Auto-annotation ────────────────────────────────────────────

  function buildAutoPattern() {
    const phrases = [];
    glossary.forEach((term) => {
      [term.term, ...term.aliases].forEach((phrase) => {
        if (phrase && phrase.length > 2) phrases.push(phrase);
      });
    });
    phrases.sort((a, b) => b.length - a.length);
    return phrases;
  }

  function annotateTextNode(textNode, phrase, term) {
    const value = textNode.nodeValue;
    const index = value.toLowerCase().indexOf(phrase.toLowerCase());
    if (index === -1) return false;

    const before = document.createTextNode(value.slice(0, index));
    const match  = el('span', { 'data-tas-term': term.id });
    match.textContent = value.slice(index, index + phrase.length);
    const after  = document.createTextNode(value.slice(index + phrase.length));

    const parent = textNode.parentNode;
    parent.insertBefore(before, textNode);
    parent.insertBefore(match, textNode);
    parent.insertBefore(after, textNode);
    parent.removeChild(textNode);
    return true;
  }

  function autoAnnotate(root = document) {
    const containers = Array.from(root.querySelectorAll(config.autoSelector));
    if (!containers.length) return;

    const phrases = buildAutoPattern();
    const counts  = new Map();

    containers.forEach((container) => {
      const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, {
        acceptNode(node) {
          const parent = node.parentElement;
          if (!parent) return NodeFilter.FILTER_REJECT;
          if (parent.closest('script, style, textarea, input, [data-tas-term], .tas-ai-term, .tas-term, nav, .tas-ai-reader-help')) {
            return NodeFilter.FILTER_REJECT;
          }
          if (!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
          return NodeFilter.FILTER_ACCEPT;
        }
      });

      const nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);

      nodes.forEach((node) => {
        for (const phrase of phrases) {
          const term = byLookup.get(slugify(phrase));
          if (!term) continue;
          const count = counts.get(term.id) || 0;
          const termMax = term.maxMatches != null ? term.maxMatches : config.maxAutoMatchesPerTerm;
          if (count >= termMax) continue;
          if (annotateTextNode(node, phrase, term)) {
            counts.set(term.id, count + 1);
            break;
          }
        }
      });
    });
  }

  // ── Reader-help orientation button ────────────────────────────

  function addReaderHelpButton(targetSelector = 'body') {
    const term = byId.get('calvin-mode');
    if (!term) return;
    const target = document.querySelector(targetSelector) || document.body;
    const button = el('button', {
      type: 'button',
      class: 'tas-ai-reader-help',
      text: 'New here? Start simple.'
    });
    button.addEventListener('click', () => openModal(term));
    target.prepend(button);
  }

  // ── Init ──────────────────────────────────────────────────────

  async function init(options = {}) {
    config = { ...DEFAULTS, ...options };
    createUi();

    try {
      const response = await fetch(config.glossaryUrl);
      if (!response.ok) throw new Error(`Glossary unavailable: ${response.status}`);
      const data = await response.json();
      normalizeTermData(data);
    } catch (err) {
      console.warn('[TASActiveInsights] Glossary load failed. Tooltips will not initialize.', err);
      return;
    }

    if (config.mode === 'auto') autoAnnotate();
    bindManualTerms();

    if (config.readerHelpButton) {
      addReaderHelpButton(config.readerHelpTarget || 'body');
    }
  }

  // ── Public API ─────────────────────────────────────────────────

  window.TASActiveInsights = {
    init,
    bindManualTerms,
    autoAnnotate,
    openTerm(id) {
      const term = byId.get(id) || byLookup.get(slugify(id));
      if (term) openModal(term);
    },
    getTerms() { return glossary.slice(); }
  };
})();
