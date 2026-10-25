# Market access controls (pre-trade risk controls for automated order entry)

Definition: The regime under which automated systems may submit orders to a market: pre-set, systematic, threshold-based controls under the licensed firm's direct and exclusive control, annual certification, kill functionality, and auto-disable on breach. The one place regulators have already specified the shape of autonomous write authority in finance.

Sub-question: structure / trust

Related concepts: [[scoped-revocable-write-authority]], [[policy-engine-authorization]], [[approval-gates-for-agent-actions]]

Evidence:
- 17 CFR 240.15c3-5 (2010): controls reasonably designed to systematically limit financial exposure; reject orders over pre-set credit or capital thresholds; reject erroneous orders; direct and exclusive control; annual CEO certification [mktaccess-17cfr-240-15c3-5].
- FINRA 15-09: change management, independent testing, quick disable in minimal steps, pilot deployment scaled as results confirm [mktaccess-finra-reg-notice-15-09].
- Knight Capital, 1 Aug 2012: 4M+ orders in 45 minutes, loss over $460M, first 15c3-5 enforcement, $12M [mktaccess-knight-capital-wilmerhale].
- MiFID II RTS 6: price collars, max order value and volume, message limits, kill function, auto-disable after repeated executions until a designated person re-enables, annual self-assessment [mktaccess-mifid-rts6-2017-589].
- Nasdaq Rule 6130 (2014): per-MPID net notional exposure limit; on breach ports disabled and open orders cancelled; reactivation on request after explaining why safe [mktaccess-nasdaq-kill-switch-2014].

C16 (0005C): class-wide rule failure = step, not drift; drift trigger misses it within period; per-rule aggregate limit + mid-period disable.

C10 (0006A): disanalogy. trade final (FINRA 11892 break ~30 min, price thresholds) vs open-period journal reversible by company (D365 reversal, On hold period, user-group restriction). Irreversible points = payment release (UCC 4A-211) + Permanently closed period. Limits belong there; period status = journal kill switch [disanalogy-finra-11892-clearly-erroneous], [disanalogy-d365-close-gl-period-end], [disanalogy-ucc-4a-211-payment-cancel].

Open questions:
- Does any ERP let a period be restricted to exclude API/agent principals specifically (NetSuite, SAP, Intacct)?
- Which of these control types map to journal posting (amount cap, account scope, period lock, duplicate rejection, auto-disable, re-enable by a named person)?
- Would an ERP vendor adopt a 15c3-5-shaped certification for agent posting before any regulator requires it?

Thesis: C10 — shape only at payment release + period lock; absorbed C6 (0006A): journals = period status + D365 workflow threshold, payments = C24 deny list + release limits. C16 — shape reaches ledger via insurer conditions (correlated loss = one wrong agent rule across class), not regulator.
0007A: C10 absorbed C2. ERP agent connections scope by role + record type only; NetSuite approval routing skips CSV/script/web service/RESTlet records -> amount gate moves to close platform there; D365 per journal name workflow (agent submits). C24 now C23; C16 retired.
0008B: C39 — amount gate question arises only where ERP exposes posting to outside agents; write exposure is vendor choice (Xero/QBO/BC/NetSuite open, Intacct read-only), unlike PSD2 Art 66 for banks.
0008C: C10 experience — controller drops per-journal approval for agent entries; day before lock works open-period reversal list, takes agent group out of period; treasury re-enables disabled agent after reading tripped limit. D365 roadmap (to Mar 2027, ERP Today) plans agent-only restrictions on postings/payments = first agent-principal scope; no ERP publishes an amount limit for agents [erpclock-*].
0008B: C50 — French e-invoice issuance (Sept 2026/2027) is a third irreversible point: invoice final at issuance, so pre-release check fits billing agents.
0008B: C10 restated: hard limits at the points an outside party records the act (payment release, period lock, clearance invoice issuance); Italy SdI since 2019 shows draft vs auto-send choice.
