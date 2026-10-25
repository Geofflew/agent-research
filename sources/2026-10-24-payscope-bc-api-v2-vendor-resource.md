# Business Central API v2.0: vendor resource

URL: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/resources/dynamics_vendor
Type: vendor
Read in session: 0008B

Summary: The standard v2.0 vendor object has address, tax, currency, payment term and payment method fields but no bank account number, IBAN or SWIFT property and no bank navigation. Standard v2.0 vendor writes therefore do not carry bank details.

Quotes:
- "Specifies which payment method the vendor uses." — vendor properties table, paymentMethodId
- "Specified the tax registration number of the vendor." — vendor properties table, taxRegistrationNumber
- "Gets the contactsinformation of the vendor." — vendor navigation table
