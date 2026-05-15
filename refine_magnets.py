import os

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"

# Base HTML Template using Proof-of-Field styling
template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Synthesis Archive :: {title}</title>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../harmonious70.css">
<style>
  :root {{
    --bg:         var(--h70-bg);
    --ink:        var(--h70-ink);
    --deep:       var(--h70-ink);
    --muted:      var(--h70-muted);
    --border:     var(--h70-line);
    --border-lt:  var(--h70-line);
    --warm:       var(--h70-surface);
    --gold:       var(--h70-signal);
    --gold-pale:  var(--h70-surface);
    --teal:       var(--h70-signal);
    --scholar:    var(--h70-ink);
    --scholar-lt: var(--h70-surface);
    --rule:       var(--h70-line);
  }}

  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}

  body {{
    background: var(--page);
    color: var(--ink);
    font-family: 'Libre Baskerville', Georgia, serif;
    font-size: 18px;
    line-height: 1.75;
    -webkit-font-smoothing: antialiased;
  }}

  .page {{
    max-width: 820px;
    margin: 0 auto;
    padding: 0 2.25rem 10rem;
    position: relative;
    z-index: 1;
  }}

  /* ── COVER ── */
  .cover {{
    padding: 10rem 0 4rem;
    border-bottom: 1px solid var(--border);
    display: grid;
    grid-template-rows: auto 1fr auto;
    position: relative;
  }}
  
  .magnet-bg-container {{
    position: absolute;
    top: 0; left: 50%;
    transform: translateX(-50%);
    width: 100vw;
    height: 60vh;
    z-index: -1;
    overflow: hidden;
  }}

  .magnet-bg {{
    width: 100%; height: 100%;
    background-image: url('../assets/hdm_magnets/{image}');
    background-size: cover;
    background-position: center;
    filter: grayscale(100%) contrast(1.2) brightness(0.25);
  }}
  .magnet-bg::after {{
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(to bottom, transparent, var(--bg));
  }}

  .cover-top {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }}

  .cover-stamp {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    letter-spacing: 0.24em;
    color: var(--muted);
    line-height: 2;
  }}

  .cover-protocol {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    letter-spacing: 0.14em;
    color: var(--gold);
    text-align: right;
    line-height: 2;
    opacity: 0.75;
  }}

  .cover-body {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 5rem 0 3rem;
  }}

  .cover-title {{
    font-size: clamp(3rem, 7vw, 5.5rem);
    font-family: var(--h70-font);
    font-weight: 700;
    font-style: normal;
    line-height: 1.0;
    color: var(--deep);
    margin-bottom: 0.5rem;
  }}

  .cover-title span {{ font-weight: 400; font-style: normal; color: var(--gold); }}

  .cover-rule {{
    width: 100%; height: 1px;
    background: var(--rule); margin: 2rem 0; position: relative;
  }}

  .cover-rule::after {{
    content: '∴'; position: absolute; left: 50%; top: 50%;
    transform: translate(-50%, -50%); background: var(--bg);
    padding: 0 0.75rem; color: var(--gold); font-size: 1rem; opacity: 0.55;
  }}

  .cover-sub {{
    font-size: 17px; font-style: normal; color: var(--muted);
    max-width: 520px; line-height: 1.75; margin-bottom: 3rem;
  }}

  .cover-toc {{
    display: grid; grid-template-columns: repeat(2, 1fr);
    border: 0.5px solid var(--border); border-radius: 3px; overflow: hidden;
  }}

  .toc-item {{
    padding: 0.9rem 1.1rem; border-right: 0.5px solid var(--border);
    border-bottom: 0.5px solid var(--border); text-decoration: none;
    color: var(--ink); transition: background 0.15s; display: block;
  }}

  .toc-item:nth-child(even) {{ border-right: none; }}
  .toc-item:nth-last-child(-n+2) {{ border-bottom: none; }}
  .toc-item:hover {{ background: var(--warm); }}

  .toc-num {{
    font-family: 'JetBrains Mono', monospace; font-size: 9px;
    letter-spacing: 0.14em; color: var(--muted); display: block; margin-bottom: 0.2rem;
  }}

  .toc-name {{ font-size: 13px; font-style: normal; color: var(--deep); line-height: 1.35; }}

  /* ── SECTION ── */
  .section {{ padding: 5.5rem 0 0; }}

  .section-header {{
    display: grid; grid-template-columns: 52px 1fr; gap: 0 1.5rem;
    margin-bottom: 3rem; padding-bottom: 1.5rem; border-bottom: 0.5px solid var(--border);
  }}

  .section-num {{
    font-family: 'JetBrains Mono', monospace; font-size: 9px;
    letter-spacing: 0.2em; color: var(--muted); padding-top: 0.5rem;
  }}

  .section-title {{
    font-size: clamp(1.4rem, 3vw, 2rem); font-family: var(--h70-font); font-weight: 400; font-style: normal;
    color: var(--deep); line-height: 1.15;
  }}

  .section-title em {{ font-style: normal; font-weight: 700; color: var(--gold); }}

  /* ── PROSE ── */
  .prose {{ max-width: 65ch; margin-left: 0; }}
  .prose p {{ font-size: 18px; line-height: 1.75; color: var(--ink); margin-bottom: 1.4rem; }}
  .prose p:last-child {{ margin-bottom: 0; }}
  .prose em {{ font-style: normal; color: var(--gold); }}
  .prose strong {{ font-weight: 700; color: var(--deep); }}

  /* ── LOCATE (Somatic opening) ── */
  .locate {{
    border-left: 2px solid var(--border); padding: 1rem 1.4rem;
    margin-bottom: 1.75rem; border-radius: 0 3px 3px 0; background: var(--warm);
  }}

  .locate-label {{
    font-family: 'JetBrains Mono', monospace; font-size: 9px;
    letter-spacing: 0.16em; color: var(--muted); margin-bottom: 0.45rem; display: block;
  }}

  .locate p {{ font-size: 17px; font-style: normal; color: var(--deep); line-height: 1.75; margin-bottom: 0; }}

  /* ── SCHOLAR VOICE :: primary source distinction ── */
  .scholar-voice {{
    border-left: 3px solid var(--scholar); padding: 1rem 1.25rem;
    background: var(--scholar-lt); border-radius: 0 3px 3px 0;
    margin: 2.5rem 0;
  }}

  .scholar-voice-label {{
    font-family: 'JetBrains Mono', monospace; font-size: 9px;
    letter-spacing: 0.16em; color: var(--scholar); margin-bottom: 0.5rem; display: block;
    opacity: 0.7;
  }}

  .scholar-voice p {{
    font-size: 16px; font-style: normal; color: var(--deep);
    line-height: 1.75; margin-bottom: 0.5rem;
  }}

  .scholar-voice .sv-source {{
    font-family: 'JetBrains Mono', monospace; font-size: 10px;
    color: var(--scholar); opacity: 0.6; font-style: normal;
    letter-spacing: 0.04em; margin-top: 0.5rem; display: block;
  }}

  /* ── PULLQUOTE ── */
  .pullquote {{
    padding: 4.5rem 0; text-align: left;
    border-top: 0.5px solid var(--border); border-bottom: 0.5px solid var(--border); margin: 4rem 0;
  }}

  .pullquote p {{
    font-size: clamp(1.2rem, 2.7vw, 1.72rem); font-style: normal; line-height: 1.52;
    color: var(--deep); max-width: 65ch; margin-left: 0; margin: 0 auto;
  }}

  .pullquote p em {{ font-style: normal; color: var(--gold); }}

  .pullquote-attr {{
    font-family: 'JetBrains Mono', monospace; font-size: 10px;
    letter-spacing: 0.16em; color: var(--muted); margin-top: 1.25rem; display: block;
  }}

  .anchor {{
    font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--gold);
    border-left: 2px solid var(--border); padding-left: 1rem;
    margin: 1.25rem 0; line-height: 1.75; letter-spacing: 0.02em;
  }}

  @media (max-width: 580px) {{
    .cover-toc {{ grid-template-columns: 1fr; }}
    .toc-item {{ border-right: none; }}
    .cover-top {{ flex-direction: column; gap: 0.5rem; }}
  }}
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

