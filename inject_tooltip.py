import os
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
files = ['magnet-ellian.html', 'magnet-clops.html', 'magnet-dragonfly.html']

replacement_template = """<div class="cover-law" style="font-family: var(--h70-mono); font-size: 10px; letter-spacing: 0.12em; color: var(--teal); border-left: 2px solid var(--teal); padding-left: 1rem; line-height: 1.9; margin-top: 2.5rem; opacity: 0.8;">
        <details style="cursor: pointer;" class="sonic-link">
          <summary style="outline: none; color: var(--h70-signal); margin-bottom: 0.5rem; user-select: none; font-weight: 500;">CROSS-INDEXED ORIGINAL ARTIFACTS ∴</summary>
          <div style="margin-bottom: 1rem; opacity: 0.85; line-height: 1.6; border-left: 1px solid var(--h70-signal); padding-left: 1rem; color: var(--h70-muted); text-transform: none; font-family: var(--h70-font); font-size: 14px; letter-spacing: 0.04em;">
            <em>These are theories in research exploration that began as Steeping Notes for Kamau Zuberi Akabueze (KzA). Each SCHOLAR referenced here has worked directly with KzA, expanding this private dialogic context into public architectural evidence.</em>
          </div>
          <div style="padding-left: 1rem;">
            {list}
          </div>
        </details>
      </div>"""

for filename in files:
    filepath = os.path.join(artifacts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the artifacts list from the existing file
    match = re.search(r'<p class="cover-law"[^>]*>\s*Cross-Indexed Original Artifacts:<br>\s*(.*?)\s*</p>', content, re.DOTALL)
    if match:
        artifacts_list = match.group(1).strip()
        new_block = replacement_template.replace('{list}', artifacts_list)
        
        # Replace the entire <p class="cover-law">... block
        content = content[:match.start()] + new_block + content[match.end():]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find cover-law block in {filename}")
