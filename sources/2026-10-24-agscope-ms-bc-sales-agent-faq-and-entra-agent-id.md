# BC agent FAQ (permission sets + profile) and Entra Agent ID access models

URL: https://learn.microsoft.com/en-us/dynamics365/business-central/faqs-sales-order-taker-agent
Type: vendor
Read in session: 0007A

Summary: BC FAQ: permission sets define objects/data and read/update/delete; a separate UI profile limits pages/fields/actions available to the agent (field-level restriction via UI role). Companion Entra page (https://learn.microsoft.com/en-us/entra/agent-id/identity-platform/what-is-agent-id) names two agent access models: autonomous (rights given directly to agent identity) and delegated (user's rights).

Quotes:
- "The agent runs as its own user in Business Central and is granted access only to the necessary parts of the product." — BC FAQ, Access and permissions
- "The permission sets define which objects and data the agent can access and whether it can read, update, or delete them." — BC FAQ, Access control
- "The agent can interact only with the UI elements available in the profile assigned to the agent account and with data allowed by the agent's permission sets." — BC FAQ, profile section
- "agents can act autonomously, using access rights given directly to the agent identity." — Entra Agent ID overview (what-is-agent-id), autonomous access
- "agents can act on behalf of human users, using access rights given to the user." — Entra Agent ID overview, delegated access
