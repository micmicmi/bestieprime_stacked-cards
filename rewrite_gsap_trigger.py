import re

def modify():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    js_pattern = r'const scrollDistance = slides\.length \* 550;.*?// Click dot to scroll'
    
    new_js = """const scrollDistance = slides.length * 550;

            const tl = gsap.timeline({
                paused: true // Manual scrubbing via wheel
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

                    // --- TEXT ANIMATION (Gentle Dissolve) ---
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

            // Handle manual scrubbing with mouse hover & click out
            let isActive = false;
            let currentTargetProgress = 0;

            // Hover activates
            section.addEventListener('mouseenter', () => {
                isActive = true;
            });

            // Click outside deactivates
            document.addEventListener('click', (e) => {
                if (!section.contains(e.target)) {
                    isActive = false;
                } else {
                    isActive = true; // Click inside ensures it's active
                }
            });

            section.addEventListener('wheel', (e) => {
                // Ignore if not active, or on mobile (let mobile gallery handle touch scroll)
                if (!isActive || window.innerWidth < 1024) return;

                const progress = tl.progress();
                
                // Allow scrolling page UP if at the start
                if (e.deltaY < 0 && progress <= 0) {
                    return; 
                }
                
                // Allow scrolling page DOWN if at the end
                if (e.deltaY > 0 && progress >= 1) {
                    return; 
                }

                // Trap scroll!
                e.preventDefault();

                // Calculate progress delta
                const deltaProgress = e.deltaY / scrollDistance;
                currentTargetProgress += deltaProgress;
                
                // Clamp between 0 and 1
                currentTargetProgress = Math.max(0, Math.min(1, currentTargetProgress));

                // Tween the timeline progress for smoothness
                gsap.to(tl, {
                    progress: currentTargetProgress,
                    duration: 0.5,
                    ease: "power2.out",
                    onUpdate: updateDots // call dot update function
                });
            }, { passive: false });

            // Update dots logic
            function updateDots() {
                const progress = tl.progress();
                const activeIndex = Math.round(progress * (slides.length - 1));
                dots.forEach((dot, i) => {
                    dot.classList.toggle('active', i === activeIndex);
                });
            }

            // Click dot to scroll"""
    
    content = re.sub(js_pattern, new_js, content, flags=re.DOTALL)

    # Now fix the click dot to scroll logic to update currentTargetProgress
    dot_click_pattern = r'dots\.forEach\(\(dot, i\) => \{.*?\}\);'
    
    new_dot_click = """dots.forEach((dot, i) => {
                dot.addEventListener('click', () => {
                    if (window.innerWidth < 1024) return;
                    
                    const targetProgress = i / (slides.length - 1);
                    currentTargetProgress = targetProgress; // sync the variable
                    
                    gsap.to(tl, { 
                        progress: targetProgress, 
                        duration: 0.8, 
                        ease: 'power2.inOut',
                        onUpdate: updateDots
                    });
                });
            });"""
    content = re.sub(dot_click_pattern, new_dot_click, content, flags=re.DOTALL)

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done rewriting GSAP logic for hover trigger")

if __name__ == '__main__':
    modify()
