import re

def modify():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the duplicated card-pagination from inside the cards
    content = re.sub(r'<div class="card-pagination">.*?</div>', '', content, flags=re.DOTALL)

    # 2. Add the global dummy overlay for dots
    overlay_html = """
    <!-- Global Fixed Pagination -->
    <div class="global-dots-wrapper">
        <div class="card-container-dummy">
            <div class="card-text-side-dummy">
                <div class="card-pagination">
                    <button class="dot active" data-index="0"></button>
                    <button class="dot" data-index="1"></button>
                    <button class="dot" data-index="2"></button>
                    <button class="dot" data-index="3"></button>
                    <button class="dot" data-index="4"></button>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Step 01 -->"""
    
    content = content.replace('<!-- Step 01 -->', overlay_html, 1)

    # 3. Add CSS for the dummy overlay
    css_pattern = r'/\* Pagination Styles \*/.*?\.expertise-wrap \{'
    new_css = """/* Pagination Styles */
        .global-dots-wrapper {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            pointer-events: none;
            z-index: 100;
        }
        
        .card-container-dummy {
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 100%; /* Match slide height */
            padding-top: 100px; /* Offset to place dots above the text */
        }
        
        .card-text-side-dummy {
            width: 100%;
            text-align: right;
            pointer-events: auto;
        }

        .card-pagination {
            display: flex;
            gap: 8px;
            justify-content: flex-start; /* align right in RTL */
        }

        .card-pagination .dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: #E2E8F0;
            border: none;
            cursor: pointer;
            padding: 0;
            transition: width 0.3s, background-color 0.3s;
        }

        .card-pagination .dot.active {
            width: 20px;
            border-radius: 8px;
            background-color: var(--primary-red, #FF1D00);
        }

        .card-pagination .dot:hover:not(.active) {
            background-color: #CBD5E1;
        }

        @media (min-width: 1024px) {
            .card-container-dummy {
                flex-direction: row;
                justify-content: space-between;
                max-width: 1140px;
                padding-top: 50px; /* adjust for desktop vertical centering */
                align-items: flex-start;
                margin-top: 60px; /* offset relative to the centered card-container */
            }
            .card-text-side-dummy {
                width: 50%;
                max-width: 420px;
            }
        }

        .expertise-wrap {"""
    
    content = re.sub(css_pattern, new_css, content, flags=re.DOTALL)

    # 4. Restore JS logic (since we removed the onUpdate earlier)
    js_update_pattern = r'// Click dot to scroll'
    js_update_replacement = """// Update dots on scroll
            tl.eventCallback("onUpdate", () => {
                const progress = tl.progress();
                const activeIndex = Math.round(progress * (slides.length - 1));
                dots.forEach((dot, i) => {
                    dot.classList.toggle('active', i === activeIndex);
                });
            });

            // Click dot to scroll"""
    content = content.replace(js_update_pattern, js_update_replacement)

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done fixing pagination overlay")

if __name__ == '__main__':
    modify()
