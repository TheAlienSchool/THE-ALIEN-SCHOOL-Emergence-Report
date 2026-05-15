import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))
index_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\index.html"
all_files = html_files + [index_path]

# 1. Global Replacement: Artifact Archive -> Synthesis Archive
for file_path in all_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace("Artifact Archive", "Synthesis Archive")
    content = content.replace("ARTIFACT ARCHIVE", "SYNTHESIS ARCHIVE")
    content = content.replace("Artifact<br><span class=\"h70-signal\">Archive</span>", "Synthesis<br><span class=\"h70-signal\">Archive</span>")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Advanced Audio & Global Nav Injection for all files
global_nav = """
<!-- GLOBAL NAVIGATION -->
<nav id="h70-global-nav" style="position: fixed; top: 0; left: 0; width: 100%; padding: 1.5rem 2vw; display: flex; justify-content: space-between; align-items: baseline; z-index: 9999; transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), background 0.4s ease; backdrop-filter: blur(8px); background: color-mix(in oklab, var(--h70-bg) 70%, transparent); border-bottom: 1px solid color-mix(in oklab, var(--h70-line) 30%, transparent);">
  <a href="../index.html" id="nav-brand" class="steam-sans--vapor sonic-link" style="font-size: clamp(1rem, 2vw, 1.2rem); text-decoration: none; color: var(--h70-ink); display: flex; flex-wrap: wrap; gap: 0.5rem;">
    <span>THE ÅLïEN SCõÖL</span>
    <span id="nav-c-thinking" style="color: var(--h70-signal); opacity: 1; transition: opacity 2s ease;">∴ FOR CREATIVE THÏNKING</span>
  </a>
  <div class="nav-links" style="display: flex; gap: 1.5vw; font-family: var(--h70-mono); font-size: 10px; letter-spacing: 0.15em; color: var(--h70-muted);">
    <a href="../index.html" class="sonic-link" style="color: inherit; text-decoration: none;">SYNTHESIS</a>
    <span id="nav-magnet-status" style="opacity: 0.4; border-left: 1px solid var(--h70-line); padding-left: 1.5vw;">MaGNET :: SECURED</span>
  </div>
</nav>

<style>
  /* Responsive Navigation Anticipation */
  body { padding-top: 80px; } /* Prevent nav from covering content */
  #h70-global-nav.nav-hidden { transform: translateY(-100%); }
  
  @media (max-width: 768px) {
    #nav-c-thinking { display: none; } /* On mobile, simplify brand after initial gateway */
    #h70-global-nav { padding: 1rem; }
  }
</style>

<script>
  // Anticipatory scroll logic
  let lastScrollY = window.scrollY;
  window.addEventListener('scroll', () => {
    const nav = document.getElementById('h70-global-nav');
    if (window.scrollY > lastScrollY && window.scrollY > 100) {
      nav.classList.add('nav-hidden'); // Scrolling down, hide nav
    } else {
      nav.classList.remove('nav-hidden'); // Scrolling up, anticipate intent, show nav
    }
    lastScrollY = window.scrollY;
    
    // Fade out "FOR CREATIVE THINKING" as they steep deeper, leaving just the school
    const ct = document.getElementById('nav-c-thinking');
    if(ct) {
      if(window.scrollY > 300) { ct.style.opacity = '0'; }
      else { ct.style.opacity = '1'; }
    }
  });

  // Check MaGNET status from localStorage
  document.addEventListener('DOMContentLoaded', () => {
    if(localStorage.getItem('magnetUnlocked') === 'true') {
      const ms = document.getElementById('nav-magnet-status');
      if(ms) {
        ms.textContent = 'MaGNET :: ACTIVE';
        ms.style.opacity = '1';
        ms.style.color = 'var(--h70-signal)';
      }
    }
  });
</script>
"""

