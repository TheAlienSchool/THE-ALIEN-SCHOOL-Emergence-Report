#!/usr/bin/env python3
"""
apply_sceu_affirmative.py
PRIMER sweep — affirmative architecture + redundancy removal.
Targets: deficit spending inside quotes and abstract examples.
Leaves: functional contrasts, direct external quotes, image-earning negations.
"""

import os
BASE = r'C:\Users\Kzaka\Documents\GitHub\tas-artifacts'

# ══════════════════════════════════════════════════════════════════
# REPORT ONE
# ══════════════════════════════════════════════════════════════════

R1 = os.path.join(BASE, 'sceu-report-one-integrating-creative-thinking.html')
with open(R1, 'r', encoding='utf-8') as f:
    r1 = f.read()

changes_r1 = []

# ── SECTION I LOCATE: "not a failure" → affirmative ───────────────
OLD = 'That gap is not a failure of individual talent. It is a structural condition.'
NEW = 'That gap is a structural condition :: held in the design, not in the limitations of any person inside it.'
r1 = r1.replace(OLD, NEW); changes_r1.append(('R1 S1 locate', OLD[:60], OLD in r1 or NEW in r1))

# ── COUPLET QUOTE: lead with the positive ────────────────────────
OLD = '"Creativity in an organization is not the output of the creative team. It is the quality of thinking available to the whole system when its conditions allow it to surface."'
NEW = '"Creativity in an organization lives in the quality of thinking available to the whole system when its conditions allow it to surface."'
r1 = r1.replace(OLD, NEW); changes_r1.append(('R1 couplet', OLD[:60], NEW in r1))

# ── SECTION II REDUNDANCY: "The system did not change." ───────────
# Sentence is redundant with "transfer rarely holds" and "adapted back"
OLD = 'Within weeks, the workshop\'s energy has been metabolized by the system it entered. The system did not change. The person changed temporarily, then adapted back.'
NEW = 'Within weeks, the workshop\'s energy has been metabolized by the system it entered. The person changed temporarily, then adapted back.'
r1 = r1.replace(OLD, NEW); changes_r1.append(('R1 S2 redundancy', OLD[:60], NEW in r1))

# ── SECTION III EVIDENCE: "not to...but to" → affirmative ────────
OLD = 'applied design thinking not to his output but to the organizational navigation problem itself'
NEW = 'turned design thinking toward the organizational navigation problem itself'
r1 = r1.replace(OLD, NEW); changes_r1.append(('R1 S3 evidence CD', OLD[:60], NEW in r1))

# ── SECTION III EVIDENCE REDUNDANCY: "A different awareness..." ───
OLD = 'A different awareness produced a different intervention.'
NEW = ''
# Replace the sentence including its leading space after the period
r1 = r1.replace(' A different awareness produced a different intervention.', '')
changes_r1.append(('R1 S3 evidence redundancy', OLD[:60], OLD not in r1))

# ── SECTION V PROP 02: "not a change in...capacity" → affirmative ─
OLD = 'The Creative Director\'s documented shift was not a change in his creative capacity :: it was a change in his relationship to his own authority to express it.'
NEW = 'The Creative Director\'s documented shift was a change in his relationship to his own authority to express what was already present.'
r1 = r1.replace(OLD, NEW); changes_r1.append(('R1 prop 02', OLD[:60], NEW in r1))

# ── SECTION V PROP 05: "not providing answers, but" → affirmative ─
OLD = 'not providing answers, but creating the conditions in which the system\'s own intelligence becomes available to itself.'
NEW = 'creating the conditions in which the system\'s own intelligence becomes available to itself.'
r1 = r1.replace(OLD, NEW); changes_r1.append(('R1 prop 05', OLD[:60], NEW in r1))

# ── SECTION VI Q3: "not just a personal trait" → affirmative ─────
OLD = 'not just a personal trait?'
NEW = 'a structural property the whole system draws from?'
r1 = r1.replace(OLD, NEW); changes_r1.append(('R1 S6 Q3', OLD[:60], NEW in r1))

with open(R1, 'w', encoding='utf-8') as f:
    f.write(r1)

print('REPORT 1 CHANGES:')
for label, snippet, ok in changes_r1:
    status = 'OK' if ok else 'MISS'
    print(f'  [{status}] {label}: {snippet}')


# ══════════════════════════════════════════════════════════════════
# REPORT TWO
# ══════════════════════════════════════════════════════════════════

R2 = os.path.join(BASE, 'sceu-report-two-illuminating-creative-thinking.html')
with open(R2, 'r', encoding='utf-8') as f:
    r2 = f.read()

changes_r2 = []

# ── COVER SUBTITLE: "not a scheduled event" → affirmative ────────
OLD = 'A session on seeing creativity in action through systems :: and advocating for Creative Thinking as a daily practice, not a scheduled event.'
NEW = 'A session on seeing creativity in action through systems :: and advocating for Creative Thinking as a daily practice :: a living rhythm available to every encounter.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 cover sub', OLD[:60], NEW in r2))

# ── SECTION I CLAIM: "not an argument about talent" → affirmative ─
OLD = 'This is not an argument about talent. It is an argument about conditions.'
NEW = 'This is an argument about conditions :: what they support and what they make possible.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 S1 claim', OLD[:60], NEW in r2))

# ── SECTION I PROSE: "not primarily cognitive" → affirmative ─────
OLD = 'the conditions most supportive of creative thinking are not primarily cognitive. They are somatic, relational, and temporal.'
NEW = 'the conditions most supportive of creative thinking are somatic, relational, and temporal.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 S1 cognitive', OLD[:60], NEW in r2))

