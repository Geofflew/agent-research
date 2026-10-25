# Configure Business Central MCP Server (Microsoft Learn)

URL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/ai/configure-mcp-server
Type: vendor
Read in session: 0006C

Summary: Business Central online ships an MCP server (page updated 2026-10-02) that lets outside clients create, modify, delete records and run actions such as posting documents. Default config is read-only; admins unblock writes and set Allow Read/Create/Modify/Delete/Actions per API object. Scope is per object and per operation, bounded by the signed-in user permissions; no amount, period or approval-threshold limit is documented.

Quotes:
- "The built-in default configuration has dynamic tool mode and read-only object discovery turned on." — Microsoft Learn, Business Central MCP configuration
- "Create records : Add new customers, items, or other entities through API pages." — Microsoft Learn, Business Central MCP configuration
- "Perform actions : Execute OData actions attached to API pages or exposed by API codeunits, like posting documents or changing statuses." — Microsoft Learn, Business Central MCP configuration
- "The specific tasks available depend on your MCP Server configuration and the permissions you define for each API object." — Microsoft Learn, Business Central MCP configuration
- "Specifies whether APIs included as tools in the configuration can perform create, update, delete, or action operations." — Microsoft Learn, Business Central MCP configuration
- "Allow Actions Specifies whether actions are" — Microsoft Learn, Business Central MCP configuration
- "Data Query Tools (Preview) Enables agents to run queries directly against your Business Central database." — Microsoft Learn, Business Central MCP configuration
