import re
with open('test.html', 'r', encoding='utf-8') as f:
    text = f.read()
for m in re.findall(r'<video[^>]*src="([^"]+)"', text):
    print(m)
