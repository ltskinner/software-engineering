# Compartmentalization

Main goal is to keep changes from rippling outside of the implementation

## Information Hiding Main Concepts

* Mostly about hiding **complexity**
  * Kindof about kiding provate information
* Class interfaces should be complete, but minimal
  * Reveal as little about the inner workings as possible
* In info hiding, each class (or package or routine) has secrets


## Two Categories of Secrets

1. Hiding complexity so that your brain doesnt have to deal with it unless youre specifically concerned with it
2. Hiding source changes so that when changes occur, the effects are localized

## Barriers to Information Hiding

* In some cases, info hiding is truly impossible
  * But, most of the time, **barriers are just mental blocks built on old habits**
* Don't use `100` use `MAX_EMPLOYEES = 100`
* Don't interleave user interaction
  * User interactions hould be in a single class, package or subsystem
  * Cannot have UI changes affecting the whole system
* Don't use circular dependencies
* Global data is cancer
  * Use class data instead
* Don't worry about perceived performance penalties
  * **Until you can measure system performance, dont sweat it**
  * As long as the design is highly modular, even if changes arise, it will be easy to modify

## Value of Information Hiding

* Studys have found programs using info hiding are **4x easier ot modify**
* Get in the habit of asking "What should I hide?"

## Abstraction

The ability to engage in a concept while ignoring some details

**Create abstractions at the following levels:**

* routine-interface level
* class-interface level
* package-interface level

## Encapsulation

Want to encapsulate the actual implementation details - picks up where abstraction leaves off

* Abstraction says: "You're allowed ot look at an object at a high level of detail"
* Encapsulation says: "Furthermore, you arent allowed to look at an object at any other level of detail"

### Example

Assigning `id++` is **bad**

* Not thead safe
* What if wanted non-sequential for security?
* What if wanted to reuse destroyed ids?

Abstract to `id = newID()`

* Here, you can play with the implementation behind an abstraction layer now

**Also,** will want to declare an `id` as its own datatype

* That way can resolve to int
* Or change to resolve to string without changing anything anywhere else in the code
