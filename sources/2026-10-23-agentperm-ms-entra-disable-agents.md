# Microsoft Entra Agent ID: disable agent identities in your tenant

URL: https://learn.microsoft.com/en-us/entra/agent-id/disable-agent-identities
Type: vendor
Read in session: 0004

Summary: Entra Agent ID = IdP-level agent identity (Copilot Studio, Foundry, Security Copilot agents). Admin can disable one agent or blueprint (object-scoped) or block token issuance tenant-wide via Conditional Access. Revocation = stop tokens, not unwind prior actions. Generic identity layer, not ERP; no finance-transaction scoping. Page last updated 2026-05-01; GA/preview status not stated in fetched text.

Quotes:
- "disabling agents in the microsoft entra admin center is object-scoped" — Microsoft Learn, approaches to disabling agent identities
- "conditional access policies can block authentication and token issuance of agent identities" — Microsoft Learn, same page
- "agents created in microsoft entra agent id or using the latest iterations of systems like microsoft copilot studio, azure ai foundry, and security copilot are created with agent identities" — Microsoft Learn, types of identities used by AI agents
- "existing agents running in your organization might begin to fail" — Microsoft Learn, disabling considerations
