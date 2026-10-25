# Does the investigation threshold per account class become the setting the controller owns once the agent prepares?

Status: dormant
Opened: session 0006B (from retired C4 and C20, merged into C30)
Yield: 1.77
Touches: C30, C12, C22; threads/what-replaces-the-checklist
Sources: [mrc-pcaob-sapa11-review-precision], [mrc-audit-analytics-restatements-lag], [talent-kpmg-material-weakness-trends], [masai-trial-ai-mammography-screening]

What we know so far: PCAOB staff say a signed-off review gives little evidence by itself and the auditor tests the reviewer's threshold for investigating differences, which they call the indication of precision. Retired C4 argued that threshold per account class becomes a versioned control setting the controller owns. Retired C20 argued that the platform able to produce a validation on demand from its own blind sample decides which seat removals hold up. C30 kept the seat logic; these two product ideas fell out.

What it would take to become a claim: the PCAOB staff text on a host the scorer can fetch (pcaobus.org returns 401/403), and one close product that stores an investigation threshold per account as a versioned record.

Open sub-questions:
- Is the investigation threshold the same object as C22's confidence threshold, or a second setting?
- Does a validation-on-demand report exist in any close product today?

0007C iter 61: C21 sharpened: the dollar gate already exists as ERP configuration (D365 journal workflow materiality limits on total debit amount [autoctl-ms-d365-journal-workflow-thresholds]; Oracle ARCS auto-reconciles within a balance threshold [autorec-oracle-methods]); agent confidence becomes a second key on an amount-governed route.

0007A pruner: C21 retired, merged into C26 (C26 now holds the dollar threshold against materiality: clearly-trivial floor, SAB 99 covenant exception, D365 workflow debit limit). Not carried, kept here: confidence routing spreads item by item as autonomous medical coding did; CodaMetrix hands 20-40% of cases to coders by specialty [coding-codametrix-globe-handoff-20-40-percent]; Mount Sinai pathology ramp 15-20% -> about half, limited by lab-system feed [coding-mount-sinai-codametrix-pathology-ramp]; liability stays with provider relying on billing vendor (OIG 1998) [coding-oig-1998-billing-company-guidance-liability]; Nym zero-human-intervention trail disagreement [coding-nym-zero-human-intervention-audit-trail]; Oracle ARCS auto-close within subledger threshold [autorec-oracle-methods]. Open: does the untouched share rise by class with feed quality in a close product (any vendor metric)?
