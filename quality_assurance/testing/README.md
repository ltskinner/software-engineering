# Testing

## Passes

### Archetype I: Program Protection

* Ensure the program runs when its supposed to
* Ensure the program fails when its supposed to

#### Pass 1: assert Statements

* Function inputs
* Subroutine outputs

#### Pass 2: Exception handling

* Create test case for exception locations

### Archetype II: Program Operate as Expected

* Ensure the program takes the right control path on the right toggles
* **Very important that code is refactored to make testing this easy**
  * Namely, hiding multi if-statements behind routine interfaces
  * This allows you to test, and therefore trust, the if-logic
  * Then the control path toggled by it is implicitly secure

#### Leverage **Implicit** tests over **Explicit** tests

* Implicit Tests
  * If one step of the system is correct:
    * The steps after the tested step will have correct info
* Explicit Tests
  * If one step of the system is correct
    * And the next step of the system is correct
      * And the next step of the system is correct
        * And the next step of the system is correct
          * And the next step of the system is correct
            * And the next step of the system is correct
              * And the next step of the system is correct
                * And the next step of the system is correct
                  * And the next step of the system is correct

#### Pass 3: Control Operations

* if/else entry and exit
* for/while loop routines

#### Pass 4: Data Operations

* Critical:
  * Perform these tests on dummy data whose VALUES are VERY DIFFERENT from real data
  * Here, we are exclusively focusing on the raw operations
* Test any transform of any data that occurs
  * Sorting
  * Addition
  * Creating new columns
  * Filling NaNs
  * Removing NaNs
  * ETL sequences

### Archetype III: Data Validity

#### Pass 5: Data values are actually correct

(Not sold this must be done if everything else is tested)

#### Pass 6: Data Edges

* These are slow and bulky interfaces to
  * Flat files
  * Databases
  * Anything that takes more than 4 seconds to test
* Ideally, break these into their own suite
* Ideally, have these operations be insulated such that you can test everything around the slow interface
  * Do this without neccessitating calling the slow routines


## Program Protection

## Unit Testing

## Integration/System Testing

## Acceptance Testing
