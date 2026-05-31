import re

css_to_add = """
        @media (max-width: 768px) {
            body { padding-top: 60px; }
            .header-inner { height: 60px; }
            .lp-container { width: 100%; padding: 0 20px; box-sizing: border-box; }
            
            .lp-hero { flex-direction: column; margin-top: 40px; margin-bottom: 40px; text-align: center; gap: 20px; }
            .lp-hero-content, .lp-hero-image { flex: 1 1 auto; width: 100%; }
            .lp-hero-image { justify-content: center; }
            .lp-hero h1 { font-size: 38px; margin-bottom: 20px; line-height: 1.1; }
            .lp-hero-subtitle { font-size: 16px; margin-bottom: 5px; }
            .lp-hero-checklist { margin-bottom: 30px; display: inline-block; text-align: right; }
            .lp-hero-checklist li { text-align: right; font-size: 16px; }
            
            .lp-banks-logos { flex-wrap: wrap; justify-content: center; gap: 15px; padding: 20px 0; }
            .lp-banks-logos img { height: 22px; }
            
            .lp-two-col { padding: 30px 0; }
            .lp-two-col-inner { flex-direction: column; gap: 20px; }
            .lp-two-col-right, .lp-two-col-left { flex: 1 1 auto; width: 100%; }
            .lp-two-col .subtitle { font-size: 20px; margin-bottom: 5px; }
            .lp-two-col h2 { font-size: 28px; line-height: 1.2; margin-bottom: 10px; }
            
            .comparison-section { flex-direction: column; gap: 30px; }
            .comparison-col { width: 100%; }
            
            .section-title { font-size: 32px; }
            
            div[style*="background:#F6F5FE"] { flex-direction: column; padding: 15px !important; }
        }
"""

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if css_to_add.strip() in content:
        print(f"{filename} already has this css.")
        return

    content = content.replace('</style>', css_to_add + '\n    </style>')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

process_file('test.html')
process_file('test2.html')

