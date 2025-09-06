# A simple script to find and replace text in specified files.

# --- CONFIGURATION ---
# Add the names of the files you want to change here.
FILES_TO_UPDATE = [
    'index.html',
    'process.html'
]

# What text are we looking for?
OLD_IMAGE_PATH = 'assets/images/silvas.svg'

# What should we replace it with?
NEW_IMAGE_PATH = 'logo.png'
# ---------------------


def update_file_content(filename):
    """Reads a file, replaces the old image path with the new one, and saves it."""
    try:
        # Step 1: Read the original file content
        with open(filename, 'r', encoding='utf-8') as file:
            original_content = file.read()
            print(f"Reading '{filename}'...")

        # Step 2: Check if there's anything to replace
        if OLD_IMAGE_PATH not in original_content:
            print(f"-> No instances of '{OLD_IMAGE_PATH}' found in '{filename}'. Skipping.")
            return

        # Step 3: Replace the old path with the new one
        updated_content = original_content.replace(OLD_IMAGE_PATH, NEW_IMAGE_PATH)
        
        # Step 4: Write the updated content back to the file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        
        print(f"-> Successfully updated '{filename}'!")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file name and location.")
    except Exception as e:
        print(f"An unexpected error occurred with '{filename}': {e}")


# --- Main execution ---
if __name__ == "__main__":
    print("Starting image source update...")
    for file_to_process in FILES_TO_UPDATE:
        update_file_content(file_to_process)
    print("\nScript finished.")
