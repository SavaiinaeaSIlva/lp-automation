# apply_changes.py
import sys
from bs4 import BeautifulSoup

# --- DEFINE THE NEW STYLES ---

# Style for the main, center card (Growth Package)
# This class string adds `z-10` to ensure it's on top by default.
main_card_classes = "p-6 rounded-xl bg-gradient-to-br from-blue-600 to-blue-700 flex flex-col relative h-full shadow-2xl hover:shadow-3xl hover:-translate-y-2 transition-all duration-300 transform scale-105 z-10"

# Style for the two side cards (Essential & Enterprise)
# This class string adds `scale-95` and the hover effects to bring it forward.
side_card_classes = "bg-gradient-to-b from-slate-800 to-slate-900 p-6 rounded-xl flex flex-col border-2 border-blue-500 shadow-lg transition-all duration-300 h-full scale-95 hover:scale-100 hover:z-20"


# --- SCRIPT LOGIC ---

file_path = 'index.html'

print(f"🔄 Attempting to modify '{file_path}'...")

try:
    # Read the original HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find the pricing section by its ID
    pricing_section = soup.find('section', id='pricing')
    if not pricing_section:
        print("❌ Error: Could not find the pricing section with id='pricing'.")
        sys.exit(1)

    # Find the three direct div children of the grid container within the pricing section
    cards = pricing_section.find('div', class_='grid').find_all('div', recursive=False)
    
    if len(cards) != 3:
        print(f"❌ Error: Expected to find 3 pricing cards, but found {len(cards)}. Aborting.")
        sys.exit(1)
        
    print(f"✅ Found {len(cards)} pricing cards.")

    # Loop through the cards and apply the new classes
    for card in cards:
        title_tag = card.find('h3')
        if not title_tag:
            continue
        
        title = title_tag.get_text(strip=True)
        
        if title == "Growth Package":
            card['class'] = main_card_classes.split()
            print("   - Updated 'Growth Package' card.")
        elif title in ["Essential Package", "Enterprise Package"]:
            card['class'] = side_card_classes.split()
            print(f"   - Updated '{title}' card.")

    # Write the modified content back to the HTML file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup.prettify()))

    print(f"✅ Successfully saved changes to '{file_path}'.")
    print("\nNext step: Don't forget to run your Tailwind build command!")

except FileNotFoundError:
    print(f"❌ Error: '{file_path}' not found. Make sure this script is in the same folder as your HTML file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
