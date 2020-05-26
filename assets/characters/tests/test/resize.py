import skimage.io
import skimage.transform
import numpy as np
from os import listdir
from os.path import isfile, join


def downscale(img):
    img = skimage.transform.resize(img,
                            (90, 64),
                            mode='edge',
                            anti_aliasing=False,
                            anti_aliasing_sigma=None,
                            preserve_range=True,
                            order=0)
    return img


def reduce_colors(img, umbral):
    colors = list()

    for y, row in enumerate(img):
        for x, pixel in enumerate(row):
            dist = float("inf")
            index = 0
            for pos, color in enumerate(colors):
                new_dist = np.linalg.norm(color-pixel)
                # print(new_dist)
                if new_dist < dist:
                    dist = new_dist
                    index = pos
            if dist > umbral:
                colors.append(pixel)
            else:
                img[y][x] = colors[index]
    return img


def get_colors(img):
    colors = set()

    for y in img:
        for pixel in y:
            colors.add(tuple(pixel.tolist()))

    return np.asarray(list(colors))


def count_colors(img):
    return get_colors(img).shape[0]


def index_colors(img, palette):
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
    return img


palette_path = './colors.png'
palette_img = skimage.io.imread(palette_path)
palette = get_colors(palette_img)
print(count_colors(palette_img))

origin = './in'
middle = './mid'
destination = './out'

files = [f for f in listdir(origin) if isfile(join(origin, f))]

for image_path in files:
    print('------------------------')
    img = skimage.io.imread(origin + '/' + image_path)
    img = downscale(img)
    print("original: ", count_colors(img))
    img = reduce_colors(img, 18)
    skimage.io.imsave(middle + '/' + image_path, img.astype(np.uint8))
    print("reduced: ", count_colors(img))
    img = index_colors(img, palette)
    skimage.io.imsave(destination + '/' + image_path, img.astype(np.uint8))
    print("indexed: ", count_colors(img))