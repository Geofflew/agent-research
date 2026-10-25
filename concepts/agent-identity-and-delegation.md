# Agent identity and delegation

Definition: Giving an AI agent its own verifiable, non-human identity and an explicit record of whose authority it acts under, so that each write can be attributed to an agent, an owner and a delegating user.

Sub-question: structure

Related concepts: [[adoption-ladder]], [[close-as-state]], [[scoped-revocable-write-authority]]

Evidence:
- MCP makes servers OAuth resource servers, binds tokens to one server by audience (RFC 8707 resource parameter), and forbids passing a client's token through to upstream APIs; downstream calls need their own token [mcp-authorization-spec].
- SPIFFE gives workloads a URI identity and a verifiable identity document obtained without static secrets [spiffe-standard]; its fit for agents is inference, not stated.
- Microsoft Entra Agent ID (agent identities, blueprints, conditional access, sponsors for lifecycle) was seen only in search summaries, no entry written; treat as unverified.
- An agent identity is distinct from the user identity: for a close, the ledger record needs agent, delegating human and policy version.
- Vendor bank segregation is a setting, not a role property: D365 bank account approval can be set to No [aprole-d365-vendor-bank-account-workflow]; NetSuite separates payment clerk from vendor master clerk [aprole-netsuite-payment-automation-roles]. Thesis C24 (0007C): agent role = human template minus bank fields + release; agent never the bank-change approver.

Open questions:
- How many ERP customers run vendor bank approval switched off? Any implementation survey or audit finding?
- Do ERPs (NetSuite, SAP, Oracle, Dynamics) model an agent as a user, a service account, or a new principal type, and what does the journal audit trail record?
- Is delegation (agent acts with a human) or impersonation (agent acts as the human) accepted by auditors?
Thesis: C2 — ERP MCP servers (NetSuite, Business Central, Oct 2026) scope agents by object/operation, not amount/period; close platform enforces limits. Sage Intacct MCP read-only.

Thesis: C24 — ERP agents inherit human security groups (Workday ASOR, NetSuite role); first class scope = deny list (vendor bank fields, payment release) subtracted from human template, before amount caps.
0007A: C23 now holds two shipped designs: inherited human role minus bank fields (Workday, SAP) vs purpose-built agent permission set without vendor approval or posting (Business Central Payables Agent).
