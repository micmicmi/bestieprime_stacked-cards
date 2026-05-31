import re

# Read stacked_cards_split.html (the split view animation)
with open('stacked_cards_split.html', 'r', encoding='utf-8') as f:
    split_html = f.read()

head_match = re.search(r'(<style>.*?</style>)', split_html, re.DOTALL)
# Extract the body parts of stacked_cards_split.html
# Desktop wrapper
desktop_match = re.search(r'(<div class="main-wrapper desktop-only">.*?</div>\s*<!-- Desktop Only Spacer -->\s*<div class="desktop-only" style="height: 40vh;"></div>)', split_html, re.DOTALL)
# Mobile wrapper
mobile_match = re.search(r'(<div class="mobile-gallery-section mobile-only">.*?</div>)', split_html, re.DOTALL)
# Script
script_match = re.search(r'(<script>.*?</script>)', split_html, re.DOTALL)

original_styles = head_match.group(1) if head_match else ""
desktop_cards = desktop_match.group(1) if desktop_match else ""
mobile_cards = mobile_match.group(1) if mobile_match else ""
original_script = script_match.group(1) if script_match else ""

# Decrease height by 30%: replace 100vh with 70vh in original_styles
original_styles = original_styles.replace('height: 100vh;', 'height: 70vh;')
# But wait, there's also `.mobile-gallery-section { min-height: 100vh; }`
original_styles = original_styles.replace('min-height: 100vh;', 'min-height: 70vh;')

# We also need to add the landing page styles and layout
new_styles = """
        /* Landing Page Styles */
        .lp-wrapper {
            background-color: #ffffff;
            color: #333333;
            font-family: 'ploni', 'Heebo', sans-serif;
            text-align: right;
            direction: rtl;
        }
        .lp-container {
            max-width: 1140px;
            margin: 0 auto;
            padding: 0 20px;
        }
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
        .lp-hero {
            text-align: center;
            padding: 60px 0 40px;
        }
        .lp-hero h1 {
            font-size: clamp(32px, 5vw, 48px);
            font-weight: 900;
            color: #000;
            line-height: 1.2;
            margin-bottom: 24px;
        }
        .lp-hero h1 span {
            color: #FF1D00;
            font-weight: 400;
            font-size: 24px;
            display: block;
            margin-bottom: 10px;
        }
        .lp-hero p {
            font-size: 18px;
            max-width: 800px;
            margin: 0 auto;
        }
        
        .lp-banks {
            text-align: center;
            padding: 20px 0 60px;
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
            height: 30px;
            object-fit: contain;
        }
        
        .lp-two-col {
            padding: 60px 0;
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

        .checklist {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .checklist li {
            position: relative;
            padding-right: 25px;
            margin-bottom: 15px;
            font-size: 17px;
        }
        .checklist li::before {
            content: "•";
            color: #FF1D00;
            font-size: 24px;
            position: absolute;
            right: 0;
            top: -5px;
        }

        .comp-card {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            margin-bottom: 20px;
            flex: 1;
        }
        .comp-card h3 {
            text-align: center;
            font-size: 20px;
            margin-bottom: 20px;
        }
        .comp-card.highlight {
            border: 2px solid #FF1D00;
        }
        .comp-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .comp-list li {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        
        @media (max-width: 768px) {
            .lp-two-col-inner {
                flex-direction: column;
            }
            .lp-nav {
                display: none;
            }
        }
        
        .cards-area-wrapper {
            background-color: var(--bg-light);
            position: relative;
            z-index: 10;
        }
"""

