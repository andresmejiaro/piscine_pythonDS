from PIL import Image
from PIL import UnidentifiedImageError
import numpy as np


def ft_load(path: str) -> np.array:
    """
    Loads an image from a given file path and returns its numpy array
    representation.

    Opens an image file, converts it to a numpy array, and prints its shape.
    Handles errors for file not found, permission issues, and unidentified
    images, printing relevant error messages.

    Parameters:
    - path (str): File path of the image to load.

    Returns:
    - np.array: Numpy array of the image if successful, None otherwise.
    """
    try:
        img = Image.open(path)
        img_array = np.array(img)
        print(f"The shape of the image is: {img_array.shape}")
        print(f"Image format is {img.format}")
        return img_array
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except UnidentifiedImageError as e:
        print(e)

    return None