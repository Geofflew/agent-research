# Continuous auditing

Definition: Automated, ongoing testing of transactions and controls proposed since 1989 (CPAS at AT&T Bell Labs) to replace periodic sampling; in practice an internal audit and management (continuous monitoring) tool that external audit relies on but has not been replaced by.

Sub-question: trust

Related concepts: [[validation-harness]], [[statistical-validation-of-automated-review]], [[market-access-controls]]

Evidence:
- CPAS built for AT&T internal audit, paper submitted Aug 1989 [ca-vasarhelyi-halper-1991-cpas].
- 2012: 9 leading internal audit orgs, none at continuous audit maturity stage [ca-vasarhelyi-2012-internal-audit-interviews].
- CA owned by audit, CM owned by management; perceived benefit = 100% testing vs samples [ca-isaca-continuous-it-auditing-cobit].
- Barriers: improvisational auditing, rigid programs, internal auditor resistance [ca-sun-2012-routinization-resistance].
- IAASB 2020 automated tools material is non-authoritative; ISAs alone authoritative [ca-iaasb-automated-tools-2020].
- CA firms pay significantly lower external audit fees; no accruals-quality difference [ca-desai-2016-audit-fees].
- 87 external auditors: budget cut only w/ functioning CA module + no prior-year material weakness [ca2-malaescu-sutton-2015-reliance].
- 2021: 39% of internal auditors implementing/using CM/CA [ca2-metricstream-2021-internal-audit-survey] (vendor survey).
- Vendor view: audit shifts from testing transactions to testing monitoring infrastructure [ca2-fieldguide-continuous-monitoring-audit-scope].

Thesis: C11 — close agents deliver full-population testing as controller's monitoring; payoff = conditional fee cut, not replaced audit.

C11 (0005C): fee cut lands second audit cycle after agent start (needs clean prior-year control report).

Open questions:
- Any named case of external audit scope changing due to client CA/CCM? 
- Will the ISA 500/330/520 revision (final planned Dec 2027) admit full-population automated tests in place of auditor procedures?
0008B: C42 — C11 fee cut needs two audited years on one model version; hosted model life 12-16 months -> audited-company controls on self-hosted open weights.
0008B: C46 — auditor runs own agent over full population instead of relying on client agent (AUASB re-performance warning); client agent saves audit effort only for frozen rules (C14).

- C42 (0008A): the frozen-model need is limited to controls where the model judges each item; a model-drafted rule that runs deterministically is benchmarked as a rule. Version drift evidence [itemjudge-chen-zaharia-zou-2023-chatgpt-drift].
