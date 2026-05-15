#!/usr/bin/env python3
"""
apply_sceu_editorial.py
Three-sweep editorial script for both SCEU field reports.
  1. PRIMER sweep — remove QWP / QUIET WARRIOR PRODUCTIONS
  2. Em dash upgrade — narrative and thinker-name — → ::
  3. Anonymity adjustment — raw first-name-last-initial → archetype labels
"""

import os, re

BASE = r'C:\Users\Kzaka\Documents\GitHub\tas-artifacts'

# ══════════════════════════════════════════════════════════════════
# REPORT ONE
# ══════════════════════════════════════════════════════════════════

R1 = os.path.join(BASE, 'sceu-report-one-integrating-creative-thinking.html')
with open(R1, 'r', encoding='utf-8') as f:
    r1 = f.read()

# ── SWEEP 1 · QWP removal ──────────────────────────────────────────
r1 = r1.replace(
    'KAMAU ZUBERI AKABUEZE · KzA · QUIET WARRIOR PRODUCTIONS',
    'KAMAU ZUBERI AKABUEZE · KzA'
)
r1 = r1.replace(
    'THE ÅLïEN SCõÖL FOR CREATIVE THÏNKING · QUIET WARRIOR PRODUCTIONS',
    'THE ÅLïEN SCõÖL FOR CREATIVE THÏNKING'
)

# ── SWEEP 2 · thinker-name em dashes ──────────────────────────────
r1 = r1.replace(
    'Donella Meadows — Leverage Points: Places to Intervene in a System (1999)',
    'Donella Meadows :: Leverage Points: Places to Intervene in a System (1999)'
)
r1 = r1.replace(
    'Otto Scharmer — Theory U: Leading from the Future as It Emerges (2007)',
    'Otto Scharmer :: Theory U: Leading from the Future as It Emerges (2007)'
)
r1 = r1.replace(
    'adrienne maree brown — Emergent Strategy: Shaping Change, Changing Worlds (2017)',
    'adrienne maree brown :: Emergent Strategy: Shaping Change, Changing Worlds (2017)'
)

# ── SWEEP 2 · Section I locate ────────────────────────────────────
r1 = r1.replace(
    'in a room — a staff meeting, a planning session, a strategy retreat — where you could feel the intelligence in the space going unused.',
    'in a room :: a staff meeting, a planning session, a strategy retreat :: where you could feel the intelligence in the space going unused.'
)

# ── SWEEP 2 · Section II prose ───────────────────────────────────
r1 = r1.replace(
    "the organization's operating paradigm — its shared assumptions about where creative intelligence lives, who holds it, and what conditions are required for it to contribute to the system's work.",
    "the organization's operating paradigm :: its shared assumptions about where creative intelligence lives, who holds it, and what conditions are required for it to contribute to the system's work."
)

# ── SWEEP 2 · Section III locate ─────────────────────────────────
r1 = r1.replace(
    'It was an awareness — a different quality of attention applied to the same situation — that changed what became visible and therefore what became possible.',
    'It was an awareness :: a different quality of attention applied to the same situation :: that changed what became visible and therefore what became possible.'
)

# ── SWEEP 2 · Section III prose ──────────────────────────────────
r1 = r1.replace(
    'operate primarily in “downloading” mode — applying existing frameworks to new situations without genuinely seeing the situation — produce solutions shaped by the past rather than by what is actually present.',
    'operate primarily in “downloading” mode :: applying existing frameworks to new situations without genuinely seeing the situation :: produce solutions shaped by the past rather than by what is actually present.'
)
# also handle plain-quote variant
r1 = r1.replace(
    'operate primarily in "downloading" mode — applying existing frameworks to new situations without genuinely seeing the situation — produce solutions shaped by the past rather than by what is actually present.',
    'operate primarily in "downloading" mode :: applying existing frameworks to new situations without genuinely seeing the situation :: produce solutions shaped by the past rather than by what is actually present.'
)

# ── SWEEP 2 · Section IV prose ───────────────────────────────────
r1 = r1.replace(
    'Responsibility is the choice to act from that perception — to offer what you see, to bring the quality of thinking the moment requires, regardless of whether the organizational role you hold has given you permission to think that way.',
    'Responsibility is the choice to act from that perception :: to offer what you see, to bring the quality of thinking the moment requires, regardless of whether the organizational role you hold has given you permission to think that way.'
)
r1 = r1.replace(
    "distribute intelligence throughout — that no single node holds all the relevant information, and that the system's capacity to respond to changing conditions depends on the quality of sensing distributed across the whole.",
    "distribute intelligence throughout :: that no single node holds all the relevant information, and that the system's capacity to respond to changing conditions depends on the quality of sensing distributed across the whole."
)
r1 = r1.replace(
    "the guide does not tell the scholar what to think — the guide creates conditions in which the scholar's own intelligence becomes available to them with enough precision to act on.",
    "the guide does not tell the scholar what to think :: the guide creates conditions in which the scholar's own intelligence becomes available to them with enough precision to act on."
)
r1 = r1.replace(
    'responsibility — in themselves and in the team — for what becomes visible.',
    'responsibility :: in themselves and in the team :: for what becomes visible.'
)

