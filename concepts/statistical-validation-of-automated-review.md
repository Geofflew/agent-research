# Statistical validation of automated review

Definition: Accepting automated review by measuring its recall and precision against a human baseline on a sample, rather than inspecting every item.

Sub-question: trust

Related concepts: [[validation-harness]], [[adoption-ladder]]

Evidence:
- TREC 2009 data showed technology-assisted teams matching or beating exhaustive manual review on recall, precision and F1; the human baseline is itself imperfect [grossman-cormack-tar-vs-manual-review].
- A court accepted computer-assisted review in 2012 on transparency, consent and proportionality [da-silva-moore-predictive-coding-ruling]; quantitative validation norms (recall estimates, elusion tests) came from later practice, not that ruling (not confirmed in sources read).

- Why sampling is the route left (C8, 0005A): test-of-one for automated controls rests on identical operation [autoctl-test-of-one-ciferi], [autoctl-benchmarking-as5-compact]; SEC rates judgment-heavy controls higher risk [autoctl-sec-2007-mgmt-guidance]; model step is judgment, so test-of-one does not transfer.

Open questions:
- What sample size and recall target would an auditor accept for agent-prepared reconciliations?
- Who owns the validation set when the agent vendor and the preparer differ?
