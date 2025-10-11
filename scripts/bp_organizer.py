import os
import shutil
import re

def organize_blog_posts(root_directory):
    """
    Creates a 'b_posts' subdirectory and moves all numbered blog files 
    (e.g., blog1.html) into it, while keeping 'blog.html' in the root.

    Args:
        root_directory (str): The main directory path of the website files.
    """
    
    # --- Configuration ---
    SUBFOLDER_NAME = 'b_posts'
    # The absolute path to the new subfolder
    target_folder = os.path.join(root_directory, SUBFOLDER_NAME)
    
    # Regex to find files that start with 'blog' followed by a number, and end with .html or .htm
    # Examples: 'blog1.html', 'blog99.htm', 'blog-10.html' (if dash is used)
    # The 'r' before the string indicates a raw string, important for regex.
    BLOG_POST_PATTERN = re.compile(r'^blog\d+.*\.html?$', re.IGNORECASE)
    
    files_moved_count = 0

    print(f"Starting blog post organization in: {root_directory}")
    print("-" * 40)
    
    # 1. Create the target subfolder if it doesn't exist
    if not os.path.exists(target_folder):
        try:
            os.makedirs(target_folder)
            print(f"✅ Created subfolder: {target_folder}")
        except Exception as e:
            print(f"❌ ERROR: Could not create folder {target_folder}. Reason: {e}")
            return # Stop execution if folder creation fails

    # 2. Iterate through files only in the root directory
    try:
        # os.listdir gets all files and folders in the current directory
        for item_name in os.listdir(root_directory):
            source_path = os.path.join(root_directory, item_name)
            
            # Check if the item is a file (not a folder)
            if os.path.isfile(source_path):
                
                # Check if the file name matches the numbered blog post pattern
                if BLOG_POST_PATTERN.match(item_name):
                    
                    # Ensure we don't accidentally try to move the new folder itself 
                    # (though it shouldn't match the regex, this is a safety check)
                    if item_name != SUBFOLDER_NAME:
                        
                        destination_path = os.path.join(target_folder, item_name)
                        
                        # Use shutil.move to move the file
                        shutil.move(source_path, destination_path)
                        print(f"➡️ Moved: {item_name}")
                        files_moved_count += 1
                        
                # 3. Explicitly confirm the homepage stays (optional print, good for reassurance)
                elif item_name.lower() == 'blog.html':
                     print(f"☑️ Left in root: {item_name}")
                     
    except Exception as e:
        print(f"❌ An unexpected error occurred while processing files: {e}")


    print("-" * 40)
    print(f"Script finished!")
    print(f"Total blog post files moved to '{SUBFOLDER_NAME}': {files_moved_count}")


# --- CONFIGURATION ---

# The confirmed root directory of your website files
WEBSITE_DIRECTORY = '/home/nza/lp-automation' 

# ---------------------

# Run the function
if __name__ == "__main__":
    # Add a check to ensure we only process files in the root, not subdirectories 
    # (as os.listdir is used, this is inherently limited to the root)
    organize_blog_posts(WEBSITE_DIRECTORY)