top_html = """
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
                <h1><span>עזבו אתכם ממחשבונים ויועצים בתשלום, קבלו</span>יועץ משכנתא עם כוח מיקוח של 3 מיליארד ש"ח</h1>
                <p>המערכת שסורקת את כל מסלולי הריבית בישראל, מחשבת עבורך החזר חודשי ומראה לך איזה תמהיל משכנתא הכי מתאים לך - ובחינם!</p>
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
                        <h2>לקחת משכנתא<br>לא צריך להיות יקר ומסובך</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <p>
                            אנחנו יודעים שלקיחת משכנתא היא ההחלטה הכלכלית הגדולה בחייכם. שנים שהבנקים ויועצי המשכנתאות גרמו
                            לתהליך להיראות מורכב ומפחיד – וגבו על כך המון כסף.<br>ב-Bestie Prime החלטנו לשנות את חוקי המשחק.
                        </p>
                        <h3>מה תקבלו אצלנו בחינם?</h3>
                        <ul class="checklist">
                            <li><strong>בדיקת זכאות מיידית:</strong> כמה הבנק באמת יסכים לתת לכם?</li>
                            <li><strong>השוואת ריביות:</strong> מהם המסלולים והריביות שניתן לקבל כיום בישראל?</li>
                            <li><strong>תכנון תמהיל אופטימלי:</strong> בניית תוכנית מדויקת שתחסוך עשרות ומאות אלפי שקלים.</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- Section 2 -->
            <section class="lp-two-col">
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <h2>הגיע הזמן להתקדם לאסטרטגיית משכנתא מנצחת</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <div style="display:flex; gap:20px;">
                            <div class="comp-card">
                                <h3>מחשבוני משכנתא רגילים</h3>
                                <ul class="comp-list">
                                    <li><span>הערכה כללית</span><span style="color:#FF1D00">✗</span></li>
                                    <li><span>תמהיל גנרי</span><span style="color:#FF1D00">✗</span></li>
                                    <li><span>בלי כוח מיקוח מול הבנקים</span><span style="color:#FF1D00">✗</span></li>
                                </ul>
                            </div>
                            <div class="comp-card highlight">
                                <h3 style="color:#FF1D00">בסטי פריים חכם</h3>
                                <ul class="comp-list">
                                    <li><span>תמהיל מותאם אישית</span><span style="color:#10B981">✓</span></li>
                                    <li><span>ניתוח הכנסות וסיכון</span><span style="color:#10B981">✓</span></li>
                                    <li><span>כוח מיקוח אדיר</span><span style="color:#10B981">✓</span></li>
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
                        <p style="color:#666; margin-bottom:10px;">אל תפנו לבד לבנק</p>
                        <h2>תנו למומחים של בסטי-פריים להילחם עבורכם!</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <h3>איך מקבלים הצעה מנצחת?</h3>
                        <p>
                            משכנתא היא החלטה שמלווה אותנו שנים קדימה ומשפיעה על רמת החיים שלנו. זה השלב שבו יועצי המשכנתא נכנסים לתמונה.
                        </p>
                        <h3>בסטי-פריים: כוח מיקוח של 3 מיליארד ש"ח</h3>
                        <p>
                            בשיתוף פעולה עם "פריים משכנתאות", אתם מקבלים ליווי מצוות יועצי משכנתאות מומחים שחי ונושם את עולם 
                            המשכנתאות מאז 2006. בזכות הנפח המשמעותי מול הבנקים, אנו מנהלים עבורכם משא ומתן קשוח.
                        </p>
                        <ul class="checklist">
                            <li><strong>כוח מיקוח אדיר:</strong> מקבלים תנאים שהלקוח הפרטי יתקשה להשיג לבד</li>
                            <li><strong>אובייקטיביות מלאה:</strong> אנחנו בצד שלכם, לא של הבנק.</li>
                        </ul>
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
                            והיכולת להתמודד עם שינויים לאורך הדרך.
                        </p>
                        <p>
                            הבנקים רואים בגופים גדולים ומנוסים לקוחות חשובים, ומוכנים להציע תנאים וריביות טובים יותר מאשר בפנייה פרטית.
                        </p>
                    </div>
                </div>
            </section>
            
            <!-- Section 5 -->
            <section class="lp-two-col" style="border-top:1px solid #E5E7EB;">
                <div class="lp-two-col-inner">
                    <div class="lp-two-col-right">
                        <p style="color:#666; margin-bottom:10px;">איך בוחרים</p>
                        <h2>תמהיל משכנתא?</h2>
                    </div>
                    <div class="lp-two-col-left">
                        <p>
                            תמהיל משכנתא נכון יכול לחסוך לכם עשרות ולפעמים גם מאות אלפי שקלים.
                        </p>
                        <p>
                            בחירת התמהיל צריכה להתחיל בהבנה של מי אתם ואיך אתם מתנהלים כלכלית. יש מי שמעדיפים ודאות ויציבות ויש אחרים שמרגישים בנוח עם תנועה ושינויים. 
                            זה בדיוק הקטע של יועץ משכנתא מצוין.
                        </p>
                    </div>
                </div>
            </section>
        </div>
    </div>
"""

# Assemble final HTML
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

print("Updated test.html with original layout from image + split animation.")
