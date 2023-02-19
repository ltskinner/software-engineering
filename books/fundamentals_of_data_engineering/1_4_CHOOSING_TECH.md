# Chapter 4. Choosing Technologies Across the Data Engineering Lifecycle

Does the data technology add value to a data product and the broader business?

Architecture first, technology second:

- Architecture is strategic - the what, why, and when
- Tools are tactical - the how

Considerations:

- Team size and capabilities
- Speed to market
- Interoperability
- Cost optimization and business value
- Today versus the future: immutable vs transitory technologies
- Location (cloud, on-prem, hybrid cloud, multicloud)
- Build vs buy
- Monolith vs modular
- Serverless versus servers
- Optimization, performance, and the benchmark wars
- The undercurrents of the data engineering lifecycle

## Team Size and Capabilities

Can people specialize or do they need to wear lots of hats?

For small teams, focus on solving the problems that directly add value to the business right

- Do people lean toward low code tools, or do they favor code first approaches?
- What languages do folks like?

## Speed to Market

In technology, speed to market wins

Slow decisions and output are the kiss of death to data teams

Deliver value early and often

## Interoperability

How well various technologies and systems connect, exchange information, and interact

## Cost Optimization and Business Value

Budgets and time are finite

Cost is a major constraint for choosing the right data architecture and technologies

### Total Cost of Ownership

- total estimated cost of an initiative, including the direct, and indirect costs
  - Direct costs - salaries of team
  - Indirect costs - overhead, independent of initiative must be paid

How something is purchased matters too:

- Capital expenses
  - require up front investment
- Operational expenses
  - spread out over time, pay as you go

### Total Opportunity Cost of Ownership

- cost of lost opportunities as a result of making a certain decision - the things you no longer have resources for
- best way to minimize is stay flexible and make reversible decisions
  - inflexible technologies are a lot like bear traps
    - easy to get into, and painful to escape

### "FinOps"

The goal of FinOps is to fully operationalize financial accountability and business value by applying DevOps-like practices of monitoring and dynamically adjusting systems

The goal here is to make money

## Today vs the Future: Imutable vs Transitory Technologies

Choose the best technology for the moment and near future, but in a way that supports future unknowns and evolution

- Immutable technologies
  - components taht underpin the cloud, or languages and paradigms that have stood the test of time
  - like, object storage, networking, servers, security
  - Lindy effect: the longer a technology has been established, the longer it will be used
- Transitory technologies:
  - ones that come and go
  - lots of hype

Suggestions:

- Evaluate tools every two years - and look two years in advance
- Find immutable technologies and use those as the base
  - Build the transitory tools around the immutable ones
- Ask, what are the barriers to leaving a chosen technology?

## Location

- On Prem
- Cloud
- Hybrid Cloud
- Multicloud
  - basically dont just use AWS lol

Ya ill cross the non-cloud bridge when I gotta lmao

### Decentralized: Blockchain and the Edge

Blockchain, web 3.0, and edge computing will facilitate decentralized shit

### Advice for selecting multicloud

- Do you need to serve data near customers on multiple clouds?
- Do industry regulations require you to house certain data in your datacenters?
- Do you have a compelling technology need for specific services on two different clouds?

Generally, have an escape plan to avoid lock in

## Build vs Buy

Build and cusomize **only** when it provides a competitive advantage for the buiness

### Community managed OSS

- Mindshare: avoid adopting tools taht done have traction and popularity
  - make sure issues are like polite and well handled
- Maturity: how old is the project?
- Troubleshooting: can community help solve the problem
- Project management: are issues addressed quickly
- Team: is a company sponsoring the project?
- Developer relations and community management: what is the project doig to encourage uptake
- Contributing: does the project encourage and accept pull requests
- Roadmap: is there a project roadmap and does it make sense
- Self-hosting and maintenance:
- Giving back to the community: how can you help

### Commercial OSS

- Value: is the paid version really worth it?
- Delivery model: how do you access the service? download, api, web/mobile ui?
- Support: what is the support model for the product, and is there and extra cost for support?
- Releases and bug fixes: is the vendor transperent
- Sales cycle and pricing: be sure to understand the tradeoffs
- Company finances: how much runway does the company have, and will it still be in business in a few years?
- Logos versus revenue: does the company care more about number of users or revenue? They gotta have their finances on lock
- Community support

### Non Open Source Shit

- Interoperability: the tools must play nice with other tools in the stack
- Mindshare and market share: is the offering popular? do people actually like it?
- Documentation and support: how good are the docs
- Pricing: does pricing make sense and is affordable/worthwhile
- Longevity: will the company survive long enough to get value from the product

## Monlith vs Modular

### Monolith

Pros:

- easy to understand
- requires lower cognitive burden and context switching

Cons:

- brittle

### Modularity

Teams of 5 are pretty good

The ability to swap out tools as technology changes is invaluable

Proper orchustration is kindof required here

#### The Distributed Monolith Pattern

## Serverless vs Servers

Serverless is so hot rn

Handling one event perfunction call can be catastrophically expensive, especially when simpler approaches liek multithreading or multiprocessing are great alternatives

Monitor to determine cost per event in real world, what happens in the extremes?

Considerations:

- Expect servers to fail
  - cows
- Use clusters and autoscaling
  - take advantage of the clouds ability to grow and shrink on demand
- Infrastructure as code
- Use containers

Advice:

- Workload size and complexity
  - serverless works best for simple, discrete tasks
- Execution frequency and duration
  - how many requests per second will the serverless application process
  - how long will each request take to process
- Requests and networking
  - dont have full networking configurability (usually)
- Language
  - Does the serverless platform support your language?
- Runtime limitations
  - Stuck within a specific runtime image
- Cost
  - conveniant but expensive

See if stuff works with serverless, then go to a server with containers if need be

## Optimization, Performance, and the Benchmark Wars

Make sure youre actually comparing apples to apples in assessing the differences of each system

Ya basically sales people are sales people and its easy to lie with stats

## Undercurrents and Their Impact on Choosing Technologies

### Data Management

- How are you protected against data breaches, both from outside and within?
- What is your products compliance with GDPR, CCPA, and other data privacy regulations?
Do you allow me to host my data to comply with these regulations?
- How do you ensure data quality and that im viewing the correct data in your solution?

### DataOps

Shit will go wrong, how does this tech enable you to fix it rapidly

### Data Architecture

- avoid unnecessary lock in
- ensure interoperability
- produce high roi

### Orchestration Example: Airflow

Uhh

Like its easy to rag on monoliths but a lot of real systems doing tons of work are just that. The big problem with fully distributed is like its so much shit to think about

### Software Engineering
