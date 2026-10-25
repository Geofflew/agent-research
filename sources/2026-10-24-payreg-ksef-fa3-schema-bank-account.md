# KSeF structured invoice schema FA(3): bank account fields

URL: https://crd.gov.pl/wzor/2025/06/25/13775/schemat.xsd
Type: standard
Read in session: 0008B

Summary: Official Ministry of Finance XSD for the FA(3) structured e-invoice (KSeF). The payment block carries the seller's bank account (RachunekBankowy, up to 100 per invoice) and separately a factor's account (RachunekBankowyFaktora, up to 20), each with full account number and optional SWIFT. So the payee account arrives as structured data on the invoice, matchable to the white list.

Quotes:
- "Informacje o rachunku" — FA(3) XSD, documentation of type TRachunekBankowy
- "Rachunek faktora" — FA(3) XSD, documentation of RachunekBankowyFaktora element
- "Numer rachunku" — FA(3) XSD, documentation of RachunekBankowy element (maxOccurs 100)
