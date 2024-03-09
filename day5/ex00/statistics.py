def check_arg(el):
    "raises if a single argument is not numeric"
    if not isinstance(el, (int, float)):
        raise ValueError("Argument is not numeric")


def error():
    "prints an useful error message"
    print("ERROR")
    return


def mean_n(vect):
    "Calculates the mean of a numeric vector raises if not enough data"
    if len(vect) == 0:
        raise ValueError("Not enough arguments")
    return sum(vect)/len(vect)


def quantile_n(vect, quant):
    "Calculates a quantile of a dataset"
    if len(vect) == 0:
        raise ValueError("Not enough arguments")
    md = int((len(vect))*quant)
    if md >= len(vect):
        md -= 1
    return sorted(vect)[md]


def var_n(vect):
    "Calculates a variance of a dataset"
    if len(vect) <= 1:
        raise ValueError("Not enough arguments")
    mean = mean_n(vect)
    return sum([(x - mean)**2 for x in vect])/(len(vect))


def std_n(vect):
    "Calculates stardard deviation of a dataset"
    return var_n(vect)**0.5


def mean_text(vect):
    "print the text of mean"
    try:
        print(f"mean : {mean_n(vect)}")
    except ValueError:
        error()


def median_text(vect):
    "print the text of median"
    try:
        print(f"median : {quantile_n(vect, 0.5)}")
    except ValueError:
        error()


def var_text(vect):
    "print the text of var"
    try:
        print(f"var : {var_n(vect)}")
    except ValueError:
        error()


def std_text(vect):
    "print the text of std"
    try:
        print(f"std : {std_n(vect)}")
    except ValueError:
        error()


def quartile_text(vect):
    "print the text of quartiles"
    try:
        print(f"quartile : {quantile_n(vect, 0.25)}, {quantile_n(vect, 0.75)}")
    except ValueError:
        error()


def print_one(kw, vect):
    "takes a keyword and prints what it is supposed to"
    opts = {"mean": mean_text, "median": median_text,
            "quartile": quartile_text, "std": std_text,
            "var": var_text}
    if kw in opts.keys():
        opts[kw](vect)


def ft_statistics(*args: any, **kwargs: any) -> None:
    "Calculate various statistics"
    try:
        vect = [x for x in args]
        [check_arg(x) for x in vect]
        for x in kwargs.values():
            print_one(x, vect)
    except ValueError:
        error()
        return


# ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
# tata="quartile")
# print("-----")
# ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
# print("-----")
# ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
#               ejfhhe="heheh", ejdjdejn="kdekem")
# print("-----")
# ft_statistics(toto="mean", tutu="median", tata="quartile")
