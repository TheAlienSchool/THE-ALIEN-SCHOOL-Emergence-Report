import os

replacements = {
    # proof-of-field.html
    "knowing something was out of alignment": "knowing the structure was out of alignment",
    "because something in him recognized the register": "because his nervous system recognized the register",
    "produce something richer than either generates alone": "produce a geometry richer than either generates alone",
    "installation of something new": "installation of a foreign system",
    "Honoring someone's perspective requires": "Honoring a scholar's perspective requires",
    
    # metaphor-library.html
    "edge of something they had never said aloud": "edge of a truth they had never said aloud",
    "and the thing landed": "and the concept landed",
    "generate something richer than either produces alone": "generate an architecture richer than either produces alone",
    "close of something meaningful": "close of a meaningful era",
    "sense something unexpressed": "sense an unexpressed capacity",
    "gives something forward rather than abandoning something behind": "gives a narrative forward rather than abandoning a burden behind",
    "given language for something they already carry": "given language for an intelligence they already carry",
    "someone things happened to": "a passive subject",
    "to the position of someone who designed": "to the position of an active architect",
    "converting them into something useful": "converting them into an asset useful",

    # frequency-report.html
    "You know you carry something.": "You know you carry an original frequency.",
    "ready for something structurally different": "ready for an entirely different architecture",
    "When someone offers you a framework": "When a guide offers you a framework",
    "something in you recognizes it": "your internal compass recognizes it",
    "when something you have always known": "when a truth you have always known",
    "felt click of something landing": "felt click of an insight landing",
    "assumes the thing was never present": "assumes the capacity was never present",

    # field-notes.html
    "Five Things This Work Demonstrates": "Five Core Proofs This Work Demonstrates",
    "Five Things This <em>Work</em> Demonstrates": "Five Core Proofs This <em>Work</em> Demonstrates",
    "conditions for something he could not yet name": "conditions for a frequency he could not yet name",
    "pull new things from me": "pull new dimensions from me",
    "The only thing standing between you": "The only boundary standing between you",
    "toward something neither could produce alone": "toward an outcome neither could produce alone",

    # elevation-codex.html
    "names something about themselves": "names a truth about themselves",
    "Something in them already knows this is right.": "Their structural intuition already knows this is right.",
    "a thing they mention in passing": "a detail they mention in passing",

    # index.html & general cleanup
    "doing things": "executing patterns",
    "the same thing": "the exact resonance",
    "the whole thing": "the entire structure",
    "some things": "specific variables"
}

target_dirs = [
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts",
    r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts"
]

files_to_sweep = [
    'proof-of-field.html', 'metaphor-library.html', 'frequency-report.html',
    'field-notes.html', 'elevation-codex.html', 'magnet-ellian.html',
    'magnet-clops.html', 'magnet-dragonfly.html', 'index.html',
    'sceu-report-one-integrating-creative-thinking.html',
    'sceu-report-two-illuminating-creative-thinking.html'
]

total_replacements = 0

for d in target_dirs:
    for filename in files_to_sweep:
        filepath = os.path.join(d, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            for old_text, new_text in replacements.items():
                if old_text in content:
                    content = content.replace(old_text, new_text)
                    total_replacements += content.count(new_text) # Rough estimate

            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Swept {filename}")

print(f"Ambiguity sweep complete. Replaced key ambiguous terms across {len(files_to_sweep)} core files.")
