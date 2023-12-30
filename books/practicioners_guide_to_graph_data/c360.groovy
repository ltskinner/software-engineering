
// Vertexes
schema.vertexLabel("Customer").
    ifNotExists().
    partitionBy("customer_id", Text).
    property("name", Text).
    create();

schema.vertexLabel("Account").
    ifNotExists().
    partitionBy("acct_id", Text).
    create();

schema.vertexLabel("Loan").
    ifNotExists().
    partitionBy("loan_id", Text).
    create();

schema.vertexLabel("CreditCard").
    ifNotExists().
    partitionBy("cc_num", Text).
    create();

// Edges

schema.edgeLabel("owes").
    ifNotExists().
    from("Customer").
    to("Loan").
    create();

schema.edgeLabel("uses").
    ifNotExists().
    from("Customer").
    to("CreditCard").
    create();

schema.edgeLabel("owns").
    ifNotExists().
    from("Customer").
    to("Account").
    property("role", Text).
    create();

// Inserting data

michael = g.addV("Customer").
    property("customer_id", "customer_0").
    property("name", "Michael").
    next();

acct_14 = g.addV("Account").
    property("acct_id", "acct_14").
    next();

loan_32 = g.addV("Loan").
    property("loan_id", "loan_32").
    next();

cc_17 = g.addV("CreditCard").
    property("cc_num", "cc_17").
    next();



g.addE("owns").
    from(michael).
    to(acct_14).
    property("role", "primary").
    next();

g.addE("owes").
    from(michael).
    to(loan_32).
    next();

g.addE("uses").
    from(michael).
    to(cc_17).
    next();

maria = g.addV("Customer").
    property("customer_id", "customer_1").
    property("name", "Maria").
    next();

g.addE("owns").
    from(maria).
    to(acct_14).
    property("role", "limited").
    next();

// Data Insertion for Rashika
rashika = g.addV("Customer").
    property("customer_id", "customer_2").
    property("name", "Rashika").
    next();

acct_5 = g.addV("Account").
    property("acct_id", "acct_5").
    next();

cc_32 = g.addV("CreditCard").
    property("cc_num", "cc_32").
    next();


g.addE("owns").
    from(rashika).
    to(acct_5).
    property("role", "primary").
    next();

g.addE("uses").
    from(rashika).
    to(cc_32).
    next();


// Data Insertion for Jamie
jamie = g.addV("Customer").
    property("customer_id", "customer_3").
    property("name", "Jamie").
    next();

acct+0 = g.addV("Account").
    property("acct_id", "acct_0").
    next();

loan_18 = g.addV("Loan").
    property("loan_id", "loan_18").
    next();

g.addE("owns").
    from(jamie).
    to(acct_0).
    property("role", "primary").
    next();

g.addE("owes").
    from(jamie).
    to(loan_18).
    next();


// Data Insertion for Aaliyah

aaliyah = g.addV("Customer").
    property("customer_id", "customer_4").
    property("name", "Aaliyah").
    next();

loan_80 - g.addV("Loan").
    property("loan_id", "loan_80").
    next();

g.addE("owns").
    from(aaliyah).
    to(acct_0).
    property("role", "primary").
    next();

g.addE("owe").
    from(aaliyah).
    to(loan_80).
    next();

g.addE("owes").
    from(aaliyah).
    to(loan_18).
    next();


// Chapter 4

// Vertexes

schema.vertexLabel("Transaction").
    ifNotExists().
    partitionBy("transaction_id", Text).
    property("transaction_type", Text).
    property("timestamp", Text).
    create();

schema.vertexLabel("Vendor").
    ifNotExists().
    partitionBy("vendor_id", Text).
    property("vendor_name", Text).
    create();

// Edges
schema.edgeLabel("withdraw_from").
    ifNotExists().
    from("Transaction").
    to("Account").
    create();

schema.edgeLabel("deposit_to").
    ifNotExists().
    from("Transaction").
    to("Account").
    create();

schema.edgeLabel("pay").
    ifNotExists().
    from("Transaction").
    to("Loan").
    create();

schema.edgeLabel("charge").
    ifNotExists().
    from("Transaction").
    to("CreditCard").
    create();

schema.edgeLabel("pay").
    ifNotExists().
    from("Transaction").
    to("Vendor").
    create();
