# In a lender-driven close, is the covenant add-back schedule where human judgment concentrates?

Status: live
Opened: session 0006B
Yield: 10.64 (0007A C29 +0.90)
Touches: C29, C21, C19, C27
Sources: [cov-matthews-form-compliance-certificate], [cov-bordeman-demerjian-2022-dch-replication], [cov-noetica-cost-savings-addbacks], [cov-xtract-compliance-certificates-private-borrowers], [cov-nini-smith-sufi-creditor-control-rights], [cov-dichev-skinner-2002-abstract], [matl-sab99-materiality-doj-copy]

What we know so far: C29 holds this as a claim. Gaps: Dichev and Skinner's bunching finding is only in the paper body (not fetchable); add-back prevalence data is from leveraged-loan documents, not private lender closes; no product found that links add-backs to agreement clauses.

What it would take to strengthen: private-credit (not broadly syndicated) add-back data; a lender-reporting product (Chronograph, Allvue, 73 Strings, Cascade) showing clause-linked add-backs; any lender statement on agent-prepared compliance certificates.

Open sub-questions:
- 0006A challenger (C29 reverted): monthly add-back review exists only where a maintenance covenant does. Proskauer: the significant majority of true mid-market direct lenders still insist on one; covenant-lite loans have no financial maintenance covenants (Fed CLO note) and test leverage only on an incurrence basis, at debt incurrence or distributions; springing revolver tests bite only above about 40% drawn. S&P (via ABL Advisor): add-backs inflated marketing EBITDA by over 28%, reported EBITDA 27% below in 2018. Open: what share of CAS-firm clients (C27) carry a maintenance covenant? Does the agent run the incurrence pro forma at event time? [cov-proskauer-covlite-vs-covloose], [cov-fed-clo-note-covlite-definition], [cov-dallasfed-incurrence-covenants-wp2311], [cov-sp-addbacks-2015-2019-ablreport]

- Does C21's covenant routing rule narrow to add-backs plus a headroom margin?
- Who signs the certificate when a CPA firm runs the close (C27)?

0007C iter 57: St. Louis Fed WP 2022-029: non-GAAP add-backs raise delinquency, default, downgrade; arrangers monitor less, sell down [addb-stlouisfed-ebitda-addbacks-step-too-far]. Counter: Badawi et al. permissiveness -> tighter covenants, fewer violations [addb-badawi-dyreng-hills-ebitda-permissiveness]. S&P 2018: realized EBITDA 29-34% under projection [addb-ii-sp-2018-addbacks-study]. spglobal.com blocks scripted fetch. Open: who reviews add-backs in the certificate.

0007A challenger (C29 reverted): key step "slack in add-backs, not managed entries" (judge: inferred). Primary passages found: Fan, Thomas, Yu (Mgmt Sci 2019, private loans): borrowers near EBITDA covenant misclassify core expenses as special items -> raises EBITDA, avoids violation [addb2-fan-thomas-yu-classification-shifting]. Reconciles with Bordeman-Demerjian (no DCH on debt/EBITDA): discretion moves from accrual size to special-item label, which contractual EBITDA removes. Ivashina-Vallee NBER 27316: avg 12 EBITDA modifications, 79 carve-outs, 76% of 5x firms can reach >6x [addb2-ivashina-vallee-weak-credit-covenants]. Badawi/de Fontenay full draft: permissiveness higher for volatile-accrual borrowers, tighter slack, fewer violations [addb2-badawi-defontenay-contractual-ebitda-draft]. Faria-e-Castro full text: +4.2% 60-day delinquency per add-back [addb2-faria-e-castro-addbacks-fulltext]. Draft edit: person decides every special/non-recurring label as add-back decision. Scored 10 then 8 on two judgements (+123 / +81 words) -> revert. Next: shorter edit swapping only the inferred step (<= +40 words). jina mirrors flaky (401/502).

0002F draft scenario (not added, 6.71 net): "By 2031 new mid-market credit agreements define covenant EBITDA as code that the lender's agent runs against the borrower's ledger every week, so the quarterly compliance certificate disappears and the negotiation moves to the code's add-back functions." Precedent: ISDA Common Domain Model (2019, open source since 2023) for derivatives terms as code. Contradicts 2031-lender-reads-the-authority-record (US/UK have no clearance record, so the lender reads the borrower's ledger). Judge: anchoring without failure analysis (it was there; noise or too thin), weekly ledger access unexplained. What would lift it: any loan agreement or agency platform with executable covenant definitions.
