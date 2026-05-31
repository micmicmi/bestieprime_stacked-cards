import re

def modify():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. First, extract the mobile gallery HTML block. We can just take the first one found.
    # It starts with <div class="mobile-gallery-section mobile-only">
    # And it ends before the next </section>
    
    first_match = re.search(r'\n\s*<div class="mobile-gallery-section mobile-only">.*?(?=\s*</section>)', content, flags=re.DOTALL)
    if not first_match:
        print("Mobile gallery HTML not found!")
        return
        
    mobile_html = first_match.group(0)

    # 2. Remove ALL occurrences of the mobile gallery HTML block
    content = re.sub(r'\n\s*<div class="mobile-gallery-section mobile-only">.*?(?=\s*</section>)', '', content, flags=re.DOTALL)

    # 3. Find the end of <section class="mwg_effect031">
    mwg_start = content.find('<section class="mwg_effect031">')
    if mwg_start == -1:
        print("Could not find mwg_effect031 section")
        return
        
    mwg_end = content.find('</section>', mwg_start)
    if mwg_end == -1:
        print("Could not find closing section of mwg_effect031")
        return

    # 4. Inject exactly ONE copy right before mwg_end
    content = content[:mwg_end] + mobile_html + '\n    ' + content[mwg_end:]

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully removed duplicates and injected mobile gallery correctly")

if __name__ == '__main__':
    modify()
