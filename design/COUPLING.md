# Coupling

Coupling decribes how tightly a class or routine is related to other classes or routines

## Keep coupling loose

* The goal is to create classes and routines with **small, direct, visible, and flexible relations** to other classes and routines - "loose coupling"
  * `sin()` - loosely coupled
  * `initVars(var1, var2, var3, var4)` - tightly coupled
    * With so many variables passed in, the calling module knows whats happening inside
* Avoid classes that depend on each others use of the same global data
  * These are even more tightly coupled

## Coupling Criteria

* **Size** - the number of connections b/w modules
  * Small is beautiful b/c its less work to connect other modules to a module that has a smaller interface
* **Visibility** - the priminence of the connection b/w two modules
  * Want to make connections as obvious and well defined as possible
* **Flexibility** - how easily you can change the connection
  * Want USB sticks, not wire and solder (lmaoo)

## Kinds of Coupling

* Simple-object coupling (Instantiate) - **OK**
  * A module is simple-objcet coupled to an object if it instantiates that object
* Object-parameter coupling
  * Object1 requires Object2 to pass it an Object3
  * Means that Object2 needs to know about Object3
* Semantic coupling - **BAD**
  * "The most insidious kind of coupling"
  * **Module makes use of another modules inner workings**
  * Arise from poor information hiding
