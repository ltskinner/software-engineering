# Chapter 4. Exploring Neighborhoods in Development

## Graph Data Modeling 101

Primary sections:

- 1. Should this be a vertex or an edge
- 2. Lost yet? Walk me through direction
- 3. A graph has no name: common mistakes in naming

### Should this be a vertex or an edge

Rule of Thumb 1: If you want to start your traversal on some piece of data, make that data a vertex

How can we use data to represent to "find all accounts owned by michael" - two ways:

- michael owns accounts
  - starting with data about people
- accounts owned by michael
  - find all accounts then keep those only owned by michael

Rule of Thumb 2: If you need the data to connect concepts, make that data an edge

- ownership - relates Customer and Account

When working with graph data, edges are the most important piece of the graph model. Edges are why you need graph technology in the first place

Rule of Thumb 3: Vertex-Edge-Vertex should read like a sentence or phrase from your queries

Verbs to Edges, Nouns to Vertices

Rule of Thumb 4: Nouns and Concepts should be vertex labels. Verbs should be edge labels

### Lost yet? Let us walk you through direction

"What are the most recent 20 transactions involving Michaels account?"

Easy to get turned around in your data model. Direction of an edge label is a difficult thing to reason around

Rule of Thumb 5: When in development, let the direction of your edges reflect how you would think about the data in your domain

Think about Vertex-Edge-Vertex in terms of subject-verb-object

#### An evolution of modeling transactions in a graph

One way to think is transaction as an edge, looping back to an account

But better is to have transaction as a vertex, linked between some edges:

- 1. Transactions withdraw from accounts
- 2. Transactions deposit to account

#### When do we use properties

Short version of the query:

- 1. Michael owns account
- 2. Transactions withdraw from his account
- 3. Select the most recent 20 transactions

Want the ability to filter transactions by time

Rule of Thumb 6: If you need to use data to subselect a group, make it a property

### A graph has no name: common mistakes in naming

Arriving at a consensus on what something should be named and maintained with your codebase is surprisingly difficult

Pitfalls in Naming Conventions 1: Using the word `has` as an edge label

Why: word `has` does not provide meaningful context regarding the edges prupose or direction

- bad, better, reccomended
- has, has_account, deposit_to

Pitfall 2: Using the word `id` sa a property

The concept of which pieces of data uniquely identify an entity is a deep topic. Using a proprty key called id is a bad decision because it is not descriptive of what it is referring to. Additionally, id is a naming convention within Cassandra and not supported

- bad, better, recco
- id, customer_id, ssn

Pitfall 3: Inconsistent use of casing

- 1. Capital `CamelCase` for vertex labels
- 2. Lowecase `snake_case` for edge labels, property keys, and example data

### Our Full Development Graph Model

Statements about transactions:

- 1. Transactions charge credit cards
- 2. Transactions pay vendors
- 3. Transactions pay loans

Note: If you could understand one concept about graph data modeling:

- Modeling data as a graph is just as much an art as it is engineering
- The art of the data modeling process involves creating and evolving your perspective on your data
- This evolution translates your mindset into the paradigm of relationship-first data modeling

When modeling cases, ask the following questions:

- 1. What does this concept mean to the end user of the application?
- 2. How are you going to read this data in your application?

### Advice on Importance of Data, Queries, and the End User

- 1. Focus on the data you have. It is easy to boil the ocean by modeling your industries entire graph problem - acoid this rabbit hole. Your graph model will evolve if you keep centered on getting to production with the data with which your application will be working
- 2. Second, apply the practice of query-driven design. Build your data model to accomodate only a predefined set of graph queries. A common red herring we run into is apps that aim to create open traversals across any discoverable data in a graph. For deve purposes this makes sense, but for production can introduce a myriad of concerns. For security, performance, and maintenance implications, strongly advise teams not to create production platforms with unbounded and unlimited traversals. The warning sign we see is a lack of specificity for your graph application.
- 3. Consider what the data means to your end user. Everything from selecting naming conventinos to the objects in the graph will be interpreted by someone else. Choose wisely

Spend time designing your data architecture, models and queries to present information that is most meaningful to them

## Implementation Details for Exploring Neighborhoods in Development

## Basic Gremlin Navigation

Query: What are the most recent 20 transactions involving michaels account?

- Start at michaels customer vertex
- Walk to his account
- Walk to all transactions
- sort by time, descending
- return top 20

Query: In December 2020, at which vendors did Michael shop, and with what frequency?

- Start at michaels customer vertex
- Walk to his credit card
- Walk to all transactions
- Only consider transactions in december 2020
- Walk to the vendors for those transactions
- Group and count them by their name

Tip: If you ever question what object type you have in the middle of developing a gremlin traversal, add `.next().getClass()` to where you are in the traversal, this will inspect the objects

Query 3: Find and update the transactions that Jamie and Aaliyah most value: their payments from their account to their mortgage loan

Query 3a: Find Aaliyas transactions that are loan payments

- Start at Aaliyas customer vertex
- Walk to her account
- Walk to transactions that are withdrawals from the account
- Go to the loan vertices
- Group and count the loan vertices

## Advanced Gremlin: Shaping Your Query Results

Goal is to answer:

"Is there anyone else who shares accounts, loans, or credit cards with Michael?"

Shaping reqults:

- 1. Shaping query results with the `project()`, `fold()`, and `unfold()`
- 2. removing data form the results with the `where(neq())` pattern
- 3. Planning for robust result payloads with `coalesce()` step

### Shaping Query results with the `project()`, `fold()`, and `unfold()` Steps

### Planning for Robust Result Payloads with the coalesce() Step

basically, try/catch blocks

## Moving from Development into Production
