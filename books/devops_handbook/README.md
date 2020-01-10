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

### [Chapter 2: The First Way: The Principles of Flow](./part_1_the_three_ways/CHAPTER_2.md)

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

### [Chapter 3: The Second Way: The Principles of Feedback](./part_1_the_three_ways/CHAPTER_3.md)

* Get feedback frequently and as soon as possible to make course corrections
* See problems as they occur - use lots of testing and telemetry to monitor
* Swarm everyone to problems so that they learn from the mistakes of others
* **According to Lean, the most important customer is the next step downstream**

### [Chapter 4: The Third Way: The Principles of Continual Learning and Experimentation](./part_1_the_three_ways/CHAPTER_4.md)

"By removing blame, you remove fear; by removing fear, you enable honestly; and honesty enables prevention"

* Turn `individual knowledge`
  * Into `team knowledge`
    * Into `organizational knowledge`
* Need to reinforce a `high trust culture` that encourages `risk taking` to the end of continually learning and improving
* Seek to **understand why** accident happened, not find blame
* If things are not bring improved, they dont stay the same, they actually degrade over time
  * Use `kaizen blitzes` to get the whole team free from actual work to improve whatever they want
    * In between sprints?
    * In between milestones?
* **NEED CENTRAL KNOWLEDGE BASE THAT EVERYONE ADDS TO**
