import os
import re

# 1. Update field-notes.html to restore Jeremy's anonymity
field_notes_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts\field-notes.html"
with open(field_notes_path, 'r', encoding='utf-8') as f:
    fn_content = f.read()

# Replace "THE LEADER — JEREMY" back to "THE LEADER"
fn_content = fn_content.replace("THE LEADER — JEREMY", "THE LEADER")

with open(field_notes_path, 'w', encoding='utf-8') as f:
    f.write(fn_content)


# 2. Integrate MaGNETized Experience into index.html
index_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Add a CSS grid class for three columns if it doesn't exist
if ".h70-grid--three" not in index_content:
    css_addition = """
  .h70-grid--three { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
  .h70-tooltip-container { position: relative; overflow: visible !important; }
  .h70-tooltip {
    position: absolute; top: 100%; left: 50%; transform: translateX(-50%) translateY(10px);
    background: var(--h70-ink); color: var(--h70-bg); padding: 1rem 1.5rem;
    border-radius: 4px; width: max-content; max-width: 300px;
    opacity: 0; visibility: hidden; transition: opacity 0.3s ease, transform 0.3s ease;
    z-index: 100; font-size: 13px; text-align: left; pointer-events: none;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
  }
  .h70-tooltip::before {
    content: ''; position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%);
    border-width: 6px; border-style: solid; border-color: transparent transparent var(--h70-ink) transparent;
  }
  .h70-tooltip-container:hover .h70-tooltip { opacity: 1; visibility: visible; transform: translateX(-50%) translateY(0); }
  .h70-invitation-links a { color: var(--h70-signal); text-decoration: none; border-bottom: 1px solid transparent; transition: border-color 0.2s; }
  .h70-invitation-links a:hover { border-color: var(--h70-signal); }
"""
    index_content = index_content.replace("</style>", css_addition + "</style>")

