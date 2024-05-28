import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define source and destination directories
DOWNLOADS_DIR = os.path.expanduser('~/Downloads')
PHOTOS_DIR = os.path.expanduser('~/Pictures')

# List of file extensions to monitor
PHOTO_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

class PhotoMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Only handle files, not directories
        if not event.is_directory:
            file_name, file_extension = os.path.splitext(event.src_path)
            # Check if the file is a photo
            if file_extension.lower() in PHOTO_EXTENSIONS:
                self.move_file(event.src_path)

    def move_file(self, src_path):
        """Move the file from the Downloads directory to the Photos directory."""
        file_name = os.path.basename(src_path)
        dest_path = os.path.join(PHOTOS_DIR, file_name)
        shutil.move(src_path, dest_path)
        print(f"Moved: {src_path} to {dest_path}")

def start_monitoring():
    # Create the event handler
    event_handler = PhotoMoverHandler()
    # Set up the observer
    observer = Observer()
    observer.schedule(event_handler, path=DOWNLOADS_DIR, recursive=False)
    # Start the observer
    observer.start()
    print(f"Monitoring started on {DOWNLOADS_DIR}...")

    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_monitoring()
