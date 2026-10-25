# Preparer and reviewer roles

Definition: The two seats on every close task, each of which can be held by a person or an agent, and what the person in each seat does once agents hold the other seat or do the routine work.

Sub-question: roles-and-economics

Related concepts: [[close-as-state]], [[validation-harness]], [[adoption-ladder]]

Evidence:
- Seed concept from an illustrative architecture sketch; no sources yet. Preparer: owns the procedures and policies the agent works from; checks the agent's inputs and steps, not just the prepared output and conclusion; answers the agent when it stops and asks; runs continuously through the month, not in the close window. Reviewer: checks the preparer's work (inputs, steps, and exceptions, not just the result); captures judgment calls and changes so they go back into the procedure and policies; reviews the rework taken when a task was rejected or an exception was resolved; approves, or rejects with a reason that points at the procedure; samples agent-prepared and agent-reviewed tasks each period; sets the threshold below which an agent can hold the reviewer seat.

C9 (0005C): reviewer queue = unlike-last-period items + random sample; show time per item; unreviewed commentary labelled.
- Shipped D365 reconciliation agent recommends action per exception, stops at configured exception limit, asks no one; residual items wait on receipts/explanations outside finance [ask-ms-acct-rec-agent], [ask-ms-recon-agent-release-plan], [query-procuredesk-accrual-email-chasing]. Thesis C9: preparer's day = chasing what agent cannot request.
- CPA 120-hour pathway: 2 yrs supervised experience (UAA 2025 [cpaexp-nasba-new-pathways-blog]); Texas non-routine work directly supervised by CPA, effective 1 Aug 2026 [cpaexp-tsbpa-pathway-b-faq]; California new route 1 Jan 2027 [cpaexp-cba-ab1175-licensure-requirements]. Thesis C17: junior queue = blind sample, supervisor compares junior figure to agent's.

Open questions:
- Will any state board rule on whether reviewing AI output counts as qualifying experience? Watch Texas from Aug 2028.
- Will any close agent send a request to a named business owner (receipt, explanation) instead of leaving the item in the queue? Microsoft release waves through 2027.
- What do people in these seats at the most automated finance teams actually do now?
- How did other professions split preparer and reviewer work when automation arrived?

Talent pipeline: 300k+ US accountants left (-17%) [talent-wsj-accountant-exodus]; grads -6.6% to 55,152 [talent-aicpa-trends-2025]; resource MWs +14% FY25 [talent-kpmg-material-weakness-trends]; 91% CFOs flat/smaller, 13% more junior [talent-oliver-wyman-nyse-cfo-survey-2026]; routine work = informal training ground [talent-cpa-practice-advisor-junior-training].
Thesis: C17 — diamond by non-hiring juniors; 2032 constraint = mid-level exception reviewers; junior queue = blind re-performance sample.

Unaudited mid-market: ~2/3 mid-large private cos no audited GAAP [midmkt-chicagobooth-private-audits]; review = inquiry + analytics, no testing [midmkt-densmore-ssars], [midmkt-beancount-lender-tiers]; CAS hourly billing 53% -> 10% [midmkt-jofa-cas-benchmark-2024].
Thesis: C27 — first exception-only agent closes at unaudited private cos via CPA firm CAS on fixed fee; firm = buyer + reviewer across clients.
- Seeded-error study: juniors catch mechanical errors, managers conceptual; separate review beats sequential on mechanical [anchor-owhoso-seeded-errors]. Thesis C30: first-level mechanical seat goes, manager conceptual review stays (resolves C4 vs C20).
0007A: C17 junior learning rests on Westermann (on-the-job acquisition) + FAR 119-auditor experiment (reviewing automation = less effort, less effective); radiology removed from C17.
0008C: C34 experience — owner's monthly sitting (accept/send back each agent exception + add-back, sign before package) is the independence safeguard; skipped -> compilation not independent or second firm. Fractional controller today ~one client at 20 hrs/week; bookkeeper manual ceiling 15-25 clients (vendor) [expq-mom-project-fractional-controller-posting], [expq-meridian-one-accountant-1m-book]. C25 experience — fieldwork pulls preparer off next close for agent-estimate support.
0008B: C45 — outsourced close: firm runs exception-only close on fixed fee; owner monthly acceptance is the independence safeguard the lender review rests on (replaces C27 + C34).
0008B: C53 — junior seat gone at audit firms and companies at once; fieldwork between reviewers who never prepared; blind sample as the remaining training ground.

- C33 (0009C): COSO 2026 GenAI guidance: named owner per GenAI tool with authority and accountability; the agent's owner is the sub-certifier.
