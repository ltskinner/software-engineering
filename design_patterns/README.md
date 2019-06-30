# Design Patterns

**Creational:** The process of **object creation**

**Structural:** The **composition** of classes or objects

**Behavioral:** Characterize the ways in which classes or objects **interact** and **distribute responsability**

**Class Scope:** Deal with relationships between classes and subclasses set at compile-time

**Object Scope:** Object relationships at run-time

|        | Creational    | Structural    | Behavioral |
| :------: | :------------- |:-------------| :-----|
| Class  | Factory Method | Adapter(*class*) | Interpreter|
| ... |  |  | Template Method |
| Object | Abstract Factory | Adapter(*object*) | Chain of Responsibility |
| ... | Builder | Bridge | Command|
| ... | Prototype | Composite | Iterator |
| ... | Singleton | Decorator | Mediator |
| ... |  | Facade | Memento |
| ... |  | Flyweight | Observer |
| ... |  | Proxy | State |
| ... |  |  | Strategy |
| ... |  |  | Visitor |

## Design Pattern Catalog

## Creational Patterns

Creational design patterns abstract the instantiation process. There purpose is to make the design more flexible - not necessarily smaller.

### [Abstract Factory](./creational/abstract_factory)

Provide an interface for creating families of related or dependent objects without specifying their concrete classes

### [Builder](./creational/builder)

Separate the construction of a complex object from its representation so that the same construction process can create different representations

### [Factory Method](./creational/factory)

Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

### [Prototype](./creational/prototype)

Specify the kinds of objects to create using a prototypical instance, and creating new objects by copying this prototype

### [Singleton](./creational/singleton)

Ensure a class only has one instance, and provide a global point of access to it

## Structural Patterns

Structural patterns are concerned with how classes and objects are composed to form larger structures. Mostly focused on inheritance to compose interfaces or implementations.

### [Adapter](./structural/adapter)

Convert the interface of a class into another interface that clients expect. Adapter lets classes work together that couldnt otherwise because of incompatible interfaces

### [Bridge](./structural/bridge)

Decouple an abstraction from its implementation so that the two can vary independently

### [Composite](./structural/composite)

Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects formally.

### [Decorator](./structural/decorator)

Attach additional responsabilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extended functionality.

### [Facade](./structural/facade)

Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher level interface that makes the subsystem easier to use

### [Flyweight](./structural/flyweight)

Use sharing to support large number of fine-grained objects efficiently

### [Proxy](./structural/proxy)

Provide a surrogate or placeholder for another object to control access to it

## Behavioral Patterns

Behavioral patterns are concerned with algorithms and the assignment of responsibilities between objects. They are focused with control flow and communication.

### [Chain of Responsibility](./behavioral/chain_of_responsibility)

Avoid coupling the sender of a request to its receiver by giving more than one object a change to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.

### [Command](./behavioral/command)

Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

### Interpreter

Given a language, define a represenation for its grammer, along with an interpreter that uses the representation to interpret sentences in the language

### [Iterator](./behavioral/iterator)

Provide a way to access the elements of an aggregate object sequentially without exposing its underlying representation

### [Mediator](./behavioral/mediator)

Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently

### [Memento](./behavioral/memento)

Without violating encapsulation, capture and externalize an objects internal state so that the object can be restored to this state later

### [Observer](./behavioral/observer)

Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically

### [State](./behavioral/state)

Allow an object to alter its behavior when its internal state changes. the object will appear to change its class

### [Strategy](./behavioral/strategy)

Define a family of algorithms, encapsulate each one, and make them interchangable. Strategy lets the algorithm vary independently from clients that use it

### [Template Method](./behavioral/template)

Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithms structure

### Visitor

Represent an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the element on which it operates

## Principals of Object Oriented Design

### 1. Program to an interface, not an implementation

* Class inheritance, in short, is borrowing another objects implementation
* Interface inheritance (or subtyping) when one object can be used in place of another (because the interfaces are the same)

### 2. Favor object composition over class inheritance

* Inheritance requires an intimate understanding of the other classes internals - white box
* Composition uses each object as a black-box for composing new functionality
  * Components must have well defined interfaces to work
* This leads to **better encapsulation**

## [Designing for Change](./CHANGE.md)

The key to maximizing reuse lies in anticipating new requirements and changes to existing ones, and designing systems so they can evolve accordingly.
