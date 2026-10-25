# Microsoft Learn: Requests limits and allocations (Power Platform / Dynamics 365)

URL: https://learn.microsoft.com/en-us/power-platform/admin/api-request-limits-allocations
Type: vendor
Read in session: 0008C

Summary: Microsoft meters Power Platform/Dynamics 365 API requests per 24 hours by license (40,000 for most paid users, 250,000 for a Power Automate per-flow plan). Admin remedies when throttled: bring usage within entitlement or add capacity; a single throttled flow needs a process license, not the add-on.

Quotes:
- "if you experience high usage enforcement, you might see throttling. to avoid it, bring usage within your entitlement or add capacity for the identity or flow that exceeds it" — source page
- "then that user has a total of 40,000 + 40,000 = 80,000 requests available per 24 hours" — source page
- "assign a process license to the flow instead" — source page
