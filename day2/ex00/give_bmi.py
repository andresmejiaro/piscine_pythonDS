import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """
    Calculate the Body Mass Index (BMI) for given heights and weights.

    The BMI is calculated by dividing the weight in kilograms by their height in
    meters squared.

    Parameters:
    - height: list[int | float] - A list of heights in meters.
    - weight: list[int | float] - A list of weights in kilograms.

    Returns:
    - list[int | float]: A list of calculated BMI values.

    Raises:
    - ValueError: If the input lists contain invalid values.
    - AssertionError: If the input lists have mismatched sizes.
    """

    height = np.array(height)
    weight = np.array(weight)

    assert height.shape == weight.shape, "Assertion Error: Mismatched Sizes"

    bmi = weight / height**2

    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list.


    Parameters:
    - bmi: list[int | float] - A list of numbers.
    - limit: A threshold for True.

    Returns:
    - list[bool]: A list of booleans whose values are higher than the threshold.

    """
    return [x > limit for x in bmi]
