import re

with open('test2.html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will replace the .lp-hero CSS inside the media query I just added.
old_css = """.lp-hero-content, .lp-hero-image { flex: 1 1 auto; width: 100%; }"""
new_css = """.lp-hero-content { display: contents; }
            .lp-hero-subtitle { order: 1; }
            .lp-hero h1 { order: 2; }
            .lp-hero-image { order: 3; flex: 1 1 auto; width: 100%; justify-content: center; margin-bottom: 20px; }
            .lp-hero-checklist { order: 4; margin-bottom: 30px; display: inline-block; text-align: right; }
            .lp-btn-primary { order: 5; }"""

text = text.replace(old_css, new_css)

with open('test2.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('test.html', 'r', encoding='utf-8') as f:
    text1 = f.read()
text1 = text1.replace(old_css, new_css)
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(text1)

print("Updated flex order for mobile hero")
