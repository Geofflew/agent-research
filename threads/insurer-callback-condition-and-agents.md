# Who must verify a changed bank instruction for the crime policy to pay once an agent runs payables?

Status: live
Opened: session 0008C
Yield: 0.0
Touches: C23, C40, C10; scenarios/2031-crime-insurer-licenses-the-payables-agent; threads/payee-change-verification; threads/insurer-as-first-outside-acceptor
Sources: [expq4-intact-social-engineering-callback-endorsement]

What we know so far: Social engineering cover is written around a person doing a callback and logging it. One carrier's endorsement pays only "provided, that prior to transferring, paying or delivering money ... an employee verified the transfer instruction according to a pre-arranged callback or other established verification procedure", adds that "such verification must be recorded, logged or otherwise documented", and requires the insured to "furnish an electronic recording or other documentation evidencing verification" [expq4-intact-social-engineering-callback-endorsement] (primary, policy form). So today the AP clerk's callback is not only a fraud control but the condition of cover: an agent that changes bank details and pays without an employee's logged callback leaves the loss uninsured, which is why C23's clerk keeps the callback and why the 2031 scenario needs the clause rewritten. C40's register match is an "other established verification procedure" only if the carrier says so.

What it would take to become a claim: a crime policy form or carrier bulletin addressing automated or AI verification of transfer instructions.

Open sub-questions:
- Does a Polish white-list lookup count as an "established verification procedure" under such wording?
- Who keeps the callback log when the agent drafts the payment and the clerk only calls?
0008C iter 95 (designer experience C23 kept 8->8, +17 words): clerk logs the callback, since the crime policy pays only on a recorded employee callback [expq4-intact-social-engineering-callback-endorsement]. iter 94 builder version scored 10 on untargeted t/r -> reverted as noise; unchanged text 8 confirms.
