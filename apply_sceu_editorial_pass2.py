#!/usr/bin/env python3
"""
apply_sceu_editorial_pass2.py
Comprehensive second pass — completes all three sweeps on both SCEU reports.
Report 1: apply remaining em dashes missed in pass 1.
Report 2: apply ALL sweeps (pass 1 errored before writing it).
"""

import os

BASE = r'C:\Users\Kzaka\Documents\GitHub\tas-artifacts'

def upgrade(content, old, new=None):
    """Replace em dash with :: in a single targeted string."""
    if new is None:
        new = old.replace(' — ', ' :: ')
    assert new != old, f'Replacement produced no change: {old[:60]}'
    return content.replace(old, new)

# ══════════════════════════════════════════════════════════════════
# REPORT ONE — additional em dashes missed in first pass
# ══════════════════════════════════════════════════════════════════

R1 = os.path.join(BASE, 'sceu-report-one-integrating-creative-thinking.html')
with open(R1, 'r', encoding='utf-8') as f:
    r1 = f.read()

# Cover subtitle
r1 = upgrade(r1,
    'beyond workshops and department walls — as an observation report and provocation primer.'
)

# Section I locate — end of locate block
r1 = upgrade(r1,
    'This report is about that structure — and what changes when creative intelligence is understood as a system property rather than a personal trait.'
)

# Section I prose — system design
r1 = upgrade(r1,
    "in the system's design — in its meeting formats, its performance metrics, its reward structures, its implicit rules about who speaks and what gets heard."
)

# Section I prose — documented practice
r1 = upgrade(r1,
    'THE ÅLïEN SCõÖL\'s documented practice — across scholars, consultants, educators, community builders, and organizational leaders — shows a consistent pattern:'
)

# Section II prose — parameters
r1 = upgrade(r1,
    'parameters — numbers, rates, individual behaviors — produce the least durable change.'
)

# Section II thinker-body (Meadows) — interventions
r1 = upgrade(r1,
    'The highest-leverage interventions — those most capable of producing durable transformation — operate at the level of goals, paradigms, and the power to transcend paradigms.'
)

# Section III thinker-body (Scharmer) — U process
r1 = upgrade(r1,
    'His five-movement U process — co-initiating, co-sensing, presencing, co-creating, co-evolving — maps closely to the tÅs methodology\'s Pause, Pivot, Merge structure:'
)

# Section III prose — actually holds
r1 = upgrade(r1,
    'Creative Awareness is the capacity to perceive what a situation actually holds — including the potential that existing mental models are actively filtering out.'
)

# Section III prose — teachable and transferable
r1 = upgrade(r1,
    'Creative Awareness is teachable and transferable — but only under specific conditions.'
)

# Section III evidence — navigation problem
r1 = upgrade(r1,
    'The consulting engagement reframed it as a creative culture problem — a mismatch between the school\'s narrative and the intelligence of its community.'
)

# Section III evidence — organizational navigation
r1 = upgrade(r1,
    'The Creative Director\'s sessions applied design thinking not to his output but to the organizational navigation problem itself — producing stated increases in confidence and professional influence.'
)

# Pullquote body paragraph
r1 = r1.replace(
    'can be designed to invite</em> — and any person can develop when the conditions support it.',
    'can be designed to invite</em> :: and any person can develop when the conditions support it.'
)

# Section IV prose — permissioned
r1 = upgrade(r1,
    'creative thinking is permissioned — that you contribute creatively when your role entitles you to, when the problem is in your domain, when you have been asked.'
)

# Section V prose intro — ongoing operation
r1 = r1.replace(
    "ongoing operation — visible in how meetings are structured, how decisions are made, how people are heard, how silence is held, how the question",
    "ongoing operation :: visible in how meetings are structured, how decisions are made, how people are heard, how silence is held, how the question"
)

# Section V prop 05 — guide function
r1 = upgrade(r1,
    'can develop — and that any leader can choose to exercise in any meeting, at any level of the hierarchy.'
)

