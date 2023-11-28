import os
import shutil

def organize_downloads_folder(folder_path):
    # List all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Create folders for different file types
    image_folder = os.path.join(folder_path, 'Images')
    document_folder = os.path.join(folder_path, 'Documents')
    other_folder = os.path.join(folder_path, 'Other')

    for file in files:
        file_path = os.path.join(folder_path, file)

        # Check the file type and move to the corresponding folder
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            move_to_folder(file_path, image_folder)
        elif file.lower().endswith(('.pdf', '.doc', '.docx', '.txt')):
            move_to_folder(file_path, document_folder)
        else:
            move_to_folder(file_path, other_folder)

def move_to_folder(file_path, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Move the file to the destination folder
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

if __name__ == "__main__":
    downloads_folder_path = "c:/Users/majd-/Downloads"
    organize_downloads_folder(downloads_folder_path)
