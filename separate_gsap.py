import re

def modify():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    js_pattern = r'function initExpertiseScrollEffect\(\) \{.*?\}(?=\s*window\.addEventListener)'
    
    new_js = """function initExpertiseScrollEffect() {
            const section = document.querySelector('.mwg_effect031');
            const slides = gsap.utils.toArray('.mwg_effect031 .expertise-slide');
            const dots = document.querySelectorAll('.card-pagination .dot');
            
            // Set initial state
            slides.forEach((slide, i) => {
                // z-index: later slides should be on top of earlier ones!
                gsap.set(slide, { zIndex: i });
                
                const mediaSide = slide.querySelector('.card-media-side');
                const textSide = slide.querySelector('.card-text-side');

                if (i > 0) {
                    // Media starts off-screen at the bottom
                    gsap.set(mediaSide, { y: '100vh' });
                    // Text is hidden initially with a slight downward offset
                    gsap.set(textSide, { autoAlpha: 0, y: 15 });
                } else {
                    gsap.set(mediaSide, { y: 0 });
                    gsap.set(textSide, { autoAlpha: 1, y: 0 });
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
                    
                    const currentMedia = slide.querySelector('.card-media-side');
                    const nextMedia = nextSlide.querySelector('.card-media-side');
                    const currentText = slide.querySelector('.card-text-side');
                    const nextText = nextSlide.querySelector('.card-text-side');
                    
                    // Create a label for this step
                    const stepLabel = 'step' + index;
                    tl.add(stepLabel);
                    
                    // --- MEDIA ANIMATION (Stacking Fold) ---
                    // Current media folds backwards
                    tl.to(currentMedia, {
                        rotationZ: (Math.random() - 0.5) * 10,
                        scale: 0.7,
                        rotationX: 40,
                        autoAlpha: 0, // fade out towards the end
                        ease: 'power1.in',
                        duration: 1
                    }, stepLabel);
                    
                    // Next media moves up from off-screen
                    tl.to(nextMedia, {
                        y: '0%',
                        ease: 'none',
                        duration: 1
                    }, stepLabel);

                    // --- TEXT ANIMATION (Gentle Dissolve) ---
                    // Current text fades out and moves slightly up
                    tl.to(currentText, {
                        autoAlpha: 0,
                        y: -15,
                        ease: 'power1.inOut',
                        duration: 0.5
                    }, stepLabel);
                    
                    // Next text fades in and settles to 0
                    tl.to(nextText, {
                        autoAlpha: 1,
                        y: 0,
                        ease: 'power1.inOut',
                        duration: 0.5
                    }, stepLabel + "+=0.5");
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
        }"""
    
    content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done separating GSAP animations")

if __name__ == '__main__':
    modify()
