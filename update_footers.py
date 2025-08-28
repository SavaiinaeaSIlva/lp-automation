import os
import re

# --- Color Palette Definition ---
# Define the old colors we want to find and the new colors to replace them with.
# This makes it easy to change your mind later!
COLOR_REPLACEMENTS = {
    # Primary CTA Button: from emerald green to a strong blue
    "bg-emerald-500": "bg-blue-500",
    "bg-emerald-600": "bg-blue-600",
    
    # Before/After Section: from red/green to a more neutral/on-brand palette
    "text-red-400": "text-gray-400",
    "text-green-400": "text-blue-400",
}

def update_html_file_colors(filepath):
    """Reads an HTML file, replaces color classes, and writes it back."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        # Perform the replacements
        for old_color, new_color in COLOR_REPLACEMENTS.items():
            content = content.replace(old_color, new_color)

        # Check if any changes were made before writing the file
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"    [SUCCESS] Colors updated in {os.path.basename(filepath)}")
            return True
        else:
            print(f"    [INFO] No colors to update in {os.path.basename(filepath)}")
            return False
            
    except Exception as e:
        print(f"    [ERROR] Could not process {os.path.basename(filepath)}: {e}")
        return False

def process_all_files():
    """Finds all HTML files in the current directory and updates their colors."""
    print("🚀 Starting color update process...")
    updated_count = 0
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            if update_html_file_colors(filename):
                updated_count += 1
    
    print(f"\n🎉 Color update finished. {updated_count} file(s) were modified.")

if __name__ == "__main__":
    process_all_files()
