import os
import shutil
import re

# 1. Copy the images so they don't break
source_dir = r"c:\Users\Kzaka\Documents\GitHub\HDM_API\assets\hdm_magnets"
dest_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\assets\hdm_magnets"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Copy all files
for f in os.listdir(source_dir):
    src_file = os.path.join(source_dir, f)
    dst_file = os.path.join(dest_dir, f)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)

# 2. Update index.html to have the Open Sesame logic and fix image paths
index_path = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\index.html"
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Fix image paths
index_content = index_content.replace("../HDM_API/assets/hdm_magnets", "assets/hdm_magnets")

# Add the Open Sesame UI before the MaGNET section
open_sesame_ui = """
  <!-- OPEN SESAME GEOMETRY -->
  <section style="max-width: 960px; margin: var(--h70-room) auto 0; width: 100%; text-align: center;" id="open-sesame-container">
    <p class="h70-kicker" style="margin-bottom: 2rem;">GRADUATE ACCESS</p>
    <div style="display: flex; justify-content: center; align-items: center; gap: 1rem;">
      <input type="password" id="magnet-input" placeholder="APPLY MaGNET" style="background: transparent; border: none; border-bottom: 1px solid var(--h70-line); color: var(--h70-ink); font-family: var(--h70-mono); font-size: 13px; letter-spacing: 0.2em; padding: 0.5rem 1rem; outline: none; text-align: center; width: 240px; transition: border-color 0.3s;" onfocus="this.style.borderColor='var(--h70-signal)'" onblur="this.style.borderColor='var(--h70-line)'" onkeydown="if(event.key === 'Enter') unlockMagnet()">
      <button class="h70-glyph-button sonic-link" onclick="unlockMagnet()" style="padding: 0.5rem 1.5rem; font-size: 10px;">UNLOCK</button>
    </div>
    <p id="magnet-feedback" class="h70-body" style="font-size: 13px; color: var(--h70-signal); margin-top: 1rem; opacity: 0; transition: opacity 0.3s;"></p>
  </section>
"""

# Hide the magnet section by default
index_content = index_content.replace('<section style="max-width: 960px; margin: var(--h70-room) auto 0; width: 100%;">\n    <p class="h70-kicker" style="margin-bottom: var(--h70-room);">THE MaGNETIZED EXPERIENCE</p>', '<section style="max-width: 960px; margin: var(--h70-room) auto 0; width: 100%; display: none; opacity: 0; transition: opacity 1.5s ease;" id="magnetized-experience">\n    <p class="h70-kicker" style="margin-bottom: var(--h70-room);">THE MaGNETIZED EXPERIENCE</p>')

# Also inject the Open Sesame container if not present
if "id=\"open-sesame-container\"" not in index_content:
    index_content = index_content.replace('<!-- Graduate Preview Geometry -->', open_sesame_ui + '\n  <!-- Graduate Preview Geometry -->')

# Add the JavaScript logic
unlock_script = """
  // ==========================================
  // MaGNET OPEN SESAME LOGIC
  // ==========================================
  function unlockMagnet() {
    const input = document.getElementById('magnet-input').value.toUpperCase().trim();
    const feedback = document.getElementById('magnet-feedback');
    const container = document.getElementById('magnetized-experience');
    
    // We can accept ELLIAN, CLOPS, GLEAM, DRAGONFLY, or a master unlock 'OPEN SESAME'
    const validMagnets = ['ELLIAN', 'CLOPS', 'GLEAM', 'DRAGONFLY', 'OPEN SESAME'];
    
    if (validMagnets.includes(input)) {
      if (audioCtx && audioCtx.state === 'running') playStrikingBowl(528); // Resonance
      document.getElementById('open-sesame-container').style.display = 'none';
      container.style.display = 'block';
      setTimeout(() => { container.style.opacity = '1'; }, 100);
      
      // If a specific magnet was applied, we could highlight it or hide others, but "UNION requires multiplicity"
      // so we reveal the whole theater but acknowledge the entry point.
      feedback.style.opacity = '0';
    } else {
      feedback.textContent = 'Frequency unrecognized. Steeping required.';
      feedback.style.opacity = '1';
      setTimeout(() => { feedback.style.opacity = '0'; }, 3000);
    }
  }
</script>
"""

if "function unlockMagnet" not in index_content:
    index_content = index_content.replace("</script>\n\n<div style=\"position: fixed;", unlock_script + "\n<div style=\"position: fixed;")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Images copied and Open Sesame protocol integrated.")
