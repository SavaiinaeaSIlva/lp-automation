import os
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
# Your correct Calendly link
calendly_url = "https://calendly.com/silvaautomation/consultation"

# Your Formspree endpoint. 
# IMPORTANT: Replace "YOUR_FORM_ID" with your actual Formspree form ID.
formspree_url = "https://formspree.io/f/xyznjyjj" 

# List of HTML files to scan and update
files_to_scan = [
    'index.html',
    'about.html',
    'packages.html',
    'blog1.html',
    'blog2.html'
]

# Keywords to identify which buttons should link to Calendly
calendly_keywords = ['schedule', 'book', 'consultation', 'discovery']

# --- SCRIPT LOGIC ---

def fix_links_in_file(filename):
    """Parses an HTML file, fixes Calendly links and the Formspree form, and saves it."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        made_changes = False

        # --- 1. Fix Calendly Links ---
        # Find all anchor tags (<a>)
        all_links = soup.find_all('a')
        for link in all_links:
            # Check if the link text contains any of our keywords
            link_text = link.get_text().lower()
            if any(keyword in link_text for keyword in calendly_keywords):
                # If it's a scheduling link, update its href and add target="_blank"
                if link.get('href') != calendly_url:
                    print(f"  -> Updating Calendly link in {filename}: '{link.get_text().strip()}'")
                    link['href'] = calendly_url
                    link['target'] = '_blank'
                    made_changes = True

        # --- 2. Fix Formspree Form (only in index.html) ---
        if filename == 'index.html':
            contact_form = soup.find('form')
            if contact_form:
                if contact_form.get('action') != formspree_url:
                    print(f"  -> Updating Formspree endpoint in {filename}")
                    contact_form['action'] = formspree_url
                    contact_form['method'] = 'POST'
                    made_changes = True
            else:
                print(f"  -> WARNING: Could not find a <form> tag in {filename}.")


        # --- 3. Save the file only if changes were made ---
        if made_changes:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"✅ Successfully updated links in {filename}")
        else:
            print(f"No changes needed for {filename}")

    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found. Skipping.")
    except Exception as e:
        print(f"An unexpected error occurred with {filename}: {e}")


# --- Main execution ---
if __name__ == "__main__":
    print("Starting site-wide link update...")
    if "YOUR_FORM_ID" in formspree_url:
        print("\n⚠️  WARNING: Please edit the script and replace 'YOUR_FORM_ID' with your real Formspree ID.\n")
        
    for file in files_to_scan:
        fix_links_in_file(file)
    
    print("\nUpdate process complete.")
