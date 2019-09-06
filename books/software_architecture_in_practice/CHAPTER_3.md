# Chapter 3: The Many Contexts of Software Architecture

"People in London think of London as the center of the world, whereas New Yorkers think the world ends three miles outside of Manhattan"

## 3.1 Architecture in a Technical Context

### Architectures Inhibit or Enable the Achievement of Quality Attributes

* ^^
* You can predict many aspects of a systems qualities by studying its architecture
* An architecture makes it easier for you to reason about and manage change

#### See [Quality Attributes](./QUALITY_ATTRIBUTES.md)

## 3.2 Architecture in a Project Life-Cycle Context

### Activities Common Across All Software Life-Cycles

#### 1) Making a business case for the system

* Understanding the use case is important for shaping system and quality requirements
  * Which in turn directly affect architecture

#### 2) Understanding the architecturally significant requirements

* Different systems will have different focuses on requirements elicitation
* Important to understand the most important requirements

#### 3) Creating or selecting the architecture

* Conceptual integrity is imperative

#### 4) Documenting and communicating the architecture

* Must be able to effectively communicate with the stakeholders
* Documentation should be
  * Informative
  * Unambiguous
  * Readable by people with varied backgrounds
  * *Minimal*

#### 5) Analyzing or evaluating the architecture

* Important to consider numerous candidates
* Selecting between the options should be the hardest part

#### 6) Implementing and testing the system based on the architecture

* Main goal is to ensure that the developers are adhering to the architecture haha

#### 7) Ensuring that the implementation conforms to the architecture

* After the system is built and goes into maintenance, must ensure the original vision is being maintained

## 3.3 Architecture in a Business Context

### Architectures and Business Goals

* Architects must understand who the vested organizations are and what their goals are
  * Government agencies
  * Subcontractors
  * These goals will have a large impact on the system
* Understanding the business pressure behing quality attributes is key too
  * "**Why* must the system to be fast?" - "So its faster than the competition"
  * *Business goals* --> Quality attributes ----v
  *                  --------------------------> Architecture

### Architectures and the Developement Organization

* Primarily concerned with team resources available
* If a bunch of P2P experts are laying around, a P2P solution will have traction

## 3.4 Architecture in a Professional Context

* Architects dont just design crap
* They also have to explain, negotiate and protect their designs
  * Primary point of contact to the nontechs

## 3.5 Stakeholders

* Each stakeholder has different interests and concerns
* Need to figure out which ones have priority

## 3.6 How is Architecture Influenced

* The requirements are the main influence
* Architects need to be aware of business and social influences

## 3.7 What Do Architects Influence

* Technical Context
  * Architect can influence the customer by delivering a superior product in less time by doing a new practice
* Project Context
  * The modules and components need to be filled by team resources to complete
  * This directly affects organizational structure and hiring needs
* Business Context
  * Successful systems can help establish a foothold in a particular market segment
* Professional Context
  * Architectures that work will be reused in future projects
  * Failed projects will not be replicated
