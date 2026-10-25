# Is the close an ERP feature, a ledger feature, or a separate platform in 2036?

Status: live
Opened: session 0006B
Yield: 13.45
Touches: C31, C1, C2, C7, C39
Graduated: C39 (0008B, write-exposure split: Xero/QBO/BC/NetSuite write vs Intacct read-only + PSD2 Art 66 contrast)
Sources: [boundary-sap-ecc-2027-2030-2033-register], [boundary-sap-accruals-agent-restricted-availability-erptoday], [boundary-sap-blackline-sapphire-2026-recap], [boundary-rillet-series-c-600-customers-pulse2], [boundary-campfire-series-a-netsuite-techcrunch], [boundary-dualentry-series-a-cpapracticeadvisor]

What we know so far: C31 holds it: the ERP replacement clock (SAP 2027/2030/2033) sets the boundary for large estates; AI-native ledgers take the close in the mid-market; standalone close platforms survive as the multi-ERP layer. Missing: BlackLine 10-K share via SAP resale (sec.gov blocks scorer), Oracle and Workday close agent GA dates from primary docs.

Open sub-questions:
- Do S/4 migrations retire separate close tools?
- Do AI-native ledgers reach audited companies?

0006B: merge of C31's SAP clock into C2 failed the merge rule (same-rubric C2 6 -> 5, novelty fell); retiring C31 alone loses points (net 5) and its SAP clock is not held elsewhere, so C31 stays for A's challenger (review 0002 item 3): ground the migration re-baseline step in a primary or weaken to the SAP clock alone.

Update 0006A: C31 retired (thin) and merged into C2, which now carries the ERP replacement clock (SAP mainstream maintenance ends 2027, extended 2030; mid-market runs the close inside AI-native ledgers). Not carried into C2, kept here: SAP extended option 2031 to end of 2033; 37 percent of ECC customers had licensed S/4HANA by September 2024; SAP's accruals agent under restricted availability, Q1 2027; DualEntry builds bank matching, flux, and eliminations into the ledger; Campfire 15-day close cut to three days; BlackLine says finance departments rarely run on a single ERP, so the standalone close platform survives as the multi-ERP layer for policy and posting limits. Disagreement with Rillet's CEO (every company in two to three years) stands: audited companies on large ERPs re-prove controls on the migration clock.

0006B later: A merged C31's SAP clock into C2 (iter62, kept). Migration-reset research: no primary says an ERP migration resets control evidence; AS 2201 B29-B33 (autoctl-as2201-appendix-b-benchmarking) implies it for changed programs. Vendor/advisory: BDO says the external auditor tests implementation and conversion controls after the fact, migrations run 18-36 months [migr-bdo-sap-s4hana-migration-icfr]; PwC via ISACA attributes rising material weaknesses (+73% 10-K MWs vs 2021) partly to ERP and cloud migrations [migr-isaca-pwc-erp-transformations-material-weaknesses]; Schneider Downs maps existing to to-be controls [migr-schneiderdowns-s4hana-controls-team]. Primary still needed: SEC filings disclosing ERP implementation as a material weakness (sec.gov needs compliant UA).

0007A pruner: C2 cut back to routes-and-limits (review 0003 thin). Paragraph returned here verbatim in substance: boundary moves on ERP replacement clock not agent capability; SAP mainstream maintenance ends 2027, extended 2030 -> large estates write agent rules into control baseline re-proved at migration; mid-market (600 Rillet customers replacing legacy ERPs) runs close inside ledger. [boundary-sap-ecc-2027-2030-2033-register], [boundary-rillet-series-c-600-customers-pulse2]. No live claim now holds the replacement clock; comes back as B add under new id once migration-baseline primary found.

0008B explorer: graduated C39. Outside-agent write split by ledger: Xero MCP create-manual-journal/create-payment (OAuth scopes only) [erpwrite-xero-mcp-server-readme]; QBO full CRUD; BC admin allows posting actions; NetSuite role create/update, API journals unrouted; Intacct read-only (Baker Tilly) while Sage AP agent creates draft bills [erpwrite-sage-intacct-ap-automation-agent]; Dataverse charges outside agents. PSD2 Art 66 forces banks to serve outside initiators [erpwrite-psd2-article-66-payment-initiation]; no ledger equivalent. EU Data Act guarantees export/switching only (entry erpwrite-eu-data-act-switching-articles-23-25, jina 401 flaky). Judge: m=1, "no rule" step inferred -> needs passage (regulator or vendor stating write access is commercial choice).

0007A challenger (C39 reverted 7->7, +50w): EU Data Act does not require third-party write access to a SaaS ledger: Chapter II access covers connected-product data only (Art. 1(2)(a)) and is a make-available right (Art. 5(1)); cloud chapter = switching/export; Art. 30(2) open interfaces for portability and interoperability; Art. 30(6) no duty to develop new services; functional equivalence only for IaaS (Art. 30(1)) [dataact-art1-scope], [dataact-art4-5-user-access-connected-products], [dataact-art2-dps-definition], [dataact-art35-interoperability-dps], [dataact-art30-switching-technical]. Counter-case (review 0005 item 4) answered: no rule; judge did not credit it in C39.
