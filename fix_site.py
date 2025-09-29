# fix_legal_header.py
import os
import shutil
import re

# --- Configuration ---
LEGAL_FILE = 'legal.html'
BACKUP_DIR = 'backups'

# The new header structure.
# It uses a three-column flexbox layout (w-1/3) to ensure the
# logo remains perfectly centered while the back link is on the far left.
NEW_LEGAL_HEADER_HTML = """<header class="bg-black border-b border-white/10 py-4">
    <div class="container mx-auto px-6 flex items-center justify-between">
        <div class="w-1/3">
            <a href="index.html" class="text-blue-500 hover:text-blue-400 font-semibold text-sm transition-colors">
                &larr; Back to main site
            </a>
        </div>
        <div class="w-1/3 flex justify-center">
            <a href="index.html" aria-label="Back to Silva Automation Home">
                <img src="assets/images/logo.png" alt="Silva Automation Logo" class="h-14 w-auto">
            </a>
        </div>
        <div class="w-1/3"></div>
    </div>
</header>"""


def create_backup():
    """Creates a backup of the legal file before modification."""
    print("--- Starting Backup ---")
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    if os.path.exists(LEGAL_FILE):
        try:
            shutil.copy2(LEGAL_FILE, os.path.join(BACKUP_DIR, os.path.basename(LEGAL_FILE)))
            print(f"Backed up '{LEGAL_FILE}'")
            print("Backup completed successfully.\n")
            return True
        except Exception as e:
            print(f"Error during backup of {LEGAL_FILE}: {e}")
            return False
    else:
        print(f"Error: File '{LEGAL_FILE}' not found for backup. Cannot proceed.")
        return False

def update_legal_header():
    """Replaces the existing header in legal.html with the new, improved version."""
    print(f"--- Updating Header for {LEGAL_FILE} ---")
    
    with open(LEGAL_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the existing <header>...</header> block to replace it
    header_pattern = re.compile(r'<header.*?</header>', re.DOTALL)
    new_content, count = header_pattern.subn(NEW_LEGAL_HEADER_HTML, content)

    if count > 0:
        with open(LEGAL_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully replaced header in '{LEGAL_FILE}'.")
    else:
        print(f"Warning: No <header> tag found in '{LEGAL_FILE}'. No changes made.")
    print("Legal page header update complete.\n")


def main():
    """Run all update tasks."""
    if create_backup():
        update_legal_header()
        print("✅ Script finished successfully!")

if __name__ == "__main__":
    main()
