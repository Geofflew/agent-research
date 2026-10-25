# RamBase help: Whitelist - bank account check (Poland)

URL: https://help.rambase.net/en/finance/region-specific-functionality/poland/whitelist-bank-account-check
Type: vendor
Read in session: 0008B

Summary: ERP vendor documentation (RamBase) for its Polish localization. The ERP downloads the Ministry of Finance white list nightly, validates supplier VAT numbers and Polish bank accounts against it, flags failures on the supplier record, and blocks remittance in the payment management step above a threshold (default PLN 15,000) unless a per-supplier override checkbox is set. Shows the check as a machine control at vendor-master and payment steps, with a log of validations.

Quotes:
- "Nightly validations of supplier, with regards to VAT number and bank accounts, are performed by RamBase." — RamBase help
- "Default value in this setting is 15 000." — RamBase help, threshold above which payables are verified in the remittance process
- "Whitelist validation failed is displayed when database is up to date and at least one of the Polish bank accounts is not on the whitelist of VAT taxpayers." — RamBase help
- "Allow to continue payment even if bank account is not validated through whitelist" — RamBase help, per-supplier override checkbox
- "Whitelist is not published is displayed when there is no data from the current day in the database." — RamBase help, on government-side publication gaps
