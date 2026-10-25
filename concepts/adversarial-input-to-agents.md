# Adversarial input to agents

Definition: Fraud and prompt injection arriving through documents the agent reads (invoices, vendor emails); attacker never talks to agent. Payments BEC is the finance case.

Related concepts: [[agent-identity-and-delegation]], [[scoped-revocable-write-authority]], [[confidence-routing]]

Evidence:
- 76% US orgs payments fraud 2025; 74% BEC; checks 58% [fraud-afp-2026-payments-fraud-release].
- BEC exposed losses $55.5B, 305,033 incidents; verify account changes via secondary channel [fraud-ic3-bec-55-billion].
- LLM apps blur data vs instructions; retrieved text controls API calls [fraud-greshake-indirect-prompt-injection].
- EchoLeak: one email, zero-click, evaded XPIA classifier [fraud-echoleak-copilot-zero-click].
- OWASP: no fool-proof prevention; limit agency, human approval for high-impact [fraud-owasp-llm01-prompt-injection], [fraud-owasp-llm06-excessive-agency].
- Callback to on-file number, pending state, second approver [fraud-stampli-bank-change-callback] (vendor).

Thesis: C23 — reading agent never holds payee/bank-change or release authority; out-of-band person verifies regardless of confidence.

Open questions:
- Any AP agent incident via injected invoice?
- Do ERP agent permission models (NetSuite, Workday ASOR) block vendor bank field edits by agents?
0008B: C40 — where a tax authority publishes account-to-tax-ID pairs, the bank-detail deny list of C23 relaxes to "register match only"; injected email cannot change the register.
