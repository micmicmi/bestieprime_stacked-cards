import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html','r',encoding='utf-8') as f:
    content = f.read()

indices = []
idx = content.find('data-index="2"')
while idx != -1:
    indices.append(idx)
    idx = content.find('data-index="2"', idx + 1)

for i in indices:
    print("---")
    print(content[i-150:i+350])
