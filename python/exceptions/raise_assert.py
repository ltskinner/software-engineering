
"""https://realpython.com/python-exceptions/"""


"""Exceptions vs Syntax Errors

Syntax errors occur when the parser detects an incorrect statement
print( 0 / 0 )) --> SyntaxError: invalid syntax

print(0/0) --> ZeroDivisionError: integer division or modulo by zero
THIS is an Exception Error.
    This type of error occurs whenever syntactically correct code
    results in an error.
You can use built-in exceptions and create self-defined ones as well.
"""

"""Raising an Exception

We can use:
    raise
to throw an exception if a condition occurs
"""
def raise_exception():
    x = 10
    if x > 5:
        raise Exception(f'x should not exceed 5. The value was: {x}')
    print("RUN DOES NOT CONTINUE AFTER RAISE")


"""The AssertionError Exception

Instead of waiting for a program to crash midway, you can start by 
making an assertion.
"""
def assert_sys_platform():
    import sys
    print(sys.platform) # win32
    assert ('linux' in sys.platform), "This code runs on Linux only"

