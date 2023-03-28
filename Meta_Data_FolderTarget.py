import os
import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def add_metadata(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg') or filename.lower().endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            try:
                with Image.open(file_path) as im:
                    exif_data = im._getexif()
                    if exif_data:
                        exif = {
                            TAGS[k]: v
                            for k, v in exif_data.items()
                            if k in TAGS
                        }
                        if 'DateTimeOriginal' in exif:
                            date_time = datetime.datetime.strptime(exif['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
                            new_date = date_time.strftime('%Y:%m:%d %H:%M:%S')
                            os.system(f'setfile -d "{new_date}" "{file_path}"')
                            print(f"Added creation date metadata to {filename}")
                        else:
                            print(f"No creation date metadata found in {filename}")
                    else:
                        print(f"No EXIF data found in {filename}")
            except Exception as e:
                print(f"Error adding metadata to {filename}: {e}")

if __name__ == '__main__':
    folder_path = '/path/to/folder'  # Replace with the path to your folder
    add_metadata(folder_path)
