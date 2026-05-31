import re

with open('text_out2.txt', 'r', encoding='utf-8') as f:
    text = f.read()

slides_data = []
blocks = text.strip().split('Slide ')
for b in blocks:
    if not b: continue
    lines = b.strip().split('\n')
    head = lines[1].replace('Head: ', '').strip()
    body = ' '.join([l.strip() for l in lines[2:]]).replace('Body: ', '').strip()
    body = re.sub(r'\s+', ' ', body)
    slides_data.append((head, body))

with open('build_final.py', 'r', encoding='utf-8') as f:
    bf = f.read()

for i, (head, body) in enumerate(slides_data):
    pattern = r"('num': '0" + str(i+1) + r"',\s*'title': ')[^']*('.*?'desc': ')[^']*(')"
    replacement = rf"\g<1>{head}\g<2>{body}\g<3>"
    bf = re.sub(pattern, replacement, bf, count=1, flags=re.DOTALL)

with open('build_final.py', 'w', encoding='utf-8') as f:
    f.write(bf)

print("build_final.py updated.")
