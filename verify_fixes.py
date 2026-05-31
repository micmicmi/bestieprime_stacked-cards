import re

with open('test2.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("mwg_effect031 matches:", re.findall(r'<section class=\"mwg_effect031.*?>', content))
print("step number css matches:", re.findall(r'\.mobile-header-text \.step-number.*?\}', content, re.DOTALL))

