import re
import subprocess

with open('test2.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
if m:
    with open('temp.js', 'w', encoding='utf-8') as f:
        f.write(m.group(1))
    result = subprocess.run(['node', '-c', 'temp.js'], capture_output=True, text=True)
    if result.returncode == 0:
        print("Syntax OK")
    else:
        print("Syntax Error:\n" + result.stderr)
else:
    print("No script found")
