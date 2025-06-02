#Wrie a python program to print the contents of a directory using os module.

import os
# Specify the directory path (or use '.' for the current directory)
directory_path = "/Coding"

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:", directory_path)
for item in contents:
    print(item)
