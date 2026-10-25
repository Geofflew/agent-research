# Do agents meet the auditor first through the request list, and on whose side?

Status: live
Opened: session 0008B
Yield: 0.0
Touches: C32, C46, C33; threads/machine-to-machine-confirmation
Sources: [pbc-suralink-document-prescreen-agent], [pbc-suralink-cloud-testing-suite], [pbc-suralink-ai-page], [pbc-fieldguide-request-analysis-agent], [pbc-auditfile-agentic-orchestrator], [pbc-agentive-yc-launch]

What we know so far (0008B explorer, diagram half: review packs, outside parties): shipped PBC agents sit on the audit firm side. Suralink prescreen reads each upload vs request, flags Needs attention, client notified right away, nothing auto accepted/rejected; vendor: firms return 1 in 10 fulfilled requests, 8 hours saved per engagement; testing agent runs procedures as each document arrives; admission: AI cannot complete if client info missing; >95% accuracy on structured data, confidence scores, Gemini 48h retention, clients can opt out. Fieldguide agent runs on every upload, flags missing/incomplete/out-of-period, agent links count as manual. AuditFile drafts PBC list from TB, humans approve. Agentive (YC): auditors took days/weeks to review client docs. No shipped client-side agent assembling or answering PBC (Kognitos list nearest; ChatFin blog 403). DataSnipper UpLink, Fieldguide request automation, Diligent blog not entered.

Draft C48 (0008B) scored 7 < bar 8 (g1 n2 m1 s2 c2 t1 e0 r2): vendor-only evidence, "first agent" and preparer-day effect inferred. What it would take: a non-vendor source (audit firm methodology, practitioner survey, regulator) on PBC turnaround or rejection rates with agent screening, or a close vendor shipping a client-side PBC agent.

Draft claim (not kept):

> ## C48. The first agent that a company's finance staff answer to will be the auditor's rather than their own, because the shipped audit-request agents run on the audit firm's side, screening every document the client uploads against what was requested and notifying the client the moment a file falls short, while no shipped client-side agent assembles the support, so in fieldwork the preparer's day is set by the auditor's agent rejecting uploads within minutes, not by an auditor's comments weeks later.
> 
> The products describe the same loop. Suralink's prescreen agent reads the file and compares it with what was requested, marks a shortfall so that both the audit team and the client are told right away, and leaves nothing accepted or rejected on its own; the vendor says firms return one in ten fulfilled requests and that the team only opens exceptions. Its testing agent executes test procedures the moment each document arrives, and the vendor admits that if a client hasn't provided all of the right information, an AI tool will never be able to complete its work. Fieldguide's agent runs automatically on every upload, flags missing, incomplete, or out-of-period information, and links files to sample items as if a person had. AuditFile's agent drafts the request list from the trial balance for the auditor to trim and send. Auditors used to take days or weeks to review what the client provided.
> 
> This turns C32 around: the close agents that ask no one outside finance meet an outside agent that asks finance, at machine speed, and C46's auditor agent reaches the company first through the request list. Consequence: during fieldwork the preparer stops batching uploads for the week and instead clears a stream of automatic rejections the same day, re-uploading the right period or the missing page, and the controller tracks how many of the firm's requests come back rather than how many are open; because the audit side screens every file, the company gains from an agent that assembles support before upload, which is the product the close vendors have not shipped. Signpost: a close vendor shipping an agent that answers an auditor's request list from the close record, with a person approving release, by the 2027 audit season, confirms; audit firms dropping upload screening counts against.
> 
> Confidence: weak
> Rests on: [[approval-gates-for-agent-actions]], [pbc-suralink-document-prescreen-agent], [pbc-suralink-cloud-testing-suite], [pbc-fieldguide-request-analysis-agent], [pbc-auditfile-agentic-orchestrator], [pbc-agentive-yc-launch]
> Counter-evidence: [pbc-suralink-ai-page] — AI features are optional and clients can disable them, so a client can refuse the screening on its uploads. [pbc-auditfile-agentic-orchestrator] — nothing is final until a person approves, so the rejection the preparer sees may wait on the auditor.
> History: 0008B added weak, explorer: diagram half, review packs and outside parties (Direction review 0005 item 4)

0009C iter 113 (designer experience C46 kept 10->10, +43 words): auditor's agent reads each upload against its request, tells client right away when one needs attention; firms return 1 in 10 fulfilled requests [pbc-suralink-document-prescreen-agent] (vendor). First kept edit from this thread.
0009C iter 118: removal of the Suralink clause from C46 reverted (9->8 noise). Next C46 designer turn replaces it (review 0008: replace, not append).
0009C iter 120 (designer experience C46 kept 9->10, +2 words net; replace edit per r0008): Suralink vendor-figure clause replaced by preparer showing the extract's agent configuration and last change, where the auditor tests controls over the information (AS 1105 as amended [taa-pcaob-as1105-standard-text]).
