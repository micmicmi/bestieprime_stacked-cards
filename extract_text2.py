import re

with open('test.html', 'r', encoding='utf-8') as f:
    text = f.read()

out = []
for i, section in enumerate(re.finditer(r'<h2 class="step-headline">(.*?)</h2>\s*<p class="step-body">\s*(.*?)\s*</p>', text, re.DOTALL)):
    out.append(f"Slide {i+1}:")
    out.append("Head: " + section.group(1))
    out.append("Body: " + section.group(2).strip())
    out.append("")

with open('text_out2.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))
