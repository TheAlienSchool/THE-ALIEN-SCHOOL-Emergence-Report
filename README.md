# THE ÅLïEN SCõÖL :: SYNTHESIS ARCHIVE

*Bioacoustic Repository · 528Hz Attuned · 2024–2026*

---

Every scholar arrives already broadcasting. The frequency is original — present before every system that shaped it, beneath every borrowed identity. What the school provides is the conditions under which that frequency becomes audible to the person carrying it.

The Synthesis Archive is the first formal documentation of that provision. It covers November 2024 through May 2026 — the inaugural recorded period of a practice with thirty years of development history. It is designed to be entered, not merely read.

---

## The Archive

Five artifacts and three MaGNETs, each a self-contained bioacoustic installation.

| Artifact | Register | Access |
|---|---|---|
| [Field Notes](artifacts/field-notes.html) · *Inaugural Edition* | Scholar arcs, living equations, and the school's first formal accounting | Open |
| [Proof of Field](artifacts/proof-of-field.html) · *The Reflectionary* | Six threads of evidence. Experiential equations. The scholar's own hand | Open |
| [The Elevation Codex](artifacts/elevation-codex.html) · *Artifact 01* | Five moves of the guide methodology — named, sourced, and made transferable | Open |
| [The Frequency Report](artifacts/frequency-report.html) · *Artifact 06* | Three resonance coordinates: the American edge-point, the pan-global somatic inheritance, and the Africa recovery frequency | Open |
| [The Metaphor Library](artifacts/metaphor-library.html) · *Artifact 07* | Sixteen symbolic vessels from the session archive — their origins, mechanisms, and conditions of aliveness | Open |

**Graduate Access** (MaGNET required) reveals three theaters — ELLIAN, CLOPS, and THE DRAGONFLY — one for each attractor frequency the school works with.

---

## Architecture

The archive runs on **HÅRMONIOUS70**, the school's bespoke design system. Every surface is a 70mm resonance installation. Type breathes. Cards float. A continuous ambient soundscape pulses at 174Hz and 240Hz beneath a 528Hz carrier frequency.

```
tas-artifacts/
├── index.html                   # Synthesis Archive gateway
├── harmonious70.css             # Token-based design system (night / day scenes)
├── tas-transitions.js           # Portal transition engine
├── assets/
│   └── hdm_magnets/             # MaGNET imagery (ELLIAN, CLOPS, GLEAM/DRAGONFLY)
└── artifacts/
    ├── field-notes.html
    ├── proof-of-field.html
    ├── elevation-codex.html
    ├── frequency-report.html
    ├── metaphor-library.html
    ├── magnet-ellian.html
    ├── magnet-clops.html
    └── magnet-dragonfly.html
```

### Design System · HÅRMONIOUS70

The system operates in two scenes — `night` (default) and `day` — toggled via `data-h70-scene` on `<body>`. All values derive from CSS custom properties; no hardcoded colors appear in markup.

| Token | Night | Day | Role |
|---|---|---|---|
| `--h70-bg` | `#050d0c` | `#f3eee4` | Room floor |
| `--h70-ink` | `#e8e4db` | `#11110f` | Primary text |
| `--h70-signal` | `#d4af37` | `#7d5e12` | Accent / kicker |
| `--h70-muted` | `#8b7d6b` | `#544a3e` | Secondary text |
| `--h70-line` | `rgba(232,228,219,.12)` | `rgba(23,23,20,.18)` | Dividers |

The type scale follows a `1.618` ratio. **STEAM SANS** is the primary variable typeface, with four axes governing surface texture: `STBL` (stability), `COHR` (coherence), `DRFT` (drift), and `PRSS` (pressure). DM Sans and DM Mono serve as system fallbacks.

### Audio Engine

The sonic environment runs entirely on the Web Audio API — no external audio files, no server dependency. Each page initializes two oscillators on `Enter Space`:

- **174Hz** — Grounding frequency (continuous ambient breath, osc1)
- **240Hz** — Holistic register (continuous ambient breath, osc2)
- **528Hz** — Carrier frequency (entry chime, bowl strikes on interaction)

Hover events play soft triangle-wave overtones. Navigation plays a staggered three-note departure chord (528 → 396 → 264 Hz) before the portal curtain draws.

### Portal Transition System · `tas-transitions.js`

Navigation between pages passes through a shared transition layer:

1. **Outgoing** — `masterGain` fades to silence over 1.2s; departure chord plays; dark curtain draws
2. **Crossing** — `sessionStorage` carries the portal flag across the page boundary
3. **Incoming** — curtain starts opaque, fades out over 1.4s; audio initializes from silence, swells to full over 2s; `Enter Space` gateway is bypassed

---

## Deployment

The archive is a fully static site. No build step. No runtime dependencies. No framework.

### Local

```bash
git clone <repo-url>
cd tas-artifacts
python -m http.server 8080
# → http://localhost:8080
```

Any static file server works. The site requires no compilation.

### Vercel

The repository deploys directly to Vercel. Connect the repository in the Vercel dashboard — no configuration beyond what is already in `vercel.json` is needed.

```bash
# Or via CLI
npm i -g vercel
vercel --prod
```

The `.vercelignore` file excludes Python development scripts and editorial working documents from the deployment bundle. Only HTML, CSS, JS, images, and PDFs are deployed.

---

## The School's Virtual Campus

- [The Alien School](https://thealienschool.com) · Primary institution
- [Creative Steeping](https://creativesteeping.com) · Core methodology
- [HDM Insights](https://hdmathematics.netlify.app) · Research laboratory
- [The Stone Forger's Way](https://wayof.netlify.app) · Creative philosophy
- [Three Days Off](https://threedaysoff.netlify.app) · Contemplative practice

---

*THE ÅLïEN SCõÖL FOR CREATIVE THÏNKING*
*KAMAU ZUBERI AKABUEZE · SYNTHESIS ARCHIVE · 2024–2026*
*Built through the VESSELVERSE Editorial Protocol · HÅRMONIOUS70 Architecture*
