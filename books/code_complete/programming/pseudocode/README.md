# Pseudocode Programming Process

#### The point is to rise above the cycle of hacking something together and running to see if it works

"Compiling something before you're sure your program works is often a symptom of the hacker mindset"

## Why Pseudocode

* Makes reviews easier
  * Dont need to slog through code
* Supports idea of iterative refinement
  * At high level design, can catch high level errors
  * At mid-level, can cathc logical errors
  * No overlap so easy to focus
* Pseudocode makes changes easier
  * A few lines of pseudocode is easier to change than a page of code
* Pseudocode minimizes commenting effort
* Pseudocode is easier to maintain than other forms of design documentation

## Guidelines

* Use english statements that precisely define specific operations
* Avoid syntactic elemts from the target language
  * You're writing pseudocode to avoid syntactic elements lmao
* Write pseudocode at the level of intent
  * Describe the maning of the approach
  * NOT how it will be implemented
* Write pseudocode at low enough level that generating code from it will be nearly etomic
  * If pseudocode is at too high of a level, it cal gloss over problematic details in the code

## High Level Pseudocode

### 1) Start with the general and work towards something more specific

* Most general is the header comment of a routine describing it
  * Trouble wriging the statement is a warning that you need to understand the routines role better
  * If its hard to summarize, assume something is wrong

### 2) Think about the data

* Good to think about the major pieces of data before logic

### 3) Check pseudocode

* Take a step back and just think about it

### 4) Ask someone else to look at it or have you explain it to them

* People are more willing to review a few lines of pseudocode than 35 lines of C (lmaoo)

### 5) Make sure you have an easy and comfortable understanding of the routine

### 6) Iterate though several ideas

* Keep the best

## [Steps in Creating a Class](./CLASS.md)

## [Steps in Creating a Routine](./ROUTINE.md)

## [Actually Coding the Routine](./CODING.md)

## [Checklists](./CC_CHECKLIST.md)

* [Code Complete Checklist](./CC_CHECKLIST.md)
