# Microsoft Learn: Power Automate limits (pending approvals time out after 30 days)

URL: https://learn.microsoft.com/en-us/power-automate/limits-and-config
Type: vendor
Read in session: 0009B

Summary: Power Automate flow run duration limit is 30 days and includes flows with pending approval steps; after that pending steps time out. The default on timeout is that the run ends/fails, not approval. Builders must model any approve/reject/escalate default themselves (see also modern-approvals page advising Dataverse for long-running approvals).

Quotes:
- "After 30 days, any pending steps time out." — Microsoft Learn, Power Automate limits, flow run duration row
