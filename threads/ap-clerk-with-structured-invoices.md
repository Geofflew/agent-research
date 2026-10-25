# What is left for the payables clerk when invoices arrive as structured e-invoices both ledgers can read?

Status: live
Opened: session 0008C
Yield: 0.0
Touches: C7, C40, C23; scenarios/2036-invoice-becomes-a-shared-record; threads/tax-authority-record-as-evidence; threads/payee-change-verification
Sources: [expq2-be-fps-einvoice-faq-specific-questions]

What we know so far: Structured delivery removes keying but leaves three judgments with the clerk. Belgium's finance ministry FAQ (B2B Peppol mandate from 1 January 2026) says "Peppol doesn't know whether an invoice is a duplicate of the original invoice or not" and "Ideally, duplicate detection should be included in the accounting system"; an invoice sent to the wrong recipient is rejected by an Invoice Response with status "RE"; and when mandatory detail such as the reverse-charge mention is missing, "You should not reject the invoice" but contact the provider [expq2-be-fps-einvoice-faq-specific-questions] (primary). So the clerk's day under the 2036 shared-record scenario keeps duplicate catching, wrong-recipient rejection, and supplier follow-up on incomplete invoices until the record itself is agreed by both sides, which is the step the scenario assumes.

What it would take to become a claim: a match-rate or touchless-rate figure for Peppol, SdI, or KSeF invoices against a purchase order, or a tax authority statement on duplicate detection.

Open sub-questions:
- Does the agent take duplicate detection and supplier follow-up, leaving the clerk only the rejections?
- In Poland (KSeF, 2026) does an invoice in the national system count as delivered, so a rejection becomes a correcting invoice instead?
