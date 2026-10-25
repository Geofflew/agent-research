# Will close agents cite a versioned policy clause, and who holds the clause library?

Status: live
Opened: session 0006A (from retired C1)
Yield: 0.0
Touches: C2, C26, C14, C3
Sources: [ms-d365-finance-account-reconciliation], [vendor-blackline-verity-prepare-ga], [vendor-sap-autonomous-enterprise-sapphire]

What we know so far: The shipped close agents write a suggested action and a free-text justification per exception (Dynamics 365), reasoning and a confidence score for sign-off (BlackLine Verity Prepare). These two source entries do not establish whether the products hold a versioned policy object; this remains an open research question. Without a policy record the reviewer re-derives the treatment to check a justification. If proposals cited a clause such as "accrual policy version 4: accrue unbilled services above $10,000", the reviewer would check only fit, a clause edit would re-run open proposals, the controller would approve policy versions instead of items, and the auditor would test the version history. The hypothesis is that the platform holding versioned clauses becomes the agent's policy reference, with the ERP providing the posting interface. This remains unproven.

What it would take to become a claim again: a shipped agent proposal that cites a versioned policy object, or vendor documentation of a policy or memo object agents read (Trullion, Rillet, Workiva, SAP).

Open sub-questions:
- Is the policy version history the error-rate record auditors would test, and does it conflict with the blind sample of C12?
- Does SAP's in-suite close assistant hold policy inside the ERP, which would move the boundary back?

Research status: the policy-library boundary remains a hypothesis in this thread, rather than a defended thesis claim.
