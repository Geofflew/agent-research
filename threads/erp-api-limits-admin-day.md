# What does the ERP administrator do when outside agents hit the ERP's API limits?

Status: live
Opened: session 0008C
Yield: 0.0
Touches: C39, C10; scenarios/2031-erp-meters-outside-agents; threads/erp-vs-close-boundary-2036; threads/general-agent-accountant-day
Sources: [expq4-netsuite-suitecloud-plus-concurrency], [expq4-ms-power-platform-request-limits]

What we know so far: ERPs already meter outside calls, by concurrency or daily requests, and the fix is buying capacity. NetSuite: "each suitecloud plus license increases the account base limit for concurrent web services requests by 10", governed per account, and "the account limit is lenient" [expq4-netsuite-suitecloud-plus-concurrency] (vendor). Microsoft's Power Platform gives per-user daily requests ("40,000 + 40,000 = 80,000 requests available per 24 hours") and under high usage "you might see throttling ... add capacity", or "assign a process license to the flow" [expq4-ms-power-platform-request-limits] (vendor). So the 2031 metering scenario needs no new mechanism, only a price per write: the administrator's day already includes watching throttling and buying licenses for integrations, and an agent posting a month of journals in a close week is the load that triggers it.

What it would take to become a claim: an ERP price list charging per agent action or per MCP tool call, or a release note applying API limits to agent principals specifically.

Open sub-questions:
- Does a close-week burst of agent writes exceed concurrency limits at a mid-market NetSuite account?
- Does the agent's request count against the user it acts for (Power Platform per-user) or against a process license?
