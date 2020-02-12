# Chapter 13: Architect for Low-Risk Releases

"Both eBay and Google are each on their fifth entire rewrite of their architecture from top to bottom"

* Strangler Application
  * Instead of "ripping out and replacing"
  * Hide exising functionality behind an API and stop making changes to it
  * All new functionality is implemented as services that use the new arch
  * Can make calls to the old system if neccessary

BAD SYMPTOM OF BAD ARCHITECTURE: "My developers spend only 15% of their time coding - the rest of their time is spent in meetings"

## An Architecture that Enables Productivity, Testability, and Safety

### Architectural Archetypes: Monoliths vs Microservices

| Archetype | Pros | Cons |
|-|-|-|
| **Monolith v1** | Simple at first | Coordination overhead increases as team grows |
| All functionality in one app) | Low inter-process latencies | Poor enforcement of modularity |
| | Single codebase, one deployment unit | Poor scaling |
| | Resource efficient at small scales | **All or nothing deploy** |
| | | Long build times |
||
| **Monolith v2** | Simple at first | Tendency for increased coupling over time |
| Sets of monolith tiers | Join queries are easy | Poor scaling and redundancy (vertical only) |
| "front end" | Single schema deployments | Difficult to tune properly |
| "application server" | Resource efficient at small scales | All or nothing schema management |
| "database layer" | | |
||
| **Microservice** | Each unit is simple | Many cooperating units |
| Modular, independent | Independent scaling and performance | Many small repos |
| Graph relationships vs tiers | Independent testing and deployment | Requires more sophisticated tooling and dependency management |
| vs isolated persistence | Can optimally tune performance | Network latencies |

#### Amazon Service Oriented Arch Migration Lessons

* Lesson 1:
  * SOA are great for achieving isolation
* Lesson 2:
  * Prohibit direct access to databases
* Lesson 3:
  * Dev and Ops both benefit from switching
  * Enable strong customer focus

### Use the Strangler Application Pattern --> SAFE!

* Enable previous functionality to be:
  * Versioned
  * Become immutable
