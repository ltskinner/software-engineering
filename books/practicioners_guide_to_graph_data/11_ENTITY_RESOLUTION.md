# Chapter 11. Simple Entity Resolution in Graphs

The problemm of inferring who is whom and what is what from keys and values in your data source has been a challenge since we began writing down information about people. This problem is called entity resolution and has a long, storied history of technical solutions

Most if not all of the entity resolution techniques you will likely be using **do not** require graph struture to figure out who is whom

## Defining a Different Complex Problem: Entity Resolution

Historically, entity resolution (also referred to as entity matching or record linkage) relied on a set of probabilistic rules, usually defined by a domain expert, to take into account data distributions and biases of data for a perticular domain. The set of probabilistic rules combine to form a functional model to calculate whether entity a is equal to entity b

Typically, entity resolution starts with finding strong identifiers that can be linked across systems of record. After that, you begin to look for different properties about the data to determine whether or not the systems really are referring to the same logical identity

Pseudocode:

- Id your data source
- Analyze the keys and values available from each source
- Map out which keys strongly identify a single logical concept
- Map out which keys weakly identify a single logical concept
- Iterate until your matched data and merged data is "good enough"
  - Form a matching process
  - Identify incorrect matches
  - Resolve errors in the matching process
  - Repeat step 1

### Seeing the Complex Problem

## Analyzing the Two Movie Datasets

## Matching and Merging the Movie Data

### Our Matching Process

## Resolving False Positives
