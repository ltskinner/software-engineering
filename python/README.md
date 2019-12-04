# Python

What is good code?

* Not code that uses every single feature
* Not even code that uses that many features of python
* Certain clarity to where and when a feature should be used
* Its code that doesnt waste the time of the person whos writing it

Leverage tools correctly:

* I have this pattern
  * Python has this mechanism
    * And everything very smoothly works

The language itself provides the core pieces you need and doesnt require you to create a new framework to make something happen

Python is a language oriented around some protocol

* There is some behavior
  * some syntax
    * some byte code
      * or some top level function
        * to do what you need

**Remember what the features are for, not their syntax**

## General Artifacts

* [Classes](./CLASSES.md)
  * When to use
  * [Inheritance](./CLASSES.md#Inheritance) (Single, Multiple)

```python
super().__init__(length=length, width=length, **kwargs)
```

## Tools

### [Loggers](./logging)

```python
# Instantiate your own logger
```

### [Dates](./DATES.md)

```python
# datetime to string
str_time = now_time.strftime('%Y-%m-%d %H:%M:%S')

# datetime from string
dt_obj = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
```

### [Exceptions](./exceptions)

```python
# Assertions
assert ('linux' in sys.platform)

# Raise
raise Exception(f'x should not exceed 5. The value was: {x}')

# udef Exceptions
class ValueTooSmallError(Exception):
    """Raised when input is too small
    
    Attributes:
        expression -- input expression that caused the error
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        """scruh...
        assert (expression), message
        """
        self.expression = expression # Param is just an eval to True lol
        self.message = message

if i_num < number:
    raise ValueTooSmallError(i_num < number, "value is too small")
```

### [Unit Testing](./unit_testing)

```python
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)


if __name__ == "__main__":
    unittest.main()
```

#### Run all tests

```bash
$ python -m unittest discover
```

### Building whls

#### [setup.py](./SETUP.md)

```bash
$ python setup.py sdist bdist_wheel
```

## Random Artifacts

### [Generators](./GENERATORS.py)

### [Decorators](./decorators)

```python
def decorator(func):
    @functools.wraps(func) # Preserves information on the original function
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
```

### [Context Managers](./CONTEXT.py) (`with ...`)

## [PyPi Distribution Sequence](./PYPI.md)



