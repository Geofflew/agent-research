# MCP authorization spec (2025-06-18 revision)

URL: https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
Type: standard
Read in session: 0004

Summary: MCP server = OAuth 2.1 resource server. Client must send RFC 8707 resource param; server must check token audience = itself; token passthrough to upstream forbidden. DCR (RFC 7591) recommended. No per-action policy, spend limits or approval semantics in spec. NEWER REVISION EXISTS: modelcontextprotocol.io lists 2026-07-28 (latest) and 2025-11-25; 2026-07-28 authorization split into subpages (overview, server discovery, client registration, security considerations); resource-param and audience-validation wording unchanged there, 2025-06-18 text used for quotes.

Quotes:
- "MUST be included in both authorization requests and token requests." — MCP spec 2025-06-18, resource parameter implementation
- "MCP servers MUST validate that access tokens were issued specifically for them as the intended audience" — MCP spec, access token privilege restriction
- "The MCP server MUST NOT pass through the token it received from the MCP client." — MCP spec, upstream API calls
- "to allow MCP clients to obtain OAuth client IDs without user interaction." — MCP spec, dynamic client registration
