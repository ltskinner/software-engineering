# CTL+F Checklist

Search each of the items in this list and correct accordingly

* [ ] `global`
  * **Get rid of global variables**
  * If they MUST exist, you MUST justify them without a shred of doubt
* [ ] `temp`
  * Do not use `temp` in variable names - find a better word or change the routine
* [ ] `main`
  * Typically, `main` is used in variable names when people start getting lazy
  * `if __name__ == '__main__':` is obviously **OK**
* [ ] `try`
  * Ensure that any try is **TRULY** neccessary
    * External interfaces - network, GPU, etx
  * If neccessary, **MUST BE CAUGHT** with valid Exception
  * Leverage `else` and `finally` when applicable
* [ ] `lambda`
  * There are rarely any good reasons to use a lambda function
  * Explicitly define the function and make a `unit test` instead
* [ ] `#`
  * Ensure your inline comments explain the `why`
  * Remove if explaining the `what` or the `how` - thats the codes job
* [ ] `).`
  * Part of larger `function1().bad().more_bad()` call chains
  * Get rid of these
