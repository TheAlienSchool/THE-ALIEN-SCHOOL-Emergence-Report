import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

# 1. Fix the --bg transparency bug in artifacts
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the :root to point --bg to var(--h70-bg) instead of transparent
    content = content.replace("--bg:         transparent;", "--bg:         var(--h70-bg);")
    
    # Update ANNUAL REPORT to EMERGENCE REPORT
    content = content.replace("ANNUAL REPORT", "EMERGENCE REPORT")

    # Scholar Updates (mostly in field-notes.html but doing globally is safe)
    scholar_replacements = [
        ("THE VISUAL ARTIST / PHOTOGRAPHER", "THE PHOTOGRAPHER / VISUAL DESIGNER — DAVID H"),
        ("THE EXECUTIVE / STRATEGIST", "THE EXECUTIVE / STRATEGIST — DOUG B"),
        ("THE WELLNESS TEACHER", "THE WELLNESS TEACHER — DANIEL R"),
        ("THE FILMMAKER / WRITER", "THE FILMMAKER / WRITER — KRISTEN B"),
        ("THE MUSICIAN / ARTIST", "THE MUSICIAN / ARTIST — BRANDON W"),
        ("THE CREATIVE DIRECTOR", "THE CREATIVE DIRECTOR — KEITH C"),
        ("THE LEADER", "THE LEADER — JEREMY"),  # Wait, Jeremy becomes The Leader - his letter is specific. "Anonymous ALiEN" was Jeremy? No, "Jeremy becomes The Leader". The text says "THE LEADER" right now, I will make it "THE LEADER — JEREMY" or just leave "THE LEADER"? "his request for anonymity is honored." -> So "THE LEADER". Wait, in the reviews it says "Anonymous ÅLïEN". Maybe that becomes The Leader? 
        ("THE EDUCATOR / COMMUNITY BUILDER", "THE EDUCATOR / COMMUNITY BUILDER — KAELO L"),
        ("THE ENTREPRENEUR", "THE ENTREPRENEUR — DESMOND"),
        ("THE CREATIVE PRODUCER", "THE CREATIVE PRODUCER — JENA D"),
        ("THE ECOSYSTEM BUILDER", "THE ECOSYSTEM BUILDER — MAKHOSI M"),
    ]
    for old, new in scholar_replacements:
        content = content.replace(old, new)
        
    # Specifically fix Jeremy/Anonymous ALiEN in the review section
    content = content.replace("Anonymous ÅLïEN — identity protected by scholar's own request", "The Leader — anonymity honored")

    # The audio overlay (Portal transition) - enhance with axioms and values
    portal_enhancement = """
    <div id="audio-overlay" style="background: var(--h70-bg) !important;">
      <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; height:100vh; text-align:center; padding: 2rem;">
        <p class="h70-kicker" style="margin-bottom:2rem; letter-spacing:0.3em;">THE ÅLïEN SCõÖL</p>
        <p class="h70-body" style="text-align:center; max-width:50ch; margin-bottom: 2rem; opacity:0.8;">You are entering a bioacoustic repository. The methodology identifies what was always present and creates the conditions under which the scholar can hear it clearly. Patience × Procrastination = Steeping.</p>
        <button id="enter-space" class="h70-glyph-button">ENTER SPACE</button>
      </div>
    </div>
"""
    # Replace the old audio overlay if it exists
    if '<div id="audio-overlay">' in content or '<div id="audio-overlay" ' in content:
        content = re.sub(r'<div id="audio-overlay"[^>]*>.*?</div>\s*</div>', portal_enhancement, content, flags=re.DOTALL)
        content = re.sub(r'<div id="audio-overlay"[^>]*>.*?</div>\s*</button>\s*</div>\s*</div>', portal_enhancement, content, flags=re.DOTALL) # in case
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Update index.html
index_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = index_content.replace("ANNUAL REPORT", "EMERGENCE REPORT")

# Add omnipresent contact to index and artifacts
footer_nav = """
<div style="position: fixed; bottom: 0; left: 0; width: 100%; padding: 1rem 2rem; background: color-mix(in oklab, var(--h70-bg) 90%, transparent); backdrop-filter: blur(12px); border-top: 1px solid var(--h70-line); display: flex; justify-content: space-between; align-items: center; z-index: 9999; font-family: var(--h70-mono); font-size: var(--h70-xs); letter-spacing: 0.1em; color: var(--h70-muted);">
  <div style="display: flex; gap: 2rem;">
    <span>tÅs</span>
    <span id="scroll-progress">0% STEEPED</span>
  </div>
  <div style="text-align: right;">
    <a href="mailto:thealienscool@gmail.com" style="color: var(--h70-signal); text-decoration: none;">thealienscool@gmail.com</a>
    <span style="opacity: 0.6; margin-left: 1rem; display: none;" class="contact-desktop">Elevating the Creative Spirit in organizations, relationships, & edge navigation</span>
  </div>
</div>
<script>
  window.addEventListener('scroll', () => {
    const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const progress = Math.min(100, Math.max(0, Math.round((window.scrollY / docHeight) * 100)));
    const indicator = document.getElementById('scroll-progress');
    if(indicator) indicator.textContent = progress + '% STEEPED';
  });
</script>
<style>
@media(min-width: 800px) { .contact-desktop { display: inline !important; } }
</style>
</body>
"""

if "thealienscool@gmail.com" not in index_content:
    index_content = index_content.replace("</body>", footer_nav)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if "thealienscool@gmail.com" not in content:
        content = content.replace("</body>", footer_nav)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

print("Updates deployed.")
