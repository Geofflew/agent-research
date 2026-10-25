# Shared record schema

Definition: A standard data format that lets an outside party read a company's figures or transactions without asking the company (XBRL, ISO 20022, EN 16931/Peppol, open-banking APIs).

Sub-question: structure

Related concepts: [[adoption-ladder]], [[close-as-state]], [[validation-harness]], [[continuous-transaction-controls]]

Evidence:
- Existing schemas cover different layers: figure-level and periodic (XBRL), payment-level between banks (ISO 20022), invoice-level (EN 16931), account-level for consumers (open banking). None covers the close itself [xbrl-data-quality-crenshaw], [swift-iso20022-cbpr].
- Schema adoption does not guarantee correctness: XBRL errors in revenue, net income and assets were reported [xbrl-data-quality-crenshaw].
- US open banking mandate is enjoined and under reconsideration [cfpb-1033-status].
- ISO 20022 conversion can truncate rich data in MT/MX mapping [swift-iso20022-cbpr].

Open questions:
- Which layer would carry an attestation by an agent?
- Can XBRL GL or SAF-T serve as the ledger-level interchange?
