import re

css_to_add = """
        @media (max-width: 768px) {
            .mobile-header-text .step-number {
                font-family: 'ploni', 'Heebo', sans-serif !important;
                font-size: 36px !important;
                color: #FF1D00 !important;
                font-weight: 700 !important;
                margin-bottom: 5px !important;
                opacity: 1 !important;
                display: block;
            }
        }
"""

for filename in ['test.html', 'test2.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "color: #FF1D00 !important;" not in content:
        content = content.replace('</style>', css_to_add + '\n    </style>')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
print('Added step-number CSS.')
