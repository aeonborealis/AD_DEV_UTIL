import os
import shutil

def clean_desktop():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    for filename in os.listdir(desktop):
        file_path = os.path.join(desktop, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1]
            if file_extension in ['.lnk', '.url', '.webloc']:
                os.remove(file_path)
            else:
                new_path = os.path.join(desktop, file_extension[1:].upper(), filename)
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
                shutil.move(file_path, new_path)

if __name__ == '__main__':
    clean_desktop()
