import re

with open('test.html', 'r', encoding='utf-8') as f:
    text = f.read()

vids = re.findall(r'<video[^>]*src="([^"]+)"', text)

with open('test2.html', 'r', encoding='utf-8') as f:
    t2 = f.read()

# Replace slide 2 video
t2 = re.sub(r'src="\./vid\+gif/הוצאות נוספות\.mp4"', f'src="{vids[1]}"', t2)
# Replace slide 3 video
t2 = re.sub(r'src="\./vid\+gif/פרטי הלווים-1\.mp4"', f'src="{vids[2]}"', t2)
# Replace slide 4 video
t2 = re.sub(r'src="\./vid\+gif/החזר חודשי_ארוך\.mp4"', f'src="{vids[3]}"', t2)

with open('test2.html', 'w', encoding='utf-8') as f:
    f.write(t2)

print("Updated video paths in test2.html")
