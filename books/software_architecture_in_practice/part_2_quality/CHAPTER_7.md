# Chapter 7: Modifiability

"Study after study shows that most of the cost of a typical software system occurs after it has been initially released"

## Questions to Consider

* What can change?
* What is the likelihood of the change?
* When is the change made and who makes it?
* What is the cost of the change?

## 7.1 Modifiability General Scenario

* Source
  * End user, developer, system admin
* Stimulus
  * A directive to add/delete/modify functionality
  * Change a quality attribute, capacity, or technlology
* Artifacts
  * Code, data, interfaces, components, resources, configurations
* Environment
  * Runtime, compile time, build time, initiation time, design time
* Response
  * One of more of the following
    * Make modification
    * Test modification
    * Deploy modification
* Response Measure
  * Cost in terms of:
    * Numer, size, complexity of affected artifacts
    * Effort
    * Calendar time
    * Money (direct outlay or opportunity cost)
    * Extent to which this modification affects other functions or quality attributes
    * New defects introduced

## 7.2 Tactics for Modifiability

* **Coupling:** the overlap between modules
* **Cohesion:** how unified of purpose a module is

### Helpful Parameters

* Size of a Module
  * Tactics that split modules will reduce the cost of making a modification
  * Smaller is better
* Coupling
  * Can reduce by putting intermediaries of sorts between A and B
  * Restrict dependencies
  * Refactor
  * Abstract common services
* Cohesion
  * Can be improved by removing responsibilities unaffected by anticipated change
* Binding Time of Modification
  * Ensure system is equipped to accomodate modification late in the life cycle
  * Must plan for this, else going to be typical and have expected price tags

#### Deferring Binding Tactics

* Bind at Compile Time
  * Component replacement (build script or makefile)
  * Compile time parameterization
* Bind at Deployment time
  * Configurations
* Bind at Startup
  * Resource files
* Bind at Runtime
  * Runtime registration
  * Dynamic lookup
  * Interpret parameters
  * Startup time binding
  * Name servers
  * Plug-ins
  * Publish-subscribe
  * Shared repos
  * Polymorphism

## 7.3 Modifiability Checklist

### Allocation of Resources

* [ ] Determine which changes, or categories of change are likely
  * [ ] Consider: technical, legal, social, business, customer forces
* [ ] What would need to be added, modified, deleted ot make the change?
* [ ] Determine impacted responsibilities

### Coordination Model

* [ ] Which functional or quality attribute can change?
* [ ] Determine devices, protocols, comm paths likely to change
  * [ ] Insulate accordingly
* [ ] Reduce coupling of dependent elements

### Data Model

* [ ] What will change in the data and their abstractions
* [ ] What categories are likely to change?
  * [ ] Creation, initialization, persistence, manipulation, translation, destruction

### Mapping among Architectural Components

* [ ] Determine if it is desirable to change the way functionality is mapped to computational elements
* [ ] Execution dependencies
* [ ] Assignment of data to databases
* [ ] Assignment of runtime elements to processes, threads, or processors

### Resource Management

* [ ] What changes might introduce new resources, remove old ones, or affect existing resource usage
* [ ] Determining what resource limits will change and how
* [ ] Encapsulate all resource managers

### Binding Time

For each category of change

* [ ] Determine the latest time at which the change will need to be made
* [ ] Choose a defer-binding time that delivers appropriate capability at the time chosen
* [ ] Determine cost of introducing the mechanism and cost of change
* [ ] Dont introduce so many binding choices that change is impeded because dependencies are complex and unknown

### Choice of Technology

* [ ] Determine what modifications are made easier or harder by your technology choices
* [ ] Is it easy to modify technology in case the technologies change?
