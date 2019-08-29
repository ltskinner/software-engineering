# Chapter 13: The Whole and the Parts

"'I can write programs that control air traffic, intercept ballistic missiles, reconcile bank accounts, control production lines.' To which the answer comes, "So can I, and so can any man, but do they work when you do write them?"

## Designing the Bugs Out

### Bug-proofing the Definition

* The most annoying an subtle bugs are system bugs arising from mismatched assumptions made by the authors of various components
  * Conceptual integrity addresses this

### Testing the Specification

* Long before any code exists, the spec must be handed to an outside testing group for completeness and clarity
  * **Dont give it to the developers**
  * "They wont tell you they dont understand it; they will happily invent their ways through the gaps and obscurities"

### Top-Down Design

* As of 1971, top down design is the top dog
  * (CC did not echo this, rather a mix of top down and bottom up and watever the horizontal ones were)
* Best way to do top down is to design through a **sequence of refinement steps**
* Aids in discovery of modules
  * Areas of work whose further refinement can proceed independently of other work

#### Good top down design avoids bugs in several ways

* Clarity of structure and representation makes the precise statement of requirements and functions of the modules easier
* Partitioning and independence of modules avoids system bugs
* Suppression of detail makes flaws in the structure more apparent
* The design can be tested at each of its refinement steps, so testing can start earlier and focus on the proper level of detail at each step

## System Debugging

* **Use debugged components**
  * Only begin debugging the system with pieces that seem to work
* **Build tons of scaffolding**
  * Scaffolding is anything used just to test that will never go into the final product
    * Dummy components
    * Miniature files
    * Dummy files
    * Aux programs - like generators
* **Control Changes**
  * Make sure any changes made are tightly regimented and documented
  * Someone must be in charge
* **Add one component at a time**
  * Make sure that if things break, it is easy to track back to the most recent component
* **Quantize updates**
  * Do big updates at once
  * Instead of small and frequent
