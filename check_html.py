import sys
sys.stdout.reconfigure(encoding='utf-8')
lines = open('index.html','r',encoding='utf-8').readlines()
idx = -1
for i, l in enumerate(lines):
    if 'class="mobile-gallery-section mobile-only"' in l:
        idx = i
        break
if idx != -1:
    print(''.join(lines[idx-3:idx+3]))
