# Seven Categories of Design Decisions

## 1) Allocation of Responsibilities

* Identifying the important responsibilities, including basic system functions, architectural infrastructure, and satisfaction of quality attributes
* Determinimg how these responsibilities are allocated to non-runtime and runtime elements (namely, modules, components, and connectors)

## 2) Coordination Model

Software works by having elements interact with each other

* Identifying the elements of the system that must coordinate, or are prohibited from coordinating
* Determining the properties of the coordination
  * Timelines, currency, completeness, correctness, consistency
* Choosing the communication mechanisms (between systems and elements)
  * Like synchronous vs asynchronous

## 3) Data Model

Every system must represent data in some internal fashion

* Choosing the major data abstractions, their operations, and their properties
  * Includes how data items are created, initialized, accessed, persisted, manipulated, translated, and destroyed
* Compiling metadata needed for consistent interpretations of the data
* Organizing the data
  * RDB, object stores, mapping between locations

## 4) Management of Resources

* Hard resources
  * CPU, GPU, battery, IO ports
* Soft resources
  * System locks, buffers, thread pools, non-thread-safe code
* Identifying resources that must be managed
  * And determining the limits of each
* Determining which system elements manage each resource
* Determining how resources are shared and arbitration strategies for contention
* Determining the impact of saturation on different resources
  * Overloaded CPUs just run slower
  * Memory, after paging runs out, crashes

## 5) Mapping among Archtiectural Elements

* Architecture must provide two types of mappings
  * Between elements in different types of architecture structures
    * Units of development (modules)
    * To units of execution (threads)
  * Between software elements and environment elements
    * Mapping processes to specific CPUs
* Mapping modues and runtime elements to each other
  * The runtime elements created from each module
  * The modules that contain code for each runtime element
* Assignment of runtime elements to processors
* Assignment of items in the data model to data stores
* MApping of modules and runtime elements to units of delivery

## 6) Binding Time Decisions

* For allocation of responsibilities, you can have build-time selection of modules via a parameterized makefile
* For choices of coordination model, you can design runtime negotiation of protocols
* For resource management, you can design a system to accept new peripheral devices plugged in at runtime, after which the system recognizes them and downloads and installes the right drivers automatically

## 7) Choice of Technology

All architecture decision must eventually be reslized by using a specific technology

* Deciding which technolologies are available to realize the decisions made in the other categories
* Determining whether the available tools (IDE, testing tools) are adequate for development to proceed
* Determining the extent of internal familliarity and external support for the technology, and whether its enough to proceed
* Determining side effects of choosing a technology
* Determining whether a new technology is compatable with the existing stack
