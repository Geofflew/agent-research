# What does the AP and AR team do with invoice statuses that an accredited platform reports to the French tax authority?

Status: live
Opened: session 0008C
Yield: 1.77 (0009C C50 +1.77)
Touches: C7, C40; scenarios/2031-tax-authority-accredits-the-invoice-agent; threads/ap-clerk-with-structured-invoices; threads/tax-authority-record-as-evidence
Sources: [expq4-legifiscal-plateformes-agreees], [expq4-tiime-facture-electronique-statuts]

What we know so far: In France, accepting or refusing an invoice becomes a reported act with a legal status. Each entity "devra choisir une pa unique pour la réception des factures", and final registration of a platform comes only after real-condition interoperability tests [expq4-legifiscal-plateformes-agreees] (secondary). Four statuses are mandatory and sent to the administration: "déposée, rejetée, refusée et encaissée"; "rejetée" is a platform technical problem while "refusée" is the buyer's commercial disagreement for a reason the norm frames, and "encaissée" feeds VAT pre-filling [expq4-tiime-facture-electronique-statuts] (secondary). So the AP clerk's refusal and the AR clerk's "paid" status become tax-relevant data from September 2026, which is the act the 2031 scenario's agent performs and the reason the authority would want to accredit who sets it.

What it would take to become a claim: the DGFiP specification or decree text on statuses and platform accreditation conditions (impots.gouv.fr), or a platform's documentation of an automated refusal.

Open sub-questions:
- If an agent sets "refusée" automatically on a PO mismatch, who answers the tax inspector's question about it?
- Does "encaissée" become the AR clerk's daily task, since VAT on services is due on receipt?
0008C iter 100 (designer experience C50 kept 8->9, +21 words): clerk works buyer refusals the platform reports as one of four mandatory statuses [expq4-tiime-facture-electronique-statuts].

0003F: scenario 2031-tax-authority-accredits-the-invoice-agent retired at the 2031 cap (fresh 13 gross, 10.50 net, lowest unprotected) when the orchestration scenario was restored at 11.04. Its file stays in scenarios/ as the draft. Core: at the 2028 and 2029 accreditation renewals the French authority adds agent conditions (reading agent separate from payment-detail agent; each status change carries agent and setter identity; issuing gated because an issued invoice cannot be edited, C50). Restore when a 2031 slot opens; it was the only scenario anchoring C50.
0009C iter 103 (designer experience C7 kept 10->10, +45 words): French payables clerk refuses citing a norm reason, platform sends refusal to administration as one of four mandatory statuses [expq4-tiime-facture-electronique-statuts]. Review 0006 item 5 (C7) done.

0008A iter130 challenger (C50 reverted 8->8, +124w): Italy as the 7-year precedent for C50's hold-before-platform. SdI: invoice "si ha per emessa quando la stessa risulta trasmessa al sistema di interscambio" [itsdi-ade-faq-emessa-when-transmitted]; accepted invoice "non si cancella", storno by credit note TD04 [itsdi-gtech-annullare-fattura-inviata]; rejected file "si considera non emessa", resend within 5 days [itsdi-ade-circolare-13e-2018-scarto]. But pre-send review is "scelte operative suggerite ... non requisiti di legge" [itsdi-nebulas-ruoli-verifica-prima-invio]; ERP preview before transmission to agree changes [itsdi-1c-anteprima-prima-invio]; penalty 70% of VAT, min EUR 300 from Sept 2024 [itsdi-informazionefiscale-sanzioni-fattura-errata]. Reading: irreversibility since 2019 produced an optional review, not a mandatory gate -> C50's hold likely a controller-marked class setting, not default. Judge: 'release routine classes directly' inferred. What it would take: Italian data on credit-note (TD04) volumes or an Italian vendor shipping auto-send agents with class holds.
0009C iter 117: C7 refusal sentence removed (review 0008: same fact as C50; one fact, one claim). Status step now lives in C50 only.

0003F iter219 draft (review 0008 item 5, 2031 regulator restore): 13 gross, 614w, 10.95 net on fresh judgement; anchors C55, C10, C23; Contradicts crime-insurer. Same-turn fresh incumbents: critical-path 13@578 = 11.07 (lowest unprotected), lender-reads 14 = 11.54, crime-insurer 14 = 11.8; sponsor, model-provider, close-vendor, erp, accounting-firm protected. Misses the 0.5 displacement margin by 0.62, so not added; the 2031 regulator floor stays unmet (decisions D8). Text:

