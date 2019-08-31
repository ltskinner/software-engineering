# Chapter 8: Pragmatic Projects

## 41) Pragmatic Teams

* **No Broken Windows**
* **Dont Let Frogs Boil**
  * Dedicate someone to checking for:
    * Increased scope
    * Decreased time scales
    * Additional features
    * New environments
    * Anything that wasnt in the original agreement
* **Communicate Effectively**
  * Be easy to work with
  * Create a team brand
* **Dont Repeat Yourself**
  * Project librarian
* **Keep Things Orthogonal**
  * Use subteams
* **Automate**
  * Everything within reason
  * Important for maintaining consistency and accuracy
  * Appoint someone to be responsible for building tools that automate the drudgery

### *Tip 60:* Organize around functionality, not job functions

## 41) Ubiquitous Automation

"Civilization advances by extending the number of important operations we can perform without thinking"

### All on Automatic

### *Tip 61:* Dont use manual procedures

* If a human has to do more than one step, theyre gonna goof it up
* Automate for the sake of repeatability and consistency
* Build and tests projects every night

### Automate Administrative Tasks

* Little distractions like email, paperwork, approval stuff needs to be as automated as possible
* Websites and other stuff should be automatic too

## 43: Rutheless Testing

* Strive to find bugs *now* instead of having to endure the shame of someone else finding our bugs later
* Think of it as fishing
  * Small nets to catch minnows (Unit tests)
  * Big nets to catch (Integration tests)

### *Tip 62:* Test early. Test often. Test automatically

* Minnows have a habit of becoming sharks if left to grow

### *Tip 63:* Coding aint done till all the tests run

### What to Test

* Unit testing
  * If the modules and parts dont work on their own, they surely wont work in conjunction with other modules hshs
* Integration testing
  * Shows that the subsystems play nice with each other
  * This is the single largest source of bugs in the system
* Validation and verification
  * Does the built system meet the functional requirements?
* Resource exhaustion, errors, and recovery
  * See how the program performs under real world conditions
* Performance testing
  * Stress testing and load testing
  * Check scalability too
* Usability testing
  * Look at it in terms of human factors
  * Were there any misunderstandings in the requirements?

### How to Test

* Regression testing
  * Compare the output of current tests with the outputs of previous tests
  * Ensures the "fixes" of today didnt break anything
* Test data
  * Real world
  * Synthetic
    * For lots of data
    * Stress testing boundary conditions
    * Data that exhibits statistical properties
* Exercising GUI systems
* Testing the tests
  * Deliberately cause bugs
  * Introduce a dedicated project saboteur whos trying to break everything
* Testing thoroughly
  * Use **coverage analysis** tools to see your testing coverage percentage

### *Tip 64:* Use saboteurs to tests your testing

### *Tip 65:* Test state coverage, not code coverage

#### Some Metrics

* McCabe Cyclomatic Complexity Metric
  * Complexity of decision structures
* Inheritance fan in and fan out
* Response set
* Class coupling ratios

### *Tip 66:* Find bugs once

* Once a bug has been found, it should never ever appear again

## 44) Its All Writing

"The palest ink is better than the best memory"

### *Tip 67:* Treat english as just another programming language

### *Tip 68:* Build documentation in, dont bolt it on

### Comments in Code

* Code should have comments, but too many can be just as bad as too few
* Comments should express the *why*
  * The code itself should already show the *how*
* Make sure names are meaningful
  * Misnomers are even more deadly than gibberish

### Executable Documents

* Suppose there is a spec list that has the columns in a database table
* There is another set of SQL commands to create the actual table
* Additionally there is a record of the schema somewhere in some code files
* Here, information is repeated THREE times
* Select an authoritative source of information
  * Let this be readable and have it become an integral part of the system

### Print It or Weave It

* Basically, keep things online so that they get updated and old information disappears

## 45) Great Expectations

### *Tip 69:* Gently exceed your users expectations

* Going overboard and doing what they werent expecting is as bad as not doing enough
* Give them just a lil more than they were expecting
  * Typically, this is on the user interface side
    * Balloon or ToolTip help
    * Keyboard shortcuts
    * A quick reference guide as a supplement to the users manual
    * Colorization
    * Log file analyzers
    * Automated installation
    * Tools for checking the integrity of the system
    * The ability to run multiple versions of the system for training
    * A splash screen customized for their organization

## 46) Pride and Prejudice

### *Tip 70:* Sign your work

* Anonymity, especially on large projects, provides a breeding ground for:
  * Sloppiness
  * Mistakes
  * Sloth
  * Bad code
