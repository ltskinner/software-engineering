# Routines

**What is a routine?** An individual method or procedure with a single purpose

## Good Attributes

* Descriptive name
* Is documented
* Good layouts with logical organization
* Input variable should not be changed
* No reading or writing to global variables
* Has single purpose
* Routine defends itself from bad data
* Numbers need to be in variables
* All parameters must be used
* No more than 7 parameters
* Parameters ordered thoughtfully

## Reasons to Create a Routine

* To reduce complexity
  * perfect for hiding information
  * pulls blocks out of nested loops or conditionals
  * moving code into its own section aids readability
* To avoid duplicating code
* To support subclassing
  * You need less new code to override a short, well factored piece of code
  * Long and poorly factored code is difficult to manage
* To hide sequences
  * forces sequences to happen in the correct order
* To simplify boolean tests
  * details of test are out of way
  * descriptive function name summarizes purpose
* To improve performance
  * can optimize in one place instead of many


## Routine Design

### Focus on cohesion

* High cohesion = `cosine()`
* Low cohesion = `cosineAndTan()`
  * b/c doing more than one thing

### Goal is to have each routine do one thing well and not do anything else

### Functional Cohesion

* When a routine performs one and only one operation
* Strongest and best kind

### Less good types

* **Sequential cohesion**
  * When routine contains operations that must be performed in a specific order
  * Share data from step to step
  * Dont make up a complete function when done together
* **Communicational cohesion**
  * Operations in a routine make use of the same data but arent related in any other way
* **Temporal cohesion**
  * When operations are combbined into a routine because they are done at the same time
  * `startup()`
  * `newEmployee()`
  * `shutDown()`

### Uacceptable types

* **Procedural cohesion**
  * When operations in a routine are done in a specific order
    * (like reading in auser input orderly?)
* **Logical cohesion**
  * When several operations are stuffed into the same routine and one of the operations is selected by a control flag
* **Coincidental cohesion**
  * When operations in a routine have no discernable relationship to each other

## Good Routine Names

### 1) Strong Verb

### 2) Followed by an Object

* Describe everything the routine does
  * and side effects
  * **If the name sounds silly, change the routine functionally**
* Avoid meaningless, vague or wishy-washy terms
  * `handleCalculation()`
  * `performServices()`
  * `outputUser()`
  * `processInput()`

## Routine Parameters

* Routine interfaces are some of the most error prone areas of a program
* Put input parameters in:
  * `1) input only`
  * `2) modify and output`
  * `3) output only`
* Use all parameters passed in
* Put status or error variables last
* Dont use routine parameters as working variables
  * Copy and assign to local
* Document assumptions about parameters
  * Whether param is input only, modified, or output only
  * Use of numeric parameters (feet, in, meter)
  * Meaning of status cudes and error vals
  * Ranges of expected values
  * Specific values that should never appear
* Pass variables and objects required to maintain its interface abstraction

## Operations that seem too simple to put into a routine

### A one liner containing 4 operations is much more readable if wrapped in a function

### How long can a routine be

Theoretically best max length is one screen, 50-150 lines

## Checklists

* [Code Complete Checklist](./CC_CHECKLIST.md)
