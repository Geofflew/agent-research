# Federal Reserve Board: New Message Format for the Fedwire Funds Service (ISO 20022 adoption notice)

URL: https://www.govinfo.gov/content/pkg/FR-2021-10-06/html/2021-21801.htm
Type: primary
Read in session: 0005A

Summary: Fed Board notice (Fed Register 6 Oct 2021) adopting ISO 20022 for Fedwire. Defines extended remittance info (ERI) = invoice refs in payment. Notes remt.001 links to pacs.008 for reconcile. Structured ERI cap 9,000 chars. Does NOT name Referred Document element or amount fields; invoice-join premise supported only at concept level.

Quotes:
- "ERI generally refers to details in the payment message regarding the purpose of a business-to-business payment. For example, a business that sends a payment to a vendor could include details regarding the invoices against which the vendor should apply the payment." — Federal Reserve Board, footnote 3
- "The Reserve Banks plan to support up to 140 characters for unstructured remittance information and up to 9,000 characters for structured ERI" — Federal Reserve Board, response to comments
- "is a standalone nonvalue message that includes the remittance details related to a payment (e.g., invoice details). This message includes a reference to the value message so that the receiver can reconcile the remt.001 message to the value message (e.g., pacs.008)." — Federal Reserve Board, footnote on remt.001
- "include structured data elements that provide for potentially richer payment message data than the current Fedwire Funds Service message format" — Federal Reserve Board, background on ISO 20022
