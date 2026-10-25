# Business Central: Set up Sales Order Agent (agent permission sets)

URL: https://learn.microsoft.com/en-us/dynamics365/business-central/sales-order-agent-setup
Type: vendor
Read in session: 0007A

Summary: BC agent has its own user account with a default system permission set (SOA - Edit) limited to sales-quote objects; admins can add/remove sets (copy, not edit) while agent is disabled. Explicitly does not inherit the reviewing user's permissions. Purpose-built allow list, not a deny list carved from a human role.

Quotes:
- "the sales order agent has a user account in Business Central, similar to other users, which defines the permissions the agent has on objects and data" — MS Learn, Manage permission sets for the agent account
- "By default, the Sales Order Agent account has the SOA - Edit permission set. This set grants access only to the objects and data necessary for handling sales quote requests." — MS Learn, same section
- "You can't modify the SOA - Edit permission set directly, because it's a system permission set." — MS Learn, same section
- "Sales Order Agent runs under its own user account and doesn't inherit permissions from the person reviewing the task." — MS Learn, resolve "agent needs additional permissions"
- "To follow the principle of least privilege, use Agent - Admin unless the user needs broader administrative access." — MS Learn, Understand permissions and access (permission for humans who configure agents)
