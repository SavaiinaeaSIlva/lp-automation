import os

# --- Configuration ---
FILENAME = "index.html"
PLACEHOLDER_LINE = '<form action="#" method="POST" class="space-y-4">'
NEW_LINE = '<form action="https://formspree.io/f/xandwpzq" method="POST" class="space-y-4">'
# -------------------

def update_form_action():
    """Finds the placeholder form tag and replaces it with the real one."""
    print(f"🚀 Attempting to update {FILENAME}...")

    # Check if the file exists
    if not os.path.exists(FILENAME):
        print(f"   [ERROR] File not found: {FILENAME}. Please run this script in the correct directory.")
        return

    # Read the file content
    with open(FILENAME, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if the placeholder exists
    if PLACEHOLDER_LINE not in content:
        print(f"   [INFO] No placeholder found. The form link might already be updated.")
        return

    # Replace the placeholder with the new line
    updated_content = content.replace(PLACEHOLDER_LINE, NEW_LINE)

    # Write the updated content back to the file
    with open(FILENAME, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"   [SUCCESS] {FILENAME} has been updated with the new Formspree link.")
    print("✨ Your contact form is now live!")

if __name__ == "__main__":
    update_form_action()
