# Xero Accounting OpenAPI spec: Contact schema carries BankAccountDetails

URL: https://raw.githubusercontent.com/XeroAPI/Xero-OpenAPI/master/xero_accounting.yaml
Type: vendor
Read in session: 0008B

Summary: Xero's official OpenAPI spec defines BankAccountDetails as a plain string property on the Contact object, so bank details travel inside the contact payload, not a separate object. Contact create/update therefore can write it.

Quotes:
- "description: Bank account number of contact" — Xero OpenAPI spec, Contact schema, BankAccountDetails property
