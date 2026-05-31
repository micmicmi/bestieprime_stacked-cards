def rebuild():
    # Read both files
    with open('test.html', 'r', encoding='utf-8') as f:
        test = f.read()
    with open('test2.html', 'r', encoding='utf-8') as f:
        t2 = f.read()

    # === EXTRACT FROM test.html ===

    # 1. The bottom sections (Section 3, 4, 5) from test.html lines 1118-1220
    bottom_sections_start = test.find('<div class="lp-wrapper">', test.find('id="mobileGallery"'))
    bottom_sections_end = test.find('        <script>', bottom_sections_start)
    bottom_sections_html = test[bottom_sections_start:bottom_sections_end].rstrip()
    print(f"Bottom sections: {len(bottom_sections_html)} chars, starts: {repr(bottom_sections_html[:80])}")

    # 2. The mobile gallery JS from test.html
    mobile_js_start = test.find('// --- Mobile Gallery Logic ---')
    mobile_js_end = test.find('</script>', mobile_js_start)
    mobile_js = test[mobile_js_start:mobile_js_end].rstrip()
    print(f"Mobile JS: {len(mobile_js)} chars")

    # === EXTRACT FROM test2.html ===

    # 1. Everything from start up to and including </section> (which closes mwg_effect031)
    mwg_section_close = t2.find('    </section>')
    if mwg_section_close == -1:
        print("ERROR: can't find mwg_effect031 close")
        return
    header_and_cards = t2[:mwg_section_close + len('    </section>')]
    print(f"Header+cards: {len(header_and_cards)} chars")

    # 2. Mobile gallery HTML from test2.html
    mobile_start = t2.find('<div class="mobile-gallery-section mobile-only">')
    # Find mobile gallery end by counting divs
    pos = mobile_start
    depth = 0
    end_pos = mobile_start
    while True:
        next_open = t2.find('<div', pos + 1)
        next_close = t2.find('</div>', pos + 1)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open
        else:
            if depth == 0:
                end_pos = next_close + 6
                break
            depth -= 1
            pos = next_close
    mobile_gallery_html = t2[mobile_start:end_pos]
    print(f"Mobile gallery HTML: {len(mobile_gallery_html)} chars")

    # 3. The GSAP JS from test2.html (the new one, not test.html's)
    gsap_js_start = t2.find('function initExpertiseScrollEffect()')
    gsap_js_end = t2.find('</script>', gsap_js_start) 
    gsap_js_full = t2[t2.find('gsap.registerPlugin', gsap_js_start - 200):gsap_js_end]
    print(f"GSAP JS: {len(gsap_js_full)} chars")

    # === BUILD THE NEW FILE ===

    # Get the CSS/head from test2.html (up to </style></head>)
    head_end = t2.find('</style>') + len('</style>')
    head_section = t2[:head_end]

    # Build complete file:
    new_file = (
        head_section + '\n</head>\n\n<body>\n\n' +
        # Header (extract from test2 - between <body> and start of lp-wrapper)
        _extract_between(t2, '<body>', '<div class="lp-wrapper">').strip() + '\n\n' +
        # First lp-wrapper (hero + banks + two-col sections 1 and 2)
        _extract_first_lp_wrapper(t2) + '\n\n' +
        # mwg_effect031 section
        '    <section class="mwg_effect031">\n' +
        _extract_between(t2, '<section class="mwg_effect031">', '</section>') +
        '    </section>\n\n' +
        # Mobile gallery (mobile-only)
        mobile_gallery_html + '\n\n' +
        # Bottom sections (3, 4, 5) from test.html
        bottom_sections_html + '\n\n' +
        # Script
        '<script>\n' +
        gsap_js_full + '\n\n' +
        mobile_js + '\n' +
        '</script>\n\n</body>\n</html>\n'
    )

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(new_file)

    print("Done! test2.html rebuilt cleanly.")

def _extract_between(content, start_marker, end_marker):
    s = content.find(start_marker)
    e = content.find(end_marker, s + len(start_marker))
    return content[s + len(start_marker):e]

def _extract_first_lp_wrapper(content):
    start = content.find('<div class="lp-wrapper">')
    # Find the close of this lp-wrapper (before mwg_effect031)
    mwg_pos = content.find('<section class="mwg_effect031">')
    end = content.rfind('</div>', start, mwg_pos) + 6
    return content[start:end]

if __name__ == '__main__':
    rebuild()
