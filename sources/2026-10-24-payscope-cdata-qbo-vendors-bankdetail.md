# CData QuickBooks Online adapter: Vendors table (VendorPaymentBankDetail)

URL: https://cdn.cdata.com/help/RNN/cis/pg_table-vendors.htm
Type: secondary
Read in session: 0008B

Summary: Third-party connector docs mapping the QBO Vendor entity show bank fields inside the vendor object (VendorPaymentBankDetail_*), so bank details are a field group in Vendor, not a separate entity. The account number is masked on read; writing bank detail needs vendor write. Intuit's own docs are JS-rendered and community pages blocked, so Intuit primary not confirmed.

Quotes:
- "The vendor's bank account number for payments." — CData Vendors table, VendorPaymentBankDetail_BankAccountNumber
- "In response, the value is masked and only the last four digits are returned." — CData Vendors table, same column
- "Required if the VendorPaymentBankDetail information is present in the request." — CData Vendors table, BankAccountName