# Section VI — not as discussion prompts
r1 = upgrade(r1,
    'Not as discussion prompts — as genuine inquiries the systems change educator holds while speaking, and offers to the audience as invitations rather than assignments.'
)

# Closing paragraph
r1 = upgrade(r1,
    'The follow-on conversation — what does this look like as a workshop, a partnership, an organizational intervention — lives in the exchanges that follow the session, not in the session itself.'
)

with open(R1, 'w', encoding='utf-8') as f:
    f.write(r1)
print('Report 1 additional em dashes applied.')


# ══════════════════════════════════════════════════════════════════
# REPORT TWO — all three sweeps (first pass never wrote this file)
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
r2 = upgrade(r2, 'Graham Wallas — The Art of Thought (1926)')
r2 = upgrade(r2, 'Teresa Amabile — Creativity in Context (1996)')
r2 = upgrade(r2, 'adrienne maree brown — Emergent Strategy (2017)')
r2 = upgrade(r2, 'Donella Meadows — Leverage Points: Places to Intervene in a System (1999)')

# ── SWEEP 2 · narrative body em dashes ───────────────────────────

# Cover subtitle
r2 = upgrade(r2, 'systems — and advocating for Creative Thinking as a daily practice, not a scheduled event.')

# Section I locate
r2 = upgrade(r2, 'a connection arrived that surprised you — something from an unrelated domain that turned out to be exactly the thing the problem needed.')
r2 = upgrade(r2, 'you were doing something you love — cooking, walking, gardening, listening to music — and an insight about your work arrived without being asked for.')

# Section I prose
r2 = upgrade(r2, 'it is not a fixed trait — it is a quality of cognitive engagement that responds to conditions.')

# Section I couplet
r2 = upgrade(r2, "not the individual's capacity — it is the system's relationship to that capacity.")

# Section II intro prose
r2 = upgrade(r2, 'from the tÅs session archive — relationships between conditions and the quality of creative thinking they produce.')

# Dynamic 01 body
r2 = upgrade(r2, 'after a period of incubation — what the tÅs methodology calls steeping — in which the problem or question has been held with attention but without pressure to resolve.')
r2 = upgrade(r2, 'Not because the people are less capable — because the conditions removed the incubation stage.')
r2 = upgrade(r2, 'hold that distinction — between avoidance and steeping — has access to a fundamentally different quality of facilitation.')

# Dynamic 01 evidence
r2 = upgrade(r2, 'shows insights arriving between sessions — not during them.')

# Dynamic 02 body
r2 = upgrade(r2, 'The insight that arrives as a felt sense — before it has language — is the most generative stage of the creative process.')
r2 = upgrade(r2, 'their felt sense — before they have formulated it into a presentable idea — is working with the actual dynamic of creative thinking rather than against it.')

# Dynamic 02 evidence
r2 = r2.replace(
    'named the sessions as "spiritual but therapeutic" in week one — before being told what they were designed to do.',
    'named the sessions as "spiritual but therapeutic" in week one :: before being told what they were designed to do.'
)
r2 = upgrade(r2, 'morning ritual — lavender, matcha, the warmth of the cup — became the somatic anchor that carried the session\'s work into his daily life.')

# Dynamic 03 body
r2 = upgrade(r2, 'not about praise or validation — it is about whether the environment treats the person\'s existing intelligence as a contribution worth receiving.')
r2 = upgrade(r2, 'The effect is structural — it removes the defensive posture that most evaluative environments produce and replaces it with the engaged receptivity that creative thinking requires.')

# Dynamic 03 evidence
r2 = upgrade(r2, 'did not add new capability — they changed his relationship to the capability he already held.')

# Dynamic 04 body
r2 = upgrade(r2, 'ways of knowing — held in a container that allowed the difference to be productive rather than threatening.')
r2 = upgrade(r2, 'UNION — Unified Non-Identical Intelligences Operating Naturally — names the structural principle')
r2 = upgrade(r2, 'The well-designed container does not smooth the difference — it holds it long enough for the productive encounter to occur.')

