# What does a close agent do when it is blocked?

Status: live
Opened: session 0007C
Graduated: C36 (0006B, rebuilt C9 under new id)
Yield: 7.72
Touches: C9, C6, C10; threads/agent-asks-a-person
Sources: [ask-ms-acct-rec-agent], [ask-ms-recon-agent-release-plan], [ms-d365-finance-account-reconciliation]

What we know so far: Only Microsoft documents this. The Dynamics 365 reconciliation agent handles a narrow scope (voucher amount mismatches and pending transfers to the general ledger), stops processing when a configured daily or monthly exception limit is reached and notifies the administrator at set percentages of that limit, and returns any undone action to an unmitigated exception in the workspace queue. It does not route a blocked item to a named owner, hold it with a reason, or create a task. Microsoft calls automatic resolution a longer-term vision. Thesis C9 now says the preparer's day becomes working this residual queue and chasing the missing receipts and explanations.

What it would take to become a claim: a second vendor's documented blocked-item behaviour (BlackLine, FloQast, NetSuite, Workday), and evidence of what the blocked items are (missing document, low confidence, out-of-scope class) and how long they sit.

Open sub-questions:
- Is the exception limit an agent volume cap that functions like the amount cap in C6, and who sets it?
- Does a blocked item carry the agent's reason, so the preparer knows whether to chase a document or make a judgment?
- What happens to blocked items at period lock?


Rebuilt C9 text (0007C iter 52, reverted on the 0.5 bar only): judge raw innovation 11 (n2 m1 s2 c2 t2 e1 r1) but reviewer 0002 thin cap holds C9 at 8, so only the -95 words counted (+0.475). This version answers reviewer 0002's objection (title now the close-native finding; translation analogy and Dratsch press release removed, translation ideas in threads/translation-review-standard). Reviewer E: if the thin verdict is lifted, this text should replace C9.

## C9. Shipped close agents recommend and queue but ask no one outside finance for anything, so once an agent prepares the reconciliations the preparer's day becomes chasing the receipts and explanations the agent cannot request, and the preparer seat turns into an exception chaser rather than disappearing.

Microsoft's Dynamics 365 reconciliation agent recommends an action for each voucher mismatch, skips processing once a configured daily or monthly exception limit is reached and notifies the administrator, and returns any undone action to an unmitigated exception in the workspace queue. Rillet's flux agent writes the variance explanation itself, and Nominal's agent assigns its recommendation to a preparer and reviewer as a task. None sends a question to the operations or budget owner who holds the missing fact, and that question is how accruals are settled today: for every purchase order with unclear receipt status the controller sends a follow-up, replies take a day or longer, and some never arrive.

This disagrees with Microsoft's release plan, which describes the agent moving toward automatic resolution of reconciliation issues as a longer-term vision. The items the agent leaves are not hard judgments a better model will learn but facts held outside finance, so resolution stalls on a request no shipped agent makes, and C32 sets out how that request must be worded when it comes.

Consequence: the preparer stops building reconciliations and spends the close chasing receipts and explanations for the residual queue, the controller sees that queue rather than a checklist, and buyers plan level 1 savings as frozen hiring rather than layoffs (C17). Signpost: a Microsoft release wave plan through 2027 adding an agent request to a named business owner would move the chase from the preparer to the agent.

Confidence: weak
Rests on: [[preparer-and-reviewer-roles]], [ask-ms-acct-rec-agent], [ask-ms-recon-agent-release-plan], [ask-rillet-ai-flux], [ask-nominal-month-end-agents], [query-procuredesk-accrual-email-chasing]
Counter-evidence: [ask-nominal-month-end-agents] — task assignment to a named preparer is a partial outbound request (vendor blog). [ask-ms-recon-agent-release-plan] — Microsoft states automatic resolution as the direction of travel.
History: 0004 added · 0005C designer queue · 0006C designer blind-first sample · 0007C designer: preparer works residual queue agent cannot ask about · 0007C designer: rebuilt on close-native evidence, translation analogy to threads/translation-review-standard
Update 0006B (explorer): additional public vendor examples. FloQast: a Human Review step stops the whole run until a reviewer approves, a rejection ends the run with reason, name, and timestamp, and a changed input file structure pauses the run and shows what changed [chk-floqast-agent-human-review-gate], [chk-floqast-sept-2026-release-notes]; unmatched items get owners, comments, and labels from people inside AI Matching, with context carried across periods. Trintech (vendor page only): exceptions auto-assigned to owners and reviewers with materiality, aging, and escalation rules. Pattern: vendors block the run, not the item; only Trintech claims routing a blocked item to a named owner.

