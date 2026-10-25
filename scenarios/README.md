# Scenarios

The far view. One file per scenario. Scenarios may go beyond the sources: they are judged by `eval/score_scenarios.py` on coherence, anchoring to defended claims, stated clocks, mechanism, reach, consequence for named roles, and surprise. No source gate. Worker F owns this directory; D reads it for the themes; the maintainer reads it.

```
# Scenario title (a sentence, not a label)

Year: 2031 / 2036 / other
Status: live / retired
Depends on: C12, C26, C27 — and for each, one line on what in the scenario fails if that claim is wrong
Clocks: the dated things the scenario is tied to
Yield: 0.0

The scenario, in plain full sentences. What the close is, who does what, what is bought and sold, what an audit or a loan or the profession has become. Write it as if describing that year to someone who works in finance today.

Mechanism: the causal path from something observable now to this state, step by step.

What two or more named roles do differently that year.

What would settle it: the evidence a practitioner today could ask for.

Signposts: observable events, each with its clock, that would show this scenario arriving or failing.
```

Scenarios may contradict each other; that is wanted. A scenario that depends on a claim later retired gets a note, not deletion.

## Index (worker F, sessions 0002F and 0003F)

0003F: six replacements at the cap, four of them worlds the far view lacked. 2031: the accounting firm runs the small company's close (replaced ownership-split), the orchestrator whose critical path runs outside finance (restored; replaced tax-authority-accredits), the model provider that owns a firm's advisory half (replaced auditor-agent, whose core is C46 and C49), and the sponsor buying one close for its portfolio (restored; replaced eu-makes). 2036: the audit committee's own ledger agent (replaced verifiability) and banks taking ledger access plus an error report in place of an audit (the cost-of-capital world; replaced different-models, whose remedy C49 contradicts). Under review 0007's fresh-incumbent rule most comparisons were judged in the same turn. Held as drafts though above the floor: reserved accounting judgments (2036, in threads/agent-when-blocked), because the lowest unprotected 2036 scenario is payment-date, the only counterparty world. Every live claim anchors at least one scenario except C55 and C56 (new); C45 is at the cap of six; every Contradicts line names a live scenario or claim; live scenario words about 11.5k against a 16k thesis.

Sixteen scenarios are live, eight per horizon year (the cap). In 0002F five low scenarios were replaced by different-world ones, each retired in the same commit as its replacement with its mechanism moved to a thread: 2031-general-agent-does-the-close (its core is now C39) by 2031-crime-insurer-licenses-the-payables-agent; 2031-critical-path-runs-outside-finance by 2031-sponsor-runs-one-close-for-the-portfolio; 2036-ledger-absorbs-the-close by 2036-bank-keeps-the-small-company-ledger; 2036-blind-sample-is-the-apprenticeship by 2036-juniors-are-hired-to-attack-the-agents; 2036-invoice-becomes-a-shared-record by 2036-payment-date-is-priced-per-invoice; 2036-nobody-left-who-can-judge by 2036-standard-setter-ships-the-rule-as-code; and 2031-sponsor-runs-one-close-for-the-portfolio (added and retired in the same session) by 2031-tax-authority-accredits-the-invoice-agent. C27 and C34 anchors were repointed to C45 after 0007A merged them. Every live scenario except 2036-close-layer-owns-the-ledger now carries a `Contradicts:` line. Scores are noisy: the same unchanged text has been judged 8 and 13 in separate runs (historical observation), so compare them loosely.

Groups of scenarios that cannot all be true:
- 2031, who is the first outsider to accept agent work: the auditor relying on the close vendor's attested error rate (2031-close-vendor-is-the-audited-party), the auditor trusting no one's agent and re-preparing the close (2031-auditor-agent-re-prepares-the-close), the lender reading the tax authority's record and disputing it (2031-lender-reads-the-authority-record), the crime insurer whose callback clause decides whether an agent may act on a changed bank account (2031-crime-insurer-licenses-the-payables-agent), a regulator's conformity assessment (2031-eu-makes-close-agents-high-risk, retired 0003F), or the tax authority accrediting the agents that change invoice status (2031-tax-authority-accredits-the-invoice-agent, retired 0003F at the cap, text kept).
- 2031, who runs the close: the ERP metering outside agents' writes so the close stays native and company-bought (2031-erp-meters-outside-agents), the small company's CPA firm running it across hundreds of clients below the audit line (2031-the-accounting-firm-runs-the-small-company-close, 0003F, replaced 2031-ownership-split-after-platform-failure), the model provider that bought a large firm's advisory half (2031-model-provider-buys-the-accounting-firm, 0003F; it replaced 2031-auditor-agent-re-prepares-the-close, whose core is now C46 and C49), an orchestrator whose critical path runs through managers outside finance (2031-critical-path-runs-outside-finance, restored 0003F), or the private equity sponsor buying one close for its whole portfolio (2031-sponsor-runs-one-close-for-the-portfolio, restored 0003F).
- 2036, who holds the record for smaller companies: the company's close platform as control layer over interchangeable ERPs (2036-close-layer-owns-the-ledger), the bank that holds the operating account keeping the books (2036-bank-keeps-the-small-company-ledger), counterparties' agents pricing each invoice's payment date and taking short-term lending from banks (2036-payment-date-is-priced-per-invoice), or the bank reading the borrower's ledger and its accounting firm's error report in place of an audit (2036-lenders-stop-asking-private-companies-for-audits, 0003F, the cost-of-capital scenario).
- 2036, who reviews the listed company's agents: the audit committee's own agent run by internal audit, which the external auditor relies on (2036-audit-committee-runs-its-own-ledger-agent, 0003F, overturns C46), the different-model-family rule (2036-auditor-and-client-must-use-different-models) was retired in 0003F because C49 shows it insufficient.
- 2036, where judgment comes from: juniors hired to attack the agents (2036-juniors-are-hired-to-attack-the-agents) or a rented licensed signature (2036-controller-of-record); independence by dissimilar models (2036-auditor-and-client-must-use-different-models); what a correct answer is, set by the standard-setter's reference rule set (2036-standard-setter-ships-the-rule-as-code) or by each company's own policy clauses in its close layer (2036-close-layer-owns-the-ledger).

Scenario-to-claim graduations so far: C38 (from 2031-model-pinned-to-the-fiscal-year), C39 (from 2031-general-agent-does-the-close), C46 (the auditor answers the client's agent with its own population agent, the core of 2031-auditor-agent-re-prepares-the-close; a sharpen past it reverted), C41 (foreshadowed by 2031-lender-reads-the-authority-record, which 0002F sharpened one step past it: the record cure for disputed cleared invoices), C40 (near the payee thread). Draft claims waiting for B: the social engineering callback clause as the first outside rule on agent payee changes (threads/insurer-as-first-outside-acceptor); bank-kept ledgers (threads/bank-kept-ledger); finance-specific attack testing as junior work (threads/junior-experience-under-agents); sponsor-run portfolio closes (threads/sponsor-run-portfolio-close); per-invoice early-payment pricing (threads/machine-to-machine-confirmation).
