# Chapter 2: A Pragmatic Approach

## 7) The Evils of Duplication

"Giving a computer two contradictory pieces of knowledge was Captain James T. Kirk's preferred way of disabling marauding artificial intelligence"

### *Tip 11:* DRY - Dont Repeat Yourself

### How Does Duplication Arise?

* Imposed Duplication
  * Developers feel they have no choice - the environment seems to require duplication
  * Reserve code comments for high level explanations
* Inadvertent duplication
  * Developers dont realize that they are duplicating information
  * Usually due to mistakes in the design
* Impatient duplication
  * Developers get lazy and duplicate because it seems easier
  * Need a routine similar to one youve written?
    * Resist the urge to copy and modify
  * **"Shortcuts make for long delays"**
* Interdeveloper duplication
  * Multiple people on a team (or different teams) duplicate a piece of information
  * Have a team/project librarian

### *Tip 12:* Make it easy to reuse. (mmm, plan for reuse.)

## 8) Orthogonality

* Critical for growing systems that are easy to design, build, test and extend
* What is is?
  * Two lines are *independent*
  * In computing, known as decoupling

### *Tip 13:* Eliminate effects between unrelated things

* Design components that are well contained:
  * Independent, with a single, well-defined purpose
  * Aka *cohesion*

### Benefits

* Gain Productivity
  * Changes are localized, so dev and test time are reduced
  * Promotes reuse
* Reduce risk
  * Diseased sections of code are isolated
    * If a module is sick, it is less likely to spread they symptoms around the rest of the system
  * Resulting system is less fragile
  * Orthogonal systems will be better tested because its easier to design tests
  * You wont be tied to particulat platforms, vendors or products

### Project teams

* When there is overlap in team roles, everyone becomes reponsible

### Design

* Layer designs
  * More rigid way of diagramming
* Dont rely on things you cant control
  * Phone numbers as unique identifiers
  * Basically any input data

## Coding

* **Keep your code decoupled**
  * Write shy code - modules that dont reveal anything unneccessary
* **Avoid global data**
  * Avoid similar functions
  * Strategy pattern

## 9) Reversibility

"Nothing is more dangerous than an idea if its the one one you have"

### *Tip 14:* There are no final decisions

* Nothing is really actually set in stone, need to build components that protect themselves from change and have the least number of assumption
* Flexibility is a double edged sword
  * Maintaining flexible components can be a bigger nightmare than an immobile stone

## 10) Tracer Bullets

* Get feedback and dial in slowly
  * Dont guess up front and magdump haha
  * A small body of code has low inertia too
* These ar different from prototypes
  * Prototypes are meant to be thrown away
  * Think of prototyping as the recon and intel gathering that goes in before a single tracer is fired

### *Tip 15:* USe tracer bullets to find the target

### Advantages

* Users get to see something working clearly
* Developers build a structure to work in
* You have an integration platform
  * No big-bangs haha
* You have something to demonstrate
* You have a better feel for progress

## 11) Prototypes and Post-it Notes

* Prototypes dont have to be code
  * They can be diagrams, post-it notes, paperclips haha
* Main thing is theyre cheap and fast and can ignore unimportant details
  * However, if you find yourself unable to give up the details, a Tracer Bullet may be better
* **Make it abundantly clear that the code is disposable, incomplete, and unable to be completed**
  * **If the work environment is one that does not understand prototyping, stick with Tracer Bullets**

### Things to Prototype

* Anything youre uncomfortable with
* Anything that carries risk
* Anything that hasnt been tried before
* Anything thats unproven, experimental, or doubtful
* Things like:
  * Architecture
  * New functionality in an existing system
  * Structure or contents of external data
  * Third-party tools or components
  * Performance issues
  * UI design
* Main thing is it needs to be a learning experience

### *Tip 16:* Prototype to learn

### How to Use Prototypes

* Ignore details like:
  * Correctness
    * Use dummy data
  * Completeness
    * The prototype may function only in a very limited sense
  * Robustness
    * Error checking is not a priority haha
  * Style
    * Dont focus on documentation or comments

### Prototype Architecture

* Are responsibilities of major components well defined an appropriate?
* Are the collaborations between major components well defined?
* Is coupling minimized?
* Can you identify potential sources of duplication?
* Are interface definitions and constraints acceptable?
* Does every module have an access path to the data it needs during execution? Does it have that access when it needs it?

## 12) Domain Languages

"The limits of language are the limits of ones world"

### *Tip 17:* Program close to the domain language

* Aka, write code that reflects the domain in which its used
  * ADTs and well named routines
  * Write error handlers that say what the issue is in domain terms

## 13) Estimating

### *Tip 18:* Estimate to avoid surprises

* Deliver estimates with a feel for the audience
  * Dont get to granular or be too high level for the recipient
* 'days' imply a higher level of fidelity than 'months'

### Where Do Estimates Come From

* First, understand whats being asked
* Second, build a model of the system
  * Use the information you have at hand to do something high level
* Third, break the model into components
  * Identify parameters that contribute to the overall model
* Fourth, give each parameter a value
  * Want to focus on the parameters that have the most impact on the result - and concentrate on getting those right
* Fifth, calculate answers
* Finally, track how successful your estimates were

### This section doesnt use great language to explain things - just read an estimating book

### Estimating Project Schedules

* Iterate through the following
  * Check requirements
  * Analyze risk
  * Design, implement, integrate
  * Validate with users

### *Tip 19:* Iterate the schedule with code

* Use the timetables and effort measures from early functionality to hone in later estimates

### What to Say When Asked for and Estimate

"I'll get back to you"

* You can almost always get better results if you slow the process down and spend some time going through the steps we describe in this section
