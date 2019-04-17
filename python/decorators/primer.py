
""" https://realpython.com/primer-on-python-decorators/ """


from datetime import datetime


""" Inner Functions """
def parent(num):
    #print("Printing from parent() function")

    def first_child():
        #print("Printing from the first_child() function")
        return "first child"

    def second_child():
        #print("Printing from the second_child() function")
        return "second child"


    #second_child()
    #first_child()
    if num == 1:
        return first_child
    else:
        return second_child


""" Simple Decorators """
def my_decorator(func):
    def wrapper():
        print("Something before the function is called")
        func()
        print("Something after the function is called")
    
    return wrapper

""" Not nighttime """
def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass # do nothing as too late
    
    return wrapper

"""
# Original
def do_twice(func):
    def do_twice_wrapper():
        func()
        func()

    return do_twice_wrapper
"""

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        #func(*args, **kwargs) # Original
        return func(*args, **kwargs) # Updated to return a value
    
    return wrapper_do_twice


#@my_decorator
@do_twice
def say_whee():
    print("Whee!")

if __name__ == "__main__":
    say_whee()


