import re

def update_test2():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix CSS for .mwg_effect031 and .expertise-slide
    css_pattern = r'/\* Stacking Section Container \*/.*?\.expertise-wrap \{'
    
    new_css = """/* Stacking Section Container */
        .mwg_effect031 {
            position: relative;
            width: 100%;
            max-width: 1400px;
            height: 700px;
            max-height: 100vh;
            margin: 0 auto;
            background-color: #F0F5F5;
            overflow: hidden;
        }

        /* Slide Styles */
        .expertise-slide {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .expertise-wrap {"""

    content = re.sub(css_pattern, new_css, content, flags=re.DOTALL)

    # 2. Fix GSAP Script
    js_pattern = r'function initExpertiseScrollEffect\(\) \{.*?\}(?=\s*window\.addEventListener)'
    
    new_js = """function initExpertiseScrollEffect() {
            const section = document.querySelector('.mwg_effect031');
            const slides = gsap.utils.toArray('.mwg_effect031 .expertise-slide');
            
            // Stack slides in reverse order so slide 0 is on top
            slides.forEach((slide, i) => {
                gsap.set(slide, { zIndex: slides.length - i });
            });

            // Calculate total scroll distance based on number of slides
            const scrollDistance = slides.length * 600;

            const tl = gsap.timeline({
                scrollTrigger: {
                    trigger: section,
                    start: 'top top+=100', // Start when section reaches below header
                    end: `+=${scrollDistance}`, // Pin for this much scrolling
                    pin: true,
                    scrub: 1
                }
            });

            // Animate each slide except the last one to fold and fade away
            slides.forEach((slide, index) => {
                if (index < slides.length - 1) {
                    const content = slide.querySelector('.expertise-content');
                    
                    // Add to timeline
                    tl.to(content, {
                        rotationZ: (Math.random() - 0.5) * 10,
                        scale: 0.7,
                        rotationX: 40,
                        autoAlpha: 0,
                        ease: 'power1.inOut'
                    });
                }
            });
        }
"""

    content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done applying GSAP fix")

if __name__ == '__main__':
    update_test2()
