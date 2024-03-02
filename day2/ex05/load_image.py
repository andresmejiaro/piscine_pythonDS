from PIL import Image
from PIL import UnidentifiedImageError
import numpy as np

def ft_load(path: str) -> np.array: 
    try:
        img = Image.open(path)
        img_array = np.array(img)
        print(f"The shape of the image is: {img_array.shape}")
        return img_array
    except FileNotFoundError as e:
        print(e)
    except PermissionError as e:
        print(e)
    except UnidentifiedImageError as e:
        print(e)

    return None