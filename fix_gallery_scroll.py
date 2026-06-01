import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_css = """        .mobile-gallery-container {
            width: 100%;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            display: flex;
            gap: 30px;
            scrollbar-width: none;
            -ms-overflow-style: none;
        }

        .mobile-gallery-container::-webkit-scrollbar {
            display: none;
        }

        .mobile-card-item {
            flex: 0 0 85%;
            scroll-snap-align: center;

        }

        .mobile-media-wrap {
            width: 100%;
            overflow: hidden;
            position: relative;
        }

        .mobile-media-wrap img,
        .mobile-media-wrap video {
            width: 100%;
            height: auto;
            display: block;
            image-rendering: high-quality;
        }"""

new_css = """        .mobile-gallery-container {
            width: 100%;
            overflow-x: auto;
            overflow-y: hidden;
            scroll-snap-type: x mandatory;
            display: flex;
            gap: 30px;
            scrollbar-width: none;
            -ms-overflow-style: none;
            flex: 1;
            min-height: 0;
            align-items: center;
        }

        .mobile-gallery-container::-webkit-scrollbar {
            display: none;
        }

        .mobile-card-item {
            flex: 0 0 85%;
            scroll-snap-align: center;
            height: 100%;
            display: flex;
            align-items: center;
        }

        .mobile-media-wrap {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }

        .mobile-media-wrap img,
        .mobile-media-wrap video {
            max-width: 100%;
            max-height: 100%;
            width: auto;
            height: auto;
            object-fit: contain;
            display: block;
            image-rendering: high-quality;
        }"""

if old_css in content:
    content = content.replace(old_css, new_css)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("CSS updated successfully!")
else:
    print("Could not find the old CSS block to replace.")
