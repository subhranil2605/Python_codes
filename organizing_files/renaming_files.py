import os
from pathlib import Path


# print(os.getcwd())
# F:/Deep-Learning-Codes/foundation

our_files = Path("F:/Deep-Learning-Codes/foundation")

# is the path a file?
print(our_files.is_file())

# is the path a directory
print(our_files.is_dir())

# parent of the file
print(our_files.parent)

# extension
print(our_files.suffix)


# Renaming files
for file in our_files.iterdir():

    # parent of the files
    directory = file.parent

    # extension of the files
    extension = file.suffix

    old_name = file.stem
    #"06_derivative_of_function_with_multiple_input.py"
    
    number = old_name.split("_")[0]
    name = "_".join(old_name.split("_")[1:])

    new_name = f"dl_{number}_{name}{extension}"
    print(new_name)

    # renaming the file
    file.rename(Path(directory, new_name))
    
    



























