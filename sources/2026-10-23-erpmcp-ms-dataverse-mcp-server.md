# Dataverse MCP server (Microsoft Learn)

URL: https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp
Type: vendor
Read in session: 0006C

Summary: Dataverse (the data platform under Dynamics 365 Finance and Supply Chain) exposes a remote MCP server whose tools include create_record, update_record and delete_record for outside clients such as Claude Code; page last updated 2026-06-05. Documented controls are environment-level enablement and an allowed-clients list, with delete gated on user approval; no amount, period or threshold scoping is described on the page. Billing for non-Copilot-Studio agents began 2025-12-15.

Quotes:
- "Microsoft Dataverse can act as an MCP server, providing intelligent access to tables and records to various MCP clients like Copilot Studio agents, Visual Studio (VS) Code GitHub Copilot, GitHub Copilot CLI, Claude desktop, Claude Code, and many others." — Microsoft Learn, Dataverse MCP page
- "To use Dataverse as an MCP server, you need to enable and configure the MCP server and allowed clients for your Power Platform environment." — Microsoft Learn, Dataverse MCP page
- "Inserts a new row into a Dataverse table and returns the GUID." — Microsoft Learn, Dataverse MCP page
- "Updates an existing row in a Dataverse table." — Microsoft Learn, Dataverse MCP page
- "Delete a row, only after explicit user approval." — Microsoft Learn, Dataverse MCP page
- "If you maintain allow or deny lists in your MCP client by tool name, review your configuration so that the new tool names reflect your intended permissions." — Microsoft Learn, Dataverse MCP page
- "Starting December 15, 2025, Dataverse MCP tools are charged when accessed by AI agents created outside of Microsoft Copilot Studio." — Microsoft Learn, Dataverse MCP page
