import os

# --- Configuration ---
# Add the names of the HTML files you want to fix to this list.
FILES_TO_FIX = [
    'marketing-agency-onboarding-guide.html',
    'hawaii-business-automation-guide.html'
]

# The class string we are looking for in the <article> tag.
# This is specific to avoid accidentally changing other tags.
STRING_TO_FIND = 'class="prose prose-lg max-w-none"'

# The new class string with "prose-invert" added.
REPLACEMENT_STRING = 'class="prose prose-invert prose-lg max-w-none"'
# --- End of Configuration ---

def fix_html_file(filename):
    """
    Reads an HTML file, adds the 'prose-invert' class, and saves it.
    """
    print(f"--- Processing: {filename} ---")
    
    # Check if the file exists before trying to open it.
    if not os.path.exists(filename):
        print(f"⚠️  Error: File not found. Skipping.")
        return

    try:
        # Read the original content of the file.
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Check if the string to fix is actually in the file.
        if STRING_TO_FIND in content:
            # Replace the old string with the new one.
            new_content = content.replace(STRING_TO_FIND, REPLACEMENT_STRING)

            # Write the modified content back to the file.
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(new_content)
            
            print(f"✅ Success: 'prose-invert' class added to {filename}")
        else:
            print(f"ℹ️  Info: The specific 'prose' class was not found. File left unchanged.")

    except Exception as e:
        print(f"❌ An error occurred while processing {filename}: {e}")

# --- Main script execution ---
if __name__ == "__main__":
    print("Starting the blog post style fixer script...")
    for file_to_process in FILES_TO_FIX:
        fix_html_file(file_to_process)
    print("\nScript finished.")