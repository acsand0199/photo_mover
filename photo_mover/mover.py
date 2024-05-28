import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define source and destination directories
DOWNLOADS_DIR = r'C:\Users\Austin\Downloads'  # Update this path to the user's Downloads directory
PHOTOS_DIR = r'C:\Users\Austin\OneDrive - Essentia\Pictures'  # Update this path to the user's Pictures directory

# Ensure the directories exist
if not os.path.exists(DOWNLOADS_DIR):
    print(f"Error: The directory {DOWNLOADS_DIR} does not exist.")
    exit(1)

if not os.path.exists(PHOTOS_DIR):
    print(f"Error: The directory {PHOTOS_DIR} does not exist.")
    exit(1)

# List of file extensions to monitor
PHOTO_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

class PhotoMoverHandler(FileSystemEventHandler):
    """Event handler for moving photos when created in the Downloads directory."""

    def on_created(self, event):
        """Handle file creation event."""
        # Only handle files, not directories
        if not event.is_directory:
            file_name, file_extension = os.path.splitext(event.src_path)
            # Check if the file is a photo
            if file_extension.lower() in PHOTO_EXTENSIONS:
                self.move_file(event.src_path)

    def move_file(self, src_path):
        """Move the file from the Downloads directory to the Photos directory."""
        try:
            file_name = os.path.basename(src_path)
            dest_path = os.path.join(PHOTOS_DIR, file_name)
            shutil.move(src_path, dest_path)
            print(f"Moved: {src_path} to {dest_path}")
        except FileNotFoundError:
            print(f"File not found: {src_path}. It might have been moved or deleted before processing.")

def start_monitoring():
    """Start monitoring the Downloads directory for new photo files."""
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
