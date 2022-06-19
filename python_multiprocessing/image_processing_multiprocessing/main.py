import time
import concurrent.futures
import os
from pathlib import Path
from PIL import Image, ImageFilter


def getting_images_names(directory: Path, file_type: str) -> list:
    image_name_list: list = []
    for file_name in directory.iterdir():
        if file_name.suffix == file_type:
            image_name_list.append(file_name.name)
    return image_name_list


result = getting_images_names(Path(os.getcwd()), '.jpg')

t1 = time.perf_counter()
size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_image, result)

    t2 = time.perf_counter()

    print(f"Finished in {t2 - t1} seconds!!")
