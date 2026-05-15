import os
import glob
import re

css_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\harmonious70.css"
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Make STEAM SANS universal
css_content = re.sub(
    r"--h70-mono:\s*[^;]+;",
    "--h70-mono: 'STEAM SANS', 'DM Mono', ui-monospace, monospace;",
    css_content
)

# Apply Harris settings to h70-kicker
if "font-variation-settings: 'STBL' 0" not in css_content.split('.h70-kicker')[1].split('}')[0]:
    css_content = css_content.replace(
        ".h70-kicker {",
        ".h70-kicker {\n    font-variation-settings: 'STBL' 0, 'COHR' 100, 'DRFT' 0, 'PRSS' 24;"
    )

# Apply HBA settings to h70-body
if "font-variation-settings: 'STBL' 50" not in css_content.split('.h70-body')[1].split('}')[0]:
    css_content = css_content.replace(
        ".h70-body {",
        ".h70-body {\n    font-variation-settings: 'STBL' 50, 'COHR' 84, 'DRFT' 13, 'PRSS' 20;\n    animation: h70-hba-breathe var(--h70-breath-cycle) var(--h70-ease) infinite;"
    )

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css_content)

# Now fix the artifacts
artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix the audio overlay transparency issue (which caused the overlapping text in the screenshot)
    # The fix_artifact_styles.py accidentally made #audio-overlay transparent because it had background: var(--bg);
    # We will explicitly force #audio-overlay to use var(--h70-bg)
    content = re.sub(r'#audio-overlay\s*\{([^}]*)background:\s*transparent;', r'#audio-overlay {\1background: var(--h70-bg);', content)
    
    # Also if it doesn't have background: transparent anymore but was changed, ensure it's var(--h70-bg)
    if 'id="audio-overlay"' in content:
        # Let's just forcefully inject a style override for the overlay to be safe
        if '#audio-overlay { background: var(--h70-bg) !important; }' not in content:
            content = content.replace('</style>', '  #audio-overlay { background: var(--h70-bg) !important; }\n</style>')

    # 2. Make all typography universally STEAM SANS
    # Force prose and general paragraphs to use the HBA animation and settings
    if '.prose p { animation: h70-hba-breathe' not in content:
        content = content.replace('</style>', """  p, li, td, .prose p, .review p, .scholar-card-body p { 
    font-family: var(--h70-font);
    font-variation-settings: 'STBL' 50, 'COHR' 84, 'DRFT' 13, 'PRSS' 20;
    animation: h70-hba-breathe var(--h70-breath-cycle) var(--h70-ease) infinite;
  }
  .cover-stamp, .section-num, .locate-label, .review-label, .link-card-label {
    font-family: var(--h70-mono);
    font-variation-settings: 'STBL' 0, 'COHR' 100, 'DRFT' 0, 'PRSS' 24;
  }
  a:hover {
    font-variation-settings: 'STBL' 100, 'COHR' 48, 'DRFT' 34, 'PRSS' 12;
    filter: blur(.16px);
  }
</style>""")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("STEAM SANS universally applied. Audio overlay transparency fixed.")
