# What does the controller see before switching a class of close work to auto-post?

Status: live
Opened: session 0006B (from retired C3 and C22, merged into C26)
Yield: 2.31
Touches: C26, C12, C14; threads/what-replaces-the-checklist
Sources: [cfgchg-protiviti-sap-benchmarking], [cfgchg-governancedocs-sox-itgc], [vendor-blackline-verity-prepare-ga], [ms-d365-finance-account-reconciliation]

What we know so far: C26 now holds the switch-as-configuration-change logic. Retired C3 also argued the reviewer's queue should keep serving a few blind records per class after the switch, and that the audit committee will ask for the per-class disagreement rate rather than the trail; retired C22 argued the auditor tests the threshold change log instead of per-item reasoning.

What it would take to become a claim: a close product that shows items moved and untouched share before a class switch, or ITGC guidance stating whether a tolerance edit in a recon tool is a significant configuration change.

Open sub-questions:
- How often do close teams change matching tolerances today?
- Does the audit committee ever see per-class rates, or only the controller?

0009C iter 107 (designer experience C26 reverted 10->7, +37 words): threshold change only when a second approver signs the list of items it moves, preparers work a post-change sample before next lock, as COSO 2026 asks of a posting threshold [owner-coso-genai-internal-control-2026]. Judge m2->1 s2->1 e2->1 (untargeted; baseline 10 was a 3-sample run). Retry only as part of a cut: C26 is 700+ words.
