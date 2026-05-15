import os
import re

# 1. Update the PRIMER
primer_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\VESSELVERSE_EDITORIAL_PROTOCOL3.1.md"
with open(primer_path, 'r', encoding='utf-8') as f:
    primer_content = f.read()

rule_addition = """
## 9.15 The Ambiguity Sweep
As a practice with the PRIMER, we must eliminate the words **"things"**, **"something"**, and **"someone"**.

These are overused ambiguities that wrestle the reader away from the central context. Humanity tends to lose the thread on what "things" are, as we are all made of a source giving us opportunity after opportunity to create from the environments we inhabit.

These placeholder words must be replaced with exact, structural nouns that carry precise meaning.

**Examples of correction:**
*   *Violation:* "Someone arrives carrying their history... and something in the conversation shifts the weight. They leave with language for something they already knew."
*   *Correction:* "A scholar arrives carrying their history... and a precise structural resonance in the conversation shifts the weight. They leave with language for the exact architecture they already possessed."

When a placeholder appears, ask: *What is the actual noun? Is it a frequency, a variable, a mechanism, a scholar, a coordinate, or an asset?* Name it.

---
"""

if "The Ambiguity Sweep" not in primer_content:
    primer_content = primer_content.replace("## 9.14 Internal Bibliography Addendum", rule_addition + "\n## 9.16 Internal Bibliography Addendum")
    with open(primer_path, 'w', encoding='utf-8') as f:
        f.write(primer_content)
    print("Updated VESSELVERSE_EDITORIAL_PROTOCOL3.1.md")

# 2. Update the specific paragraphs in the artifacts
artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
files_to_check = ['elevation-codex.html', 'proof-of-field.html', 'frequency-report.html', 'metaphor-library.html', 'field-notes.html']

old_p1 = "You have been doing this for a long time. Someone arrives :: carrying their history, their blocks, their partial self-knowledge :: and something in the conversation shifts the weight. They leave with language for something they already knew but had never found words for. They leave taller."
new_p1 = "You have been doing this for a long time. A scholar arrives :: carrying their history, their blocks, their partial self-knowledge :: and a precise structural resonance in the conversation shifts the weight. They leave with language for the exact architecture they already possessed but had never found words for. They leave taller."

old_p2 = "You are in a conversation with someone :: a scholar, a collaborator, a person at the edge of something :: and something shifts."
new_p2 = "You are in a conversation with a practitioner :: a scholar, a collaborator, a person at the edge of a new frequency :: and the structural geometry shifts."

for filename in files_to_check:
    filepath = os.path.join(artifacts_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        if old_p1 in content:
            content = content.replace(old_p1, new_p1)
            modified = True
        if old_p2 in content:
            content = content.replace(old_p2, new_p2)
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")
