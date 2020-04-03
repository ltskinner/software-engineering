# Programmatic Considerations

## Program Organization

* Made up of blocks
  * Single tasks
  * Collections of classes and routines
* Every feature listed in requirements should be covered by at least one building block
  * If a function is claimed by more than one block, their claims should cooperate not conflict
* Each blocks responsibility should be well defined and compartmentalized
  * Abstract and encapsulate information as well as possible
* Communication between blocks should be well defined
  * Which blocks can access others and how those lines are done
* Rationale for every decision needs to be documented
  * This is at least as important as the design itself

## Major Classes

* Specify the 20% of classes that make up 80% of the system behavior
* Identify responsibilities and other class info
  * Class hierarchies
  * States of transition
  * Object persistence
  * Subsystems

## Data Design

* Describe major files and table designs
  * Note alternatives and justify decisions
* Databases and their contents
  * Why database over flat file? What interactions and views are created? etc.
* **Every decision made about the data**

## User Interface Design

* Anywhere the user touches it
  * API, GUI, Web, CLI
* Want to ensure modular design so new UIs can be plugged in easily

## Overengineering Decision

* Clearly indicate whether programmers should err on the side of overengineering or simplicity
* By setting expectations explicitly in the architecture, you can avoid cases where some classes are exceptionally robust and others aren’t
