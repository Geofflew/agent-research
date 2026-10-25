# OWASP LLM01:2025 Prompt Injection

URL: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
Type: standard
Read in session: 0005B

Summary: OWASP GenAI top-10 entry 1. Indirect injection = LLM ingests external files/sites with hidden instructions. Severity depends on agency of model. Admits no fool-proof prevention. Mitigations: least privilege, human approval high-risk, segregate untrusted content.

Quotes:
- "Indirect prompt injections occur when an LLM accepts input from external sources, such as websites or files." — OWASP LLM01:2025
- "These inputs can affect the model even if they are imperceptible to humans" — OWASP LLM01:2025
- "are largely dependent on both the business context the model operates in, and the agency with which the model is architected" — OWASP LLM01:2025
- "it is unclear if there are fool-proof methods of prevention for prompt injection" — OWASP LLM01:2025, Prevention
- "research shows that they do not fully mitigate prompt injection vulnerabilities" — OWASP LLM01:2025, on RAG and fine-tuning
- "Require human approval for high-risk actions" — OWASP LLM01:2025, Prevention item 5
- "Implement human-in-the-loop controls for privileged operations to prevent unauthorized actions." — OWASP LLM01:2025, Prevention
- "Provide the application with its own API tokens for extensible functionality, and handle these functions in code rather than providing them to the model." — OWASP LLM01:2025, Prevention item 4
