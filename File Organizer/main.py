## Made by Gekko

import os
import shutil

# Define the directory to organize
directory = 'File Organizer/files'

# Define the file type to folder mapping
file_type_mapping = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.html', '.css']
}

# Create folders if they don't exist
for folder in file_type_mapping.keys():
    folder_path = os.path.join(directory, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to their respective folders
def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder, extensions in file_type_mapping.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, folder, filename))
                    moved = True
                    break
            if not moved:
                # Move to 'Others' folder if the file type is not recognized
                others_folder = os.path.join(directory, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))

def main():
    organize_files(directory)
    print(f"Files in '{directory}' have been organized.")

if __name__ == "__main__":
    main()