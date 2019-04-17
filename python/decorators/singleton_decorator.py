
""" https://realpython.com/primer-on-python-decorators/ """

import functools

def singleton(class_to_mod):
    """Make a class a Singleton class (only one instance)
    
    Singletons are like None, True or False
    Lets you use the 'is' keyword

    Using 'is' returns True for only objects that are the exact
    same instance.

    @singleton turns a class intoa  singleton by storing the first
    instance of the class as an attribute
    """
    @functools.wraps(class_to_mod)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = class_to_mod(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
class TheOne:
    pass


if __name__ == "__main__":
    first_one = TheOne()
    second_one = TheOne()

    if first_one is second_one:
        print("both are TheOne")
