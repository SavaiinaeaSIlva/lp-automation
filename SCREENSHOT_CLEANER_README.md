# Screenshot Cleaner 🖼️

A safe Python script to clean up old screenshot files while protecting your web development projects.

## 🛡️ Safety Features

- **Protects web project folders** - Won't touch any files in folders containing:
  - `index.html`
  - `assets/` subdirectory
  - `package.json`, `main.js`, `style.css`, etc.
- **Dry run by default** - Shows what would be deleted without actually deleting
- **Age filtering** - Only deletes files older than specified days
- **Detailed reporting** - Shows file sizes, ages, and space savings

## 🚀 Usage

### Basic Usage (Dry Run)
```bash
python3 screenshot_cleaner.py
```

### Delete Files Older Than 60 Days
```bash
python3 screenshot_cleaner.py --days 60
```

### Actually Delete Files (Live Mode)
```bash
python3 screenshot_cleaner.py --live
```

### Add Custom Search Path
```bash
python3 screenshot_cleaner.py --path "/path/to/your/folder"
```

## 📁 What It Searches

- Desktop
- Downloads
- Pictures
- Documents
- /tmp
- /var/tmp
- Any custom paths you specify

## 🔍 What It Finds

- Screenshot*.png/jpg
- Screen Shot*.png/jpg
- IMG_*.png/jpg
- Photo*.png/jpg
- And more screenshot patterns

## ⚠️ Safety Notes

- Always run without `--live` first to see what would be deleted
- The script will ask for confirmation before deleting in live mode
- Web project folders are automatically protected
- Files are only deleted if they're older than the specified age threshold

## 🎯 Example Output

```
🖼️  Screenshot Cleaner
==================================================
Mode: DRY RUN
Age threshold: 30 days
Cutoff date: 2025-08-15 00:55

🔍 Searching in: /home/user/Desktop
🛡️  Skipped 3 files in web project folders

📸 Found 15 old screenshots:
================================================================================
File                                            Size       Age      Modified
================================================================================
Screenshot 2024-12-01 at 10.30.15.png         2.3 MB     45d      2024-12-01
Screenshot 2024-11-28 at 14.22.33.png         1.8 MB     48d      2024-11-28
================================================================================
Total files: 15
Total size: 25.4 MB
Space to free: 25.4 MB

💡 This was a DRY RUN. No files were actually deleted.
💡 Run with --live to actually delete the files.
```
