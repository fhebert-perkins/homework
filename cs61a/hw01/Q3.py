from operator import add, mul

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    
    return (max(add(mul(a,a),mul(b,b)),add(mul(a,a),mul(c,c)),add(mul(b,b),mul(c,c))))
    
print(two_of_three(1,2,3))