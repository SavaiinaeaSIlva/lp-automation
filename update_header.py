# update_header_position.py

import os

# --- Configuration: Define all the code blocks to find and replace ---

# For index.html
INDEX_HTML_HEADER_ORIGINAL = '<header class="fixed top-0 left-0 right-0 z-50 transition-all duration-300" id="main-header">'
INDEX_HTML_HEADER_NEW = '<header class="absolute top-0 left-0 right-0 z-50 transition-all duration-300" id="main-header">'

INDEX_JS_BLOCK_ORIGINAL = """    const header = document.getElementById('main-header');
    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 50) header.classList.add('header-scrolled');
            else header.classList.remove('header-scrolled');
        };
        handleScroll(); 
        window.addEventListener('scroll', handleScroll);
    }"""
INDEX_JS_BLOCK_NEW = """    /*
    const header = document.getElementById('main-header');
    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 50) header.classList.add('header-scrolled');
            else header.classList.remove('header-scrolled');
        };
        handleScroll(); 
        window.addEventListener('scroll', handleScroll);
    }
    */"""

# For process.html
PROCESS_HTML_HEADER_ORIGINAL = '<header class="fixed top-0 left-0 right-0 z-50 transition-all duration-300" id="main-header">'
PROCESS_HTML_HEADER_NEW = '<header class="absolute top-0 left-0 right-0 z-50 transition-all duration-300" id="main-header">'

# For assets/js/script.js
SCRIPT_JS_BLOCK_ORIGINAL = """    // --- Header Scroll Behavior ---
    const header = document.getElementById('main-header');
    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('header-scrolled');
            } else {
                header.classList.remove('header-scrolled');
            }
        };
        handleScroll(); 
        window.addEventListener('scroll', handleScroll);
    }"""
SCRIPT_JS_BLOCK_NEW = """    // --- Header Scroll Behavior ---
    /*
    const header = document.getElementById('main-header');
    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 50) {
                header.classList.add('header-scrolled');
            } else {
                header.classList.remove('header-scrolled');
            }
        };
        handleScroll(); 
        window.addEventListener('scroll', handleScroll);
    }
    */"""

# --- Main Script Logic ---

def process_file(filepath, replacements):
    """Reads a file, applies replacements, and writes it back if changed."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"-> SKIPPING: File not found at '{filepath}'")
        return

    original_content = content
    changes_made = False

    for original, new in replacements:
        if original in content:
            content = content.replace(original, new)
            changes_made = True

    if changes_made:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"-> SUCCESS: Updated '{filepath}'")
    else:
        print(f"-> INFO: No changes needed for '{filepath}'")


if __name__ == "__main__":
    print("Starting header update script...")

    # Define which replacements apply to which file
    all_tasks = {
        "index.html": [
            (INDEX_HTML_HEADER_ORIGINAL, INDEX_HTML_HEADER_NEW),
            (INDEX_JS_BLOCK_ORIGINAL, INDEX_JS_BLOCK_NEW)
        ],
        "process.html": [
            (PROCESS_HTML_HEADER_ORIGINAL, PROCESS_HTML_HEADER_NEW)
        ],
        os.path.join("assets", "js", "script.js"): [
            (SCRIPT_JS_BLOCK_ORIGINAL, SCRIPT_JS_BLOCK_NEW)
        ]
    }

    # Execute all tasks
    for filepath, replacements in all_tasks.items():
        process_file(filepath, replacements)

    print("\nScript finished.")
