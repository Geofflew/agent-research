# What does the controller do each year with a close vendor's controls report if auditors rely on the vendor's attested error rate?

Status: live
Opened: session 0008C
Yield: 0.0
Touches: C38, C26, C12; scenarios/2031-close-vendor-is-the-audited-party; threads/model-retirement-control-change
Sources: [expq2-berrydunn-soc-report-review-checklist], [expq2-linford-soc-bridge-gap-letters]

What we know so far: Today the user company's SOC 1 review is an annual checklist per vendor plus a gap letter the vendor signs itself. The checklist asks whether the period ends "within last six months", whether "a bridge (gap) letter" exists, which complementary user entity controls apply and how the company tests them, and "If control objectives are qualified, how will we expand our due diligence activities" [expq2-berrydunn-soc-report-review-checklist] (secondary, audit-firm form). The bridge letter is signed "by the service organization, not the service auditor", and "The AICPA doesn't actually cover bridge letter requirements" [expq2-linford-soc-bridge-gap-letters] (secondary). So in the 2031 scenario, a vendor's attested error rate per task class would reach the controller with a period end that misses year-end, covered only by the vendor's own letter, and a model change in the gap (C38) would be disclosed, if at all, in that unaudited letter.

What it would take to become a claim: a SOC 1 description that reports a measured error rate or names a model version, or audit guidance on what a bridge letter must say about a program change in the gap.

Open sub-questions:
- Would the user-entity controls for an agent vendor be "run your own blind sample" (C12), turning the customer's sample into the complementary control?
- Who at the customer reads the error-rate section: the controller, or the SOX lead who reads the rest?

0009C iter 109 (designer experience C38 kept 11->11, +43 words): controller reads the vendor-signed bridge letter at year-end for a model change since the SOC period end [expq2-linford-soc-bridge-gap-letters] (secondary). First kept edit from this thread. Still wanted: a primary (AICPA SOC 1 guide or AT-C 320) on the gap.
