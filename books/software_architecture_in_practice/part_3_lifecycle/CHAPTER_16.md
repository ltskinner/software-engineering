# Chapter 16: Architecture and Requirements

* ASR - Architecturally Significant Requirement
* Compenetent architects make an effort to talk to the most important stakeholders to begin uncovering them

## ASRs

* A profound impact on the architecture
* A high business or mission value

## 16.1 Gathering ASRs from Requirements Documents

* MoSCoW style documentation
  * Must, should, could wont (lmaoo)

| Design Decision Category | Look for Requirements Addressing... |
| - | - |
| Allocation of Responsibilities | Planned evolution of repsponsibilities, user, roles, system modes, major processing steps, commercial packages |
| Coordination Model | Properties of the coordination (Timliness, currency, completeness, correctness, consistency). Names of external elements, protocols, sensors or actuators (devices), middlewear, network configurations (security configs) |
| Data Model | Processing steps, information flows, major domain entities, access rights, persistence, evolution requirements |
| Management of Resources | Time, concurrency, memory footprint, scheduling, multiple users, multiple activities, devices, energy usage. Scalability requirements |
| Mapping among Architectural Elements | Plans for teaming, processors, families of processors, evolution of processors, network configurations |
| Binding Time Decisions | Extensions of or flexibility of functionality, regional distinctions, language distinctions, portability, calibrations, configurations |
| Choice of Technology | Named technologies, changes to technologies (planned and unplanned) |

## 16.2 Gathering ASRs by Interviewing Stakeholders

### The Quality Attribute Workshop (QAW)

A facilitated, takeholder focused method to generate, prioritize, and refine quality attribute scenarios before the architecture is completed. It is keenly dependent on the participation of system stakeholders

* Step 1: QAW Presentation and Introductions
  * Describe the motivations and each step
  * Also introduce everyone in the room, background, role, relation to the system
* Step 2: Business/Mission Presentation
  * Stakeholder representing business concerns
  * Broad functional reqs, constraints, known quality attribute requirements
* Step 3: Architectural Plan Presentation
  * Present architectural plans as they stand
* Step 4: Identification of Architectural Drivers
  * Facilitators will share a list of key architectural drivers
  * Ask stakeholders for clarifications, additions, deletions, corrections
  * Main goal is to reach a consensus on a distilled list of architectural drivers
* Step 5: Scenario Brainstorming
  * Stakeholders express a scenario representing their concerns with respect to the system
  * Ensure there is at least one scenario for each architectural driver
* Step 6: Scenario Consolidation
  * Consolidate similar ones before "voting"
* Step 7: Scenario prioritization
  * Some stupid ass rules about giving stakeholders votes
* Step 8: Scenario Refinement
  * Top scenarios are refined and elaborated on
  * Go through the source-stimulus-artifact-environment-response-response measure thing

## 16.3 Gathering ASRs by Understanding the Business Goals

1. Business goals often lead to quality attribute requirements
2. Business goals may directly affect the architecture without supplying a quality attribute - like being forced to use a system
3. No influence at all

### Standard Business Goal Categories

1. Contributing to the growth and continuity of the organization
2. Meeting financial objectives
3. Meeting personal objectives
4. Meeting responsibility to employees
5. Meeting responsibility to society
6. Meeting responsibility to state
7. Meeting responsibility to shareholders
8. Managing market position
9. Improving business process
10. Managing the quality and reputation fo products
11. Managing change in environmental factors

### Expressing Business Goals

* The Goal Source
  * The people or written artifacts providing the goal
* The Goal Subject
  * The stakeholders who own the goal and wish it to be true
* The Goal Object
  * The entities that the goal apply to or are driven by
* Environment
  * This is the context for the goal
  * Social, legal, competitive, customer, technological, political
* The Goal
  * Any business goal articulated by the goal source
* The Goal Measure
  * A testable beasurement to determine how one would know if the goal has been achieved
* Pedigree and Value
  * The pedigree tells us the degree of confidence the person who stated the goal has in it, and the goals volatility and value

## 16.4 Capturing ASRs in a Utility Tree

### PALM

Typically carried out over a day and a half workshop attended by architects and stakeholders

#### PALM Overview

* Overview of PALM, the problem it solves, its steps, and its expected outcomes

#### Business Drivers Presentation

* Briefing of business drivers by PMs

#### Architecture Drivers Presentation

* Briefing by the architect on the driving business and quality attribute requirements
* aka the ASRs

#### Business Goals Elicitation

* Using standard business goal categories to guide discussion, capture a set of important business goals for the system
* Goals are expressed in scenarios

#### Identification of Potential Quality Attributes

* Using the business goal scenarios, participats describe a quality attribute that would help achieve the goal

#### Assignment of Pedigree to Existing Quality Attribute Drivers

* Of the existing architectural drivers, assign quality attributes that will result from them

#### Exercise Conclusion

* Review of results, next steps, and participat feetback
