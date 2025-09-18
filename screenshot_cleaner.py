#!/usr/bin/env python3
"""
Screenshot Cleaner Script
Safely finds and removes screenshot files from common locations
"""

import os
import glob
import shutil
from pathlib import Path
from datetime import datetime, timedelta
import argparse

class ScreenshotCleaner:
    def __init__(self, dry_run=True, days_old=30):
        self.dry_run = dry_run
        self.days_old = days_old
        self.cutoff_date = datetime.now() - timedelta(days=days_old)
        
        # Common screenshot file patterns
        self.screenshot_patterns = [
            'Screenshot*.png',
            'Screenshot*.jpg',
            'Screenshot*.jpeg',
            'Screen Shot*.png',
            'Screen Shot*.jpg',
            'Screen Shot*.jpeg',
            'screenshot*.png',
            'screenshot*.jpg',
            'screenshot*.jpeg',
            'screen*.png',
            'screen*.jpg',
            'screen*.jpeg',
            'IMG_*.png',
            'IMG_*.jpg',
            'IMG_*.jpeg',
            'Photo*.png',
            'Photo*.jpg',
            'Photo*.jpeg'
        ]
        
        # Common screenshot locations
        self.search_paths = [
            str(Path.home() / 'Desktop'),
            str(Path.home() / 'Downloads'),
            str(Path.home() / 'Pictures'),
            str(Path.home() / 'Pictures' / 'Screenshots'),
            str(Path.home() / 'Documents'),
            '/tmp',
            '/var/tmp'
        ]
    
    def is_web_project_folder(self, folder_path):
        """Check if folder contains index.html or assets subdirectory"""
        try:
            # Check for index.html in the folder
            if os.path.exists(os.path.join(folder_path, 'index.html')):
                return True
            
            # Check for assets subdirectory
            if os.path.exists(os.path.join(folder_path, 'assets')):
                return True
                
            # Check for common web project files
            web_files = ['package.json', 'index.js', 'main.js', 'app.js', 'style.css', 'main.css']
            for web_file in web_files:
                if os.path.exists(os.path.join(folder_path, web_file)):
                    return True
                    
        except (OSError, FileNotFoundError):
            pass
        
        return False
    
    def should_skip_path(self, file_path):
        """Check if file path should be skipped (in web project folder)"""
        path_parts = Path(file_path).parts
        
        # Check each directory in the path
        for i in range(len(path_parts)):
            current_path = os.path.join(*path_parts[:i+1])
            if self.is_web_project_folder(current_path):
                return True
        
        return False
    
    def find_screenshots(self):
        """Find all screenshot files matching patterns"""
        screenshots = []
        skipped_count = 0
        
        for search_path in self.search_paths:
            if not os.path.exists(search_path):
                continue
                
            print(f"🔍 Searching in: {search_path}")
            
            for pattern in self.screenshot_patterns:
                # Search for files matching pattern
                search_pattern = os.path.join(search_path, '**', pattern)
                files = glob.glob(search_pattern, recursive=True)
                
                for file_path in files:
                    try:
                        # Skip files in web project folders
                        if self.should_skip_path(file_path):
                            skipped_count += 1
                            continue
                        
                        # Get file modification time
                        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                        
                        # Check if file is older than cutoff date
                        if mod_time < self.cutoff_date:
                            file_size = os.path.getsize(file_path)
                            screenshots.append({
                                'path': file_path,
                                'size': file_size,
                                'modified': mod_time,
                                'age_days': (datetime.now() - mod_time).days
                            })
                    except (OSError, FileNotFoundError):
                        continue
        
        if skipped_count > 0:
            print(f"🛡️  Skipped {skipped_count} files in web project folders")
        
        return screenshots
    
    def format_size(self, size_bytes):
        """Convert bytes to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def display_screenshots(self, screenshots):
        """Display found screenshots in a nice format"""
        if not screenshots:
            print("✅ No old screenshots found!")
            return
        
        total_size = sum(s['size'] for s in screenshots)
        
        print(f"\n📸 Found {len(screenshots)} old screenshots:")
        print("=" * 80)
        print(f"{'File':<50} {'Size':<10} {'Age':<8} {'Modified'}")
        print("=" * 80)
        
        for screenshot in screenshots:
            filename = os.path.basename(screenshot['path'])
            size = self.format_size(screenshot['size'])
            age = f"{screenshot['age_days']}d"
            modified = screenshot['modified'].strftime('%Y-%m-%d')
            
            print(f"{filename:<50} {size:<10} {age:<8} {modified}")
        
        print("=" * 80)
        print(f"Total files: {len(screenshots)}")
        print(f"Total size: {self.format_size(total_size)}")
        print(f"Space to free: {self.format_size(total_size)}")
    
    def clean_screenshots(self, screenshots):
        """Remove screenshot files"""
        if not screenshots:
            return
        
        removed_count = 0
        removed_size = 0
        errors = []
        
        print(f"\n{'🧹 DRY RUN - ' if self.dry_run else '🗑️  DELETING '}Screenshots...")
        
        for screenshot in screenshots:
            try:
                if not self.dry_run:
                    os.remove(screenshot['path'])
                
                removed_count += 1
                removed_size += screenshot['size']
                
                status = "Would delete" if self.dry_run else "Deleted"
                print(f"{status}: {os.path.basename(screenshot['path'])}")
                
            except OSError as e:
                error_msg = f"Error deleting {screenshot['path']}: {e}"
                errors.append(error_msg)
                print(f"❌ {error_msg}")
        
        # Summary
        print(f"\n{'📊 DRY RUN ' if self.dry_run else '✅ CLEANUP '}Summary:")
        print(f"Files {'would be ' if self.dry_run else ''}removed: {removed_count}")
        print(f"Space {'would be ' if self.dry_run else ''}freed: {self.format_size(removed_size)}")
        
        if errors:
            print(f"\n❌ Errors encountered: {len(errors)}")
            for error in errors:
                print(f"  - {error}")
    
    def run(self):
        """Main execution function"""
        print("🖼️  Screenshot Cleaner")
        print("=" * 50)
        print(f"Mode: {'DRY RUN' if self.dry_run else 'LIVE DELETION'}")
        print(f"Age threshold: {self.days_old} days")
        print(f"Cutoff date: {self.cutoff_date.strftime('%Y-%m-%d %H:%M')}")
        print()
        
        # Find screenshots
        screenshots = self.find_screenshots()
        
        # Display results
        self.display_screenshots(screenshots)
        
        if screenshots:
            if self.dry_run:
                print(f"\n💡 This was a DRY RUN. No files were actually deleted.")
                print(f"💡 Run with --live to actually delete the files.")
            else:
                # Ask for confirmation
                response = input(f"\n⚠️  Are you sure you want to delete {len(screenshots)} files? (y/N): ")
                if response.lower() in ['y', 'yes']:
                    self.clean_screenshots(screenshots)
                else:
                    print("❌ Operation cancelled.")
        else:
            print("\n🎉 No old screenshots found to clean!")

def main():
    parser = argparse.ArgumentParser(description='Clean up old screenshot files (protects web project folders)')
    parser.add_argument('--live', action='store_true', 
                       help='Actually delete files (default is dry run)')
    parser.add_argument('--days', type=int, default=30,
                       help='Delete files older than this many days (default: 30)')
    parser.add_argument('--path', type=str,
                       help='Additional path to search (can be used multiple times)')
    
    args = parser.parse_args()
    
    # Add custom path if provided
    cleaner = ScreenshotCleaner(dry_run=not args.live, days_old=args.days)
    
    if args.path:
        cleaner.search_paths.append(args.path)
    
    cleaner.run()

if __name__ == "__main__":
    main()
