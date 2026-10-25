# Service organization attestation

Definition: Independent auditor's report on a vendor's controls (SOC 1 for ICFR, SOC 2 trust services; Type 1 design at a point, Type 2 operating effectiveness over a period) that user auditors rely on instead of testing the vendor themselves; complementary user entity controls (CUECs) stay with the customer.

Related concepts: [[validation-harness]], [[ai-performance-insurance]], [[statistical-validation-of-automated-review]]

Evidence:
- Type 1 cannot reduce substantive procedures; Type 2 gives operating-effectiveness evidence [attest-auasb-gs007-user-auditor].
- Type 2 serves many user auditors; period overlap and assertion relevance matter; service assumes user controls [attest-isa402-type2-report].
- SOC 1 = controls relevant to user entities' ICFR [attest-aicpa-soc1-guide].
- AICPA + AIUC: SOC 2 controls opinion + AIUC-1 live agent testing (hallucination, leakage, injection); quarterly retest; full launch early 2027 [attest-aicpa-aiuc-joint-offering].
- No AI-specific SOC 2 criteria; clean reports can test different control sets [attest-csa-soc2-ai-gap].

Thesis: C18 — per-class agent error rate attested via SOC 1 Type 2-style report on vendor; blind sample + rule approval = CUECs; not attack testing.

Open questions:
- Will AICPA publish AI-specific criteria covering output accuracy rates? When?
- Does a vendor-level rate transfer to a client whose data differs (assertion relevance)?
