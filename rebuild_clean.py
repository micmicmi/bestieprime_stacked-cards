import re

def rebuild_clean():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Extract the script block (JS only, no tag)
    script_start = content.find('<script>')
    script_end_tag = content.find('</script>', script_start)
    js_code = content[script_start + len('<script>'):script_end_tag]

    # Step 2: Remove the old script entirely
    content = content[:script_start].rstrip() + content[script_end_tag + len('</script>'):]

    # Step 3: Now remove all the broken lp-wrapper / lp-container nesting that came after mwg_effect031
    # The mobile gallery section closes at some point, then there's broken nesting:
    # </div>\n\n        <div class="lp-wrapper"> ... 
    # This broken structure includes the duplicate lp-wrapper and all the extra sections
    
    # Let's find the mobile gallery end
    mobile_gallery_start = content.find('<div class="mobile-gallery-section mobile-only">')
    # Find its closing </div>
    # The mobile gallery section has nested divs. Count depth.
    pos = mobile_gallery_start
    depth = 0
    while pos < len(content):
        next_open = content.find('<div', pos + 1)
        next_close = content.find('</div>', pos + 1)
        if next_close == -1:
            break
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open
        else:
            if depth == 0:
                mobile_end = next_close + 6
                break
            depth -= 1
            pos = next_close

    # Content after mobile gallery should just be </body></html>
    # But right now it has broken lp-wrapper etc.
    # Find the real </body> tag
    body_close = content.rfind('</body>')
    html_close = content.rfind('</html>')
    
    after_mobile_current = content[mobile_end:body_close]
    print(f"Broken HTML after mobile gallery (first 300 chars): {repr(after_mobile_current[:300])}")
    
    # Rebuild: everything up to and including mobile gallery + clean close
    clean_content = content[:mobile_end] + '\n\n</body>\n</html>\n'

    # Now insert the script back before </body>
    clean_content = clean_content.replace('</body>', '<script>' + js_code + '</script>\n</body>')

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(clean_content)

    print("Done: removed broken HTML after mobile gallery, script inserted at end of body")

if __name__ == '__main__':
    rebuild_clean()
