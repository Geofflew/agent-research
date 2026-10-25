# What does the controller see and decide when changing an agent's threshold, tolerance, or policy setting?

Status: live
Opened: session 0007C
Yield: 0.75 (0006A C14 verifier: AS 2201 B30 parameters part of control)
Touches: C3, C14, C22, C6; threads/agent-when-blocked
Sources: [cfgchg-protiviti-sap-benchmarking], [cfgchg-oracle-arcs-profile-history], [cfgchg-oracle-fcm-audit-trail-reports], [cfgchg-microsoft-d365-database-logging], [cfgchg-onapsis-sap-table-change-logging], [cfgchg-governancedocs-sox-itgc], [ask-ms-acct-rec-agent], [autoctl-ms-d365-journal-workflow-thresholds]

What we know so far: Auditors may rely on a benchmarked automated control in later years without retesting only while IT general controls work, and Protiviti says significant configuration changes require re-baselining, so changing a setting restarts the evidence. Oracle's reconciliation profiles already log changes to workflow assignments, risk ratings, and the match balance threshold percentage, and SAP and Dynamics 365 can log configuration table changes. Dynamics 365 lets an administrator set the reconciliation agent's daily or monthly exception limit, and journal workflows set approval limits on total debit amount. Thesis C3 says a class auto-approve switch is a configuration change and proposes a pre-switch screen showing the items that would move, the untouched share before and after, and the sample restart; C22 says the confidence threshold is the tested control. The 0006C attempt to put this screen into C14 was reverted only because C14 was already at the maximum score.

What it would take to become a claim of its own: a shipped close product that shows the effect of a setting change before it is saved (items affected, before and after), or audit firm guidance treating an agent threshold change as a program change.

Open sub-questions:
- Who approves an agent threshold change: the controller alone, or the controller plus IT change management?
- Does the auditor pull the configuration change log for agent settings in the year-end walkthrough, and does a mid-year change force a second sample?
- Should the screen block the change in the last days before period lock?

0007C iter 62 (C14 sharpen reverted, 9->9, +60 words): the screen as work. Agent proposes a tolerance or threshold change; controller sees the open items it would move and that the benchmark restarts (AS 2201 B30: parameters part of the control; B33: baseline reestablished [autoctl-as2201-appendix-b-benchmarking]); no approval in the days before the period goes On hold [disanalogy-d365-close-gl-period-end]; at year end auditor pulls the threshold change history Oracle reconciliation profiles already log [cfgchg-oracle-arcs-profile-history]. C14's c already 2; the gap is novelty and reach. Better home: a claim whose consequence is still a screen (C10 per review 0003).

0008C (designer, experience, C14 kept 9->9): the day around a frozen rule. Controller reads scope + test cases once, freezes; preparer files a tolerance change at month end and waits instead of editing; auditor interim visit tests rule once, samples model exceptions. Open: who approves a tolerance change on day 3 of close when the controller is the bottleneck; does the wait push items into the exception queue, so the preparer works exceptions the old tolerance would have matched?
0008C (designer, experience, C26 kept 7->9 vs last full run, +25 words): rule edit reapplies matches [scope-floqast-matching-rules-drawer], so the preparer who signed the account opens the moved matches and re-signs before lock. Open: does a rule edit after sign-off unsign the account automatically? who is notified, preparer or reviewer? does the controller freeze rule edits from day N of close?

0008A iter131 pruner: C14 merged into C26 (C26 8->9, ~-320 words). Left out of C26, kept here: preparer who wants a wider month-end tolerance files a change and waits for approval instead of editing it; auditor's interim visit tests the rule once and samples only the model's exceptions; signpost: an auditor documenting reliance on an agent-authored automated control before end of 2029; reliance waiting on the ISA 500 revision counts against.
