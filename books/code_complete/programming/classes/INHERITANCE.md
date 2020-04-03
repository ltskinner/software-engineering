# Inheritance

## When to use

* If multiple classes share **common data** but not behavior
  * Create a common object that those objects can contain
* If multiple classes share **common behavior** but not data
  * Derive them from a common base class that defines the common routines
* If multiple classes share **common data and behavior**
  * Inherit from a common base class that defines the common data and routines
* **Inherit** when you want the base class to control your interface
* **Contain** when you want to control your interface

## Inheritance as a Whole

* When deciding to use, need to make several decisions:
  * For each member routine, will the routine be visible to the derived class?
  * Will it have a default implementation?
  * Will the default implementation be overridable?
  * For each data member (variables, named constants, etc), how will the data member be visible to the derived class?
* How to make these decisions:
  * Implement "is a" through public interface
    * If the derived class isnt going to adhere **COMPLETELY** to the same interface defined by the base class, inheritance is not the right technique
  * **"Design and document for inheritance, or prohibit it"**

## Inherited routines

* Abstract overridable routines
  * Derived class inherits from the routines interface, but not its imlpementation
* Overridable routine
  * Derived class inherits the routines interface and a default implementation, and is allowed to use the default implementation
* Non-overridable routine
  * Derived class inherits the routines interface and its default imementation and is not allowed to override the routines imlementation
* **Dont reuse names of non-overridable base-class routines in derived classes**

## Rules of Thumb

* Move common interfaces, data, and behavior as high as possible in the inheritance tree.
  * The higher you move these, the more easily derived classes can use them
* Be susplicious of classes of which there is only one inheritance
  * Single instances might indicate that the design confuses objects with classes
  * Can the variations of the derived class be represented in data rather than a distinct class?
* Be suspicious of bases classes of which there is only one derived class
* Be suspicious of classes that override a routine and do nothing inside the derived routine
* **Fix the base class to handle variations in derived**

## Multiple Inheritance

* **Is a thing but gets overly complex easily**
* **(stay away from it lmao)**
