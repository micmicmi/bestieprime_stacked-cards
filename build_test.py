import re

with open('stacked_cards_split.html', 'r', encoding='utf-8') as f:
    original_html = f.read()

# Separate head and body
head_match = re.search(r'(<head>.*?</head>)', original_html, re.DOTALL)
body_match = re.search(r'<body>(.*)</body>', original_html, re.DOTALL)

head = head_match.group(1) if head_match else ""
body = body_match.group(1) if body_match else ""

# The gray area is the body background which is already set in body { background-color: var(--bg-light); }
# But we want the top landing page to have a white background, so we will wrap the new content in a white container,
# and wrap the existing content in a gray container.

new_styles = """
    <style>
        .lp-wrapper {
            background-color: #ffffff;
            color: #333333;
            font-family: 'ploni', 'Heebo', sans-serif;
            text-align: right;
            direction: rtl;
        }
        
        /* Container */
        .lp-container {
            max-width: 1140px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Header */
        .lp-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            border-bottom: 1px solid #E5E3FF;
        }
        .lp-nav {
            display: flex;
            gap: 24px;
        }
        .lp-nav a {
            text-decoration: none;
            color: #626262;
            font-size: 16px;
            font-weight: 400;
        }
        .lp-header-contact {
            display: flex;
            align-items: center;
            gap: 16px;
        }
        .lp-header-contact .phone {
            font-size: 18px;
            font-weight: 700;
        }
        .lp-header-contact .btn {
            background: #FF1D00;
            color: white;
            padding: 10px 24px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 700;
        }
        
        /* Hero */
        .lp-hero {
            text-align: center;
            padding: 80px 0 60px;
        }
        .lp-hero h1 {
            font-size: clamp(32px, 5vw, 48px);
            font-weight: 300;
            color: #000;
            line-height: 1.2;
            margin-bottom: 24px;
        }
        .lp-hero h1 span {
            font-weight: 700;
        }
        .lp-hero p {
            font-size: 18px;
            max-width: 800px;
            margin: 0 auto 40px;
            line-height: 1.6;
        }
        .lp-benefits {
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap;
            text-align: right;
        }
        .lp-benefit-item {
            flex: 1;
            min-width: 200px;
            max-width: 250px;
        }
        .lp-benefit-item h4 {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 10px;
            color: #FF1D00;
        }
        .lp-benefit-item p {
            font-size: 15px;
            line-height: 1.4;
        }
        
        /* Comparison */
        .lp-comparison {
            padding: 60px 0;
            background: #F9FAFB;
        }
        .lp-comparison h2 {
            text-align: center;
            font-size: 36px;
            margin-bottom: 40px;
        }
        .lp-comp-grid {
            display: flex;
            gap: 30px;
            justify-content: center;
        }
        .lp-comp-card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            flex: 1;
            max-width: 450px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        }
        .lp-comp-card.highlight {
            border: 2px solid #FF1D00;
            box-shadow: 0 15px 40px rgba(255,29,0,0.1);
        }
        .lp-comp-card h3 {
            font-size: 24px;
            margin-bottom: 30px;
            text-align: center;
        }
        .lp-comp-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .lp-comp-list li {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
            border-bottom: 1px solid #eee;
            font-size: 17px;
        }
        .lp-comp-list li:last-child {
            border-bottom: none;
        }
        
        /* Two Col Text */
        .lp-two-col {
            padding: 80px 0;
        }
        .lp-two-col-inner {
            display: flex;
            gap: 60px;
            align-items: flex-start;
        }
        .lp-two-col-right {
            flex: 1;
        }
        .lp-two-col-left {
            flex: 1.5;
        }
        .lp-two-col h2 {
            font-size: 36px;
            line-height: 1.2;
            margin-bottom: 20px;
        }
        .lp-two-col h3 {
            font-size: 20px;
            font-weight: 700;
            margin: 30px 0 15px;
        }
        .lp-two-col p {
            font-size: 17px;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        
        /* Banner */
        .lp-banner {
            background: #F6F5FE;
            padding: 30px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            gap: 20px;
            margin: 40px 0;
        }
        .lp-banner p {
            font-size: 18px;
            margin: 0;
            flex: 1;
        }
        .lp-banner-icon {
            width: 50px;
            height: 50px;
            background: #FF1D00;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        /* Banks */
        .lp-banks {
            text-align: center;
            padding: 40px 0 80px;
        }
        .lp-banks h3 {
            font-size: 20px;
            margin-bottom: 30px;
        }
        .lp-banks-logos {
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap;
            align-items: center;
            opacity: 0.7;
        }
        .lp-banks-logos img {
            height: 40px;
            object-fit: contain;
        }
        
        @media (max-width: 768px) {
            .lp-nav {
                display: none;
            }
            .lp-comp-grid {
                flex-direction: column;
            }
            .lp-two-col-inner {
                flex-direction: column;
            }
            .lp-header {
                flex-direction: column;
                gap: 20px;
            }
        }
        
        /* Ensure the stacked cards gray section remains separate */
        .cards-area-wrapper {
            background-color: var(--bg-light);
            position: relative;
            z-index: 10;
        }
    </style>
"""

