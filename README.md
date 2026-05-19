# THE ÅLïEN SCõÖL :: SYNTHESIS ARCHIVE

*Bioacoustic Repository · 528Hz Attuned · 2024–2026*

---

The Synthesis Archive documents the inaugural recorded period of The Alien School for Creative Thinking — November 2024 through May 2026, drawn from thirty years of prior development. It is a living record of a methodology: what was practiced, what was proven, what emerged.

Every artifact in this archive was built to be entered. Not scanned. Not summarized. Entered.

---

## How to Enter

The archive opens at [index.html](index.html) — the Synthesis Archive gateway. From there you are invited to **Enter Space**, which initializes the ambient sound environment and opens the navigation layer.

Each artifact is a self-contained room. You can move between them via the portal navigation, which plays a departure chord and draws a curtain between spaces. The audio environment carries across transitions.

If you are running locally:

```bash
git clone <repo-url>
cd tas-artifacts
python -m http.server 8080
# Open http://localhost:8080
```

No build step. No dependencies. Any static file server works.

---

## The Artifacts

Five public artifacts and three graduate-access theaters.

### Open Access

| Artifact | What It Is |
|---|---|
| [Field Notes](artifacts/field-notes.html) · *Inaugural Edition* | The school's first formal accounting: scholar arcs, living equations, and what the practice produced across the inaugural period |
| [Proof of Field](artifacts/proof-of-field.html) · *The Reflectionary* | Six threads of evidence rendered as experiential equations — built to be completed in the scholar's own hand |
| [The Elevation Codex](artifacts/elevation-codex.html) · *Artifact 01* | Five moves of the guide methodology — named, sourced, and made transferable for the first time |
| [The Frequency Report](artifacts/frequency-report.html) · *Artifact 06* | Three resonance coordinates: the American edge-point, the pan-global somatic inheritance, and the Africa recovery frequency |
| [The Metaphor Library](artifacts/metaphor-library.html) · *Artifact 07* | Sixteen symbolic vessels from the session archive — origins, mechanisms, and the conditions under which each one stays alive |

### Graduate Access · MaGNET Required

Three theaters — **ELLIAN**, **CLOPS**, and **THE DRAGONFLY** — one for each attractor frequency the school works with. Access requires a MaGNET credential issued through the school.

---

## The Sound Environment

The archive runs entirely on the Web Audio API. No external audio files, no server dependency.

Each space initializes two oscillators at threshold:

- **174Hz** — grounding frequency (continuous ambient breath)
- **240Hz** — holistic register (continuous ambient breath)
- **528Hz** — carrier frequency (entry chime; bowl strikes on interaction)

Hover events play soft triangle-wave overtones. Navigation plays a staggered departure chord (528 → 396 → 264 Hz) before the portal curtain draws. The experience is designed to be felt as much as seen.

---

## The Design System · HÅRMONIOUS70

Every surface is a 70mm resonance installation. The system runs in two scenes — `night` (default) and `day` — toggled via `data-h70-scene` on `<body>`. All color values derive from CSS custom properties; no hardcoded colors appear in markup.

| Token | Night | Day | Role |
|---|---|---|---|
| `--h70-bg` | `#050d0c` | `#f3eee4` | Room floor |
| `--h70-ink` | `#e8e4db` | `#11110f` | Primary text |
| `--h70-signal` | `#d4af37` | `#7d5e12` | Accent / kicker |
| `--h70-muted` | `#8b7d6b` | `#544a3e` | Secondary text |
| `--h70-line` | `rgba(232,228,219,.12)` | `rgba(23,23,20,.18)` | Dividers |

The type scale follows a `1.618` golden ratio. **STEAM SANS** is the primary variable typeface — four axes: `STBL` (stability), `COHR` (coherence), `DRFT` (drift), `PRSS` (pressure). DM Sans and DM Mono serve as system fallbacks.

### Active Insights · Tooltip Layer

Terms throughout the archive carry embedded definitions via the Active Insights system. Hovering a highlighted term reveals a contextual gloss drawn from [active-insights/active-insights-glossary.json](active-insights/active-insights-glossary.json). The tooltip layer is initialized per-page via [active-insights/tas-tooltips.js](active-insights/tas-tooltips.js).

---

## Repository Structure

```
tas-artifacts/
├── index.html                        # Synthesis Archive gateway
├── harmonious70.css                  # Token-based design system (night / day)
├── tas-transitions.js                # Portal transition engine
├── tas-glossary.css / .js            # Glossary UI layer
├── 404.html                          # Error page
├── vercel.json                       # Deployment configuration
├── active-insights/
│   ├── active-insights-glossary.json # Term definitions
│   ├── tas-tooltips.js               # Tooltip engine
│   └── tas-tooltips.css              # Tooltip styles
├── artifacts/
│   ├── field-notes.html
│   ├── proof-of-field.html
│   ├── elevation-codex.html
│   ├── frequency-report.html
│   ├── metaphor-library.html
│   ├── magnet-ellian.html            # Graduate: ELLIAN theater
│   ├── magnet-clops.html             # Graduate: CLOPS theater
│   └── magnet-dragonfly.html         # Graduate: THE DRAGONFLY theater
└── assets/
    └── hdm_magnets/                  # MaGNET imagery (ELLIAN, CLOPS, GLEAM/DRAGONFLY)
```

---

## Deployment

The archive deploys to Vercel from this repository with no additional configuration. Connect the repository in the Vercel dashboard and it deploys on push.

```bash
# Or via CLI
npm i -g vercel
vercel --prod
```

The `.vercelignore` file excludes development scripts and editorial working documents from the deployment bundle. Only HTML, CSS, JS, images, and PDFs are served.

---

## The School's Ecosystem

- [The Alien School](https://thealienschool.com) · Primary institution
- [Creative Steeping](https://creativesteeping.com) · Core methodology
- [HDM Insights](https://hdmathematics.netlify.app) · Research laboratory
- [The Stone Forger's Way](https://wayof.netlify.app) · Creative philosophy
- [Three Days Off](https://threedaysoff.netlify.app) · Contemplative practice

---

*THE ÅLïEN SCõÖL FOR CREATIVE THÏNKING*
*KAMAU ZUBERI AKABUEZE · SYNTHESIS ARCHIVE · 2024–2026*
*Built through the VESSELVERSE Editorial Protocol · HÅRMONIOUS70 Architecture*
