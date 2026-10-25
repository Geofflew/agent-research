# Mandated spending authority

Definition: A signed, bounded grant that lets an agent commit money for a principal without that principal present, with a verifiable trail for disputes.

Sub-question: roles-and-economics

Related concepts: [[adoption-ladder]], [[agent-identity-and-delegation]], [[approval-gates-for-agent-actions]]

Evidence:
- AP2 uses verifiable credentials as mandates in Open and Closed stages; Open mandates set budget and allowed instruments in advance and enable human-not-present transactions; the chain gives a non-repudiable audit trail for accountability [ap2-docs-mandates].
- ACP (OpenAI, Stripe) passes secure payment tokens through agents; it is in beta (latest stable 2026-04-17); the README does not describe limits [agentic-commerce-protocol-readme].
- Visa and Mastercard agent products were not read; their status is unverified here.

Open questions:
- Is a purchase-order or payment-run approval limit in an ERP the same shape as an AP2 Open mandate, and could a close agent hold one?
- Who bears liability in the dispute chain when an agent exceeds intent?
