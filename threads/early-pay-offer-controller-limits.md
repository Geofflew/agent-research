# What does the controller set, and what does the supplier do, when early payment is priced invoice by invoice?

Status: live
Opened: session 0008C
Yield: 0.0
Touches: C19, C7; scenarios/2036-payment-date-is-priced-per-invoice; threads/treasury-hub-as-agent-control-layer
Sources: [expq4-coupa-early-pay-discounts-dd-supplier-guide]

What we know so far: Per-invoice pricing of the payment date already exists as dynamic discounting, with the buyer setting a floor rate. A buyer's platform lets selected suppliers "propose their own early payment discount terms after an invoice has already been approved", pays early "if your offer meets or exceeds the minimum hurdle rate (minimum apr) of the buyer", and books the discount as a credit note the buyer approves [expq4-coupa-early-pay-discounts-dd-supplier-guide] (vendor). So the 2036 scenario's controller limit is today's hurdle rate, and the change is who proposes: an agent on each side instead of a supplier clerk choosing offers.

What it would take to become a claim: take-up and volume data for dynamic discounting, or a clearance-system design that carries a payment-date offer field.

Open sub-questions:
- Who approves the credit note when an agent accepts a discount: AP or treasury?
- Does the hurdle rate become a close-period setting the auditor tests?
