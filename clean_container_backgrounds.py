# clean_html.py
# This script removes specific background classes from an HTML file to make containers transparent.

import os

def clean_container_backgrounds():
    """
    Reads index.html, removes specified background classes, and overwrites the file.
    """
    file_path = 'index.html'

    # Verify that the HTML file exists in the current directory
    if not os.path.exists(file_path):
        print(f"❌ Error: '{file_path}' not found.")
        print("Please make sure this script is in the same directory as your index.html file.")
        return

    # List of tuples containing the exact class string to find and its replacement.
    replacements = [
        # 1. Large Section Containers (Problem, Process, About)
        (
            'class="bg-slate-900/50 backdrop-blur-sm rounded-2xl p-8 md:p-12 border border-white/10 shadow-lg shadow-white/[0.03]"',
            'class="rounded-2xl p-8 md:p-12 border border-white/10 shadow-lg shadow-white/[0.03]"'
        ),
        # 2. Small "Step" boxes in the Process section
        (
            'class="bg-slate-900 p-8 rounded-2xl border border-slate-700 text-center"',
            'class="p-8 rounded-2xl border border-slate-700 text-center"'
        ),
        # 3. "Why Work With Me?" box in the About section
        (
            'class="bg-slate-900 p-6 rounded-lg border border-slate-700"',
            'class="p-6 rounded-lg border border-slate-700"'
        ),
        # 4. ROI Calculator box
        (
            'class="space-y-6 bg-slate-900/50 p-6 rounded-lg border border-slate-700"',
            'class="space-y-6 p-6 rounded-lg border border-slate-700"'
        ),
        # 5. Contact Form box
        (
            'class="bg-slate-900/50 p-8 rounded-lg border border-slate-700"',
            'class="p-8 rounded-lg border border-slate-700"'
        )
    ]

    try:
        # Read the entire content of the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        original_content = content
        total_changes = 0

        # Loop through the list of replacements and apply them
        for find_str, replace_str in replacements:
            # Count how many times the target string appears
            occurrences = content.count(find_str)
            if occurrences > 0:
                # Replace all occurrences
                content = content.replace(find_str, replace_str)
                total_changes += occurrences

        # Only write back to the file if changes were actually made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"✅ Success! Made {total_changes} replacements in '{file_path}'.")
            print("Your containers should now have clear backgrounds.")
        else:
            print("🤔 No changes needed. It looks like the classes have already been updated.")

    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# This ensures the function runs when the script is executed
if __name__ == "__main__":
    clean_container_backgrounds()