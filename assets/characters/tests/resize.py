from PIL import Image
from os import listdir
from os.path import isfile, join


def downscale(origin,destination):
    files = [f for f in listdir(origin) if isfile(join(origin, f))]

    for image in files:
        img = Image.open(origin + '/' + image)
        img = img.resize((64,90))
        img.save(destination + '/' + image) 

downscale('./big_color','./small_color')
downscale('./big_norm','./small_norm')
