import os
from bs4 import BeautifulSoup

# --- Configuration ---
# List of files to update.
FILES_TO_UPDATE = ['about.html', 'packages.html', 'blog.html']

# The HTML snippet for the video and overlay.
VIDEO_SNIPPET = """
<video autoplay loop muted playsinline class="absolute z-0 w-full h-full object-cover">
    <source src="assets/videos/hero-backdrop.webm" type="video/webm" />
    <source src="assets/videos/hero-backdrop.mp4" type="video/mp4" />
    Your browser does not support the video tag.
</video>
<div class="absolute inset-0 bg-black/70 z-0"></div>
"""

def update_html_file(filename):
    """
    Reads an HTML file, adds a video background to the main section,
    and overwrites the file with the changes.
    """
    if not os.path.exists(filename):
        print(f"⚠️  Warning: File '{filename}' not found. Skipping.")
        return

    try:
        # Read the original HTML file content
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')

        # Find the main tag, then the first section within it
        main_tag = soup.find('main')
        if not main_tag:
            print(f"❌ Error: No <main> tag found in '{filename}'. Skipping.")
            return

        hero_section = main_tag.find('section')
        if not hero_section:
            print(f"❌ Error: No <section> tag found within <main> in '{filename}'. Skipping.")
            return

        # --- Modify the section's classes ---
        # Get current classes, or an empty list if none exist
        current_classes = hero_section.get('class', [])
        
        # Remove old background classes if they exist
        classes_to_remove = ['bg-hero-pattern', 'bg-black']
        updated_classes = [c for c in current_classes if c not in classes_to_remove]

        # Add the overflow-hidden class to ensure video is contained
        if 'overflow-hidden' not in updated_classes:
            updated_classes.append('overflow-hidden')
        
        # Update the class attribute on the section tag
        hero_section['class'] = updated_classes

        # --- Insert the video and overlay ---
        # Create a new soup from the video snippet
        video_soup = BeautifulSoup(VIDEO_SNIPPET, 'html.parser')

        # Insert the new elements at the beginning of the section
        # The .contents extracts the tags from the parsed snippet
        for element in reversed(video_soup.contents):
             if element.name: # Ensure it's a tag and not just whitespace
                hero_section.insert(0, element)

        # Write the modified HTML back to the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))

        print(f"✅ Successfully updated '{filename}' with video background.")

    except Exception as e:
        print(f"❌ An unexpected error occurred while processing '{filename}': {e}")


# --- Main execution ---
if __name__ == "__main__":
    print("🚀 Starting website update script...")
    for file in FILES_TO_UPDATE:
        update_html_file(file)
    print("\n✨ Script finished.")
