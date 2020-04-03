
"""https://www.youtube.com/watch?v=cKPlPJyQrt4"""

import time

"""
There is always some top-level sytax
    - like a function
that implements
    - some __method__

XXXXXXX() -> __call__
"""

def add1(x, y):
    return x + y

class Adder:
    def __call__(self, x, y):
        return x + y
add2 = Adder()

# Are these two not the same?


def compute():
    """This will always take 5 seconds.
    Regardless of our answer being the first or the last value

    This will also take up 10 memory units.
    Regardless of our answer being the fist value
    
    This behavior is called "eager"
    """
    rv = []
    for i in range(10): # what if 14 billion?
        time.sleep(.5) # What if 5 seconds??
        rv.append(i)


class Compute:
    """
    def __call__(self):
        rv = []
        for i in range(10):
            time.sleep(.5)
            rv.append(i)
        return rv
    """
    # Would never want to actually write this haha
    def __iter__(self):
        self.last = 0
        return self
    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        time.sleep(.5)
        return rv

compute = Compute()


"""Same as Compute()"""
def new_compute():
    for i in range(10):
        time.sleep(.5)
        yield i


# ----------------------------------------------------------
"""
Subroutines:
Any piece of executable code that run from one single starting point
to one single ending point. They run, theyre done.

Interleave user-code with library based generator
"""

first = second = last = print()

class Api:
    def run_this_first(self):
        first()
    def run_this_second(self):
        second()
    def run_this_last(self):
        last()

def api():
    first()
    yield # Returns control to user
    second()
    yield
    last()