# ── SWEEP 2 · Section V propositions ─────────────────────────────
r1 = r1.replace(
    'operational rhythm — not as an add-on, but as a structural feature — consistently produce',
    'operational rhythm :: not as an add-on, but as a structural feature :: consistently produce'
)
r1 = r1.replace(
    'his creative capacity — it was a change in his relationship to his own authority to express it.',
    'his creative capacity :: it was a change in his relationship to his own authority to express it.'
)
r1 = r1.replace(
    'a physical experience — a felt sense, a breath pattern, a moment of stillness — hold across time and return as usable knowing.',
    'a physical experience :: a felt sense, a breath pattern, a moment of stillness :: hold across time and return as usable knowing.'
)
r1 = r1.replace(
    'the honest edge — the areas where the methodology met his resistance, and where the coaching acknowledged that limit rather than overriding it.',
    'the honest edge :: the areas where the methodology met his resistance, and where the coaching acknowledged that limit rather than overriding it.'
)

# ── SWEEP 2 · Section VI provocation ─────────────────────────────
r1 = r1.replace(
    'not whether this is true — it is always true — but what the organization currently believes about why that intelligence is not contributing.',
    'not whether this is true :: it is always true :: but what the organization currently believes about why that intelligence is not contributing.'
)
r1 = r1.replace(
    "the system actually operates — not how it is designed to operate, but how it actually functions — holds creative intelligence about that system's real behavior.",
    "the system actually operates :: not how it is designed to operate, but how it actually functions :: holds creative intelligence about that system's real behavior."
)

# ── SWEEP 2 · Closing ────────────────────────────────────────────
r1 = r1.replace(
    'a forty-minute perspective-sharing session — a provocation, not a prescription.',
    'a forty-minute perspective-sharing session :: a provocation, not a prescription.'
)

# ── SWEEP 3 · Anonymity — attribution tags ───────────────────────
r1 = r1.replace('Keith C · 2025', 'THE CREATIVE DIRECTOR · 2025')
r1 = r1.replace('Greg S · Shenzhen · Dec 2025', 'THE SCHOOL DIRECTOR · DEC 2025')
r1 = r1.replace('Tanya K / Aki J · Dec 2025', 'THE PLATFORM ARCHITECTS · DEC 2025')

# ── SWEEP 3 · Anonymity — body text ──────────────────────────────
r1 = r1.replace(
    'The Tanya and Aki session named the school explicitly as a resource for organizations',
    'The Platform Architects named the school explicitly as a resource for organizations'
)

with open(R1, 'w', encoding='utf-8') as f:
    f.write(r1)

# Verify: report remaining em dashes (excluding known-safe pullquote-attr and cite lines)
hits_r1 = [(i, l.strip()) for i, l in enumerate(r1.splitlines(), 1) if '—' in l]
safe_r1  = [h for h in hits_r1 if not any(k in h[1] for k in ['pullquote-attr', 'thinker-cite', 'closing-sig'])]
print(f'Report 1 written. Remaining em dashes outside safe zones: {len(safe_r1)}')
for ln, txt in safe_r1:
    print(f'  L{ln}: {txt[:120]}')


# ══════════════════════════════════════════════════════════════════
# REPORT TWO
# ══════════════════════════════════════════════════════════════════

R2 = os.path.join(BASE, 'sceu-report-two-illuminating-creative-thinking.html')
with open(R2, 'r', encoding='utf-8') as f:
    r2 = f.read()

# ── SWEEP 1 · QWP removal ──────────────────────────────────────────
r2 = r2.replace(
    'KAMAU ZUBERI AKABUEZE · KzA · QUIET WARRIOR PRODUCTIONS',
    'KAMAU ZUBERI AKABUEZE · KzA'
)
r2 = r2.replace(
    'THE ÅLïEN SCõÖL FOR CREATIVE THÏNKING · QUIET WARRIOR PRODUCTIONS',
    'THE ÅLïEN SCõÖL FOR CREATIVE THÏNKING'
)

