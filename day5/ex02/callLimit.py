# %%
def callLimit(limit: int):
    "A decorator to build a decorator"
    def decorator(func):
        "a decorator"
        def count_thing(*args, **kwargs):
            "static trick from last time"
            count_thing.static += 1
            errorstr = f"Error: <function {func.__name__} at "
            errorstr = errorstr + f"{hex(id(func))}> call too many times"
            if count_thing.static > limit:
                print(errorstr)
            else:
                func(*args, **kwargs)
        count_thing.static = 0
        return count_thing
    return decorator


# # %%

# @callLimit(3)
# def f():
#     print ("f()")
# @callLimit(1)
# def g():
#     print ("g()")
# for i in range(3):
#     f()
#     g()
