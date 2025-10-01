# re.py
import os

# --- Configuration ---
# The full script tag you want to manage.
script_to_manage = '<script src="//code.tidio.co/lzqrmnv0dmxjzjtah0zyvzplmzxb3qes.js" async></script>'
# The file that SHOULD contain the script.
main_file = 'index.html'
# The directory where your HTML files are. '.' means the current directory.
target_directory = '.'
# --- End of Configuration ---

def process_html_files():
    """
    Scans the target directory for HTML files.
    - Removes the script_to_manage from all .html files except main_file.
    - Ensures the script_to_manage is present just before the </body> tag in main_file.
    """
    try:
        # Get a list of all files in the specified directory
        all_files = os.listdir(target_directory)
    except FileNotFoundError:
        print(f"❌ Error: Directory not found at '{target_directory}'")
        return

    # Filter for only HTML files
    html_files = [f for f in all_files if f.endswith('.html')]

    if not html_files:
        print("🤔 No HTML files found in this directory.")
        return

    print("🚀 Starting script management...")

    for filename in html_files:
        filepath = os.path.join(target_directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                original_content = content
            
            # --- Logic for the main file (e.g., index.html) ---
            if filename == main_file:
                # First, remove any existing instances to prevent duplicates or wrong placement
                content = content.replace(script_to_manage, '')

                # Then, insert it cleanly before the closing body tag
                if '</body>' in content:
                    content = content.replace('</body>', f'    {script_to_manage}\n</body>')
                else:
                    print(f"⚠️  Warning: No </body> tag found in {filename}. Could not add script.")

                # Write changes only if the file was modified
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(content)
                    print(f"✅  Corrected script position in: {filename}")
                else:
                    print(f"👍  Script already correct in: {filename}")

            # --- Logic for all other HTML files ---
            else:
                if script_to_manage in content:
                    content = content.replace(script_to_manage, '')
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(content)
                    print(f"🗑️  Removed script from: {filename}")
                else:
                    print(f"⚪️  No script to remove from: {filename}")

        except Exception as e:
            print(f"❗️ Error processing {filename}: {e}")
    
    print("\n✨ Done.")

# --- Run the function ---
if __name__ == "__main__":
    process_html_files()
