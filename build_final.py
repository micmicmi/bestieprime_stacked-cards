"""
Build test2.html from scratch by combining:
- CSS from test2.html (has the stacking card CSS)
- Header HTML from test.html  
- First lp-wrapper (hero, banks, sections) from test.html
- mwg_effect031 section (5 stacking slides) - we'll rebuild this from test.html's content adapted
- mobile gallery from test.html
- bottom sections from test.html
- GSAP JS (hover-based) from test2.html's original JS logic
- Mobile gallery JS from test.html
"""

def build():
    with open('test.html', 'r', encoding='utf-8') as f:
        test = f.read()
    with open('test2.html', 'r', encoding='utf-8') as f:
        t2 = f.read()

    # === FROM test2.html ===
    # Extract CSS (everything in <style>...</style>)
    style_start = t2.find('<style>')
    style_end = t2.find('</style>') + len('</style>')
    css_block = t2[style_start:style_end]
    print(f"CSS: {len(css_block)} chars")

    # Extract the GSAP JS (hover-based scrubbing) from test2
    gsap_start = t2.find('gsap.registerPlugin')
    gsap_end = t2.find('</script>', gsap_start)
    gsap_js = t2[gsap_start:gsap_end].strip()
    print(f"GSAP JS: {len(gsap_js)} chars")

    # === FROM test.html ===
    # 1. Header HTML
    header_start = test.find('<header class="site-header">')
    header_end = test.find('</header>') + len('</header>')
    header_html = test[header_start:header_end]
    print(f"Header: {len(header_html)} chars")

    # 2. First lp-wrapper (hero + banks + 2 two-col sections)
    lp1_start = test.find('<div class="lp-wrapper">')
    cards_area_start = test.find('<section class="cards-area-wrapper">')
    lp1_end = test.rfind('</div>', lp1_start, cards_area_start) + 6
    lp1_html = test[lp1_start:lp1_end]
    print(f"First lp-wrapper: {len(lp1_html)} chars")

    # 3. Mobile gallery 
    mob_start = test.find('<div class="mobile-gallery-section mobile-only">')
    # Find the end: it's followed by two </div> closings and then lp-wrapper
    # Let's count divs
    pos = mob_start; depth = 0
    while True:
        no = test.find('<div', pos + 1)
        nc = test.find('</div>', pos + 1)
        if nc == -1: break
        if no != -1 and no < nc:
            depth += 1; pos = no
        else:
            if depth == 0:
                mob_end = nc + 6; break
            depth -= 1; pos = nc
    mobile_html = test[mob_start:mob_end].strip()
    print(f"Mobile gallery: {len(mobile_html)} chars")

    # 4. Bottom sections (Section 3, 4, 5)
    bottom_start = test.find('<div class="lp-wrapper">', mob_end)
    bottom_end = test.find('        <script>', bottom_start)
    bottom_html = test[bottom_start:bottom_end].rstrip()
    print(f"Bottom sections: {len(bottom_html)} chars, starts: {repr(bottom_html[:60])}")

    # 5. Mobile JS
    mob_js_start = test.find('// --- Mobile Gallery Logic ---')
    mob_js_end = test.find('</script>', mob_js_start)
    mobile_js = test[mob_js_start:mob_js_end].strip()
    print(f"Mobile JS: {len(mobile_js)} chars")

    # === BUILD mwg_effect031 from the slide data ===
    mwg_section = build_mwg_section()
    print(f"mwg section: {len(mwg_section)} chars")

    # === ASSEMBLE ===
    result = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bestie Prime - ייעוץ משכנתא</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;800;900&display=swap"
        rel="stylesheet">
    <!-- GSAP & Plugins -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollToPlugin.min.js"></script>
    {css_block}
</head>

<body>

{header_html}

{lp1_html}

{mwg_section}

{mobile_html}

{bottom_html}

<script>
{gsap_js}
</script>

