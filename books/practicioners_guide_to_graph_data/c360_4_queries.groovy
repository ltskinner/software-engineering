// What are the most recent 20 transactions involving michaels account

dev.V().has("Customer", "customer_id", "customer_0"). // the customer
    out("owns").  // walk to his account
        in("withdraw_from", "deposit_to").  // edges coming in - walk to all transactions
        order().  // sort the vertices
            by("timestamp", desc).  // by their timestamp, descending
        limit(20).  // take the first 20
        values("transaction_id")  // return the transaction ids


// In December 2020, at which vendors did michael shop, and with what frequency?

dev.V().has("Customer", "customer_id", "customer_0"). // the customer
    out('uses').  // walk to his credit card
    in('charge').  // walk to all transactions
        has('timestamp').between("2020-12", "2021-01").  // filter to transactions in dec 2020
        out("pay").  // walk to vendors for those transactions
    groupCount().by("vendor_name")  // group and count them by name


// Find and update the transactions that Jamie and Aaliyah most value: their payments from their account to their mortgage loan

dev.V().has("Customer", "customer_id", "customer_4").  // Start at Aaliyas customer vertex
    out("owns").  // Walk to her account
    in("withdraw_from"). // Walk to transactions that are withdrawals from the account
    out("pay").  // Go to the loan vertices
        has("Loan", "loan_id", "loan_18").  // Filter to aalyiahs loan id
        property("transaction_type", "mortgage payment").  // only get payments of type mortgage payment
            values("transaction_id", "transaction_type") // Group and count the loan vertices

// Check that we didnt update every transaction
dev.V().has("Customer", "customer_id", "customer_4").  // Start at Aaliyas customer vertex
    out("owns").  // Walk to her account
    in("withdraw_from"). // Walk to transactions that are withdrawals from the account
    groupCount().
    by("transaction_type")


// Shaping results
dev.V().has("Customer", "customer_id", "customer_0").
    project("CreditCardUsers", "AccountOwners", "LoanOwners").
        by(constant("name or no owner for credit card")).  // create a value for the CreditCardUsers key
        by(constant("name or no owner for accounts")).  // create a value ofr the AccountOwners key
        by(constant("name or no owner for loans"))  // create a value for the LoanOwnersKey

// Uhh populating: finding people who share a credit card with Michael

dev.V().has("Customer", "customer_id", "customer_0").
    project("CreditCardUsers", "AccountOwners", "LoanOwners").
        by(
            out("uses").  // walk to the credit card
            in("uses").  // walk to the customers who use the same credit card
                where(neq("michael")).
            values("name").  // return their names
            fold().  // return the list of names
            coalesce(
                unfold(),                   // try block
                constant("NoOtherUsers")    // catch block
            ).fold()
        ).
        by(
            out("owns").
            in("owns").
                where(neq("michael")).
            values("name").
            fold().
            coalesce(
                unfold(),                   // try block
                constant("NoOtherUsers")   // catch block
            ).fold()
        ).
        by(
            out("owns").
            in("owns").
                where(neq("michael")).
            values("name").
            fold().
            coalesce(
                unfold(),                   // try block
                constant("NoOtherUsers")   // catch block
            ).fold()
        )

// Produces:
//{
//    "CreditCardUsers": [
//        "NoOtherUsers",
//    ],
//    "AccountOwners": [
//        "Maria",
//    ],
//    "LoanOwners": [
//        "NoOtherUsers",
//    ]
//}
// note, the where(neq("michael")) will remove Michael instances
