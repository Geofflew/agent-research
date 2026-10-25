# What does the accountant do when a general-purpose model's agent works in the client's ledger?

Status: live
Opened: session 0008C
Yield: 0.0
Touches: C39, C10, C23; scenarios/2031-general-agent-does-the-close; threads/agent-governance-layer-contest; threads/erp-vs-close-boundary-2036
Sources: [expq3-accountingweekly-quickbooks-mcp-for-accountants], [expq3-intuit-quickbooks-claude-chatgpt-expansion]

What we know so far: Even on an open ledger, the connector a general agent uses can be narrower than the ledger's protocol server. A practitioner article says Intuit's Claude connector "by design, it cannot post a journal entry or reclassify a transaction", while the QuickBooks MCP server can "fetch bills, post transactions, run reconciliations, create journal entries"; the advice to accountants is "start with read-only access, scope your permissions carefully, and log every tool call" and test "in a sandbox environment before touching live client data" [expq3-accountingweekly-quickbooks-mcp-for-accountants] (secondary). Intuit markets the in-chat actions as "complete done-for-you experiences", listing invoices and customers, not journals [expq3-intuit-quickbooks-claude-chatgpt-expansion] (vendor). So C39's ledger-by-ledger write choice has a second layer, connector by connector, and the accountant's day under the 2031 scenario starts with choosing which connector each client's agent gets and keeping the tool-call log as the audit trail.

What it would take to become a claim: vendor documentation listing the tools each connector exposes (Claude, ChatGPT, Copilot) for the same ledger, or a firm's written policy on general-agent access to client books.

Open sub-questions:
- If the general agent cannot post journals, does the accountant post its proposals by hand, keeping C39's "preparer as poster"?
- Who keeps the tool-call log: the firm, the model provider, or the ledger?
0008C iter 92 (designer experience C39 kept 7->7, +19 words): Intuit Claude connector withholds JE posting by design -> accountant posts drafts by hand on an open ledger; connector layer under ledger layer.
