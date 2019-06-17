# High Level Design Patterns

### Important notes

* Need to be careful and not change or force code too much to fit a pattern
* Only use a pattern when it is the correct solution for the task
  * Don't use one just cause you want to try it out

## Design Patterns

### Abstract Factory

* Supports creation of sets of related objects by specifying the kind of set, but nut the kinds of each specific object

### Adapter

* Converts the interface of a class into a different interface

### Bridge

* Builds an interface with an implementation in such a way that either can vary without the other varying

### Composite

* Consists of an object that contains additional objects of its own type so that client code can interact with top level objects and not concern itself with all the detailed objects

### Decorator

* Attaches responsabilities to an object dynamicaaly, without creating specific subclasses for each possible configuration of responsabilities

### Facade

* Provides an interface to code that wouldn't otherwise offer a consistent interface

### Factory Method

* Instantiates classes derived from a specific base class without needing to keep track of the individual derived classes anywhere but the Factory Method

### Iterator

* A server object that provides access to each element in a set sequentially

### Observer

* Keeps multiple objects in sync with one another by making objects responsible for notifying the set of related objects about changes to any member in the set

### Singleton

* Provides global access to a class that has one and only one instance

### Strategy

* Defines a set of algorithms or behaviors that are dynamically interchangable with each other

### Template Method

* Defines the structure of an algorithm but leaves some of the detailed implementation to the subclasses
