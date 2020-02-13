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

### [Chapter 8: How to Get Great Outcomes by Integrating Operations into the Daily Work of Development](./part_2_where_to_start/CHAPTER_8.md)

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

"Although testing can be automated, creating quality cannot. To have humans executing tests that should be automated is a waste of human potential."

* Use an automated deployment pipeline to ensure that after every change the code successfully integrates into a production-like environment
* Primary goal is to know when something is break as soon as possible after the change was introduced so its easy to remove
  * Single worst thing this incurrs: `devs know the build is always broken, so changes arent checked in until big banged the night before the product is due`
* Focus on tests that validate the business goals
  * Prefer a small number of great tests, over a large number of FP tests
  * Macys had 10 tests they deved with for years, then slowly built out

### [Chapter 11: Enable and Practice Continouous Integration](./part_3_first_way_flow/CHAPTER_11.md)

"Without automated testing, CI is the fastest way to get a big pile of junk that never compiles or runs correctly"

* When merging is difficult, we become less able and less motivated to improve and refactor code
  * this is because refactors are more likely to cause rework for everyone else

"When we do not aggressively refactor our codebase, it becomes more difficult to make changes and to maintain over time, slowing down the rate at which we can add new features"

### [Chapter 12: Automate and Enable Low-Risk Releases](./part_3_first_way_flow/CHAPTER_12.md)

* Green-blue releases are dope
* Dark launches are dope too
  * Just use invisible triggers to spool functionality without actually displaying
  * Leverage internal controls
  * Leverage external configs

"Deployments should be low-risk, push-button events we can perform on demand"

### [Chapter 13: Architect for Low-Risk Releases](./part_3_first_way_flow/CHAPTER_13.md)

"Both eBay and Google are each on their fifth entire rewrite of their architecture from top to bottom"

* bruh, thats how i feel

BAD SYMPTOM OF BAD ARCHITECTURE: "My developers spend only 15% of their time coding - the rest of their time is spent in meetings"

## [Part IV: The Second Way - The Technical Practices of Feedback](./part_4_second_way_feedback)

* Create telemetry to enable seeing and solving problems
* Use telemetry to better anticipate problems and achieve goals
* Integrate user research and feedback into the work of product teams
* Enable feedback so Dev and Ops can safely perform deployments
* Enable feedback to increase the quality of our work through peer reviews and pair programming

### [Chapter 14: Create Telemetry to Enable Seeing and Solving Problems](./part_4_second_way_feedback/CHAPTER_14.md)

"If it moves, we track it"

* Need libraries and infrastructure to make it dummy easy for people in both Dev and Ops to create telemetry for ANY functionality they build

`information radiator`: "The generic term for any of a number of handwritten, drawn, printer, or electronic displays which a team places in a highly visible location, so that all team members as well as passers-by can see the latest information at a glance: count of automated tests, velocity, incident reports, CI status, and so on. This idea originated as part of the Toyota Production System"

* Team has nothing to hide from its visitors (customers, stakeholders, etc)
* Team has nothing to hide from itself: it acknowledges and confronts problems

#### Only store actionable metrics

### [Chapter 15: Analyze Telemetry to better Anticipate Problems and Achieve Goals](./part_4_second_way_feedback/CHAPTER_15.md)

"Given a herd of cattle that all look and act the same, which cattle look different from the rest? Or more concretely, if we have a thousand-node stateless compute cluster, all running the same software and sibject to the same approximate traffic load, our challence is to find any nodes that dont look like the rest of the nodes"

* Use Business Intelligence people to help interpret time series stuff

### [Chapter 16: Enable Feedback So Development and Operations Can Safely Deploy Code](./part_4_second_way_feedback/CHAPTER_16.md)

* Main goal is to ensure new features are operating as expected once deployed
* Also want to ensure that another service has not been broken
* Make sure everyone in the value stream shares downstream responsibilities of something breaking
  * "We found that when we woke up developers at 2 a.m., defects were fixed faster than ever"
* Create mechanism for Ops to `hand-back` deployed services back to the dev team so they arent burdened
  * Leverage `Launch Readiness Reviews` and `Hand-Off Readiness Review`

### [Chapter 17: Integrate Hypothesis-Driven Deployment and A/B Testing into Our Daily Work](./part_4_second_way_feedback/CHAPTER_17.md)

Before we build a feature, we should rigorously ask ourselves, "Should we build it, and why?"

"Research suggests that 2/3rds of feature 'enhancements' actually have no effect or are even detrimental"

### [Chapter 18: Create Review and Coordination Processes to Increase Quality of Our Current Work](./part_4_second_way_feedback/CHAPTER_18.md)

* Primary goal is to reduce risk of production changes before they are made

* With respect to "Overly regulated change control management"
  * "The people closest to a problem typically know the most about it"
  * Going up the food chain to people that dont know shit usually ends poorly

"Ask a programmer to review ten lines of code, he'll find ten issues. Ask him to do 500 lines, and he'll say it looks good" HAHA
