def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    maxFac = 0
    for i in range(1, n):
         if (n*n-1) % i == 0:
             maxFac = i
    return(maxFac)
    
print(largest_factor(4))

