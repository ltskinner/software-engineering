# Other Heuristics

### Aim for Strong Cohesion

Cohesion - how focused the class is

* Refers to how closely other routines in a class (or all the code in a routine) support a central focus
* Typically looked at the routine level
* Rebranded as **abstraction** at the class level

### Build Hierarchies

* Just like hierarchical understanding of the program
* Want to make things easier to grasp

### Formalize Class Contracts

* Give me `x, y, z` in these formats, and I will return `i, j, k`

### Assign Responsabilities

* Ask what each object should be responsible for

### Design for Test

* If modifying an object to make it easier to test, probably also improving the object itself

### Seek Failure Points

* Always look for ways the program could fail
  * Instead of just looking at the successes

### Choose Binding Time consciously

* The time a specific value is bound to a variable
* Code that minds early tends to be simpler, but less flexible

### Make Central Points of Control

### Consider Using Brute Force

* A brute force solution that works is better than an elagent one that doesnt

### Draw a Diagram
