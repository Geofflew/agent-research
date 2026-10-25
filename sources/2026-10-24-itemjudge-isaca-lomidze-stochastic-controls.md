# Lomidze, Need for Extension of ISACA Frameworks for Non-Deterministic and Quantum Technologies (ISACA Tbilisi Chapter blog, 13 Aug 2026)

URL: https://engage.isaca.org/tbilisichapter/blogs/irakli-lomidze/2026/08/14/need-for-extension-of-isaca-frameworks-for-non-det
Type: secondary
Read in session: 0008A

Summary: Chapter-president opinion post, not ISACA guidance. Argues re-performance and sample-based testing assume determinism; an LLM making the per-item decision gives different classifications on the same input and model version, and hosted-model updates can pass change management while decision behavior drifts. Contrasts a rules engine, which the auditor can inspect and re-perform. Supports narrowing C42 to controls where the model judges each item; it is a rationale, not a standard.

Quotes:
- "The auditor submits the same complaint to the same model version and gets a different classification. Not necessarily a wrong one. A different one. Five runs, three escalations" — Irakli Lomidze, ISACA Tbilisi Chapter blog
- "Setting the sampling temperature to zero does not restore that: batching effects, floating-point non-associativity across hardware, silent model updates on hosted APIs and imperfectly reconstructed context all leave residual variance" — Irakli Lomidze, ISACA Tbilisi Chapter blog
- "An organization can therefore pass every change-management test in the framework while its actual decision behavior drifts with every update its vendor ships" — Irakli Lomidze, ISACA Tbilisi Chapter blog
- "Sample-based testing works because a control's behavior is a stable function of its configuration or its documented procedure, which is why change management rather than continuous observation is the anchor control" — Irakli Lomidze, ISACA Tbilisi Chapter blog
- "Re-performance, generally regarded as the strongest form of audit evidence, presumes that past behavior can be reproduced" — Irakli Lomidze, ISACA Tbilisi Chapter blog
- "Nothing in ITAF prepares the auditor for this" — Irakli Lomidze, ISACA Tbilisi Chapter blog
- "a stochastic control deviates by design, and its deviation rate is an intrinsic property with no cause to find" — Irakli Lomidze, ISACA Tbilisi Chapter blog
- "When the routing logic is a rules engine, the auditor inspects the rules, re-performs a sample of decisions against the deployed configuration, and signs off" — Irakli Lomidze, ISACA Tbilisi Chapter blog
- "The part that decides is not recorded in any configuration item the organization maintains" — Irakli Lomidze, ISACA Tbilisi Chapter blog
