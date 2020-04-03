# Loops


## Creating Loops Easily

* Start with one case
* Write pseudocode in comments
* Code case with literals
* Indent it, and put a loop around it
* Replace literals with:
  * loop indexes
  * computed expressions
* Replace more literals
* Repeat as many times as needed

## Avoiding Problems

* Minimize the number of factors affecting the loop
* Treat inside of the loop as if it were a routine
  * Surrounding program knows the control conditions but not the contents
* Make loop termination obvious
* Dont have code that depends on a loop indexes final value
* Limit nesting to 3 levels

## Types of Loops

### While Loops

* Flexible - use when unknown how many times will execute
* Two types:
  * Test at the beginning
  * Test at the end

### For Loops

* Rigid - use when known how many times need to execute
* Good for simple activities that dont require internal loop controls

## Testing Loops

* Care about three cases of interest
  * The first case
  * An arbitrary middle case
  * The last case
* **CHECK ALL OF THESE**
