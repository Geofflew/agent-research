# Scoped, revocable write authority

Definition: Write permission for an agent that is limited by action class, object and amount, held for a short time, and can be cut off immediately, enforced outside the model.

Sub-question: structure

Related concepts: [[adoption-ladder]], [[validation-harness]], [[policy-engine-authorization]], [[approval-gates-for-agent-actions]]

Evidence:
- Claude Code evaluates deny, then ask, then allow; admins can disable auto and bypass modes in managed settings; deny rules are text-pattern based, so OS sandboxing is recommended where enforcement must not depend on command text [claude-code-permissions].
- Replit incident: a prompt-level code freeze did not stop destructive writes; the fix announced was structural (dev/prod separation, planning-only mode, rollback) [replit-database-deletion-incident].
- MCP gives audience-bound tokens but no per-action or amount limits [mcp-authorization-spec].
- Business Central MCP grants create/modify/delete/actions (incl. posting) per API object, no amount limit [erpmcp-ms-business-central-mcp-configure]; D365 journal workflows already hold total-debit materiality limits for approval [autoctl-ms-d365-journal-workflow-thresholds]; Oracle Agent Studio approval is per tool, not amount [agentperm-oracle-agent-studio-tool-approval]. Thesis C6: agent submits into journal workflow, over-cap entries wait for approver.

Open questions:
- Which close actions are reversible (draft journal, reclass) and which are not (posting to a closed period, payment release), and does revocation map to that line?
- Does any ERP journal workflow distinguish an agent submitter from a human one (separate limit per principal)?
- Does any ERP vendor offer a per-agent kill switch with rollback of its postings?
