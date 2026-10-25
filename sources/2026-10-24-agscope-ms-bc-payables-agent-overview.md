# Business Central: Payables Agent overview (vendor blocking, no vendor approval)

URL: https://learn.microsoft.com/en-us/dynamics365/business-central/payables-agent
Type: vendor
Read in session: 0007A

Summary: Agent works within admin-assigned permissions and profile. Vendors the agent creates are auto-blocked; agent has no vendor or bank-account approval capability; it does not post invoices. Control on vendor/bank risk is a product behavior (block + human callback), not a deny list on a human role.

Quotes:
- "The agent works within the permissions and profile (role) the admin assigns." — MS Learn, Permissions and profiles
- "When the agent creates a new vendor, the Blocked field on the vendor card is set to All" — MS Learn, create vendor note
- "usually, vendors and their bank accounts are approved by having communication with the vendor and doing human callbacks to the vendor's finance department" — MS Learn, same note
- "The agent itself doesn't provide any capabilities for vendor approvals." — MS Learn, same note
- "the agent doesn't post the invoice." — MS Learn, draft review confirmation
