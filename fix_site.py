import os
from bs4 import BeautifulSoup

def ensure_hero_image_exists(file_path, image_src, alt_text, caption_text):
    """
    Checks a blog post file and adds a hero image figure if it's missing.
    This ensures the structure is correct before renaming.
    """
    print(f"\n--- Checking for hero image in: {file_path} ---")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        article = soup.find('article')
        if not article:
            print(f"  - ERROR: Cannot find <article> tag in {file_path}.")
            return False

        if article.find('figure'):
            print(f"  - Hero image structure already exists. OK.")
            return True

        print(f"  - FIXING: Hero image structure is missing. Adding it now...")
        
        # Create the new <figure> element
        figure_tag = soup.new_tag('figure')
        img_tag = soup.new_tag('img', src=image_src, alt=alt_text, attrs={'class': 'w-full aspect-video object-cover rounded-lg shadow-lg mb-8'})
        figcaption_tag = soup.new_tag('figcaption', attrs={'class': 'text-center text-sm text-gray-500 mt-2'})
        figcaption_tag.string = caption_text
        
        figure_tag.append(img_tag)
        figure_tag.append(figcaption_tag)
        
        # Insert the new figure at the beginning of the article
        article.insert(0, figure_tag)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        print(f"  - SUCCESS: Added missing hero image to {file_path}.")
        return True

    except Exception as e:
        print(f"  - ERROR: An unexpected error occurred in ensure_hero_image_exists: {e}")
        return False

def update_all_image_paths():
    """
    Systematically updates all placeholder blog images to their correct,
    final filenames across all relevant HTML files.
    """
    print("\n--- Updating all image paths to final filenames ---")

    image_mapping = {
        'blog1.html': 'assets/images/blog1.png',
        'blog2.html': 'assets/images/blog2.png',
        # Adding old filenames for robustness, in case links change
        'hawaii-business-automation-guide.html': 'assets/images/blog1.png',
        'how-to-beat-the-odds-in-hawaii.html': 'assets/images/blog2.png'
    }
    
    files_to_process = ['index.html', 'blog.html', 'blog1.html', 'blog2.html']

    for file_path in files_to_process:
        if not os.path.exists(file_path):
            print(f"\n[SKIP] File not found: {file_path}")
            continue

        print(f"\n--- Processing: {file_path} ---")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')

            changes_made = False
            
            # Logic for list pages (index.html, blog.html)
            if file_path in ['index.html', 'blog.html']:
                links_to_posts = soup.find_all('a', href=lambda href: href in image_mapping)
                for link in links_to_posts:
                    href = link.get('href')
                    correct_image_src = image_mapping[href]
                    img_tag = link.find('img')
                    if img_tag and img_tag.get('src') != correct_image_src:
                        img_tag['src'] = correct_image_src
                        changes_made = True
                        print(f"  - Updated image for link '{href}' to '{correct_image_src}'")

            # Logic for individual post pages (blog1.html, blog2.html)
            elif file_path in ['blog1.html', 'blog2.html']:
                correct_image_src = image_mapping.get(file_path)
                for img_tag in soup.find_all('img'):
                    # Don't change the logo
                    if 'logo' in img_tag.get('alt', '').lower():
                        continue
                    if img_tag.get('src') != correct_image_src:
                        img_tag['src'] = correct_image_src
                        changes_made = True
                        print(f"  - Updated a page image to '{correct_image_src}'")
            
            if changes_made:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup.prettify()))
                print(f"  - Successfully saved changes to {file_path}.")
            else:
                print(f"  - No path updates were needed for {file_path}.")

        except Exception as e:
            print(f"  - ERROR: An error occurred in update_all_image_paths: {e}")

def main():
    """
    Main function to run the entire fix-and-update process.
    """
    print("=====================================================")
    print("Silva Automation - Website Image Corrector")
    print("=====================================================")

    # Step 1: Ensure the basic HTML structure is correct for each post.
    ensure_hero_image_exists(
        'blog1.html', 
        'assets/images/blog1.png', 
        'A Guide to Hawaii Business Automation', 
        'Automating business processes can save significant time and reduce costly errors.'
    )
    ensure_hero_image_exists(
        'blog2.html', 
        'assets/images/blog2.png', 
        'Strategy for overcoming high business costs in Hawaii', 
        'Automation provides a strategic advantage against high operational costs.'
    )

    # Step 2: Now that structures are verified, update all paths to be correct.
    update_all_image_paths()

    print("\n--- SCRIPT COMPLETE ---")
    print("All files have been checked and updated.")
    print("Please verify your website. Remember to place 'blog1.png' and 'blog2.png' in the 'assets/images/' folder.")
    print("=====================================================")

if __name__ == "__main__":
    main()