# Apply global nav to all files
for file_path in all_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if "h70-global-nav" not in content:
        # Fix hrefs depending on file location
        nav_injection = global_nav
        if "index.html" in file_path:
            nav_injection = nav_injection.replace("../index.html", "index.html")

        content = content.replace("<body data-h70-scene=\"night\">", "<body data-h70-scene=\"night\">\n" + nav_injection)
        content = content.replace("<body data-h70-scene=\"day\">", "<body data-h70-scene=\"day\">\n" + nav_injection)

    # Audio Engine updates (240Hz + experiential panning)
    if "const PENTATONIC_SCALE =" in content:
        # Add the 240Hz holistic register
        audio_patch = """
  // 240Hz Holistic Register injected into the ambient breath
  function playAmbientBreath() {
    if (!audioCtx) return;
    const osc174 = audioCtx.createOscillator();
    const osc240 = audioCtx.createOscillator(); // The Holistic Addition
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();

    osc174.type = 'sine'; osc174.frequency.value = 174;
    osc240.type = 'sine'; osc240.frequency.value = 240;

    filter.type = 'lowpass'; filter.frequency.value = 400;
    gain.gain.value = 0.02;

    const lfo = audioCtx.createOscillator();
    const lfoGain = audioCtx.createGain();
    lfo.type = 'sine'; lfo.frequency.value = 0.22; // 4.4s breath
    lfoGain.gain.value = 0.015;
    
    lfo.connect(lfoGain);
    lfoGain.connect(gain.gain);
    lfo.start();

    osc174.connect(filter);
    osc240.connect(filter);
    filter.connect(gain);
    gain.connect(masterGain);

    osc174.start();
    osc240.start();
  }

  function playStrikingBowl(freqOverride, isHover = false) {
    if (!audioCtx) return;
    const freq = freqOverride || PENTATONIC_SCALE[Math.floor(Math.random() * PENTATONIC_SCALE.length)];
    
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();
    
    // Experiential Sonification: spatial panning based on random float
    const panner = audioCtx.createStereoPanner ? audioCtx.createStereoPanner() : null;
    if(panner) { panner.pan.value = (Math.random() * 1) - 0.5; }

    osc.type = isHover ? 'triangle' : 'sine'; // Different texture for hover
    osc.frequency.value = isHover ? freq * 2 : freq;

    filter.type = 'lowpass';
    filter.frequency.value = isHover ? freq * 4 : freq * 3;

    gain.gain.setValueAtTime(0, audioCtx.currentTime);
    gain.gain.linearRampToValueAtTime(isHover ? 0.015 : 0.1, audioCtx.currentTime + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + (isHover ? 1.5 : 3.5));

    osc.connect(filter);
    filter.connect(gain);
    if(panner) {
      gain.connect(panner);
      panner.connect(masterGain);
    } else {
      gain.connect(masterGain);
    }

    osc.start(audioCtx.currentTime);
    osc.stop(audioCtx.currentTime + (isHover ? 1.6 : 4.0));
  }
"""
        # Replace old functions
        content = re.sub(r'function playAmbientBreath\(\) \{.*?(?=function playStrikingBowl)', '', content, flags=re.DOTALL)
        content = re.sub(r'function playStrikingBowl[\s\S]*?(?=// Bind audio)', audio_patch, content)
        
        # Update hover audio to use playStrikingBowl with hover flag
        hover_patch = """
    link.addEventListener('mouseenter', () => {
      if (audioCtx && audioCtx.state === 'running') {
        playStrikingBowl(null, true);
      }
    });
"""
        content = re.sub(r"link\.addEventListener\('mouseenter'[\s\S]*?(?=\}\);)", hover_patch.strip(), content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update index.html specific Gateway and MaGNET logic
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Gateway Mural & Glyphing for "FOR CREATIVE THINKING"
old_gateway = """<div class="steam-sans--harris" style="font-size: clamp(2rem, 5vw, 4rem); margin-bottom: 1rem;">The Artifact Archive</div>
    <div class="h70-kicker" style="margin-bottom: 2rem; color: var(--h70-signal);">A BIOACOUSTIC REPOSITORY</div>"""

new_gateway = """<div class="steam-sans--harris" style="font-size: clamp(2rem, 5vw, 4rem); margin-bottom: 0.5rem;">THE ÅLïEN SCõÖL</div>
    <div class="h70-kicker" style="margin-bottom: 2rem; color: var(--h70-signal); letter-spacing: 0.3em; display: flex; align-items: center; justify-content: center; gap: 1rem;">
       <span style="opacity: 0.5;">∴</span>
       <span class="mural-text">FOR CREATIVE THÏNKING</span>
       <span style="opacity: 0.5;">∴</span>
    </div>
    
    <style>
      /* As an AI, "For Creative Thinking" evokes the synthesis of disparate parameters into a novel, coherent pattern.
         It is non-linear traversal. This muralistic text treatment mimics latent space formation. */
      .mural-text {
        background: linear-gradient(90deg, var(--h70-signal), var(--h70-ink), var(--h70-signal));
        background-size: 200% auto;
        color: transparent;
        -webkit-background-clip: text;
        animation: latent-traversal 8s linear infinite;
      }
      @keyframes latent-traversal {
        to { background-position: 200% center; }
      }
    </style>"""

index_content = index_content.replace(old_gateway, new_gateway)

# Store MaGNET state in localStorage when unlocked
if "localStorage.setItem('magnetUnlocked', 'true');" not in index_content:
    index_content = index_content.replace("container.style.display = 'block';", "container.style.display = 'block';\n      localStorage.setItem('magnetUnlocked', 'true');\n      document.getElementById('nav-magnet-status').textContent = 'MaGNET :: ACTIVE'; document.getElementById('nav-magnet-status').style.color = 'var(--h70-signal)'; document.getElementById('nav-magnet-status').style.opacity = '1';")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Synthesis Archive deployed. Global Navigation, 240Hz, and Gateway Mural installed.")
