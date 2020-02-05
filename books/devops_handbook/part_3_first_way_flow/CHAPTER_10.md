# Chapter 10: Enable Fast and Reliable Automated Testing

## Automate testing on push to cource control

## Continuously Build, Test and Integrate our Code Environments

### Why automated build and test processes are critical

* Our build and test processes can run all the time, independent of the work habits of individual engineers
* A segregated build and test process ensure that we understand all the dependenceis required to build, package, run, and test our code
  * No more "it worked on my machine"
* We can package our aplication to enable the repeated installation of code and configurations into an environment
* Instead of putting our code in packages, may choose to package our applications into deployable containers
* Environments can be made more production-like in a way that is consistent and repeatable
  * Like removing compilers from env, debugging flags are turned off

### Deployment pipeline

* Commit stage (automated)
* Acceptance stage (automated)
  * Static code analysis
  * Duplication and test coverage analysis
  * Style checking
* Exploratory testing (manual)
* User Acceptance Testing (UAT) (manual)
* Staging (manual)
* Production (manual)

### Create the Continouout Integration practices with the following capabilities:

* A comprehensive and reliable set of automated tests that validate we are in a deployable state
* A culture that "stops the entire production line" when our validation tests fail
* Developers working in small batches on trunk rather than long lived feature branches

### Build a Fast and Reliable Automated Validation Test Suite

* Primary goal is to know when something is break as soon as possible after the change was introduced so its easy to remove
  * Single worst thing this incurrs: `devs know the build is always broken, so changes arent checked in until big banged the night before the product is due`

#### Unit Tests ~ 10 min

* Single method, class, function tested in isolation
* Need to be kept fast and stateless
* Unit tests often 'stub out' databases and external dependedcies
  * Modified to refurn static, predefined values instead of calling a real DB

#### Acceptance Tests

* Prove the program works as the client expects it to
  * NOT how the programmer expects it to
* After this step, tests are mada available for integration testing

#### Integration Tests ~ A couple hours

* Makes sure the program plays nice with other applications and services
* Want severely minimize the number of integration tests
* MUST be able to simulate remote services

### Write Automated Tests BEFORE the Code

* 1) Write a tests that validates the expected behavior fails
* 2) Write the code that makes teh test pass

#### Formally:

* Ensure the tests fail. "Write a test for the next bit of functionality you want to add." Check in.
* Ensure the tests pass. "Write the functional code until the test passes." Check in.
* Refactor both new and old code to make it well structured." Ensure the tests pass. Check in again.

### Integrate Performance Testing Into Test Suite

* Dont want to wait till production to realize the app doesnt perform as expected
* Write tests that span the whole stack
  * Network, database, storage, other
* Want to uncover unforseen limitations

#### Things to Look For

* Database query times grow non-linearly
  * (forgot to turn on indexing)
* Code change causes # of DB, storage, network calls to increase tenfold

#### Tips

* Build performance tests first so you dont have to retrofit a testing env that will handle it
* Fail performance tests on 2% slower than previous run

### Integrate NonFunctional Requirements Testing

* Supporting applications, databases, libraries
* Language interpreters, compilers
* Operating systems
* All dependencies

## Pull the Andon Cord When Deployment Pipeline Breaks

* Emphasis on a prioritization of team goals over individual goals
* Whoever broke the system gets full access to anyone and everyone to help solve
