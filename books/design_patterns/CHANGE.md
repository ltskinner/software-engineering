# Designing for Change

Common causes of redesign

## 1) Creating an object by specifying a class explicitly

* Specifying a class name chwn you create an object commits you to a particular implementation instead of a particular interface.
* To avoid - create objects indirectly
* **Design Patterns**
  * Abstract Factory
  * Factory Method
  * Prototype

## 2) Dependence on specific operations

* When specifying a particular operation, you commit to one way of satisfying a request
* Avoid hard coded requests
* **Design Patterns**
  * Chain of Responsibility
  * Command

## 3) Dependence on hardware and software platform

* External OS interfaces and APIs are different all around
* Limit these dependancies
* **Design Patterns**
  * Abstract Factory
  * Bridge

## 4) Dependance on object representation of implementations

* Clients that know how an object is
  * represented
  * stored
  * located
  * implemented
  * Will need to be changed when the object changes
* **Design Patterns**
  * Abstract Factory
  * Bridge
  * Memento
  * Proxy

## 5) Algorithmic dependencies

* Algorithms are often extended, optimized, and replaced during development and reuse
* Isolate these bois
* **Design Patterns**
  * Builder
  * Iterator
  * Strategy
  * Template Method
  * Visitor

## 6) Tight coupling

* **Design Patterns**
  * Abstract Factory
  * Bridge
  * Chain of Responsibility
  * Command
  * Facade
  * Mediator
  * Observer

## 7) Extending functionality by subclassing

* Need to find a balance between inheritance and composition
* **Design Patterns**
  * Bridge
  * Chain of Responsibility
  * Composite
  * Decorator
  * Observer
  * Strategy

## 8) Inability to alter classes conveniently

* **Design Patterns**
  * Adapter
  * Decorator
  * Visitor