# Dynamic 04 evidence (public Biennale collaboration — both em dashes)
r2 = upgrade(r2, 'The Bombay Beach Biennale installation — SCAR Wash merged with Catarina\'s Thread of Life into Birth, Life, and Becoming — produced a work neither could have made alone.')

# Dynamic 05 body
r2 = upgrade(r2, 'quality of attention creative thinking requires — across the distance between formal sessions, without requiring a new event to reactivate it.')

# Dynamic 05 evidence
r2 = upgrade(r2, 'changed — three domains of daily life altered through daily practice sustained after the formal sessions ended.')

# Pullquote body
r2 = r2.replace(
    '<em>operates in people</em> — more or less accessibly, depending on the conditions the system creates around them.',
    '<em>operates in people</em> :: more or less accessibly, depending on the conditions the system creates around them.'
)

# Section III intro
r2 = upgrade(r2, 'The tÅs experiential equations — observable patterns extracted from documented sessions — translate directly into systems language.')

# Section IV advocacy
r2 = upgrade(r2, 'UNION — Unified Non-Identical Intelligences Operating Naturally — is not only a creative principle')
r2 = upgrade(r2, "the most durable change happens at the level of paradigm and mindset — Meadows's highest-leverage interventions.")
r2 = upgrade(r2, 'their felt sense — through structured reflection, embodied practices, or simply the quality of attention the facilitator brings to the space.')

# Section V thinkers
r2 = upgrade(r2, 'Wallas identified four stages of the creative process — preparation, incubation, illumination, and verification — nearly a century ago.')
r2 = upgrade(r2, 'intrinsic motivation — working on a task because it is inherently interesting and engaging — consistently produces higher-quality creative thinking than extrinsic motivation tied to evaluation or reward.')
r2 = upgrade(r2, "creative capacity — it is how that capacity is sustained.")
r2 = upgrade(r2, 'Shifting that assumption — through education, through lived evidence, through the design of conditions that make it visibly false — is high-leverage work.')

# Section VI provocation
r2 = upgrade(r2, 'worth holding while speaking — and worth offering to the room as genuine invitations rather than rhetorical moves.')
r2 = upgrade(r2, 'Not what it intends to do — what it is actually doing.')
r2 = upgrade(r2, 'What daily practice could your system adopt — not as a program, but as a rhythm — that would maintain the conditions for creative thinking between formal interventions?')
r2 = upgrade(r2, 'apply their own expertise — systems thinking, leverage points, feedback loops — to the advocacy for creative thinking, rather than treating creative thinking as separate from the systems work they already know how to do.')

# Closing
r2 = upgrade(r2, "with observable patterns — and for making the case that those dynamics are relevant to, and available to, the systems change education community's own work.")

# ── SWEEP 3 · Anonymity — attribution tags ───────────────────────
r2 = r2.replace('Daniel R · Dec 2024–May 2025',  'THE WELLNESS TEACHER · DEC 2024–MAY 2025')
r2 = r2.replace('David H · 2025',                'THE VISUAL DESIGNER · 2025')
r2 = r2.replace('Kristen B · Jul 2025',           'THE FILMMAKER · JUL 2025')
r2 = r2.replace('Brandon W · Aug 2025',           'THE MUSICIAN · AUG 2025')
r2 = r2.replace('Keith C · Jul 2025',             'THE CREATIVE DIRECTOR · JUL 2025')
r2 = r2.replace(
    'Kaelo L, Desmond, Jena D, Makhosi M · 2025–2026',
    'THE EDUCATOR, THE ENTREPRENEUR, THE CREATIVE PRODUCER, THE ECOSYSTEM BUILDER · 2025–2026'
)
r2 = r2.replace('Doug B · Apr 2025', 'THE EXECUTIVE · APR 2025')

with open(R2, 'w', encoding='utf-8') as f:
    f.write(r2)
print('Report 2 all sweeps applied.')
print('\nDone. QWP removed · Em dashes upgraded · Scholar identities anonymized.')
