# Agent pricing units

Definition: Unit agent vendors bill: seat, outcome (resolution/task completed), or consumption (credits per action). Outcome units outside finance define success as no human escalation.

Related concepts: [[validation-harness]], [[automation-bias]], [[preparer-and-reviewer-roles]]

Evidence:
- Intercom Fin: per resolution; assumed resolution = customer leaves w/o asking more; hard limits [price-intercom-fin-outcome].
- Zendesk: per automated resolution w/o escalation; base still per seat [price-zendesk-automated-resolution-pricing].
- Sierra: paid only on completed task; seat vendors conflicted [price-sierra-outcome-based-pricing].
- Salesforce: $2/conversation -> Flex Credits $0.10/action; licences convertible [price-salesforce-agentforce-flex-credits-release], [price-salesforce-agentforce-pricing-page].
- Workday Flex Credits: usage not headcount; only ERP analog found [price-workday-flex-credits].
- Gartner: no mass seat shrinkage seen; Salesforce back toward seat bundles [price-register-salesforce-seat-based-ai-licensing].

Thesis: C13 — outcome pricing exists in bookkeeping (zero-touch unit); audited-company close prices by credits spent only on reviewer-accepted items.

- Finance outcome pricing exists (C13, 0005A): Digits Apr 2026 charges accounting firms per client only if >=95% transactions zero-touch (no human create/edit before close) [fprice-digits-outcome-pricing-launch]; Deloitte ASC 606 spotlight: credits consumed only on success, or base fee + refunds below threshold [fprice-deloitte-dart-outcome-pricing-agentic-ai].

Open questions:
- Do BlackLine/FloQast publish agent pricing? Unit?
- Does credit pricing still bias vendor toward more actions (more agent work, less human)?
