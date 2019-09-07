# Chapter 18: Documenting Software Architectures

"If it is not written down, it does not exist"

* If an architecture is not documented, the system is essentially useless and will be subject to illinformed modifications and bastardizations of use
* All the hard work will have been wasted

## 18.1 Uses and Audiences for Architecture Documentation

* Docs serve as a means of educating
* Is the primary vehicle for communication with stakeholders
* Is the basis for system analysis and construction

## 18.2 Notations for Architecture Documentation

* Informal notations
  * Views are depicted using general diagramming tools
  * Decription are in natural language
* Semiformal notations
  * Standardized notations that uses graphical elements and rules of construction
  * UML is like this
* Formal notations
  * Views are described in a notation that has a precise (and usually math based) semantics

## 18.3 Views

### Module Views

* Show how a systems source code is decomposed into units
* The assumptions that can be made about each unit
* How units are composed into larger structures
* Relations
  * Is part of
  * Depends on
  * Is a

#### Properties to include

* Name
* Responsibilities
* Visibility interfaces (public v private)
* Mapping to source code units
* Test information
* Management information (schedule, budget)
* Implementation constraints
* Revision history

### Component & Connector Views

* Components
  * Have *ports* to interact with connectors
  * Do the actual processing
* Connectors
  * The pathways of interaction
* Relations
  * Attachments
  * Interface delegation

#### Properties

* Reliability
* Performance
* Resource requirements
* Functionality
* Security
* Concurrency
* Modifiability
* Tier

### Allocation Views

* Elements
  * Software element
  * Environment element
* Relations
  * Allocated to

### Quality Views

* Security Views
* Communications View
* Exception/Error Handling View
* Reliability View
* Performance View

## 18.4 Choosing the Views

* At minimum will need:
  * One Module view
  * One C&C view
  * Sometimes an Allocation view for larger systems

### Step 1: Build a stakeholder view table

* Enumerate the stakeholders
* Enumerate the views that apply to the system
* Fill out the level of detail that each stakeholder would find useful

### Step 2: Combine views

* Need to narrow down to a reasonable number of views
* Want to serve the most important or largest number of stakeholders

### Step 3: Prioritize and Stage

* Decomposition views are easy to release early
* Dont have to cover everything, just need to get 80% to be immensely useful
* Dont have to complete views sequentially, can take a breadth first approach

## 18.5 Combining Views

* Sometimes, can be useful to present two views in tandem

## 18.6 Building the Documentation Package

### Documenting a View

#### Section 1: The Primary Presentation

* Shows the elements and the relations of the view
* The main information you are trying to convey
* This is often graphical

#### Section 2: The Element Catalog

* Details the elements depicted in the primary presentation
* Specific parts are
  * Elements and their properties
  * Relations and their properties
  * Element interfaces
  * Element behavior

#### Section 3: Context Diagram

* Shows how the primary view relates to the environment

#### Section 4: Variability Guide

* Shows how vertain points in the architecture may be varied

#### Section 5: Rationale

* Explains why the design came to be

### Documenting Information Beyond Views

1. Overview of the architecture documentation - how things are layed out
2. Information about the architecture

#### Section 1: Documentation Roadmap

What information there is and where to find it

* Scope and summary
* How documentation is organized
* View overview - what views are included
  * Name of view and patters it instantiates
  * Description of views elements, relations, properties
  * Description of language, modeling techniques used to create view
* How stakeholders can use the documentation

#### Section 2: How a View is Documented

* Explain standard organization
* Tells how to find info from a view

#### Section 3: System Overview

#### Section 4: Mapping Between Views

* Help the reader understand the associations
  * many-to-many
  * one-to-many
  * etc

#### Section 5: General Rationale

#### Section 6: Directory

* Reference material
  * Terms, glossary, acronyms

## 18.7 Documenting Behavior

* Two kinds of notations available:
  * Trace-oriented languages
  * Comprehensive languages

### Traces

* Traces are sequences of activities or interactions that describe a systems response to a specific stimuli when the system is in a specific state
* Can depict through
  * Use cases
  * UML sequence diagrams
  * UML communication diagrams
  * UML activity diagrams

### Comprehensive

* Architecture Analysis and Design Language (AADL)
* Specification and Description Language (SDL)

## 18.8 Architecture Documentation and Quality Attributes

* Major design approaches will have quality attributes associated to them
  * Record with rationale
* Individual components typically have qa associated with them
  * Record as properties
* Quality attributeds typically have a language associated with them
  * Use this domain specific language to express them
* Make finding the QA metrics easy
  * Put in the directory

## 18.9 Documenting Architectures That Change Faster Than You Can Document Them

* Document whats true about all versions of your system
* Document in ways that architecture is allowed to change

## 18.10 Documenting Architecture in an Agile Development Project

* If information isnt needed, dont document it
* All documentation should be produced with an audience in mind

### Tips

* Adopt a template or standard organization to capture design decisions
* Plan to document a view if (and only if) it has a stongly identified stakeholder backing
* Fill in info on views as it becomes available
  * Dont feel obliguated to fill in all the sections of the template
* Produce just enough documentation that the code can move forward
