# Chapter 3: The Second Way: The Principles of Feedback

Right and left blow between Dev and Ops

* Typically, errors are only noticed after something catastrophic is underway
* When failures and accidents occur, use them as learning opportunities - dont berate people

## Working Safely Within Complex Systems

* Easily defined as a system that one person cannot see the system as a whole and understand how all the pieces fit together
* Can also be defined as a system who can do the same thing twice, but wont neccessarily have the same result

### Safety checklist

* Complex work is managed so that problems in design and operations are revealed
* Problems are swarmed and solved, resulting in quick construction of new knowledge
* New local knowledge is exploited globally throughout the organization
* Leaders create other leaders who continually grow these types of capabilities

## See Problems as They Occur

* Must constantly lest our design and operating assumptions
  * The more assumptions we can invalidate, the faster we can find and fix problems
* Create pervasive telemetry

## Swarm and Solve Problems to Build New Knowledge

* Main goal is to contain problems before they have a chance to spread
* And to diagnose and treat problems so that it cannot recur
* Swarming extreme example - in Toyota plants, whenever anything goes wrong, a cord is pulled
  * Unless the problem can be solved in 55 seconds, the entire plant is halted so everyone can be a part of learning the solution
  * `Andond cord`

### Why Swarming is Neccessary

* Prevents the problem from progressing downstream (where cost and effort to repair grows exponentially)
* Prevents the workcenter from starting new work, new work that will likely introduce new errors into the system
* If the problem is not addressed, the work center could potentially have the same problem in the next operation (55s later...)

## Keep Pushing Quality Closer to the Source

* Keep decision making as close to where the decision affects as possible

### INEFFECTIVE Quality Controls

* Requiring another team to complete tedious, error prone, and manual tasks that could easily be automated (and run as needed by the team who needs the work performed)
* Requiring approvals from busy people who are distant from the work, forcing them to make decisions without an adequate knowledge of the work or the potential implications (never seen this before :))
* Creating large volumes of documentation of questionable detail which become obsolete shortly after they are written
* Pushing large batches of work to teams and special committees for approval and processing and then waiting for responses

"Its impossible for a developer to learn anything when someone yells at them for something they broke six months ago" - need feedback as quickly as possible

## Enable Optimizing for Downstream Workcenters

* Can design for the external customer
* Can design for the internal customer (the person recieving and processing work after us)
* **According to Lean, the most important customer is the next step downstream**
