# Xero MCP server client code: default OAuth scopes (XeroAPI/xero-mcp-server, xero-client.ts)

URL: https://raw.githubusercontent.com/XeroAPI/xero-mcp-server/master/src/clients/xero-client.ts
Type: vendor
Read in session: 0008B

Summary: Xero's own MCP server code lists default scopes. Granular V2 set (required for new apps) splits invoices, payments, bank transactions, manual journals, reports, but contacts stays one scope (accounting.contacts). Fetched and quoted by orchestrator (one-file check after jina 401 on the scopes doc page).

Quotes:
- "Granular scopes (required for new apps)" — xero-client.ts comment above XERO_DEFAULT_AUTH_SCOPES_V2
- "accounting.reports.trialbalance.read”, “accounting.contacts”, “accounting.settings" — xero-client.ts, V2 scope list
- "Legacy scopes (deprecated but still supported for existing apps)" — xero-client.ts comment above V1 list