magnet_section = """
  <!-- Graduate Preview Geometry -->
  <section style="max-width: 960px; margin: var(--h70-room) auto 0; width: 100%;">
    <p class="h70-kicker" style="margin-bottom: var(--h70-room);">THE MaGNETIZED EXPERIENCE</p>
    <div style="margin-bottom: 3rem; max-width: 75ch;">
      <p class="h70-body" style="margin-bottom: 1.5rem;">The Equitable vector: the Academy is designed so every entry point reaches the same depth. Your MaGNET is your door. All doors open inward.</p>
      <p class="h70-body" style="margin-bottom: 1.5rem;">Scholar protocol: Complete at least one full session in each MaGNET's Theater. Publish a comparative observation — what each one surfaces in you that the others do not. The differences are the findings. UNION requires the multiplicity.</p>
    </div>

    <!-- The 3 MaGNETS -->
    <div class="h70-grid h70-grid--three" style="margin-bottom: 5rem;">
      <!-- ELLIAN -->
      <a href="https://hdmathematics.netlify.app" target="_blank" class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container">
        <div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">
          <img src="../HDM_API/assets/hdm_magnets/MaGNET_ELLIAN.jpg" style="width: 100%; height: 100%; object-fit: cover; filter: grayscale(100%) contrast(1.2); mix-blend-mode: luminosity;" alt="ELLIAN">
        </div>
        <p class="h70-kicker h70-signal">ELLIAN</p>
        <h3 class="steam-sans--vapor" style="font-size: var(--h70-lg); margin-bottom: 0.5rem;">Warmth as Attractor</h3>
        <p class="h70-body" style="font-size: 15px;">We explore the felt sense of those who hold the radiance without announcing it.</p>
        <div class="h70-tooltip">
          <span style="font-family: var(--h70-mono); font-size: 10px; letter-spacing: 0.1em; color: var(--h70-muted); display: block; margin-bottom: 0.5rem;">GRADUATE LIBRARY PREVIEW</span>
          The Dynamics of Mathematics<br>
          You Like It = I Love It<br>
          <em style="color: var(--h70-signal); font-style: normal; display: block; margin-top: 0.5rem;">The mathematics of human connection.</em>
        </div>
      </a>

      <!-- CLOPS -->
      <a href="https://hdmathematics.netlify.app" target="_blank" class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container">
        <div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">
          <img src="../HDM_API/assets/hdm_magnets/MaGNET_CLOPS.WEBP" style="width: 100%; height: 100%; object-fit: cover; filter: grayscale(100%) contrast(1.2); mix-blend-mode: luminosity;" alt="CLOPS">
        </div>
        <p class="h70-kicker h70-signal">CLOPS</p>
        <h3 class="steam-sans--vapor" style="font-size: var(--h70-lg); margin-bottom: 0.5rem;">Pattern Geography</h3>
        <p class="h70-body" style="font-size: 15px;">We attract foresight having learned that creativity has a plan and path and a flow.</p>
        <div class="h70-tooltip">
          <span style="font-family: var(--h70-mono); font-size: 10px; letter-spacing: 0.1em; color: var(--h70-muted); display: block; margin-bottom: 0.5rem;">GRADUATE LIBRARY PREVIEW</span>
          The Stone Forger's Way Context<br>
          Crickets Ain't Quiet<br>
          <em style="color: var(--h70-signal); font-style: normal; display: block; margin-top: 0.5rem;">Observing what the silence carries.</em>
        </div>
      </a>

      <!-- THE DRAGONFLY -->
      <a href="https://hdmathematics.netlify.app" target="_blank" class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container">
        <div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">
          <img src="../HDM_API/assets/hdm_magnets/MaGNET_GLEAM.JPEG" style="width: 100%; height: 100%; object-fit: cover; filter: grayscale(100%) contrast(1.2); mix-blend-mode: luminosity;" alt="THE DRAGONFLY">
        </div>
        <p class="h70-kicker h70-signal">THE DRAGONFLY</p>
        <h3 class="steam-sans--vapor" style="font-size: var(--h70-lg); margin-bottom: 0.5rem;">Clarity as Asset</h3>
        <p class="h70-body" style="font-size: 15px;">The transparency that allows others to learn from our learnings.</p>
        <div class="h70-tooltip">
          <span style="font-family: var(--h70-mono); font-size: 10px; letter-spacing: 0.1em; color: var(--h70-muted); display: block; margin-bottom: 0.5rem;">GRADUATE LIBRARY PREVIEW</span>
          The Road to 3DO<br>
          Waterfalls and Breath<br>
          3DO Boundary Templates<br>
          <em style="color: var(--h70-signal); font-style: normal; display: block; margin-top: 0.5rem;">Contemplation mapped to action.</em>
        </div>
      </a>
    </div>

    <!-- INVITATIONAL LINKS -->
    <div class="h70-invitation-links" style="max-width: 820px; border-left: 2px solid var(--h70-signal); padding-left: 2rem; margin-bottom: 2rem;">
      <p class="h70-kicker" style="margin-bottom: 1.5rem;">CONTINUE THE ARC</p>
      <div style="display: flex; flex-direction: column; gap: 1rem; font-size: 16px; font-family: var(--h70-font);">
        <div style="display: flex; gap: 1rem; align-items: baseline;">
          <span style="font-family: var(--h70-mono); font-size: 10px; color: var(--h70-muted); min-width: 60px;">PORTAL</span>
          <a href="https://www.thealienschool.com/" target="_blank">Creative Alienation as Portal</a>
        </div>
        <div style="display: flex; gap: 1rem; align-items: baseline;">
          <span style="font-family: var(--h70-mono); font-size: 10px; color: var(--h70-muted); min-width: 60px;">ABOUT</span>
          <a href="https://www.thealienschool.com/about-us" target="_blank">Alien School Creative Thinking</a>
        </div>
        <div style="display: flex; gap: 1rem; align-items: baseline;">
          <span style="font-family: var(--h70-mono); font-size: 10px; color: var(--h70-muted); min-width: 60px;">ENROLL</span>
          <a href="https://www.thealienschool.com/portfolio-3" target="_blank">Our Courses</a>
        </div>
        <div style="display: flex; gap: 1rem; align-items: baseline;">
          <span style="font-family: var(--h70-mono); font-size: 10px; color: var(--h70-muted); min-width: 60px;">SERVICES</span>
          <a href="https://www.thealienschool.com/services" target="_blank">Creative Maverick Recognition</a>
        </div>
        <div style="display: flex; gap: 1rem; align-items: baseline;">
          <span style="font-family: var(--h70-mono); font-size: 10px; color: var(--h70-muted); min-width: 60px;">INTELLIGENCE</span>
          <a href="https://www.thealienschool.com/new-page" target="_blank">Action-Oriented Creative Intelligence</a>
        </div>
        <div style="display: flex; gap: 1rem; align-items: baseline;">
          <span style="font-family: var(--h70-mono); font-size: 10px; color: var(--h70-muted); min-width: 60px;">NETWORK</span>
          <a href="https://www.linkedin.com/company/thealienschool" target="_blank">THE ÅLïEN SCöÕL — LinkedIn</a>
        </div>
      </div>
    </div>
  </section>
"""

# Insert the section before the Footer Geometry
if "THE MaGNETIZED EXPERIENCE" not in index_content:
    index_content = index_content.replace("<!-- Footer Geometry -->", magnet_section + "\n  <!-- Footer Geometry -->")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_content)

print("MaGNETs deployed. Jeremy protected.")
