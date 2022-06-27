# Chapter 11: The Human Side of Machine Learning

## User Experience

How differ from traditional software:

- ML systems are probabilistic instead of deterministic
  - for ml, can get different results from same input
- ML predictions are mostly correct, but we dont know for which inputs it is correct
- they can be large and slow

### Ensuring User Experience Consistency

Imagine changing the corner that the close button is on in each window? annoying

ML stuff changes all the time, can be disconcerting and annoying if not anticipated

### Combatting "Mostly Correct" Predictions

Uhh, human in the loop?

### Smooth Failing

Have online contingencies for if the main model shits out - slow or wrong

## Team Structure

### Cross-functional Teams Collaboration

- most people only think of smes during data labeling
- but with continual learning, gonna continually need these bois
- involve smes early on and empower them to make contributions without giving undue burden to engineers that will actually facilitate

### End-to-end Data Scientists

Generally two approaches:

- have dedicated ops team
  - communication overhead
  - debugging challanges
  - finger pointing
  - narrow context
- have data scientists own the entire process

HAHA "What one programmer can do in one month, two programmers can do in two months" bro thats brutal hahaha

```txt
Things id prioritize learning if I was to study to become a ML engineer again:

1. Version control
2. SQL+NoSQL
3. Python
4. Pandas/Dask
5. Data structures
6. Prob & stats
7. ML algos
8. Parallel computing
9. REST API
10. Kubernetes + Airflow
11. Unit/integration tests
```

The success of a full-stack data scientist relies on the tools they have. They need tools that "abstract the data scientists from the complexities of containerization, distributed processing, automatic failover, and other advanced computer science concepts"

In the netflix model, specialists (who originally owned a portion of a project), create tools to automate their specialist part. The other data scientists can use their automation without needing to become experts

## Responsible AI
