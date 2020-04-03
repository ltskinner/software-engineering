# Code Complete Classes Checklist

## Abstract Data Types

* [ ] Class interfaces evaluated as abstract data types

## Abstraction

* [ ] Class has a central purpose
* [ ] Class is well named
  * [ ] name describes central purpose
* [ ] Classes interface provides consistent abstraction
* [ ] Classes interface makes class usage obvious
* [ ] Class interface is properly abstracted
  * [ ] class is a proper black box
  * [ ] dont have to think about how services are implemented
* [ ] Class complete enough so other classes dont need to meddle with internal data
* [ ] Unrelated info moved out of the class
* [ ] Class has been subdivided into component classes as much as possible
* [ ] Class interface properly preserved after modification

## Encapsulation

* [ ] Class minimizes acceeeibility to its members
* [ ] Class avoids exposing member data
* [ ] Class hides implementation details as much as possible
* [ ] Class avoids making assumptions about its users
  * [ ] including its derived classes
* [ ] Class independant of other classes
  * [ ] (loosely coupled)

## Inheritance

* [ ] Only used to model "is a" relationships
* [ ] Calss documentation describes inheritance strategy
* [ ] Derived classes avoid overridding non-overridable routines?
* [ ] Common interfaces as high in the inheritance tree as possible
  * [ ] interfaces
  * [ ] data
  * [ ] behavior
* [ ] Inheritance trees fairly shallow
* [ ] Data members in the base class private rather than protected

## General Implementation

* [ ] Class contains about 7 data members or fewer
* [ ] Class minimizes direct and indirect routine calls to other classes
* [ ] Class only collaborates with another class when necessary
* [ ] All member data initialized in the constructor
* [ ] Class designed to use deep copies

## Key Points

* Class interface should provide consistent abstraction
* Class interface should hide something
  * System interface
  * Design decision
  * Implementation detail
* Containment is preferable to inheritance
  * Unless modling an "is a" relationship
* Inheritance is a useful tool - BUT - it adds complexity
* Classes are the primary tool for managing complexity
  * give their design as much attention as possible to accomplish that objective
