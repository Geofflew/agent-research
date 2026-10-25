# Automation bias

Definition: The tendency of a human reviewer to accept an automated suggestion even when it is wrong, so that review of agent output adds less independent assurance than it appears to.

Sub-question: trust

Related concepts: [[preparer-and-reviewer-roles]], [[validation-harness]], [[ironies-of-automation]]

Evidence:
- In a 27-reader mammography study, wrong AI advice lowered correct scoring in all experience groups, most for inexperienced readers [dratsch-automation-bias-mammography].
- CAD was reimbursed and widely used yet showed no accuracy gain and lower sensitivity for a subgroup of readers [lehman-cad-mammography-jama-im].
- Billing per accepted item gives the vendor a revenue interest in anchoring; regulators already bar or warn against result-dependent fees for auditors and coding vendors [fee-sec-reg-sx-210-2-01-contingent-fees], [coding-oig-1998-billing-company-guidance-liability]. Thesis: C28 keeps the blind sample outside the billing unit.
- Suggested mitigation: reviewer accountability for own decision (same study, small sample, weak evidence).

Open questions:
- Does showing the agent's steps and inputs, rather than only its conclusion, reduce or increase anchoring for a close reviewer?
- Can seeded errors (known-bad planted items) be used each period to measure reviewer automation bias?

Thesis: C12 — edit log from anchored review measures agreement, not accuracy; error rate needs blind re-performance sample (reviewer prepares w/o agent draft), adjudicated.
Thesis: C9 — ISO 18587 full review fails since reviewer reads output first; blind-first sample on reviewer queue (own figure before agent's), disagreement rate to controller.

Finance-domain evidence (0005B): auditors anchor on unaudited values [anchor-heintz-unaudited-values]; 25%/56% revised plans on uncorroborated mgmt explanation [anchor-glover-mgmt-explanation]; PCAOB: over-reliance on mgmt explanations, MRC precision deficiencies [anchor-breger-pcaob-overreliance], [anchor-pcaob-mrc-cfgi]; BUT auditors discount AI evidence vs human specialist = algorithm aversion [anchor-commerford-ai-reliance]; mgmt explanation did not suppress hypothesis generation [anchor-ng-explanation-no-interference]; seeded-error review teams underperform [anchor-owhoso-seeded-errors].
Thesis: C25 — anchoring sits with company reviewer (agent explanation ~ mgmt explanation); auditors averse to AI -> more testing first.
- Outside finance: pre-filled estimates sent to business owners (Legal Tracker) make the reply anchored inquiry; clinical query rules (non-leading, unable-to-determine option, no repeat asking) bind AI-generated queries [query-acdis-ahima-2019-compliant-query-brief]. Thesis: C32.
0008B: C51 — anchoring for company accountants is confidence-dependent (intervene at low confidence, follow at high); blind sample drawn from confident band. Replaces C12 premise.
