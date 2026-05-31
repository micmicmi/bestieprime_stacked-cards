import re

with open('stacked_cards_split.html', 'r', encoding='utf-8') as f:
    split_html = f.read()

head_match = re.search(r'(<style>.*?</style>)', split_html, re.DOTALL)
desktop_match = re.search(r'(<div class="main-wrapper desktop-only">.*?</div>\s*<!-- Desktop Only Spacer -->\s*<div class="desktop-only" style="height: 40vh;"></div>)', split_html, re.DOTALL)
mobile_match_split = split_html.split('<div class="mobile-gallery-section mobile-only">')
if len(mobile_match_split) > 1:
    mobile_cards = '<div class="mobile-gallery-section mobile-only">' + mobile_match_split[1].split('<!-- Desktop View -->')[0]
else:
    mobile_cards = ""
script_match = re.search(r'(<script>.*?</script>)', split_html, re.DOTALL)

original_styles = head_match.group(1) if head_match else ""
desktop_cards = desktop_match.group(1) if desktop_match else ""
original_script = script_match.group(1) if script_match else ""

original_styles = original_styles.replace('height: 100vh;', 'height: 70vh;')
original_styles = original_styles.replace('min-height: 100vh;', 'min-height: 70vh;')
original_styles = original_styles.replace('background-color: var(--bg-light);', 'background-color: #ffffff;')

new_styles = """
        /* Landing Page Styles */
        body {
            background-color: #ffffff;
            margin: 0;
            padding: 0;
            font-family: 'ploni', 'Heebo', sans-serif;
            color: #000;
        }
        .lp-wrapper {
            background-color: #ffffff;
            text-align: right;
            direction: rtl;
        }
        .lp-container {
            width: 1180px;
            max-width: 100%;
            margin: 0 auto;
        }
        
        /* User Header Snippet Wrapper */
        .user-header-wrapper {
            display: flex;
            justify-content: center;
            padding: 20px 0;
            border-bottom: 1px solid #E5E3FF;
            margin-bottom: 50px;
        }

        /* Hero Section */
        .lp-hero {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
            margin-bottom: 80px;
        }
        .lp-hero-content {
            flex: 0 0 600px;
        }
        .lp-hero-image {
            flex: 0 0 500px;
            display: flex;
            justify-content: flex-end;
        }
        .lp-hero-image img {
            max-width: 100%;
            height: auto;
        }
        .lp-hero-subtitle {
            color: #FF1D00;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 10px;
        }
        .lp-hero h1 {
            font-size: 52px;
            font-weight: 900;
            color: #000;
            line-height: 1.1;
            margin-top: 0;
            margin-bottom: 30px;
            letter-spacing: -1px;
        }
        .lp-hero-checklist {
            list-style: none;
            padding: 0;
            margin: 0 0 40px 0;
        }
        .lp-hero-checklist li {
            position: relative;
            padding-right: 30px;
            margin-bottom: 15px;
            font-size: 18px;
            color: #555;
            line-height: 1.4;
        }
        .lp-hero-checklist li::before {
            content: "";
            position: absolute;
            right: 0;
            top: 4px;
            width: 18px;
            height: 18px;
            background-image: url('data:image/svg+xml;utf8,<svg width="18" height="18" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="10" cy="10" r="10" fill="%23FFEDEB"/><path d="M6 10.5L8.5 13L14 7" stroke="%23FF1D00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>');
            background-repeat: no-repeat;
        }
        .lp-btn-primary {
            background: #FF1D00;
            color: white;
            font-size: 20px;
            font-weight: 700;
            padding: 16px 50px;
            border-radius: 40px;
            text-decoration: none;
            display: inline-block;
            box-shadow: 0 8px 24px rgba(255, 29, 0, 0.25);
        }
        
        /* Banks */
        .lp-banks {
            text-align: center;
            padding: 0 0 80px;
        }
        .lp-banks-logos {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-top: 1px solid #E5E7EB;
            border-bottom: 1px solid #E5E7EB;
            padding: 30px 0;
            opacity: 0.6;
        }
        .lp-banks-logos img {
            height: 25px;
            object-fit: contain;
            filter: grayscale(100%);
        }
        
        .lp-two-col {
            padding: 50px 0;
        }
        .lp-two-col-inner {
            display: flex;
            gap: 120px;
            align-items: flex-start;
        }
        .lp-two-col-right {
            flex: 0 0 300px;
        }
        .lp-two-col-left {
            flex: 1;
        }
        .lp-two-col h2 {
            font-size: 32px;
            font-weight: 700;
            line-height: 1;
            margin: 0;
            letter-spacing: -0.5px;
        }
        .lp-two-col .subtitle {
            color: #000;
            font-size: 32px;
            font-weight: 400;
            line-height: 1;
            margin-bottom: 0;
        }
        .lp-two-col p {
            font-size: 18px;
            color: #444;
            line-height: 1.6;
            margin-top: 0;
            margin-bottom: 25px;
        }

        .checklist-red {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .checklist-red li {
            position: relative;
            padding-right: 20px;
            margin-bottom: 15px;
            font-size: 18px;
            color: #444;
        }
        .checklist-red li::before {
            content: "";
            position: absolute;
            right: 0;
            top: 8px;
            width: 6px;
            height: 6px;
            background-color: #FF1D00;
            border-radius: 50%;
        }

        .comparison-section {
            display: flex;
            gap: 60px;
            margin-top: 20px;
        }
        .comparison-col h4 {
            font-size: 18px;
            font-weight: 900;
            color: #000;
            margin-bottom: 15px;
        }
        .comparison-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .comparison-list li {
            position: relative;
            padding-right: 25px;
            margin-bottom: 15px;
            font-size: 16px;
            color: #555;
        }
        .comparison-list.bad li::before {
            content: "✗";
            position: absolute;
            right: 0;
            top: 0;
            color: #FF1D00;
            font-weight: bold;
        }
        .comparison-list.good li::before {
            content: "✓";
            position: absolute;
            right: 0;
            top: 0;
            color: #FF1D00; /* In the image, the checkmarks for Bestie Prime are also red! */
            font-weight: bold;
        }

        .cards-area-wrapper {
            background-color: #F0F5F5;
            position: relative;
            z-index: 10;
        }
"""

