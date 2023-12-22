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
