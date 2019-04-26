
""" py.test is a "no-boilerplate" alternative to unittest

Main advantage is much less work than unittest
"""

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4


"""
$ pip install pytest
$ py.test

I actually kinda like this one
also, all testing files need to lead with:
    test_xxxxxx.py


https://docs.pytest.org/en/latest/cache.html
"""