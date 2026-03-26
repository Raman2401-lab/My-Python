''' Q. write a python program to print the contents of a
       directory using the os module. Search online for the function which does that.
'''

import os

# Specify the directory path
directory_path = "/PYTHON COURSE"

# Get list of files and directories
contents = os.listdir(directory_path)

# Print each item
print("Contents of directory:")
for item in contents:
    print(item)