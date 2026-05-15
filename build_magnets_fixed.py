import os

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
index_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\index.html"

# Base HTML Template (using the established HÅRMONIOUS70 architecture)
template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>THE ÅLïEN SCõÖL :: {title}</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=EB+Garamond:ital,wght@0,400..800;1,400..800&family=Playfair+Display:ital,wght@0,400..900;1,400..900&family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../harmonious70.css">
<style>
  .magnet-header {
    height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .magnet-bg {
    position: absolute;
    inset: 0;
    background-image: url('../assets/hdm_magnets/{image}');
    background-size: cover;
    background-position: center;
    filter: grayscale(100%) contrast(1.2) brightness(0.3);
    z-index: -1;
  }
  .magnet-bg::after {
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(to bottom, transparent, var(--h70-bg));
  }
</style>
</head>
<body data-h70-scene="night">

<!-- GLOBAL NAVIGATION -->
<nav id="h70-global-nav" style="position: fixed; top: 0; left: 0; width: 100%; padding: 1.5rem 2vw; display: flex; justify-content: space-between; align-items: baseline; z-index: 9999; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s ease; backdrop-filter: blur(8px); background: color-mix(in oklab, var(--h70-bg) 70%, transparent); border-bottom: 1px solid color-mix(in oklab, var(--h70-line) 30%, transparent);">
  <a href="../index.html" id="nav-brand" class="steam-sans--vapor sonic-link" style="font-size: clamp(1rem, 2vw, 1.2rem); text-decoration: none; color: var(--h70-ink); display: flex; flex-wrap: wrap; gap: 0.5rem;">
    <span>THE ÅLïEN SCõÖL</span>
  </a>
  <div class="nav-links" style="display: flex; gap: 1.5vw; font-family: var(--h70-mono); font-size: 10px; letter-spacing: 0.15em; color: var(--h70-muted);">
    <a href="../index.html" class="sonic-link" style="color: inherit; text-decoration: none;">SYNTHESIS</a>
    <span id="nav-magnet-status" style="opacity: 0.4; border-left: 1px solid var(--h70-line); padding-left: 1.5vw;">MaGNET :: SECURED</span>
  </div>
</nav>

<main class="h70-installation">
  <div class="h70-muralist parallax-mural" aria-hidden="true"></div>

  <header class="magnet-header">
    <div class="magnet-bg parallax-vessel"></div>
    <p class="h70-kicker h70-signal" style="letter-spacing: 0.4em;">MaGNETIZED SYNTHESIS</p>
    <h1 class="steam-sans--harris" style="font-size: clamp(3rem, 6vw, 5rem); margin: 1rem 0;">{title}</h1>
    <p class="h70-body" style="font-size: var(--h70-lg); letter-spacing: 0.1em; opacity: 0.8;">{subtitle}</p>
  </header>

  <article style="max-width: 680px; margin: 0 auto; padding: 4rem 2rem;">
    <p class="h70-body" style="font-size: 1.2rem; line-height: 1.8; margin-bottom: 3rem; color: var(--h70-signal);">
      {intro}
    </p>

    <div style="border-left: 2px solid var(--h70-line); padding-left: 2rem; margin-bottom: 4rem;">
      <p class="h70-kicker">CROSS-INDEXED ARTIFACTS</p>
      {cross_index}
    </div>

    {content}

  </article>

  <footer style="max-width: 820px; margin: var(--h70-mural) auto 4rem; text-align: center;">
    <p class="h70-kicker" style="line-height: 2.2; opacity: 0.6;">
      THE ÅLïEN SCõÖL FOR CREATIVE THÏNKING :: SYNTHESIS ARCHIVE<br>
      GRADUATE SCHOLAR LIBRARY :: {title}
    </p>
    <div style="margin-top: 3rem;">
      <button class="h70-glyph-button sonic-link" onclick="window.location.href='../index.html'">RETURN TO HUB ∴</button>
    </div>
  </footer>
</main>

<script>
  let targetX = 0, targetY = 0;
  let currentX = 0, currentY = 0;
  const ease = 0.08;
  document.addEventListener('mousemove', (e) => {
    targetX = (e.clientX / window.innerWidth - 0.5) * 2;
    targetY = (e.clientY / window.innerHeight - 0.5) * 2;
  });
  function renderParallax() {
    currentX += (targetX - currentX) * ease;
    currentY += (targetY - currentY) * ease;
    const vessels = document.querySelectorAll('.parallax-vessel');
    vessels.forEach(vessel => {
      vessel.style.transform = `translate(${currentX * 6}px, ${currentY * 6}px)`;
    });
    requestAnimationFrame(renderParallax);
  }
  if (window.matchMedia("(pointer: fine)").matches) {
    requestAnimationFrame(renderParallax);
  }
</script>
</body>
</html>
"""

def render_magnet(title, subtitle, image, intro, cross_index, content):
    html = template.replace("{title}", title)
    html = html.replace("{subtitle}", subtitle)
    html = html.replace("{image}", image)
    html = html.replace("{intro}", intro)
    html = html.replace("{cross_index}", cross_index)
    html = html.replace("{content}", content)
    return html

# ELLIAN DATA
ellian_html = render_magnet(
    title="ELLIAN",
    subtitle="Warmth as Attractor",
    image="MaGNET_ELLIAN.jpg",
    intro="We explore the felt sense of those who hold the radiance without announcing it. The mathematics of human connection require an ecosystem where 'You Like It = I Love It' becomes a structural truth rather than a polite sentiment.",
    cross_index="""<ul style="list-style: none; padding: 0; font-family: var(--h70-font); font-size: 0.9rem; line-height: 2;">
        <li><span style="color: var(--h70-signal);">∴</span> The Dynamics of Mathematics</li>
        <li><span style="color: var(--h70-signal);">∴</span> You Like It = I Love It</li>
      </ul>""",
    content="""
    <h2 class="steam-sans--vapor" style="margin-top: 3rem; margin-bottom: 1rem; font-size: 2rem;">The Architecture of Warmth</h2>
    <p class="h70-body">Warmth operates not as an emotion, but as a gravitational field. In the original <em>Elevation Codex</em>, we established that the guide must provide a mirror. Ellian scales this. The mathematics of connection dictate that when a practitioner is fully witnessed, the necessity for external validation collapses. Warmth attracts the truth out of the scholar because the environment does not demand performance.</p>
    
    <h2 class="steam-sans--vapor" style="margin-top: 3rem; margin-bottom: 1rem; font-size: 2rem;">You Like It = I Love It</h2>
    <p class="h70-body">This is the equation of permission. When the environment inherently supports the scholar's baseline preference ("You Like It"), the ecosystem amplifies it into a structural mandate ("I Love It"). It is the removal of the deficit. The practitioner does not have to justify their aesthetic or their direction; the field already loves what they merely like. This is how the <em>Proof of Field</em> becomes undeniable.</p>
    """
)

# CLOPS DATA
clops_html = render_magnet(
    title="CLOPS",
    subtitle="Pattern Geography",
    image="MaGNET_CLOPS.WEBP",
    intro="We attract foresight having learned that creativity has a plan and path and a flow. The silence is never empty; it is carrying the exact structural geometry we need to proceed.",
    cross_index="""<ul style="list-style: none; padding: 0; font-family: var(--h70-font); font-size: 0.9rem; line-height: 2;">
        <li><span style="color: var(--h70-signal);">∴</span> The Stone Forger's Way Context</li>
        <li><span style="color: var(--h70-signal);">∴</span> TSFW Cohort</li>
        <li><span style="color: var(--h70-signal);">∴</span> Crickets Ain't Quiet</li>
      </ul>""",
    content="""
    <h2 class="steam-sans--vapor" style="margin-top: 3rem; margin-bottom: 1rem; font-size: 2rem;">The Abstract Volume of the Silent Treatment</h2>
    <p class="h70-body">As articulated in <em>Crickets Ain't Quiet</em>, silence is not an absence. It is a geometric field of unspoken tensions that reshapes entire relationship systems with mathematical precision. The "Crystal Silo" prevents authentic connection while maintaining the illusion of a functional relationship. Pattern Geography requires us to map these silos and recognize the silence as a loud, structural signal.</p>
    
    <h2 class="steam-sans--vapor" style="margin-top: 3rem; margin-bottom: 1rem; font-size: 2rem;">The Stone Forger's Architecture</h2>
    <p class="h70-body">To forge is to apply heat and pressure to raw material until it assumes a new form. <em>The Stone Forger's Way</em> applies this to cohort methodology. The patterns we map in isolation become the curriculum of the collective. When we understand that creativity has a flow, we stop trying to invent the path and instead learn to read the geography that is already there. This is the direct application of the <em>Frequency Report</em> into physical space.</p>
    """
)

# DRAGONFLY DATA
dragonfly_html = render_magnet(
    title="THE DRAGONFLY",
    subtitle="Clarity as Asset",
    image="MaGNET_GLEAM.JPEG",
    intro="The transparency that allows others to learn from our learnings. Clarity is not the absence of complexity; it is the mastery of boundaries and the breath.",
    cross_index="""<ul style="list-style: none; padding: 0; font-family: var(--h70-font); font-size: 0.9rem; line-height: 2;">
        <li><span style="color: var(--h70-signal);">∴</span> The Road to 3DO</li>
        <li><span style="color: var(--h70-signal);">∴</span> Waterfalls and Breath</li>
        <li><span style="color: var(--h70-signal);">∴</span> 3DO Boundary Templates</li>
      </ul>""",
    content="""
    <h2 class="steam-sans--vapor" style="margin-top: 3rem; margin-bottom: 1rem; font-size: 2rem;">The Road to 3DO (Three Days Off)</h2>
    <p class="h70-body">Contemplation must be mapped to action. The 3DO protocol is not merely about rest; it is the intentional design of boundaries. Using the <em>Boundary Madlibs Templates</em>, scholars construct exact linguistic containers for their time. This is clarity deployed as an asset. When the boundary is transparent, the ecosystem reorganizes around it without friction.</p>
    
    <h2 class="steam-sans--vapor" style="margin-top: 3rem; margin-bottom: 1rem; font-size: 2rem;">Waterfalls and Breath</h2>
    <p class="h70-body">Referencing the foundational <em>Field Notes</em>, the breath is the practice itself. A waterfall does not force its descent; it surrenders to gravity with total clarity. The dragonfly hovers in the mist of this descent, maintaining absolute precision in a chaotic environment. Clarity is achieved not by stopping the water, but by mastering the hover.</p>
    """
)

with open(os.path.join(artifacts_dir, 'magnet-ellian.html'), 'w', encoding='utf-8') as f: f.write(ellian_html)
with open(os.path.join(artifacts_dir, 'magnet-clops.html'), 'w', encoding='utf-8') as f: f.write(clops_html)
with open(os.path.join(artifacts_dir, 'magnet-dragonfly.html'), 'w', encoding='utf-8') as f: f.write(dragonfly_html)

# Update index.html to point to these new local files
with open(index_path, 'r', encoding='utf-8') as f:
    idx = f.read()

# Replace the Netlify links in the MaGNET cards
idx = idx.replace('href="https://hdmathematics.netlify.app" target="_blank" class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container"\\n        <div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">\\n          <img src="assets/hdm_magnets/MaGNET_ELLIAN.jpg"', 'href="artifacts/magnet-ellian.html" class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container"\\n        <div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">\\n          <img src="assets/hdm_magnets/MaGNET_ELLIAN.jpg"')

# Simple regex string replacement because exact whitespace matching might fail
import re
idx = re.sub(r'href="https://hdmathematics\.netlify\.app"\s+target="_blank"\s+class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container"\s*>\s*<div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">\s*<img src="assets/hdm_magnets/MaGNET_ELLIAN', r'href="artifacts/magnet-ellian.html" class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container">\n        <div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">\n          <img src="assets/hdm_magnets/MaGNET_ELLIAN', idx)

idx = re.sub(r'href="https://hdmathematics\.netlify\.app"\s+target="_blank"\s+class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container"\s*>\s*<div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">\s*<img src="assets/hdm_magnets/MaGNET_CLOPS', r'href="artifacts/magnet-clops.html" class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container">\n        <div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">\n          <img src="assets/hdm_magnets/MaGNET_CLOPS', idx)

idx = re.sub(r'href="https://hdmathematics\.netlify\.app"\s+target="_blank"\s+class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container"\s*>\s*<div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">\s*<img src="assets/hdm_magnets/MaGNET_GLEAM', r'href="artifacts/magnet-dragonfly.html" class="h70-vessel-card site-link parallax-vessel sonic-link h70-tooltip-container">\n        <div style="height: 180px; overflow: hidden; margin-bottom: 1.5rem; border-radius: 2px;">\n          <img src="assets/hdm_magnets/MaGNET_GLEAM', idx)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx)

print("MaGNET experiential portals created and linked.")
