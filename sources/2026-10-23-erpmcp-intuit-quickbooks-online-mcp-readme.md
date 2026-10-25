# Intuit QuickBooks Online MCP Server README (GitHub)

URL: https://raw.githubusercontent.com/intuit/quickbooks-online-mcp-server/main/README.md
Type: vendor
Read in session: 0006C

Summary: Intuit-published open-source MCP server for QuickBooks Online, local stdio, with full CRUD on 29 entity types including Journal Entry. It is not a hosted endpoint. Write control is a coarse environment switch that suppresses all create_, update_ or delete_ tools; there is no amount, account or period scoping. Date of release not stated in the README.

Quotes:
- "It includes full CRUD operations for 29 entity types and 11 financial reports, giving you comprehensive access to QuickBooks Online functionality." — Intuit repo README
- "Note: this is a local MCP server. It runs as a stdio subprocess on the developer's or partner's machine and authenticates to a QuickBooks Online company." — Intuit repo README
- "# QUICKBOOKS_DISABLE_WRITE=true # suppress create_* tools" — Intuit repo README
- "# QUICKBOOKS_DISABLE_UPDATE=true # suppress update_* tools" — Intuit repo README
- "# QUICKBOOKS_DISABLE_DELETE=true # suppress delete_* tools" — Intuit repo README
- "Optional: restrict which tool categories are registered (default: all enabled)" — Intuit repo README
