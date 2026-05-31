import re

def fix2():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Restore background: none !important
    css_fix = """        @media (min-width: 1024px) {
            .card-container {
                background: none !important;
                border-radius: 2.5rem;"""
    content = re.sub(
        r'@media \(min-width: 1024px\) \{\s*\.card-container \{\s*border-radius: 2\.5rem;',
        css_fix,
        content
    )

    # 2. JS replacement
    new_js = """function initExpertiseScrollEffect() {
            const section = document.querySelector('.mwg_effect031');
            const slides = gsap.utils.toArray('.mwg_effect031 .expertise-slide');
            
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
            const scrollDistance = slides.length * 600;

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
        }
"""
    content = re.sub(
        r'function initExpertiseScrollEffect\(\) \{.*?\}(?=\s*window\.addEventListener)',
        new_js,
        content,
        flags=re.DOTALL
    )

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done")

if __name__ == '__main__':
    fix2()
