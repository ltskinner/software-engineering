
"""https://realpython.com/python-exceptions/"""

"""Else

Using the else statement, you can instruct a program to execute a 
certain block of code only in the absence of exceptions.

Aka:
else:
    run this if no exceptions
"""

from raise_assert import assert_sys_platform
from try_except import past

def assert_is_windows():
    import sys
    assert ('win32' in sys.platform), "Not windows machine"

@past
def else_example():
    try:
        #assert_sys_platform() # else: wont run
        assert_is_windows() # else: does run
    except AssertionError as error:
        print(error)
    else:
        print('Executing the else clause')


"""Finally

Always runs at the end of a try block
"""
@past
def finally_example():
    try:
        #assert_sys_platform() # else: wont run
        assert_is_windows() # else: does run
        #raise Exception("is windows") # kills everything lmao
    except AssertionError as error:
        print("---")
        print(error)
        print("---")
    else:
        print('Executing the else clause')
    finally:
        print('Cleaning up, regardless of any exceptions encountered')
        print('This also runs after the else: block')

finally_example()
