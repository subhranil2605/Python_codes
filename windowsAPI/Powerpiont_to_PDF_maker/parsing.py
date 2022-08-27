import argparse
import os
from ppt_to_pdf import presentation_to_pdf


def dir_path(path):
    
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


parser = argparse.ArgumentParser(description='Converting powerpoint ppts to pdf files')
parser.add_argument('-x', '--delete_file', action='store_true', help='delete the ppt file or not')
parser.add_argument('path', nargs='+', help='Path of a file or a folder of files.')
args = parser.parse_args()


def path_format(path):
    file_path = ''
    for i in path:
        file_path += f"{i} "
    return file_path.strip()


if __name__ == "__main__":
    path = path_format(args.path)    
    if args.delete_file: 
        presentation_to_pdf(path, True)
    else:
        presentation_to_pdf(path, False)
