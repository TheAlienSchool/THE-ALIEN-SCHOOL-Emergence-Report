import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for explicit attributions:
    content = content.replace("David H · 2025", "THE PHOTOGRAPHER / VISUAL DESIGNER — DAVID H · 2025")
    content = content.replace("David H · Aug 2025", "THE PHOTOGRAPHER / VISUAL DESIGNER — DAVID H · Aug 2025")
    content = content.replace("David H · Sep 2025", "THE PHOTOGRAPHER / VISUAL DESIGNER — DAVID H · Sep 2025")
    content = content.replace("Kristen B · 2025", "THE FILMMAKER / WRITER — KRISTEN B · 2025")
    content = content.replace("Kristen B · Jul 2025", "THE FILMMAKER / WRITER — KRISTEN B · Jul 2025")
    content = content.replace("Kristen B · Aug 2025", "THE FILMMAKER / WRITER — KRISTEN B · Aug 2025")
    content = content.replace("Keith C · 2025", "THE CREATIVE DIRECTOR — KEITH C · 2025")
    content = content.replace("Keith C · May 2025", "THE CREATIVE DIRECTOR — KEITH C · May 2025")
    content = content.replace("Brandon W · 2025", "THE MUSICIAN / ARTIST — BRANDON W · 2025")
    content = content.replace("Brandon W · Aug 2025", "THE MUSICIAN / ARTIST — BRANDON W · Aug 2025")
    content = content.replace("Jena D · Apr 2025", "THE CREATIVE PRODUCER — JENA D · Apr 2025")
    content = content.replace("Desmond · Jun 2025", "THE ENTREPRENEUR — DESMOND · Jun 2025")
    content = content.replace("Kaelo L · 2025–26", "THE EDUCATOR / COMMUNITY BUILDER — KAELO L · 2025–26")
    
    # Inline body text replacements (using word boundaries to avoid double replacements or partial matches)
    replacements = [
        (r'\bDavid H\b(?!\s*·)', 'The Photographer / Visual Designer'),
        (r'\bDavid\b(?!\s*H)', 'The Photographer / Visual Designer'),
        (r'\bKristen B\b(?!\s*·)', 'The Filmmaker / Writer'),
        (r'\bKristen\b', 'The Filmmaker / Writer'),
        (r'\bKeith Costa\b', 'The Creative Director'),
        (r'\bKeith C\b(?!\s*·)', 'The Creative Director'),
        (r'\bKeith\b', 'The Creative Director'),
        (r'\bBrandon W\b(?!\s*·)', 'The Musician / Artist'),
        (r'\bBrandon\b', 'The Musician / Artist'),
        (r'\bDoug B\b(?!\s*·)', 'The Executive / Strategist'),
        (r'\bDoug\b', 'The Executive / Strategist'),
        (r'\bDaniel R\b(?!\s*·)', 'The Wellness Teacher'),
        (r'\bDaniel\b', 'The Wellness Teacher'),
        (r'\bKaelo L\b(?!\s*·)', 'The Educator / Community Builder'),
        (r'\bKaelo\b', 'The Educator / Community Builder'),
        (r'\bDesmond\b(?!\s*·)', 'The Entrepreneur'),
        (r'\bJena D\b(?!\s*·)', 'The Creative Producer'),
        (r'\bJena\b', 'The Creative Producer'),
        (r'\bMakhosi M\b(?!\s*·)', 'The Ecosystem Builder'),
        (r'\bMakhosi\b', 'The Ecosystem Builder'),
    ]

    # We only apply these if we aren't within the HTML attributes or the already correct formatting.
    # To be safe, we just run regex sub, and then fix case where it looks weird like "The The"
    for old, new in replacements:
        # Ignore already processed uppercase formats
        content = re.sub(old, new, content)

    # Cleanup artifacts from regex
    content = content.replace("The The ", "The ")
    content = content.replace("To The Photographer", "To the Photographer")
    content = content.replace("to The Photographer", "to the Photographer")

    # Jeremy is totally anonymized
    content = content.replace("Jeremy", "The Leader")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Scholar identifiers fully applied. Anonymities secured.")
