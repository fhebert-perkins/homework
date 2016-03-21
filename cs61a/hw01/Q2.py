from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = (b * -1) + a
    else:
        f = b + a
    return f(a, b)
a_plus_abs_b(3, -5)
