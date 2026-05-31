import re

with open('stacked_cards_split.html', 'r', encoding='utf-8') as f:
    split_content = f.read()

# Extract CSS from stacked_cards_split.html
mobile_css_match = re.search(r'(/\* Mobile Gallery Styles \*/.*?)(/\* Replaces Tailwind Utility Classes \*/|\</style\>)', split_content, re.DOTALL)
if mobile_css_match:
    correct_css = mobile_css_match.group(1)
    
    for target_file in ['test.html', 'test2.html']:
        with open(target_file, 'r', encoding='utf-8') as f:
            target_content = f.read()
            
        old_css_match = re.search(r'(/\* Mobile Gallery Styles \*/.*?)(/\* Replaces Tailwind Utility Classes \*/|\</style\>)', target_content, re.DOTALL)
        if old_css_match:
            old_css = old_css_match.group(1)
            # Replace old mobile css with correct mobile css
            target_content = target_content.replace(old_css, correct_css)
            
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(target_content)
            print(f"Updated CSS in {target_file}")
        else:
            print(f"Could not find old css in {target_file}")
else:
    print("Could not find CSS in split file")
