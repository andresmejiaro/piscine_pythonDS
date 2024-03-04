from load_image import ft_load
import numpy as np
from PIL import Image


def main():
    img = ft_load("animal.jpeg")
    if img is None:
        return
    print(img)
    (height, width, colors) = img.shape
    img2 = img[int(0.3 * height): int(0.7 * height),
               int(0.45 * width):int(0.8 * width)]
    img2 = np.mean(img2, axis=2)
    (height, width) = img2.shape
    print(f"The shape of the image afet slicing is {img2.shape}")
    print(img2)
    img3 = np.zeros(shape=(width, height))
    for i in range(height):
        for j in range(width):
            img3[j, i] = img2[i, j]

    realimg = Image.fromarray(img3)
    realimg.show()


if __name__ == "__main__":
    main()
