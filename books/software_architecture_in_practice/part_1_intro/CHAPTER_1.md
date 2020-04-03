# Chapter 1: What Is Software Architecture

"Good judgement is usually the result of experience. And experience is frequently the result of bad judgement. But to learn from the experience of other requires those who have the experience to share the knowledge with those who follow"

## 1.1 What Software Architecture Is and Isnt

### Architecture Definitions

* Architecture is a set of software structures
  * Modules
* Architecture is an abstraction
* Every software system has software architecture
* Architecture Includes Behavior
* Not all architectures are good architectures

### System and Enterprise Architectures

* System Architecture
  * A mapping of functionality onto hardware and software components
* Enterprise Architecture
  * The description of the structure and behavior of an organizations:
    * Processes
    * Personnel
    * Organizational subunits
  * And how these allight with the organizations:
    * Core goals
    * Strategic direction

## 1.2 Architectural Structures and Views

In short, a view is a representation of a structure

### Three kinds of structures

### 1) Module Structures

* These embody how a system is to be broken apart
* Allow the answering of:
  * What is the primary functional responsibility assigned to each module?
  * What other software elements is a module allowed to use?
  * What other software does it actually use and depend on?
  * What modules are related to other modules by generalization or specialisation (inheritance)?
* **Good for gauging a systems modifiability**

#### Useful Module Structures

* Decomposition structure
  * Related by *is-a-submodule-of* relationships
* Uses structure
  * Which modules *use* what
* Layer structure
  * Layer is only allowed to use systems of the layer immediately below
* Class (or generalization) structure
  * *Inherits from*, or is an *instance of*
* Data model
  * Describes the static information structure in terms of *data entities* and their relationships

### 2) Component-and-Connector Structures

* Components = elements with runtime behavior
* Connectors = interactions
* Answer questions like:
  * What are the major executing components and how do they interact at runtime?
  * What are the major shared data stores?
  * Which parts of the system are replicated?
  * How does data progress through the system?
  * What parts of the system can run in parallel?
  * Can the systems structure change as it executes and, if so, how?
* **Figure out the runtime properties like performance, security, availability, and more**

#### Useful C&C Structures

* Service structure
  * Units are services that interoperate with each other
  * Orchustrated by service coordination mechanisms like SOAP
* Concurrency structure
  * Find opportunities to parallelize
  * Break components into logical threads that can be done in separate layers

### 3) Allocation Structures

* Decisions on how the system will relate to non-software components
  * CPUs
  * File systems
  * Networks
  * Development teams
* These help answer:
  * What processor does each software element execute on?
  * In what directories or files is each element stored during development, testing, and system building?
  * What is the assignment of each software element to development teams?

#### Useful Allocation Structures

* Deployment structure
  * Shows how software is assigned to hardware processing and communication elements
  * Typically a process from a C&C view, hardware entities, and communication pathways
  * Relations are *allocated-to* with respect to the hardware
    * *migrates-to* if the allocation is dynamic
* Implementation structure
  * Show how software elements (usually modules) are mapped to the file structure
    * In dev, integration, or configuration control environments
* Work assignment structure
  * Assigns repsonsibility for implementing and integrating the modules to the teams who will carry it out
  * Also determines major communication pathways among teams

### Which Structures to Choose?

* Pick whatever fits the 80% functionality component
  * Choose a structure that will best deliver desired attributes

## 1.3 Architectural Patterns

Patterns are strategies for solving problems that have been seen before

### 1) Module Type Patterns

#### Layered Pattern

* A layer is a coherent set of related functionality
* When the *uses* relation among software is **strictly unidirectional**
* Strictly, when a layer only uses the services in the layer immediately below it

### 2) C&C Patterns

#### Shared-data (or repository) pattern

* Create, store, and access persistent data
* Typically, this takes the form of a commercial database
* Connectors are protocols for managing the data
  * Like SQL

#### Client-Server Pattern

* Components are the clients and servers
* Connectors are the protocols and messages they share to carry out work

### 3) Allocation Patterns

#### Multi-Tier Pattern

* How to distribute and allocate the components of a system in distinct **subsets of hardware and software**
* Specializes in generic deployment

#### Competence Center and Platform

* Patterns that specialize a software systems work assignment structure
* In **Competence Center**, work is allocated to sites depending on technical or domain expertise located at a site
* In **Platform**, one site is tasked with developing reusable core assets of a software product line, and other sites develop applications that use the core assets

## 1.4 What Makes a "Good" Architecture

### [Rules of Thumb](./RULES_OF_THUMB.md)
