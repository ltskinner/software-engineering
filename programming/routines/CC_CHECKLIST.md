# Code Complete Routine Checklist

## Big Picture

* [ ] Routine has a good reason for being created
* [ ] All parts of routine put into routines of their own
* [ ] Routine has strong, clear name
  * [ ] `1) Strong Verb`
  * [ ] `2) Object`
  * [ ] describes everything the routine does
* [ ] Naming convention established
* [ ] Routine does one thing and only one thing really well
* [ ] Routines are loosely coupled
  * [ ] connections to other routines are
    * [ ] small
    * [ ] intimate
    * [ ] visible
    * [ ] flexible
* [ ] Routine lenght determined by its function and logic, not arbitrary standard

## Parameter Passing Issues

* [ ] Parameters present a consistent interface abstraction
* [ ] Routine parameters in sensible order
  * [ ] order matches other similar routines
* [ ] Interface assumptions documented
* [ ] Routine has 7 or fewer params
* [ ] Input parameters not used as working variables
* [ ] Returns valid value in all circumstances (if expected to)

## Key Points

* [ ] Routine created for good reason
  * [ ] improves intellectual manageability
  * [ ] improves readability
  * [ ] improves reliability
  * [ ] improves modifiability
* [ ] Simple operations that would benefit from their own routine have them
* [ ] Routine names are good
  * [ ] Routines with bad names are changed functionally
