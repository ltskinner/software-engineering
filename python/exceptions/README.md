# Data Science Specific Program Protection

## if/else Error Handling

* Use your brain
* If youve seen something happen in dev/testing, create an if/else block to handle it

```python
def some_function_to_test_condition(condition):
    # remember - lead w/ positive
    if condition:
        return True
    else:
        return False

runtime_condition = True
if some_function_to_test_condition(runtime_condition):
    downstream_variable = 'positive_condition'
else:
    downstream_variable = 'negative_condition'

use_downstream_variable(downstream_variable)
```

## assert Assumptions

* Conditions that should **NEVER** occur
* Conditions that originate from **INSIDE** the program
* Use assertions to document assumptions **explicitly**

```python
# Not empty samples
assert (train_df.shape[0] != 0), "No samples!"

# Sequences of proper length
sample = train_df.values[0]
word_0_vec = sample[0]
assert (len(word_0_vec) == seq_len), "Sample length is not specified seq_len"

# Data is of proper type
assert (isinstance(word_0_vec[0], int)), "Sample is improper data type"

assert (word_0_vec[0] > -1 and word_0_vec[0] < 1), "Sample value is out of range"
```

## Exceptions

* Conditions that should **NEVER** occur
* Conditions that originate from **OUTSIDE** the program
  * network (requests, boto3)
  * hardware (gpu grabbing)

[reference this](https://github.com/ltskinner/software-engineering/blob/master/python/exceptions/else_finally.py#L37)
