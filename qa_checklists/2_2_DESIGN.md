# 2.2 - Design

## Abstract Design Goals

### General Goals

* [ ] Issues identified in the architecture are addressed
* [ ] Design is stratified into layers
* [ ] You are happy with how the system has been decomposed
  * [ ] subsystems
  * [ ] packages
  * [ ] classes
  * [ ] routines
* [ ] Classes are designed for minimal interaction with each other?
* [ ] Classes and subsystems designed such that they could be used in other systems
* [ ] Program will be easy to maintain
* [ ] Design is lean
* [ ] Design uses standard techniques
  * [ ] Nothing exotic
  * [ ] Nothing hard to understand
* [ ] Design minimizes complexity
  * [ ] Accidential
  * [ ] Essential

### Practices

* [ ] Has the best design out of several iterations been selected?
  * [ ] several iterations actually done
* [ ] System has been decomposed in several different ways
  * [ ] decomposed one way
  * [ ] decomposed another
* [ ] System been approached
  * [ ] Top-down
  * [ ] Bottom-up
* [ ] Rapid prototypes for
  * [ ] Risky components of the system
  * [ ] Unfamilliar components
* [ ] Design reviewed by others
  * [ ] Formally or informally
* [ ] Design is at the point where implementation is obvious
* [ ] Design work has been properly documented

### Essential Questions

* [ ] Has complexity been minimzed as much as possible?
* [ ] Has the design gone through several iterations?
* [ ] Has "What should I hide?" been asked numerous times?

### Core Goals

* [ ] Complexity is at an absolute minimum
* [ ] Design is as modular as possible
* [ ] Everything is as black boxed as possible
* [ ] Interfaces are simple and intuitive
* [ ] Functionality of each block is well defined

## Specific Design Principles

### Change

* [ ] Areas likely to change have been identified
* [ ] Areas likely to change have been separated into their own class or module
* [ ] Areas likely to change have highly abstract interfaces that the rest of the program can expect not to change
* [ ] Access routines are used instead of expecting a specific variable type

### Compartmentalization

* [ ] Information is effectively hidden so the brain doesnt have to deal with it
* [ ] Information is hidden to allow easy change
* Program abstracted at:
  * [ ] Routine interface level
  * [ ] Class interface level
  * [ ] Package interface level
* [ ] Communication paths are as narrow as possible

### Coupling

* [ ] Methods and routines have the absolute minimum number of parameters
* [ ] Method and routine interfaces lend itself to easy testing

### Failure

* [ ] Have created test cases that will break the routine being tested
* [ ] Extra time has been spent brain-storming more ways it could fail

### Control Flow Design

* [ ] Control flow decisions are hidden behind easily testable interfaces
* [ ] No functions harbor more than 1 control block
  * [ ] No nested `if` blocks
  * [ ] No nested `for` or `while` loops

### Data Design

* [ ] Connections to DBs are parameterized to allow for easy testing
* [ ] Operations on data are hidden behind abstract testable interfaces
* [ ] Expected states of data in each step of the program are testable

### Model Design

* [ ] Saving models is easy
* [ ] Retrieving models is easy
* [ ] Switching between version of models is easy
* [ ] Models live in very narrow scopes that dont inhibit easy testing of scaffolding and harnesses

### UX Design

* [ ] UX mock ups have been reviewed by the Client before implementing
* [ ] Package, module and routine breakouts mirror grouping of UX elements
* [ ] Have you showed the client as many different options as possible?

## Most Important Question

* [ ] Design is as simple as possible
