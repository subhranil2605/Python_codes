import shutil, os
from pathlib import Path
import math


# source location
p = Path("D:/DighaImages")

# destination location
dest = Path("D:/digha_wp")


# creating a list where all the files' location is saved
files = []

# filtering .JPG files from the files
for file in p.iterdir():
    if file.is_file() and file.suffix == '.JPG':
        files.append(file)


# how many folder have to made if each folder contains maximum 30 files
max_number_files = 30
folder_number = math.ceil(len(files) / max_number_files)


# Creating the sub folders and copying files into them
# start index
start = 0
for i in range(folder_number):

    # name of the new folder
    name = f"{i+1}"

    # new folder's path
    new_path = dest.joinpath(name)
    print(new_path)

    # creating the subfolder if not exists
    if not new_path.exists():
        new_path.mkdir()

    # copying each file into each sub folder
    for f in files[start:start + max_number_files]:
        print(f"The file {f}", end="")
        shutil.copy(f, new_path)
        print(f" has been copied to {new_path}")
    print()

    # start index gets updated each time iteration happens
    start += max_number_files


    
