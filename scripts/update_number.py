import os
import re

def update_phone_number_in_html(directory_path, old_number, new_number):
    """
    Finds and replaces an old phone number with a new one in all HTML files
    within the specified directory and its subdirectories.

    Args:
        directory_path (str): The root directory to start searching for files.
        old_number (str): The phone number to be replaced (e.g., "8083081107").
        new_number (str): The new phone number to use (e.g., "8082235888").
    """
    
    # --- Phone Number Formatting and Pattern Setup ---
    
    # 1. Pattern to match the old number, ignoring common separators
    old_number_digits = "".join(filter(str.isdigit, old_number))
    if len(old_number_digits) != 10:
        print(f"Error: The old number '{old_number}' must contain exactly 10 digits.")
        return

    area_code = old_number_digits[:3]
    prefix = old_number_digits[3:6]
    line_number = old_number_digits[6:]

    # Regex to catch variations like 808-308-1107, (808) 308-1107, 8083081107, etc.
    old_number_pattern = re.compile(
        # Optional: Start of group capture for optional parentheses or leading 'tel:'
        r'(\s*tel:|\(?\s*)?' 
        # Area code (e.g., 808)
        + re.escape(area_code) 
        # Separator (e.g., ), -, ., or space)
        + r'(\)?[\s\-\.]*)?' 
        # Prefix (e.g., 308)
        + re.escape(prefix)
        # Separator
        + r'([\s\-\.]*)?'
        # Line number (e.g., 1107)
        + re.escape(line_number)
        , re.IGNORECASE
    )

    # 2. Standard format for the new number replacement
    new_number_formatted = f'{new_number[:3]}-{new_number[3:6]}-{new_number[6:]}'
    
    # 3. Standard format for the old number (for logging)
    old_number_formatted = f'{old_number[:3]}-{old_number[3:6]}-{old_number[6:]}'

    print(f"Starting phone number replacement in: {directory_path}")
    print(f"  Old Number: {old_number_formatted}")
    print(f"  New Number: {new_number_formatted}")
    print("-" * 30)
    
    files_updated_count = 0
    total_replacements = 0

    # Walk through all directories and files starting from the specified path
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            # Check if the file is an HTML file
            if file_name.endswith(('.html', '.htm')):
                file_path = os.path.join(root, file_name)
                
                try:
                    # 1. Read the file content
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # 2. Perform the replacement using the regex pattern
                    new_content, count = old_number_pattern.subn(new_number_formatted, content)
                    
                    if count > 0:
                        # 3. Write the new content back to the file
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                            
                        print(f"✅ Updated {count} occurrence(s) in: {file_path}")
                        files_updated_count += 1
                        total_replacements += count
                        
                except Exception as e:
                    print(f"❌ Error processing file {file_path}: {e}")

    print("-" * 30)
    print(f"Script finished!")
    print(f"Total files updated: {files_updated_count}")
    print(f"Total number replacements: {total_replacements}")


# --- FINALIZED CONFIGURATION ---

# ⚠️ The path has been updated to the one you provided
WEBSITE_DIRECTORY = '/home/nza/lp-automation' 

# Your current (old) phone number
OLD_NUMBER = '8083081107'

# Your new phone number
NEW_NUMBER = '8082235888'
# -------------------------------

# Run the function with the path and numbers set above
if __name__ == "__main__":
    
    # --- Path Check for Safety ---
    if not os.path.isdir(WEBSITE_DIRECTORY):
        print("🛑 ERROR: The directory path is invalid or does not exist.")
        print(f"Please check: {WEBSITE_DIRECTORY}")
    else:
        update_phone_number_in_html(WEBSITE_DIRECTORY, OLD_NUMBER, NEW_NUMBER)
