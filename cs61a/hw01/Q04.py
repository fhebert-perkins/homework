def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    "*** YOUR CODE HERE ***"
    current = 0
    for x in range(1, n**2):
        if ((n**2)-1)%x==0 and x<n and current<x:
            current = x
    return current
    #An alternative to this would seem to be
    #def largest_factor(n):
        #return n-1
    #not 100% sure, but I ran a few numbers and this is the conclusion I've drawn

for x in range(1, 1001):
    print("working on %s..." % x)
    if largest_factor(x) != x-1:
        print(x, "doesn't work!")
        break
else:
    print("Works from 1-1000!")
    #This just tests for what I talked about in the last comment, and checks in a range from n-m, where in this example n=1 and m=1000
    #If it ever doesn't work, it will print(x, "doesn't work!") and break