> # By 2031 tax authorities in invoice-clearance countries, not auditors or AI regulators, write the first binding rules on what a company's agent may sign, because an agent's acceptance, rejection, or cancellation of an invoice is already a legal act in their systems, and they require every automated response to carry the identity of the agent and of the person who set its authority
> 
> Year: 2031
> Status: live
> Contradicts: 2031-crime-insurer-licenses-the-payables-agent. There the first outside rule on agent authority is an insurer's policy endorsement on payee changes; here it is a tax authority's technical rule on invoice responses, which binds every company that invoices, insured or not, two years earlier.
> Depends on:
> - C55 (in Mexico a buyer must answer a supplier's cancellation request within three business days with a response signed by its own digital seal, and silence counts as acceptance): an agent that waits for a reviewer accepts by default, so the authority sees agents' defaults in its own data first; if silence did not bind, agents' waiting would cost nothing and no rule would be needed.
> - C10 (hard limits belong where a party outside the company records the agent's act, which in clearance countries includes invoice issuance): the authority is that outside party, so it is the one placed to set the limit; if issued invoices could be edited before lock, the authority would have no stake in who issues them.
> - C23 (the agent that reads outside documents is kept from payee details and payment release): the authority's rule requires the agent that answers invoices to be separate from any agent that changes payment details; if injection were not the binding risk, the rule would cover only message format.
> Clocks: Mexico's three-business-day cancellation response with tacit acceptance has applied since 2022; France requires large and mid-sized companies to issue through approved platforms from 1 September 2026 and small companies from 1 September 2027, with platform accreditation renewed every three years, so 2028 and 2029 renewals are the first chance to add agent conditions; EU cross-border digital reporting starts on 1 July 2030.
> Yield: 0.0
> 
> In 2031 a Mexican subsidiary's controller learns what the payables agent may sign from the tax authority's technical annex, not from the auditor. Each cancellation acceptance or rejection the agent sends must carry the agent's registered identity and the name of the employee who set its rules, and an agent that lets the deadline lapse on a cancellation above a set amount (illustrative) triggers a review notice. In France, the platform's renewed accreditation allows agents to issue and reject invoices only under the same identity condition.
> 
> Mechanism: Once agents answer invoices, the authorities' own data shows their defaults: cancellations accepted by silence, rejections sent without cause (C55). Because these acts are recorded by the authority at once and cannot be undone inside the company (C10), the authority is the party that bears them and already licenses the software that sends them. It writes the condition it can check automatically, an agent identity and a responsible person on every response, and the separation of reading agents from paying agents (C23), into the next technical annex or accreditation renewal.
> 
> The controller stops designing agent permissions for invoices and configures what the authority allows. The tax inspector asks which agent sent a response and who set its authority. The auditor reads the authority's identity log as evidence of who acted.
> 
> What would settle it: a tax authority's technical specification addressing automated or agent responses on invoice status; review notices on tacitly accepted cancellations.
> 
> Signposts: by the 2028 French renewals or a Mexican annex update, a rule naming automated responses; failing signpost, by 2030 authorities still regulate only message format.

0003F iter221 sharpen of the draft (orchestrator: one turn toward 11.57): added the annual tax miscellany resolution clock and the inspector, crime insurer, and lender as roles that read the identity log; 13 gross (reach still 1), 681w = 10.73. Still short; draft unchanged above, regulator floor for 2031 waits on review 0009.
0009C iter 121 (builder C50 kept 8->10, t1->2 m1->2, +46 words; r0008 item 3): signpost checked at go-live. Pennylane (approved platform) auto-transmits eligible invoices, no correction window before transmission, fix = credit note + new invoice visible to client [frhold-pennylane-einvoicing-experience]; recurring invoices draft / finalised / finalised-and-sent [frhold-pennylane-recurring-invoice-modes]; Sellsy automatic vs after-validation (11 Sept 2026) [frhold-sellsy-subscription-validation-mode]. Stale C10-ordering disagreement replaced by Pennylane's documented design. Secondary first-week figures: 2.5M flows, rejection 7%->32%, 166 provisional platforms [frhold-comparatif-fe-first-week-rejection-rates].
