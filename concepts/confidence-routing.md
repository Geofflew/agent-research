# Confidence routing

Definition: Per-item routing where the agent posts items above a confidence threshold untouched and sends the rest to a human; share untouched rises by class as feeds and models improve. Autonomous medical coding is the working case.

Related concepts: [[adoption-ladder]], [[validation-harness]], [[preparer-and-reviewer-roles]]

Evidence:
- CodaMetrix: 20-40% to humans by specialty; per-chart confidence score [coding-codametrix-globe-handoff-20-40-percent].
- Mount Sinai pathology: 15-20% (2022) -> ~half, 70% target; ramp gated by lab-system feed [coding-mount-sinai-codametrix-pathology-ramp].
- CMS CERT: random stratified sample of paid claims; 6.55% improper FY2025 [coding-cms-cert-fy2025-improper-payment-rate].
- OIG: provider liable when relying on billing vendor; spot-check coders [coding-oig-1998-billing-company-guidance-liability].
- Coder shortage up to 30%; coders to audit AI [coding-uc-davis-coders-become-auditors-human-in-loop].
- Vendor: zero human intervention, audit trail per decision [coding-nym-zero-human-intervention-audit-trail].

Thesis: C21 — close headless work spreads item by item via confidence threshold per class; feed quality limits; outside check = random sample of posted results.

Open questions:
- Does confidence routing + anchored review of low-confidence items bias the sample (C12)?
- Any close vendor reporting touchless posting rate by class?

Thesis: C22 — threshold = the tested control; changes under logged change mgmt w/ before/after touchless share; blind sample drawn above threshold, stratified by class.

Thesis: C26 — routes sort by task class: frozen rule (structured, recurring), confidence route (judgment exceptions), an informal preference needs a baseline test or an outcome sample before it can serve as a control.
0007A: C26 absorbed C21 (threshold set in dollars vs materiality and in confidence; sample from above it).
