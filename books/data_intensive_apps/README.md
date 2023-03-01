# Designing Data-Intensive Applications

"we have to dig deeper than buzzwords"

[https://github.com/ept/ddia-references](https://github.com/ept/ddia-references)

## Part I. Foundations of Data Systems

### [Chapter 1. Reliable, Scalable, and Maintainable Applications](./1_1_RELIABLE_SCALABLE_MAINTAINABLE.md)

- Reliability
  - Tolerating hardware and software faults
  - Human error
- Scalability
  - Measuring load and performance
  - Latency percentiles throughput
  - Will likely need to rethink architecture on every order of magnitude load increase
- Maintainability
  - Operability, simplicity, and evolvability

It is impossible to reduce the probability of a fault ot zero, therefore it is usually best to design fault tolerance mechanisms that **prevent faults from causing failures**

### [Chapter 2. Data Models and Query Languages](./1_2_MODELS_LANGAUGES.md)

"Data models are perhaps the most important part of developing software, because they have such a profound effect: not only on how the software is written, but also on how we *think about the problem* that we are solving"
