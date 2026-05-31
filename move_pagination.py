import re

def modify():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the old global pagination block
    old_html_pattern = r'<!-- Pagination Dots -->\s*<div class="expertise-pagination">.*?</section>'
    content = re.sub(old_html_pattern, '</section>', content, flags=re.DOTALL)

    # 2. Add the new card-level pagination into each card
    # We will find every `<div class="card-text-side">\s*<h2 class="step-label">(\d+)</h2>`
    # and replace it with the new HTML.
    
    def replacement(match):
        step_num = int(match.group(1))
        index = step_num - 1 # 0 to 4
        
        dots = ""
        for i in range(5):
            active_class = " active" if i == index else ""
            dots += f'\n                                <button class="dot{active_class}" data-index="{i}"></button>'
            
        return f"""<div class="card-text-side">
                            <div class="card-pagination">{dots}
                            </div>
                            <h2 class="step-label">{match.group(1)}</h2>"""

    content = re.sub(r'<div class="card-text-side">\s*<h2 class="step-label">(\d+)</h2>', replacement, content)

    # 3. Update CSS
    old_css_pattern = r'/\* Pagination Styles \*/.*?\.expertise-wrap \{'
    new_css = """/* Pagination Styles */
        .card-pagination {
            display: flex;
            gap: 8px;
            margin-bottom: 5px;
            margin-top: 15px;
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

        .expertise-wrap {"""
    
    content = re.sub(old_css_pattern, new_css, content, flags=re.DOTALL)

    # 4. Update JS
    # Remove the `onUpdate` listener, and update the click listener selector to `.card-pagination .dot`
    
    js_update_pattern = r'// Update dots on scroll.*?// Click dot to scroll'
    content = re.sub(js_update_pattern, '// Click dot to scroll', content, flags=re.DOTALL)

    js_selector_pattern = r"const dots = document\.querySelectorAll\('\.expertise-pagination \.dot'\);"
    content = content.replace(js_selector_pattern, "const dots = document.querySelectorAll('.card-pagination .dot');")

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done moving pagination")

if __name__ == '__main__':
    modify()
