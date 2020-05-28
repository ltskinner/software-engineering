# Testing

## Passes

### Archetype I: Program Protection

* Ensure the program runs when its supposed to
* Ensure the program fails when its supposed to

#### Pass 1: assert Statements

* Function inputs
* Subroutine outputs
* Note, there is a school of thought that suggests `turning these off in prod`

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
  * Also, try not to use `static variables` in your testing - better to rely on operations
    * (This is because if the program changes, so will the exepcted resulting static variables)
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

## QA

### Checklist

* [ ] Checklists from this folder are being used
* [ ] Results of the reviews are tracked and used to assess individual growth?
* [ ] Checklists are actually effective in improving system quality?

### Feedback

* [ ] Excellent communication lines maintained with client
* [ ] Communication with client is done over the medium they like most
* [ ] Client understands they cant be shiny blue object people
* [ ] Client understands that feedback is meant to ensure team is building what theyve committed to building
* [ ] Feedback cycles are as short and tight as possible
* [ ] Dev team gives client feedback on their feedback

## Environments

* [ ] A testing environment has been created?
* [ ] Test environment mimics dev environments?

## Tests

### Program Protection

### Unit Testing

* [ ] Unit tests are run on every pull request?
* [ ] Unit tests run fast enough to not impede development?
* [ ] Unit tests are kept up to date?
* [ ] Unit tests are created on pace with new functionality, if not before?

### Acceptance Tests

* [ ] Client has made time to witness or test new functionality
* [ ] Disparities between Dev understanding and Client expectation are addressed early and often

### Integration

* [ ] Integration tests effectively test the system?
* [ ] Test fixtures have been installed to allow faster (and more frequent) testing?

### Performance Tests

* [ ] Performance tests are in place?

### Maual Tests

* [ ] Manual tests are nearly eliminated?
