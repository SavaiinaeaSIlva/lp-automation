from bs4 import BeautifulSoup
import os
import sys
import shutil

# --- Configuration ---
# The correct path your logo should have
correct_logo_path = 'assets/images/logo.png' 
# The alt text used to identify your logo's <img> tag
logo_identifier_alt_text = 'Silva Automation Logo'
# --------------------

# --- Script Logic (No need to edit below this line) ---

# Get the filename from the command line argument
if len(sys.argv) < 2:
    print("❌ Error: Please provide a filename to check.")
    print(f"   Usage: python {sys.argv[0]} your_file.html")
    sys.exit(1) # Exit the script

filename_to_check = sys.argv[1]
backup_filename = filename_to_check + '.bak'

try:
    if not os.path.exists(filename_to_check):
        raise FileNotFoundError
    # Create a safe backup of the original file
    shutil.copyfile(filename_to_check, backup_filename)
    print(f"✅ Created a safe backup: '{backup_filename}'")

    # Read and parse the HTML file
    with open(filename_to_check, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find all image tags that are the logo
    logo_images = soup.find_all('img', alt=logo_identifier_alt_text)
    
    if not logo_images:
        print(f"⚠️ Warning: Could not find any logo images with alt text: '{logo_identifier_alt_text}'.")
    else:
        print(f"Found {len(logo_images)} logo instance(s) in '{filename_to_check}'. Checking paths...")
        changes_made = 0
        
        # Loop through them and correct the path if it's wrong
        for img in logo_images:
            original_path = img.get('src')
            if original_path != correct_logo_path:
                print(f"  - Path was incorrect: '{original_path}'")
                img['src'] = correct_logo_path
                print(f"    -> Corrected to: '{correct_logo_path}'")
                changes_made += 1
            else:
                print(f"  - Path is already correct.")

        # Write the corrected HTML back to the file
        if changes_made > 0:
            with open(filename_to_check, 'w', encoding='utf-8') as file:
                file.write(str(soup.prettify()))
            print(f"\n✨ Success! Fixed {changes_made} path(s) in '{filename_to_check}'.")
        else:
            print("\n✅ No changes were needed.")

except FileNotFoundError:
    print(f"❌ Error: The file '{filename_to_check}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
