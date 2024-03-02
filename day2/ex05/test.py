from pimp_image import ft_blue, ft_green, ft_grey, ft_invert, ft_red
import numpy as np
from PIL import Image
from load_image import ft_load

def main():
    img = ft_load("landscape.jpg")
    if img is None:
        return
    realimg = Image.fromarray(ft_invert(img))
    realimg.show()
    realimg = Image.fromarray(ft_red(img))
    realimg.show()
    realimg = Image.fromarray(ft_green(img))
    realimg.show()
    realimg = Image.fromarray(ft_blue(img))
    realimg.show()
    realimg = Image.fromarray(ft_grey(img))
    realimg.show()

if __name__ ==  "__main__":
    main()