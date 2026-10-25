# Oracle EPM Task Manager: Setting Task Predecessors

URL: https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/agfcc/cm_tasks_predecessors.html
Type: vendor
Read in session: 0008B

Summary: Oracle's close Task Manager supports predecessor links with four condition types. Dependencies gate when a successor may start or complete; nothing on the page says dates move automatically when a predecessor is late or errors, or that the schedule is re-planned. Behaviour is a static rule set (a successor waits, or proceeds on error only if the condition is Finish Error to Start).

Quotes:
- "The task starts as soon as the predecessor task completes or finishes with warning." — Oracle docs, Finish to Start condition (default)
- "The task starts as soon as the predecessor task completes, even if it is in error." — Oracle docs, Finish Error to Start condition
- "A task does not need predecessor tasks as long as a start date and time is specified." — Oracle docs
- "the task begins when the predecessor tasks are started or complete (for Finish to Start) and the start date and time is reached" — Oracle docs
- "The task cannot be marked as Complete until the predecessor task is marked as complete." — Oracle docs, Finish to Finish
