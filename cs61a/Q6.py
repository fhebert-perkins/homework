def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"

    length = 1
    print(n)
    while n != 1:
        length +=1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
    return length

print("The sequence is",hailstone(18), "parts long")
