
""" https://realpython.com/primer-on-python-decorators/ """

import functools


""" Stateful Decorators """
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1 # um where is this stored
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0 # defined under def so ok
    return wrapper_count_calls



""" Classes as Decorators """
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print(f"Current count is {self.count}")


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__ !r}")
        return self.func(*args, **kwargs)


#@count_calls
@CountCalls
def say_whee():
    print("Whee!")


if __name__ == "__main__":
    say_whee()
    say_whee()
    say_whee()


