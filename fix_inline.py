import re

def fix():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the mwg_effect031 section
    start_idx = content.find('<section class="mwg_effect031">')
    end_idx = content.find('</section>', start_idx)
    
    mwg_content = content[start_idx:end_idx]
    
    # Let's add inline styles to hide text and media for slides index 1 to 4
    # We can do this by finding all card-text-side and card-media-side in mwg_content
    # The first one is slide 0 (dummy from dots?), no wait dots use card-text-side-dummy
    # Slides have card-text-side and card-media-side.
    
    # We will just replace all card-text-side with a version that has inline style,
    # EXCEPT the first one.
    
    text_sides = [m.start() for m in re.finditer(r'<div class="card-text-side">', mwg_content)]
    media_sides = [m.start() for m in re.finditer(r'<div class="card-media-side">', mwg_content)]
    
    if len(text_sides) == 5:
        # We replace from the 2nd one
        new_mwg = mwg_content
        # Do it in reverse so indices don't shift
        for i in range(4, 0, -1):
            pos_t = text_sides[i]
            new_mwg = new_mwg[:pos_t] + '<div class="card-text-side" style="opacity:0; visibility:hidden; transform: translateY(15px);">' + new_mwg[pos_t+len('<div class="card-text-side">'):]
            
            pos_m = media_sides[i]
            new_mwg = new_mwg[:pos_m] + '<div class="card-media-side" style="transform: translateY(100vh);">' + new_mwg[pos_m+len('<div class="card-media-side">'):]
            
        content = content[:start_idx] + new_mwg + content[end_idx:]
        
        with open('test2.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Fixed inline styles for slides 2-5")
    else:
        print(f"Found {len(text_sides)} text sides, expected 5")

if __name__ == '__main__':
    fix()
