import os
import shutil
from pathlib import Path

# Organize panna pora folder - Downloads
folder = Path.home() / "Downloads"

categories = {
    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".mp3": "Videos",
    ".zip": "Archives",
    ".py": "Code",
}

moved = 0
for file in os.scandir(folder):
    if file.is_file():
        ext = Path(file.name).suffix.lower()
        category = categories.get(ext, "Others")
        dest_folder = folder / category
        dest_folder.mkdir(exist_ok=True)
        dest = dest_folder / file.name

        try:
            # Same peru la file iruntha peru mathu
            if dest.exists():
                name = Path(file.name).stem + "_copy" + ext
                dest = dest_folder / name
            shutil.move(file.path, dest)
            print(f"Moved: {file.name} -> {category}/")
            moved += 1
        except PermissionError:
            print(f"Permission denied: {file.name}")
        except FileExistsError:
            print(f"Already exists: {file.name}")

print(f"\nTotal files relocated: {moved}")
