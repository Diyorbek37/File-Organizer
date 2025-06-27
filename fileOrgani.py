import os
import shutil

file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Gif": [".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".tar"],
    "Musics": [".mp3", "wav"],
    "Other": [],
    }

folder_path = input("Enter foldder path. ")

if not os.path.isdir(folder_path):
    print("Invalid folder path!")
else:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    category_path = os.path.join(folder_path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, category_path)
                    moved = True
                    break
            if not moved:
                other_path = os.path.join(folder_path, "Others")
                os.makedirs(other_path, exist_ok=True)
                shutil.move(file_path, other_path)
print("Files organized seccessfully!")




