# Continuous transaction controls

Definition: Tax-authority regimes (clearance or near-real-time reporting of every invoice) that give an outside party the transaction record directly, so the authority can produce figures such as a pre-filled VAT return without asking the company.

Sub-question: structure

Related concepts: [[adoption-ladder]], [[close-as-state]], [[shared-record-schema]]

Evidence:
- Italy SdI has cleared invoices in real time since 2019 and offers optional pre-filled VAT ledgers and returns from 2021 [italy-sdi-prefilled-vat] (secondary, search-summary only).
- EU ViDA mandates e-invoicing and near real-time reporting for intra-EU transactions from 1 July 2030, EN 16931 format [vida-digital-reporting].
- 2026 national mandates (Belgium Jan, Poland Feb/Apr, France Sep) are staggered and use different platforms [eu-einvoicing-2026-mandates] (vendor marketing).
- Scope is VAT/transaction level, not ledger, close or audit assertions.

- Authority builds the books: Chile SII register of purchases and sales from e-documents, company book duty removed (2017) [ctc2-sii-chile-prefilled-f29-from-dte]; India GSTR-2B read-only, taxpayer told to reconcile own books to it [ctc2-gst-gstr2b-auto-drafted-itc]. C7 step 2.
- Payment leg: Fedwire ISO 20022 up to 9,000 chars structured remittance naming invoices [ctc2-fed-iso20022-eri-remt]; BoE CHAPS structured remittance [ctc2-boe-chaps-iso20022-structured-remittance]. C7 step 3.
- Thesis C7 (0007C): AP/AR preparer starts close from ledger-vs-authority residual (GSTR-2B read-only, must reconcile to books [ctc2-gst-gstr2b-auto-drafted-itc]); auditor tests residual list; spread clock = ViDA 1 Jul 2030 [vida-digital-reporting].

Open questions:
- Does a tax-authority copy of every invoice become a reconciliation source that auditors and agents rely on?
- Do national platforms converge before ViDA 2035?
0008B: C40 — authority payee registers (PL white list, CZ published accounts) let an ERP/agent check a new bank account against the tax-ID record; closes payee redirection that C7 completeness logic did not cover.
0008B: C41 — India PSB credit model reads GST + AA bank data instead of borrower-prepared statements; close stops being loan input, ledger-to-return reconciliation becomes month-end job.
0008B: C47 — GSTR-3B liability locked to GSTR-1; one GSTR-1A before 3B; close value for GST-read borrowers = accuracy before lock, not speed.

- C41 (0008A, absorbed C47): India's GSTR-3B liability locked to GSTR-1, one GSTR-1A before filing; the lender reads the locked return, so the close is worth what it fixes before the 20th.
0008B: C55 — Mexico CFDI cancellation needs buyer acceptance in 3 business days, silence accepts; buyer agent answering signs with company seal; control = accept rule + reject default for paid invoices.

- C7 (0009C): French buyer's refusal (Refus) is a mandatory platform status sent to the administration with a reason the norm frames; clerk's refusal joins the outside record.
- C55 (0009C): SAT primary pages: 3 business days, silence = acceptance; CFF 29-A cancellation window runs to the annual ISR return month.
