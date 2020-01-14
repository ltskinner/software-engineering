# Python

## General Artifacts

* [Classes](./CLASSES.md)
  * When to use
  * [Inheritance](./CLASSES.md#Inheritance) (Single, Multiple)

```python
super().__init__(length=length, width=length,
                 *args, **kwargs)
```

## Tools

### [Loggers](./logging)

```python
import logging
from logging.config import dictConfig

def get_logger(output_path, logging_level=logging.DEBUG):
    """
    logging.CRITICAL --> only critical
    logging.DEBUG --> all
    """
    logging_config = dict(
        version = 1,
        formatters = {
            'row_format': {
                'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
            }
        },
        handlers = {
            'console_logger': {
                'class': 'logging.StreamHandler',
                'formatter': 'row_format',
                'level': logging_level
            },
            'file_logger': {
              'class': 'logging.FileHandler',
              'formatter': 'row_format',
              'level': logging_level,
              'filename': output_path,
            }
        },
        root = {
            'handlers': ['console_logger'],
            'level': logging_level,
        },
    )

    dictConfig(logging_config)
    logger = logging.getLogger()
    return logger

logger = get_logger('./project.log')
logger.debug('often makes a very good meal of %s', 'visiting tourists')
```

### [Dates](./DATES.md)

```python
# datetime to string
str_time = now_time.strftime('%Y-%m-%d %H:%M:%S')

# datetime from string
dt_obj = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
```

### [argparse](./ARGPARSE.md)

```python
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--some_int', action='store',
                        type=int,
                        required=True,
                        default=42)
args = my_parser.parse_args()
print(args.some_int)
```

## [Networking](./networking)

* UDP
* TCP

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

### Packaging

* [setup.py example](./SETUP.md)
* [pypi distribution](./PYPI.md)

#### Anaconda

```
# ---- Creating new env ----
$ conda create -n {new_env} python=3.6

# ---- Exporting ----
$ pip freeze > requirements.txt

$ conda env export > environment.yml


# ---- Deleting ----
## First deactivate
$ conda deactivate
$ deactivate

$ conda remove --name {new_env} --all


# ---- Rebuilding env ----
## Build with whatever name is in .yml
# conda env create -f environment.yml

## -U = upgrade
$ pip install -r requirements.txt -U

```

#### __init__.py

```python
# Option 1
from . import first_module

# Option 2
from .second_module import second_function
```

#### Usage

```python
# Option 1
import package

package.first_module.first_function()
package.second_function()

# Option 2
from package.first_module import first_function
from package import second_function

first_function()
second_function()
```

```bash
$ python setup.py sdist bdist_wheel
```

### [Program Protection](./exceptions)

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

## What is good code?

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
