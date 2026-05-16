#!/usr/bin/env python3
"""
remove_client_names.py
Full sweep — delete all client names from the archive.
"""

import os, glob

BASE = r'C:\Users\Kzaka\Documents\GitHub\tas-artifacts'

def sweep(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    log = []
    for old, new in replacements:
        count = content.count(old)
        if count:
            content = content.replace(old, new)
            log.append(f'  [{count}x] {repr(old[:70])} → {repr(new[:70])}')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return log

# ══════════════════════════════════════════════════════════════════
# proof-of-field.html
# ══════════════════════════════════════════════════════════════════

POF = os.path.join(BASE, 'artifacts', 'proof-of-field.html')

log = sweep(POF, [

    # ── Scholar section headers and scholar-name elements ─────────
    ('The Wellness Teacher Richards :: <em>The Trailing Notes</em>',
     'The Wellness Teacher :: <em>The Trailing Notes</em>'),
    ('The Executive / Strategist Berger :: <em>The Complete Semester</em>',
     'The Executive / Strategist :: <em>The Complete Semester</em>'),

    # ── Prose intro (Part II header text) ─────────────────────────
    ('The Wellness Teacher Richards, whose Trailing Notes',
     'The Wellness Teacher, whose Trailing Notes'),
    ('and The Executive / Strategist Berger, whose complete semester',
     'and The Executive / Strategist, whose complete semester'),

    # ── All sv-source citation lines ─────────────────────────────
    (', The Wellness Teacher Richards',
     ''),
    ('by The Wellness Teacher Richards',
     'by The Wellness Teacher'),
    ('The Executive / Strategist Berger ::',
     'The Executive / Strategist ::'),
    ('The Filmmaker / Writer M Beury ::',
     'The Filmmaker / Writer ::'),

    # ── Attribution tags with initials ────────────────────────────
    ('The Wellness Teacher R ·',         'The Wellness Teacher ·'),
    ('The Executive / Strategist B ·',   'The Executive / Strategist ·'),
    ('The Educator / Community Builder L ·', 'The Educator / Community Builder ·'),

    # ── Thread body text: David Hartz ─────────────────────────────
    ('sessions with David Hartz,',
     'sessions with The Visual Designer,'),
    ('David Hartz naming his studio demolition a sand mandala.',
     'The Visual Designer naming his studio demolition a sand mandala.'),

    # ── Thread body text: Jesse Elliott ───────────────────────────
    ("Jesse Elliott's public showcase.",
     "A scholar's public showcase."),

    # ── Thread body text: John Leto ───────────────────────────────
    ('The session with John Leto where ancestral candles were lit.',
     'The session where ancestral candles were lit.'),

    # ── Thread body text: Hamilton ────────────────────────────────
    ("Hamilton's graduation at St. Peter's Prep in Jersey City",
     "A graduation at St. Peter's Prep in Jersey City"),

    # ── Closing signature ────────────────────────────────────────
    ('DANIEL RICHARDS AND DOUG BERGER ARCS INFUSED',
     'THE WELLNESS TEACHER AND EXECUTIVE / STRATEGIST ARCS INFUSED'),
])

print(f'proof-of-field.html:')
for line in log: print(line)

# ══════════════════════════════════════════════════════════════════
# frequency-report.html
# ══════════════════════════════════════════════════════════════════

FREQ = os.path.join(BASE, 'artifacts', 'frequency-report.html')

log2 = sweep(FREQ, [
    ('The Ecosystem Builder M ·', 'The Ecosystem Builder ·'),
])

print(f'\nfrequency-report.html:')
for line in log2: print(line)

# ══════════════════════════════════════════════════════════════════
# Broad sweep — any remaining name that slipped through other files
# ══════════════════════════════════════════════════════════════════

all_html = glob.glob(os.path.join(BASE, '*.html')) + \
           glob.glob(os.path.join(BASE, 'artifacts', '*.html'))

broad_replacements = [
    # Catch any standalone surname occurrences not already handled
    (' Richards', ''),
    (' Berger', ''),
    (' Elliott', ''),
    (' Beury', ''),
]

print('\nBroad remaining-name sweep across all HTML:')
for fpath in sorted(all_html):
    # Skip proof-of-field (already handled above with care)
    if 'proof-of-field' in fpath:
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    found = []
    for old, new in broad_replacements:
        count = content.count(old)
        if count:
            content = content.replace(old, new)
            found.append(f'  [{count}x] {repr(old)} removed')
    if found:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        fname = os.path.relpath(fpath, BASE)
        print(f'  {fname}:')
        for f_line in found: print(f_line)

print('\nClient name sweep complete.')
