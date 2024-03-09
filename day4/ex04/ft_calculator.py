
class calculator:
    "More a namespace than anything else"

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Did you know that if this is zero it means that the
        vectors are perpendicualar to one another?"""
        result = sum([a*b for (a, b) in zip(V1, V2)])
        print(f"Dot product is: {result}")
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Did you know that you can graphically add
        vectors using the paralellogram method?"""
        result = [a + b for (a, b) in zip(V1, V2)]
        print(f"Add vector is: {result}")
        return result

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Did you know that 42 cannot properly translate stuff to
        english"""
        result = [a - b for (a, b) in zip(V1, V2)]
        print(f"Sous vector is: {result}")
        return result


# from ft_calculator import calculator
# a = [5, 10, 2]
# b = [2, 4, 3]
# calculator.dotproduct(a,b)
# calculator.add_vec(a,b)
# calculator.sous_vec(a,b)
