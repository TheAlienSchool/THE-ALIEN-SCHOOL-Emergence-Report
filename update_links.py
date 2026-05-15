import os

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
files = ['magnet-ellian.html', 'magnet-clops.html', 'magnet-dragonfly.html']

for filename in files:
    filepath = os.path.join(artifacts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update links to bypass the initial gateway
    content = content.replace('href="../index.html"', 'href="../index.html#archive-core"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated links to point to the second layer of index.html.")
