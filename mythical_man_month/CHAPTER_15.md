# Chapter 15: The Other Face

"What we do not understnad we do not possess"

## What Documentation Is Required

### To Use a Program

#### Be real slow and step wayyy back

* Purpose
  * What is the main function, the reason for the program?
* Environment
  * On what machine, hardware configurations, and operating system configurations will it run?
* Domain and Range
  * What domain of input is valid?
  * What range of output can legitimately appear?
* Functions Realized and Algorithms Used
  * Precisely what does it do?
* Input-Output Formats
  * Precise and complete
* Operating Instructions
  * Inlcuding normal and abnormal behavior, as seen at the console and on the outputs
* Options
  * What choices does the user have about functions?
  * Exactly how are those choices specified?
* Running Time
  * How long does it take to do a problem of specified size on a specified configuration?
* Accuracy and Checking
  * How precise are the answers expected to be?
  * What means of checking accuracy are we incorporating?
* All this should be done in like 3-4 pages

### To Believe a Program

#### Need to ship some small test cases that can be used to reassure the user

* Mainline cases that test the programs chief functions for commonly encountered data
* Barely legitimate cases that proble the edge of the input data domain, ensuring that the largest poissible value, smalles possible value, and all kinds of valid exceptions work
* Barely illegitimate cases that proble the domain boundary from the other side, ensuring that invalid inputs raise proper diagnostic messages

### To Modify a Program

#### Modifying a program requires a lot more info haha

* A flow chart of subprogram structure graph
* Complete descriptions of the algorithms used, or else references to such descriptions in the literature
* An explanation of the layout of all files used
* An overview of the pass structure - the sequences in which data or programs are brought from tape or disk - and what is accomplished on each pass
* A discussion of modifications contemplated in the original design, the nature and location of hooks and exits, and discursive discussion of the ideas of the original author about what modifications might be desirable and how one might proceed. His observations on hidden pitfalls are also useful

## The Flow-Chart Curse

* Flow charts are usually oversold
  * These show the decision structure of the program
* "Why lay a load on their backs which neither our ancestors nor we ourselves were able to carry?"
