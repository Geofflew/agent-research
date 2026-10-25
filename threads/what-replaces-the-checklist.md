# What replaces the preparer's close checklist once an agent prepares?

Status: live
Opened: session 0007C
Yield: 6.03
Graduated: C33 (0006B, retry with AS 2201 Appendix B)
Touches: C9, C17, C1
Sources: [ask-ms-d365-period-close-workspace], [ask-ms-acct-rec-agent], [ask-nominal-month-end-agents], [ask-rillet-ai-flux]

What we know so far: The non-agent baseline in Dynamics 365 is a closing template whose tasks are generated each period with a named assignee and a relative due date, and users with view-only rights cannot add or remove tasks. Microsoft's agent produces an exception queue and an activity timeline rather than tasks. Nominal's agent creates a task per recommendation for a preparer and reviewer; Rillet assigns account ownership per flux row with dollar and percentage materiality filters. So two patterns are emerging: the checklist survives with the agent's output attached to each task, or the checklist is replaced by an exception queue that only shows what the agent could not finish.


Open sub-questions:
- If the checklist becomes an exception queue, what does the controller sign off at period end: the task list, or an empty queue?
- Does the auditor's walkthrough still follow the checklist when the checklist no longer lists the work the agent did?


Draft claim (0006B, scored 7 net < median 8; g2 n1 m1 s2 c2 t2 e1 r1; not kept):

> ## C33. The close checklist will survive agents as the control record, but the preparer's sign-off on routine items will be made by the agent itself, so the controller's period-end review changes from confirming that every task was ticked to checking which items an agent signed and what evidence it attached, and agent sign-offs without attached output will have to be blocked.
> 
> FloQast's agent skills can attach run output to a checklist item and sign it off [chk-floqast-agent-checklist-upload-signoff].
> 
> The control question follows from AS 2201, which tests whether the person performing a control possesses the necessary authority and competence. A checklist line signed by an agent records that a step happened but not who judged it, and FloQast states that checklist items do not need supporting documentation to be signed off. That disagrees with what an auditor walking through the checklist needs: for a line an agent signed, the evidence is the attached output, since there is no competent person behind the tick. Consequence: the preparer stops ticking routine items and works the ones the agent left open; the reviewer's period-end view separates agent-signed from person-signed lines and opens the attached output for each agent line rather than taking the tick; and the controller turns off agent sign-off for any item where no output is attached. Signpost: a close vendor making attached evidence mandatory for agent sign-offs, or an auditor requesting the list of agent-signed items, within the first year-end audit after FloQast's agent sign-off skill went live.
> 
> Confidence: weak
> Rests on: [[preparer-and-reviewer-roles]], [chk-floqast-agent-checklist-upload-signoff], [chk-floqast-agent-human-review-gate], [chk-trintech-global-insurer-cadency-case], [mrc-pcaob-as2201-test-controls]
> Counter-evidence: [chk-trintech-exception-management-agent] — the exception layer, not the checklist, may become the surface people work in. 
> History: 0006B added weak, explorer: checklist sign-off (threads what-replaces-the-checklist, agent-when-blocked)

What it would take to pass the median: novelty and mechanism scored 1. A passage stating the causal step (auditor or ITGC guidance on how a tick by an automated actor is evidenced, or an inspection finding on unsupported sign-offs), or a practitioner account of controllers treating agent ticks differently, would lift both.
