# Code Complete Defensive Programming Checklist

## General

* [ ] Routines protect themself from bad input data
* [ ] Assertions used to document assumptions
  * [ ] pre-conditions
  * [ ] post-conditions
* [ ] Error handling techniques specified by architecture or high-level design
* [ ] Favoring robustness or correctness specified by architecture or h-l d
* [ ] Barricades created
  * [ ] contain damaging effects of errors
  * [ ] reduce amount of code related to error processing
* [ ] Debugging aids used in code
* [ ] Debugging aids installed in a way that they can be easily activated or deactivated
* [ ] Proper amount of defensive programming
  * [ ] not too much
  * [ ] not too little
* [ ] Errors are difficult to overlook during development

## Exceptions

* [ ] Defined standardized approach for handling exceptions
* [ ] Considered alternatives to using exceptions
* [ ] Errors are handled locally
* [ ] Exceptions arent thrown in constructors or destructors
* [ ] Exceptions at appropriate levels of abstraction in their routines
* [ ] Each exception includes all relevant background info
* [ ] Code is free of empty catch blocks

### Security issues

* [ ] Input data checked for
  * [ ] buffer overflows
  * [ ] SQL injection
  * [ ] integer overflows
  * [ ] other malicious inputs
* [ ] All error-return codes checked
* [ ] All exceptions caught
* [ ] Error messages dont provide information that would help an attacker break into the system

## Key Points

* [ ] Defensive programming techniques make errors:
  * [ ] easier to find
  * [ ] easier to fix
  * [ ] less damaging to production code
* [ ] Assertions used to detect errors early
* [ ] Decision on how to handle errors has been made
