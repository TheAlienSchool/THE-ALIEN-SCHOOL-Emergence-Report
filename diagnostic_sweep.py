import os
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
files_to_check = [
    'elevation-codex.html', 'proof-of-field.html', 
    'frequency-report.html', 'metaphor-library.html', 
    'field-notes.html', 'magnet-ellian.html', 
    'magnet-clops.html', 'magnet-dragonfly.html'
]

knots = [r'\bdoes not\b', r'\bis not\b', r'\bare not\b', r'\bdo not\b', r'\bwill not\b', r'\bcannot\b', r'\bnever\b', r'\bnot just\b']
ambiguities = [r'\bsomething\b', r'\bsomeone\b', r'\bthings\b', r'\bthing\b']

print("--- KNOTS & NEGATIONS ---")
for filename in files_to_check:
    filepath = os.path.join(artifacts_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            for knot in knots:
                if re.search(knot, line, re.IGNORECASE):
                    # Filter out CSS and HTML attributes that might have 'does not' accidentally? Unlikely.
                    if '<style>' in line or 'display: none' in line or 'function' in line:
                        continue
                    clean_line = re.sub('<[^<]+>', '', line).strip()
                    if len(clean_line) > 0 and 'script' not in clean_line.lower():
                        print(f"[{filename}:{i+1}] {knot}: {clean_line[:150]}")

print("\n--- AMBIGUITIES ---")
for filename in files_to_check:
    filepath = os.path.join(artifacts_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            for amb in ambiguities:
                if re.search(amb, line, re.IGNORECASE):
                    clean_line = re.sub('<[^<]+>', '', line).strip()
                    if len(clean_line) > 0 and 'script' not in clean_line.lower():
                        print(f"[{filename}:{i+1}] {amb}: {clean_line[:150]}")
