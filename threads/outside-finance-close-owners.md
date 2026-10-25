# What do people outside finance do in the close today, and what deadline do they carry?

Status: live
Opened: session 0008C
Yield: 0.0
Touches: C32, C33; scenarios/2031-critical-path-runs-outside-finance; threads/agent-asks-a-person; threads/agent-when-blocked
Sources: [expq-bu-year-end-close-webinar-2023], [expq-kognitos-pbc-list], [ask2-ledge-month-end-benchmarks-2025]

What we know so far: Outside-finance owners feed the close by email against a cutoff set by finance, not through a task they own in a close tool. Boston University's year-end training asks departments to email invoices over $5,000 not posted by 30 June to a year-end mailbox by "Noon July 5th" [expq-bu-year-end-close-webinar-2023] (primary, training slides). Audit support is likewise "owned by someone in a different function" [expq-kognitos-pbc-list] (vendor). Nothing fetched shows a close product assigning a task with a deadline to a non-finance owner; FloQast, BlackLine, and Trintech pages either blocked or did not mention it. So the 2031 scenario's business owner with a response deadline in their objectives is a change in who owns the deadline, from finance's cutoff email to the owner's own queue.

What it would take to become a claim: a close vendor's help doc for request portals or task assignment to non-finance users, or a benchmark giving the share of close delay caused by other departments (the "nearly eight in ten" figure attributed to LiveFlow was not fetched).

Open sub-questions:
- When the agent asks the department directly (C32), does the cutoff email disappear or does the department now get both?
- What happens to an unanswered department request at lock: accrued by estimate, or held?

0002F (futurist): scenario 2031-critical-path-runs-outside-finance retired at the 2031 cap (8.82, lowest). Its mechanism: once agents sign the preparer lines (C33), the close's critical path to the lender's 30-day package and 45-day certificate runs through business owners answering the agent (C32), so owners carry response deadlines in annual objectives and the controller manages the company's answers. Replaced by 2031-sponsor-runs-one-close-for-the-portfolio (9.42), in which the orchestrator and portfolio view belong to the private equity sponsor. Open question: does any company already put close-response deadlines in non-finance managers' objectives?

0003F iter189 restore attempt (D 0014D item 3, orchestration): rewritten 743w, anchors C32 C33 (C36 retired, C29 dropped), clock from threads/dynamic-close-sequencing (task managers gate, not re-plan), Contradicts 2031-the-accounting-firm-runs-the-small-company-close. 12 gross (rea 1, sur 1) = 9.52 net < 2031 floor 11.29 (crime-insurer, lowest unprotected). not restored.
0008C iter 98 (designer experience C32 kept 9->10, +22 words): controller still sends the year-end cutoff request (BU: departments email unposted invoices over $5,000 by 30 June) [expq-bu-year-end-close-webinar-2023]; source re-hosted via r.jina.ai (raw PDF failed the scorer).

0009C iter 134 (designer experience replace C32 kept 7->8, +30 words; r0007 item 5): BU university cutoff step replaced by a company's own procedure: Ramp finance sends accrual requests for unbilled services (legal, audit), books from history or contract terms [cutoff-ramp-monthly-close-own-process] (primary, company describing own close; also marketing). Other 0009C sources: Stampli 5/1-day reminders, FloQast ReMind escalation (vendor).
