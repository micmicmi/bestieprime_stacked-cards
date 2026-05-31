import re

with open('test.html', 'r', encoding='utf-8') as f:
    text = f.read()

for i, section in enumerate(re.finditer(r'<h2 class="step-headline">(.*?)</h2>\s*<p class="step-body">\s*(.*?)\s*</p>', text, re.DOTALL)):
    print(f"Slide {i+1}:")
    print("Head: " + section.group(1))
    print("Body: " + section.group(2).strip())
    print()
