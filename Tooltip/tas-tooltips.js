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

  function slugify(value) {
    return String(value || '')
      .trim()
      .toLowerCase()
      .normalize('NFKD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/(^-|-$)/g, '');
  }

  function escapeHtml(value) {
    return String(value || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }

  function createUi() {
    tooltip = document.createElement('div');
    tooltip.className = 'tas-ai-tooltip';
    tooltip.setAttribute('role', 'tooltip');
    tooltip.setAttribute('aria-hidden', 'true');
    document.body.appendChild(tooltip);

    overlay = document.createElement('div');
    overlay.className = 'tas-ai-overlay';
    overlay.setAttribute('aria-hidden', 'true');
    overlay.innerHTML = `
      <section class="tas-ai-modal" role="dialog" aria-modal="true" aria-labelledby="tas-ai-modal-title">
        <button class="tas-ai-close" type="button" aria-label="Close insight">×</button>
        <div class="tas-ai-modal__inner">
          <div class="tas-ai-modal__eyebrow"></div>
          <h2 class="tas-ai-modal__title" id="tas-ai-modal-title"></h2>
          <p class="tas-ai-modal__body"></p>
          <p class="tas-ai-modal__why"></p>
          <div class="tas-ai-modal__actions"></div>
        </div>
      </section>
    `;
    document.body.appendChild(overlay);

    overlay.addEventListener('click', (event) => {
      if (event.target === overlay || event.target.closest('.tas-ai-close')) closeModal();
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        hideTooltip();
        closeModal();
      }
    });
  }

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
      source: term.source || ''
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

  function positionTooltip(anchor) {
    const rect = anchor.getBoundingClientRect();
    const tipRect = tooltip.getBoundingClientRect();
    const margin = 12;
    let top = rect.bottom + 10;
    let left = rect.left + rect.width / 2 - tipRect.width / 2;

    if (top + tipRect.height > window.innerHeight - margin) {
      top = rect.top - tipRect.height - 10;
    }
    if (left < margin) left = margin;
    if (left + tipRect.width > window.innerWidth - margin) {
      left = window.innerWidth - tipRect.width - margin;
    }

    tooltip.style.top = `${Math.max(margin, top)}px`;
    tooltip.style.left = `${Math.max(margin, left)}px`;
  }

  function showTooltip(anchor, term) {
    activeTerm = term;
    tooltip.innerHTML = `<span class="tas-ai-tooltip__term">${escapeHtml(term.term)}</span>${escapeHtml(term.tooltip)}`;
    tooltip.setAttribute('aria-hidden', 'false');
    tooltip.dataset.visible = 'true';
    requestAnimationFrame(() => positionTooltip(anchor));
  }

  function hideTooltip() {
    tooltip.dataset.visible = 'false';
    tooltip.setAttribute('aria-hidden', 'true');
  }

  function openModal(term) {
    activeTerm = term;
    overlay.querySelector('.tas-ai-modal__eyebrow').textContent = term.category.replace(/-/g, ' ');
    overlay.querySelector('.tas-ai-modal__title').textContent = term.expanded_title;
    overlay.querySelector('.tas-ai-modal__body').textContent = term.expanded;
    overlay.querySelector('.tas-ai-modal__why').innerHTML = term.why_it_matters
      ? `<strong>Why it matters:</strong> ${escapeHtml(term.why_it_matters)}`
      : '';

    const actions = overlay.querySelector('.tas-ai-modal__actions');
    actions.innerHTML = '';

    const close = document.createElement('button');
    close.type = 'button';
    close.className = 'tas-ai-button';
    close.textContent = 'Close';
    close.addEventListener('click', closeModal);
    actions.appendChild(close);

    if (config.showSourceLinks && term.source) {
      const link = document.createElement('a');
      link.className = 'tas-ai-source';
      link.href = term.source;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.textContent = 'Continue reading';
      actions.appendChild(link);
    }

    overlay.dataset.visible = 'true';
    overlay.setAttribute('aria-hidden', 'false');
    overlay.querySelector('.tas-ai-close').focus();
  }

  function closeModal() {
    overlay.dataset.visible = 'false';
    overlay.setAttribute('aria-hidden', 'true');
  }

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
      element.addEventListener('click', (event) => {
        event.preventDefault();
        openModal(term);
      });
      element.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          openModal(term);
        }
      });
    });
  }

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
    const match = document.createElement('span');
    match.setAttribute('data-tas-term', term.id);
    match.textContent = value.slice(index, index + phrase.length);
    const after = document.createTextNode(value.slice(index + phrase.length));

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
    const counts = new Map();

    containers.forEach((container) => {
      const walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, {
        acceptNode(node) {
          const parent = node.parentElement;
          if (!parent) return NodeFilter.FILTER_REJECT;
          if (parent.closest('script, style, textarea, input, [data-tas-term], .tas-ai-term')) return NodeFilter.FILTER_REJECT;
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
          if (count >= config.maxAutoMatchesPerTerm) continue;
          if (annotateTextNode(node, phrase, term)) {
            counts.set(term.id, count + 1);
            break;
          }
        }
      });
    });
  }

  function addReaderHelpButton(targetSelector = 'body') {
    const term = byId.get('calvin-mode');
    if (!term) return;
    const target = document.querySelector(targetSelector) || document.body;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'tas-ai-reader-help';
    button.textContent = 'New here? Start simple.';
    button.addEventListener('click', () => openModal(term));
    target.prepend(button);
  }

  async function init(options = {}) {
    config = { ...DEFAULTS, ...options };
    createUi();

    const response = await fetch(config.glossaryUrl);
    if (!response.ok) throw new Error(`Unable to load glossary: ${response.status}`);
    const data = await response.json();
    normalizeTermData(data);

    if (config.mode === 'auto') autoAnnotate();
    bindManualTerms();

    if (config.readerHelpButton) {
      addReaderHelpButton(config.readerHelpTarget || 'body');
    }
  }

  window.TASActiveInsights = {
    init,
    bindManualTerms,
    autoAnnotate,
    openTerm(id) {
      const term = byId.get(id) || byLookup.get(slugify(id));
      if (term) openModal(term);
    },
    getTerms() {
      return glossary.slice();
    }
  };
})();
