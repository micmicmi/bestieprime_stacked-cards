import re

step_css = """
        .step-number {
            font-size: 56px;
            font-weight: 900;
            color: var(--primary-red);
            line-height: 0.8;
            margin-bottom: 1rem;
            opacity: 0.15;
            margin-bottom: 0;
        }

        @media (max-width: 768px) {
            .step-number {
                font-size: 36px;
                margin-bottom: 5px !important;
                opacity: 1;
                color: #FF1D00;
                font-family: 'ploni', 'Heebo', sans-serif;
            }
        }
"""

for target_file in ['test.html', 'test2.html']:
    with open(target_file, 'r', encoding='utf-8') as f:
        target_content = f.read()
        
    if '.step-number {' not in target_content:
        target_content = target_content.replace('</style>', step_css + '\n    </style>')
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(target_content)
        print(f"Added step-number CSS to {target_file}")
    else:
        print(f"step-number CSS already exists in {target_file}")
