# DevOps Handbook

* Be sure to look into infrastructure as code

## [Introduction](./INTRO.md)

## [Part 1: The Three Ways](./part_1_the_three_ways)

### [Chapter 1: The Manufacturing Value Stream](./part_1_the_three_ways/CHAPTER_1.md)

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

## [Part II: Where to Start](./part_2_where_to_start/)

### [Chapter 5: Selecting Which Value Stream to Start With](./part_2_where_to_start/CHAPTER_5.md)

* Apply lots of pressure and attention on the areas (and groups) most likely to budge
* **Not super fruitful to change the mind of people whose minds dont want to be changed**
* Demonstrate early wins
* Broadcast successes

### [Chapter 6: Understanding the Work in Our Value Stream, Making it Visible, and Expanding it Across the Organization](./part_2_where_to_start/CHAPTER_6.md)

* Create a value stream map - see chapter for more detail
* Create a dedicated transformation team
* Agree on shared goals (that can be measured)
* Ensure horizons and intervals are short
  * Short enough to ensure actionable data can be collected within weeks

#### Use MINIMUM 20% of time to paydown technical debt

* Documentation
* Refactoring
* Testing
* Automation

### [Chapter 7: How to Design Our Organization and Architecture with Conway's Law in Mind](./part_2_where_to_start/CHAPTER_7.md)

`The organization of the software and the organization of the software team will be congruent; commonly states as 'if you have four groups working on a compiler, youll get a 4-pass compiler'`

* Create loosely coupled architectures that have *bounded contexts*
* Keep teams small - "Two-Pizza Teams"
* Make sure everyone understands how they contribute to the value stream
* Generalists > specialists

### [Chapter 8: How to Get Great Outcomes by Integrating Operations into the Daily Work of Development]

* Need self service tools with ZERO lag time between needing a service and getting it
* On embedding: "Use the Ops engineers to lay the tracks and build the bridges, not just drive the train"

## [Part III: The First Way: The Technical Practices of Flow](./part_3_first_way_flow)

### [Chapter 9: Create the Foundations of Our Deployment Pipeline](./part_3_first_way/CHAPTER_9.md)

* Need self service environment creation
* Whether Ops uses version control is a higher predictor of IT and organizational performance than whether Dev uses is
* Used to treat servers like pets "You name them and when they get sick, you nurse them back to health. Now, servers are treated like cattle. You number them and when they get sick, you shoot them"
* The ONLY way to change a production environment is to completely rebuild from scratch
* At the end of each development interval, we have:
  * Integrated
  * Tested
  * Working
  * Potentially shippable code
  * **Demonstrated in a production-like environment**

### [Chapter 10: Enable Fast and Reliable Automated Testing](./part_3_first_way_flow/CHAPTER_10.md)

* Use an automated deployment pipeline to ensure that after every change the code successfully integrates into a production-like environment