<main class="h70-installation" style="display:block;">
  <div class="h70-muralist parallax-mural" aria-hidden="true"></div>
  
  <div class="magnet-bg-container">
    <div class="magnet-bg parallax-vessel"></div>
  </div>

  <div class="page" style="background: transparent;">

  <!-- COVER -->
  <div class="cover">
    <div class="cover-top">
      <span class="cover-stamp">SYNTHESIS ARCHIVE · FIELD NOTE<br>CROSS-INDEXED INVESTIGATIVE REPORT</span>
      <span class="cover-protocol">VESSELVERSE EDITORIAL PROTOCOL<br>PRIMER INSTALLED</span>
    </div>

    <div class="cover-body">
      <h1 class="cover-title"><span>{title}</span></h1>
      <div class="cover-rule"></div>
      <p class="cover-sub">{subtitle}. {intro}</p>

      <div class="cover-toc">
        {toc_items}
      </div>

      <p class="cover-law">
        Cross-Indexed Original Artifacts:<br>
        {artifacts_list}
      </p>
    </div>
  </div>

  {content}

  </div>
</main>
<script>
  let targetX = 0, targetY = 0;
  let currentX = 0, currentY = 0;
  const ease = 0.08;
  document.addEventListener('mousemove', (e) => {{
    targetX = (e.clientX / window.innerWidth - 0.5) * 2;
    targetY = (e.clientY / window.innerHeight - 0.5) * 2;
  }});
  function renderParallax() {{
    currentX += (targetX - currentX) * ease;
    currentY += (targetY - currentY) * ease;
    const vessels = document.querySelectorAll('.parallax-vessel');
    vessels.forEach(vessel => {{
      vessel.style.transform = `translate(${{currentX * 6}}px, ${{currentY * 6}}px)`;
    }});
    requestAnimationFrame(renderParallax);
  }}
  if (window.matchMedia("(pointer: fine)").matches) {{
    requestAnimationFrame(renderParallax);
  }}