header_html = """
<div class="user-header-wrapper">
<div style="width: 1180px; height: 42px; position: relative">

  <div style="width: 108.51px; height: 30px; left: 3px; top: 0px; position: absolute">

    <div data-svg-wrapper style="left: 0px; top: 0px; position: absolute">

      <svg width="109" height="30" viewBox="0 0 109 30" fill="none" xmlns="http://www.w3.org/2000/svg">

      <path fill-rule="evenodd" clip-rule="evenodd" d="M81.9511 7.29409C84.1223 7.31948 85.9547 5.65476 85.9549 3.65711C85.9549 1.64559 84.1101 -0.0212749 81.908 0.000205311C79.767 0.0210997 77.9048 1.70554 77.9018 3.62391C77.8989 5.62489 79.7115 7.26773 81.9511 7.29409ZM101.731 16.7955C101.864 17.1143 101.732 17.1413 101.431 17.1397C100.341 17.1333 99.2496 17.1342 98.1587 17.135C97.7842 17.1353 97.4098 17.1356 97.0353 17.1356L95.7848 17.1359C94.7725 17.1361 93.76 17.1364 92.7477 17.135C92.1741 17.1343 92.1526 17.1091 92.3691 16.614C93.0728 15.0038 94.4261 14.1468 96.3094 13.97C97.5908 13.8497 98.8327 13.9786 99.9475 14.6519C100.827 15.1831 101.368 15.9204 101.731 16.7955ZM41.5849 16.731C41.734 17.0765 41.6356 17.1448 41.2563 17.1413C40.1863 17.1313 39.1159 17.1329 38.0457 17.1345C37.6503 17.135 37.255 17.1356 36.8597 17.1356C36.463 17.1356 36.0663 17.1348 35.6696 17.134C34.6189 17.1319 33.5681 17.1298 32.5177 17.1425C32.11 17.1473 32.0649 17.0431 32.1987 16.7234C32.8916 15.0677 34.2357 14.1598 36.1675 13.9716C37.4873 13.8431 38.7639 13.9808 39.8994 14.6953C40.7176 15.21 41.23 15.9083 41.5849 16.731ZM64.8612 17.8892C64.8616 18.6262 64.862 19.3632 64.8607 20.1003C64.8607 20.1226 64.8632 20.1457 64.8658 20.1693C64.8752 20.2544 64.8853 20.347 64.7787 20.4385C63.2716 18.0556 60.6275 17.351 57.9539 16.6951C57.8474 16.669 57.7408 16.6431 57.6342 16.6172C56.8852 16.4352 56.1364 16.2533 55.4158 15.9907C54.7125 15.7347 54.3768 15.3532 54.4329 14.9029C54.4956 14.3981 54.9421 14.0577 55.695 13.9372C57.0911 13.7136 58.2135 14.1216 58.9664 15.1903C59.2719 
<truncated 27683 bytes>
967 3.12109 16.0492 3.62812 16.9261 4.46475L17.1007 4.63684C18.2291 5.78781 18.8114 7.16051 18.8411 8.73993C18.8547 9.29038 18.8376 9.40594 18.7896 9.50255C18.6882 9.69469 18.4856 9.79298 18.2803 9.78987C18.1001 9.78681 17.9341 9.70634 17.8421 9.55843L17.8058 9.48868C17.766 9.39699 17.7338 9.19296 17.7305 8.98198C17.7094 7.65262 17.0886 6.14788 16.2076 5.2935C15.4191 4.52919 14.1797 4.01509 12.9316 3.91308L12.6814 3.89845C12.3251 3.88683 12.1152 3.85878 11.9796 3.80593C11.8891 3.77046 11.8298 3.72255 11.7808 3.64692L11.7346 3.56169C11.6467 3.37221 11.6579 3.20188 11.7318 3.07144C11.8068 2.9396 11.9573 2.82769 12.1853 2.78304L12.1872 2.78301ZM12.6422 5.6356C12.8782 5.63733 13.1353 5.65567 13.3082 5.68962L13.3101 5.69056C13.4861 5.72387 13.8392 5.84984 14.0919 5.96642L14.338 6.09148C14.4086 6.13111 14.4702 6.17115 14.5304 6.21446C14.6521 6.30195 14.7725 6.40955 14.9483 6.58002C15.4402 7.06158 15.7147 7.52681 15.8755 8.15649C15.9431 8.4237 15.9754 8.71254 15.974 8.9568C15.9733 9.07883 15.9643 9.18834 15.9478 9.27561C15.9393 9.31997 15.9292 9.35622 15.9192 9.38447L15.8889 9.44843C15.6533 9.7817 15.1452 9.75034 14.9424 9.37538C14.9424 9.37538 14.9413 9.37029 14.9382 9.36079C14.9351 9.35106 14.9309 9.33801 14.9269 9.3219C14.9188 9.28877 14.9105 9.245 14.9024 9.19532C14.8863 9.09562 14.8724 8.97219 14.8658 8.8521L14.8657 8.84917C14.8504 8.65053 14.8342 8.51229 14.8008 8.38431C14.767 8.25501 14.7158 8.14077 14.6363 7.98547C14.2787 7.28764 13.6334 6.83782 12.8844 6.75597L12.7338 6.74465C12.4558 6.73399 12.3227 6.72444 12.2341 6.70171C12.1595 6.68253 12.1147 6.65481 12.0172 6.57423L12.0182 6.57324C11.7354 6.33296 11.8086 5.82696 12.1603 5.67149C12.1791 5.66393 12.2337 5.65324 12.3269 5.64543C12.4153 5.63805 12.525 5.63476 12.6422 5.6356Z" fill="#4D45ED"/>

        </svg>

      </div>

    </div>

  </div>

</div>

הרקע הוא לבן. ורק באזור של הכרטיסיות הנגללות הוא אפור
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-05-31T17:32:48+03:00.
</ADDITIONAL_METADATA>
</div>
"""

