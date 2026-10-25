# Policy-engine authorization

Definition: Authorization rules kept as analyzable policy code outside the application and the model, evaluated on every request (for example Cedar, OPA).

Sub-question: structure

Related concepts: [[validation-harness]], [[scoped-revocable-write-authority]], [[adoption-ladder]]

Evidence:
- Cedar separates policies from application code so they can be independently authored, updated, analyzed and audited, and is designed for automated-reasoning analysis [cedar-policy-readme].
- No source read ties policy engines to ERP or to agents specifically; this is a candidate mechanism for per-decision-class limits (amount, account, entity) that an auditor could inspect.

Open questions:
- Can an external auditor treat a versioned, formally analyzed policy as a control (ITGC/ICFR evidence) in place of reviewing each transaction?
- Do ERP-native approval rules (workflow, delegation of authority) already serve as the policy layer?
