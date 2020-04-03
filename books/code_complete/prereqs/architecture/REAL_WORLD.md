# Real World Considerations

## Architectural Feasability

* Must demonstrate the system is technically feasible
* If any issues, it needs to be indicated how those issues have been investigated

## Business Rules and Constraints

* If the architecture depends on specific business rules, these need to be identified and their impact explained
  * Lifespan of customer data forcing certain updates
    * (the mybama 20min timeout thing)

## Buy-vs-Build Decisions

* If not using off the shelf, need to justify how building will result in better performance than ready-made libraries and components

## Reuse Decisions

* If plans call to reuse existing
  * Software
  * Test cases
  * Data formats
* Must elaborate on how reused components will be made to conform to other architectural goals

## Interoperability

* If a system is expected to share data or resources with other software or hardware, how that is accomplished needs to be described

## Change Strategy

* Need to make architecture flexible enough to accommodate changes
* Likely changes include
  * Volatile data types
  * File formats
  * Changed functionality
  * New features
  * Etc
* Show anticipated changes and benefits of the changes
  * “possible enhancements"
