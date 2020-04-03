# Naming Specific Data Types

### Loop indexes

* If variable used outside of loop, dont use `i, j, k`
* Use a good name if loop is longer than a few lines

### Naming Status Variables

* Think of better name than `flag`
* Flags themselves should be thought of as status variables
  * `CONTROL_CHARACTER = 0X80`
  * `status = CONTROL_CHARACTER`

### Temporary Variables

* Dont name casually just because its temporary
* Usually lots of errors around temp variables

### Boolean Variables

* Done
  * Use to indicate whether something is done
  * Set to `False` before, `True` after
* Error
  * Set to `False` before, `True` after error found
* Found
  * Use to indicate whether a value has been found
  * Set to `False` before, `True` after found
  * Use for searching array, file, list, etc
* Can use "is" prefix
  * `isDone`
  * `isFound`
  * The second word must be meaningful
