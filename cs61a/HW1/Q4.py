def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, 
...
    8
    """
    factors = []
    gf = 1
    nt = ((n**2) - 1)
    for f in range(1,nt):
        if nt % f == 0:
            factors.append(f)
    for i in factors:
        if i < n:
            gf = i
    print(factors)
    return gf
print(largest_factor(4))
print(largest_factor(9))