0003F draft scenario (iter205, 13 gross / 631w / 10.90 net, agent-edges world D 0014D flagged): state accountancy laws reserve a short list of judgments (going concern, impairment, obsolescence reserve, variable consideration) to a licensed person the company employs, so the agent's edge is drawn by statute. Anchors C32, C30, C51. Contradicts 2036-standard-setter-ships-the-rule-as-code. Not added: it beat the 2036 floor, but the lowest unprotected incumbent was 2036-payment-date-is-priced-per-invoice (10.597, one word below lenders-stop at 10.600), the only counterparty-agents world; same trade declined at iter199. Text:

> # By 2036 state accountancy laws reserve a short list of accounting judgments, such as going concern, impairment, and the estimates behind revenue, to a licensed person employed by the company, the way attest work is reserved to CPAs, so the agent's edge in the close is drawn by statute rather than by the vendor's settings
> 
> Year: 2036
> Status: live
> Contradicts: 2036-standard-setter-ships-the-rule-as-code. There the setter turns more of each standard into executable rules and companies record departures; here the law marks the paragraphs that may not be executed by an agent at all, so the reference rule set stops where the reserved list begins.
> Depends on:
> - C32 (shipped agents stop and wait for a finance reviewer when they cannot finish an item): the reserved list turns that voluntary stop into a required one for named judgments; if agents never stopped, there would be no existing hand-off point for the law to fix in place.
> - C30 (the mechanical first-level review goes while the conceptual review the auditor tests stays with a manager): the reserved judgments are exactly that conceptual layer, now protected by statute; if conceptual review could also go, there would be nothing for the law to reserve.
> - C51 (the blind sample is drawn from the items the agent marks confident, where surviving errors sit): agents' confident errors in estimates show up in blind samples in the late 2020s, which is the evidence boards use to justify the list; if confident errors were rare, regulators would have no case.
> Clocks: attest services are already reserved to licensed CPAs by state accountancy law, and the UK already reserves six legal activities to authorised persons, so the legal form exists; state boards of accountancy and the national association revise the model accountancy act in cycles, and the experience-route amendments of 2024 and 2025 show a revision can pass most states within two to three years; a model-act revision proposed in 2032 after the first agent-caused estimate restatements reaches most states by 2035.
> Yield: 0.0
> 
> In 2036 a mid-market manufacturer's close agent stops at four lines it is not allowed to finish: the going-concern assessment, the goodwill impairment test, the inventory obsolescence reserve, and the variable-consideration estimate in revenue. For each it prepares the data and a draft, and a licensed controller employed by the company makes and signs the judgment, because the state's accountancy law now names those judgments as reserved. The vendor ships the reserved list as a locked setting that no customer configuration can remove, and the auditor's first test is whether a licensed person signed each reserved line.
> 
> Mechanism: Agents stop and wait today when they cannot finish (C32), and the conceptual review stays with a manager (C30). As agents prepare estimates, blind samples drawn from their confident items find errors in judgments rather than in transactions (C51), and the first restatements caused by agent-prepared estimates reach boards of accountancy. Boards already reserve attest work and already amended the model act quickly in 2024 and 2025, so in 2032 they propose reserving a short list of judgments to licensees employed by the company, and most states adopt it by 2035.
> 
> The controller stops supervising every agent output and owns the reserved lines personally, with their license behind each signature. Small companies that cannot employ a licensee buy their reserved judgments from an accounting firm, which then cannot audit them. The vendor's product team maintains one locked list per state.
> 
> What would settle it: a board of accountancy or the model accountancy act discussing judgments that software may not make; a vendor documenting tasks its agent is barred from completing.
> 
> Signposts: by 2031 a state board opens a rulemaking on automated accounting judgments; failing signpost, by 2034 no state reserves any judgment and vendors set agent edges alone.

0003F grounder (iter207, 5 reserved-* sources) for the reserved-judgments draft: no regulator or standard says particular accounting judgments must be made by a person. The IESBA Code's technology revisions (effective December 2024) name automation bias, require an accountant using technology output to exercise professional judgment and to consider whether they can understand, use, and explain it, and for audit clients require that client management make all judgments that are management's responsibility through a competent individual [reserved-iesba-code-technology-revisions]. IESBA's June 2026 snapshot says professional responsibility cannot be delegated to a machine, but it has chosen not to revise the Code further and plans guidance in Q4 2026 [reserved-iesba-technology-snapshot-2026]. The Uniform Accountancy Act reserves reports on financial statements and attest and compilation services to licensees and leaves preparing financial statements open to anyone [reserved-uaa-8th-edition-section-14]. The UK reserves six legal activities by statute, the model the draft borrows [reserved-legal-services-act-2007-s12].
Finding: the boundary between agent and person is left to the company and the professional's judgment; what is reserved is the signed report, not the judgment. The draft's step (a state law reserving named judgments) has the legal form as precedent but no movement toward it; IESBA's decision not to revise is counter-evidence. What would move it: a board of accountancy or IESBA proposing a judgment that technology may not make.
