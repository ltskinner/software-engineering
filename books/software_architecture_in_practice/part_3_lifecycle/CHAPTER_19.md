# Chapter 19: Architecture, Implementation, and Testing

"You dont make progrss by standing on the sidelines, whimpering and complaining. You make progress by implementing ideas"

## 19.1 Architecture and Implementation

* Many times, it is easier to code away from the architecture
* Need to mitigate this

### Embedding the Design in the Code

* Document the architectural concept or guidance inside the code thats being worked on
* Work to localize architectural elements as well

### Use Frameworks

### Code Templates

### Keep Code and Architecture Consistent

* Easy for the two to drift apart
* Things that help
  * Sync at life-cycle milestones
  * Sync at crisis
  * Sync at check-in
    * Ensure this is automated
    * Alert architects if a component breaks predetermined rules

## 19.2 Architecture and Testing

### Levels of Testing and How Architecture Plays a Role in Each

* Unit Testing
  * Tests run on specific pieces of software
  * Part of the job of implementing those pieces
  * Architecture defines
    * Which units are to exist
    * What each units are supposed to do - the things being tested
* Integration Testing
  * Tests what happens when separate software units start to work together
  * Architecture helps define the increments in which things will be tested
  * The interfaces between components are also defined
* Acceptance Testing
  * Testing run by users
  * The point of testing is to "bring down the house"
    * The architecture shows where the most important walls are

#### Risk-Based Testing

* Knowing what components are riskiest is the architects job
* Knowing these allows for more focused testing

### The Architects role

* Ensure testers have access to soure code, design docs, and change records
* Give testers ability to control and reset the entire dataset
* Give testers the ability to install multiple versions of a software product line
