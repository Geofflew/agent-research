# What does a CPA firm accountant see and do across many clients' closes once agents prepare them?

Status: live
Graduated: C45 (0008B, one account of the outsourced close; replaces C27 + C34 under thin-cap escape)
Opened: session 0007C
Yield: 0.0
Touches: C27, C29, C19; threads/covenant-addback-review
Sources: [casq-intuit-accountant-suite-uk], [casq-itwire-intuit-cross-client], [casq-puzzle-ai-close-debit-co], [casq-zeni-accounting-firms], [casq-cpacom-cas-benchmark-2024], [casq-karbon-analytics], [midmkt-jofa-cas-benchmark-2024]

What we know so far: The cross-client screens that exist show clients, jobs, and close stages, not transactions. Intuit's Accountant Suite (live October 2025, August 2026 update mostly in beta) adds cross-client portfolio insights so an accountant can spot which client needs attention without opening each file, and a Books Close template with progress tracking. Karbon's dashboards compare client portfolios on profitability and capacity. The review queue of low-confidence items (Zeni) sits inside each client's books. Puzzle reports one firm closing 15 clients by the fourth business day, saving one to one and a half hours per client, and expecting to carry three times its client load with the same team. CAS fees per professional rose 29% to $156,250 in the 2024 survey with fixed-fee recurring billing. No source gives the share of closes agent-prepared.

Tried in 0007C (iter 50, reverted): C27 consequence rewritten from one cross-client queue to triage by client then per-client queue. C27 stayed 8 (consequence already 2; mechanism 1 is the gap: fixed-fee to exception-only incentive is inferred, no passage). Retry target is mechanism: a source where a fixed-fee firm says it stopped full review.

What it would take to become a claim: a help doc or release note showing a transaction-level exception queue across clients, or a firm reporting clients per reviewer before and after agents.

Open sub-questions:
- Does the accountant's day become portfolio triage (which client is red) followed by per-client queues, and who decides which client is red: the agent or a rule?
- What does the client or lender receive at month end from these firms: a package, a covenant report, a review report?
- If the firm carries three times the clients per person, what does the reviewer still read?

0007C iter 64 (C27 sharpen reverted 8->7, +62 words): put the fixed-fee -> exception-only step on firm sources (Zeni low-confidence review queue, 250 accountants / 1,000+ customers; Puzzle 15 clients by BD4, 3x load). Judge still m=1: vendor pages do not establish the incentive step. Also: C27 body still cites retired C8/C9/C18 and says "one exception queue across dozens of clients" (contradicted here) - pruner/cut candidate. What it would take: a CAS survey or firm filing (not vendor) on review staffing per client under fixed fees.

From retired scenario 2031-firms-fire-the-messy-clients (0001F, lowest net 7.30 under the review 0004 cap): on fixed fees, once agents clear clean feeds, a firm's cost per client is almost entirely its exceptions plus the add-back review, so firms price by exception rate at the annual renewal and drop clients with spreadsheet job costs or hand-exported inventory, creating a segment defined by data quality. What would settle it: a firm's exceptions per client-month, or engagement letters priced by feed quality.

0008C iter 68 (builder C27 sharpen reverted 8->8, +42 words): carried C34 qualification (firm buys/runs agents; reviewer of record = owner or second firm), dropped dead C8/C9/C18 sentence and one-queue line, portfolio-view-then-per-client-queue consequence, signpost on CAS survey cycle (2022, 2024 -> 2026/2028). Judge unchanged: m1 (fixed-fee -> exception-only inferred), e1 (secondary/vendor), and title still names retired C8 ("reliance condition C8 places after 2028"). Next: the title fix is a wholesale rewrite -> B add from this thread or A merge C27 into C34 (C34 now 9-10, the stronger claim).
New 0008C evidence: [expq-meridian-one-accountant-1m-book] (vendor) "A bookkeeper running manual closes typically carries 15 to 25 monthly clients before the close starts slipping"; "Review time scales with exceptions, not with transaction volume". [expq-mom-project-fractional-controller-posting] fractional controller 20 hrs/week, one client. [expq-creative-planning-outsourced-controller-posting] "Ability to work with multiple clients", no count. Still no non-vendor clients-per-reviewer figure.

0008B synthesizer: C45 added (net 10; g2 n1 m2 s2 c2 t2 e2 r2). Carries C27 market premises, fixed-fee incentive, C34 AICPA chain, owner monthly sitting, Puzzle 15 clients BD4, JofA "bookkeeping or audit, not both". Lender reads tax filings (C41) added as counter. A to retire C27/C34.

0007A pruner: C27 retired (r0005 thin), replaced by C45. Not carried into C45: AI-native vendors such as Basis sell agents that run in the background and return completed deliverables for human review [midmkt-pulse2-basis-series-b]; median advisory revenue +61% in two years [midmkt-jofa-cas-benchmark-2024].
