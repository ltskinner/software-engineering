
""" https://realpython.com/primer-on-python-decorators/ """

import functools
from stateful_decorators import count_calls

def say_run(func):
    """Says the function is being called lmao
    Turns out count_calls is already doing this haha
    """
    @functools.wraps(func)
    def wrapper_say_run(*args, **kwargs):
        print(f"Running: {func.__name__!r}")
        return func(*args, **kwargs)
    return wrapper_say_run


def cache(func):
    """Keep cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache


@cache # better option is @functools.lru_cache(maxsize=4)
@count_calls
@say_run
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

if __name__ == "__main__":
    fibonacci(10)
    print("fib5:", fibonacci(5))
