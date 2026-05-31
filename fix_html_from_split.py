import re

def extract_section(content, class_name):
    start_idx = content.find(f'<div class="{class_name}')
    if start_idx == -1: return None
    
    pos = start_idx
    depth = 0
    while True:
        no = content.find('<div', pos + 1)
        nc = content.find('</div>', pos + 1)
        if nc == -1: break
        
        if no != -1 and no < nc:
            depth += 1
            pos = no
        else:
            if depth == 0:
                end_idx = nc + 6
                return content[start_idx:end_idx]
            depth -= 1
            pos = nc
    return None

with open('stacked_cards_split.html', 'r', encoding='utf-8') as f:
    split_content = f.read()

correct_mobile_section = extract_section(split_content, 'mobile-gallery-section mobile-only')
if correct_mobile_section:
    # Fix the typo inside the extracted section
    correct_mobile_section = correct_mobile_section.replace('.m p4', '.mp4')

    for target_file in ['test.html', 'test2.html']:
        with open(target_file, 'r', encoding='utf-8') as f:
            target_content = f.read()
            
        old_section = extract_section(target_content, 'mobile-gallery-section mobile-only')
        if old_section:
            # First, clean up the broken remnants at the bottom
            # The broken remnants are `<div class="m-dot"></div>` left below the gallery.
            # Actually, instead of replacing just the section, let's fix the broken remnants too.
            # The remnants were at the end of the mobile gallery section.
            
            # Since the broken remnants were at the end of the mobile-gallery-container,
            # Let's just find the start of mobile-gallery-section and the end of lp-wrapper, and replace
            start_mobile = target_content.find('<div class="mobile-gallery-section mobile-only">')
            end_mobile_approx = target_content.find('<div class="lp-wrapper">', start_mobile)
            
            # Cleanly replace everything between start_mobile and <div class="lp-wrapper">
            # with the correct_mobile_section
            if start_mobile != -1 and end_mobile_approx != -1:
                new_content = target_content[:start_mobile] + correct_mobile_section + '\n\n    ' + target_content[end_mobile_approx:]
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed mobile section in {target_file}")
            else:
                print(f"Could not find boundaries in {target_file}")

else:
    print("Could not extract from stacked_cards_split.html")
