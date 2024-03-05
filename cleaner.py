import tkinter as tk
from tkinter import ttk, filedialog
import os
import shutil
from ttkthemes import ThemedTk

def organize_files(directory_path):
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    image_folder = os.path.join(directory_path, 'Images')
    document_folder = os.path.join(directory_path, 'Documents')
    installer_folder = os.path.join(directory_path, 'Installers')
    other_folder = os.path.join(directory_path, 'Other')

    for file in files:
        file_path = os.path.join(directory_path, file)

        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            move_to_folder(file_path, image_folder)
        elif file.lower().endswith(('.pdf', '.doc', '.docx', '.txt')):
            move_to_folder(file_path, document_folder)
        elif file.lower().endswith(('.exe')):
            move_to_folder(file_path, installer_folder)
        else:
            move_to_folder(file_path, other_folder)

def move_to_folder(file_path, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    shutil.move(file_path, os.path.join(destination_folder, os.path.basename(file_path)))

def get_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_var.set(directory_path)

def organize_files_in_selected_directory():
    directory_path = directory_var.get()
    if directory_path:
        organize_files(directory_path)
        show_completion_message()

def show_completion_message():
    # Destroy the main window
    root.destroy()

    # Create a new window for the completion message
    completion_window = ThemedTk(theme="equilux")
    completion_window.title("Organization Complete")

    # Display a message
    completion_label = ttk.Label(completion_window, text="Organization complete!")
    completion_label.pack(pady=20, padx=10)

    # Add a button to close the completion window and exit the application
    close_button = ttk.Button(completion_window, text="Close", command=completion_window.destroy)
    close_button.pack(pady=10, padx=20)

# Create the main window
root = ThemedTk(theme="equilux")
root.title("File Organizer")

# Create a StringVar to store the directory path
directory_var = tk.StringVar()

frame_a = ttk.Frame(width=370, height=50)
frame_a.pack(fill=tk.BOTH, expand=True)

# Create a button to open a directory dialog
choose_directory_button = ttk.Button(frame_a, text="Choose Directory", command=get_directory)
choose_directory_button.grid(row=0, column=0, padx=10, pady=10)

entry = ttk.Entry(frame_a, textvariable=directory_var, width=40)
entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button to organize files in the selected directory
organize_files_button = ttk.Button(frame_a, text="Organize Files", command=organize_files_in_selected_directory)
organize_files_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