# ── SECTION I COUPLET: "not the individual's capacity" → affirmative
OLD = '"Creative Thinking has dynamics that can be illuminated. When they are seen clearly, they can be designed for. What changes is not the individual\'s capacity :: it is the system\'s relationship to that capacity."'
NEW = '"Creative Thinking has dynamics that can be illuminated. When they are seen clearly, they can be designed for. What changes is the system\'s relationship to a capacity that was already present."'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 couplet', OLD[:60], NEW in r2))

# ── DYNAMIC 01: "Not because the people are less capable" → affirm.
OLD = 'Not because the people are less capable :: because the conditions removed the incubation stage.'
NEW = 'The conditions removed the incubation stage :: the capacity of the people inside them remains intact.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 D01 not-because', OLD[:60], NEW in r2))

# ── DYNAMIC 01: "not through periodic intensive interventions" ────
OLD = 'not through periodic intensive interventions but through the establishment of small, daily practices that maintain the conditions creative thinking requires.'
NEW = 'through the establishment of small, daily practices that maintain the conditions creative thinking requires.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 D01 not-through', OLD[:60], NEW in r2))

# ── DYNAMIC 02: "not about praise or validation" → affirmative ───
OLD = 'This is not about praise or validation :: it is about whether the environment treats the person\'s existing intelligence as a contribution worth receiving.'
NEW = 'It is about whether the environment treats the person\'s existing intelligence as a contribution worth receiving.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 D02 not-praise', OLD[:60], NEW in r2))

# ── DYNAMIC 02 REDUNDANCY: collapse two sentences into one ───────
OLD = 'An insight with a body address holds. An insight that lives only in language evaporates between meetings.'
NEW = 'An insight with a body address holds :: it returns between meetings as usable knowing.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 D02 redundancy', OLD[:60], NEW in r2))

# ── DYNAMIC 03 EVIDENCE: "did not add new capability" → affirm. ──
OLD = 'The sessions did not add new capability :: they changed his relationship to the capability he already held.'
NEW = 'The sessions shifted his relationship to a capability he already held :: the confidence arrived when the relationship did.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 D03 evidence', OLD[:60], NEW in r2))

# ── DYNAMIC 04: cut opening negation sentence ────────────────────
# "did not emerge from homogeneous conversations" is redundant with the affirmative following sentence
OLD = 'The most generative creative thinking in the tÅs archive did not emerge from homogeneous conversations. It emerged from the encounter between genuinely different perspectives, experiences, and ways of knowing :: held in a container that allowed the difference to be productive rather than threatening.'
NEW = 'The most generative creative thinking in the tÅs archive emerged from the encounter between genuinely different perspectives, experiences, and ways of knowing :: held in a container that allowed the difference to be productive rather than threatening.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 D04 homogeneous', OLD[:60], NEW in r2))

# ── DYNAMIC 05: "does not need to be elaborate" → affirmative ────
OLD = 'The daily practice does not need to be elaborate.'
NEW = 'The daily practice is small, specific, and sustained.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 D05 elaborate', OLD[:60], NEW in r2))

# ── SECTION III EQ-NOTE 2: collapse cannot/cannot → affirmative ──
OLD = 'In systems language: feedback loops require accurate information. When the system\'s members cannot name what they are experiencing with enough precision to communicate it, the information cannot flow. Precise naming is a structural intervention that opens the feedback loop.'
NEW = 'In systems language: feedback loops require accurate information. Precise naming is the structural intervention that opens the flow :: when language matches experience, information moves through the system.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 S3 eq-note 2', OLD[:60], NEW in r2))

# ── SECTION IV ADVOCACY: "not a motivational claim" → remove ─────
OLD = 'That shift is not a motivational claim. It has practical consequences for how systems are designed, how learning environments are structured, and how organizational cultures treat the intelligence distributed throughout them.'
NEW = 'That shift carries practical consequences for how systems are designed, how learning environments are structured, and how organizational cultures treat the intelligence distributed throughout them.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 S4 not-motivational', OLD[:60], NEW in r2))

# ── SECTION IV DIRECTIVE 3: "not a coaching technique" → affirmative
OLD = 'The Permission Structure is a design principle, not a coaching technique.'
NEW = 'The Permission Structure is a design principle :: it belongs in the system\'s architecture before it belongs in the facilitator\'s repertoire.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 S4 permission', OLD[:60], NEW in r2))

# ── SECTION IV DIRECTIVE 5: "not only a creative principle" ──────
OLD = 'UNION :: Unified Non-Identical Intelligences Operating Naturally :: is not only a creative principle. It is a systems design principle.'
NEW = 'UNION :: Unified Non-Identical Intelligences Operating Naturally :: functions as a systems design principle.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 S4 UNION not-only', OLD[:60], NEW in r2))

# ── SECTION IV REDUNDANCY: container metaphor repeated ───────────
# Dynamic 05 already said "The daily practice is the container."
# Replace repetition with something that advances the advocacy.
OLD = 'The learning event that does not produce a daily practice is producing an experience without a container to carry it forward. The daily practice is the container. Systems that invest in the conditions for daily creative practice are investing in the sustained availability of creative thinking to the system\'s ongoing work.'
NEW = 'Systems that invest in the conditions for daily creative practice are investing in the sustained availability of the thinking their work requires.'
r2 = r2.replace(OLD, NEW); changes_r2.append(('R2 S4 container redundancy', OLD[:60], NEW in r2))

with open(R2, 'w', encoding='utf-8') as f:
    f.write(r2)

print('\nREPORT 2 CHANGES:')
for label, snippet, ok in changes_r2:
    status = 'OK' if ok else 'MISS'
    print(f'  [{status}] {label}: {snippet}')

print('\nAffirmative architecture sweep complete.')
