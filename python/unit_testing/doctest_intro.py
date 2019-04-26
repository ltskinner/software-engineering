
"""Doctest searches for pieces of text that look like interactive
python sessions in docstrings, then executes those sessions to verify 
that they work exactly as shown

Not used to find obscure bugs, just to make sure things are working 

This one only makes noise if things are broken
"""

def square(x):
    """Return the square of x.

    >>> square(2)
    4
    >>> square(-2)
    4
    """

    return x * x


if __name__ == "__main__":
    import doctest
    doctest.testmod()

