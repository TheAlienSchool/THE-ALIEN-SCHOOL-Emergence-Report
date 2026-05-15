import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

# We also process index.html
index_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\index.html"
html_files.append(index_path)

# 1. EVOLVE EM DASHES TO ::
for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Evolve the em dashes (—) and spaced en dashes ( – ) to the mighty ::
    content = content.replace(" — ", " :: ")
    content = content.replace("—", "::")
    content = content.replace(" – ", " :: ")
    
    # We want to be careful not to replace dashes inside HTML tags, but usually em dashes are in text.
    # The literal "—" (em dash) is very safe to replace.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. ENHANCE THE GATEWAY MURAL (index.html)
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Replace the current #audio-overlay CSS
old_overlay_css = """  #audio-overlay {
    position: fixed; inset: 0; background: var(--h70-bg); z-index: 10000;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    color: var(--h70-ink); transition: opacity 1.5s ease; text-align: center;
    padding: var(--h70-gutter);
  }"""

new_overlay_css = """  #audio-overlay {
    position: fixed; inset: 0; z-index: 10000;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    color: var(--h70-ink); transition: opacity 1.5s ease; text-align: center;
    padding: var(--h70-gutter);
    overflow: hidden;
    background: var(--h70-bg);
  }
  
  /* Multidimensional Mural Installation for the Gateway */
  #audio-overlay::before, #audio-overlay::after {
    content: '';
    position: absolute;
    inset: -20%;
    z-index: -1;
    background: radial-gradient(circle at 30% 70%, color-mix(in oklab, var(--h70-signal) 12%, transparent) 0%, transparent 40%),
                radial-gradient(circle at 70% 30%, color-mix(in oklab, var(--h70-ink) 8%, transparent) 0%, transparent 50%);
    filter: blur(40px);
    opacity: 0.8;
    animation: gateway-breathe 8s infinite alternate ease-in-out;
  }
  #audio-overlay::after {
    background: radial-gradient(circle at 50% 50%, color-mix(in oklab, var(--h70-signal) 5%, transparent) 0%, transparent 60%);
    animation: gateway-breathe 12s infinite alternate-reverse ease-in-out;
    mix-blend-mode: overlay;
  }
  
  @keyframes gateway-breathe {
    0% { transform: scale(1) rotate(0deg); opacity: 0.5; }
    100% { transform: scale(1.1) rotate(2deg); opacity: 1; }
  }

  .gateway-content {
    position: relative; z-index: 2;
    backdrop-filter: blur(10px);
    padding: 3rem 4rem;
    border-radius: 4px;
    background: color-mix(in oklab, var(--h70-bg) 60%, transparent);
    border: 1px solid color-mix(in oklab, var(--h70-line) 50%, transparent);
    box-shadow: 0 40px 100px rgba(0,0,0,0.2);
  }
"""

if "gateway-breathe" not in index_content:
    index_content = index_content.replace(old_overlay_css, new_overlay_css)
    
    # Update HTML structure inside the overlay to use the .gateway-content container
    old_overlay_html = """<!-- INVITATION GATEWAY -->
<div id="audio-overlay">
  <div class="steam-sans--harris" style="font-size: clamp(2rem, 5vw, 4rem); margin-bottom: 1rem;">The Artifact Archive</div>
  <div class="h70-kicker" style="margin-bottom: 2rem;">A BIOACOUSTIC REPOSITORY</div>
  <button class="h70-glyph-button sonic-link" onclick="initializeSpace()">Enter Space</button>
</div>"""

    new_overlay_html = """<!-- INVITATION GATEWAY -->
<div id="audio-overlay">
  <div class="gateway-content parallax-vessel">
    <div class="steam-sans--harris" style="font-size: clamp(2rem, 5vw, 4rem); margin-bottom: 1rem;">The Artifact Archive</div>
    <div class="h70-kicker" style="margin-bottom: 2rem; color: var(--h70-signal);">A BIOACOUSTIC REPOSITORY</div>
    <button class="h70-glyph-button sonic-link" onclick="initializeSpace()" style="background: var(--h70-ink); color: var(--h70-bg); border-color: transparent;">ENTER SPACE</button>
  </div>
</div>"""

    index_content = index_content.replace(old_overlay_html, new_overlay_html)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Em dashes evolved to :: and Gateway Mural enhanced.")
