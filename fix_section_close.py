import re

def rebuild():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start of the mwg_effect031 section
    mwg_start = content.find('<section class="mwg_effect031">')
    if mwg_start == -1:
        print("ERROR: Can't find mwg_effect031")
        return

    # Find the mobile gallery section start (right after the last expertise-slide)
    mobile_gallery_start = content.find('<div class="mobile-gallery-section mobile-only">', mwg_start)
    mobile_gallery_end = content.find('</div>', content.find('</div>', mobile_gallery_start + 100) + 100) 
    # That's rough - let's find it properly
    # The mobile gallery ends with </div>\n\n    </div>\n\n        </div> pattern
    # Let's just find the </div>\n\n from right after mobile-gallery-container close
    
    gallery_container_end = content.find('</div>', content.find('</div>', content.find('id="mobileGallery"') + 10) + 10)
    # Find close of mobile-gallery-section
    mobile_section_end = content.find('</div>', gallery_container_end + 1) + 6
    
    # The content AFTER the mobile section that properly closes things
    after_mobile = content[mobile_section_end:]
    
    # Now check what comes after - there should be  </section> to close mwg_effect031
    # But it's missing. Let's close it properly.
    # Find the next significant thing after mobile_section_end
    print(f"After mobile section: {repr(after_mobile[:200])}")
    
    # Rebuild: everything before the mobile gallery + </section> closing + rest
    # The mobile gallery should be INSIDE the section (or we move it outside)
    # Let's move the mobile gallery OUTSIDE the section (after </section>)
    
    before_mobile = content[:mobile_gallery_start]
    mobile_html = content[mobile_gallery_start:mobile_section_end]
    after_mobile_rest = content[mobile_section_end:]
    
    # Trim any stray whitespace/newlines before inserting </section>
    before_mobile = before_mobile.rstrip()
    
    # Insert </section> after the slides, then the mobile gallery, then continue
    fixed = before_mobile + '\n    </section>\n\n    ' + mobile_html + after_mobile_rest
    
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(fixed)
    
    print("Fixed: </section> added after slides, mobile gallery moved outside")

if __name__ == '__main__':
    rebuild()
