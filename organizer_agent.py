import os
import shutil
import time
import mimetypes

WATCHED_FOLDER = r"D:\Madhu\AIAgents\file-organizer-agent\agent_folder"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp", ".raw", ".heic", ".jfif", ".avif"],
    "Compressed": [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z"],
    "Text": [".txt", ".csv", ".log", ".md", ".json", ".xml", ".yaml", ".yml"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp"],
    "Scripts": [".py", ".js", ".html", ".css", ".php", ".java", ".c", ".cpp", ".rb", ".sh", ".bat"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
    "Executables": [".exe", ".msi", ".apk", ".bin", ".dmg", ".iso"],
    "Databases": [".db", ".sql", ".sqlite", ".mdb", ".accdb"],
    "Unknown": []
}

def organize_files():
    for filename in os.listdir(WATCHED_FOLDER):
        file_path = os.path.join(WATCHED_FOLDER, filename)
        if os.path.isdir(file_path):
            continue
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type:
            main_type = mime_type.split('/')[0]
            if main_type == 'image':
                folder = 'Images'
            elif main_type == 'video':
                folder = 'Videos'
            elif main_type == 'audio':
                folder = 'Audio'
            elif main_type == 'text':
                folder = 'Text'
            elif main_type in ['application', 'document']:
                folder = 'Documents'
            elif main_type == 'compressed':
                folder = 'Compressed'
            elif main_type == 'script':
                folder = 'Scripts'
            else:
                folder = 'Unknown'
        else:
            folder = 'Unknown'
        if folder == 'Unknown':
            print(f"Unknown file type detected: {filename}")
        destination_folder = os.path.join(WATCHED_FOLDER, folder)
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(destination_folder, filename))
        print(f"Moved {filename} to {folder}")

print("🤖 Agent started. Watching folder...")
while True:
    organize_files()
    time.sleep(10)
