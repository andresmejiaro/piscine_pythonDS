import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    assert isinstance(family, list), "Not a list"
    family = np.array(family)
    print(f"My shape is {family.shape}")
    to_return = family[start:end]
    print(f"My new shape is {to_return.shape}")
    return to_return.tolist()
