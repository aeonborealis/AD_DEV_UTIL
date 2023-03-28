import os
import shutil

def organize_files(directory):
    # Create a dictionary to store file extensions and their corresponding files
    file_dict = {}
    
    # Loop through all files in the directory and group them by extension
    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1].lower()
        if file_extension:
            if file_extension not in file_dict:
                file_dict[file_extension] = []
            file_dict[file_extension].append(filename)
    
    # Create a folder for each file extension and move the corresponding files to the folder
    for file_extension, files in file_dict.items():
        folder_path = os.path.join(directory, file_extension[1:])
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            src_path = os.path.join(directory, file)
            dst_path = os.path.join(folder_path, file)
            shutil.move(src_path, dst_path)
            print(f"Moved {file} to {folder_path}")
            
if __name__ == '__main__':
    directory = '/path/to/directory'  # Replace with the path to your directory
    organize_files(directory)
