import re

for filename in ['test.html', 'test2.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Hide mwg_effect031 on mobile
    content = content.replace('<section class="mwg_effect031">', '<section class="mwg_effect031 desktop-only">')
    content = content.replace('<section class="mwg_effect031 desktop-only desktop-only">', '<section class="mwg_effect031 desktop-only">')

    # 2. Move .mobile-nav-dots below mobile-gallery-container
    nav_dots_match = re.search(r'(<div class="mobile-nav-dots">.*?</div>\s*)<div class="mobile-gallery-container"', content, re.DOTALL)
    if nav_dots_match:
        nav_dots = nav_dots_match.group(1)
        content = content.replace(nav_dots, '')
        
        insert_target = '        </div>\n    </div>\n\n    <div class="lp-wrapper">'
        replacement = '        </div>\n\n' + nav_dots + '    </div>\n\n    <div class="lp-wrapper">'
        
        if insert_target in content:
            content = content.replace(insert_target, replacement)
        else:
            print(f'Warning: Could not find insert target in {filename}')
            
    # 3. Add .step-number CSS to the media query
    css_to_add = """
            .mobile-header-text .step-number {
                font-family: 'ploni', 'Heebo', sans-serif;
                font-size: 36px;
                color: #FF1D00;
                font-weight: 700;
                margin-bottom: 5px;
                opacity: 1;
            }"""
    if 'mobile-header-text .step-number' not in content:
        # inject into the @media (max-width: 768px) block we added
        target = '.header-inner { height: 60px; }'
        content = content.replace(target, target + css_to_add)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print('Updated HTML and CSS.')
