# Chapter 3: The Basic Tools

Spend time to learn your tools

## 14) The Power of Plain Text

### *Tip 20:* Keep knowledge in plain text

* We have the ability to encode information representations as we please - use this effectively
* Insures against obsolescence
  * Human readable forms of data, and self-describing data will outlive all other forms of data and the applications that created them
* Easier to leverage
* Easier to test

## 15) Shell Games

* Get dope on the Shell
* With GUI, what you see is *all* you get

## 16) Power Editing

* It is better to know one editor very well, and use it for all editing tasks
* Pick one, know it thoroughly, and use it for all editing tasks
  * Want keystrokes to be reflex

### *Tip 22:* Use a single editor well

### Editor Features

* Configurable
  * All your preferences need to be able to be modified
  * Fonts, colors, window sizes, keystroke bindings
* Extensible
  * Shoudld be able to handle editing new languages and whatnot
* Programmable
  * You should be able to program the editor to perform complex, multistep tasks
* Other desirables:
  * Syntax highlighting
  * Auto-completion
  * Auto-indentation
  * Initial code or document boilerplate
  * Tie-in to help systems
  * IDE-like features (comple, debug, etc)

## 17) Source Code Control

"Progress, far from consisting in change, depends on retentiveness. Those who cannot remember the past are condemned to repeat it"

* A big advantage is being able to undo stuff

### *Tip 23:* Always use source code control

* Make sure absolutely **everything** is in source control
* Ensure source code builds are:
  * Automatic
  * Repeatable

## 18) Debugging

"It is a painful thing \n To look at your own trouble and know \n That you yourself and no one else has made it"

"When you see hoofprints, think horses - not zebras"

### Psychology of Debugging

* Just think of it as *problem solving*
* Dont let it devolve to passing blame

### *Tip 24:* Fix the problem, not the blame

### *Tip 25:* Dont panic (...)

### Process

* Start at the last place the code was working
* Isolate the problem as much as you can
* Strategies:
  * Visualize the data
  * Trace the program
    * Look over the context of time - not just now
  * Rubber duck
  * Use the process of elimination
* Dont assume it - prove it

### Debugging Checklist

* Is the problem reported a direct result of the underlying bug, or merely a symptom
* Is the bug *really* in the compiler? Is it in the OS? Or is it in your code?
* If you explained this problem in detail to a coworker, what would you say?
* If the suspect code passes its unit tests, are the tests complete enough? What happens if you run the unit test with *this* data?
* Do the conditions that caused this bug exist anywhere else in the system?

## 19) Text Manipulation

### *Tip 28:* Learn a text manipulation language

* Python and Perl are noted here. Not sure what the focus of this is??
  * But I guess im more used to text cleaning than anything else haha

## 20) Code generators

### *Tip 29:* Write code that writes code

### Types

* Passive Code Generators
  * Run once to produce a results
  * The result is freestanding and has no more relation to the code generator
  * Mostly to save typing
  * Uses
    * Creating new source files (like copyrights)
    * Performing one off conversions
    * Producing lookup tables or other resources that are expensive to compute at runtime
* Active Code Generators
  * Used each time their results are required
  * The results are throw-away - it can always be reproduced by the generator
  * Example
    * Need datatypes to be generated as the result of a database schema
    * Have a section read the DB then get the cols
    * As opposed to updating hardcoded cols
  * Example 2:
    * Have a language neutral doc
    * Have a generator for creating
      * C
      * Pascal
