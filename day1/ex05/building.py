from sys import argv


def count_char_type(string: str, type: str) -> int:
    """
    counts the number of characters in a string of a given type

    Parameters:
    string (str): The string to count on
    type (str): String identifier of the characteristic to count

    Returns:
    int: Number of characters of a given type in the string
    """
    types = {"isupper": lambda x: x.isupper(),
             "islower": lambda x: x.islower(),
             "isnumeric": lambda x: x.isnumeric(),
             "isspace": lambda x: x.isspace()}

    if type not in types.keys():
        return 0

    return sum(map(types[type], string))


def main():
    try:
        assert len(
            argv) < 3, "Assertion Error: more than one argument is provided"
    except AssertionError as error:
        print(error)
        return
    if len(argv) == 1:
        user_input = input("Please enter a string: ")
    else:
        user_input = argv[1]
    length = len(user_input)
    spaces = count_char_type(user_input, "isspace")
    lower = count_char_type(user_input, "islower")
    numeric = count_char_type(user_input, "isnumeric")
    upper = count_char_type(user_input, "isupper")

    print(f"The text contains {length} characters:")
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{length - spaces - numeric - lower - upper} punctuation marks')
    print(f'{spaces} spaces')
    print(f'{numeric} digits')


if __name__ == "__main__":
    main()
