# Agent skills over state

Definition: Agent capability delivered as a set of skills that read and write the close state through a protocol layer (MCP in the seed diagram), rather than as features built separately into each product.

Sub-question: work

Related concepts: [[close-as-state]], [[validation-harness]], [[adoption-ladder]]

Evidence:
- Seed concept from an illustrative architecture sketch; no sources yet. The diagram lists: portfolio view (the whole close at a glance, every task by state, what is blocked and by whom, the critical path, how much ran on agents); orchestrator (starts work as soon as it is unblocked, nudges whoever holds the seat, reports blockers and the critical path, does no accounting); domain skills (accruals, recs, rollforwards, flux; work the task the way the procedure says, one comment per step, then submit; can hold the reviewer seat below the threshold); dynamic task sequencing (works out which tasks have to finish before which, from the procedures, the accounts, and past sign-off order; a controller approves; feeds the orchestrator); outreach and data ingestion (asks people and vendors for what a task is waiting on, pulls source files and line detail into the task as evidence); validation harness; review packs (shows the preparer and reviewer what the agent used and did, step by step: inputs, evidence, exceptions, changes from last period).

What the thesis says: C2 — two routes (ERP features vs close-platform skills over protocol); NetSuite AI Connector scopes outside agent by role/record type, not amount/period; close platform carries limits.

Open questions:
- Which of these skills do vendors ship today, and which are the hardest?
- Does the skill-over-protocol pattern hold, or do ERP vendors keep agents inside their own products?
