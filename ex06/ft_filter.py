def ft_filter(function, iterable):
    """
    Mimics the behavior of Python's built-in filter() function.
    Returns an iterable containing items for which the function evaluates to True.
    """
    return [item for item in iterable if function(item)]
