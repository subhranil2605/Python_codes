import time
import pydicom as dicom
import concurrent.futures
import numpy as np
from PIL import Image
import os
from pathlib import Path


def get_files(direc: str, file_type: str):
    files_ = []
    for (root, dirs, files) in os.walk(direc, topdown=True):
        if files:
            for f in files:
                if os.path.splitext(f)[1] == file_type:
                    path = os.path.join(root, f)
                    files_.append(path)
    return files_


dcm_files = get_files('raw_mci', '.dcm')
size = len(dcm_files)

t1 = time.perf_counter()


# converting image
def convert(dcm):
    ds = dicom.read_file(Path(dcm)).pixel_array.astype(float)
    final_image = Image.fromarray(np.uint8((np.maximum(ds, 0) / ds.max()) * 255))
    new_filename = Path(dcm.replace('.dcm', '.jpg')).name
    save_dir = "F:/Project_CNN/python_helper/processed_mci/" + new_filename
    final_image.save(Path(save_dir))
    print(f"{new_filename} : converted!")


# main function
if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(convert, dcm_files)

    t2 = time.perf_counter()
    print(f"it takes {t2 - t1} seconds!")
