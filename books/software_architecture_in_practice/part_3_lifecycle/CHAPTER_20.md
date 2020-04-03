# Chapter 20: Architecture Reconstruction and Conformance

* Architecture reconstruction serves to:
  * Document where documenatation never existed (or is hopelessly out of date)
  * To ensure conformance between the as-built and the designed architecture

## 20.1 Architecture Reconstruction Process

### Raw View Extraction

* Raw information is obtained from
  * Source code
  * Execution traces
  * Build scripts
* These are called views
* Strive to answer specific questions about the architecture
  * Elements, relations

### Database Construction

* Converting raw extracted information into a standard form
* This is then put into a database
* The database is then used to generate authoritative architecture documentation

### View Fusion and Manipulation

* Combines various views of all the information stored in the database

### Archtiecture Analysis: Finding Violations

* View fusion creates a bunch of hypotheses about the architecture
* With these hypotheses, can begin evaluation
* How to test:
  * Conformange by Construction
    * Can use generators to produce backbone components of the desired architecture
  * Conformance by Analysis
    * Reverse engineer a system
    * Raise red flags as appropriate
    * Bring offenders back to conformance

## 20.6 Guidelines

* Have a goal and set of objectives or questions in mind before starting
* Obtain some representation, no matter how rough, before beginning reconstruction
  * Identifies which information needs to be extracted
  * Guides the reconstructor in determining what to look for and what views to generate
* Use old docs to reconstruct initial views, but dont be afraid to throw away
* Leverage reconstruction tools as best you can
