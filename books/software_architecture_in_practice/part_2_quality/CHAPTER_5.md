# Chapter 5: Availability

* Availability: Property of software that it is there and ready to carry out its task when you need it to be
* Dependability: Availity to avoid failures that are more frequent and more severe than is acceptable

## Planning for Failure

"Its tempting to say that failure is not an option. Its a catchy phrase, but its a lousy design philosophy"

* The first step in planning is to understnad what the consequences of each will be

### 1) Hazard Analysis

Catalogue the hazards that can occur during the operation of a system. Furthermore, it categorizes each hazard according to severity

* Catastrophic
  * Failure may cause a crash
  * Loss of critical function
* Hazardous
  * Failure has a large negative impact on safety or performance
* Major
  * Safety is effected
* Minor
  * Failure is noticable
* No effect

### 2) Fault Tree Analysis

* Specifies the state of the system that negatively impacts safety or reliability
  * Then traces the systems context and operation to find all the ways the undesirable state could occur

## 5.1 Availability General Scenario

### [See Availability Table](./AVAILABILITY.md)

## 5.2 Tactics for Availability

### Three Categories

1. [Fault Detection](./FAULT_DETECTION.md)
2. [Fault Recovery](./FAULT_RECOVERY.md)
3. [Fault Prevention](./FAULT_PREVENTION.md)

## 5.2 Avilability Checklist

### Allocation of Responsibilities

Determine system responsibilites that need to be available

* [ ] Detect
  * [ ] Omissions
  * [ ] Crashes
  * [ ] Incorrect timing
  * [ ] Incorrect reponses
* [ ] Log faults
* [ ] Notify approproate entities (people or systems)
* [ ] Disable source of events causing the fault
* [ ] Be temporarily unavailable
* [ ] Fix or mast the fault/failure
* [ ] Operate in a degraded mode

### Coordination Model

Determine the systems responsibilities that need to be highly available

* [ ] Ensure coordination mechanisms can detect faults
* [ ] Ensure coordination mechanisms:
  * [ ] Properly log fault
  * [ ] Properly notify
  * [ ] Perform protective actions from Allocation of Responsibilities
* [ ] Ensure coordination model supports replacement of artifacts that broke
* [ ] Determine if coord will work under impaired conditions
  * [ ] Degraded comms
  * [ ] Startup/shutdown

### Data Model

Determinw which data structures are likely to cause problems

* [ ] Ensure these components can be
  * [ ] Disabled
  * [ ] Made temporarily unavailable
  * [ ] Outright fixed

### Mapping among Architectural Elements

Determine artifacts that may produce a fault

* [ ] Find which processes on failed processers need to be reassigned
* [ ] Find processors, data stores, comms channels that can be reactivated or reassigned
* [ ] How data on failed processors or storage can be served by replacement units
* [ ] How quickly can the system be reinstalled

### Resource Management

Determine what critical resources are neccessary to continue operating in the presence of a fault

### Binding Time

Determine how and when architectural elements are bound

* [ ] Will chosen fault detection and recovery mechanisms work for all possible bindings
* [ ] Is the recovery strategy sufficient to handle all cases
* [ ] What are the availability characterisitics of the late binding mechanism itself?

### Choice of Technology

* [ ] Determine the available tehcnologies that can help detect and recover from faults, as well as reintroduce failed components
* [ ] Determine availability characteristics of these technologies as well
