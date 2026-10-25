# NetSuite AI Connector Service: required features and permissions

URL: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_0714080625.html
Type: vendor
Read in session: 0004

Summary: NetSuite help page, modified 2026-10-19, latest release (GA docs). External AI client connects via MCP under a NetSuite role; admin adds MCP Server Connection + OAuth 2.0 permission per role. Blocked for Administrator or full-access roles. Standard Tools SuiteApp can create, retrieve, update records only if role holds REST web services permission. Scope = role permissions (record types), not amount. Revocation = remove permission from role; no unwind text.

Quotes:
- "you must give the required permissions to all roles in your account that should be able to use the netsuite ai connector service" — NetSuite help, required features and permissions
- "it is not possible to run the netsuite ai connector service if you've logged in to netsuite with the administrator role or roles that have full permissions to access netsuite features" — NetSuite help, same page
- "if you want your users to also be able to use the suiteapp to create, retrieve, and update netsuite records, you must give the rest web services permission to the specific role" — NetSuite help, same page
