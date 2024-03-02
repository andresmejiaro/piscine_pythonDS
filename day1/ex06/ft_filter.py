
def ft_filter(func: function, itera):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if func is None:
        func = lambda x: x

    return iter([x for x in itera if func(x)])  