top_html = header_html + """
    <div class="lp-wrapper">
        <div class="lp-container">

            <!-- Hero -->
            <section class="lp-hero">
                <div class="lp-hero-content">
                    <div class="lp-hero-subtitle">עזבו אתכם ממחשבונים ויועצים בתשלום, קבלו</div>
                    <h1>יועץ משכנתא עם כוח מיקוח של 3 מיליארד ש"ח</h1>
                    <ul class="lp-hero-checklist">
                        <li>המערכת שסורקת את כל מסלולי הריבית בישראל, מחשבת עבורך החזר חודשי ומראה לך איזה תמהיל משכנתא הכי מתאים לך - ובחינם!</li>
                        <li>חישוב כוח מיקוח אדיר של 3 מיליארד ש"ח מול הבנקים, כדי להבטיח את הריביות הכי נמוכות עבורך.</li>
                    </ul>
                    <a href="#" class="lp-btn-primary">יאללה, בואו נחסוך במשכנתא</a>
                </div>
                <div class="lp-hero-image">
                    <img src="./img/hero2.png" alt="Hero Illustration">
                </div>
            </section>
            
            <!-- Banks -->
            <section class="lp-banks">
                <div class="lp-banks-logos">
                    <span>בנק הפועלים</span>
                    <span>בנק לאומי</span>
                    <span>מזרחי טפחות</span>
                    <span>בנק דיסקונט</span>
                    <span>הבינלאומי</span>
                    <span>מרכנתיל</span>
                    <span>יהב</span>
                    <span>בנק ירושלים</span>
                </div>
            </section>

            <!-- Section 1 -->
            <section class="lp-two-col">
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <div class="subtitle">לקחת משכנתא</div>
                        <h2>לא צריך להיות יקר ומסובך</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <p>
                            אנחנו יודעים שלקיחת משכנתא היא ההחלטה הכלכלית הגדולה בחייכם. שנים שהבנקים ויועצי המשכנתאות גרמו
                            לתהליך להיראות מורכב ומפחיד – וגבו על כך המון כסף.<br>ב-Bestie Prime החלטנו לשנות את חוקי המשחק. הפכנו את כל הידע המקצועי לנגיש, ברור, וחינמי לגמרי.
                        </p>
                        <h3 style="color:#000; font-size:17px; margin-top:30px;">מה תקבלו אצלנו ב-<span style="color:#FF1D00; font-weight:700;">100% חינם?</span></h3>
                        <ul class="checklist-red">
                            <li><strong>בדיקת זכאות מיידית:</strong> כמה הבנק באמת יסכים לתת לכם?</li>
                            <li><strong>השוואת ריביות:</strong> מהם המסלולים והריביות שניתן לקבל כיום בישראל?</li>
                            <li><strong>תכנון תמהיל אופטימלי:</strong> בניית תוכנית משכנתא מדויקת ומותאמת אישית שתחסוך לכם עשרות ומאות אלפי שקלים.</li>
                            <li><strong>ייעוץ פרסונלי ומאובטח:</strong> בלי אותיות קטנות ובלי התחייבויות.</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Section 2 -->
            <section class="lp-two-col">
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <div class="subtitle">הגיע הזמן להתקדם</div>
                        <h2>לאסטרטגיית משכנתא מנצחת</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <p>
                            מחשבונים לא מכירים את ההכנסות שלכם, לא מנתחים את הסיכונים העתידיים ולא יודעים
                            להתמקח מול הבנק. אנחנו בונים לכם תמהיל אישי ומדויק שחוסך לכם עשרות אלפי שקלים-
                            באפס מאמץ ובחינם לגמרי.
                        </p>
                        
                        <div class="comparison-section">
                            <div class="comparison-col">
                                <h4>מחשבוני משכנתא רגילים</h4>
                                <ul class="comparison-list bad">
                                    <li>הערכה כללית</li>
                                    <li>תמהיל גנרי</li>
                                    <li>בלי כוח מיקוח מול הבנקים</li>
                                    <li>ניחושים שלא מתחשבים בכם</li>
                                </ul>
                            </div>
                            <div class="comparison-col">
                                <h4 style="color:#000">בסטי פריים - <span style="color:#FF1D00">יועץ משכנתא חכם</span></h4>
                                <ul class="comparison-list good">
                                    <li>תמהיל מותאם אישית</li>
                                    <li>ניתוח הכנסות ורמת סיכון</li>
                                    <li>כוח מיקוח מול הבנקים</li>
                                    <li>חינם לגמרי</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </div>
    </div>
"""

