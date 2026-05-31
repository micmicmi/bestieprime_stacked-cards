import re

with open('test2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the script tag
script_start = content.find('<script>')
script_end = content.find('</script>', script_start)

script_content = content[script_start:script_end]

# Split by the comment
parts = script_content.split('// --- Mobile Gallery Logic ---')

if len(parts) > 2:
    # Keep the first part (GSAP) and the second part (Mobile JS)
    new_script = parts[0] + '// --- Mobile Gallery Logic ---' + parts[1]
    
    new_content = content[:script_start] + new_script + content[script_end:]
    
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Fixed script duplication")
else:
    print(f"Found {len(parts)} parts, no duplication?")
