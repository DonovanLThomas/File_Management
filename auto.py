import time
import os
from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "/Users/dono_1k/Downloads"
source_dir_Images = "/Users/dono_1k/Documents/Images"
source_dir_SFX = "/Users/dono_1k/Documents/SFX"
source_dir_Movies = "/Users/dono_1k/Documents/Movies"
source_dir_Music = "/Users/dono_1k/Documents/Music"
source_dir_Pdf = "/Users/dono_1k/Documents/Pdf"

def make_unique(destination, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(join(destination, name)):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name

def organize(destination, entry, name):
    if exists(join(destination, name)):
        unique_name = make_unique(destination, name)
        new_path = join(destination, unique_name)
        os.rename(entry.path, new_path)
    else:
        move(entry.path, destination)

class FileMover(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                if entry.is_file():
                    name = entry.name
                    if name.endswith((".wav", ".mp3")):
                        destination = source_dir_SFX if entry.stat().st_size < 25000000 or "SFX" in name else source_dir_Music
                    elif name.endswith((".mov", ".mp4")):
                        destination = source_dir_Movies
                    elif name.endswith((".jpg", ".jpeg", ".png", ".HEIC")):
                        destination = source_dir_Images
                    elif name.endswith((".pdf"):
                        destination = source_dir_Pdf
                    else:
                        continue
                    organize(destination, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = FileMover()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
