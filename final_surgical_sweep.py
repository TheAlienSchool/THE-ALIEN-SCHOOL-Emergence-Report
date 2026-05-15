import os

replacements = {
    # --- AMBIGUITIES ---
    "Something in them already knows this is right.": "Their internal architecture already knows this is right.",
    "Each one asks something different of the school's approach.": "Each one asks a distinct engagement of the school's approach.",
    "You have always known things through the body": "You have always known truths through the body",
    "drift to someone else who needs it more": "drift to the next scholar who needs it more",
    "Someone else may need it.": "The next practitioner may need it.",
    "gave him something worth writing down": "gave him material worth writing down",
    "gave him something worth returning to": "gave him a practice worth returning to",
    
    # --- KNOTS (Deficit Spending) ---
    "The school is not a philosophy that gestures toward human flourishing. It is a practice environment": "The school operates as a practice environment",
    "The school does not install the frequency. The school develops the conditions": "The school develops the conditions",
    "The school does not install creativity. It develops the conditions": "The school develops the conditions",
    "Rest is not what happens between the work. Rest is what makes the next work possible.": "Rest is the architecture that makes the next work possible.",
    "It is not the school's language. It is the scholar's distillation": "It operates independently of the school's language as the scholar's distillation",
    "Tea does not rush.": "Tea takes its exact required time.",
    "The answer to the right side of this equation is not fixed.": "The answer to the right side of this equation is inherently fluid.",
    "These are not claims about universal human experience. They are patterns": "These are specific patterns",
    "The documented changes in the scholar record are not abstractions:": "The documented changes in the scholar record are physical facts:",
    "do not typically value:": "typically bypass:",
    "what the school provides is not enrichment. It is essential maintenance.": "what the school provides is essential maintenance.",
    "These are not AI summaries of what was said. They are what the scholar kept.": "These represent exactly what the scholar kept.",
    "The rock and the ocean do not blend. They meet.": "The rock and the ocean meet.",
    "does not force its descent": "surrenders entirely to gravity",
    "never empty": "always transmitting",
    "never to be altered": "permanently fixed",
    "cannot fully name": "struggle to fully name",
    "cannot see the structure": "struggle to see the structure"
}

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
files_to_sweep = [
    'proof-of-field.html', 'metaphor-library.html', 'frequency-report.html', 
    'field-notes.html', 'elevation-codex.html', 'magnet-ellian.html', 
    'magnet-clops.html', 'magnet-dragonfly.html'
]

total_replacements = 0

for filename in files_to_sweep:
    filepath = os.path.join(artifacts_dir, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        for old_text, new_text in replacements.items():
            if old_text in content:
                content = content.replace(old_text, new_text)
                total_replacements += content.count(new_text)

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Surgically corrected {filename}")

print(f"Final surgical sweep complete. The geometry is fully intact.")
