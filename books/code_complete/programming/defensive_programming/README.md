# Defensive Programming

#### Take responsability for protecting yourself even when its the other drivers fault

"Defensive programming is about adopting the mindset that you have no idea what other drivers are going to do."

* Use error-handling for conditions you **expect** to occur
* Use assertions for conditions that should **never** occur - originating inside the program
* Use exceptions for conditions that should **never** occur - originating externally (hardware, network, etc)

**Too much defensive programming creates problems of its own**


## Protecting from Invalid Inputs

### 1) Check values of data from EXTERNAL SOURCES

* Allowable ranges
* Within tolerances
* Strings short enough
* Integer overflows
* Buffer overflows

### 2) Check values of all routine INPUT PARAMETERS

* Same as 1 but checking internal routine outputs

### 3) Decide how to HANDLE bad inputs

* Once detected, what do do with it?

## Assertions

* Allows a program to check itself while it runs
* Especially useful in large, complicated, and high reliability programs
* Guidelines:
  * Use error-handling for conditions you **expect** to occur
  * Use assertions for conditions that should **never** occur
  * Treat assertions as declared assumptions about the data
  * Avoid putting non value code in assertions (no routines)
  * Split assertions into:
    * Pre-conditions
    * Post-conditions

## Error-Handling Techniques

* Return a neutral value
  * a value thats known to be harmless
* Substitute the next piece of valid data
  * wait for next reading
  * go to next record in database
* Return the same answer as the previous time
* Substitute closest legal value
* Log a warning message to a file
* Return an error code
* Display an error message whnever the error is encountered
* Shut down

### Follow the same approach consistently through program

## Correctness vs Robustness

* Correctness means never getting an inaccurate result
  * **No result is better than an inaccurate one**
* Robustness means finding a way to keep the software operating
  * **Even if results are inaccurate**
* Safety-critical lean towards correctness
* Consumer applications favor robustness

## Exceptions

* Exceptions are specific means by which code can pass along errors or exceptional events
* Use for events that should **NEVER** occur
* Handle errors locally if possible
* Avoid empty try/catch blocks
* Standardize use of Exceptions
  * Standardize data types, object, etc
  * Consider project specific error class
    * Centralize and standardize logging and reporting
  * Define specific circumstances under which code is allowed to throw exceptions that wont be handled locally
  * Consider whether program really needs to handle exceptions period.

## Barricade Programs to Contain Damage Caused by Errors

* Create zones of code that expect incoming data to be raunchy
  * Outputs of these zones should be perfect
* Think like an operating room - need to sterilize the data

## Debugging Aids

* Dont automatically apply production constraints in dev
* **Be willing to trade speed and resource during dev in exchange for resources that can make developments go more smoothly**
* Use Offensive Programming
  * "A dead program does a lot less damage than a crippled one"
  * Make sure asserts abort the program
    * Make the problem painful enough to be fixed
  * Completely fill any memory allocated
  * Completely fill any files or streams allocated
  * Be sure code in case statements fail really hard
  * Fill an object with junk data before its deleted
  * Setup the program to email error log files to yourself

### Plan to remove debugging aids as well

* Use version control tools and build tools
* In dev, set build tool to include debug code
* In prod, set build tool to exclude

## Determining Ammount of Defensive Programming to Leave in Prod

* During dev, want errors to be loud and noticable
* On prod, want to be as quiet as possible

### Guidelines

* Leave in code that checks for important errors
  * Decide which areas can afford to have undetected errors and which cannot
* Remove code that chekcs for trivial erros (with trivial consequences)
* Remove code that results in hard crashes
* On prod, give users a chance to save work before crashing
* On prod, leave in code that helps programs crash gracefully
* Log erros for tech support personnel
* Make sure errors are friendly

## Checklist

* [Code Complete Checklist](./CC_CHECKLIST.md)
