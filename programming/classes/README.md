# Classes

"Classes are your primary tool for managing complexity"

## Class Foundations: Abstract Data Types (ADTs)

* Collection of data and operations to do work on that data
* Without understanding that, easy to make classes that are just a conveient carrying case for loosely related data and routines
* With an understanding of ADTs, can create classes that are easier to implement and modify
* **Main goal is giving yourself the ability to work in the problem domain - not the low level implementation domain**

### Examples

* Light
  * turn on
  * turn off
* Fuel Tank
  * fill
  * drain
  * get capacity
  * get tank status

## ADTs and Classes

* One way to think of a class is an ADT plus inheritance and polymorphism
  * (same interface differing underlying data types)
  * --> __repr__, __edd__, etc
* Classes should implement one and only one ADT
  * If you cant determine what the ADT class implements, its time to reorganize the class into one or more well defined ADTs
* Provide service in pairs
  * If you have an operation, there is usually an opposite or inverse
* Make interfaces programmatic, not semantic
  * **Programatic** part consists of data types things enforced by compiler
  * **Semantic** part is the assumptions abbout how the interface will be used
    * Proper initialization
    * Sequence
    * this should be well documetned
    * look for ways to convert semantic elements to programmatic with asserts or other techniques
  * **Beware of erosion of the interfaces abstraction under modification**
  * **DONT ADD PUBLIC INTERFACE ROUTINES THAT ARE OUT OF LINE WITH ORIGINAL PURPOSE AND CLASS-IFICATION**

|           | Interface        |
| --------- |-----------------:|
| Good      |   NextEmployee() |
| Bad       | NextItemInList() |

## Good Encapsulation

* Minimize accessibility
  * Dont expose data members in public
    * Use getters and setters
  * Avoid putting private implementation details into a classes interface
  * Dont make assumptions about the classes users
    * Should be designed and implemented to adhere to the contract implied by the class interface
  * Dont put a routine into the public interface just because it only uses public routines
  * **Favor read-time convenience over write time convenience**
    * **Code is read far more times than it is written**
  * Dont do semantic violations
  * **It isnt abstract if you have to look at the underlying implementation to understand whats going on**

## Containment

"has a" relationships

* Containment is the simple idea that a class contains a primitive data element of an object
* More is written about inheritance b/c it is difficult, but Containment still slaps
* "has a"
  * employee has a phone number
  * has a name
  * has a tax ID
* Implement "has a" through private inheritance as a last resort
* Limit yourself ot 7+-2 data members

## [Ineritance](./INHERITANCE.md)

"is a" relationships

* Inheritance is the idea that one class is a specialization of another class
* The purpose of inheritance is to create simpler code by redefining a base class that specifies common elements of two or more derived classes
* Common elements can be
  * Routine interfaces
  * Implementations
  * Data members
  * Data types

## Member Functions and Data

### Guidelines

* Keep number of routines in a class as small as possible
  * Higher number of routines associated with higher fault rates
* Disallow implicitly generated member functions and operators you dont want
* Minimize the number of different routines called by a class
  * Higher fault rates correlate to the total number of routines called from within a class
  * The more classes a class uses, the higher its fault rates
* Minimize indirect routine calls to other classes
  * accounts.ContactPerson().DaytimeContactInfo().PhoneNumber = BAD
* Essentially:
  * Minimize the number of kinds of objects instantiated
  * Min number of different direct routine calls on uninstantiated objects

## Constructors

* Initialize all member data in all constructors
* Enforce singleton property by using a private constructor
* Prefer deep copies to shallow copies until proven otherwise

## Checklists

* [Code Complete Checklist](./CC_CHECKLIST.md)
