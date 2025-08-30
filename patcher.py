import os

# --- Configuration ---
# List of HTML files to modify
HTML_FILES = ['terms.html', 'privacy.html', 'cookie.html', 'refund.html']

# --- Replacement Rules based on the uploaded HTML files ---

# Rule 1: Fix the <body> tag
# The old tag found in the files
OLD_BODY_TAG = '<body class="antialiased">'
NEW_BODY_TAG = '<body class="antialiased bg-black text-gray-300">'

# Rule 2: Fix the .prose <div> tag
# The old div found in the files
OLD_PROSE_DIV = '<div class="prose prose-invert max-w-none text-neutral-300 space-y-6">'
NEW_PROSE_DIV = '<div class="prose max-w-none space-y-6">'

# --- Main Script Logic ---
def patch_html_files():
    """
    Loops through the specified HTML files and applies the necessary fixes
    to the body and prose div tags.
    """
    print("Starting the HTML patching process for legal pages...")
    files_processed = 0
    files_changed = 0

    for filename in HTML_FILES:
        print(f"\n--- Processing '{filename}' ---")
        
        if not os.path.exists(filename):
            print(f"❌ Error: File not found. Skipping.")
            continue

        files_processed += 1
        made_change = False
        
        try:
            # Read the original file content
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            original_content = content
            
            # Apply Rule 1: Fix the body tag
            if OLD_BODY_TAG in content:
                content = content.replace(OLD_BODY_TAG, NEW_BODY_TAG)
                print("✅ Patched <body> tag.")
                made_change = True
            else:
                print("🔹 Notice: <body> tag did not need patching.")

            # Apply Rule 2: Fix the prose div
            if OLD_PROSE_DIV in content:
                content = content.replace(OLD_PROSE_DIV, NEW_PROSE_DIV)
                print("✅ Patched .prose <div> tag.")
                made_change = True
            else:
                print("🔹 Notice: .prose <div> did not need patching.")

            # Write the updated content back to the file if changes were made
            if made_change:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(content)
                files_changed += 1
                print(f"✨ '{filename}' has been updated.")
            else:
                print(f"✨ '{filename}' is already up to date.")

        except Exception as e:
            print(f"An unexpected error occurred while processing {filename}: {e}")
    
    print("\n--- Patching complete! ---")
    print(f"Processed: {files_processed} files.")
    print(f"Changed: {files_changed} files.")

# --- Run the script ---
if __name__ == "__main__":
    patch_html_files()
