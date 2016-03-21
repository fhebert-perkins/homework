def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.
    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result
def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    
    if c() == True:
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return False

def t():
    0

def f():
    1

print (with_if_function())
print (with_if_statement())

"""Having some confusion with the main question of this problem. I would like some help/advice."""
