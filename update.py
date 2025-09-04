import re
import os

# --- CONFIGURATION ---

# The HTML files you want to update.
TARGET_FILES = [
    'index.html',
    'process.html', 
]

# The full HTML for the link you want to add or update.
# NOTE: The script will also make this link 'font-bold' on the process.html page.
NEW_LINK_HTML = '<a class="nav-link text-gray-300 hover:text-white transition-colors" href="process.html">Our Process</a>'

# A unique part of the link that should come *before* the new one.
# The script will insert the new link immediately after this one.
ANCHOR_LINK_CONTENT = 'href="index.html#how-it-works"'

# --- SCRIPT LOGIC (No need to edit below) ---

def update_navigation_links():
    """
    Adds or updates a specific navigation link in both the desktop
    and mobile menus of the target HTML files.
    """
    print("🚀 Starting navigation update script...")

    # Use regex to extract the href for checking if the link exists
    href_match = re.search(r'href="([^"]+)"', NEW_LINK_HTML)
    if not href_match:
        print("❌ ERROR: Could not find an href in your NEW_LINK_HTML. Exiting.")
        return
    link_href = href_match.group(1)

    # Process each file
    for filename in TARGET_FILES:
        if not os.path.exists(filename):
            print(f"   -> ⚠️  File '{filename}' not found. Skipping.")
            continue

        print(f"   -> Processing '{filename}'...")
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # --- Define the regex patterns for the menus ---
        # Pattern for the desktop <nav>
        desktop_nav_pattern = re.compile(r'(<nav class="hidden md:flex.*?">)(.*?)(</nav>)', re.DOTALL)
        # Pattern for the mobile <nav>
        mobile_nav_pattern = re.compile(r'(<nav class="flex flex-col space-y-8.*?">)(.*?)(</nav>)', re.DOTALL)

        # Update both menus
        content = process_menu(content, desktop_nav_pattern, link_href, filename)
        content = process_menu(content, mobile_nav_pattern, link_href, filename)

        # Write the updated content back to the file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   -> ✔️  Finished updating '{filename}'")

    print("\n✨ Script finished. Navigation links should be consistent.")

def process_menu(content, pattern, link_href, current_file):
    """Finds a menu, then adds or updates the link within it."""
    menu_match = pattern.search(content)
    if not menu_match:
        return content

    nav_open, nav_content, nav_close = menu_match.groups()
    
    # Check if the link already exists in this menu
    link_exists_regex = re.compile(f'<a [^>]*href="{re.escape(link_href)}".*?</a>')
    
    final_link_html = NEW_LINK_HTML
    # Special rule: If we are on the page the link points to, make it bold.
    if link_href == current_file:
         # Add font-bold and remove hover effect classes for active state
         final_link_html = NEW_LINK_HTML.replace('text-gray-300 hover:text-white transition-colors', 'text-white font-bold')

    if link_exists_regex.search(nav_content):
        # Link exists, so UPDATE it to the latest version
        updated_nav_content = link_exists_regex.sub(final_link_html, nav_content)
    else:
        # Link doesn't exist, so ADD it after the anchor
        anchor_regex = re.compile(f'(<a [^>]*{re.escape(ANCHOR_LINK_CONTENT)}.*?</a>)')
        # Add the new link on a new line with indentation for readability
        replacement_str = f'\\1\n    {final_link_html}'
        updated_nav_content = anchor_regex.sub(replacement_str, nav_content)

    # Reassemble the full content
    return content.replace(menu_match.group(0), f"{nav_open}{updated_nav_content}{nav_close}")


# Run the script
if __name__ == "__main__":
    update_navigation_links()
