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

    validint_h = [isinstance(x,int) for x in height]
    validfloat_h = [isinstance(x,float) for x in height]
    valid_h = [a or b for (a,b) in zip(validint_h, validfloat_h)]
    validint_w = [isinstance(x,int) for x in weight]
    validfloat_w = [isinstance(x,float) for x in weight]
    
    valid_w = [a or b for (a,b) in zip(validint_w, validfloat_w)]
    if not all(valid_h) or not all(valid_w):
        raise ValueError("Value Error: Non valid height or weight")
    
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
    validint = [isinstance(x,int) for x in bmi]
    validfloat = [isinstance(x,float) for x in bmi]
    valid = [a or b for (a,b) in zip(validint, validfloat)]
    
    if not all(valid):
        raise ValueError("Value Error: Non valid bmi")

    return [x > limit for x in bmi]

# from give_bmi import give_bmi, apply_limit


# def main():
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))
#     ## noncoforming
#     try:
#         height = [2.71, 1.15, 10]
#         weight = [165.3, 38.4]
#         bmi = give_bmi(height, weight)
#     except AssertionError as e:
#         print(e)
#     ## non valid values
#     try:
#         height = [2.71, 1.15, 10]
#         weight = [165.3, 38.4, "pear"]
#         bmi = give_bmi(height, weight)
#     except ValueError as e:
#         print(e)


# if __name__ == "__main__":
#     main()
