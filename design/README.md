# Design

“Once you understand that all other technical goals in software are secondary to managing complexity, many design considerations become straightforward.”

## Design Goals

* **Minimize complexity**
* Make design as **modular** as possible
* **Black box** everything
* **Simple interfaces**
* **Well defined functionality**

## Typical Challanges

* Need to solve part of the problem before the whole problem can be fully defined
* Design is mega sloppy
  * Lots of mistakes involved
* Design is about tradeoffs, priorities and restrictions
* There are many ways to design the same system
* Designs grow and change after spending more and more time with the code and seeing whats possible

## Primary goal is to Minimize Complexity

* **Goals**
  * To minimize the amount of a program you have to think about at any one time
  * To write code that compensates for inherent human limitations
  * To avoid situations where nobody completely understands the impact their code changes have
* **How to Attack Complexity?**
  * Minimize amount of essential complexity that anyone’s brain has to deal with at any one time
  * Keep accidental complexity at a minimum

## Design can be broken into several Levels

1. The software system - **designer**
2. Division into subsystems/packages - **designer**
3. Division into classes within packages - **designer**
4. Division into data and routines within packages - **programmer**
5. Internal routine design - **programmer**

* The **package divisons** need to account for
  * All major **subsystems**
    * Databases, UIs, business rules, interpreters, reporting engine
  * **Communications** between each package
    * **Make each subsystem meaningful by RESTRICTING communications**
    * **Allow communication on a NEED TO KNOW basis**
    * If all can communicate, there will be unintended consequences
    * Much easier to relax communication than make it more strict

## Common Heuristics

### [Find real world Objects](./OBJECTS.md)

* Modeling an OOP system effectively

### [Compartmentalize](../COMPARTMENTALIZATION.md)

* Abstract, Encapsulate and Hide Information effectively

### [Identify areas likely to Change](./CHANGE_AREAS.md)

* Protecting frozen functionality from changes

### [Keep Coupling loose](./COUPLING.md)

* The more easily the other modules can call a module, the more loosely coupled it is
  * `sin()` vs `initVar(var1, var2, var3, var4)`

### [Use Design Patterns when applicable](./CC_DESIGN_PATTERNS.md)

* Code level patterns

### [Other (just as important) Heuristics](./HEURISTICS.md)

## Common Design Practices

These are steps that can be taken to help produce a desirable design

* Iteration
  * Subsequent attempts are better than the previous
* Divide and Conquer
  * Break problem into different areas of concern to tackle individually
* Top-down
  * Guiding principal is the human brain can only focus on a certain amount of detail at a time
  * Essentiallty trying to decompose the problem
* Bottom-up
  * This is a more tangible approach, as Top-down can be too abstract
  * Need to keep to goals of the system always in mind
    * What does the system need to do?
    * What are the concrete objects and responsabilities at this level?
    * What common objects can I group?
    * Set up to the next level
* Experimental Prototyping
  * Two heads are better than one, so bounce ideas off others
    * Co-workers
    * Meetings with stakeholders
    * Ask a third party for help
    * Drawer your design and come back to it in a week once you've forgotten it

## Desirable Charactersistics of a Design

* **Minimal Complexity**
  * Avoid “clever” designs like the plague
  * Do make “simple” and “easy-to-understand” designs
* **As lean as possible**
  * "A book is finished when nothing more can be taken away, not when nothing more can be added"
* **Standardized techniques**
  * The more a system relies on exotic practices, the more intimidating it will be for someone to try and understand
* **Stratified properly**
  * Keep levels of decomposition stratified so the system can be viewed consistently from any single level
    * View at one level without dipping into other levels
  * Compartmentalize code by creating a good interface
* **Loosely coupled**
  * Connections among different parts of a program to a minimum
  * Good abstractions in class interfaces
  * Encapsulation
* **Has high fan-in**
  * High number of classes that a given class uses
  * Means a system has been designed to make good use of utility classes at the lower levels in the system
* **Has a low to medium fan-out**
  * The number of classes a given class uses is low (>7 is high)
* **Easily extensible**
  * Changes (“enhancements”) to the system don’t cause violence to the underlying parts
* **Is portable**
  * Can easily be moved to another environment
* **Easy to maintain**
* **Is reusable** (if desired)

## How much design is enough?

* Most problems arise from a lack of design detail - not too much of it
* Exploring other design options is a better use of time than polishing design documentation

| Situation | Pre-Construction Detail | Documentation Formality|
| --- |:-------------:|:-----:|
| Team has deep experience in applications area | low | low |
| Team has deep experience but is inexperienced in the applications area | medium | medium |
| Team is inexperienced | medium-high | low-medium |
| Team has moderate-high turnover | medium | - |
| Application is safety-critical | high | high |
| Application is mission-critical | medium | medium-high |
| Project is small | low | low |
| Project is large | medium | medium |
| Software is expected to have a short lifetime (weeks or months) | low | low |
| Software is expected to have a long lifetime (months or years) | medium | medium |
