from sys import argv

def main():
    try:
        assert len(argv) < 3, "Assertion Error: more than one argument is provided"
        if len(argv) == 1:
            return
        try:
            number = int(argv[1])
        except ValueError:
            raise AssertionError ("Assertion Error: argument is not an integer")
        if number %2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as error:
        print(error)
if __name__ == "__main__":
    main()