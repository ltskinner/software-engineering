# Chapter 4: Understanding Quality Attributes

"Functionality often takes the front seat in the development scheme. This preference is often shortsighted, howver. Systems are frequently redesigned not because they are functionally deficient - the replacements are often functionally identical - but because they are difficult to maintina, port, or scale; or are too slow; or they have been compromised by hackers"

* A Quality Attribute is a measurable or testable property of a system used to indicate how well the system satisfies the needs of its stakeholders

## 4.1 Architecture and Requirements

### 1) Functional Requirements

* What the system must do, and how it must behave or react to runtime stimuli
* --> Satisfied by assigning an appropriate sequence of responsibilities throughout the design

### 2) Quality Attribute Requirements

* These are qualifications of the functional requirements or overall product
* --> Satisfied by the variouis structures designed into the architecture, and the behaviors and interactions of their elements

### 3) Constraints

* Design decisions with zero degrees of freedom
* That is, a design decision thats already been made
  * Programming language, reuse or a specific module
* --> Satisfied by accepting the design decision and reconciling it with other affected design decisions

## 4.2 Functionality

* "First of all, functionality does not determine architecture"
* "In fact, if functionality were the only thing that mattered, you wouldnt have to divide the system into pieces at all; a single monolithic blob with no internal structure would do just fine" lmaooo
* The division into elements serves to
  * Make systems understandable
  * Support a variety of other purposes (quality attributes)

## 4.3 Quality Attribute Considerations

### Problems With Functional Requirements

* The definitions provided ate not testable (well...)
* Discussion often fouses on which quality a particular concern belongs to
* Each attribute community has developed its own vocabulary

## 4.4 Specifying Quality Attribute Requirements

* Quality attribute requirements should me unambiguous and testable

### [Expressing Quality Attributes](./QUALITY_EXPRESSION.md)

## 4.5 Achieving Quality Attributes through Tactics

* A tactic is a design decision that influences the achievement of a quality attribute response
* Input is the stimulus, and the output is the response

## 4.6 Guiding Quality Design Decisions

### [Categories of Design Decisions](./DESIGN_DECISIONS.md)
