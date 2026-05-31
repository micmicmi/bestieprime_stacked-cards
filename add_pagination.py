import re

def add_pagination():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. HTML Replace
    # Find the end of mwg_effect031 section
    pagination_html = """
        <!-- Pagination Dots -->
        <div class="expertise-pagination">
            <button class="dot active" data-index="0" aria-label="Slide 1"></button>
            <button class="dot" data-index="1" aria-label="Slide 2"></button>
            <button class="dot" data-index="2" aria-label="Slide 3"></button>
            <button class="dot" data-index="3" aria-label="Slide 4"></button>
            <button class="dot" data-index="4" aria-label="Slide 5"></button>
        </div>
    </section>"""
    
    content = content.replace('    </section>', pagination_html)

    # 2. CSS Replace
    pagination_css = """
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

        /* Helpers */"""
    
    content = content.replace('        /* Helpers */', pagination_css)

    # 3. JS Replace
    js_pattern = r'const tl = gsap\.timeline\(\{[^}]*\}\s*\}\);\s*'
    
    match = re.search(js_pattern, content, flags=re.DOTALL)
    if match:
        original_tl = match.group(0)
        new_js = original_tl + """
            const dots = document.querySelectorAll('.expertise-pagination .dot');
            
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

            """
        content = content.replace(original_tl, new_js)
    else:
        print("Could not find GSAP timeline definition in JS!")

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Done")

if __name__ == '__main__':
    add_pagination()
