# Software Architecture in Practice

## Part 1: Introduction

### [Chapter 1: What Is Software Architecture](./CHAPTER_1.md)

* The [Rules of Thumb](./RULES_OF_THUMB.md) are soo good
* [Architecture Structures Table](./ARCHITECTURE_STRUCTURES_TABLE.md)

### [Chapter 2: Why Is Software Architecture Important](./CHAPTER_2.md)

"The earlier you can find a problem in your design, the cheaper, easier, and less disruptive it will be to fix"

* Early ripples can become tsunamis
  * Be thoughtful about decisions and assumptions made early on
* Spend extensive time researching before deciding on an architecture
  * Changes are very costly
* Archtiecture and associated metrics for patterns are huge in helping managers allocate resources
  * A consensus between top-down estimates (from architects and PMs) and bottom-up estimates (created by developers) is great

### [Chapter 3: The Many Contexts of Software Architecture](./CHAPTER_3.md)

### See [Quality Attributes](./QUALITY_ATTRIBUTES.md)

"Functionality is not a driver of the architecture as much as it is a consequence of it"

## Part Two: Quality Attributes

### [Chapter 4: Understanding Quality Attributes](./CHAPTER_4.md)

"Functionality often takes the front seat in the development scheme. This preference is often shortsighted, howver. Systems are frequently redesigned not because they are functionally deficient - the replacements are often functionally identical - but because they are difficult to maintina, port, or scale; or are too slow; or they have been compromised by hackers"

* A Quality Attribute is a measurable or testable property of a system used to indicate how well the system satisfies the needs of its stakeholders

#### [Expressing Quality Attributes](./QUALITY_EXPRESSION.md)

#### [Categories of Design Decisions](./DESIGN_DECISIONS.md)

### [Chapter 5: Availability](./CHAPTER_5.md)

"Its tempting to say that failure is not an option. Its a catchy phrase, but its a lousy design philosophy"

#### [See Availability Table](./AVAILABILITY.md)

#### Availability Tactics

1. [Fault Detection](./FAULT_DETECTION.md)
2. [Fault Recovery](./FAULT_RECOVERY.md)
3. [Fault Prevention](./FAULT_PREVENTION.md)

#### [Avilability Checklist](./AVAILABILITY_CHECKLIST.md)

### [Chapter 6: Interoperability](./CHAPTER_6.md)

Interoperability is the degree to which two or more systems can usefull exchange meaningful information via interfaces in a particular context

* Basically, use SOAP or REST and WS* for interface boundaries

[Interoperability Checklist](./INTEROPERABILITY_CHECKLIST.md)
