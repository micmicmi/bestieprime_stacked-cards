import re

def modify():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove padding-right from card-text-side-dummy
    content = re.sub(
        r'\.card-text-side-dummy\s*\{[^}]*\}',
        """.card-text-side-dummy {
            width: 100%;
            text-align: right;
            pointer-events: auto;
            position: relative;
        }""",
        content
    )

    # 2. Update card-pagination
    pagination_css = r'\.card-pagination\s*\{[^}]*\}'
    new_pagination_css = """.card-pagination {
            position: absolute;
            top: 25px; /* Offset it to sit right above the "01" */
            right: 0px; /* Align precisely with the right margin of the text */
            display: flex;
            flex-direction: row; /* Horizontal */
            gap: 8px;
            justify-content: flex-start; /* Right aligned in RTL */
        }"""
    content = re.sub(pagination_css, new_pagination_css, content)

    # 3. Update active dot to pill
    active_dot_css = r'\.card-pagination \.dot\.active\s*\{[^}]*\}'
    new_active_dot_css = """.card-pagination .dot.active {
            width: 20px;
            height: 8px;
            border-radius: 8px;
            background-color: var(--primary-red, #FF1D00);
        }"""
    content = re.sub(active_dot_css, new_active_dot_css, content)

    # 4. Remove scale from normal dot transition and set color to light gray
    dot_css = r'\.card-pagination \.dot\s*\{[^}]*\}'
    new_dot_css = """.card-pagination .dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: #DADEE3; /* Light gray */
            border: none;
            cursor: pointer;
            padding: 0;
            transition: width 0.3s, background-color 0.3s;
        }"""
    content = re.sub(dot_css, new_dot_css, content)

    # 5. Remove padding-right from card-text-side
    content = re.sub(
        r'\.card-text-side\s*\{([^}]*?)padding-right:\s*40px;([^}]*)\}',
        r'.card-text-side {\1\2}',
        content
    )

    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print("Done rotating dots to horizontal pill format")

if __name__ == '__main__':
    modify()
