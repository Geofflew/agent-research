# When and on what evidence will external auditors rely on the judgment part of agent-prepared close work?

Status: live
Graduated: C46 (0008B)
Opened: session 0006A (from retired C8)
Touches: C14, C12, C11, C25
Sources: [audit-iaasb-isa500-exposure-draft-2026], [audit-aicpa-ai-practice-aid-2026], [audit-icaew-ey-canvas-agents-2026], [autoctl-test-of-one-ciferi], [autoctl-as2201-appendix-b-benchmarking], [autoctl-sec-2007-mgmt-guidance], [fda-idx-dr-autonomous-ai-denovo], [masai-trial-ai-mammography-screening], [taa-pcaob-as1105-standard-text]
Yield: 9.62 (0008B C46 add)

What we know so far: The two reliance routes auditors use both fail for a model that judges each record. The test-of-one route for automated controls assumes the control operates identically every time, and review of each output anchors the reviewer on the agent's answer. The IAASB's revised ISA 500 was planned for December 2027, the AICPA practice aid of October 2026 defers evidence from a company's AI, and EY makes each auditor the mandatory human in the loop for its own tools. Domains that did accept machine first-pass work measured it outside item review: IDx-DR by a prospective study, MASAI by a randomized trial against double reading. C14 now carries the frozen-rule route and C12 the blind-sample rate the judgment part needs.

What it would take to become a claim again: a Big Four firm or standard-setter publishing a reliance condition for client-agent work, or a documented audit relying on a client's measured agent error rate.

Open sub-questions:
- Will the auditor's walkthrough of an agent task test how the blind sample was drawn rather than one configuration?
- Does PCAOB AS 1105 .10 (test the information or the controls over it) already give the route, with the agent's controls tested instead of its outputs?

0008B explorer: C46 added (net 8). Auditor answers client agent with own full-population agent: AUASB (logic can change, reperformance may not be possible; do not over-rely on entity AI; parallel first year) [audagent-auasb-impact-of-ai-on-auditors]; EY 1.4tn JE lines/yr, end-to-end by 2028 [audagent-ey-global-agentic-ai-audit-release]; PwC Evidence Match [audagent-pwc-evidence-match-accountingtoday]; Ledgerline op-ed: 100% testing, incomplete population limit, more exceptions [audagent-cpapa-testing-every-transaction]; Koreff predictive models raise budgeted hours; Richardson internal-audit ADA lowers fees (counter). F scenario need 2031-auditor-agent-re-prepares-the-close.
0002F draft scenario (not added, 8.68 then 7.55): "By 2031 the large audit firms sell the agents they built to re-prepare audits as close software to companies they do not audit, so the enterprise close market splits along audit relationships and every company's close vendor is a rival of its auditor." Independence rules bar bookkeeping and system design only for audit clients. Contradicts 2031-close-vendor-is-the-audited-party. Judge: rival-reliance logic thin, clocks partly tied. What would lift it: a large firm licensing an audit-built agent to non-audit clients.

0008A iter124 verifier C46 kept (8->10, m1->2 e1->2, +~75w): AS 1105 .10 (test accuracy/completeness of company info or controls over it) + AS 2301 .49-.50 (investigate flagged items, judge untested remainder) [taa-pcaob-as1105-standard-text] [taa-pcaob-as2301-tests-of-details] put under the own-agent step: client agent logic not re-performable -> controls not testable -> test output -> full population = own agent. AUASB page retyped secondary (review 0006 item 3). Judge still: own-agent route inferred; overlap with C49.

