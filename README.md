# AUTO_FILE_MANAGER
OVERVIEW:

AutoFileOrganizer is a Python script designed to automatically detect and organize files in a specified source directory. Using the Watchdog library, the script monitors changes to the directory and moves files into appropriate subdirectories based on their type and size.

The script is highly configurable, allowing users to set their preferred source and destination directories for various file types. It supports file types such as images, music, movies, PDFs, and sound effects (SFX), with special handling for large files (e.g., distinguishing between music and SFX based on size).

FEATURES:

Monitoring -  Uses the watchdog library to automatically detect changes in a source directory and organize files without manual instruction. 
File Types Supported - Images (.PNG, .JPG, .JPEG, .HEIC), PDF (.PDF), AUDIO FILES (.WAV, .MP3), VIDEO (.MP4, .MOV).
Unique File Names - Handles filename conflicts by renaming files to avoid overwriting existing files in the destination folder.

INSTALLATION:

- Python 3.x
- Watch dog Library
-   pip install watchdog

CONFIGURATION:

Before running the script, you need to configure the following variables:

source_dir: The directory where the script will monitor and move files from (e.g., "/Users/username/Downloads").
Destination directories for file types:

source_dir_Images: Directory for images (e.g., "/Users/username/Documents/Images").
source_dir_SFX: Directory for sound effects (e.g., "/Users/username/Documents/SFX").
source_dir_Movies: Directory for movies (e.g., "/Users/username/Documents/Movies").
source_dir_Music: Directory for music (e.g., "/Users/username/Documents/Music").
source_dir_Pdf: Directory for PDFs (e.g., "/Users/username/Documents/Pdf").
Make sure these paths are set to match your local directory structure

USAGE:

Clone or download the script.
Modify the source_dir and destination folder paths to match your system.
Run the script:

python3 auto.py
The script will begin monitoring the source directory. Any new files or changes will trigger the sorting and movement process.
The first time running all files already in the directory examined will not move until a new change is made, after that only new files added to the directory will transfer.

EXAMPLE OUTPUT:

When a file is moved, the log might look like:

2024-10-18 14:34:56 - Moving file 'song.mp3' to 'Music/song.mp3'
2024-10-18 14:34:57 - File 'photo.jpg' moved to 'Images/photo.jpg'



Stopping the Script
You can stop the script by pressing CTRL+C in the terminal. The script will shut down the monitoring process.

AUTHOR:
Donovan Thomas


