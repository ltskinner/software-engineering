# DevOps Handbook

* Be sure to look into infrastructure as code

## (Introduction)(./INTRO.md)

## (Part 1: The Three Ways)(./part_1_the_three_ways)

### (Chapter 1: The Manufacturing Value Stream)(./part_1_the_three_ways/CHAPTER_1.md)

* "Best indicator of value is the lead time"
* How to minimize?
  * Smooth and even workflows
  * Small batch sizes
  * Reducing work in progress (WIP)
  * Preventing the need for rework
  * Dont pass defects downstream

### Chapter 2:

"Stop starting. Start finishing"

#### Codify and enforce WIP limits

* **NO MORE THAN A CERTAIN NUMBER OF CARDS PER PERSON PER COLUMN**
* Must ensure that no work can be performed unless its on a card
  * Pattern sections like reqs, design, arch, testing dont need their own cards - just swimlanes
* Keep pace of development as steady as possible
  * Bottlenecks at any point need to be ironed out at any cost
  * There is no reason to optimize before or after a bottleneck so long as the bottleneck exists
* **Reliance on anything that cant be automated is a liability**
* If anyone has to do anything unreasonable to bring it to production, thats a big problem
