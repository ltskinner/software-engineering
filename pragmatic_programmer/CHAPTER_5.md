# Chapter 5: Bend or Break

## Decoupling and the Law of Demeter

"Good fences make good neighbors"

### Minimize Coupling

* Symptoms of Coupling
  * "Simple" changes to one module end up propogating through unrelated modules in the system
  * Developers are afraid to change code because they dont know what will be affected

#### The Law of Demeter for Functions

* Methods of a class should only call methods that:
  * Belong to itself
  * Belong to parameters passed in
  * Belong to objects it created
  * Belong to any directly held objects (??)

### *Tip 36:* Minimize coupling between modules

* The more routines called by a method, the higher defect rates

## 27) Metaprogramming

"No amount of genius can overcome a preoccupation with detail"

### Dynamic Configurations

* Want to make systems highly configurable
* Need to make sure this is done through options
  * Not integration or engineering

### *Tip 37:* Configure, dont integrate

### *Tip 38:* Put abstractions in code, details in metadata

### Benefits to Metadata

* Forces you to decouple your design
  * Results in more flexible and adaptable program
* Forces you to make a more robust and abstract design by deferring details - deferring them all the way out of the program
* You can customize the application without recompiling it
  * You can also use this level of customization to provice easy workarounds for critical bugs in live production systems
* Metadata can be expressed in a manner thats much closer to the problem domain than a general purpose programming language
* You may even be able to implement several different projects using the same application engine, but with different metadata

### Dont Write Dodo Code

* Without metadata, code is not as flexible or adaptable as it could be
  * Like the dodo who did not adapt, your code will die

## 28) Temporal Coupling

* Things that need to be run in a certain order

### *Tip 39:* Analyze workflow to improve concurrency

* Drawing out whats actually happening, you will see many tasks that can be performed out of sequence

### *Tip 40:* Design using services

* Instead of components, create **services**
  * Independen, concurrent objects behind well defined and consistent interfaces

### Design for Concurrency

* Parallelization
* With linear code, its easy to make assumptions that lead to sloppy programming
* Thinking about this leads to cleaner interfaces as well

### *Tip 41:* Always design for concurrency

## 29) Its Just a View

"Still, a man hears \n What he wants to hear \n And disregards the rest \n La la la..."

### Model-View-Controller

* Model
  * The abstract data model representing the target object
  * The model has no direct knowledge of any views or controllers
* View
  * A way to interpret the model
  * It subscribes to changes in the model and logical events from the controller
* Controller
  * A way to control the view and provide the model with new data
  * It publishes events to both the model and the view

### *Tip 42:* Separate views from models

## 30) Blackboards

Like police detective blackboards

### Key features

* None of the detectives need to know of the existence of any other detectives
  * They simply watch the board for new info and add their findings
* The detectives may be trained in different disciplines, or even work in different states
  * But they all share the desire to solve the case
* Different detectives may come and go during the course of the process, and may work in different shifts
* There are no restrictions on what may be placed on the blackboard

### *Tip 43:* Use blackboards to coordinate workflow