</body>
</html>
"""

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(result)

    # Verify
    print(f"\nVerification:")
    print(f"  Has mwg_effect031: {'mwg_effect031' in result and '<section class=\"mwg_effect031\">' in result}")
    print(f"  Has expertise-slides: {result.count('expertise-slide desktop-only')}")
    print(f"  Has mobile gallery: {'mobile-gallery-section' in result}")
    print(f"  Has bottom sections (Section 3): {'Section 3' in result}")
    print(f"  Has GSAP hover JS: {'isActive' in result}")
    print(f"  sections open/close: {result.count('<section')} / {result.count('</section>')}")
    print(f"  Total lines: {result.count(chr(10))}")


def build_mwg_section():
    slides = [
        {
            'num': '01',
            'title': 'כמה הבית באמת עולה לכם?',
            'desc': 'הגדרת מחיר הנכס וההון העצמי הם הבסיס לכל התהליך. נתונים אלה מאפשרים לנו לחשב את אחוז המימון המדויק ולהבטיח שהמשכנתא שלכם עומדת בתקנות בנק ישראל ומותאמת ליכולות שלכם.',
            'video': './vid+gif/text.mp4',
            'img': './img/1.webp',
        },
        {
            'num': '02',
            'title': 'מה לגבי ההוצאות הנוספות?',
            'desc': 'עורך דין, שמאי, תיווך ומס רכישה – אלו עלויות שיכולות להגיע לעשרות אלפי שקלים. אנחנו מחשבים עבורכם את הכל מראש כדי שלא תופתעו ותדעו בדיוק כמה כסף נזיל אתם צריכים.',
            'video': './vid+gif/הוצאות נוספות.mp4',
            'img': './img/3.webp',
        },
        {
            'num': '03',
            'title': 'הפרופיל הפיננסי שלכם.',
            'desc': 'נתוני השכר והיציבות התעסוקתית הם המפתח לקבלת ריביות מעולות. ככל שהמידע שתזינו יהיה מדויק יותר, כך נוכל להילחם עבורכם על תנאים מנצחים מול הבנקים השונים.',
            'video': 'vid+gif\.mp4פרטי הלווים-1.mp4',
            'img': './img/3.webp',
        },
        {
            'num': '04',
            'title': 'כמה נוח לכם לשלם בחודש?',
            'desc': 'אנחנו מתאימים את המשכנתא לחיים שלכם, לא להיפך. הגדרת החזר חודשי ריאלי תבטיח שתעמדו בתשלומים בנוחות לאורך שנים ותשמרו על איכות החיים שאתם רגילים אליה.',
            'video': 'vid+gif/החזר חודשי_ארוך.mp4',
            'img': './img/1.webp',
        },
        {
            'num': '05',
            'title': 'המשכנתא המנצחת מוכנה!',
            'desc': 'המערכת מציגה לכם 2-3 תמהילים אופטימליים לבחירה: מאוזן, יציב או חסכוני. לכל אחד יתרונות משלו, כך שתוכלו לבחור בביטחון את המסלול שהכי נכון למשפחה שלכם.',
            'video': None,
            'img': './img/דף תוצאות_2.png',
        },
    ]

    dots = ''.join([f'<button class="dot{" active" if i==0 else ""}" data-index="{i}"></button>\n                                        ' for i in range(5)])

    slides_html = ''
    for i, slide in enumerate(slides):
        video_tag = f'<video src="{slide["video"]}" autoplay loop muted playsinline class="media-asset desktop-media"></video>' if slide['video'] else ''
        img_tag = f'<img src="{slide["img"]}" alt="Step {slide["num"]}" class="media-asset{" desktop-media" if not slide["video"] else " mobile-media"}">'
        
        # Hide all but the first slide text and media to prevent FOUC / overlap
        text_style = ' style="opacity:0; visibility:hidden; transform: translateY(15px);"' if i > 0 else ''
        media_style = ' style="transform: translateY(100vh);"' if i > 0 else ''

        slides_html += f"""
        <div class="expertise-slide desktop-only">
            <div class="expertise-wrap">
                <div class="expertise-content">
                    <div class="card-container">
                        <div class="card-text-side"{text_style}>
                            <h2 class="step-label">{slide['num']}</h2>
                            <h3 class="step-title">{slide['title']}</h3>
                            <p class="step-description">{slide['desc']}</p>
                        </div>
                        <div class="card-media-side"{media_style}>
                            {video_tag}
                            {img_tag}
                        </div>
                    </div>
                </div>
            </div>
        </div>
"""

    return f"""<section class="mwg_effect031">

        <!-- Pagination dots (desktop only) -->
        <div class="global-dots-wrapper desktop-only">
            <div class="card-container-dummy">
                <div class="card-text-side-dummy">
                    <div class="card-pagination">
                        {dots}
                    </div>
                </div>
            </div>
        </div>
{slides_html}
</section>"""


if __name__ == '__main__':
    build()
