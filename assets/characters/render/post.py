import skimage.io
import skimage.transform
import time
import numpy as np
from os import listdir
from os.path import isfile, join
import time
from tqdm import tqdm

origin = './blender_albedo'
destination = './final_albedo'
palette_path = './palettes/colors.png'

downscale_time = 0.0
reduce_colors_time = 0.0
get_colors_time = 0.0
count_colors_time = 0.0
index_colors_time = 0.0

def downscale(img):
    global downscale_time
    start = time.time()

    img = skimage.transform.resize(img,
                            (90, 64),
                            mode='edge',
                            anti_aliasing=False,
                            anti_aliasing_sigma=None,
                            preserve_range=True,
                            order=0)

    end = time.time()
    downscale_time += end - start
    return img


def reduce_colors(img, threshold):
    global reduce_colors_time
    start = time.time()

    colors = list()

    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            dist = float("inf")
            index = 0
            for pos, color in enumerate(colors):
                print(color)
                new_dist = np.linalg.norm(color-pixel)
                # print(new_dist)
                if new_dist < dist:
                    dist = new_dist
                    index = pos
            if dist > threshold:
                colors.append(pixel)
            else:
                img[y][x] = colors[index]

    end = time.time()
    reduce_colors_time += end - start
    return img


def get_colors(img):
    global get_colors_time
    start = time.time()

    colors = set()

    for y in img:
        for pixel in y:
            colors.add(tuple(pixel.tolist()))

    ret = np.asarray(list(colors))

    end = time.time()
    get_colors_time += end - start
    return ret


def count_colors(img):
    global count_colors_time
    start = time.time()

    ret = get_colors(img).shape[0]

    end = time.time()
    count_colors_time += end - start
    return ret


def index_colors(img, palette):
    global index_colors_time
    start = time.time()

    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            dist = float("inf")
            index = None
            for pos, color in enumerate(palette):
                new_dist = np.linalg.norm(color-pixel)
                if new_dist < dist:
                    dist = new_dist
                    index = pos
            img[y][x] = palette[index]

    end = time.time()
    index_colors_time += end - start
    return img

palette_img = skimage.io.imread(palette_path)
palette = get_colors(palette_img)
print("palette number of colours: ",count_colors(palette_img))



files = [f for f in listdir(origin) if isfile(join(origin, f))]

for image_path in tqdm(files):
    # print('------------------------')
    start = time.time()
    img = skimage.io.imread(origin + '/' + image_path)
    img = downscale(img)
    # print("original: ", count_colors(img))
    img = reduce_colors(img, 18)
    # print("reduced: ", count_colors(img))
    img = index_colors(img, palette)
    skimage.io.imsave(destination + '/' + image_path, img.astype(np.uint8))
    # print("indexed: ", count_colors(img))
    end = time.time()
print()
print("total time functions: ", downscale_time + reduce_colors_time + get_colors_time + count_colors_time + index_colors_time)
print("total time real: ", end-start)
print("downscale_time: ", downscale_time)
print("reduce_colors_time: ", reduce_colors_time)
print("get_colors_time: ", get_colors_time)
print("count_colors_time: ", count_colors_time)
print("index_colors_time: ", index_colors_time)
print("total images: ", len(files))