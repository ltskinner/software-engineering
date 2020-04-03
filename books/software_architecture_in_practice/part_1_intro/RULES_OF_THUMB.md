# Rules of Thumb

## Process Recommendations

* The architecture should be the product of a single architect or a small group of architects with an identified technical lead
  * Critical for ensuring **conceptual integrity** and **technical consistency**
* The architect (or arch. team) should, on an ongoing basis, base the architecture on a prioritized list of well specified quality attribute requirements
  * Keeps tradeoffs front of mind
* The architecture should be documented using views
  * Views should address the concerns of the most important stakeholders in support of the project timeline
  * This may mean minimal documentation first, elaborated on later
* Architecture should be **evaluated** for its ability to deliver the systems important quality attributes
  * Do this evaluation early in the life cycle when it returns the most benefit
* The architecture should lend itself ot incremental implementation, to avoid big bangs
  * One way to do this is through skeleton systems
    * Where communication paths are the skeleton
  * Functionality can be added to the communication paths
  * Emphasis on "grow"ing the system

## Structural Rules of Thumb

* Architecture should feature well-defined modules
  * Functional responsibilites are assigned on the principles of **information hiding** and **separation of concerns**
  * Info hiding modules should **encapsulate things likely to change**
  * Maintain well defined interfaces as well
* Quality attributes should be achieved using well known architectural patterns and tactics specific to each attribute
  * See Chapter 13
* Architecture should never depend on a particular version of a commercial product or tool
  * If it must, ensure its structure so that changes will be easy and inexpensive
* Modules that produce data should be separate from modules that consume data
  * This tends to increase modifiability because changes are frequently confined to either the production OR the consumption side
  * If new data is added, both sides will have to change, but the separation allows for staged upgrades
* Dont expect a one-to-one correspondence between modules and components
* Every process should be written so that its assignment to a specific processor can be easily changed (maybe even at runtime)
* The architecture should feature a small number of ways for components to interact
  * aka the system should do the same things in the same way throughout
  * Aids in:
    * Understandability
    * Reduce development time
    * Increase reliability
    * Enhance modifiability
* Architecture should contain a specific (and small) set of resource contention areas
  * Ex. If network utilization is a concern, the architect should produce (and enforce) guidelines for each development team that will minimize network traffic
