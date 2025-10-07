import os
import shutil
from bs4 import BeautifulSoup

# --- Configuration ---
PROJECT_ROOT = os.getcwd()
VIDEO_DIR = os.path.join(PROJECT_ROOT, "assets", "videos")
HTML_FILES = ["index.html", "about.html", "blog.html", "packages.html"]
NEW_VIDEO_FILES = ["hero-backdrop.mp4", "hero-backdrop.webm"]
NEW_VIDEO_NAME = "hero-backdrop"

# --- Main Functions ---

def setup_video_files():
    """Creates the video directory and moves the new video files into it."""
    print("--- 1. Setting up video files ---")
    try:
        # Create the directory if it doesn't exist
        os.makedirs(VIDEO_DIR, exist_ok=True)
        print(f"✅ Directory '{VIDEO_DIR}' is ready.")

        # Move each video file
        for video_file in NEW_VIDEO_FILES:
            source_path = os.path.join(PROJECT_ROOT, video_file)
            dest_path = os.path.join(VIDEO_DIR, video_file)

            if os.path.exists(source_path):
                shutil.move(source_path, dest_path)
                print(f"✅ Moved '{video_file}' to '{VIDEO_DIR}'.")
            elif os.path.exists(dest_path):
                 print(f"👍 '{video_file}' is already in the correct directory.")
            else:
                print(f"⚠️  WARNING: Could not find '{video_file}' in the root directory. Please make sure it's there.")
    except Exception as e:
        print(f"❌ ERROR setting up video files: {e}")


def update_html_files():
    """Updates the hero sections in all HTML files."""
    print("\n--- 2. Updating HTML files ---")
    for filename in HTML_FILES:
        filepath = os.path.join(PROJECT_ROOT, filename)
        if not os.path.exists(filepath):
            print(f"⚠️  Skipping non-existent file: '{filename}'")
            continue

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f, "lxml")

            hero_section = soup.find("section", id="hero")
            if not hero_section:
                print(f"🤷 No hero section found in '{filename}'.")
                continue

            # --- Apply structural fixes for non-index pages ---
            is_updated = False
            if filename != "index.html":
                current_classes = hero_section.get("class", [])
                
                # Classes to remove and add for consistency
                classes_to_remove = ["py-20", "md:py-32"]
                classes_to_add = ["h-[60vh]", "flex", "items-center", "justify-center"]

                original_class_count = len(current_classes)
                current_classes = [c for c in current_classes if c not in classes_to_remove]
                for c in classes_to_add:
                    if c not in current_classes:
                        current_classes.append(c)
                
                if len(current_classes) != original_class_count:
                    is_updated = True

                hero_section["class"] = current_classes

            # --- Update video sources in all pages ---
            video_sources = hero_section.find_all("source")
            if video_sources:
                for source_tag in video_sources:
                    if "mp4" in source_tag["src"]:
                        new_src = f"assets/videos/{NEW_VIDEO_NAME}.mp4"
                        if source_tag["src"] != new_src:
                            source_tag["src"] = new_src
                            is_updated = True
                    elif "webm" in source_tag["src"]:
                        new_src = f"assets/videos/{NEW_VIDEO_NAME}.webm"
                        if source_tag["src"] != new_src:
                            source_tag["src"] = new_src
                            is_updated = True
            
            if is_updated:
                 with open(filepath, "w", encoding="utf-8") as f:
                    f.write(str(soup.prettify()))
                 print(f"✅ Updated hero section in '{filename}'.")
            else:
                 print(f"👍 No changes needed for '{filename}'.")


        except Exception as e:
            print(f"❌ ERROR processing '{filename}': {e}")


# --- Script Execution ---
if __name__ == "__main__":
    setup_video_files()
    update_html_files()
    print("\n🚀 Script finished!")
    print("🔴 IMPORTANT: Please run your Tailwind build command now to see the changes.")
