# Approval gates for agent actions

Definition: Points where an agent's proposed action pauses for a human or a second checker, graded by action risk and loosened over time.

Sub-question: trust

Related concepts: [[preparer-and-reviewer-roles]], [[adoption-ladder]], [[scoped-revocable-write-authority]]

Evidence:
- Claude Code grades approval by tool type, offers plan (read-only) mode, and in auto mode uses a classifier in place of a person for routine calls; managed settings can lock these modes [claude-code-permissions].
- AP2 pairs a pre-signed Open mandate (limits) with a Closed mandate per transaction, which is a gate that is satisfied by prior bounded consent [ap2-docs-mandates].
- Replit moved toward a no-write planning mode after an incident [replit-database-deletion-incident].

Open questions:
- When a model-based classifier replaces the human approver, who is the reviewer of record for audit purposes?
- Does approval fatigue erode the gate in practice (no source read measures this)?

Thesis: C14 — agent authors deterministic rule, controller approves as versioned object; auditor relies via AS5 benchmarking (baseline + ITGC change mgmt); only model step needs blind-sample error rate (C12).
0008C: C14 experience — controller reads rule scope/test cases once then freezes; preparer files tolerance change and waits at month end. C26 experience — rule edit reapplies matches, preparer reopens moved matches and re-signs before lock.
