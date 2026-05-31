import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Move mobile-nav-dots ABOVE mobile-gallery-container
    nav_dots_match = re.search(r'<div class="mobile-nav-dots">.*?</div>', content, re.DOTALL)
    if nav_dots_match:
        nav_dots = nav_dots_match.group(0)
        # remove it from current location (which is below mobile-gallery-container right now)
        content = content.replace(nav_dots, '')
        
        # insert above mobile-gallery-container
        insert_target = '<div class="mobile-gallery-container"'
        if insert_target in content:
            content = content.replace(insert_target, nav_dots + '\n\n        ' + insert_target)

    # 2. Fix CSS of .mobile-gallery-section to match stacked_cards_split
    old_section_css = r'\.mobile-gallery-section\s*\{\s*padding: 60px 0 60px;\s*/\* Equivalent to pt-24 \(approximated\) \*/\s*background: #F0F5F5;\s*min-height: 70vh;\s*overflow: hidden;\s*display: flex;\s*flex-direction: column;\s*\}'
    new_section_css = """.mobile-gallery-section {
            padding: 60px 0 60px;
            /* Equivalent to pt-24 (approximated) */
            background: #F8FAFC;
            min-height: 100vh;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }"""
    content = re.sub(old_section_css, new_section_css, content)

    # 3. Fix CSS of .mobile-nav-dots
    old_dots_css = r'\.mobile-nav-dots\s*\{\s*display: flex;\s*justify-content: center;\s*gap: 8px;\s*margin-top: 15px;\s*\}'
    new_dots_css = """.mobile-nav-dots {
            display: flex;
            justify-content: start;
            gap: 10px;
            margin-top: 0px;
            margin-bottom: 40px;
            margin-right: 24px;
        }"""
    content = re.sub(old_dots_css, new_dots_css, content)

    # 4. Remove the step-number CSS I added to the media query
    # and add the proper step-number CSS
    bad_step_css = r'\.mobile-header-text \.step-number\s*\{[^\}]*\}'
    content = re.sub(bad_step_css, '', content)
    
    # insert step-number css before .mobile-gallery-section
    step_css_to_add = """
        .step-number {
            font-size: 56px;
            font-weight: 900;
            color: var(--primary-red);
            line-height: 0.8;
            margin-bottom: 1rem;
            opacity: 0.15;
            margin-bottom: 0;
        }

        @media (max-width: 768px) {
            .step-number {
                font-size: 36px;
                margin-bottom: 5px !important;
                opacity: 1;
                color: #FF1D00;
            }
        }
"""
    if '.step-number {' not in content:
        content = content.replace('.mobile-gallery-section {', step_css_to_add + '\n        .mobile-gallery-section {')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

for f in ['test.html', 'test2.html']:
    update_file(f)

print('Updated to stacked_cards_split styling and layout.')
