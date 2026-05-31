import re

with open('test.html', 'r', encoding='utf-8') as f:
    text = f.read()
vids = re.findall(r'<video[^>]*src="([^"]+)"', text)

with open('build_final.py', 'r', encoding='utf-8') as f:
    bf = f.read()

# Replace slide 2 video
bf = re.sub(r"'video': '\./vid\+gif/הוצאות נוספות\.mp4'", f"'video': '{vids[1]}'", bf)
# Replace slide 3 video
bf = re.sub(r"'video': '\./vid\+gif/פרטי הלווים-1\.mp4'", f"'video': '{vids[2]}'", bf)
# Replace slide 4 video
bf = re.sub(r"'video': '\./vid\+gif/החזר חודשי_ארוך\.mp4'", f"'video': '{vids[3]}'", bf)

with open('build_final.py', 'w', encoding='utf-8') as f:
    f.write(bf)

print("Updated build_final.py")
