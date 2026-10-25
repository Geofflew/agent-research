# Close as state

Definition: The close represented as a set of records the platform holds (accounts and transactions, tasks, task state, ownership, dependencies, procedure, policies, evidence) rather than as a checklist people work through, so that agents and people can act on the same state.

Sub-question: structure

Related concepts: [[agent-skills-over-state]], [[preparer-and-reviewer-roles]]

Evidence:
- Seed concept from an illustrative architecture sketch; no sources yet. The diagram lists the state as: accounts and transactions (trial balances by account and entity, and the transaction lines behind them, for the period); tasks (the checklist); task state (not started, in progress, waiting on input, submitted, reviewed); ownership (who holds the preparer and reviewer seat on each task, a person or an agent); dependencies (which tasks have to be reviewed before this one can start); procedure (the instructions for whoever holds the seat); policies (materiality thresholds, tolerances, and the accounting memos that apply); evidence (workbooks, linked files, one comment per step, the submission, the sign-off and timestamp). Sources are the ERP (general ledger) and source systems (banks, billing, spend, payroll).

What the thesis says: C1 — shipped agents hold exception, proposal, approval, evidence; not policy/procedure. Reviewer screen shifts to checking agent citation of versioned policy clause; holder of policy library holds ERP/close boundary.

Open questions:
- Is this state distinct from what the ERP already holds, and who should hold it?
- Which of these records do current close platforms actually hold in a form an agent can act on?

Close speed economics: median monthly close 6.4 days, top quartile 4.8 [freq-apqc-close-benchmark]; SEC semiannual option proposed 2026 [freq-sec-semiannual-proposal]; faster filing no valuation effect [freq-byu-filing-speed-null]; lenders: monthly ~30d, quarterly + compliance cert ~45d [freq-lender-reporting-covenants].
Thesis: C19 — agent speed value captured in lender package + cost per close, not public reporting; days-to-close pitch hits ceiling.
- 0006B C31: boundary set by ERP replacement clock (SAP 2027/2030/2033; 37% ECC licensed S/4 Sept 2024); AI-native ledgers (Rillet 600+, DualEntry, Campfire) hold close as ledger feature in mid-market; standalone close platform = multi-ERP layer [boundary-sap-ecc-2027-2030-2033-register], [boundary-rillet-series-c-600-customers-pulse2].
