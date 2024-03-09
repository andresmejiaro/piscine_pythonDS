class calculator:
    "A simple vector calculator"

    def __init__(self, vector: list):
        "vector creator"
        if not isinstance(vector, list):
            print("not a vector")
            self.vect = []
            return
        a = [isinstance(x, int) for x in vector]
        b = [isinstance(x, float) for x in vector]
        is_number = [x or y for (x, y) in zip(a, b)]
        if not all(is_number):
            print("non buildable elements in list")
            self.vect = []
            return
        self.vect = vector

    def __add__(self, object) -> None:
        """adding vector to a scalar (made a vector of same size),
        keeps result in"""
        self.vect = [x + object for x in self.vect]
        print(self.vect)

    def __mul__(self, object) -> None:
        """multiplying vector to a scalar keeps result in"""
        self.vect = [x * object for x in self.vect]
        print(self.vect)

    def __sub__(self, object) -> None:
        """substracting vector to a scalar (made a vector of same size),
        keeps result in"""
        self.vect = [x - object for x in self.vect]
        print(self.vect)

    def __truediv__(self, object) -> None:
        """multiplying vector to a inverse of scalar keeps result in"""
        self.vect = [x / object if object != 0 else float("NaN")
                     for x in self.vect]
        print(self.vect)

    def __str__(self):
        """printed the thing"""
        return self.vect.__str__()


#     from ft_calculator import calculator
# v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v1 + 5
# print("---")
# v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
# v2 * 5
# print("---")
# v3 = calculator([10.0, 15.0, 20.0])
# v3 - 5
# v3 / 5
