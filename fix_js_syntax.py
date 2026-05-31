import re

def modify():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    js_start = content.find('function initExpertiseScrollEffect() {')
    js_end = content.find('</script>', js_start)

    if js_start == -1 or js_end == -1:
        print("Could not find JS block")
        return

    clean_js = """function initExpertiseScrollEffect() {
            const section = document.querySelector('.mwg_effect031');
            const slides = gsap.utils.toArray('.mwg_effect031 .expertise-slide');
            const dots = document.querySelectorAll('.card-pagination .dot');

            // Set initial state
            slides.forEach((slide, i) => {
                gsap.set(slide, { zIndex: i });

                const mediaSide = slide.querySelector('.card-media-side');
                const textSide = slide.querySelector('.card-text-side');

                if (i > 0) {
                    gsap.set(mediaSide, { y: '100vh' });
                    gsap.set(textSide, { autoAlpha: 0, y: 15 });
                } else {
                    gsap.set(mediaSide, { y: 0 });
                    gsap.set(textSide, { autoAlpha: 1, y: 0 });
                }
            });

            const scrollDistance = slides.length * 550;

            const tl = gsap.timeline({
                paused: true
            });

            slides.forEach((slide, index) => {
                if (index < slides.length - 1) {
                    const nextSlide = slides[index + 1];

                    const currentMedia = slide.querySelector('.card-media-side');
                    const nextMedia = nextSlide.querySelector('.card-media-side');
                    const currentText = slide.querySelector('.card-text-side');
                    const nextText = nextSlide.querySelector('.card-text-side');

                    const stepLabel = 'step' + index;
                    tl.add(stepLabel);

                    tl.to(currentMedia, {
                        rotationZ: (Math.random() - 0.5) * 10,
                        scale: 0.7,
                        rotationX: 40,
                        autoAlpha: 0,
                        ease: 'power1.in',
                        duration: 1
                    }, stepLabel);

                    tl.to(nextMedia, {
                        y: '0%',
                        ease: 'none',
                        duration: 1
                    }, stepLabel);

                    tl.to(currentText, {
                        autoAlpha: 0,
                        y: -15,
                        ease: 'power1.inOut',
                        duration: 0.5
                    }, stepLabel);

                    tl.to(nextText, {
                        autoAlpha: 1,
                        y: 0,
                        ease: 'power1.inOut',
                        duration: 0.5
                    }, stepLabel + "+=0.5");
                }
            });

            let isActive = false;
            let currentTargetProgress = 0;

            section.addEventListener('mouseenter', () => { isActive = true; });

            document.addEventListener('click', (e) => {
                if (!section.contains(e.target)) {
                    isActive = false;
                } else {
                    isActive = true;
                }
            });

            function updateDots() {
                const progress = tl.progress();
                const activeIndex = Math.round(progress * (slides.length - 1));
                dots.forEach((dot, i) => {
                    dot.classList.toggle('active', i === activeIndex);
                });
            }

            section.addEventListener('wheel', (e) => {
                if (!isActive || window.innerWidth < 1024) return;

                const progress = tl.progress();
                
                if (e.deltaY < 0 && progress <= 0) return;
                if (e.deltaY > 0 && progress >= 1) return;

                e.preventDefault();

                const deltaProgress = e.deltaY / scrollDistance;
                currentTargetProgress += deltaProgress;
                currentTargetProgress = Math.max(0, Math.min(1, currentTargetProgress));

                gsap.to(tl, {
                    progress: currentTargetProgress,
                    duration: 0.5,
                    ease: "power2.out",
                    onUpdate: updateDots
                });
            }, { passive: false });

            dots.forEach((dot, i) => {
                dot.addEventListener('click', () => {
                    if (window.innerWidth < 1024) return;

                    const targetProgress = i / (slides.length - 1);
                    currentTargetProgress = targetProgress;

                    gsap.to(tl, {
                        progress: targetProgress,
                        duration: 0.8,
                        ease: 'power2.inOut',
                        onUpdate: updateDots
                    });
                });
            });
        }

        window.addEventListener("load", () => {
            if ('requestIdleCallback' in window) {
                requestIdleCallback(initExpertiseScrollEffect);
            } else {
                setTimeout(initExpertiseScrollEffect, 500);
            }
        });
"""
    # Find the window.addEventListener at the end to know where to stop exactly.
    # Actually just replacing everything up to </script> is safest.
    content = content[:js_start] + clean_js + '    </script>' + content[js_end+9:]

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Fixed JS syntax")

if __name__ == '__main__':
    modify()
