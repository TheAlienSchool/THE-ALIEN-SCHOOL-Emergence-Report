# tÅs Active Insights Toolkit

Developer-oriented glossary, tooltip system, and integration manual for `scoolreport2026.vercel.app`.

## Purpose

The Synthesis Archive is rich, layered, and symbolically precise. The Active Insights layer helps first-time and returning navigators stay oriented without flattening the work.

Core principle:

> Name the mechanism. Keep the magic.

## Package Contents

- `active-insights-glossary.json` — editable glossary dataset for tooltips and pop-ups.
- `tas-tooltips.js` — lightweight vanilla JavaScript tooltip/pop-up engine.
- `tas-tooltips.css` — default accessible styling.
- `implementation-manual.md` — full developer manual and editorial protocol.
- `deployment-checklist.md` — launch checklist for Vercel/static deployment.
- `demo.html` — local demo showing the tooltip system in action.

## Quick Start

1. Copy these files into your site, ideally:

```txt
/public/active-insights/active-insights-glossary.json
/public/active-insights/tas-tooltips.js
/public/active-insights/tas-tooltips.css
```

2. Add this before the closing `</head>` tag:

```html
<link rel="stylesheet" href="/active-insights/tas-tooltips.css">
```

3. Add this before the closing `</body>` tag:

```html
<script src="/active-insights/tas-tooltips.js" defer></script>
<script>
  window.TASActiveInsights.init({
    glossaryUrl: '/active-insights/active-insights-glossary.json',
    mode: 'manual'
  });
</script>
```

4. Wrap important terms in the report:

```html
<span data-tas-term="reflationary-lab">Reflationary Lab</span>
```

5. Optional auto-annotation:

```html
<main data-tas-auto-annotate>
  ...article content...
</main>
```

Use auto-annotation sparingly. Manual markup gives stronger editorial control.
