# Chapter 6: While You Are Coding

## 31) Programming by Coincidence

### *Tip 44:* Dont program by coincidence

* Basically if youre not deliberately putting evey piece of code in the order its in, but it still works, thats coincidence

### How to program deliberately

* Always be aware of what you are doing
* Dont build applications you dont fully understand
  * Or use technology you arent familliar with
* Always follow a plan
* Only rely on reliable things
  * Dont depend on accidents or assumptions
* Document your assumptions
* Dont just test your code: test your assumptions as well
  * Dont just guess, actually try it
* Prioritize your effort
  * Specifically on the important aspects
* Dont be a slave to history
  * Dont let existing code dictate future code

## 32) Algorithm Speed

### *Tip 45:* Estimate the order of your algorithms

### *Tip 46:* Test your estimates

## 33) Refactoring

* Software is like gardening
  * You have an initial plan, but some plants do well, and others die
  * Need to revise the plan as new information becomes available

### When to Refactor

* **Duplication**
  * Code violates the DRY principle
* **Non Orthogonal Design**
* **Outdated Knowledge**
* **Performance**

### *Tip 47:* Refactor early, refactor often

### How to Refactor

* Dont try to add functionality as you refactor
* Make sure you have good tests before you begin refactoring
  * Run these tests as often as possible
* Take short deliberate steps
  * Move a field from one class to another
  * Fuse two similar methods
* Fix code as soon as you recognize it needs to be fixed
  * If it hurts now, its going to hurt even more later
  * "Manage the pain"

## 34) Code thats Easy to Test

## Unit Testing

* Testing done on each module
  * Done in isolation
  * Done to verify behavior

### Test Againast the Contract

### *Tip 48:* Design to test

### Writing Unit Tests

* Unit test directories should be super easy to access
* Use a Testing Harness
  * Standard way to specify setup and cleanup
  * Methods for selecting individual tests or all available tests
  * Means for analyzing output for expected (and unexpected) results
  * Standardizes failure reporting
* Write tests to run in production too
* Make sure that logs are dumped somewhere easy to view
  * Creating a pretty way to look at logs is cool too

### Want to cultivate a culture of testing

## 35) Evil Wizards

* These are code generators provided by someone else
* The point where these become a problem is when the code becomes too interleaved with code written by the developer
  * When you lose the distinction, the developer begins to think wizard code is theirs (without actually understanding it)

### *Tip 50:* Dont use wizard code you dont understand
