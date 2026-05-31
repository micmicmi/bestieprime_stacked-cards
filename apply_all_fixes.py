import re

def apply_fixes():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Restore background: none !important for desktop cards
    css_fix = """        @media (min-width: 1024px) {
            .card-container {
                background: none !important;
                border-radius: 2.5rem;"""
    content = re.sub(
        r'@media \(min-width: 1024px\) \{\s*\.card-container \{\s*border-radius: 2\.5rem;',
        css_fix,
        content
    )

    # 2. Update CSS for the stack effect + pagination (550px height)
    css_pattern = r'/\* Stacking Section Container \*/.*?\.expertise-wrap \{'
    
    new_css = """/* Stacking Section Container */
        .mwg_effect031 {
            position: relative;
            width: 100%;
            max-width: 1400px;
            height: 550px;
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

        /* Pagination Styles */
        .expertise-pagination {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 12px;
            z-index: 100;
        }

        .expertise-pagination .dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background-color: #fca5a5;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.3s;
            padding: 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .expertise-pagination .dot:hover {
            background-color: #ef4444;
        }

        .expertise-pagination .dot.active {
            background-color: var(--primary-red, #ef4444);
            transform: scale(1.3);
        }

        .expertise-wrap {"""

    content = re.sub(css_pattern, new_css, content, flags=re.DOTALL)

    # 3. Inject Pagination HTML safely
    pagination_html = """
        <!-- Pagination Dots -->
        <div class="expertise-pagination">
            <button class="dot active" data-index="0" aria-label="Slide 1"></button>
            <button class="dot" data-index="1" aria-label="Slide 2"></button>
            <button class="dot" data-index="2" aria-label="Slide 3"></button>
            <button class="dot" data-index="3" aria-label="Slide 4"></button>
            <button class="dot" data-index="4" aria-label="Slide 5"></button>
        </div>
    </section>
    
    <div class="lp-wrapper">"""
    
    content = content.replace('    </section>\n\n    <div class="lp-wrapper">', pagination_html)

    # 4. Replace JS
    js_pattern = r'function initExpertiseScrollEffect\(\) \{.*?\}(?=\s*window\.addEventListener)'
    
    new_js = """function initExpertiseScrollEffect() {
            const section = document.querySelector('.mwg_effect031');
            const slides = gsap.utils.toArray('.mwg_effect031 .expertise-slide');
            const dots = document.querySelectorAll('.expertise-pagination .dot');
            
            // Set initial state
            slides.forEach((slide, i) => {
                // z-index: later slides should be on top of earlier ones!
                gsap.set(slide, { zIndex: i });
                
                if (i > 0) {
                    // Start off-screen at the bottom
                    gsap.set(slide, { y: '100%' });
                }
            });

            // Calculate total scroll distance based on number of slides
            const scrollDistance = slides.length * 550;

            const tl = gsap.timeline({
                scrollTrigger: {
                    trigger: section,
                    start: 'top top+=100', // Pin when section reaches header
                    end: `+=${scrollDistance}`, // Pin for this much scrolling
                    pin: true,
                    scrub: 1
                }
            });

            // Animate each transition
            slides.forEach((slide, index) => {
                if (index < slides.length - 1) {
                    const nextSlide = slides[index + 1];
                    const content = slide.querySelector('.expertise-content');
                    
                    // Create a label for this step
                    const stepLabel = 'step' + index;
                    tl.add(stepLabel);
                    
                    // The current slide folds backwards
                    tl.to(content, {
                        rotationZ: (Math.random() - 0.5) * 10,
                        scale: 0.7,
                        rotationX: 40,
                        ease: 'power1.in',
                        duration: 1
                    }, stepLabel);
                    
                    // The next slide moves up from 100% to 0%
                    tl.to(nextSlide, {
                        y: '0%',
                        ease: 'none',
                        duration: 1
                    }, stepLabel);

                    // The current slide fades out towards the end of the step
                    tl.to(content, {
                        autoAlpha: 0,
                        ease: 'power1.inOut',
                        duration: 0.25
                    }, stepLabel + "+=0.75");
                }
            });

            // Update dots on scroll
            tl.eventCallback("onUpdate", () => {
                const progress = tl.progress();
                const activeIndex = Math.round(progress * (slides.length - 1));
                dots.forEach((dot, i) => {
                    dot.classList.toggle('active', i === activeIndex);
                });
            });

            // Click dot to scroll
            dots.forEach((dot, i) => {
                dot.addEventListener('click', () => {
                    const st = tl.scrollTrigger;
                    if (st) {
                        const scrollPos = st.start + (st.end - st.start) * (i / (slides.length - 1));
                        gsap.to(window, { scrollTo: scrollPos, duration: 0.8, ease: 'power2.inOut' });
                    }
                });
            });
        }
"""
    content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done")

if __name__ == '__main__':
    apply_fixes()
