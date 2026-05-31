import re

def restore_sections():
    with open('test.html', 'r', encoding='utf-8') as f:
        test_content = f.read()

    with open('test2.html', 'r', encoding='utf-8') as f:
        test2_content = f.read()

    # In test.html, extract the second lp-wrapper that comes AFTER the mwg_effect031 section
    # (the one with sections 3, 4, 5 etc.)
    # In test.html, there are two lp-wrappers. The second one starts after the mwg_effect031 section.
    
    # Find the mwg_effect031 section in test.html
    mwg_end_test = test_content.find('</section>', test_content.find('mwg_effect031')) + len('</section>')
    
    # Now find the next lp-wrapper after that
    second_lp_wrapper_start = test_content.find('<div class="lp-wrapper">', mwg_end_test)
    
    if second_lp_wrapper_start == -1:
        print("ERROR: Could not find second lp-wrapper in test.html")
        return
    
    # Find where the second lp-wrapper ends (before </body>)
    body_close_test = test_content.rfind('</body>')
    # Go backwards to find the last </div> before </body>
    second_lp_wrapper_end = test_content.rfind('</div>', 0, body_close_test) + len('</div>')
    
    extracted_html = test_content[second_lp_wrapper_start:second_lp_wrapper_end]
    print(f"Extracted {len(extracted_html)} chars of section HTML")
    print(f"Preview: {repr(extracted_html[:200])}")
    
    # Now insert this into test2.html before </body>
    insertion_point = test2_content.find('<script>')
    if insertion_point == -1:
        insertion_point = test2_content.find('</body>')
    
    new_content = test2_content[:insertion_point] + '\n' + extracted_html + '\n\n' + test2_content[insertion_point:]
    
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done: sections restored into test2.html")

if __name__ == '__main__':
    restore_sections()
