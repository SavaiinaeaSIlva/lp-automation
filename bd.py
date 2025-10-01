import os

def update_footer_style(directory='.'):
    """
    Finds all HTML files and updates the footer style for a more distinct look.
    """
    print("Starting script to update footer style...")

    # The exact string of the old footer tag we want to replace
    old_footer_tag = '<footer class="bg-black/60 backdrop-blur-sm border-t border-white/10">'
    
    # The new footer tag with a solid background and clearer border
    new_footer_tag = '<footer class="bg-zinc-900 border-t border-zinc-800">'

    try:
        html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' was not found.")
        return

    if not html_files:
        print(f"No HTML files found in '{os.path.abspath(directory)}'.")
        return

    files_changed = 0
    for filename in html_files:
        filepath = os.path.join(directory, filename)
        print(f"Processing '{filename}'...")

        try:
            with open(filepath, 'r+', encoding='utf-8') as f:
                content = f.read()
                
                # Check if the old footer tag exists in the file
                if old_footer_tag in content:
                    # Replace the old tag with the new one
                    new_content = content.replace(old_footer_tag, new_footer_tag)
                    
                    # Go back to the start of the file to overwrite its content
                    f.seek(0)
                    f.write(new_content)
                    f.truncate()
                    
                    print(f"-> Updated footer style in '{filename}'.")
                    files_changed += 1
                else:
                    print(f"-> Footer style already updated or not found. No change needed.")

        except Exception as e:
            print(f"-> Failed to process '{filename}': {e}")
            
    print(f"\nScript finished. {files_changed} file(s) were updated.")

if __name__ == "__main__":
    update_footer_style()
