import numpy as np


def ft_invert(array: np.array) -> np.array:
    return 255 - array


def ft_red(array2: np.array) -> np.array:
    array = array2.copy()
    array[:, :, 1:] = array[:, :, 1:] * 0
    return array
# your code here


def ft_green(array2: np.array) -> np.array:
    array = array2.copy()
    array[:, :, 0] = array[:, :, 0] - array[:, :, 0]
    array[:, :, 2] = array[:, :, 2] - array[:, :, 2]
    return array
# your code here


def ft_blue(array2: np.array) -> np.array:
    array = array2.copy()
    array[:, :, 0] = 0
    array[:, :, 1] = 0
    return array
# your code here


def ft_grey(array2: np.array) -> np.array:
    array = array2.copy()
    array[:, :, 0] = array2[:, :, 1]
    array[:, :, 2] = array2[:, :, 1]
    return array


# from pimp_image import ft_blue, ft_green, ft_grey, ft_invert, ft_red
# import numpy as np
# from PIL import Image
# from load_image import ft_load


# def main():
#     img = ft_load("landscape.jpg")
#     if img is None:
#         return
#     realimg = Image.fromarray(ft_invert(img))
#     realimg.show()
#     realimg = Image.fromarray(ft_red(img))
#     realimg.show()
#     realimg = Image.fromarray(ft_green(img))
#     realimg.show()
#     realimg = Image.fromarray(ft_blue(img))
#     realimg.show()
#     realimg = Image.fromarray(ft_grey(img))
#     realimg.show()


# if __name__ == "__main__":
#     main()
