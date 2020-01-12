# Chapter 7: How to Design Our Organization and Architecture with Conway's Law in Mind

"Five people were assigned to the COBOL job and three to the ALGOL job. The resulting COBOL compiler ran in five phases, the ALGOG compiler ran in three"

## Conways Law:

`organizations which design systems... are constrained to produce designs which are copies of the communication structures of these organizations... The larger an organization is, the less flexibility it has and the more pronounced the phenomenon`

* Holy shit, when there are no rules, and its a wild west crawling with cowboys, thats the kind of software you get
* When you have two people working a project, you get the data engineer and the ux designer...

`The organization of the software and the organization of the software team will be congruent; commonly states as 'if you have four groups working on a compiler, youll get a 4-pass compiler'`

* You MUST design your organizations to **leverage** Conways law, not be bound by it

## Organizational Archetypes

* Functional
  * Optimize for expertise, division of labor, or reducing cost
  * Centralize expertise, which enables career growth and skill development
  * Typically have tall hierarchical organizational structures
  * This is how Operations typically is: server admins, network admins, database admins
* Matrix
  * Attempt to combine functional and market orientation
  * Typically, gets complicated and has people reporting to two managers (or more)
  * Sometimes achieves neither the goals of functional or market...
* Market
  * Optimize for responding quickly to customer needs
  * Tend to be flat, composed of multiple cross functional disciplines (marketing, engineering, etc) - this can lead to redundancy
  * This is how many prominent organizations adopting DevOps operate

## Problems Often Caused by Overly Functional Orientation ("Optimizing for Cost")

* Results in long lead times, especially for complex activities due to the required coordination
* People performing work also have little visibility and understanding of how their work relates to any value stream goals
  * Puts people in a creativity and motivation vacuum
* People working on multiple value streams are also forced to weigh and compete for cycle time
  * Typically, requires someone too high up the chain to make a priority decision - far away from the value stream
* Also results in:
  * Long queues
  * Long lead times
  * Poor handoofs
  * Large amounts of rework
  * Quality issues
  * Bottlenecks
  * Delays

## Enable Market-Oriented Teams ("Optimizing for Speed")

* For DevOps to work, need to minimize the effects of `functional orientation`, and enable `market orientation`
  * Want mane small teams working safely and independently

## Making Functional Orientation Work

* CAN work if everyone in the value stream views customer and organizational outcomes as a **shared goal**
  * Etsy, Google and Github use this
  * Rely on a core Operations team that is quick and reliable to access (essentially On-Demand)

## Testing, Operations and Security as Everyones Job, Every Day

## Enable Every Team Member to be a Generalist

* Over specialization leads to *siloization*

| "I-Shaped" (specialists) | "T-Shaped" (Generalists) | "E-Shaped" |
|-|-|-|
| Deep expertise in one area | Deep expertise in one area | Deep expertise in a few areas|
| Very few skills or experience in other areas | Broad skills across many areas | Experience across many areas. Proven execution skills. Always innovating |
| Creates bottlenecks quickly | Can step up to remove bottlenecks | Almost limitless potential |
| Insensitive to downstream waste and impact | Sensitive to downstream waste and impact | |
| Prevents planning flexibility or absorbtion of variability | Helps make planning flexible and absorbs variability | |

* Generalists perform magnitudes over specialists
  * While one generalist manager may cost twice as much than two specialists, their ability to grease wheels and remove queues is unrivaled
  * "Faster flows are overwhelming"

## Fund Not Projects, But Services and Products

* Product based funding model values:
  * Achievements of organizational and customer outcomes
  * Revenue, customer lifetime value, customer adoption rate
  * All with the minimum output (ammount of effort or time, lines of code)
* Contrast this to traditional measures
  * Completed within a promised budget, time, and scope

## Design Team Boundaries in Accordance with Conways Law

* Different floors, different buildings, different time zones makes for problems in creating and maintaining a shared and mutual trust

## Create Loosely-Coupled Architectures to Enable Developer Productivity and Safety

* Service Oriented Architectures (SOAs)
  * Services are independently testable and deployable
  * Composed of *loosely-coupled* services with *bounded contexts*
  * Goal is for each service to be updated independently of anything else
  * NO COMMON SCHEMAS haha

## Keep Team Sizes Small (The "Two-Pizza Team" Rule)

* 5-10 people
* Ensures the team has a clear, shared understanding of the system they are working on
  * Larger teams require more communication to ensure everyone knows whats going on
* Limits growth rate of the product and services
  * Ensures everyone maintains a shared understanding of the system
* Decentralizes power and enables autonomy
  * The leader of the 2PT works with executives to decide the key business metric that the team is responsible for aka `the fitness function`
* Leading a 2PT allows employees to gain leadership experience in an environment where failure does not have catastrophic consequences
