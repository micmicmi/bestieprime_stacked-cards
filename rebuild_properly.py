def rebuild_properly():
    with open('test.html', 'r', encoding='utf-8') as f:
        test = f.read()
    with open('test2.html', 'r', encoding='utf-8') as f:
        t2 = f.read()

    # === FROM test2.html - extract the good parts ===
    # 1. Head (CSS)
    head_close = t2.find('</style>') + len('</style>')
    head_section = t2[:head_close]

    # 2. Header HTML (between </style></head> and the first lp-wrapper)
    body_start = t2.find('<body>')
    first_lp = t2.find('<div class="lp-wrapper">')
    header_html = t2[body_start + len('<body>'):first_lp].strip()

    # 3. The first lp-wrapper (hero, banks, sections 1+2 in test2)
    lp1_start = t2.find('<div class="lp-wrapper">')
    # Find the first </div> that balances it
    pos = lp1_start
    depth = 0
    lp1_end = lp1_start
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
                lp1_end = next_close + 6
                break
            depth -= 1
            pos = next_close
    first_lp_html = t2[lp1_start:lp1_end]
    print(f"First lp-wrapper: {len(first_lp_html)} chars, ends with: {repr(first_lp_html[-50:])}")

    # 4. The mwg_effect031 section from test2.html - find it after lp1_end
    mwg_start = t2.find('<section class="mwg_effect031">', lp1_end)
    if mwg_start == -1:
        print("ERROR: mwg_effect031 not found in test2.html")
        return
    # Find its close
    mwg_close = t2.find('    </section>', mwg_start) + len('    </section>')
    mwg_html = t2[mwg_start:mwg_close]
    print(f"mwg section: {len(mwg_html)} chars")

    # 5. The GSAP JS from test2.html
    gsap_start = t2.find('gsap.registerPlugin')
    gsap_end = t2.find('</script>', gsap_start) 
    gsap_js = t2[gsap_start:gsap_end]
    print(f"GSAP JS: {len(gsap_js)} chars")

    # === FROM test.html - extract the parts not in test2 ===

    # Mobile gallery HTML from test.html
    mob_start = test.find('<div class="mobile-gallery-section mobile-only">')
    mob_end_marker = test.find('        </div>\n\n        <div class="lp-wrapper">', mob_start)
    mobile_html = test[mob_start:mob_end_marker + len('        </div>')].strip()
    print(f"Mobile gallery: {len(mobile_html)} chars")

    # Bottom sections (Section 3, 4, 5) from test.html
    bottom_start = test.find('<div class="lp-wrapper">', mob_end_marker)
    bottom_end = test.find('        <script>', bottom_start)
    bottom_html = test[bottom_start:bottom_end].rstrip()
    print(f"Bottom sections: {len(bottom_html)} chars")

    # Mobile JS from test.html
    mob_js_start = test.find('// --- Mobile Gallery Logic ---')
    mob_js_end = test.find('</script>', mob_js_start)
    mobile_js = test[mob_js_start:mob_js_end]
    print(f"Mobile JS: {len(mobile_js)} chars")

    # === BUILD ===
    result = (
        head_section +
        '\n</head>\n\n<body>\n\n' +
        header_html + '\n\n' +
        first_lp_html + '\n\n' +
        mwg_html + '\n\n' +
        mobile_html + '\n\n' +
        bottom_html + '\n\n' +
        '<script>\n' +
        gsap_js + '\n\n' +
        mobile_js +
        '\n</script>\n\n</body>\n</html>\n'
    )

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(result)

    # Verify
    open_sections = result.count('<section')
    close_sections = result.count('</section>')
    print(f"\nSections: {open_sections} open, {close_sections} close")
    print(f"Has mwg_effect031: {'mwg_effect031' in result}")
    print(f"Has mobile gallery: {'mobile-gallery-section' in result}")
    print(f"Has bottom sections: {'לתפנו לבד לבנק' in result or 'Section 3' in result}")
    print(f"Total lines: {result.count(chr(10))}")
    print("DONE!")

if __name__ == '__main__':
    rebuild_properly()
