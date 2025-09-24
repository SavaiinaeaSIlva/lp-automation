# finalize_design.py
import sys
from bs4 import BeautifulSoup

# --- FINAL DESIGN SPECIFICATIONS ---

# Hero Section
HERO_STYLE = "background-image: linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.9)), url('assets/images/backdrop.png'); background-size: cover; background-position: center;"
HERO_CTA_CLASSES = "inline-block text-base font-semibold text-white bg-orange-600 py-3 px-8 rounded-lg transition-all duration-300 hover:bg-orange-700 hover:-translate-y-1 hover:shadow-[0_0_30px_rgba(249,115,22,0.5)]"
HERO_ROBOT_IMAGE = "assets/images/hero2.jpg"

# Pricing Section
PRICING_SUBHEADING_CLASSES = "inline-block text-lg font-medium text-blue-300 bg-blue-500/10 border border-blue-500/30 rounded-full px-6 py-3 mb-8"
PRICING_SUBHEADING_TEXT = "One price. No subscriptions. No hidden fees. Just more time for you, and less stress every day."

# Pricing Cards (Face-off effect)
MAIN_CARD_CLASSES = "p-6 rounded-xl bg-gradient-to-br from-blue-600 to-blue-700 flex flex-col relative h-full shadow-2xl hover:shadow-3xl hover:-translate-y-2 transition-all duration-300 transform scale-105 z-10"
SIDE_CARD_CLASSES = "bg-gradient-to-b from-slate-800 to-slate-900 p-6 rounded-xl flex flex-col border-2 border-blue-500 shadow-lg transition-all duration-300 h-full scale-95 hover:scale-100 hover:z-20"

# Pricing Buttons
MAIN_BUTTON_CLASSES = "mt-auto w-full text-base font-semibold bg-orange-600 text-white py-2 px-4 rounded-lg transition-all duration-300 hover:bg-orange-700 hover:-translate-y-1 hover:shadow-lg"
SIDE_BUTTON_CLASSES = "mt-auto w-full text-base font-semibold bg-transparent border-2 border-blue-500 text-blue-400 py-2 px-4 rounded-lg transition-all duration-300 hover:bg-blue-500 hover:text-white hover:-translate-y-1 hover:shadow-lg"


def apply_all_changes(file_path='index.html'):
    """Finds and updates the hero and pricing sections to the final design."""
    print(f"🔄 Starting the design finalization process for '{file_path}'...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

        # --- 1. UPDATE HERO SECTION ---
        print("   - Updating Hero Section...")
        hero_section = soup.find('section', id='hero')
        if hero_section:
            # Delete any duplicate hero sections to be safe
            for duplicate in hero_section.find_next_siblings('section', id='hero'):
                duplicate.decompose()
                print("     - Found and removed a duplicate hero section.")

            # Set the background style
            hero_section['style'] = HERO_STYLE
            
            # Find and update the CTA button
            hero_cta = hero_section.find('a', string=lambda t: 'Start My Project' in t if t else False)
            if hero_cta:
                hero_cta['class'] = HERO_CTA_CLASSES.split()
            
            # Find and fix the robot image
            robot_img = hero_section.find('img', {'alt': 'Silva Automation Mascot'})
            if robot_img:
                robot_img['src'] = HERO_ROBOT_IMAGE
            print("     - Hero section styles and images updated.")
        else:
            print("     - WARNING: Could not find hero section.")

        # --- 2. UPDATE PRICING SECTION ---
        print("   - Updating Pricing Section...")
        pricing_section = soup.find('section', id='pricing')
        if pricing_section:
            # Fix subheading
            h2_tag = pricing_section.find('h2')
            if h2_tag:
                old_p = h2_tag.find_next_sibling('p')
                if old_p:
                    old_p['class'] = PRICING_SUBHEADING_CLASSES.split()
                    old_p.string = PRICING_SUBHEADING_TEXT
                    print("     - Pricing subheading updated to badge style.")

            # Apply face-off effect and button styles to cards
            cards = pricing_section.find('div', class_='grid').find_all('div', recursive=False)
            if len(cards) == 3:
                # Essential Card (Side)
                cards[0]['class'] = SIDE_CARD_CLASSES.split()
                cards[0].find('a')['class'] = SIDE_BUTTON_CLASSES.split()
                # Growth Card (Main)
                cards[1]['class'] = MAIN_CARD_CLASSES.split()
                cards[1].find('a')['class'] = MAIN_BUTTON_CLASSES.split()
                # Enterprise Card (Side)
                cards[2]['class'] = SIDE_CARD_CLASSES.split()
                cards[2].find('a')['class'] = SIDE_BUTTON_CLASSES.split()
                print("     - 'Face-off' effect and button styles applied to pricing cards.")
        else:
            print("     - WARNING: Could not find pricing section.")

        # --- SAVE THE FILE ---
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup.prettify()))
        
        print(f"\n✅ All changes have been saved to '{file_path}'.")
        print("➡️ Next step: Run your Tailwind build command!")

    except FileNotFoundError:
        print(f"❌ ERROR: Could not find '{file_path}'. Make sure this script is in the same folder.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Ensure BeautifulSoup is installed
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("❌ ERROR: BeautifulSoup library not found.")
        print("Please install it by running this command in your terminal: pip install beautifulsoup4")
        sys.exit(1)
    
    apply_all_changes()