0003F: scenario 2031-auditor-agent-re-prepares-the-close retired at the 2031 cap (fresh 12, 9.60 net) when the model-provider scenario was added at 10.92. Its core is now C46 (auditor's own population agent) and C49 (agreement is not evidence); its last kept version (iter185) had the senior triage the 312 differences and then sample agreed entries in the classes where both agents were most confident. The file stays in scenarios/ as the draft. C49 now anchors no live scenario.

0003F iter222 draft (D 0016D: audit reorganized around two agents; C46, C49, C55): 12 gross (rea 1, sur 1), 623w = 9.92 vs lowest unprotected 2036 incumbent lenders-stop fresh 12@731 = 9.56 (payment-date 13 = 10.18). Gap 0.36 < 0.5 margin: tie, incumbent stays. Text:

> # By 2036 an audit's fieldwork is a signed exchange between the auditor's agent and the client's agent, with a deadline on every request and silence counting as acceptance of the auditor's proposed treatment, so the controller's audit work becomes deciding which of the agent's answers to defend before the clock runs out
> 
> Year: 2036
> Status: live
> Contradicts: 2036-audit-committee-runs-its-own-ledger-agent. There the auditor stops running its own population agent and relies on the board's; here the auditor keeps its own agent and the audit becomes a protocol between it and the client's, in which no third agent is needed because every disagreement is settled message by message.
> Depends on:
> - C46 (the auditor answers the client's agent with its own population agent, so the two exception lists must be reconciled in fieldwork): the exchange is that reconciliation turned into messages; if auditors relied on the client's agent, there would be one list and nothing to exchange.
> - C49 (two agents agreeing is not evidence, so the auditor samples agreed entries): the auditor's agent sends requests on a sample of entries both agents treated the same way, not only on disputes; if agreement counted, the exchange would cover only differences and stay small.
> - C55 (in Mexico a buyer must answer a supplier's cancellation within three business days by a signed response, and silence counts as acceptance): the audit protocol copies the one binding machine exchange already running between two companies' systems; if no such precedent existed, firms and clients would keep fieldwork in email and meetings.
> Clocks: the PCAOB's confirmation standard, effective for fiscal years ending on or after 15 June 2025, already lets the auditor use an electronic intermediary the company cannot override; its technology-assisted analysis amendments apply to fiscal years beginning on or after 15 December 2025; EY expects its agents to support all audit activities by 2028; a request-and-response message standard for audits, agreed by the large firms and the close vendors in 2031 and 2032 (illustrative), is in use for calendar 2034 audits.
> Yield: 0.0
> 
> In February 2036 a $500 million (illustrative) retailer's controller opens the audit queue. Overnight the firm's agent sent 1,900 signed requests (illustrative): 300 entries where the two agents disagree, and 1,600 drawn from entries where they agree. The client's agent answered 1,750 with the policy clause and the document it relied on; each answer is signed with the agent's identity and its owner's name. For the remaining 150 the agent could not answer, and each carries a five-day deadline after which the auditor's treatment stands. The controller spends the week on those 150, deciding which to defend with a person's explanation and which to let lapse.
> 
> Mechanism: Auditors run their own agents over every entry (C46), and because agreement proves nothing (C49) they also question agreed entries, so the number of requests grows past what email can carry. The confirmation standard already allows electronic intermediaries, and Mexico shows a signed machine reply with a deadline and tacit acceptance can bind a company (C55). Firms and close vendors agree on a message standard so requests and answers can be logged and signed, and deadlines with tacit acceptance keep fieldwork from stalling on unanswered requests.
> 
> The audit senior stops writing request lists and reviews the agent's escalations. The controller stops gathering support and decides which unanswered requests are worth defending. The agent's named owner signs for what the agent answered.
> 
> What would settle it: an audit firm and a close vendor connecting their agents for request and response; an engagement letter setting response deadlines with default treatment.
> 
> Signposts: by 2030 a large firm's audit agent exchanges requests with a client close platform through an API; failing signpost, by 2034 fieldwork requests still travel as spreadsheets and email.

0003F grounder (iter224, 3 negconf-* sources) on the two-agent fieldwork draft's tacit-acceptance step: audit standards are moving away from silence as evidence. ISA 505 allows a negative confirmation (the party answers only if it disagrees) as the sole substantive procedure only when risk is low with control evidence, items are many small and homogeneous, exceptions are expected to be very rare, and nothing suggests recipients will ignore requests; failure to respond does not show the request was received [negconf-frc-isa-uk-505]. The UK prohibits negative confirmations outright [negconf-frc-isa-uk-505]. The PCAOB's new AS 2310 says negative requests may not be the sole substantive procedure, because recipients increasingly do not consider them, and notes that few if any global network firms used them alone and that intermediaries and email are now commonplace [negconf-fr-2023-22491-pcaob-notice]; the SEC approved it for fiscal years ending on or after 15 June 2025 [negconf-fr-2023-26773-sec-approval-as2310].
Finding: the draft's "silence counts as acceptance of the auditor's treatment" runs against the direction of the standards: Mexico's tacit acceptance (C55) binds companies under tax law, but audit evidence now needs a positive answer. The stronger version of the draft: in an exchange between agents the auditor's agent must obtain a signed positive response to every request, so a client agent that stops and waits for a reviewer (C32) becomes the audit's bottleneck, and the controller's fieldwork is clearing the client agent's unanswered requests. Draft claim for B (C46 x C32, AS 2310): the auditor's own population agent multiplies requests, and because silence no longer counts as audit evidence, the client agent's waiting rather than the auditor's testing sets fieldwork time.

0003F iter225 reframed draft (positive answers required; client agent's waiting sets fieldwork time; C46 C49 C32): 13 gross (clo 1), 609w = 10.97 vs lenders-stop fresh 13@731 = 10.56 (payment-date 13@744 = 10.52). Gap 0.41 < 0.5: held. Text:

> # By 2036 an audit's fieldwork is a signed exchange between the auditor's agent and the client's agent, and because audit standards no longer accept silence as evidence, the client agent's habit of stopping to wait for a reviewer, not the auditor's testing, sets how long the audit takes
> 
> Year: 2036
> Status: live
> Contradicts: 2036-audit-committee-runs-its-own-ledger-agent. There the auditor stops running its own population agent and relies on the board's; here it keeps its own agent, and the audit becomes a protocol between that agent and the client's, settled request by request.
> Depends on:
> - C46 (the auditor answers the client's agent with its own population agent, so the two exception lists must be reconciled in fieldwork): the exchange is that reconciliation turned into messages; if auditors relied on the client's agent, there would be one list and nothing to exchange.
> - C49 (two agents agreeing is not evidence, so the auditor samples agreed entries): the auditor's agent sends requests on agreed entries as well as disputes, so requests run to thousands; if agreement counted, the exchange would cover only differences and stay small.
> - C32 (shipped agents stop and wait for a finance reviewer when they cannot finish an item): every request the client's agent cannot answer waits for a person, and since an unanswered request proves nothing, the audit waits too; if agents answered everything, fieldwork would finish when the auditor's agent did.
> Clocks: the PCAOB's revised confirmation standard, approved by the SEC for fiscal years ending on or after 15 June 2025, bars negative requests, where silence counts as agreement, as the sole substantive procedure, and the UK prohibits them outright, so an audit protocol cannot let silence settle a request; the same standard allows electronic intermediaries the company cannot override; EY expects its agents to support all audit activities by 2028; Mexico has run a binding signed exchange between companies' systems on invoice cancellations since 2022, the template firms and vendors copy for a request-and-response format (illustrative dates: agreed 2032, in use for calendar 2034 audits).
> Yield: 0.0
> 
> In February 2036 a $500 million (illustrative) retailer's controller opens the audit queue. Overnight the firm's agent sent 1,900 signed requests (illustrative): 300 on entries where the two agents disagree and 1,600 on entries where they agree. The client's agent answered 1,750 with the policy clause and document it relied on, each answer signed with the agent's identity and its owner's name. The other 150 are waiting for a person, and the audit cannot close until each has a positive answer. The controller's week is those 150.
> 
> Mechanism: Auditors run their own agents over every entry (C46) and, because agreement proves nothing (C49), question agreed entries too, so requests outgrow email. Firms and close vendors adopt a signed message format through intermediaries the standard already allows. Because silence cannot count as evidence, every request needs an answer, and the client agent's stops (C32) become the audit's critical path. Controllers start measuring their agent's unanswered-request rate the way they once measured days to close, and close vendors compete on how few audit requests their agent leaves for a person.
> 
> The audit senior stops writing request lists and reviews the agent's escalations. The controller stops gathering support and clears the client agent's unanswered requests. The agent's named owner signs for what it answered.
> 
> What would settle it: an audit firm and a close vendor connecting their agents for request and response; a close vendor reporting its agent's unanswered audit-request rate.
> 
> Signposts: by 2030 a large firm's audit agent exchanges requests with a client close platform through an API; failing signpost, by 2034 fieldwork requests still travel as spreadsheets and email.
