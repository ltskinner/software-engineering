# Chapter 17: Designing an Architecture

## 17.1 Design Strategy

### Decomposition

* Decomposing makes things more bite sized
* Allows you to focus on quality attributes at a more granular level

### Designing to Architecturally Significant Requirements

* Have to keep the priorities always in line
* Planning ahead gets easier with experience

### Generate and Test

#### Generating

* Most initial designs can be reused from existing solutions
  * Very few systems are completely unprescedented
* Leverage frameworks
* Leverage patterns and tactices
* Leverage domain decomposition
* Use design checklists to help as well

#### Testing

* Use [analysis techniques](../part_2_quality/CHAPTER_14.md)
* Use design checklists
* Use ASRs

## 17.2 The Attribute-Driven Design Model (ADD)

* Iterative model that helps the architect
  * Choose a part of the system to design
  * Marshal all the architecturally significant requirements for that part
  * Create and test a design for that part

### Inputs to ADD

* Functional, quality, and constraint requirements should be known
  * Well, as many as possible
* Want as many ASRs as possible too, and the correct ones
* These provide the designer with a contect description:
  * What are the boundaries of the system being designed?
    * Whats on the inside of the system and whats on the outside
  * What are the external systems, devices, users, and environmental conditions that the system needs to interact with?

### Outputs of ADD

* Sets of scketches and architectural views

## 17.3 The Steps of ADD

### Step 1: Choose an Element of the System to Design

* The first iteration typically just figures out what elements there need to be
* There are two refinement strategies
  * Breadth first
  * Depth first
* Factors that effect which route to go
  * Personnel availability
    * If a technical keystone is gone, dont want to work in that realm until the resource becomes available
  * Risk mitigation
    * Want to go deep enough so that problems can be identified and solved early on
    * This is critical when using new technology
    * Done through prototyping
  * Deferral of functionality
    * Dont tackle things before you have the right information to make a good decision

### Step 2: Identify the ASRs for the Chosen Element

### Step 3: Generate a Design Solution for the Chosen Element

* This is where the **Generate and Test** is applied

### Step 4: Inventory Remaining Requirements and Select the Input for the Next Iteration

#### ASR Quality Attribute Not Met

* Consider applying (more) tactics
  * Will this tactic improve the quality attribute sufficiently?
  * Should this tactic be used in conjunction with another tactic?
  * What are the tradeoffs when applying this tactic?

#### ASR functional Responsiblity Not Met

* Assign responsibility to a module containing similar ones
* Break a moduel into portions when it is too complex
* Assign the responsiblitiy to a module contining responsibilities with similar quality attribute characteristics

#### ASR Constraints Not Met

* Modify the design
* Relax the constraint

### Step 5: Repeat Steps 1-4 until all ASRs have been satisfied
