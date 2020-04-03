




"""Honestly this is cancer"""







"""Hypothesis is a library that lets you write tests that are
parameterized by a source of examples. It then generates simple and
comprehensible examples that make your tests fail, letting you find
more bugs with less work

This is weird, hitchikers guide example doesnt work
"""

from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_ints_are_commutative(x, y):
    assert x + y == y + y


if __name__ == "__main__":
    #test_ints_are_commutative() # yes this is supposed to not take args
    print("nope")


"""Bail, this isnt useful"""
