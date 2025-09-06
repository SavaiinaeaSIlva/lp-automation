# update_logo_size.py

# --- Configuration ---
# The name of the file you want to modify.
file_to_modify = 'index.html'

# Define the exact HTML line for the header logo to find and replace.
header_logo_original = '<img alt="Silva Automation Logo" class="h-12 md:h-16 w-auto transition-all duration-300" src="assets/images/logo.png" width="200" height="64"/>'
header_logo_new      = '<img alt="Silva Automation Logo" class="h-24 md:h-32 w-auto transition-all duration-300" src="assets/images/logo.png" width="200" height="64"/>'

# Define the exact HTML line for the footer logo to find and replace.
footer_logo_original = '<img alt="Silva Automation Logo" class="h-8 w-auto mx-auto md:mx-0" src="assets/images/logo.png"/>'
footer_logo_new      = '<img alt="Silva Automation Logo" class="h-16 w-auto mx-auto md:mx-0" src="assets/images/logo.png"/>'

# --- Main Script Logic ---
print(f"Attempting to update logo sizes in '{file_to_modify}'...")

try:
    # Read the original content of the file
    with open(file_to_modify, 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Keep track of original content to see if changes were made
    original_content = content
    
    # Replace the header logo line
    if header_logo_original in content:
        content = content.replace(header_logo_original, header_logo_new)
        print(" -> Header logo updated.")
    else:
        print(" -> Header logo original code not found. Skipping.")
        
    # Replace the footer logo line
    if footer_logo_original in content:
        content = content.replace(footer_logo_original, footer_logo_new)
        print(" -> Footer logo updated.")
    else:
        print(" -> Footer logo original code not found. Skipping.")

    # Write the modified content back to the file only if changes were made
    if content != original_content:
        with open(file_to_modify, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"\nSuccessfully saved changes to '{file_to_modify}'.")
    else:
        print("\nNo changes were made. The file might already be updated.")

except FileNotFoundError:
    print(f"\nError: The file '{file_to_modify}' was not found.")
    print("Please make sure this script is in the same folder as your index.html file.")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
