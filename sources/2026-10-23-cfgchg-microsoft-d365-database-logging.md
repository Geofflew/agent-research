# Configure database logging (Dynamics 365 Finance and Operations)

URL: https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/sysadmin/configure-manage-database-log
Type: vendor
Read in session: 0006C

Summary: Microsoft docs: opt-in database log (sysdatabaselog) records table/field changes; not for batch jobs, and any user with DB access can query it by default. Logging is a selection, not automatic.

Quotes:
- "Create an auditable record of changes to specific tables that contain sensitive information." — Microsoft Learn
- "It isn't designed to track automated transactions that run in batch jobs." — Microsoft Learn
- "By default, any user who has database access can query the database log table" — Microsoft Learn
- "Limit log entries and help improve performance by selecting specific fields to log instead of whole tables." — Microsoft Learn
- "The Database Log report displays up to 10,000 records." — Microsoft Learn
