# OWASP LLM06:2025 Excessive Agency

URL: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
Type: standard
Read in session: 0005B

Summary: OWASP entry on agents with too much power. Damage follows from manipulated/ambiguous LLM output regardless of cause. Root causes: functionality, permissions, autonomy. Fixes: minimize tools, per-user context, human approval, downstream authorization outside LLM.

Quotes:
- "Excessive Agency is the vulnerability that enables damaging actions to be performed in response to unexpected, ambiguous or manipulated outputs from an LLM, regardless of what is causing the LLM to malfunction." — OWASP LLM06:2025
- "The root cause of Excessive Agency is typically one or more of: excessive functionality; excessive permissions; excessive autonomy." — OWASP LLM06:2025
- "An LLM-based application or extension fails to independently verify and approve high-impact actions." — OWASP LLM06:2025, Excessive Autonomy
- "Utilise human-in-the-loop control to require a human to approve high-impact actions before they are taken." — OWASP LLM06:2025, Prevention item 6
- "Track user authorization and security scope to ensure actions taken on behalf of a user are executed on downstream systems in the context of that specific user" — OWASP LLM06:2025, Prevention item 5
- "accesses downstream systems with a generic high-privileged identity" — OWASP LLM06:2025, Excessive Permissions
