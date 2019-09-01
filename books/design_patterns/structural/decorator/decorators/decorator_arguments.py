
""" https://realpython.com/primer-on-python-decorators/ """


import functools

""" Repeats function num_times times """
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


""" Supercharged repeat that has optional parameters """
# _private, * forces all args to be keyword only, default num_times=2
def superpeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    
    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

@superpeat
def say_whee():
    print("Whee!")

@superpeat(num_times=3)
def supergreet(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    greet("bruhsev")

    say_whee()

    supergreet("super")


