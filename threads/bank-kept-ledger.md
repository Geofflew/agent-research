# Will the bank that holds a small company's operating account end up keeping its ledger and running its close?

Status: live
Opened: session 0002F
Yield: 0.34
Touches: C7, C41, C23, C40, C34; scenarios/2036-bank-keeps-the-small-company-ledger, scenarios/2036-close-layer-owns-the-ledger
Sources: [bankledger-freeagent-natwest-free], [bankledger-freeagent-natwest-tax-pr], [bankledger-ramp-accounting-agent], [bankledger-brex-accounting-api], [bankledger-psr-app-protections-start]

What we know so far: NatWest Group gives FreeAgent free to NatWest, RBS, and Ulster business current account holders "for as long as they retain the account" [bankledger-freeagent-natwest-free], and shows the tax owed inside the banking app [bankledger-freeagent-natwest-tax-pr], so one bank already gives a ledger away to hold the account. Ramp's accounting agent (February 2026) auto-posts low-risk transactions and accrues what has not synced, then reverses it next month [bankledger-ramp-accounting-agent], and Brex syncs two-way with AI-native ERPs [bankledger-brex-accounting-api]; both still sync to an outside ERP, so spend platforms are a front end, not the book of record. UK banks reimburse authorised push payment fraud for individuals, microenterprises and charities up to £85,000 from 7 October 2024 [bankledger-psr-app-protections-start], which gives banks a reason to control payees.

Counter-case: the ledger stays a separate product even inside NatWest (opt-in, add-ons charged); spend platforms push to the ERP rather than replace it; a bank lending on books it prepared raises a self-review problem the judge flagged as the scenario's weak step.

What it would take to become a claim: a bank posting non-cash month-end entries (accruals, depreciation, deferred revenue) for business customers, or a bank credit policy that lends on its own kept ledger in place of borrower statements.

Open sub-questions:
- Does any bank in India, the UK, or the EU post accruals for business customers today?
- Does a bank lending on books it keeps need an outside review, and who pays for it?
- Does switching banks become switching ledgers, and does the EU Data Act's export right cover it?

0002F draft scenario, the mirror case (not added, 7.70 then 8.47 vs lowest 2036 9.60): "By 2036 the vendor that hosts a mid-sized company's ledger is also its main working-capital lender, lending against receivables and inventory it watches nightly and pricing reserves on the close agent's measured error rate, so the bank is reduced to a payment rail." Precedents: QuickBooks Capital lending on QuickBooks data since 2017; SAP Taulia working capital since 2022. Contradicts 2036-bank-keeps-the-small-company-ledger (same three things, opposite hands). Judge: who runs the blind sample the lender prices (conflict), 'large share' unsupported. What would lift it: an ERP vendor offering an asset-based line priced on ledger data to mid-sized companies.
