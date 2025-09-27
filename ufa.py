# A simple script to find and replace the blog image placeholder in HTML files.

# --- Configuration ---
# List of files to search through. Add more file names if needed.
files_to_process = ["index.html", "blog.html"]

# The exact placeholder HTML we are looking for.
placeholder_html = '<div class="aspect-video bg-slate-800 rounded-lg mb-4"></div>'

# The new HTML that will replace the placeholder.
new_image_html = '<img src="assets/images/pic1.png" alt="Blog post image" class="aspect-video w-full object-cover rounded-lg mb-4">'
# --- End of Configuration ---


def update_html_files():
    """
    Loops through the specified files, reads their content, replaces the
    placeholder, and writes the changes back to the file.
    """
    print("Starting image placeholder update...")
    
    for filename in files_to_process:
        try:
            # Read the original content of the file
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()

            # Check if the placeholder exists in the content
            if placeholder_html in content:
                # Replace the placeholder with the new image tag
                updated_content = content.replace(placeholder_html, new_image_html)
                
                # Write the updated content back to the file
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                
                print(f"✅ Successfully updated '{filename}'")
            else:
                print(f"ℹ️ Placeholder not found in '{filename}'. No changes made.")

        except FileNotFoundError:
            print(f"❌ Error: File '{filename}' not found. Please check the file name and location.")
        except Exception as e:
            print(f"❌ An unexpected error occurred with '{filename}': {e}")

    print("\nScript finished.")


# Run the main function
if __name__ == "__main__":
    update_html_files()
