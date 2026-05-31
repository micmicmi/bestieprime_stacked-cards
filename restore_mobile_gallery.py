import re

def main():
    with open('test.html', 'r', encoding='utf-8') as f:
        test_content = f.read()
    
    with open('test2.html', 'r', encoding='utf-8') as f:
        test2_content = f.read()

    # 1. Extract CSS
    css_start = test_content.find('/* Mobile Gallery Styles */')
    css_end = test_content.find('</style>')
    if css_start != -1 and css_end != -1:
        mobile_css = test_content[css_start:css_end]
        # remove it if it already exists in test2, then inject
        test2_content = re.sub(r'/\* Mobile Gallery Styles \*/.*?(?=</style>)', '', test2_content, flags=re.DOTALL)
        test2_content = test2_content.replace('</style>', mobile_css + '\n    </style>')

    # 2. Extract HTML
    html_start = test_content.find('<div class="mobile-gallery-section mobile-only">')
    if html_start != -1:
        # Find the end of the mobile gallery section. It ends before </section>
        # The easiest way is to search for '    </section>' after html_start
        html_end = test_content.find('    </section>', html_start)
        mobile_html = test_content[html_start:html_end]
        
        # Inject it into test2.html just before the closing </section> of mwg_effect031
        if '<div class="mobile-gallery-section mobile-only">' not in test2_content:
            test2_content = test2_content.replace('    </section>', '\n' + mobile_html + '\n    </section>')

    # 3. Extract JS
    js_start = test_content.find('function initMobileGallery()')
    if js_start != -1:
        # Find where the DOMContentLoaded listener starts
        js_end = test_content.find("document.addEventListener('DOMContentLoaded'", js_start)
        if js_end == -1: # fallback
             js_end = test_content.find("window.addEventListener('load'", js_start)
        mobile_js = test_content[js_start:js_end]
        
        # Inject into test2.html
        if 'function initMobileGallery()' not in test2_content:
            # Put it right before window.addEventListener('load'
            test2_content = test2_content.replace("        window.addEventListener('load', () => {", mobile_js + "\n        window.addEventListener('load', () => {\n            initMobileGallery();\n")

    # Add .desktop-only to mwg_effect031 if not there
    # Wait, mwg_effect031 is the section. If I add desktop-only to the section, it hides the mobile gallery which is INSIDE it!
    # Ah! The HTML for test2 has <section class="mwg_effect031">
    # The slides are <div class="expertise-slide">.
    # The dummy is <div class="global-dots-wrapper">.
    # I should wrap them in a .desktop-only div, OR add .desktop-only class to them!
    
    test2_content = test2_content.replace('<div class="global-dots-wrapper">', '<div class="global-dots-wrapper desktop-only">')
    test2_content = test2_content.replace('<div class="expertise-slide">', '<div class="expertise-slide desktop-only">')
    
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(test2_content)

    print("Mobile elements restored")

if __name__ == '__main__':
    main()
