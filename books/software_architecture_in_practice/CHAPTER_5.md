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

## 5.2 [Avilability Checklist](./AVAILABILITY_CHECKLIST.md)
