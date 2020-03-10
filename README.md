# Cognitive-Scale
1. Django Project 
2. Has 2 endpoints
   a. account/   
      input json : {"account":{"active_card": true, "available_limit": 100}}
   b. transaction/
      input json : {"transaction": {"merchant": "Burger King", "amount": 20, "time":"2019-02-13T10:00:00.000Z"}}
3. Used Rest-API to create APIs
4. Logic in account/case/views.py
5. Models in account/case/model.py
6. Account Creation
● Input: Creates the account with `available-limit` and `active-card` set. For simplicity sake,
we will assume the application will deal with just one account at a time.
● Output: The created account's current state + any business logic violations.
● Business Rules: Once created, the account should not be updated or recreated:
`account-already-initialized`.

7. Transaction authorization
● Input: Tries to authorize a transaction for a particular merchant, amount and time given
the account's state and previous transaction(s).
● Output: The account's current state + any business logic violations.
● Business Rules: You should implement the following rules, keeping in mind new rules
will appear in the future:
○ No transaction should be accepted without a properly initialized account:
account-not-initialized
○ The transaction amount should not exceed available limit: insufficient-limit
○ There should not be more than 3 transactions on a 2 minute interval:
high-frequency-small-interval (the input order cannot be relied upon, since
transactions can eventually be out of order respectively to their time’s)
○ There should not be more than 1 similar transactions (same amount and
merchant) in a 2 minutes interval: doubled-transaction