</script>
</body>
</html>
"""

def render_magnet(title, subtitle, image, intro, toc_items, artifacts_list, content):
    html = template.replace("{title}", title)
    html = html.replace("{subtitle}", subtitle)
    html = html.replace("{image}", image)
    html = html.replace("{intro}", intro)
    html = html.replace("{toc_items}", toc_items)
    html = html.replace("{artifacts_list}", artifacts_list)
    html = html.replace("{content}", content)
    return html

# ELLIAN DATA
ellian_html = render_magnet(
    title="ELLIAN",
    subtitle="Warmth as Attractor",
    image="MaGNET_ELLIAN.jpg",
    intro="We explore the felt sense of those who hold the radiance without announcing it. Drawn from the dynamics of mathematics and the structural truth of 'You Like It = I Love It'.",
    toc_items="""
        <a href="#locate" class="toc-item"><span class="toc-num">LOCATE</span><div class="toc-name">The Baseline Preference</div></a>
        <a href="#mechanics" class="toc-item"><span class="toc-num">PART I</span><div class="toc-name">The Architecture of Warmth</div></a>
        <a href="#equation" class="toc-item"><span class="toc-num">PART II</span><div class="toc-name">The Permission Equation</div></a>
    """,
    artifacts_list="∴ The Dynamics of Mathematics<br>∴ You Like It = I Love It",
    content="""
  <section class="section" id="locate">
    <div class="section-header">
      <span class="section-num">LOCATE</span>
      <h2 class="section-title">The Baseline <em>Preference</em></h2>
    </div>
    <div class="locate">
      <span class="locate-label">LOCATE · SOMATIC REGISTER</span>
      <p>You enter a space where you are fully witnessed. The necessity for external validation collapses. Warmth attracts the truth out of you because the environment does not demand performance. What happens to the nervous system when preference is not merely tolerated, but structurally loved?</p>
    </div>
  </section>

  <section class="section" id="mechanics">
    <div class="section-header">
      <span class="section-num">PART I</span>
      <h2 class="section-title">The <em>Architecture</em> of Warmth</h2>
    </div>
    <div class="prose">
      <p>Warmth operates not as an emotion, but as a gravitational field. In the original <em>Elevation Codex</em>, we established that the guide must provide a mirror. Ellian scales this logic. The mathematics of connection dictate that when a practitioner is fully witnessed, the necessity for external validation collapses.</p>
    </div>
    <div class="scholar-voice">
      <span class="scholar-voice-label">FIELD EVIDENCE :: THE DYNAMICS OF MATHEMATICS</span>
      <p>"Warmth attracts the truth out of the scholar because the environment does not demand performance."</p>
      <span class="sv-source">Synthesis Protocol :: Ellian Coordinate</span>
    </div>
    <div class="prose">
      <p>The practitioner does not have to justify their aesthetic or their direction. When performance is removed, original geometry is permitted to emerge. The warmth is the attractor beam.</p>
    </div>
  </section>

  <div class="pullquote">
    <p>When the environment inherently supports the scholar's baseline preference, the ecosystem amplifies it into a <em>structural mandate</em>.</p>
    <span class="pullquote-attr">:: ELLIAN FIELD NOTE</span>
  </div>

  <section class="section" id="equation">
    <div class="section-header">
      <span class="section-num">PART II</span>
      <h2 class="section-title">The <em>Permission</em> Equation</h2>
    </div>
    <div class="prose">
      <p>This is the equation of permission: "You Like It = I Love It." It is the total removal of the deficit. The practitioner does not have to justify their aesthetic or their direction; the field already loves what they merely like.</p>
    </div>
    <div class="anchor">This is how the Proof of Field becomes undeniable. The field responds affirmatively to the scholar's inherent structure.</div>
  </section>
    """
)

# CLOPS DATA
clops_html = render_magnet(
    title="CLOPS",
    subtitle="Pattern Geography",
    image="MaGNET_CLOPS.WEBP",
    intro="We attract foresight having learned that creativity has a plan and path and a flow. The silence is never empty; it is carrying the exact structural geometry we need to proceed.",
    toc_items="""
        <a href="#locate" class="toc-item"><span class="toc-num">LOCATE</span><div class="toc-name">The Geometric Volume</div></a>
        <a href="#abstract-volume" class="toc-item"><span class="toc-num">PART I</span><div class="toc-name">The Abstract Volume of the Silent Treatment</div></a>
        <a href="#forger" class="toc-item"><span class="toc-num">PART II</span><div class="toc-name">The Stone Forger's Architecture</div></a>
    """,
    artifacts_list="∴ The Stone Forger's Way Context<br>∴ TSFW Cohort<br>∴ Crickets Ain't Quiet",
    content="""
  <section class="section" id="locate">
    <div class="section-header">
      <span class="section-num">LOCATE</span>
      <h2 class="section-title">The Geometric <em>Volume</em></h2>
    </div>
    <div class="locate">
      <span class="locate-label">LOCATE · SOMATIC REGISTER</span>
      <p>You send a vulnerability into the system—a proposal, an expression of need—and receive nothing in return. You are hearing crickets. But anyone who has actually listened to crickets knows they create one of nature's most complex and layered soundscapes. The silence is not quiet at all. It is abstract volume.</p>
    </div>
  </section>

  <section class="section" id="abstract-volume">
    <div class="section-header">
      <span class="section-num">PART I</span>
      <h2 class="section-title">The Abstract Volume of the <em>Silent Treatment</em></h2>
    </div>
    <div class="prose">
      <p>As articulated in the raw field text of <em>Crickets Ain't Quiet</em>, silence is not an absence. It is a geometric field of unspoken tensions that reshapes entire relationship systems with mathematical precision.</p>
    </div>
    <div class="scholar-voice">
      <span class="scholar-voice-label">FIELD EVIDENCE :: CRICKETS AIN'T QUIET</span>
      <p>"The 'Crystal Silo'—an invisible barrier that prevents authentic connection while maintaining the illusion of functional relationship."</p>
      <span class="sv-source">Abstract Volume Reporting</span>
    </div>
    <div class="prose">
      <p>Pattern Geography requires us to map these silos and recognize the silence as a loud, structural signal. We must track the cascade effect: how professional silence invades personal space, how the nervous system registers a communication void as an actual injury.</p>
    </div>
    <div class="anchor">The irony is devastating: experiencing the Silent Treatment leads to unconsciously employing it.</div>
  </section>

  <div class="pullquote">
    <p>When we understand that creativity has a flow, we stop trying to invent the path and instead learn to <em>read the geography</em> that is already there.</p>
    <span class="pullquote-attr">:: CLOPS FIELD NOTE</span>
  </div>

  <section class="section" id="forger">
    <div class="section-header">
      <span class="section-num">PART II</span>
      <h2 class="section-title">The <em>Stone Forger's</em> Architecture</h2>
    </div>
    <div class="prose">
      <p>To forge is to apply heat and pressure to raw material until it assumes a new form. <em>The Stone Forger's Way</em> applies this to cohort methodology. The patterns we map in isolation become the curriculum of the collective. This is the direct application of the <em>Frequency Report</em> into physical space.</p>
    </div>
  </section>
    """
)

# DRAGONFLY DATA
dragonfly_html = render_magnet(
    title="THE DRAGONFLY",
    subtitle="Clarity as Asset",
    image="MaGNET_GLEAM.JPEG",
    intro="The transparency that allows others to learn from our learnings. Clarity is not the absence of complexity; it is the mastery of boundaries and the breath.",
    toc_items="""
        <a href="#locate" class="toc-item"><span class="toc-num">LOCATE</span><div class="toc-name">The Hover</div></a>
        <a href="#3do" class="toc-item"><span class="toc-num">PART I</span><div class="toc-name">The Road to 3DO</div></a>
        <a href="#waterfalls" class="toc-item"><span class="toc-num">PART II</span><div class="toc-name">Waterfalls and Breath</div></a>
    """,
    artifacts_list="∴ The Road to 3DO<br>∴ Waterfalls and Breath<br>∴ 3DO Boundary Templates",
    content="""
  <section class="section" id="locate">
    <div class="section-header">
      <span class="section-num">LOCATE</span>
      <h2 class="section-title">The <em>Hover</em></h2>
    </div>
    <div class="locate">
      <span class="locate-label">LOCATE · SOMATIC REGISTER</span>
      <p>A waterfall does not force its descent; it surrenders to gravity with total clarity. The dragonfly hovers in the mist of this descent, maintaining absolute precision in a chaotic environment. Clarity is achieved not by stopping the water, but by mastering the hover.</p>
    </div>
  </section>

  <section class="section" id="3do">
    <div class="section-header">
      <span class="section-num">PART I</span>
      <h2 class="section-title">The Road to <em>3DO</em></h2>
    </div>
    <div class="prose">
      <p>Contemplation must be mapped to action. The 3DO protocol is not merely about rest; it is the intentional design of boundaries. Using the <em>Boundary Madlibs Templates</em>, scholars construct exact linguistic containers for their time.</p>
    </div>
    <div class="scholar-voice">
      <span class="scholar-voice-label">FIELD EVIDENCE :: 3DO PROTOCOL</span>
      <p>"When the boundary is transparent, the ecosystem reorganizes around it without friction."</p>
      <span class="sv-source">Boundary Templates Synthesis</span>
    </div>
    <div class="prose">
      <p>This is clarity deployed as an asset. Transparency allows the team, the cohort, and the family to read the exact coordinates of the scholar's availability.</p>
    </div>
  </section>

  <div class="pullquote">
    <p>Clarity is achieved not by stopping the water, but by <em>mastering the hover.</em></p>
    <span class="pullquote-attr">:: DRAGONFLY FIELD NOTE</span>
  </div>

  <section class="section" id="waterfalls">
    <div class="section-header">
      <span class="section-num">PART II</span>
      <h2 class="section-title"><em>Waterfalls</em> and Breath</h2>
    </div>
    <div class="prose">
      <p>Referencing the foundational <em>Field Notes</em>, the breath is the practice itself. It is the metric by which we gauge the depth of the work. The dragonfly in the mist is not fighting the mist—it is using it. It is using the clarity of its own architecture to remain perfectly stable.</p>
    </div>
    <div class="anchor">The transparency of the dragonfly's wings allows others to learn from our learnings. It leaves no shadow.</div>
  </section>
    """
)

with open(os.path.join(artifacts_dir, 'magnet-ellian.html'), 'w', encoding='utf-8') as f: f.write(ellian_html)
with open(os.path.join(artifacts_dir, 'magnet-clops.html'), 'w', encoding='utf-8') as f: f.write(clops_html)
with open(os.path.join(artifacts_dir, 'magnet-dragonfly.html'), 'w', encoding='utf-8') as f: f.write(dragonfly_html)

print("Field Reporting applied to MaGNET portals.")
