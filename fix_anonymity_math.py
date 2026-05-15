import os
import glob

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Scrub the exposed identities from the tags
    content = content.replace(" — DAVID H", "")
    content = content.replace(" — KRISTEN B", "")
    content = content.replace(" — KEITH C", "")
    content = content.replace(" — BRANDON W", "")
    content = content.replace(" — DOUG B", "")
    content = content.replace(" — DANIEL R", "")
    content = content.replace(" — KAELO L", "")
    content = content.replace(" — DESMOND", "")
    content = content.replace(" — JENA D", "")
    content = content.replace(" — MAKHOSI M", "")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Anonymity mathematics corrected. Identities scrubbed.")
