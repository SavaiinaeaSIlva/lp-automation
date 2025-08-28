import os
from bs4 import BeautifulSoup

WEBSITE_ROOT = '.'
# Add the filenames of the pages you want to update here
PAGES_TO_UPDATE = ['index.html', 'about.html', 'pricing.html', 'contact.html']

def refine_html_file(soup):
    """Finds the main section and headline to apply design refinements."""
    
    # Find the first <section> tag inside the <main> tag
    main_content = soup.find('main')
    if not main_content:
        return False

    first_section = main_content.find('section')
    if not first_section:
        return False

    print("    - Found main content section...")
    
    # 1. Increase vertical spacing/padding for the section
    # This replaces existing py- classes with more generous ones.
    section_classes = first_section.get('class', [])
    padding_classes = [c for c in section_classes if not c.startswith('py-')]
    padding_classes.extend(['py-24', 'md:py-36'])
    first_section['class'] = padding_classes

    # 2. Find the main headline (h1 or h2) and make it bolder/larger
    headline = first_section.find(['h1', 'h2'])
    if headline:
        print("    - Found main headline...")
        headline_classes = headline.get('class', [])
        # Remove old text size classes and add new, larger ones
        size_classes = [c for c in headline_classes if 'text-' not in c]
        size_classes.extend(['text-5xl', 'md:text-6xl', 'font-bold'])
        headline['class'] = size_classes
        
    return True

def process_files():
    """Walks through the website root and updates specified HTML files."""
    print("🚀 Starting design refinement process...")
    
    for filename in PAGES_TO_UPDATE:
        filepath = os.path.join(WEBSITE_ROOT, filename)
        if os.path.exists(filepath):
            print(f"--- Processing: {filepath}")
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    soup = BeautifulSoup(content, 'lxml')
                
                if refine_html_file(soup):
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(str(soup.prettify()))
                    print(f"    [SUCCESS] Design refined for {filename}")
                else:
                    print(f"    [INFO] No main section/headline found in {filename}")
            except Exception as e:
                print(f"    [ERROR] Could not process {filename}: {e}")
        else:
            print(f"    [WARNING] File not found, skipping: {filename}")

    print("\n🎉 Design refinement finished.")

if __name__ == "__main__":
    process_files()
