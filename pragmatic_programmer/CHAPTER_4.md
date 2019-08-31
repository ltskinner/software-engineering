# Chapter 4: Pragmatic Paranoia

### *Tip 30:* You cant write perfect software

"They dont trust themselves, either"

* Defend yourself from your own damn mistakes
  * As much and more than from outside offenders

## 21) Design by Contract

* Defines your rights and responsibilities, as well as those of the other party

### Expectations

* **Preconditions**
  * What must be true in order for the routine to be called
  * The routines requirements
* **Postconditions**
  * What the routine is guaranteed to do
* **Class invariants**
  * A class ensures that this condition is always true from the persepctive of the caller

### *Tip 31:* Design with contracts

* Be strict in what you will accept before you begin
* Promise as little as possible in return

### Implementing DBC

* Forces the issue of requirements and guarantees to the forefront
  * Without doing this, you are merely programming by coincidence
* **Assertions** are very helpful
* Aids in the concept of forceful crashes early on
  * When a contract is broken, everybody knows about it haha
* Loop issues
  * Banana problem
    * "I know how to spell 'banana' but I dont know when to stop"
  * Fencepost errors
    * Whether to count the fenceposts or the spaces between them
  * Off by one errors

## 22) Dead Programs Tell No Lies

### *Tip 32:* Crash early

### Crash, Dont Trash

* Much better to be dead than wreak unknown havoc

## 23) Assertive Programming

### **Tip 33:** If it cant happen, use assertions to ensure that it wont

* Dont turn off assertions in shipped code
* The wild is much more perilous than any testing environment

## 24) When to Use Exceptions

* Good to use when other error handling results in modifying the flow of the program
* Traditional error handlers are better

### *Tip 34:* Use exceptions for exceptional problems

## 25) How to Balance Resources

* This is mainly about resource allocation and deallocation

### *Tip 35:* Finish what you start

* Open and close files in the same control regime
