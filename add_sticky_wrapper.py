import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

idx_start = -1
for i, l in enumerate(lines):
    if 'class="mobile-gallery-section mobile-only"' in l:
        idx_start = i
        break

if idx_start != -1:
    open_tags = 0
    idx_end = -1
    for i in range(idx_start, len(lines)):
        line = lines[i]
        open_tags += line.count('<div') - line.count('</div')
        if open_tags <= 0:
            idx_end = i
            break
    
    print(f'Start: {idx_start}, End: {idx_end}')
    
    # Let's write the modifications
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add wrapper HTML
    # We will just replace the exact lines
    lines.insert(idx_end + 1, '    </div><!-- end mobile-sticky-wrapper -->\n')
    lines.insert(idx_start, '    <div class="mobile-sticky-wrapper mobile-only">\n')
    
    # Update CSS
    css_to_replace = """        .mobile-gallery-section {
            padding: 20px 0 20px;
            /* Equivalent to pt-24 (approximated) */
            background: #F0F5F5;
            min-height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }"""
    
    new_css = """        .mobile-sticky-wrapper {
            position: relative;
            height: 200vh; /* Provides vertical scroll space for sticky section */
        }

        .mobile-gallery-section {
            padding: 20px 0 20px;
            background: #F0F5F5;
            position: sticky;
            top: 70px; /* Header height offset */
            height: calc(100vh - 70px);
            min-height: calc(100vh - 70px);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }"""
        
    with open('index.html', 'w', encoding='utf-8') as f:
        new_content = "".join(lines)
        if css_to_replace in new_content:
            new_content = new_content.replace(css_to_replace, new_css)
            print("CSS replaced successfully.")
        else:
            print("Could not find exact CSS to replace.")
        f.write(new_content)
else:
    print("Could not find start index.")
