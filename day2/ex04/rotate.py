from load_image import ft_load
import numpy as np
import plotly.express as px


def main():
    """ Now it is looking at you sideways!"""
    img = ft_load("animal.jpeg")
    if img is None:
        return
    print(img)
    (height, width, _) = img.shape
    img2 = img[int(0.3 * height): int(0.7 * height),
               int(0.45 * width):int(0.8 * width)]
    img2 = np.mean(img2, axis=2)
    (height, width) = img2.shape
    print(f"The shape of the image afer slicing is {img2.shape}")
    print(img2)
    img3 = np.zeros(shape=(width, height))
    for i in range(height):
        for j in range(width):
            img3[j, i] = img2[i, j]

    fig = px.imshow(img3, binary_string =True)
    fig.show()


if __name__ == "__main__":
    main()
