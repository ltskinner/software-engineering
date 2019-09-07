# Chapter 11: Usability

"Any darn fool can make something complex; it takes a genius to make something simple" - Einstein

* Usability is concerned with how easy it is to use a system
* Areas include:
  * Learning system features
    * How can learning things be made easier?
  * Using a system efficiently
    * What can the system do to make the user more efficient
  * Minimizing the impact of errors
    * How can the system protect itself from user error
  * Adapting the system to user needs
    * How can the system be modified to make the users task easier
  * Increasing confidence and satisfaction
    * What does the system do to give the user confidence that the correct action is being taken?

## 11.1 Usability General Scneario

## 11.2 Tactics for Usability

### Separate the User Interface

* Abstract and make easy to drop in lots of prototypes
* Increase coherence, encapsulate well
* Restrict dependencies
* Defer binding
* MVC has become the dominant pattern
* Usability and modifiability are correlated

### Support User Initiative

* Cancel
  * System must be listening
* Undo
  * System must maintain previous states
  * Must account for reversible operations
* Pause/Resume
  * Good for long running operations
* Aggregate
  * If the same op is done on a bunch of low level objects, provide a way to batch and free the user from the drudgery

### Support System Initiative

* Maintain Task mModel
  * Task model determines the context so the system can have some idea of what the user is attempting and provide assistance
* Maintain User Model
  * Model explicitly represents the users knowledge of the system
  * Other metrics about the users specific behavior
* Maintain System Model
  * System maintains a model of itsself
  * Common manifestation is a progress bar

## 11.3 Usability Checklist

### Allocation of Responsibilities

* Assist user in:
  * Learning the system
  * Working efficiently
  * Adapting and configuring the system
  * Recovering from user errors

### Coordination Model + Data Model

* Make sure abstractions are provided to actually help the user accomplish tasks
