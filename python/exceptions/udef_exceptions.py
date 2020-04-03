
"""https://www.programiz.com/ \
python-programming/user-defined-exception

https://docs.python.org/3.6/tutorial/errors.html
"""

# Define python udef exceptions
"""Not sure why use this as base instead of Exception...
I think its to create unified parent for all the Exceptions
in a module, without all of them talking directly to source Exception
"""
class Error(Exception):
    """Base class for exceptions in this module"""
    pass


class ValueTooSmallError(Error):
    """Raised when input is too small
    
    Attributes:
        expression -- input expression that caused the error
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        """scruh...
        assert (expression), message
        """
        self.expression = expression # Param is just an eval to True lol
        self.message = message


class ValueTooLargeError(Error):
    """Raised when input is too large"""
    pass



number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError(i_num < number, "value is too small")
        elif i_num > number:
            raise ValueTooLargeError("help suh")
        break
    except ValueTooSmallError as e:
        print(e.message)
        print()
    except ValueTooLargeError:
        print("This is the value too large error message")
        print()

print("Done")

