# Which close tasks go to agents first, and why?

Status: live
Opened: session 0006B
Yield: 0.00
Touches: C9, C21, C26, C14; threads/agent-asks-a-person
Sources: [order-cfotech-automate-first], [order-floqast-healthcare-staffing-case], [order-floqast-recon-ai-autorec-2024], [order-floqast-agent-builder-2025], [order-netsuite-2026-1-rand-group], [order-mit-sloan-choi-xie-accounting-ai]

What we know so far: Vendor ship order runs matching and reconciliation first (FloQast AI AutoRec, March 2024, with threshold-based automated sign-off), then agent builders and exception detection (FloQast, September 2025), then generated flux or variance explanations (FloQast September 2025; NetSuite 2026.1 or 2026.2, unresolved), while autonomous journal posting without review is still described as not ready. The best explanation is verifiability: a reconciliation has a ground truth because balances tie out, so a wrong match is cheap to catch. The one customer case with task numbers (a healthcare staffing company on FloQast) did not start with matching: it timed every close activity and built its first four agents for the most time-consuming rule-based preparation, accrual data prep (16 to 4 hours a month) and commission audits (32 to 16 hours a week), and its close went from 20 to 10 business days. So the order may be set by each team's own time map within the set of verifiable tasks, not by a single industry sequence. An MIT Sloan study of 79 small firms found adopters closed 7.5 days faster, with self-selected adoption, and that accountants over-follow the AI on uncertain categories.

What it would take to become a claim: an independent per-task adoption survey (Gartner and NetSuite pages return 403 to the scorer); two or more more customer cases with task-level hours; NetSuite's own release notes for the flux date.

Open sub-questions:
- Does verifiability (a tie-out exists) predict order better than time spent, materiality, or risk?
- Is flux commentary early (low reliance, C9) or late (needs judgment) in practice? Evidence conflicts.
- Do teams that pick by their own time map reach exception-only review sooner than teams that follow vendor order?


Honest stop on the time-map hypothesis: no case compares time-map selection with vendor order, so whether it reaches exception-only review sooner is untested in reachable evidence. The work sub-question stays at C21 and C32 (and C26's routes).

Candidate finding (not tested as a claim): the share of reconciliations that go unreviewed first (about 22% to 66% across cases) is set by the shape of the chart of accounts, the count of static, zero-balance, and rules-driven accounts, not by the tool or the team's choice of task. What it would take: a non-vendor source on account composition or auto-certification rates (APQC, a benchmarking study, an audit firm survey), since all five cases are vendor pages.

From retired scenarios (0001F, review 0004 cap): 2036-audit-cost-sets-the-task-order (net 6.15) held that at audited companies the order is set by what an auditor can test cheaply, because the US estimates standard and specialist amendments make an agent-prepared estimate costly to audit while frozen rules are tested once; 2031-standard-setters-drop-the-cost-objection (net 7.52) held that cheap agent classification lets standard setters add disclosure depth after the expense disaggregation standard (calendar 10-Ks from early 2028) and IFRS 18 (2027). Both are candidate inputs to the work sub-question's ordering claim.

0008B explorer (D 0012D item 3, one turn): non-vendor premise found = published reconciliation policies (Macquarie auto-certify per-account approval, $10k tolerance, bi-annual re-confirm; La Trobe static 6-monthly; Stanford risk/materiality/history; UMN preparer+approver on every rec). No APQC/Hackett/IMA benchmark on account composition. Draft C43 scored 7 net < bar 8 (g1 n1 m1 s2 c2 t2 e1 r1; judge: mechanism inferred, sources university policies + vendor cases, n1 vs C26). What it would take: a benchmark of static/zero-balance share vs auto-certified share, or a company/auditor text stating auto-certification limited to the policy tier. Direction said one turn only: stop here.

Draft claim (0008B, not kept):

> ## C43. The first close work to go unreviewed is the set of balance-sheet accounts that the company's own reconciliation policy already treats as predictable or static, approved account by account by a finance director, so the share of reconciliations an agent may certify without review is fixed by the chart of accounts and that approval list rather than by what the agent can do, and adding an agent changes how fast the list is worked, not how long it is.
> 
> Organisations write the tiers before any agent arrives. Macquarie University's procedure reconciles only subledger, large, and high-risk accounts monthly and all others at least quarterly, lets accounts whose balances can be predicted in advance auto-certify in BlackLine within a $10,000 tolerance, requires the Director of Financial Control and Treasury to approve that feature for each account, and requires a written confirmation twice a year that the preloaded balance is still right. La Trobe University's policy sets critical accounts monthly, static accounts every six months, and annual accounts yearly, with every new account treated as critical; Stanford designates frequency by risk, materiality, and history. The vendor cases land where those lists would put them: Aviva Canada had 66% of a pilot team's reconciliations system-certified, which its finance head attributed to auto-certification of low-risk, rules-driven reconciliations, and Sysco auto-certifies nearly half of more than 10,000 accounts.
> 
> This disagrees with the University of Minnesota's policy, and with the many like it, that every balance-sheet reconciliation must have both a preparer and an approver: under such a policy no agent reaches unreviewed work at all, so the policy text, not the tool, is the variable to measure. It narrows C26's routes to the accounts this list admits. Consequence: the preparer stops reconciling static accounts monthly and works the critical tier; the controller's new standing work is the approval list, signing each account onto it, re-confirming expected balances every six months, and pulling back any account whose balance moved; and each new account opened in the period comes back to a person first. Signpost: a case study reporting an auto-certified share well above its own count of static, zero-balance, and predictable accounts counts against.
> 
> Confidence: weak
> Rests on: [[reconciliation-risk-tiers]], [[confidence-routing]], [recrisk-macquarie-bs-reconciliation-procedure-autocertify], [recrisk-latrobe-balance-sheet-reconciliation-policy], [recrisk-stanford-bs-reconciliation-fingate], [recrisk-umn-reconciling-verifying-gl-policy], [case-aviva-canada-blackline], [case-sysco-trintech-video]
> Counter-evidence: [recrisk-latrobe-balance-sheet-reconciliation-policy] — static accounts are still prepared and authorised by two people, only less often, so tiering cuts frequency rather than review. [recrisk-umn-reconciling-verifying-gl-policy] — some policies leave no unreviewed tier at all.
> History: 0008B added weak, explorer: reconciliation policy tiers (Direction D 0012D item 3; thread which-close-tasks-go-first)
