import os

# 1. Mobile Responsiveness for Tooltips & Links in index.html
index_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Enhance the tooltip CSS to be mobile friendly (iPhone 13 Pro Max)
if "@media (hover: none)" not in index_content:
    mobile_css = """
  @media (hover: none) and (pointer: coarse), (max-width: 768px) {
    .h70-tooltip {
      position: relative; top: 0; left: 0; transform: none; width: 100%; max-width: 100%;
      opacity: 1; visibility: visible; margin-top: 1rem; box-shadow: none; pointer-events: auto;
    }
    .h70-tooltip::before { display: none; }
    .h70-invitation-links { padding-left: 1rem !important; border-left-width: 1px !important; }
  }
"""
    index_content = index_content.replace("</style>", mobile_css + "</style>")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

# 2. Privacy & Co-Creation Acknowledgement in field-notes.html
field_notes_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts\field-notes.html"
with open(field_notes_path, 'r', encoding='utf-8') as f:
    fn_content = f.read()

# We want to add a paragraph to the Scholar Record section to honor the co-creation and privacy
honor_paragraph = """
      <p class="h70-body" style="margin-bottom: 2.5rem; padding-left: 1.5rem; border-left: 2px solid var(--h70-signal); opacity: 0.9;">
        <em>Privacy as a respectable politic.</em> The identifiers below honor the specific arcs of those who stepped into the field, while preserving the sanctity of the room. This record is presented as a matter of profound gratitude. The transformation documented here is not a service rendered by the school — it is the exact return on investment from what each scholar offered to what we co-created together.
      </p>
"""

if "Privacy as a respectable politic." not in fn_content:
    # Insert it right before <div class="scholar-grid">
    fn_content = fn_content.replace('<div class="scholar-grid">', honor_paragraph + '    <div class="scholar-grid">')

with open(field_notes_path, 'w', encoding='utf-8') as f:
    f.write(fn_content)

print("Cohesion cleanse complete. Mobile responsiveness added. Privacy and gratitude embedded.")
