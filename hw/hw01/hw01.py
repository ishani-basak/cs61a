from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # A check that you didn't change the return statement!
    >>> # You don't need to understand the code for this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # Check that your code consists of nothing but a return statement.
    >>> # You don't need to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return sub((x*x + y*y + z*z), (max(x, y, z)*max(x, y, z)))


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    f = 2
    while f <= n:
        if n % f == 0:
            return n // f
        f += 1


def limited(x, z, limit):
    """Logic that is common to invert and change."""
    if x != 0:
        return min(z/x, limit)
    else:
        return limit


def invert_short(x, limit):
    """Return 1/x, but with a limit.

    >>> x = 0.2
    >>> 1/x
    5.0
    >>> invert_short(x, 100)
    5.0
    >>> invert_short(x, 2)
    2

    >>> x = 0
    >>> 1/x  # Cannot divide by 0
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    >>> invert_short(x, 100)
    100
    >>> invert_short(x, 2)
    2
    >>> # Check that your code consists of nothing but a return statement.
    >>> # You don't need to understand the code of this test.
    >>> import inspect, ast
    >>> source = inspect.getsource(invert_short)
    >>> [type(x).__name__ for x in ast.parse(source).body[0].body]
    ['Expr', 'Return']
    """
    return limited(x, 1, limit)


def change_short(x, y, limit):
    """Return abs(y - x) as a fraction of x, but with a limit.

    >>> x, y = 2, 5
    >>> abs(y - x) / x
    1.5
    >>> change_short(x, y, 100)
    1.5
    >>> change_short(x, y, 1)
    1
    >>> x = 0
    >>> abs(y - x) / x # Cannot divide by 0
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    >>> change_short(x, y, 100)
    100
    >>> change_short(x, y, 1)
    1
    >>> # Check that your code consists of nothing but a return statement.
    >>> # You don't need to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(change_short)).body[0].body]
    ['Expr', 'Return']
    """
    return limited(x, abs(y - x), limit)


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
    count = 0
    while n!=1:
        print(n)
        if n%2==0: 
            n//=2
        else:
             n = n * 3 + 1
        count+=1
    print(1)
    return count+1


quine = ''
def quine_test():
    """
    >>> quine_test()
    QUINE!
    """
    import contextlib, io

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        exec(quine)
    quine_output = f.getvalue()
    if quine == quine_output:
        print("QUINE!")
        return
    print("Not a quine :(")
    print("Code was:   %r" % quine)
    print("Output was: %r" % quine_output)
    print("Side by side:")
    print(quine)
    print("*" * 100)
    print(quine_output)
    print("*" * 100)
