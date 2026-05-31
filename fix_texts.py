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
    # clean up multiple spaces
    body = re.sub(r'\s+', ' ', body)
    slides_data.append((head, body))

with open('test2.html', 'r', encoding='utf-8') as f:
    t2 = f.read()

# Replace desktop texts
for i, (head, body) in enumerate(slides_data):
    # Find the h3 step-title for this slide
    # Slide i is the one with <h2 class="step-label">0{i+1}</h2>
    
    # We can use regex to replace it
    pattern = r'(<h2 class="step-label">0' + str(i+1) + r'</h2>\s*<h3 class="step-title">)[^<]*(</h3>\s*<p class="step-description">)[^<]*(</p>)'
    replacement = rf'\g<1>{head}\g<2>{body}\g<3>'
    t2 = re.sub(pattern, replacement, t2, count=1)

# Replace mobile texts in the JS array
# Look for mobileStepsData = [ ... ]
js_start = t2.find('const mobileStepsData = [')
js_end = t2.find('];', js_start)

if js_start != -1:
    new_arr = "const mobileStepsData = [\n"
    for i, (head, body) in enumerate(slides_data):
        new_arr += f"""            {{
                num: "0{i+1}",
                head: "{head}",
                body: "{body}"
            }}{"," if i < 4 else ""}
"""
    t2 = t2[:js_start] + new_arr + t2[js_end:]

with open('test2.html', 'w', encoding='utf-8') as f:
    f.write(t2)

print("test2.html updated with correct texts.")
