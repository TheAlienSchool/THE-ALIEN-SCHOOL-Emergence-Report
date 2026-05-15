import os

artifacts_dir = r"c:\Users\Kzaka\Documents\GitHub\tas-artifacts\artifacts"
files = ['magnet-ellian.html', 'magnet-clops.html', 'magnet-dragonfly.html']

for filename in files:
    filepath = os.path.join(artifacts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the double curly braces in the JS script
    content = content.replace('{{', '{')
    content = content.replace('}}', '}')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed syntax errors in Javascript blocks.")
