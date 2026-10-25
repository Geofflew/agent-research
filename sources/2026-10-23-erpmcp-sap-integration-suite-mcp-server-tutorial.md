# Create an MCP Server for Enterprise AI Agents (SAP Developers tutorial)

URL: https://developers.sap.com/tutorials/integration-suite-mcp-server/
Type: vendor
Read in session: 0006C

Summary: SAP tutorial (created 2026-09-23) shows MCP Server artifacts in SAP Integration Suite that wrap an OpenAPI spec; this is build-your-own exposure of S/4HANA or other APIs, not a prebuilt journal-entry endpoint. Default authorization is a single coarse OAuth scope or developer key (API.invoke), with no amount, period or threshold scoping; fine-grained limits live in the backend API. Nothing found for a native S/4HANA Cloud finance MCP server in fetchable SAP docs.

Quotes:
- "How to create an Integration Package and add an MCP Server backed by an OpenAPI Specification" — SAP tutorial
- "How the default policy model secures the MCP Server with authentication and authorization" — SAP tutorial
- "Access is granted if the caller presents either a valid OAuth scope" — SAP tutorial
- "Do not use Enterprise-managed authorization" — SAP tutorial
- "Re-generate a fresh token" — SAP tutorial
