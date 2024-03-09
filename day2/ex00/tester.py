from give_bmi import give_bmi, apply_limit


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    ## noncoforming
    try:
        height = [2.71, 1.15, 10]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
    except AssertionError as e:
        print(e)
    ## non valid values
    try:
        height = [2.71, 1.15, 10]
        weight = [165.3, 38.4, "pear"]
        bmi = give_bmi(height, weight)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
