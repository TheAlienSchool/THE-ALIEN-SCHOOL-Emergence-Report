import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remap the root variables to H70 variables
    root_replacement = """  :root {
    --bg:         transparent;
    --ink:        var(--h70-ink);
    --deep:       var(--h70-ink);
    --muted:      var(--h70-muted);
    --border:     var(--h70-line);
    --border-lt:  var(--h70-line);
    --warm:       var(--h70-surface);
    --gold:       var(--h70-signal);
    --gold-pale:  var(--h70-surface);
    --teal:       var(--h70-signal);
    --teal-pale:  var(--h70-surface);
    --scholar:    var(--h70-ink);
    --scholar-lt: var(--h70-surface);
    --review:     var(--h70-signal);
    --review-lt:  var(--h70-surface);
    --rule:       var(--h70-line);
  }"""
    content = re.sub(r':root\s*\{[^}]+\}', root_replacement, content)

    # 2. Fix typography
    content = re.sub(r"font-family:\s*['\"]EB Garamond['\"][^;]*;", "font-family: var(--h70-font);", content)
    content = re.sub(r"font-family:\s*['\"]Playfair Display['\"][^;]*;", "font-family: var(--h70-font);", content)
    content = re.sub(r"font-family:\s*var\(--fSerif\);", "font-family: var(--h70-font);", content)
    content = re.sub(r"font-family:\s*var\(--fBody\);", "font-family: var(--h70-font);", content)
    
    # 3. Strip italics
    content = re.sub(r'font-style:\s*italic;', 'font-style: normal;', content)
    content = re.sub(r'em\s*\{([^}]+)font-style:\s*italic;([^}]+)\}', r'em {\1 font-style: normal;\2}', content)

    # 4. Remove old noise/grain
    content = re.sub(r'body::before\s*\{[^}]+\}', '', content)
    
    # 5. Fix hardcoded colors causing accessibility disasters in inverted blocks (.field-close)
    content = re.sub(r'color:\s*#f0e8d4;', 'color: var(--bg);', content)
    content = re.sub(r'color:\s*#c8a040;', 'color: var(--gold);', content)
    content = re.sub(r'color:\s*rgba\(200,180,138,0\.82\);', 'color: var(--bg); opacity: 0.9;', content)
    content = re.sub(r'color:\s*rgba\(196,180,136,0\.5\);', 'color: var(--bg); opacity: 0.7;', content)
    
    # 6. Any stray white text or light text hardcodes should be cleared
    content = re.sub(r'color:\s*#fff(?:fff)?;', 'color: var(--ink);', content)
    
    # Ensure paragraphs are readable length
    # previously I used a regex that might have failed if it wasn't exact
    if '.prose {' in content:
         content = re.sub(r'\.prose\s*\{[^}]+\}', '.prose { max-width: 65ch; margin-left: 0; }', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Artifacts remapped to consume H70 variables and Warm Technology typographics. Hardcoded contrast errors destroyed.")
