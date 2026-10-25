# Agentic Commerce Protocol (OpenAI, Stripe): Delegate Payment RFC

URL: https://raw.githubusercontent.com/agentic-commerce-protocol/agentic-commerce-protocol/main/rfcs/rfc.delegate_payment.md
Type: standard
Read in session: 0004

Summary: ACP (OpenAI + Stripe maintained, beta, Apache 2.0) Delegate Payment RFC: issues delegated vault token for card credential, usable by merchant PSP only inside allowance (one_time, max_amount in minor units, currency, checkout_session_id, merchant_id, expires_at). Answers earlier gap: token IS bounded. RFC status draft, version 2025-09-29. Repo README (same repo) says maintained by OpenAI and Stripe, latest stable spec 2026-04-17.

Quotes:
- "delegate payment credential tokenization and controlled usage via allowance constraints" — ACP Delegate Payment RFC, scope line
- "the returned token **must only** be usable within the provided **allowance** (reason, max_amount, currency, expiry)." — ACP Delegate Payment RFC, 2.5 usage and expiry
- "the token **must** become invalid at or after `allowance.expires_at`." — ACP Delegate Payment RFC, 2.5 usage and expiry