bottom_html = """
    <div class="lp-wrapper">
        <div class="lp-container">
            <!-- Section 3 -->
            <section class="lp-two-col">
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <div class="subtitle">אל תפנו לבד לבנק</div>
                        <h2>תנו למומחים של בסטי-פריים להילחם עבורכם!</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <h4 style="font-size:17px; margin:0 0 10px;">איך מקבלים הצעה מנצחת?</h4>
                        <p>
                            אז מצאתם בית במחיר שמתאים לכם ואתם מוכנים להתקדם. מה שנשאר עכשיו זה לסגור את
                            המשכנתא, או בשמה השני "ההתחייבות הכלכלית הכי גדולה שרובנו נעשה בחיים".
                            משכנתא היא החלטה שמלווה אותנו שנים קדימה ומשפיעה על רמת החיים שלנו. ובכל זאת,
                            לא מעט אנשים בוחרים מסלול משכנתא בלי להבין באמת איך הריביות, ההחזרים והמסלולים
                            באמת עובדים. זה השלב שבו יועצי המשכנתא נכנסים לתמונה.
                        </p>
                        <h4 style="font-size:17px; margin:20px 0 10px;">בסטי-פריים: כוח מיקוח של 3 מיליארד ש"ח - ניצחון מול כולם</h4>
                        <p>
                            בשיתוף פעולה עם "פריים משכנתאות", אתם מקבלים ליווי מצוות יועצי משכנתאות מומחים שחי ונושם את
                            עולם המשכנתאות מאז 2006. בזכות הנפח המשמעותי מול הבנקים, אנו מנהלים עבורכם משא ומתן קשוח ומשפרים ריביות.
                        </p>
                        <h4 style="font-size:17px; margin:20px 0 10px;">מה זה אומר עבורכם?</h4>
                        <ul class="checklist-red">
                            <li><strong>כוח מיקוח אדיר:</strong> גוף שמגלגל כ-3 מיליארד ש"ח מקבל תנאים שהלקוח הפרטי יתקשה להשיג לבד</li>
                            <li><strong>אובייקטיביות מלאה:</strong> אנחנו בצד שלכם, לא של הבנק.</li>
                            <li><strong>שקט נפשי:</strong> אנחנו מנהלים את המשא ומתן ומלווים אתכם יד ביד עד החתימה.</li>
                        </ul>
                        
                        <div style="background:#F9FAFB; padding:20px; border-radius:12px; margin-top:30px; display:flex; align-items:flex-start; gap:15px;">
                            <div style="color:#FF1D00;">✦</div>
                            <div style="font-size:16px;">
                                <strong style="color:#FF1D00;">בעמדה חזקה מול הבנקים - </strong>
                                עם כוח מיקוח של 3 מיליארד ש"ח, אנחנו לא מבקשים מהבנק תנאים - אנחנו די קובעים אותם. 
                                בכל מסלול שתבחרו, בסטי פריים תפעל להשיג לכם את הריביות הנמוכות ביותר האפשריות עבורכם!
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Section 4 -->
            <section class="lp-two-col" style="border-top:1px solid #E5E7EB;">
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <h2>מה עושים יועצי המשכנתא של בסטי פריים ולמה זה כל כך חשוב?</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <p>
                            יועצי המשכנתא המומחים שלנו יודע לבחון את המצב הכלכלי הנוכחי שלכם, את התזרים, התוכניות לעתיד
                            והיכולת להתמודד עם שינויים לאורך הדרך. המטרה היא לבנות משכנתא שאפשר לחיות איתה עכשיו וגם 
                            לתכנן איתה את העתיד.
                        </p>
                        <p>
                            עוד עניין שחשוב לקחת בחשבון - כשייעוץ המשכנתא נעשה דרך גוף גדול ומנוסה, היתרון גדל עוד יותר. 
                            הבנקים רואים בגופים כאלה לקוחות חשובים, ומוכנים להציע תנאים וריביות טובים יותר מאשר בפנייה פרטית.
                        </p>
                    </div>
                </div>
            </section>
            
            <!-- Section 5 -->
            <section class="lp-two-col" style="border-top:1px solid #E5E7EB;">
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <div class="subtitle">איך בוחרים</div>
                        <h2>תמהיל משכנתא?</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <h4 style="font-size:17px; margin:0 0 10px;">משכנתא תפורה בול עבורכם</h4>
                        <p>
                            תמהיל משכנתא נכון יכול לחסוך לכם עשרות ולפעמים גם מאות אלפי שקלים.
                            וכדי שהמספרים יסתדרו לטובתכם, בחירת התמהיל צריכה להתחיל בהבנה של מי אתם ואיך אתם מתנהלים
                            כלכלית. יש מי שמעדיפים ודאות ויציבות: תנו להם החזר חודשי קבוע. אחרים מרגישים בנוח עם
                            תנועה ושינויים.
                        </p>
                        <p>
                            וזה בדיוק הקטע של יועץ משכנתא מצוין - הוא לוקח בחשבון את האופי שלכם, רמת הסיכון שנוחה
                            לכם, והיכולת להתמודד עם שינויים. המטרה היא לתכנן משכנתא שתוכלו לחיות איתה לאורך זמן -
                            בביטחון, בלי לחץ מיותר, ועם תחושה שבחרתם נכון.
                        </p>
                    </div>
                </div>
            </section>
        </div>
    </div>
"""

final_head = original_styles.replace('</style>', new_styles + '</style>')
final_html = f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bestie Prime - ייעוץ משכנתא</title>
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;500;700;800;900&display=swap" rel="stylesheet">
    <!-- GSAP & Plugins -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollToPlugin.min.js"></script>
    {final_head}
</head>
<body>
{top_html}
<div class="cards-area-wrapper">
{desktop_cards}
{mobile_cards}
</div>
{bottom_html}
{original_script}
</body>
</html>
"""

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("test.html updated with EXACT layout, headers, hero positioning, typography, and lists from the user's Figma image.")
