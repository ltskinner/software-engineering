# Chapter 13: Architectural Tactics and Patterns

* An Architectural Pattern:
  * Is a package of design decisions that is found repeatedly in practice
  * Has known properties that permit reuse
  * Describes a class of architectures

## 13.1 Architectural Patterns

Architectural patterns establish a relationship between:

* A context
  * A recurring, common situation that gives rise to a problem
* A problem
  * The problem that arises in a given context
  * Often includes quality attributes that must be met
* A solution
  * A successful architectural resolution to the problem, appropriately abstracted
  * Includes
    * Set of element types (data repos, processes, objects)
    * Set of connectors (method calls, events, message bus)
    * A topological layout of components
    * A set of semantic constraints covering topology, behavior and interaction

## 13.2 Overview of the Patterns Catalog

### [Layered Pattern](./LAYERED.md)

* When a system needs to be able to be developed independently

### Component and Connector Patterns

#### [Broker Pattern](./BROKER.md)

* When you have a collection of services across multiple servers
* A broker is an intermediary that separates clients from servers that provides all the complexity wrangling

#### [Model-View-Controller Pattern](./MVC.md)

* UI is typically the most modified portion of an application
* Need to keep modifications separate from the rest of the system

#### [Pipe-and-Filter Pattern](./PIPE_FILTER.md)

* Good for transforming streams of data from an imput to a usable output
* Can create the transofmations as independent, reusable parts

### [Client-Server Pattern](./CLIENT_SERVER.md)

* There are shared resources that a large number of clients wish to use
* But we wish to control access or quality of service

### [Peer-to-Peer Pattern](./P2P.md)

* For distributed computational entities, each of which are considered equally important, that need to collaborate to provide a service to a distributed community of users

### [Service-Oriented Architecture Pattern](./SERVICE_ORIENTED.md)

* Service consumers need to be able to understand and use services without any detailed knowledge of their implementation
* SOAP, REST
* Enterprise Service Busses
* Main benefit is interoperability

### [Publish-Subscribe Pattern](./PUBLISH_SUBSCRIBE.md)

* There are a number of independent producers and consumers of data that must interact
* The precise number is not predetermined or fixed, nor is the data they share
* MVCs use this
* GUIs in general
* Social networks

### [Shared-Data Pattern](./SHARED_DATA.md)

* Various computational components need to share and manipulate large amounts of data
* Data does not belong solely to any one of those components
* Good in secure environments

## Allocation Patterns

### [Map-Reduce Pattern](./MAP_REDUCE.md)

* When need to quickly analyze 'enormous' volumes of data

### [Multi-tier Pattern](./MULTI_TIER.md)

* Can either be a C&C or allocation, depending on criteria used to define tiers
* In distributed deployment, often need to distribute a systems infrastructure into distinct subsets
* Become logical groupings of components
  * May either be for business or operational reasons
* Can result in high costs and complexity
* BUT make it easier to ensure security

## Other Allocation Patterns

### Platform

* In software product line development, one site is tasked with developing reusable core assets of the product line
  * Other sites are tasked with applications that use the core assets

### Competence Center

* Work is allocated to sites depending on the technical or domain experience located at a site

### Open Source

## 13.3 Relationships between Tactics and Patterns

### Patterns Comprise Tactics

* Patterns are made up of tactics
