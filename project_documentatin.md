# File Organizer Agent Documentation

## Modules Used

### 1. `os`
- Provides functions to interact with the operating system, such as reading directories, creating folders, and working with paths.
- **Example**: `os.listdir()` lists all files and folders in a directory.

### 2. `shutil`
- Used for high-level file operations, such as copying, moving, and deleting files.
- **Example**: `shutil.move()` moves a file from one location to another.

### 3. `time`
- Provides time-related functions, such as pausing the program for a specific duration.
- **Example**: `time.sleep(10)` pauses the program for 10 seconds.

### 4. `mimetypes`
- Used to guess the MIME type of a file based on its filename or extension.
- **Example**: `mimetypes.guess_type("example.jpg")` returns `('image/jpeg', None)`.

#### Sample Data:
- File: `example.jpg` in the folder `Images`.
- **Code**: `mimetypes.guess_type("example.jpg")` returns `('image/jpeg', None)`.

---

## Watching the Folder

### `WATCHED_FOLDER`
```python
WATCHED_FOLDER = r"D:\Madhu\AIAgents\file-organizer-agent\agent_folder"
```

### Explanation:
1. **WATCHED_FOLDER**:
    - Specifies the folder that the agent will monitor for changes.
    - The `r` before the string makes it a raw string, ensuring backslashes (`\`) are treated literally.

2. **Purpose**:
    - The agent continuously monitors this folder (`agent_folder`) for new files or changes and organizes them into subfolders based on their types.

#### Sample Data:
- Folder: `agent_folder`
- Subfolders: `Images`, `Documents`, `Text`, etc.
- Files: 
  - `example.pdf` (in `Documents`)
  - `133863245164225738.jpg` (in `Images`)

---

## File Types and Their Target Folders

### 📂 File Types and Target Folders
```python
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
     "Unknown": []  # For files that don't match any category
}
```

### Explanation:
- **FILE_TYPES Dictionary**:
  - Maps file categories (e.g., "Images", "Documents") to a list of file extensions.
  - **Example**:
     - `"Images"` includes extensions like `.jpg`, `.png`, `.gif`, etc.
     - `"Documents"` includes extensions like `.pdf`, `.docx`, `.xlsx`, etc.

- **Purpose**:
  - Determines the appropriate folder for each file based on its extension.
  - Files with unknown extensions are placed in the `"Unknown"` folder.

#### Sample Data:
1. File: `example.pdf`
    - Extension: `.pdf`
    - Category: `"Documents"`
    - Target Folder: `Documents/`
2. File: `133863245164225738.jpg`
    - Extension: `.jpg`
    - Category: `"Images"`
    - Target Folder: `Images/`
3. File: `unknownfile.xyz`
    - Extension: `.xyz`
    - Category: `"Unknown"`
    - Target Folder: `Unknown/`

---

## Organizing Files

### Function: `organize_files`
```python
def organize_files():
     for filename in os.listdir(WATCHED_FOLDER):
          file_path = os.path.join(WATCHED_FOLDER, filename)

          # Skip if it's a folder
          if os.path.isdir(file_path):
                continue

          # Detect MIME type of the file
          mime_type, _ = mimetypes.guess_type(file_path)
          
          # Determine the folder based on MIME type
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

          # Log unknown file types
          if folder == 'Unknown':
                print(f"Unknown file type detected: {filename}")

          # Create the destination folder if it doesn't exist
          destination_folder = os.path.join(WATCHED_FOLDER, folder)
          os.makedirs(destination_folder, exist_ok=True)

          # Move the file to the appropriate folder
          shutil.move(file_path, os.path.join(destination_folder, filename))
          print(f"Moved {filename} to {folder}")
```

### Explanation:
1. **Purpose**:
    - Organizes files in the `WATCHED_FOLDER` directory.

2. **Steps**:
    - Iterates through files in the folder.
    - Skips folders.
    - Detects MIME type to determine the target folder.
    - Logs unknown file types.
    - Creates the destination folder if it doesn't exist.
    - Moves the file to the appropriate folder.

#### Sample Data:
1. File: `example.pdf`
    - MIME Type: `application/pdf`
    - Target Folder: `Documents/`
    - **Action**: File is moved to `Documents/`.
2. File: `unknownfile.xyz`
    - MIME Type: `None`
    - Target Folder: `Unknown/`
    - **Action**: File is moved to `Unknown/` and a log message is printed.

---

## Watching the Folder Periodically

### Code:
```python
# 🔁 Watch folder every 10 seconds
print("🤖 Agent started. Watching folder...")
while True:
     organize_files()
     time.sleep(10)
```

### Explanation:
1. **Purpose**:
    - Continuously monitors the folder for changes.

2. **Steps**:
    - Prints a message indicating the agent has started.
    - Enters an infinite loop:
      - Calls `organize_files()` to process files.
      - Waits for 10 seconds before repeating.

#### Sample Data:
1. **Initial State**:
    - `agent_folder` contains:
      - `example.pdf` in `Documents/`
      - `unknownfile.xyz` in the root folder.
2. **After 10 Seconds**:
    - Files are processed:
      - `example.pdf` is moved to `Documents/`.
      - `unknownfile.xyz` is moved to `Unknown/`.
3. **New File Added**:
    - A new file, `new_image.png`, is added to the folder.
    - After 10 seconds, the agent detects and moves it to `Images/`.

---
