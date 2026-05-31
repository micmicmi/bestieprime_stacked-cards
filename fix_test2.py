import sys

def fix_html():
    with open('test.html', 'r', encoding='utf-8') as f:
        content = f.read()

    new_html = """<section class="mwg_effect031">
        <!-- Step 01 -->
        <div class="expertise-slide">
            <div class="expertise-wrap">
                <div class="expertise-content">
                    <div class="card-container">
                        <div class="card-text-side">
                            <h2 class="step-label">01</h2>
                            <h3 class="step-title">כמה הבית באמת עולה לכם?</h3>
                            <p class="step-description">
                                הגדרת מחיר הנכס וההון העצמי היא הבסיס לכל התהליך. מאפשר לנו לחשב את אחוז המימון המדויק ולהבטיח שהמשכנתא שלכם עומדת בתקנות בנק ישראל.
                            </p>
                        </div>
                        <div class="card-media-side">
                            <video src="./vid+gif/text.mp4" autoplay loop muted playsinline class="media-asset desktop-media"></video>
                            <img src="./img/1.webp" alt="Step 1 Mobile" class="media-asset mobile-media">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Step 02 -->
        <div class="expertise-slide">
            <div class="expertise-wrap">
                <div class="expertise-content">
                    <div class="card-container">
                        <div class="card-text-side">
                            <h2 class="step-label">02</h2>
                            <h3 class="step-title">הוצאות הנוספות?</h3>
                            <p class="step-description">
                                עורך דין, שמאי, תיווך ומס רכישה – אלו עלויות שיכולות להגיע לעשרות אלפי שקלים. אנחנו מחשבים עבורכם את הכל מראש כדי שלא תופתעו ותדעו בדיוק כמה כסף נזיל אתם צריכים.
                            </p>
                        </div>
                        <div class="card-media-side">
                            <video src="./vid+gif/הוצאות נוספות.mp4" autoplay loop muted playsinline class="media-asset desktop-media"></video>
                            <img src="./img/3.webp" alt="Step 2 Mobile" class="media-asset mobile-media">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Step 03 -->
        <div class="expertise-slide">
            <div class="expertise-wrap">
                <div class="expertise-content">
                    <div class="card-container">
                        <div class="card-text-side">
                            <h2 class="step-label">03</h2>
                            <h3 class="step-title">הפרופיל הפיננסי שלכם.</h3>
                            <p class="step-description">
                                נתוני השכר והיציבות התעסוקתית הם המפתח לריביות מעולות. ככל שהמידע שתזינו יהיה מדויק יותר, כך נוכל להילחם עבורכם.
                            </p>
                        </div>
                        <div class="card-media-side">
                            <video src="vid+gif\\.mp4פרטי הלווים-1.mp4" autoplay loop muted playsinline class="media-asset desktop-media"></video>
                            <img src="./img/3.webp" alt="Step 3 Mobile" class="media-asset mobile-media">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Step 04 -->
        <div class="expertise-slide">
            <div class="expertise-wrap">
                <div class="expertise-content">
                    <div class="card-container">
                        <div class="card-text-side">
                            <h2 class="step-label">04</h2>
                            <h3 class="step-title">כמה נוח לכם לשלם בחודש?</h3>
                            <p class="step-description">
                                אנחנו מתאימים את המשכנתא לחיים שלכם. הגדרת החזר חודשי ריאלי תבטיח שתעמדו בתשלומים בנוחות ותשמרו על איכות החיים שלכם.
                            </p>
                        </div>
                        <div class="card-media-side">
                            <video src="./vid+gif/החזר חודשי_ארוך.mp4" autoplay loop muted playsinline class="media-asset desktop-media"></video>
                            <img src="./img/1.webp" alt="Step 4 Mobile" class="media-asset mobile-media">
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Step 05 -->
        <div class="expertise-slide">
            <div class="expertise-wrap">
                <div class="expertise-content">
                    <div class="card-container">
                        <div class="card-text-side">
                            <h2 class="step-label">05</h2>
                            <h3 class="step-title">המשכנתא המנצחת מוכנה!</h3>
                            <p class="step-description">
                                המערכת מציגה לכם 2-3 תמהילים אופטימליים לבחירה. כך תוכלו לבחור בביטחון את המסלול שהכי נכון למשפחה שלכם.
                            </p>
                        </div>
                        <div class="card-media-side">
                            <img src="./img/דף תוצאות_2.png" alt="Step 5 Desktop" class="media-asset desktop-media">
                            <img src="./img/2.webp" alt="Step 5 Mobile" class="media-asset mobile-media">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>\n\n    """
    
    import re

    # 1. CSS Replace using regex
    new_css = """/* Stacking Section Container */
        .mwg_effect031 {
            position: relative;
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 1400px;
            margin: 0 auto;
            padding-bottom: 700px; /* Gives the last card room to stay pinned */
            background-color: #F0F5F5;
        }

        /* Slide Styles */
        .expertise-slide {
            position: relative;
            width: 100%;
            height: 700px;
            max-height: 100vh;
        }

        .expertise-wrap {
            perspective: 1500px;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }

        .expertise-content {
            width: 100%;
            max-width: 1200px;
            padding: 0 1.5rem;
            will-change: transform, opacity;
            transform-origin: center center;
        }

        @media (min-width: 768px) {
            .expertise-content {
                padding: 0;
            }
        }

        @media (max-width: 1024px) {
            .expertise-wrap {
                align-items: flex-start;
                padding-top: 10vh;
            }
        }

        @media (max-width: 768px) {
            .expertise-wrap {
                padding-top: 5vh;
            }
        }

        /* Card Styles */
        .card-container {
            background: #f0f5f5e8;
            border-radius: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 24px;
            border: none;
            height: auto;
            overflow: visible;
            position: relative;
            box-shadow: none;
        }

        @media (min-width: 640px) {
            .card-container {
                border-radius: 2rem;
            }
        }

        @media (min-width: 1024px) {
            .card-container {
                background: none !important;
                border-radius: 2.5rem;
                padding: 0;
                flex-direction: row;
                justify-content: space-between;
                height: auto;
                width: 1140px;
            }
        }

        .card-text-side {
            width: 100%;
            text-align: right;
        }

        @media (min-width: 1024px) {
            .card-text-side {
                width: 50%;
                max-width: 420px;
            }
        }

        .step-label {
            color: var(--primary-red);
            font-size: 28px;
            font-weight: 900;
            line-height: 30px;
            margin-bottom: 8px;
            padding: 0;
            margin-top: 20px;
        }

        @media (min-width: 1024px) {
            .step-label {
                font-size: 36px;
                line-height: 40px;
                margin-bottom: 16px;
                padding: 0;
                margin-top: 0;
            }
        }

        .step-title {
            font-size: 26px;
            font-weight: 700;
            color: #333333;
            line-height: 26px;
            letter-spacing: 0.2px;
            margin-bottom: 12px;
            padding: 0;
            margin-top: 0;
        }

        @media (min-width: 1024px) {
            .step-title {
                font-size: 33px;
                line-height: 30px;
                letter-spacing: -0.2px;
                margin-bottom: 20px;
                padding: 0;
            }
        }

        .step-description {
            font-size: 17px;
            line-height: 26px;
            color: var(--text-muted);
            width: 100%;
            letter-spacing: 0.3px;
            margin: 0;
        }

        @media (min-width: 1024px) {
            .step-description {
                font-size: 18px;
                line-height: 1.6;
                max-width: 500px;
            }
        }

        .card-media-side {
            width: 100%;
            max-width: 630px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .media-asset {
            width: 100%;
            height: auto;
            display: block;
            border-radius: 10px;
            box-shadow: 0 4px 20px 4px rgba(147, 147, 147, 0.2);
            margin: 0 auto;
            image-rendering: high-quality;
            image-rendering: -webkit-optimize-contrast;
        }

        /* Desktop specific media */
        .desktop-media {
            display: none;
        }

        @media (min-width: 1024px) {
            .desktop-media {
                display: block;
            }
        }

        /* Mobile specific media */
        .mobile-media {
            display: block;
            box-shadow: none;
        }

        @media (min-width: 1024px) {
            .mobile-media {
                display: none;
            }
        }

        /* Helpers */
        .w-full {
            width: 100%;
        }

        .h-full {
            height: 100%;
        }

        """
    content = re.sub(
        r'/\* Split Layout Container \*/.*?/\* Landing Page Styles \*/',
        new_css + '/* Landing Page Styles */',
        content,
        flags=re.DOTALL
    )

    new_js = """gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

        function initExpertiseScrollEffect() {
            const slides = document.querySelectorAll('.mwg_effect031 .expertise-slide');

            slides.forEach((slide, index) => {
                const isLast = index === slides.length - 1;
                const contentWrapper = slide.querySelector('.expertise-wrap');
                const content = slide.querySelector('.expertise-content');
                // The pinning uses 700px explicitly
                const pinDuration = 700;

                if (!isLast) {
                    gsap.to(content, {
                        rotationZ: (Math.random() - 0.5) * 10,
                        scale: 0.7,
                        rotationX: 40,
                        ease: 'power1.in',
                        scrollTrigger: {
                            pin: contentWrapper,
                            trigger: slide,
                            start: 'top top+=100', // Offset from header
                            end: '+=' + pinDuration,
                            scrub: true
                        }
                    });

                    gsap.to(content, {
                        autoAlpha: 0,
                        ease: 'power1.inOut',
                        scrollTrigger: {
                            trigger: slide,
                            start: `top+=${pinDuration * 0.75} top+=100`,
                            end: `top+=${pinDuration} top+=100`,
                            scrub: true
                        }
                    });
                } else {
                    // Pin the last slide as well
                    ScrollTrigger.create({
                        pin: contentWrapper,
                        trigger: slide,
                        start: 'top top+=100',
                        end: '+=' + pinDuration
                    });
                }
            });
        }

        window.addEventListener("load", () => {
            if ('requestIdleCallback' in window) {
                requestIdleCallback(initExpertiseScrollEffect);
            } else {
                setTimeout(initExpertiseScrollEffect, 500);
            }
        });
    </script>"""

    content = re.sub(
        r'gsap\.registerPlugin\(ScrollTrigger, ScrollToPlugin\);.*?</script>',
        new_js,
        content,
        flags=re.DOTALL
    )

    start_idx = content.find('<section class="cards-area-wrapper">')
    
    # If not found, try div just in case
    if start_idx == -1:
        start_idx = content.find('<div class="cards-area-wrapper">')
    # We want to find the <!-- Section 3 --> that comes BEFORE the true <section class="lp-two-col"> text
    # Let's find "אל תפנו לבד לבנק" which is in Section 3
    anchor_idx = content.find('אל תפנו לבד לבנק')
    
    # Find the lp-wrapper right before this anchor
    end_idx = content.rfind('<div class="lp-wrapper">', 0, anchor_idx)
    
    if start_idx != -1 and end_idx != -1:
        content = content[:start_idx] + new_html + content[end_idx:]
    else:
        print(f"Could not find indices! start_idx: {start_idx}, end_idx: {end_idx}")
        return
        
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done replacing HTML")

if __name__ == '__main__':
    fix_html()
