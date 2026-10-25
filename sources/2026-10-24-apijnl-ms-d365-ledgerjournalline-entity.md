# LedgerJournalLine entity (Dynamics 365 Finance and Operations)

URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/entity-general-journal-ledgerjournalline
Type: vendor
Read in session: 0007A

Summary: Data-entity reference. The entity creates and updates general journal lines over OData; the General journal entity (data management) is for high volume. Lines must attach to an existing, unposted journal header. The page documents no posting action and says nothing about workflow submission or approval: docs are silent on whether imported journals enter workflow (workflow is configured per journal name; see existing source autoctl-ms-d365-journal-workflow-thresholds).

Quotes:
- "The LedgerJournalLine entity supports creating and updating general journal lines." — Microsoft Learn
- "It must reference an existing, unposted header to be able to create or update lines." — Microsoft Learn, JournalBatchNumber field
- "The LedgerJournalLine entity should be used for synchronous scenarios with OData." — Microsoft Learn
- "The General journal entity uses Data management and is recommended for high volume scenarios." — Microsoft Learn
