import os
import shutil
import time

# 👀 The folder the agent will watch
WATCHED_FOLDER = r"D:\Madhu\AIAgents\file-organizer-agent\agent_folder"  # change this to your real path!

# 📂 File types and their target folders
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".raw", ".heic", ".jfif", ".avif"],
    "Compressed": [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z"],
    "Text": [".txt", ".csv", ".log"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Scripts": [".py", ".js", ".html", ".css", ".php"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi"],
}

def organize_files():
    for filename in os.listdir(WATCHED_FOLDER):
        file_path = os.path.join(WATCHED_FOLDER, filename)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Check file type and move accordingly
        for folder, extensions in FILE_TYPES.items():
            if filename.lower().endswith(tuple(extensions)):
                destination_folder = os.path.join(WATCHED_FOLDER, folder)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved {filename} to {folder}")
                break

# 🔁 Watch folder every 5 seconds
print("🤖 Agent started. Watching folder...")
while True:
    organize_files()
    time.sleep(5)  # Check every 5 seconds
    # You can change this to a longer interval if needed
    # For example, time.sleep(60) will check every minute
