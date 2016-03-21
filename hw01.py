#QUESTION 2
def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = -b +a
    else:
        f = b+a
    return f

#QUESTION 4
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

for x in range(1, 1000):
    print("working on %s..." % x)
    if largest_factor(x) != x-1:
        print(X, "doesn't work!")
        break
else:
    print("Works from 1-1000!")
    #This just tests for what I talked about in the last comment, and checks in a range from n-m, where in this example n=1 and m=1000
    #If it ever doesn't work, it will print(x, "doesn't work!") and break

#QUESTION 5
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
    if condition == True:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"

def t():
    "*** YOUR CODE HERE ***"

def f():
    "*** YOUR CODE HERE ***"

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

challenge_question_program = """
"*** YOUR CODE HERE ***"
"""
