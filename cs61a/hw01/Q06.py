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
    total = 1
    print("Begin the hailstone!")
    print(n)
    while n != 1:
        if n%2==0:
            n=n/2
            print(int(n))
            total +=1
        elif n%2==1:
            n = (n*3)+1
            print(int(n))
            total +=1
    else:
        print("Total number of steps:", total)
hailstone(int(input("Input your hailstone number here: ")))