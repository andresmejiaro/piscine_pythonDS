from load_image import ft_load
import numpy as np
import plotly.express as px

def main():
    """
    Look at that raccon it is judging you!
    """
    img = ft_load("animal.jpeg")
    if img is None:
        return
    print(img)
    (height, width, colors) = img.shape
    img2 = img[int(0.3 * height): int(0.7 * height),
               int(0.45 * width):int(0.8 * width)]
    img2 = np.mean(img2, axis=2)
    print(f"The shape of the image afer slicing is {img2.shape}")
    print(img2)
    fig = px.imshow(img2, binary_string =True)
    fig.show()


if __name__ == "__main__":
    main()
