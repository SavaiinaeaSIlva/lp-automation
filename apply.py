# swap_and_resize.py
# This script swaps the background styles of the Process and About sections
# and further enlarges the profile picture in the About section.

import os

def swap_and_resize_styles():
    """
    Finds the specific class strings for the Process and About sections
    and their profile picture, then swaps/updates them.
    """
    file_path = 'index.html'

    if not os.path.exists(file_path):
        print(f"❌ Error: '{file_path}' not found.")
        print("Please ensure this script is in the same directory as your index.html file.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        original_content = content
        
        # --- DEFINE CURRENT AND NEW STYLES ---

        # The current blue-tinted style of the "Process" section
        current_blue_style = "p-8 md:p-12 bg-slate-900/40 backdrop-blur-sm rounded-2xl shadow-lg shadow-blue-500/10"
        
        # The current black style of the "About" section
        current_black_style = "p-8 md:p-12 bg-black/50 backdrop-blur-sm rounded-2xl shadow-xl shadow-white/5"

        # The current size of the profile picture
        current_pic_size = 'class="w-24 h-24 rounded-full border-2 border-slate-700 object-cover shadow-lg mr-4"'
        
        # The new, larger size for the picture
        new_pic_size = 'class="w-32 h-32 rounded-full border-2 border-slate-700 object-cover shadow-lg mr-4"'

        # A list of tuples for each replacement: (string_to_find, string_to_replace_with)
        replacements = [
            # 1. Change the Process section from blue to black
            (current_blue_style, current_black_style),
            
            # 2. Change the About section from black to blue
            (current_black_style, current_blue_style),
            
            # 3. Enlarge the picture
            (current_pic_size, new_pic_size)
        ]

        for find_str, replace_str in replacements:
            content = content.replace(find_str, replace_str)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print("✅ Success! The section styles have been swapped and the picture has been enlarged.")
        else:
            print("🤔 No changes were made. The styles may not match what the script is looking for.")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    swap_and_resize_styles()