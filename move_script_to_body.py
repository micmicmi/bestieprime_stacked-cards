import re

def fix():
    with open('test2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the full script tag
    script_start = content.find('<script>')
    script_end = content.find('</script>', script_start) + 9  # +9 for len('</script>')
    
    if script_start == -1:
        print("No script found")
        return
    
    script_text = content[script_start:script_end]
    
    # Remove the script from where it is
    content = content[:script_start] + content[script_end:]
    
    # Place it just before </body>
    content = content.replace('</body>', script_text + '\n</body>')
    
    with open('test2.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Moved script to end of body")

if __name__ == '__main__':
    fix()
