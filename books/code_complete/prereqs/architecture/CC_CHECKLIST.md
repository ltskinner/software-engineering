# Code Complete Architecture Checklist

## Programmatic Considerations

* [ ] Major classes are well defined
  * [ ] The 20% controlling the 80% are defined
  * [ ] Everything is properly broken into **blocks**
    * [ ] **blocks** specify
      * [ ] area of **responsability**
      * [ ] **interfaces** to other blocks
    * [ ] requirements **functionality** covered sensibly
      * [ ] not **too many** blocks
      * [ ] not **too few** blocks
* [ ] Overall organization clear
  * [ ] **overview** of architecture
  * [ ] **justification** of architecture
* [ ] Data Design
  * [ ] Internal Data
    * [ ] desicribed
    * [ ] justified
  * [ ] Database description
    * [ ] organization
    * [ ] content
* [ ] User Interface Design
  * [ ] strategy for design described
  * [ ] UI properly modularized so changes won't affect rest of program
* [ ] I/O handling strategy
  * [ ] user interface
  * [ ] internal subsystems
* [ ] Overengineering decision clearly stated with justification

## System Considerations

* [ ] System performance specified
  * [ ] performance **goals** explicity stated
    * [ ] goals stated in reqs (not imaginary or made up on the spot)
    * [ ] estimates and explanations
    * [ ] at risk areas noted and elaborated on
  * [ ] time + speed budgets
    * [ ] core functionality
    * [ ] subsystems
    * [ ] classes
* [ ] Scarce resource **management plans**
  * [ ] database connections
  * [ ] memory
    * [ ] RAM
    * [ ] GPU
  * [ ] bandwidth
  * [ ] threads
  * [ ] handles
  * [ ] etc.
* [ ] Scarce resource **usage estimates**
  * [ ] database connections
  * [ ] memory
    * [ ] RAM
    * [ ] GPU
  * [ ] bandwidth
  * [ ] threads
  * [ ] handles
  * [ ] etc.
* [ ] Scalability properly addressed
  * [ ] description of how system will scale
  * [ ] anticipated growth areas and **solutions**
    * [ ] database growth
    * [ ] compute requirements
    * [ ] transaction or request volume
    * [ ] network nodes
    * [ ] users
    * [ ] etc.

## System Protection

* [ ] Error processing approach
  * [ ] error handing strategy declared
    * [ ] corrective or defective processing approach declared
    * [ ] active or passive detection approach declared
  * [ ] conventions declared
  * [ ] class level data validation declared
    * [ ] **data cleanliness assumptions**
  * [ ] error propagation handling technique
    * [ ] discarding data?
    * [ ] enter error processing state?
    * [ ] notify at end of processing?
  * [ ] exceptions handling
    * [ ] when code can throw declared
    * [ ] where caught declared
    * [ ] logging practices
    * [ ] error documentation practices
  * [ ] use environments exception handling or build own?
* [ ] Fault tolerance approach
  * [ ] error detection means
  * [ ] error recovery means
  * [ ] error containment strategy
* [ ] Security approach
  * [ ] untrusted data handling rules (external sources)
  * [ ] threat modeling considered

## Real World Considerations

* [ ] All parts of system **technically feasible**
* [ ] Key **business rules** identified
  * [ ] **requirements** clearly defined
  * [ ] **impact** on system described
* [ ] **Buy-vs-Build** decisions included
* [ ] **Reuse** decisions
  * [ ] will or will not be reusing code
  * [ ] how reused code will be modified
* [ ] **Interoperability** strategy declared
  * [ ] shared data
  * [ ] shared resources
* [ ] Anticipated **changes** declared
* [ ] System designed to **accomodate** likely changes
  * [ ] volatile data tpyes
  * [ ] file formats
  * [ ] changed functionality
  * [ ] new features

## Architecture Quality

* [ ] **Conceptually** makes sense
* [ ] All **requirements** accounted for
* [ ] Major decision **motivations** provided
* [ ] No part is **over or under architected**
  * [ ] expectations for this set explicitly
* [ ] Design is language independant
* [ ] Design is machine independant
* [ ] Architecture makes sense and is comfortable to the programmer
