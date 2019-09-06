# Chapter 2: Why Is Software Architecture Important

"Sofware archtiecture is the set of design decisions which, if made incorrectly, may cause your project to be cancelled"

## Reasons Architecture Is Important

1. An architecture will inhibit or enable a system's driving quality attributes
2. The decisions made in an architecture allow you to reason about and manage change as the system evolves
3. The analysis of an architecture enables early prediction of a systems qualities
4. A documented architecture enhances communication among stakeholders
5. The architecture is acarrier of the earliest and most fundamental, hardest to change design decisions
6. Architecture defines a set of constraints on dubsequent implementation
7. The architecture dictates the structure of an organization, or vice versa
8. An architecture can provide the basis for evolutionary prototyping
9. An architecture is the key artifact that allows the architect and project manager to reason about cost and schedule
10. An architecture can be created as a transferable, reusable model that forms the heart of a product line
11. Architecture based development focuses attention on the assembly of components, rather than simply on their creation
12. By restricting design alternatives, architecture channels the creativity of developers, reducing design and system complexity
13. An architecture can be the foundation for training a new team member

## 2.1 Inhibiting or Enabling a Systems Quality Attributes

#### See [Quality Attributes](./QUALITY_ATTRIBUTES.md)

## 2.2 Reasoning About and Managing Change

Modifiability - the ease with which changes can be made to a system

### Categories of Change

* Local
  * Local change can be accomplished by modifying a single element.
  * Like adding a new rule to a price logic module
* NonLocal
  * A nonlocal change requires multiple element modifications but leaves the underlying architectural approach intact
    * Adding new fields to the DB
    * Revealing results in the UI
* Architectural
  * Affects the fundamental way in which the elements interact with eachother
  * Changing from client-server to peer-to-peer

## 2.3 Predicting System Qualities

"The earlier you can find a problem in your design, the cheaper, easier, and less disruptive it will be to fix"

## 2.4 Enhancing Communication among Stakeholders

* Architecture provides an abstracted common language for nontechs to engage with
* Congressional hearing example
  * Architecture is usually the only intersection with non-techs
  * Most below it will be disregarded for lack of ability to comprehend

## 2.5 Carrying Early Design Decisions

* Early ripples can become tsunamis

### Some Early Considerations

* Will the system run on one processor or be distributed?
* Will the software be layered? If so, how many layers? What will each one do?
* Will components communicate synchronously or asynchronously? Will they interact be trasferring control or data or both?
* Will the system depend on specific features of the OS or hardware?
* Will the information that flows through the system be encrypted or not?
* What operating system will we use?
* What communication protocol will we choose?

## 2.6 Defining Constraints on an Implementation

* Things like performance constraints need to be imposed by the architect

## 2.7 Influencing the Organizational Structure

* Typically this becomes a work-breakdown task for allocating team resources
* Spend extensive time researching before deciding on an architecture
  * Changes are very costly

## 2.8 Enabling Evoluntionary Prototyping

* Once an architecture has been defined, it can be analyzed and prototyped as a skeletal system
* Do this haha saves cost downstream by ruling out bad ideas

## 2.9 Improving Cost and Schedule Estimates

* Cost and schedule estimates are critical for project managers to acquire neccessary resources and monitor progress
* Most work and resource allocations are done based on the architecture as well
* A consensus between top-down estimates (from architects and PMs) and bottom-up estimates (created by developers) is great

## 2.10 Supplying a Transferable, Reusable Model

* The earlier int he lifecycle that reuse is applied, the greater the benefit

## 2.11 Allowing Incorporation of Independently Developed Components

* Architecture based dev focuses on *composing* or *assembling elements*
  * As opposed to programming being the main focus

## 2.12 Restricting the Vocabulary of Design Alternatives

* Restricting choice is often better than letting stuff go haywire haha
  * ADD vs procedural
  * 7 jams or something like that

## 2.13 Provide a Basis for Training

* Explaining the architecture is a good exercise in describing the system to others