# ── SWEEP 2 · thinker-name em dashes ──────────────────────────────
r2 = r2.replace(
    'Graham Wallas — The Art of Thought (1926)',
    'Graham Wallas :: The Art of Thought (1926)'
)
r2 = r2.replace(
    'Teresa Amabile — Creativity in Context (1996)',
    'Teresa Amabile :: Creativity in Context (1996)'
)
r2 = r2.replace(
    'adrienne maree brown — Emergent Strategy (2017)',
    'adrienne maree brown :: Emergent Strategy (2017)'
)
r2 = r2.replace(
    'Donella Meadows — Leverage Points: Places to Intervene in a System (1999)',
    'Donella Meadows :: Leverage Points: Places to Intervene in a System (1999)'
)

# ── SWEEP 2 · Dynamic 01 body ─────────────────────────────────────
r2 = r2.replace(
    'Not because the people are less capable — because the conditions removed the incubation stage.',
    'Not because the people are less capable :: because the conditions removed the incubation stage.'
)

# ── SWEEP 2 · Dynamic 04 body ─────────────────────────────────────
r2 = r2.replace(
    'UNION — Unified Non-Identical Intelligences Operating Naturally — names the structural principle',
    'UNION :: Unified Non-Identical Intelligences Operating Naturally :: names the structural principle'
)
r2 = r2.replace(
    'The well-designed container does not smooth the difference — it holds it long enough for the productive encounter to occur.',
    'The well-designed container does not smooth the difference :: it holds it long enough for the productive encounter to occur.'
)

# ── SWEEP 2 · Section III intro ───────────────────────────────────
r2 = r2.replace(
    'The tÅs experiential equations — observable patterns extracted from documented sessions — translate directly into systems language.',
    'The tÅs experiential equations :: observable patterns extracted from documented sessions :: translate directly into systems language.'
)

# ── SWEEP 2 · Section IV advocacy ────────────────────────────────
r2 = r2.replace(
    'UNION — Unified Non-Identical Intelligences Operating Naturally — is not only a creative principle',
    'UNION :: Unified Non-Identical Intelligences Operating Naturally :: is not only a creative principle'
)

# ── SWEEP 2 · Section V thinker body (Amabile quote) ─────────────
r2 = r2.replace(
    'intrinsic motivation — working on a task because it is inherently interesting and engaging — consistently produces higher-quality creative thinking than extrinsic motivation tied to evaluation or reward.',
    'intrinsic motivation :: working on a task because it is inherently interesting and engaging :: consistently produces higher-quality creative thinking than extrinsic motivation tied to evaluation or reward.'
)

# ── SWEEP 2 · Section VI provocation ─────────────────────────────
r2 = r2.replace(
    'What daily practice could your system adopt — not as a program, but as a rhythm — that would maintain the conditions for creative thinking between formal interventions?',
    'What daily practice could your system adopt :: not as a program, but as a rhythm :: that would maintain the conditions for creative thinking between formal interventions?'
)

# ── SWEEP 2 · Closing ────────────────────────────────────────────
r2 = r2.replace(
    "with observable patterns — and for making the case that those dynamics are relevant to, and available to, the systems change education community's own work.",
    "with observable patterns :: and for making the case that those dynamics are relevant to, and available to, the systems change education community's own work."
)

# ── SWEEP 3 · Anonymity — attribution tags ───────────────────────
r2 = r2.replace('Daniel R · Dec 2024–May 2025',  'THE WELLNESS TEACHER · DEC 2024–MAY 2025')
r2 = r2.replace('David H · 2025',                      'THE VISUAL DESIGNER · 2025')
r2 = r2.replace('Kristen B · Jul 2025',                'THE FILMMAKER · JUL 2025')
r2 = r2.replace('Brandon W · Aug 2025',                'THE MUSICIAN · AUG 2025')
r2 = r2.replace('Keith C · Jul 2025',                  'THE CREATIVE DIRECTOR · JUL 2025')
r2 = r2.replace(
    'Kaelo L, Desmond, Jena D, Makhosi M · 2025–2026',
    'THE EDUCATOR, THE ENTREPRENEUR, THE CREATIVE PRODUCER, THE ECOSYSTEM BUILDER · 2025–2026'
)
r2 = r2.replace('Doug B · Apr 2025', 'THE EXECUTIVE · APR 2025')

with open(R2, 'w', encoding='utf-8') as f:
    f.write(r2)

hits_r2 = [(i, l.strip()) for i, l in enumerate(r2.splitlines(), 1) if '—' in l]
safe_r2  = [h for h in hits_r2 if not any(k in h[1] for k in ['pullquote-attr', 'thinker-cite', 'closing-sig'])]
print(f'\nReport 2 written. Remaining em dashes outside safe zones: {len(safe_r2)}')
for ln, txt in safe_r2:
    print(f'  L{ln}: {txt[:120]}')

print('\n✓ Three-sweep editorial complete.')
print('  QWP removed · Em dashes upgraded to :: · Scholar identities anonymized.')
