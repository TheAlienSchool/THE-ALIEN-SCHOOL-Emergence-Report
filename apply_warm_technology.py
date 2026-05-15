import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply Warm Technology typography corrections
    
    # 1. Strip EB Garamond dependency and default to H70 sans-serif
    content = content.replace("font-family: 'EB Garamond', serif;", "font-family: var(--h70-font);")
    
    # 2. Convert mass italicization to normal font-style for dyslexia readability
    # (We replace font-style: italic; with font-style: normal;)
    content = content.replace("font-style: italic;", "font-style: normal;")
    
    # 3. Increase base line-height from 1.7 or 1.6 to 1.75 for breathing room
    content = re.sub(r'line-height:\s*1\.[67]\d*;', 'line-height: 1.75;', content)
    
    # 4. Limit max-width of prose to 65ch for ADHD scanning
    content = content.replace("max-width: 680px;", "max-width: 65ch; margin-left: 0;")
    content = content.replace("max-width: 560px;", "max-width: 65ch; margin-left: 0;")
    content = content.replace("max-width: 580px;", "max-width: 65ch; margin-left: 0;")
    
    # 5. Left align text globally in the artifacts where it was centered
    content = content.replace("text-align: center;", "text-align: left;")
    
    # 6. Ensure .h70-body is applied to paragraphs inside .prose and .review
    content = re.sub(r'<p>', '<p class="h70-body">', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Warm Technology accessibility vectors applied to all artifacts.")
