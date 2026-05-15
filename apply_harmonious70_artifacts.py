import os
import glob
import re

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
html_files = glob.glob(os.path.join(artifacts_dir, "*.html"))

parallax_script = """
<script>
  // ==========================================
  // PARALLAX SCIENCES
  // ==========================================
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

    const mural = document.querySelector('.parallax-mural');
    if (mural) {
      mural.style.transform = `translate(${currentX * -20}px, ${currentY * -20}px) scale(1.05)`;
    }

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
"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add stylesheet link if not present
    if "harmonious70.css" not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="../harmonious70.css">\n</head>')

    # Set data-h70-scene on body
    content = re.sub(r'<body[^>]*>', '<body data-h70-scene="night">', content)

    # Wrap page in h70-installation and add muralist if not present
    if 'h70-installation' not in content:
        content = content.replace('<div class="page">', 
            '<main class="h70-installation" style="display:block; padding-top: 2rem;">\n  <div class="h70-muralist parallax-mural" aria-hidden="true"></div>\n  <div class="page" style="background: transparent;">')
        content = content.replace('</body>', '</main>\n</body>')

    # Add parallax-vessel to specific elements
    content = content.replace('class="scholar-card"', 'class="scholar-card parallax-vessel"')
    content = content.replace('class="review"', 'class="review parallax-vessel"')
    content = content.replace('class="link-card"', 'class="link-card parallax-vessel"')

    # Inject Parallax Script before </body>
    if "PARALLAX SCIENCES" not in content:
        content = content.replace('</body>', parallax_script + '\n</body>')

    # Optional: ensure smooth transitions for parallax vessels in internal style
    if '.parallax-vessel' not in content:
        content = content.replace('</style>', '  .parallax-vessel { will-change: transform; transition: box-shadow 420ms var(--h70-ease), border-color 420ms var(--h70-ease); }\n</style>')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("HÅRMONIOUS70 and Parallax Sciences injected into all artifacts.")
