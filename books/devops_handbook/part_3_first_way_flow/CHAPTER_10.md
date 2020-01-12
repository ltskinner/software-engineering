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
