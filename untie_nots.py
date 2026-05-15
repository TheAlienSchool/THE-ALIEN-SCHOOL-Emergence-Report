import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

# We also need to process index.html
index_file = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\index.html"
html_files.append(index_file)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Rule of Affirmative Architecture - Untying the Nots
    
    # 1. Elevation Codex
    content = content.replace("The Codex is a field guide, not a script.", "The Codex operates as a field guide.")
    content = content.replace("The elevation must be true at the scholar's current coordinate — not a future state dressed in present tense.", "The elevation must be true at the scholar's current coordinate.")
    content = content.replace("rather than just physical stillness — the breath is the practice, not the preparation for it.", "— the breath is the practice itself.")
    content = content.replace("not the container in which the work is placed, but the mechanism through which transformation occurs.", "the active mechanism through which transformation occurs.")
    content = content.replace("The rest was the practice, not the pause between practices.", "The rest was the practice itself.")
    content = content.replace("The five moves are not a sequence applied in order. They are simultaneous capacities", "The five moves operate as simultaneous capacities")
    
    # 2. Field Notes
    content = content.replace("THE ÅLïEN SCõÖL is not a coaching program. It is a practice environment", "THE ÅLïEN SCõÖL operates as a practice environment")
    content = content.replace("— not just to the work he produced within it.", "— expanding beyond the work he produced within it.")
    content = content.replace("Slowness is the active ingredient, not the obstacle.", "Slowness is the active ingredient.")
    content = content.replace("The Wellness Teacher's Know. Flow. Grow. was not given — it was built by the scholar", "The Wellness Teacher's Know. Flow. Grow. was built by the scholar")
    content = content.replace("This is not a client list — it is an ecology of conversations", "This functions as an ecology of conversations")
    content = content.replace("The school does not install creativity. It develops the conditions in which", "The school develops the conditions in which")
    content = content.replace("The guide does not supply new intelligence. The guide reflects", "The guide reflects")
    
    # Other potential nots
    content = content.replace("not just a", "a")
    content = content.replace("not a sign that you have failed", "the atmosphere already carrying you forward")
    content = content.replace("Rest is not the absence of creation, but", "Rest is")
    
    # Remove Invisible Authority Citations (QWP)
    content = re.sub(r'QUIET WARRIOR PRODUCTIONS(?:<br>|\s*·\s*|\\n)?', '', content)
    content = re.sub(r'· QUIET WARRIOR PRODUCTIONS', '', content)
    content = content.replace("QWP", "")

    # Ensure "The Leader" is explicitly "THE LEADER — JEREMY" as user asked if my last script missed it
    content = content.replace("THE LEADER</span>", "THE LEADER — JEREMY</span>")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Affirmative Architecture rules applied. Nots untied. QWP citations removed.")
