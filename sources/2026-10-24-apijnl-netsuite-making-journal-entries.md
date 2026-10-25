# Making Journal Entries (NetSuite Help)

URL: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1469880.html
Type: vendor
Read in session: 0007A

Summary: Basic JE page. States unapproved journals are not posted until approved, so the exclusion of API/script-created records from approval routing matters for what posts. Also gives line limits by channel (1,000 via UI/sync SOAP; 10,000 via SuiteScript, CSV, async SOAP). Docs are silent on how script-created JEs get an approved status.

Quotes:
- "Journal entry transactions aren't posted until they're approved." — NetSuite Help, Making Journal Entries
- "for transactions submitted through SuiteScript, CSV import, or through asynchronous SOAP web services, the limit is 10,000 lines per transaction." — NetSuite Help, Making Journal Entries
