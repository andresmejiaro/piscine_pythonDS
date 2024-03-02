from sys import argv

def main():
    try:
        assertstring = "AssertionError: the arguments are bad"
        assert len(argv) == 3, assertstring
        try:
            max_length = int(argv[2])
        except ValueError:
            raise AssertionError(assertstring)
    except AssertionError as error:
        print(error)
        return
    
    first = argv[1].split(None)
    check_len =lambda x: len(x) > max_length
    second = [x for x in first if check_len(x)]
    print(second)


if __name__ == "__main__":
    main()
