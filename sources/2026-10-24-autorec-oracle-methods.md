# Oracle ARCS: About Auto Reconciliation Methods

URL: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/suarc/setup_profile_auto_reconciliation_methods.html
Type: vendor
Read in session: 0007C

Summary: Oracle Account Reconciliation setup guide. Lists auto-rec methods (zero balance, no activity, balance within range, balance match % and # tolerance) and conditions. Success sets status Closed; preparer and reviewer steps done automatically. Balance Comparison zero-balance ignores subsystem balance.

Quotes:
- "If the balance associated with the reconciliation for a given period is 0, then the reconciliation is prepared and reviewed automatically for that period." — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
- "If the balance is not 0, then the reconciliation must be manually prepared and reviewed." — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
- "The threshold percentage is multiplied against the source system balance to calculate a threshold value." — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
- "If the difference between the source system balance and the subsystem balance is less than the threshold value in a period, then the reconciliation is prepared and reviewed automatically for that period." — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
- "Enter the Match Balance Threshold (Percent) as a whole number between 1 and 100." — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
- "The prior reconciliation status must be Complete." — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
- "Age is recalculated by subtracting the Open Date from the new period end date" — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
- "If a previous reconciliation does not exist, then the prior reconciliation Source System balance is presumed to be zero" — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
- "For Balance Comparison format with No Activity, you can use a custom rule to obtain the correct results." — Oracle docs, Oracle ARCS: About Auto Reconciliation Methods
