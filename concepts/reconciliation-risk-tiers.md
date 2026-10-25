# Reconciliation risk tiers

Definition: a company's written policy that sorts balance-sheet accounts by risk and predictability and sets how often each tier is reconciled and how it is reviewed; some policies let predictable accounts auto-certify within a tolerance on a per-account approval.

Sub-question: work

Related concepts: [[confidence-routing]], [[preparer-and-reviewer-roles]], [[approval-gates-for-agent-actions]]

Thesis: none live (draft C43 0008B in threads/which-close-tasks-go-first, 7 < bar 8) — the unreviewed share an agent reaches is the policy's predictable/static tier, approved account by account; C26 routes apply only inside it.

Evidence:
- Macquarie: monthly only subledger / >$10m / high-risk, others quarterly; BlackLine auto-certify within $10,000 tolerance, per-account director approval, bi-annual written re-confirmation [recrisk-macquarie-bs-reconciliation-procedure-autocertify].
- La Trobe: Critical monthly, Important quarterly, Static 6-monthly, Annual yearly; new accounts critical; master list re-tiered monthly [recrisk-latrobe-balance-sheet-reconciliation-policy].
- Stanford: frequency by risk, materiality, history; central sample review [recrisk-stanford-bs-reconciliation-fingate]. UMN: quarterly floor, preparer + approver on every rec [recrisk-umn-reconciling-verifying-gl-policy].
- Vendor cases: Aviva 66% system-certified (low-risk, rules-driven) [case-aviva-canada-blackline]; Sysco ~50% of 10,000+ [case-sysco-trintech-video].

Open questions:
- Any benchmark (APQC, Hackett) on share of static / zero-balance accounts, to test whether auto-certified share tracks it?
- Do agents get added to the approval list per account, or does a vendor release widen the list by default?
