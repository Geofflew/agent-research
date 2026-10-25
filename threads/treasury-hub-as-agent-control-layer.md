# Does the treasury payment hub already do for payments what the close layer would do for every agent that touches money?

Status: live
Opened: session 0008C
Yield: 0.0
Touches: C10, C23, C40; scenarios/2036-close-layer-owns-the-ledger; threads/payee-change-verification; threads/agent-governance-layer-contest
Sources: [expq3-kyriba-payments-fact-sheet], [expq3-sapinsider-bank-communication-management]

What we know so far: For payments the cross-ERP control layer exists and is configured by treasury. Kyriba's hub offers "up to 9 levels of rule-based payment approval", "synchronized account signatory management", "automatic quarantining of suspicious and non-compliant payments", and tells customers to "enforce workflow to initiate exceptional payments in kyriba instead of in different uncontrolled banking portals", while "ap users never have to leave the erp" [expq3-kyriba-payments-fact-sheet] (vendor). SAP's bank communication management adds batching, approval "before they are delivered to the bank", and status tracking [expq3-sapinsider-bank-communication-management] (secondary). So the 2036 scenario's close layer holding limits and bank identities for every agent is today's treasury hub widened to journals; the treasury analyst's day (release batches, work the quarantine, keep signatories) is the template for C10's payment-release point.

What it would take to become a claim: a treasury or payment hub product documenting agent principals (an AP agent's payments entering the hub's approval and quarantine), or a release note adding agent-specific limits.

Open sub-questions:
- If an AP agent's payments enter the hub's quarantine, does the treasury analyst become the reviewer of agent payments rather than AP?
- Does the hub's signatory list include agents as initiators?

0009C iter 111 (designer experience C10 reverted 11->10, +27 words): treasury analyst clears payments the hub quarantined before the batch goes to the bank [expq3-kyriba-payments-fact-sheet] (vendor). Judge n2->1 (untargeted). Step is real but C10 already has the payment-day re-enable; try under a payables claim with no treasury step.
