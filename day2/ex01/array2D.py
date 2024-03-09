import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a list from start to end index and returns it.

    Validates that the input is a list, converts it to a numpy array to slice,
    and then returns the sliced part as a list. Prints the original and new
    shapes of the array.

    Parameters:
    - family (list): List to slice.
    - start (int): Starting index of slice.
    - end (int): Ending index of slice, exclusive.

    Returns:
    - list: Sliced list from start to end - 1.
    """
    assert isinstance(family, list), "Not a list"

    family = np.array(family)
    print(f"My shape is {family.shape}")

    to_return = family[start:end]
    print(f"My new shape is {to_return.shape}")

    return to_return.tolist()
