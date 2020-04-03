# Code Complete Requirements Checklist

## Functionality Specifications

* [ ] **System**
  * [ ] **Inputs**
    * [ ] source
    * [ ] accuracy
    * [ ] range of values
    * [ ] frequency
  * [ ] **Outputs**
    * [ ] destination
    * [ ] accuracy
    * [ ] range of values
    * [ ] frequency
    * [ ] format
  * [ ] **Results formats**
    * [ ] Web pages
    * [ ] reports
    * [ ] etc.
* [ ] Each **Task**
  * [ ] **Input** data and format
  * [ ] **Output** data and format
* [ ] **External interfaces**
  * [ ] hardware
    * [ ] disk space
    * [ ] memory
    * [ ] GPU specs
  * [ ] software
  * [ ] communication
    * [ ] handshakes
    * [ ] error-checking
    * [ ] protocols

## Quality

* [ ] Definitions of:
  * [ ] success
  * [ ] failure
* [ ] Timing considerations
  * [ ] response to user for all tasks
  * [ ] processing time
  * [ ] datatransfer rate
  * [ ] system throughput
* [ ] Reliability
  * [ ] consequences of software failure
  * [ ] protecting vital information
  * [ ] error detection and recovery strategy
* [ ] Security expectations

## Quality of Requirements

* [ ] **Understandable** by users
* [ ] **All possible changes to the requirements specified**
  * [ ] Likelihood of each change
* [ ] Requirements don't specify the design
* [ ] Requirements **avoid conflicts** with each other
* [ ] **Tradeoffs** between competing attributes specified
  * Ex. between robustness and correctness
* [ ] Consistent level of **detail**
  * [ ] Should any be specified in **more** detail?
  * [ ] Should any be specified in **less** detail?
* [ ] **Clear** and easy to understand
  * [ ] enough for an independent group to understand?
  * [ ] developers agree?
* [ ] All items are **relevant**
  * [ ] **solutions** to each item are relevant as well
  * [ ] **origin** of each item in the problem environment is tracable
* [ ] Each requirement is **testable**
  * [ ] able to be independently tested

## Requirements Completeness

* [ ] Areas of **incomplete information** specified
  * [ ] Information that is **unavailable** when development begins
* [ ] **Comfortable** with **all** the requirements
  * [ ] **NO** **impossible** to implement reqs
  * [ ] **NO** reqs that only serve to **appease** a customer or boss
* [ ] If every requirement is satisifed, will the product be acceptable?
