import os

# Specify the file path and name
file_path = "/path/to/file"
file_name = "filename.ext"

# Construct the full file path
full_path = os.path.join(file_path, file_name)

# Hide the file by changing its attributes
os.system("attrib +h " + full_path)
