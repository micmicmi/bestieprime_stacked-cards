import re

# Fix media queries in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('(min-width: 1025px)', '(min-width: 769px)')
content = content.replace('(max-width: 1024px)', '(max-width: 768px)')
content = content.replace('(min-width: 1024px)', '(min-width: 769px)')

# Fix mobile card images in index.html
# Card 4 should be 4.png instead of 3.webp
content = content.replace('<!-- Card 4 -->\n            <div class="mobile-card-item" data-index="3">\n                <div class="mobile-media-wrap">\n                    <img src="./img/3.webp" alt="">', '<!-- Card 4 -->\n            <div class="mobile-card-item" data-index="3">\n                <div class="mobile-media-wrap">\n                    <img src="./img/4.png" alt="">')
# Card 5 should be דף תוצאות_2.png instead of 3.webp
content = content.replace('<!-- Card 5 -->\n            <div class="mobile-card-item" data-index="4">\n                <div class="mobile-media-wrap" style="padding-left: 26px;">\n                    <img src="./img/3.webp" alt="">', '<!-- Card 5 -->\n            <div class="mobile-card-item" data-index="4">\n                <div class="mobile-media-wrap" style="padding-left: 26px;">\n                    <img src="./img/דף תוצאות_2.png" alt="">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)


# Fix video syntax in stacked_cards_split.html and stacked cards.html
for file in ['stacked_cards_split.html', 'stacked cards.html']:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()
            
        file_content = file_content.replace(r'vid+gif\.mp4פרטי הלווים-1.mp4', './vid+gif/פרטי הלווים.mp4')
        file_content = file_content.replace(r'vid+gif\.mp4פרטי הלווים-1', './vid+gif/פרטי הלווים')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(file_content)
    except Exception as e:
        print(f"Failed to process {file}: {e}")

print("Fixed media queries, mobile images, and video syntax errors.")
