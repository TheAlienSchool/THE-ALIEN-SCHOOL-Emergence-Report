# tÅs Active Insights Integration Manual

## 1. Mission

The Active Insights layer turns the Synthesis Archive into a guided reading environment. It gives first-time navigators a simple bridge into the work while preserving the symbolic and poetic intelligence of tÅs.

The tool is designed around one law:

> Name the mechanism. Keep the magic.

A tooltip should explain enough for the reader to continue. A pop-up should deepen the term without becoming a second essay. A source link should let advanced readers keep descending.

## 2. Reader Problem Being Solved

A new reader may arrive at the report and encounter:

- symbolic typography
- internal terms
- intellectual lineage language
- metaphors with private histories
- graduate-access language
- field report structure
- multiple related sites and portals

The Active Insights layer prevents the report from feeling like a private language. It turns the language into a navigable system.

## 3. Recommended UX Architecture

### 3.1 First-Read Button

Place this near the top of the homepage or archive:

```html
<button type="button" class="tas-ai-reader-help" onclick="window.TASActiveInsights.openTerm('calvin-mode')">
  New here? Start simple.
</button>
```

This pop-up should say plainly:

> THE ALIEN SCHOOL helps Creative Mavericks recover access to their own creative intelligence. The deeper archive uses symbolic language, metaphors, and field reports; the core offer is guided creative development for people and systems ready to move with clarity.

### 3.2 Inline Tooltips

Use manual markup for important terms:

```html
<span data-tas-term="reflationary-lab">Reflationary Lab</span>
```

The `data-tas-term` value should match an `id` in `active-insights-glossary.json`.

### 3.3 Expandable Pop-Ups

Every tooltip can be clicked or opened by keyboard to reveal:

- category
- expanded title
- expanded explanation
- “why it matters”
- optional continue-reading source link

### 3.4 Optional Auto-Annotation

Auto-annotation can scan a content region and mark the first instance of each known term:

```html
<main data-tas-auto-annotate>
  <!-- report content -->
</main>
```

Initialize with:

```html
<script>
  window.TASActiveInsights.init({
    glossaryUrl: '/active-insights/active-insights-glossary.json',
    mode: 'auto',
    maxAutoMatchesPerTerm: 1
  });
</script>
```

Use auto mode carefully. Editorially selected terms will produce a more elegant reader experience.

## 4. File Placement

For a static/Vercel site, recommended paths:

```txt
/public/active-insights/active-insights-glossary.json
/public/active-insights/tas-tooltips.js
/public/active-insights/tas-tooltips.css
```

Then add to each page template:

```html
<link rel="stylesheet" href="/active-insights/tas-tooltips.css">
<script src="/active-insights/tas-tooltips.js" defer></script>
<script>
  window.addEventListener('DOMContentLoaded', function () {
    window.TASActiveInsights.init({
      glossaryUrl: '/active-insights/active-insights-glossary.json',
      mode: 'manual',
      readerHelpButton: true,
      readerHelpTarget: 'main'
    });
  });
</script>
```

## 5. Glossary Data Model

Each glossary entry uses this shape:

```json
{
  "id": "reflationary-lab",
  "term": "Reflationary Lab",
  "aliases": ["reflationary", "Reflationary", "reflation"],
  "category": "methodology",
  "tooltip": "A practice environment that restores creative capacity after it has been compressed.",
  "expanded_title": "Reflationary Lab",
  "expanded": "A Reflationary Lab restores what systemic pressure, alienation, overwork, or inherited patterns have deflated.",
  "why_it_matters": "This is one of the strongest plain-language bridges between the poetic world of tÅs and its practical outcome.",
  "source": "https://scoolreport2026.vercel.app/tas-emergence-report.html"
}
```

### Field Rules

- `id`: stable slug used in HTML.
- `term`: display term.
- `aliases`: optional terms for auto-annotation.
- `category`: used as the modal eyebrow.
- `tooltip`: one clean sentence.
- `expanded_title`: pop-up title.
- `expanded`: the larger explanation.
- `why_it_matters`: practical orientation.
- `source`: relevant report or artifact URL.

## 6. Editorial Rules

### Rule 1: Plain Language First

