def fix():
    with open('test.html', 'r', encoding='utf-8') as f:
        test_content = f.read()

    with open('test2.html', 'r', encoding='utf-8') as f:
        test2_content = f.read()

    # From test.html, find the SECOND lp-wrapper (the one that comes after the cards section)
    # The structure in test.html is:
    # <div class="lp-wrapper"> ... hero, banks, two-col sections ... </div>
    # <section class="cards-area-wrapper"> ... mwg_effect031 ... </section>
    # <div class="lp-wrapper"> ... sections 3, 4, 5 ... </div>
    
    # Find the second lp-wrapper
    first_lp = test_content.find('<div class="lp-wrapper">')
    second_lp = test_content.find('<div class="lp-wrapper">', first_lp + 10)
    
    if second_lp == -1:
        print("No second lp-wrapper found, trying after mwg section")
        mwg_pos = test_content.find('mwg_effect031')
        second_lp = test_content.find('<div class="lp-wrapper">', mwg_pos)
    
    # Find the end (before </body>)
    body_close = test_content.rfind('</body>')
    last_div_close = test_content.rfind('</div>', 0, body_close) + 6
    
    sections_html = test_content[second_lp:last_div_close]
    
    print(f"Sections from second lp-wrapper: {len(sections_html)} chars")
    print(f"Starts with: {repr(sections_html[:150])}")
    
    # Now in test2.html, check if this lp-wrapper already exists after mwg_effect031
    # It was inserted by restore_sections.py but may have included hero + banks sections too
    # Let's remove ALL the stuff after the mobile gallery and re-insert cleanly
    
    # Find mobile gallery end in test2.html
    mobile_end = test2_content.find('</div>', 
                  test2_content.find('</div>',
                  test2_content.find('id="mobileGallery"') + 10) + 10) + 6
    
    # Find the script tag
    script_pos = test2_content.find('<script>')
    
    # Everything between mobile_end and script is the stuff we inserted (may be incorrect)
    # Replace it with correct sections
    new_content = test2_content[:mobile_end] + '\n\n' + sections_html + '\n\n' + test2_content[script_pos:]
    
    # Also add missing </section> for lp-two-col if needed
    # Count sections to check
    open_count = new_content.count('<section')
    close_count = new_content.count('</section>')
    print(f"Open sections: {open_count}, Close sections: {close_count}")
    
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Done")

if __name__ == '__main__':
    fix()
