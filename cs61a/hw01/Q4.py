def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.
    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, 
...
    8
    """

    """returns a list of prime factors of n"""

    factors = [ ] 
    d = 1
    ns = ((n**2) -1) 
    for i in range(1,ns):
      if n % i == 0:
        factors.append(i)
        """ got stuck at the append part so I had to look up how to do it"""
        
    for h in factors:
        if i < n:
            d = i
    print (factors)
    return d
print (largest_factor(9))
"""It is not squaring the original number, can't figure out why"""
