# Claude Code permissions docs

URL: https://code.claude.com/docs/en/permissions
Type: vendor
Read in session: 0004

Summary: Anthropic docs. Rules deny > ask > allow, first match wins. Modes incl. plan, auto (background classifier), dontAsk, bypassPermissions. Admins disable bypass/auto via managed settings. Deny rules match command text only; hard enforcement via sandbox. Layered: rules, classifier, sandbox.

Quotes:
- "Rules are evaluated in order: deny, then ask, then allow. The first match in that order determines the outcome, and rule specificity doesn't change the order." — Claude Code docs, permission rules
- "For filesystem and network enforcement that doesn't depend on the command text" — Claude Code docs, Bash rule limits
- "A deny rule doesn't match the same program by path or inside sh -c" — Claude Code docs, WebFetch/network restriction note
- "These are most useful in managed settings where they can't be overridden." — Claude Code docs, disabling bypass and auto modes
- "before actions such as shell commands and network requests run, a background classifier checks that they align with your request" — Claude Code docs, auto mode
