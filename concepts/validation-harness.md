# Validation harness

Definition: A second model checks the preparer agent's work before a person sees it: it flags exceptions and judgment calls, scores confidence, and sends feedback back for reprocessing. The check is done by something that did not do the work.

Sub-question: trust

Related concepts: [[agent-skills-over-state]], [[adoption-ladder]], [[preparer-and-reviewer-roles]]

Evidence:
- Seed concept from an illustrative architecture sketch; no sources yet. It is the mechanism by which level 2 (verification) is meant to work: verifying agent work without reading it, and producing a known error rate.

C3 (0005C): blind per-class re-performance sample on reviewer queue after auto-approve; disagreement rate beside the toggle.

Open questions:
- Where has independent machine verification of machine work been accepted by auditors or regulators in any domain?
- What error-rate reporting would an audit committee or auditor accept?
Thesis: C3 — class auto-approve switch = config change; re-baseline restarts evidence; controller pre-switch screen (items moved, untouched share before/after, sample restart).
0008C: C38 experience — model migration week: preparers work before/after blind sample in vendor preview window (ERP templates: Workday 5 weeks, Oracle 2 weeks mandatory [expq-workday-release-best-practices-guide], [expq-oracle-quarterly-update-testing-guide]); controller signs switch as program change, refuses year-end dates.

- C42 (0008A): the frozen-model need is limited to controls where the model judges each item; a model-drafted rule that runs deterministically is benchmarked as a rule. Version drift evidence [itemjudge-chen-zaharia-zou-2023-chatgpt-drift].
