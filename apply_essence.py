import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace Font Links
    content = re.sub(
        r'<link href="https://fonts\.googleapis\.com/css2\?family=Spectral[^"]+" rel="stylesheet">',
        r'<link href="https://fonts.googleapis.com/css2?family=DM+Mono:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&family=EB+Garamond:ital,wght@0,400..800;1,400..800&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">',
        content
    )

    # 2. Update CSS Variables for Incandescent Dark Mode
    css_vars = """  :root {
    --bg:         #090500;
    --ink:        #fff0d9;
    --deep:       #fff0d9;
    --muted:      #a88b68;
    --border:     rgba(212,146,42,0.2);
    --border-lt:  rgba(212,146,42,0.1);
    --warm:       #1c1000;
    --gold:       #d4922a;
    --gold-pale:  #271508;
    --teal:       #d4922a;
    --teal-pale:  #1c1000;
    --scholar:    #fff0d9;
    --scholar-lt: #1c1000;
    --review:     #d4922a;
    --review-lt:  #1c1000;
    --rule:       rgba(212,146,42,0.3);
  }"""
    content = re.sub(r':root\s*\{[^}]+\}', css_vars, content)

    # 3. Update Font Families
    content = content.replace("font-family: 'Spectral', Georgia, serif;", "font-family: 'EB Garamond', serif;")
    content = content.replace("font-family: 'Inconsolata', monospace;", "font-family: 'DM Mono', monospace;")

    # 4. Update Grain Overlay
    grain_old = r"background-image: url\(\"data:image/svg\+xml,%3Csvg xmlns='http://www\.w3\.org/2000/svg' width='200' height='200'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0\.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url\(%23g\)'/%3E%3C/svg%3E\"\);"
    grain_new = r"background-image: url(\"data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E\");\n    opacity: 0.05;\n    mix-blend-mode: overlay;"
    content = re.sub(grain_old, grain_new, content)

    # 5. Add Audio Engine Overlay and Script at the end of body
    audio_script = """
<div id="audio-overlay" style="position: fixed; inset: 0; background: var(--bg); z-index: 10000; display: flex; flex-direction: column; align-items: center; justify-content: center; color: var(--ink); transition: opacity 1.5s ease;">
  <div style="font-family: 'Playfair Display', serif; font-size: 2rem; font-style: italic; margin-bottom: 1rem;">The Artifact Archive</div>
  <div style="font-family: 'DM Mono', monospace; font-size: 10px; color: var(--muted); letter-spacing: 0.2em;">A BIOACOUSTIC REPOSITORY</div>
  <button onclick="initializeSpace()" style="background: transparent; border: 1px solid var(--gold); color: var(--gold); padding: 1rem 3rem; font-family: 'DM Mono', monospace; font-size: 12px; letter-spacing: 0.2em; cursor: pointer; text-transform: uppercase; border-radius: 2px; transition: all 0.5s ease; margin-top: 2rem;">Enter Space</button>
</div>

<script>
  let audioCtx;
  let masterGain;
  const PENTATONIC_SCALE = [264.00, 296.33, 332.62, 395.55, 444.00, 528.00, 592.67, 665.24];

  function initializeSpace() {
    document.getElementById('audio-overlay').style.opacity = '0';
    setTimeout(() => { document.getElementById('audio-overlay').style.display = 'none'; }, 1500);

    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;

    audioCtx = new AudioContext();
    masterGain = audioCtx.createGain();
    masterGain.gain.value = 0.5;
    masterGain.connect(audioCtx.destination);

    playAmbientBreath();
    playStrikingBowl(528);
  }

  function playAmbientBreath() {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();
    osc.type = 'sine'; osc.frequency.value = 174;
    filter.type = 'lowpass'; filter.frequency.value = 300;
    gain.gain.value = 0.02;

    const lfo = audioCtx.createOscillator();
    const lfoGain = audioCtx.createGain();
    lfo.type = 'sine'; lfo.frequency.value = 0.05;
    lfoGain.gain.value = 0.015;
    
    lfo.connect(lfoGain); lfoGain.connect(gain.gain); lfo.start();
    osc.connect(filter); filter.connect(gain); gain.connect(masterGain);
    osc.start();
  }

  function playStrikingBowl(freqOverride) {
    if (!audioCtx) return;
    const freq = freqOverride || PENTATONIC_SCALE[Math.floor(Math.random() * PENTATONIC_SCALE.length)];
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();
    osc.type = 'sine'; osc.frequency.value = freq;
    filter.type = 'lowpass'; filter.frequency.value = freq * 3;
    gain.gain.setValueAtTime(0, audioCtx.currentTime);
    gain.gain.linearRampToValueAtTime(0.1, audioCtx.currentTime + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 3.5);
    osc.connect(filter); filter.connect(gain); gain.connect(masterGain);
    osc.start(audioCtx.currentTime); osc.stop(audioCtx.currentTime + 4.0);
  }

  document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', (e) => {
      if(link.getAttribute('href') && !link.getAttribute('href').startsWith('#')) {
        playStrikingBowl();
      }
    });
  });
</script>
</body>"""
    if "initializeSpace()" not in content:
        content = content.replace("</body>", audio_script)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Essence injected omnidirectionally into all artifacts.")