new_html = f"""
    <div class="lp-wrapper">
        <div class="lp-container">
            <!-- Header -->
            <header class="lp-header">
                <div class="lp-header-logo">
                    <img src="./img/embedded_0.png" alt="Bestie Prime" style="height:40px">
                </div>
                <nav class="lp-nav">
                    <a href="#">דף הבית</a>
                    <a href="#">השוואת ביטוחים</a>
                    <a href="#">ייעוץ משכנתא</a>
                    <a href="#">אודות</a>
                    <a href="#">מגזין</a>
                </nav>
                <div class="lp-header-contact">
                    <span class="phone">052-4576588</span>
                    <a href="#" class="btn">לתיאום פגישת ייעוץ חינם</a>
                </div>
            </header>

            <!-- Hero -->
            <section class="lp-hero">
                <h1>לקחת משכנתא<br><span>לא צריך להיות יקר ומסובך</span></h1>
                <p>
                    אנחנו יודעים שלקיחת משכנתא היא ההחלטה הכלכלית הגדולה בחייכם. שנים שהבנקים ויועצי המשכנתאות גרמו
                    לתהליך להיראות מורכב ומפחיד – וגבו על כך המון כסף.
                    <br>ב-Bestie Prime החלטנו לשנות את חוקי המשחק. הפכנו את כל הידע המקצועי לנגיש, ברור, וחינמי לגמרי.
                </p>
                <h3 style="margin-bottom:30px">מה תקבלו אצלנו ב-100% חינם?</h3>
                <div class="lp-benefits">
                    <div class="lp-benefit-item">
                        <h4>בדיקת זכאות מיידית</h4>
                        <p>כמה הבנק באמת יסכים לתת לכם?</p>
                    </div>
                    <div class="lp-benefit-item">
                        <h4>השוואת ריביות</h4>
                        <p>מהם המסלולים והריביות שניתן לקבל כיום בישראל?</p>
                    </div>
                    <div class="lp-benefit-item">
                        <h4>תכנון תמהיל אופטימלי</h4>
                        <p>בניית תוכנית משכנתא מדויקת ומותאמת אישית שתחסוך לכם עשרות ומאות אלפי שקלים.</p>
                    </div>
                    <div class="lp-benefit-item">
                        <h4>ייעוץ פרסונלי ומאובטח</h4>
                        <p>בלי אותיות קטנות ובלי התחייבות.</p>
                    </div>
                </div>
                <div style="margin-top: 40px; background: #FFF9F9; padding: 20px; border-radius: 12px; display:inline-block; max-width:800px; text-align:right;">
                    <h4 style="color: #FF1D00; margin-bottom:10px;">אז על מה כן משלמים?</h4>
                    <p style="margin:0; font-size:16px;">
                        רק אם תבחרו שנלווה אתכם פיזית "עד הבית", ננהל עבורכם את כל הבירוקרטיה מול הבנקים ונוודא שתקבלו
                        את הריביות הטובות ביותר עבורכם. נבקש תשלום הגון, שקוף ותחרותי. הכוח עובר לידיים שלכם. בואו נתחיל
                        לבנות את העתיד שלכם.
                    </p>
                </div>
            </section>
        </div>

        <!-- Comparison -->
        <section class="lp-comparison">
            <div class="lp-container">
                <p style="text-align:center; max-width:800px; margin: 0 auto 40px; font-size:18px;">
                    מחשבונים לא מכירים את ההכנסות שלכם, לא מנתחים את הסיכונים העתידיים ולא יודעים להתמקח מול הבנק. אנחנו
                    בונים לכם תמהיל אישי ומדויק שחוסך לכם עשרות אלפי שקלים- באפס מאמץ ובחינם לגמרי.
                </p>
                <div class="lp-comp-grid">
                    <div class="lp-comp-card">
                        <h3>מחשבוני משכנתא רגילים</h3>
                        <ul class="lp-comp-list">
                            <li><span>הערכה כללית</span> <span style="color:#FF1D00">✗</span></li>
                            <li><span>תמהיל גנרי</span> <span style="color:#FF1D00">✗</span></li>
                            <li><span>בלי כוח מיקוח מול הבנקים</span> <span style="color:#FF1D00">✗</span></li>
                            <li><span>ניחושים שלא מתחשבים בכם</span> <span style="color:#FF1D00">✗</span></li>
                        </ul>
                    </div>
                    <div class="lp-comp-card highlight">
                        <h3 style="color:#FF1D00">בסטי פריים - יועץ חכם</h3>
                        <ul class="lp-comp-list">
                            <li><span>תמהיל מותאם אישית</span> <span style="color:#10B981">✓</span></li>
                            <li><span>ניתוח הכנסות ורמת סיכון</span> <span style="color:#10B981">✓</span></li>
                            <li><span>כוח מיקוח מול הבנקים</span> <span style="color:#10B981">✓</span></li>
                            <li><span>חינם לגמרי</span> <span style="color:#10B981">✓</span></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- Two Col Text 1 -->
        <section class="lp-two-col">
            <div class="lp-container">
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <h2>הגיע הזמן להתקדם<br><span>לאסטרטגיית משכנתא מנצחת</span></h2>
                        <p style="font-size:24px; font-weight:700; margin-top:40px;">
                            אל תפנו לבד לבנק.<br>תנו למומחים של בסטי-פריים להילחם עבורכם!
                        </p>
                    </div>
                    <div class="lp-two-col-left">
                        <h3>איך מקבלים הצעה מנצחת?</h3>
                        <p>
                            אז מצאתם בית במחיר שמתאים לכם ואתם מוכנים להתקדם. מה שנשאר עכשיו זה לסגור את המשכנתא, או בשמה
                            השני "ההתחייבות הכלכלית הכי גדולה שרובנו נעשה בחיים".
                        </p>
                        <p>
                            משכנתא היא החלטה שמלווה אותנו שנים קדימה ומשפיעה על רמת החיים שלנו. ובכל זאת, לא מעט אנשים 
                            בוחרים מסלול משכנתא בלי להבין באמת איך הריביות, ההחזרים והמסלולים באמת עובדים. 
                            זה השלב שבו יועצי המשכנתא נכנסים לתמונה.
                        </p>
                        <h3>בסטי-פריים: כוח מיקוח של 3 מיליארד ש"ח</h3>
                        <p>
                            בשיתוף פעולה עם "פריים משכנתאות", אתם מקבלים ליווי מצוות יועצי משכנתאות מומחים שחי ונושם את עולם 
                            המשכנתאות מאז 2006. בזכות הנפח המשמעותי מול הבנקים וההיכרות העמוקה עם "מאחורי הקלעים", אנו מנהלים 
                            עבורכם משא ומתן קשוח ומשפרים ריביות.
                        </p>
                        <h3>מה זה אומר עבורכם?</h3>
                        <ul style="padding-right:20px; line-height:1.8; font-size:17px;">
                            <li><strong>כוח מיקוח אדיר:</strong> גוף שמגלגל כ-3 מיליארד ש"ח בשנה מקבל תנאים שהלקוח הפרטי יתקשה להשיג לבד</li>
                            <li><strong>אובייקטיביות מלאה:</strong> אנחנו בצד שלכם, לא של הבנק.</li>
                            <li><strong>שקט נפשי:</strong> אנחנו מנהלים את המשא ומתן ומלווים אתכם יד ביד עד החתימה.</li>
                        </ul>
                    </div>
                </div>

                <div class="lp-banner">
                    <p>
                        <strong>בעמדה חזקה מול הבנקים - </strong>
                        עם כוח מיקוח של 3 מיליארד ש"ח, אנחנו לא מבקשים מהבנק תנאים – אנחנו די קובעים אותם. 
                        בכל מסלול שתבחרו, בסטי פריים תפעל להשיג לכם את הריביות הנמוכות ביותר האפשריות עבורכם!
                    </p>
                </div>
            </div>
        </section>

        <!-- Two Col Text 2 -->
        <section class="lp-two-col" style="background: #F9FAFB;">
            <div class="lp-container">
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
                
                <hr style="border:0; border-top:1px solid #E5E7EB; margin:60px 0;">
                
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <h2>איך בוחרים תמהיל משכנתא?</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <h3>משכנתא תפורה בול עבורכם</h3>
                        <p>
                            תמהיל משכנתא נכון יכול לחסוך לכם עשרות ולפעמים גם מאות אלפי שקלים.
                        </p>
                        <p>
                            וכדי שהמספרים יסתדרו לטובתכם, בחירת התמהיל צריכה להתחיל בהבנה של מי אתם ואיך אתם מתנהלים
                            כלכלית. יש מי שמעדיפים ודאות ויציבות: תנו להם החזר חודשי קבוע. אחרים מרגישים בנוח עם 
                            תנועה ושינויים.
                        </p>
                        <p>
                            וזה בדיוק הקטע של יועץ משכנתא מצוין - הוא לוקח בחשבון את האופי שלכם, רמת הסיכון שנוחה לכם,
                            והיכולת להתמודד עם שינויים. המטרה היא לתכנן משכנתא שתוכלו לחיות איתה לאורך זמן - בביטחון, 
                            בלי לחץ מיותר, ועם תחושה שבחרתם נכון.
                        </p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Banks -->
        <section class="lp-banks">
            <div class="lp-container">
                <h3>בסטי-פריים משווה ריביות מול כל הבנקים</h3>
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
            </div>
        </section>
        
        <!-- Intro to Cards -->
        <div style="text-align:center; padding: 60px 0 20px;">
            <h2 style="font-size:36px; margin-bottom:10px;">יועץ משכנתא עם כוח מיקוח של 3 מיליארד ש”ח</h2>
            <p style="font-size:20px; color:#666; max-width:600px; margin: 0 auto;">עזבו אתכם ממחשבונים ומיועצים בתשלום, המערכת שלנו סורקת את כל המסלולים ומתאימה לך אישית תמהיל משכנתא!</p>
        </div>
    </div>
"""

# Rebuild the final HTML
final_head = head.replace('</style>', new_styles + '</style>')
final_html = f"<!DOCTYPE html>\n<html lang=\"he\" dir=\"rtl\">\n{final_head}\n<body>\n{new_html}\n<div class=\"cards-area-wrapper\">\n{body}\n</div>\n</body>\n</html>"

with open('test.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("test.html created successfully.")
