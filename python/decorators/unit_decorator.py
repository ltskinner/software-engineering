
""" https://realpython.com/primer-on-python-decorators/ """

import math
import functools
import pint


def set_unit(unit):
    """Register a unit on a function"""
    def decorator_set_unit(func):
        func.unit = unit
        return func
    return decorator_set_unit


@set_unit("cm^3")
def volume(radius, height):
    return math.pi * radius**2 * height


""" Using external library converts inside decorator """
def use_unit(unit):
    """Have a function return a Quantity with given unit"""
    use_unit.ureg = pint.UnitRegistry()
    def decorator_use_unit(func):
        @functools.wraps(func)
        def wrapper_use_unit(*args, **kwargs):
            value = func(*args, **kwargs)
            return value * use_unit.ureg(unit)
        return wrapper_use_unit
    return decorator_use_unit

@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration



if __name__ == "__main__":
    print(volume(4, 5))
    print(volume.unit)
