# fix_subheading.py
import sys
from bs4 import BeautifulSoup

# --- DEFINE THE CORRECT SUBHEADING ---

# The correct text for the subheading
subheading_text = "One price. No subscriptions. No hidden fees. Just more time for you, and less stress every day."

# The correct Tailwind classes to make it visible (light gray text)
subheading_classes = "max-w-2xl mx-auto text-base text-gray-300 mb-4"


# --- SCRIPT LOGIC ---

file_path = 'index.html'

print(f"🔄 Attempting to fix subheading in '{file_path}'...")

try:
    # Read the original HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the pricing section by its ID
    pricing_section = soup.find('section', id='pricing')
    if not pricing_section:
        print("❌ Error: Could not find the pricing section with id='pricing'.")
        sys.exit(1)

    # Find the h2 heading within the pricing section
    h2_tag = pricing_section.find('h2', string=lambda t: 'No-Nonsense' in t if t else False)
    if not h2_tag:
        print("❌ Error: Could not find the main 'No-Nonsense' heading.")
        sys.exit(1)

    # Find the paragraph that should be the subheading (the first <p> after the <h2>)
    subheading_p = h2_tag.find_next_sibling('p')

    if subheading_p:
        # If the tag exists, update its class and text to be sure it's correct
        subheading_p['class'] = subheading_classes.split()
        subheading_p.string = subheading_text
        print("✅ Found existing subheading tag and corrected it.")
    else:
        # If the tag was deleted, create a new one and insert it
        new_subheading_p = soup.new_tag('p')
        new_subheading_p['class'] = subheading_classes.split()
        new_subheading_p.string = subheading_text
        h2_tag.insert_after(new_subheading_p)
        print("✅ Subheading tag was missing. A new one has been created and inserted.")

    # Write the modified content back to the HTML file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))

    print(f"✅ Successfully saved changes to '{file_path}'.")
    print("\nNext step: Remember to run your Tailwind build command!")

except FileNotFoundError:
    print(f"❌ Error: '{file_path}' not found. Make sure this script is in the same folder as your HTML file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
