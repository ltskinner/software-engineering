
"""https://realpython.com/python-exceptions/"""

from raise_assert import assert_sys_platform

"""The try and except Block: Handling Exceptions"""

def past(func):
    def past_wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print("\n-- past try block -- ")
        return value
    return past_wrapper


@past
def example1():
    try:
        assert_sys_platform()
    except AssertionError as error:
        print(error) # error is the user coded assertion comment
        print("assert_sys_platform() was not executed")
        

@past
def example2():
    try:
        with open('file.log') as file:
            read_data = file.read()
            print(read_data)
    except FileNotFoundError as fnf_error:
        print(fnf_error)


"""Note, block passes after first exceptio is caught"""
@past
def mega_example():
    try:
        assert_sys_platform()
        with open('file.log') as file:
            read_data = file.read()
            print(read_data)
    except AssertionError as error:
        print(error) # error is the user coded assertion comment
        print("assert_sys_platform() was not executed")
    except FileNotFoundError as fnf_error:
        print(fnf_error)

example1()