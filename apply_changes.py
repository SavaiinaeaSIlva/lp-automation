# fix_subheading_v2.py
import sys
from bs4 import BeautifulSoup

# --- DEFINE THE CORRECT SUBHEADING ---

# The text you want to display
subheading_text = "One price. No subscriptions. No hidden fees. Just more time for you, and less stress every day."

# The new "badge" style classes to make it pop
subheading_classes = "inline-block text-lg font-medium text-blue-300 bg-blue-500/10 border border-blue-500/30 rounded-full px-6 py-3 mb-8"


# --- SCRIPT LOGIC (More Robust Version) ---

file_path = 'index.html'

print(f"🔄 Attempting to robustly fix subheading in '{file_path}'...")

try:
    # Read the original HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the pricing section by its ID
    pricing_section = soup.find('section', id='pricing')
    if not pricing_section:
        raise ValueError("Could not find the pricing section with id='pricing'.")

    # Find the container div with the text-center class
    text_center_div = pricing_section.find('div', class_='text-center')
    if not text_center_div:
        raise ValueError("Could not find the 'text-center' div inside the pricing section.")
        
    # Find the main heading (h2) to use as an anchor for placement
    h2_tag = text_center_div.find('h2')
    if not h2_tag:
        raise ValueError("Could not find the h2 heading inside the 'text-center' div.")

    # Find the first paragraph (the old subheading) inside this container
    old_subheading = text_center_div.find('p')
    if old_subheading:
        print("   - Found old subheading, removing it...")
        old_subheading.decompose() # This completely removes the old tag

    # Create the new, correctly styled subheading tag
    new_subheading_p = soup.new_tag('p')
    new_subheading_p['class'] = subheading_classes.split()
    new_subheading_p.string = subheading_text

    # Insert the new tag immediately after the h2 heading
    h2_tag.insert_after(new_subheading_p)
    print("   - Inserted new, correctly styled subheading.")

    # Write the modified content back to the HTML file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))

    print(f"✅ Successfully saved changes to '{file_path}'.")
    print("\nNext step: Run your Tailwind build command!")

except FileNotFoundError:
    print(f"❌ Error: '{file_path}' not found. Make sure this script is in the same folder as your HTML file.")
except Exception as e:
    print(f"An error occurred: {e}")
