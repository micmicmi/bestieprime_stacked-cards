def fix_mobile_and_sections():
    with open('test.html', 'r', encoding='utf-8') as f:
        test = f.read()
    with open('test2.html', 'r', encoding='utf-8') as f:
        t2 = f.read()

    # Extract mobile gallery from test.html (lines 1064-1113)
    mobile_start = test.find('<div class="mobile-gallery-section mobile-only">')
    mobile_end_search = test.find('        </div>\n\n        <div class="lp-wrapper">', mobile_start)
    # close tag is at 1113-1116
    mobile_html = test[mobile_start:mobile_end_search + len('        </div>')].strip()
    print(f"Mobile gallery: {len(mobile_html)} chars, starts: {repr(mobile_html[:60])}")

    # In test2.html, find where mwg_effect031 section closes
    mwg_close = t2.find('    </section>')
    after_mwg = t2[mwg_close + len('    </section>'):]
    before_mwg = t2[:mwg_close + len('    </section>')]

    # Now find where the bottom lp-wrapper starts in test2
    bottom_lp_start = after_mwg.find('<div class="lp-wrapper">')
    # And where the script starts
    script_start = after_mwg.find('<script>')

    bottom_sections = after_mwg[bottom_lp_start:script_start].strip()
    script_and_rest = after_mwg[script_start:]

    print(f"Bottom sections already in test2: {len(bottom_sections)} chars")

    # Rebuild: before_mwg + newline + mobile_gallery + newline + bottom_sections + newline + script
    new_content = (
        before_mwg + '\n\n' +
        mobile_html + '\n\n' +
        bottom_sections + '\n\n' +
        script_and_rest
    )

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("Done! Mobile gallery and sections are now in correct order.")

if __name__ == '__main__':
    fix_mobile_and_sections()
