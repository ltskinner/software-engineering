# Chapter 3. Getting Started: A Simple Customer 360

Relational tools are not well suited for delivering certain shapes of data - specifically, deeply connected data

## The Foundational Use Case for Graph Data: C360

Customer 360 is customer centric data structures

### Why Do Businesses Care About C360

## Implementing a C360 Application in a Relational System

Goal is to introduce the minimum needed to understand the complexities of using a relational system for a C360 app

### Data Models

### Relational Implementation

### Example C360 Queries

Which credit cards does this customer use?

```sql
SELECT
  Customers.customer_id,
  Customers.name,
  CreditCards.cc_num,
  CreditCards.created_date
FROM
  Customers
LEFT JOIN
  CreditCards
  ON
  (Customers.customer_id = CreditCards.customer_id)
WHERE
  Customers.customer_id = 'customer_0';
```

Which accounts does this customer own?

```sql
SELECT
  Customers.customer_id,
  Customers.name,
  Accounts.acct_id
  Accounts.created_date
FROM
  Customers
LEFT JOIN
  Owns
  ON
  (Customers.customer_id = Owns.customer_id)
  LEFT JOIN
    Accounts
    ON
    (Accounts.acct_id = Owns.acct_id)
WHERE
  Customers.customer_id = 'customer_0';
```

Which loans does this customer owe?

```sql
SELECT
  Customers.customer_id,
  Customers.name,
  Loans.loan_id,
  Loans.created_date
FROM
  Customers
  LEFT JOIN
    Owes
    ON
    (Customers.customer_id = Owes.customer_id)
    LEFT JOIN
      Loans
      ON
      (Loans.loan_id = Owes.loan_id)
WHERE
  Customers.customer_id = '4';
```

What do we know about this customer?

```sql
SELECT
  Customers.customer_id,
  Customers.name,
  Accounts.acct_id,
  Accounts.created_date,
  Loans.loan_id,
  Loans.created_date,
  CreditCards.cc_num,
  CreditCards.created_date
FROM
  Customers
LEFT JOIN
  Owns
  ON
  (Customers.customer_id = Owns.customer_id)
LEFT JOIN
  Accounts
  ON
  (Accounts.acct_id = Owns.acct_id)
LEFT JOIN
  Owes
  ON
  (Customers.customer_id = Owes.customer_id)
LEFT JOIN
  Loans
  ON
  (Loans.loan_id = Owes.loan_id)
LEFT JOIN
  CreditCards
  ON
  (Customers.customer_id = CreditCards.customer_id)
WHERE
 Customers.customer_id = 'customer_0';
```

## Implementing a C360 Application in a Graph System

### Creating your graphs schema

#### Graph Traversals

- Graph Traversal - A graph traversal is an iterative process of visiting the vertices and edges of a graph in a well defined order

When using Gremlin, you start your traversals with a traversal source

- Traversal Source - A traversal source wraps two concepts together: the graph data you are traversing, and traversal strategies, such as exploring data without indexes. The traversal source you will use for examples in this book are `dev` (for development) and `g` for production

### Example C360 Queries 2

We like to think of querying a graph database, loosely, as the reverse of a SQL query.

- The common relational querying mindset is: `SELECT`-`FROM`-`WHERE`
- In graph, we are essentially asking the traversal to follow in reverse: `WHERE`-`JOIN`-`SELECT`

#### Query: Which credit cards does this customer use

```gremlin
dev.V().has('Customer', 'customer_id', 'customer_0'). // WHERE
  out('uses').                                        // JOIN
  values('cc_num')                                    // SELECT
```

#### Query: Which accounts does this customer own

```gremlin
dev.V().has('Customer', 'customer_id', 'customer_0'). // WHERE
  out('owns').                                        // JOIN
  values('acct_id')                                   // SELECT
```

Lets do the same query again, but this time would like to display the customers name alongside their account id

```gremlin
dev.V().has('Customer', 'customer_id', 'customer_0'). // WHERE
  as('customer').                                     // LABEL
  out('owns').                                        // JOIN
  as('account').                                      // LABEL
  select('customer', 'account').                      // SELECT, grabs multiple pieces
  by(values('name')).                                 // SELECT BY (for the customer)
  by(values('acct_id'))                               // SELECT BY (for the account)
```

#### Query: Which loans does this customer owe

```gremlin

dev.V().has('Customer', 'customer_id', 'customer_4'). // WHERE
  out('owes').                                        // JOIN
  values('loan_id')                                   // SELECT
```

#### Query: What do we know about this customer

```gremlin
dev.V().has('Customer', 'customer_id', 'customer_0'). // WHERE
  out().                                              // JOIN
  elementMap()                                        // SELECT *
```

## Relational vs Graph: How to Choose

### Relational vs Graph: Data Modeling

Quantitative and subjective items to consider when comparing

Quantitative arguments around data modeling designs will point at relataional b/c higher volume of resources and production usage of relational systems

Data modeling of graphs are more intuitive

### Relational vs Graph: Representing Relationships

- Relational:
  - low upfront cost to add new entities and relationships
  - expensive on retrieval b/c joins

If there is a need to model and reason about relationships in your data, graph tech provide a more seamless transition from human to machine

### Relational vs Graph: Query languages

three sapects:

- language complexity
  - SQL is more mature, but for deeply nested or large joins, gremlin is better
- query performance
  - the more complex, the better graph performs over relational
- expressiveness

### Relational vs Graph: Main Points

| Feature | Relational | Graph |
| - | - | - |
| Data modeling | Well documented | Digital representation matches human interpretation |
| Representing relationships in data | Known limitations and complexities | More intuitive representation |
| Queries | Well documented | Steep learning curve |
| | Difficulty when querying many relationships together | More expressie query language |

## Summary

### Why not relational

Short version: relational is great for tabular data, graph is better for complex data. Otherwise, the two are remarkably similar

Long version: the key is how your business values time. Time spent on engineering custom solutions and time spent waiting on queries

The differences are quite clear when your business needs to answer deeper or unplanned queries.

- Relational systems require architectural changes, adding tables, and building your own query language.
- Graph systems require augmenting your schema and inserting more data

Essentially, graph technologies makes it easier to work with complex data, whereas relational technology is easier for simple (i.e. tabular data). The depth and complexity your project needs to expand into will help make this choice clearer for you

"Are relationships first-class citizens"
