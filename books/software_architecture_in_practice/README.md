# Software Architecture in Practice

## Part 1: Introduction

### [Chapter 1: What Is Software Architecture](./part_1_intro/CHAPTER_1.md)

* The [Rules of Thumb](./part_1_intro/RULES_OF_THUMB.md) are soo good
* [Architecture Structures Table](./part_1_intro/ARCHITECTURE_STRUCTURES_TABLE.md)

### [Chapter 2: Why Is Software Architecture Important](./part_1_intro/CHAPTER_2.md)

"The earlier you can find a problem in your design, the cheaper, easier, and less disruptive it will be to fix"

* Early ripples can become tsunamis
  * Be thoughtful about decisions and assumptions made early on
* Spend extensive time researching before deciding on an architecture
  * Changes are very costly
* Archtiecture and associated metrics for patterns are huge in helping managers allocate resources
  * A consensus between top-down estimates (from architects and PMs) and bottom-up estimates (created by developers) is great

### [Chapter 3: The Many Contexts of Software Architecture](./part_1_intro/CHAPTER_3.md)

### See [Quality Attributes](./part_2_quality/QUALITY_ATTRIBUTES.md)

"Functionality is not a driver of the architecture as much as it is a consequence of it"

## Part Two: Quality Attributes

### [Chapter 4: Understanding Quality Attributes](./part_2_quality/CHAPTER_4.md)

"Functionality often takes the front seat in the development scheme. This preference is often shortsighted, howver. Systems are frequently redesigned not because they are functionally deficient - the replacements are often functionally identical - but because they are difficult to maintina, port, or scale; or are too slow; or they have been compromised by hackers"

* A Quality Attribute is a measurable or testable property of a system used to indicate how well the system satisfies the needs of its stakeholders

#### [Expressing Quality Attributes](./part_2_quality/QUALITY_EXPRESSION.md)

#### [Categories of Design Decisions](./part_2_quality/DESIGN_DECISIONS.md)

### [Chapter 5: Availability](./part_2_quality/CHAPTER_5.md)

"Its tempting to say that failure is not an option. Its a catchy phrase, but its a lousy design philosophy"

#### [See Availability Table](./part_2_quality/AVAILABILITY.md)

#### Availability Tactics

1. [Fault Detection](./part_2_quality/FAULT_DETECTION.md)
2. [Fault Recovery](./part_2_quality/FAULT_RECOVERY.md)
3. [Fault Prevention](./part_2_quality/FAULT_PREVENTION.md)

### [Chapter 6: Interoperability](./part_2_quality/CHAPTER_6.md)

Interoperability is the degree to which two or more systems can usefull exchange meaningful information via interfaces in a particular context

* Basically, use SOAP or REST and WS* for interface boundaries

### [Chapter 7: Modifiability](./part_2_quality/CHAPTER_7.md)

"Study after study shows that most of the cost of a typical software system occurs after it has been initially released"

### [Chapter 8: Performance](./part_2_quality/CHAPTER_8.md)

### [Chapter 9: Security](./part_2_quality/CHAPTER_9.md)

### [Chapter 10: Testability](./part_2_quality/CHAPTER_10.md)

"Testing leads to failure, and failure leads to understanding" - the leading to failure is why its so hard to rally to test, and why its so critical

### [Chapter 11: Usability](./part_2_quality/CHAPTER_11.md)

"Any darn fool can make something complex; it takes a genius to make something simple" - Einstein

### [Chapter 12: Other Quality Attributes](./part_2_quality/CHAPTER_12.md)

### [Chapter 13: Architectural Tactics and Patterns](./architecture_patterns)

### [Chapter 14: Quality Attribute Modeling and Analysis](./part_2_quality/CHAPTER_14.md)

* Architectural patterns let you predict quality attributes
* Many times, this can be done with general equations for latency, queueing and availability

#### [Analytics Models](./part_1_quality/ANALYTICS_MODELS.md)

## Part 3: Architecture in the Life Cycle

### [Chapter 15: Architecture in Agile Projects](./part_3_lifecycle/CHAPTER_15.md)

"Just enough architecture" - the whole point is to reduce risk

### [Chapter 16: Architecture and Requirements](./part_3_lifecycle/CHAPTER_16.md)

* ASR - Architecturally Significant Requirement
* Compenetent architects make an effort to talk to the most important stakeholders to begin uncovering them
* QAW - Quality Attribute Workshop
  * Good to do before finalizing the architecture
* PALM to capture Business Goals

### [Chapter 17: Designing an Architecture](./part_3_lifecycle/CHAPTER_17.md)

### [Chapter 18: Documenting Software Architectures](./part_3_lifecycle/DOCUMENTING.md)

"If it is not written down, it does not exist"

* If an architecture is not documented, the system is essentially useless and will be subject to illinformed modifications and bastardizations of use
* All the hard work will have been wasted
* Also critical for noting the why behind things
  * Shmucks and jerks!
* Be sure to document decisions as well
* **Follow a release strategy**
  * This will greatly help with documentation

### [Chapter 19: Architecture, Implementation, and Testing](./part_3_lifecycle/CHAPTER_19.md)

"You dont make progrss by standing on the sidelines, whimpering and complaining. You make progress by implementing ideas"

### [Chapter 20: Architecture Reconstruction and Conformance](./part_3_lifecycle/CHAPTER_20.md)

### [Chapter 21: Architecture Evaluation](./part_3_lifecycle/CHAPTER_21.md)

"Fear cannot be banished, but it can be calm and without panic; it can be mitigated by reason and evaluation"

### [Chapter 22: Management and Governance](./part_3_lifecycle/CHAPTER_22.md)

"How does a project get to be a year behind schedule? One dat at a time"


Revisit this book in 2 years to refresh on the last two sections regarding large scale architectures and business level decisions.

## Part 4: Architecture and Business

### Chapter 23: Economic Analysis of Architectures

### Chapter 24: Architecture Competence

### Chapter 25: Architecture and Software Product Lines

## Part 5: The Brave New World

### Chapter 26: Architecture in the Cloud

### Chapter 27: Architectures for the Edge
