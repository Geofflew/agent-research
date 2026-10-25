# Xero MCP Server README (XeroAPI/xero-mcp-server)

URL: https://raw.githubusercontent.com/XeroAPI/xero-mcp-server/master/README.md
Type: vendor
Read in session: 0008B

Summary: Xero's official MCP server exposes write tools to outside agents: create manual journal, invoice, payment, bank transaction, credit note, contact, plus update tools. Controls are OAuth scopes only (read and write scopes listed separately, scopes can be narrowed with XERO_SCOPES); the README describes no approval-before-write step. Xero thus gives outside agents write access, the counter-case to Sage Intacct. Update tools are limited to drafts for invoices, quotes and credit notes.

Quotes:
- "`create-manual-journal`: Create a new manual journal" — Xero MCP README, command list
- "`create-payment`: Create a new payment" — Xero MCP README, command list
- "`update-invoice`: Update an existing draft invoice" — Xero MCP README, command list
- "`update-manual-journal`: Update an existing manual journal" — Xero MCP README, command list
- "You can override these by setting the `XERO_SCOPES` environment variable to a space-separated list of scopes." — Xero MCP README, scopes note
- "From Apr 29, 2026" — Xero MCP README, scopes table (granular permissions for newer custom connections)
