# Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection

URL: https://arxiv.org/abs/2302.12173
Type: primary
Read in session: 0005B

Summary: Greshake et al, Feb 2023. LLM apps blur data vs instructions. Attacker plants prompt in data likely to be retrieved; no direct interface needed. Demoed on Bing Chat, GPT-4 apps. Retrieved prompt acts like arbitrary code execution; controls which APIs get called. Mitigations lacking.

Quotes:
- "We argue that LLM-Integrated Applications blur the line between data and instructions." — Greshake et al., abstract
- "enable adversaries to remotely (without a direct interface) exploit LLM-integrated applications by strategically injecting prompts into data likely to be retrieved" — Greshake et al., abstract
- "We show how processing retrieved prompts can act as arbitrary code execution, manipulate the application's functionality, and control how and if other APIs are called." — Greshake et al., abstract
- "effective mitigations of these emerging threats are currently lacking" — Greshake et al., abstract
