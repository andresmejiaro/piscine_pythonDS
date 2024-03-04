from sys import argv


def character_to_morse(char: chr) -> str:
    morse_code_dict = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '/'}
    if char not in morse_code_dict.keys():
        raise AssertionError("AssertionError: the arguments are bad")
    return morse_code_dict[char]


def main():
    try:
        assertstring = "AssertionError: the arguments are bad"
        assert len(argv) == 2, assertstring
        abd = [character_to_morse(x) for x in argv[1].lower()]
        exit = "".join(abd)
        print(exit)
    except AssertionError as error:
        print(error)
        return


if __name__ == "__main__":
    main()
