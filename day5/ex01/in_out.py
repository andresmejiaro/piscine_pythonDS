
def square(x: int | float) -> int | float:
    "good ol' square"
    return x**2


def pow(x: int | float) -> int | float:
    "good ol' thing...."
    return x**x


def outer(x: int | float, fun) -> object:
    "statics in python"
    def inner() -> float:
        inner.static_var = fun(inner.static_var)
        return inner.static_var
    inner.static_var = x
    return inner


# # %%
# my_counter = outer(3, square)
# print(my_counter())
# print(my_counter())
# print(my_counter())
# print("---")
# another_counter = outer(1.5, pow)
# print(another_counter())
# print(another_counter())
# print(another_counter())
# # %%
