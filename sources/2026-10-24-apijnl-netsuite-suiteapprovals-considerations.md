# SuiteApprovals Considerations (NetSuite Help)

URL: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_0806110833.html
Type: vendor
Read in session: 0007A

Summary: NetSuite's SuiteApprovals (approval routing) documentation lists cases where a transaction is not routed for approval. Records created by CSV import, script deployment, web service, or RESTlet are excluded, as are records created under a role whose "set by" is System. Documented as a limitation of the routing feature, not as a setting. Docs say nothing here about how such records are later approved.

Quotes:
- "the transaction is created through CSV import, script deployment, web service, or RESTlet." — NetSuite Help, SuiteApprovals Considerations, Approval Routing
- "the transaction is created using a role that sets the Set by column (under the System Notes subtab) to System" — NetSuite Help, SuiteApprovals Considerations, Approval Routing
- "voided transactions aren't supported." — NetSuite Help, SuiteApprovals Considerations
