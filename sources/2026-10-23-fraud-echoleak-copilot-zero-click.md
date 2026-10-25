# EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System

URL: https://arxiv.org/abs/2509.10540
Type: primary
Read in session: 0005B

Summary: Reddy and Gujral, Sep 2025. CVE-2025-32711, M365 Copilot. One crafted email, no user click, exfiltrates data. Chained bypass of Microsoft XPIA classifier. Lessons: least privilege, defense in depth, provenance-based access control.

Quotes:
- "a zero-click prompt injection vulnerability in Microsoft 365 Copilot that enabled remote, unauthenticated data exfiltration via a single crafted email" — Reddy and Gujral, abstract
- "evading Microsofts XPIA (Cross Prompt Injection Attempt) classifier" — Reddy and Gujral, abstract
- "achieved full privilege escalation across LLM trust boundaries without user interaction" — Reddy and Gujral, abstract
- "Our findings establish prompt injection as a practical, high-severity vulnerability class in production AI systems" — Reddy and Gujral, abstract
- "emphasizing the principle of least privilege, defense-in-depth architectures, and continuous adversarial testing" — Reddy and Gujral, abstract
