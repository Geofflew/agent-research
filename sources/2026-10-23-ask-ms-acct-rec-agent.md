# Microsoft Learn: Account Reconciliation Agent (production ready preview)

URL: https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/acct-rec-agent
Type: vendor
Read in session: 0007C

Summary: The agent raises exceptions in a workspace and recommends one action each; the user accepts or picks another. It covers only two exception types. Admin sets daily/monthly exception limits and alerts, and the agent skips runs when a limit is hit. Every agent action can be undone, returning the exception to unmitigated. No person is asked anything; the user opens the queue.

Quotes:
- "recommends actions for voucher amount mismatch exceptions" — Microsoft Learn, note under agent recommendations
- "Specify the exception limits to apply during processing (daily or monthly)" — Microsoft Learn, setup steps
- "The system triggers a notification when the agent skips processing due to reaching a configured limit" — Microsoft Learn, alert settings
- "The agent doesn't run until" — Microsoft Learn, setup steps (confirmation step)
- "Every exception is logged to capture the history of actions that users, automation, or agents take" — Microsoft Learn, benefits
- "The exception then returns to an unmitigated state" — Microsoft Learn, undo of a reconciled activity
- "Accept without change" — Microsoft Learn, alternative actions the user can select instead of the recommendation
