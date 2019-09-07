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
