# System Protection

## Error Processing

* Is processing corrective or defective?
  * If defective, the program can continue processing as nothing happened or quit
* Is error detection active or passive?
  * Like can the system anticipate errors so the program can discard it?
    * Like user giving a number that’s too big
* How does the program propagate errors?
  * Discard data immediately?
  * Enter error processing state?
  * Wait until processing complete then notify?
* What error handling conventions are there?
  * Need to specify a single consistent strategy
* How will exceptions be handled? Need to address:
  * When code can throw an exception
  * Where they will be caught
  * How they will be logged
  * How they will be documented
  * Etc.
* Inside the program, at what level are errors handled?
  * Point of detection or pass to error handling class or up call chain?
* What is the level of responsibility of each class for validating its input data?
  * Is each class responsible for validating its own?
  * Is there a group of classes responsible for validating data?
  * Can classes at any level assume the data they receive is clean?
* Do you want to use your environments built in exception handling mechanism or build your own?

## Fault Tolerance

* Collection of techniques that increase a systems reliability by:
  * Detecting errors
  * Recovering from them, or
  * Containing bad effects
* Example for error in computing a square root
  * Have system back up to a point where it knew everything was all right and continue from there
  * Use auxiliary code if the answer from the primary code is wrong
  * Use a voting algorithm where three routines answers are compared
  * Replace erroneous values with phony values known to have no negative effects on the rest of the system

## Security

* Need code level security
* Perform threat modeling
* Have rules for handling
  * buffers
  * **untrusted data (user input, configs, external sources)**
  