Preferred:

> The Alien School for Creative Thinking, stylized as THE ÅLïEN SCõÖL.

Avoid leading with symbolic spelling when the reader has no context.

### Rule 2: Tooltips Are Not Essays

Tooltip: one sentence.

Pop-up: 50–110 words.

Source link: deeper reading.

### Rule 3: Explain Mechanism Before Mythos

Example:

Weak:

> MaGNET is your cosmic door into the field of original frequency.

Stronger:

> MaGNET is a personalized doorway into the deeper tÅs experience. Each doorway offers a different way to recognize yourself.

### Rule 4: Symbolic Language Is Optional Depth

Symbols such as `Å`, `ï`, and `õÖ` should be framed as part of an inner symbolic layer. Readers should know they can keep reading without decoding every mark.

### Rule 5: Preserve the Atmosphere

Do not over-flatten the work. The goal is orientation, not reduction.

## 7. Recommended Terms for First Deployment

Start with these terms only:

1. THE ÅLïEN SCõÖL / tÅs
2. Creative Intelligence
3. Creative Maverick
4. Reflationary Lab
5. Reflectionary
6. Scholar
7. Guide
8. Elevation Move
9. Somatic Tether
10. Steeping as Time Design
11. MaGNET
12. Å
13. New here? Start simple.

Once the first layer feels smooth, expand to the full glossary.

## 8. Accessibility Requirements

The included tooltip system supports:

- keyboard focus
- Enter/Space modal opening
- Escape close
- visible focus states
- high-contrast modal presentation
- no required hover-only information
- reduced-motion preference

Before launch, test with:

- keyboard only
- mobile tap
- browser zoom at 200%
- VoiceOver or equivalent screen reader

## 9. Performance Notes

The JavaScript is intentionally lightweight and dependency-free.

Recommended deployment mode:

- Manual annotation for production pages.
- Auto-annotation only for prototypes or controlled content regions.
- Keep glossary JSON under 100KB if possible.

## 10. Developer API

After initialization, the page exposes:

```js
window.TASActiveInsights.openTerm('reflationary-lab')
window.TASActiveInsights.getTerms()
window.TASActiveInsights.bindManualTerms()
window.TASActiveInsights.autoAnnotate()
```

Use `openTerm()` for buttons, onboarding cards, and custom navigation.

## 11. Integration Pattern for Existing Archive Cards

Example:

```html
<p>
  The school is a <span data-tas-term="reflationary-lab">Reflationary Lab</span>
  in formation, supported by the <span data-tas-term="elevation-codex">Elevation Codex</span>
  and the <span data-tas-term="proof-of-field">Proof of Field</span>.
</p>
```

## 12. “Calvin Mode” Orientation Layer

This is the most important first deployment feature.

Suggested placement:

- fixed or inline near the first headline
- repeated once before Graduate Access
- not hidden in footer

Button label:

> New here? Start simple.

Purpose:

- lower cognitive friction
- clarify audience and offer
- make the symbolic layer feel chosen rather than imposed

## 13. QA Test Script

Test these interactions:

1. Hover a marked term.
2. Focus the term with Tab.
3. Press Enter to open modal.
4. Press Escape to close modal.
5. Tap a term on mobile.
6. Click Continue Reading.
7. Confirm external source opens in a new tab.
8. Confirm symbols have simple explanations.
9. Confirm first-time orientation button is visible without scrolling.
10. Confirm the page remains readable if JavaScript fails.

## 14. No-JavaScript Fallback

Keep the actual text readable even without tooltips. Do not make essential understanding dependent on JavaScript.

Preferred HTML:

```html
The Alien School for Creative Thinking, stylized as <span data-tas-term="tas">THE ÅLïEN SCõÖL</span>, is a creative development school...
```

The plain sentence remains complete if the tooltip never loads.

## 15. Future Enhancements

Potential next versions:

- Searchable glossary drawer
- “Reader Mode” toggle: simple / symbolic / scholar
- Per-page glossary subsets
- Analytics for most-opened terms
- Tooltip heatmap for terms causing friction
- Glossary CMS integration
- “Ask the Archive” conversational assistant
- Multi-lingual symbol guide
