
import os
import shutil

def organize_files(Folder):
    files = os.listdir(Folder)

    # Create folders
    folders = {
        "PDFs": [".pdf"],
        "Images": [".jpg", ".jpeg", ".png"],
        "Videos": [".mp4"],
        "Others": []
    }

    for folder in folders:
        os.makedirs(os.path.join(Folder, folder), exist_ok=True)

    counts = {
        "PDFs": 0,
        "Images": 0,
        "Videos": 0,
        "Others": 0
    }

    for file in files:
        path = os.path.join(Folder, file)

        if os.path.isdir(path):
            continue

        ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder, extensions in folders.items():
            if ext in extensions:
                shutil.move(path, os.path.join(Folder, folder, file))
                counts[folder] += 1
                moved = True
                break

        if not moved:
            shutil.move(path, os.path.join(Folder, "Others", file))
            counts["Others"] += 1

    print("\n--- Summary ---")
    for key, value in counts.items():
        print(f"{key}: {value}")


def rename_files(Folder):
    files = os.listdir(Folder)
    count = 1

    for f in files:
        old_path = os.path.join(Folder, f)

        if os.path.isdir(old_path):
            continue

        _, ext = os.path.splitext(f)
        new_name = f"file_{count}{ext}"
        new_path = os.path.join(Folder, new_name)

        os.rename(old_path, new_path)
        count += 1

    print("Files renamed successfully!")


# -------- MAIN --------
Folder = input("Enter folder to organize: ")
organize_files(Folder)

choice = input("Do you want to rename files? (yes/no): ").lower()

if choice == "yes":
    rename_folder = input("Enter folder to rename files: ")
    rename_files(rename_folder)