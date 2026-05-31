def fix():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # The lp-wrapper with sections got inserted inside the mobileGallery container.
    # Find the lp-wrapper that's wrongly inside mobileGallery
    mobile_gallery_container = content.find('id="mobileGallery"')
    lp_wrapper_inside = content.find('<div class="lp-wrapper">', mobile_gallery_container)

    if lp_wrapper_inside == -1:
        print("lp-wrapper not found inside mobileGallery - already fixed?")
        return

    print(f"Found lp-wrapper inside mobileGallery at pos {lp_wrapper_inside}")

    # Find the END of the mobile-gallery-section
    # This is simpler: find </div> that closes mobile-gallery-section mobile-only
    mobile_section_start = content.find('<div class="mobile-gallery-section mobile-only">')
    
    # Find the </div> that closes mobile-gallery-section (3 levels deep: section > dots + gallery-container > cards)
    # Just find the 4th </div> after mobile_section_start (section close)
    pos = mobile_section_start
    count = 0
    while True:
        pos = content.find('</div>', pos + 1)
        if pos == -1:
            print("ERROR: ran out of closing divs")
            return
        count += 1
        # Count corresponding opens between mobile_section_start and this </div>
        opens = content[mobile_section_start:pos].count('<div')
        closes = content[mobile_section_start:pos+6].count('</div>')
        if opens == closes:
            mobile_section_end = pos + 6
            print(f"Mobile section ends at pos {mobile_section_end}")
            break

    # Extract the lp-wrapper from inside mobileGallery
    # Find where lp-wrapper ends
    lp_end_pos = lp_wrapper_inside
    depth = 0
    while True:
        next_open = content.find('<div', lp_end_pos + 1)
        next_close = content.find('</div>', lp_end_pos + 1)
        if next_close == -1:
            print("ERROR: no closing div")
            return
        if next_open != -1 and next_open < next_close:
            depth += 1
            lp_end_pos = next_open
        else:
            if depth == 0:
                lp_wrapper_end = next_close + 6
                break
            depth -= 1
            lp_end_pos = next_close

    lp_wrapper_html = content[lp_wrapper_inside:lp_wrapper_end]
    print(f"lp-wrapper is {len(lp_wrapper_html)} chars, starts: {repr(lp_wrapper_html[:80])}")

    # Remove lp-wrapper from inside mobileGallery
    content = content[:lp_wrapper_inside] + content[lp_wrapper_end:]

    # Recalculate mobile_section_end after the removal (it shifted left)
    shift = len(lp_wrapper_html)
    mobile_section_end -= shift

    # Now insert AFTER mobile-gallery-section
    content = content[:mobile_section_end] + '\n\n' + lp_wrapper_html + content[mobile_section_end:]

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done - sections moved to correct position")

if __name__ == '__main__':
    fix()
