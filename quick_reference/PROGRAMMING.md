# Programming Best Practices

* The primary goal is to minimize complexity
* Use effective variable, routine and Class names
* Don't write "clever" code
* Remember that code is read far more times than its written

## Naming Conventions

**If a name sounds dumb, change the functionality not the name**

* Constants
  * UPPERCASE_NAMES
  * MAGIC_NUMBERS, MAGIC_STRINGS
* Variables, functions, methods
  * lowercase, use_underscores
* Classes
  * UpperCamelCase
* Modules
  * module.py, module_name.py
* Packages
  * package, nounderscore

## Imports

* Thoughtfully ordered
* Spacing is used to group libraries by functionality
* Non-standard abbreviations `import xxx as reeee` are never entertained
* NEVER `from module import *`
* Prefer `import module` over `from module import (x, y, z, a, c, b, d)`
  * The `module.function()` convention is easier than tracing to an import

```python
from typing import Sequence, Dict      # Typing utils first

import os                              # Basic libraries first, increasing in complexity
import math
import numpy as np
import pandas as pd
from datetime import datetime

import requests                        # Grouped by functionality (data collection)
from bs4 import BeautifulSoup          # Uses libraries from previous group

import psycopg2                        # Grouped by (data storage)
import sqlalchemy                      # Uses libraries from previous group
import boto3

import nltk                            # Grouped by (data processing)
import sklearn                         # Uses libraries from previous group
import tensorflow as tf

import module_with_lots_of_functions   # Grouped by (udef), order these by functionality + complexity as well
from my_module import my_function      # Uses libraries from previous group
```

## Variables

### Do

* Use the name to express the **what**
  * A variable and its name should be the same thing
* Keep a low "live" time
  * Variable used close to where its defined
  * Makes refactoring easy

### Don't

* DONT USE GLOBAL VARIABLES
* Dont use names that look similar, but have different meanings
  * `client_recs` vs `client_reps`
* Dont use names that sound the same
  * `wrap` vs `rap`
* Dont use numbers in names
  * `file1`, `file2`
* Dont use commonly misspelled words
* Dont use `temp` under any circumstance
 * There is always a better way to express the variable

## Routines

Individual procedure with a *single purpose*

### Why create a function?

* Reduce complexity
* Avoid duplicating code
* To hide sequences
* To simplify boolean tests

### Do

* Use a name that expresses exactly what the function does
  * Use a strong verb followed by an object
  * `multiply_by_two()`
* Use a low number of parameters - <7
* Order parameters thoughfully
* Document assumptions in docstrings

### Don't

* Dont use vague terms in the name
  * `handle_data()` or `process_input()`
* Dont use chained function/method calls
  * `result = object.first_op().clean().transform()`
  * High defect rates in these lines

## Classes

**Classes are your primary tool for managing complexity**

### Do

* Use classes to work in the problem domain (instead of the implementation domain)
  * Light: `light.on(), light.off()`
  * Not: `bool: light_on = False`
* Have well defined class interfaces
* Hide as many implementation details as possible
* Have a low number of methods

### Don't

* Make assumptions about the user
  * What they know
  * What they dont know

## Program Protection

**Check data in input of functions, Classes**

### Error Handling

* For conditions you expect to occur
* if/else control

### Assertions

* For conditions that should never occur
* Things originating from inside the program

### Exceptions

* For conditions that should never occur
* Things originating externally
  * network, hardware

### Try Statements

* Minimize
* **NEVER** leave uncaught
  * Exception or trace is invaluable

## PEP8

* Focus on properly indenting code for readability
  * Inline operators
  * Function parameters
* 80 char lines dont always need to be followed

## Commenting

### Inline Comments

* Minimize
  * Use better artifact names to describe whats happening
* Only explain the **why**
  * Code should explain the **what** and the **how**

### Docstring Comments

* Elaborate on parameter and return types if not made clear by type hinting
* Use to explain the why - useful for definition peeks
* Use Google docstrings

## Type Hinting

* Use to remove ambiguity in parameter and return types

```python
def func(non_default: bool, optarg: bool = True) -> int:
    return -1

def deal_hands(
    deck: List[Tuple[str, str]]
) -> Tuple[
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
    List[Tuple[str, str]],
]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])
```

## Linters

* pylint
* pycodestyle
* mypy
