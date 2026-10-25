# Oracle ARCS: Creating Amortizing or Accreting Transactions

URL: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/adarc/admin_amortizing_accreting_trans_manually_106xe1af307f.html
Type: vendor
Read in session: 0007C

Summary: System computes amortization schedule and ending amount; ending must be 0.00 else error forces manual correction. Rule-computed roll-forward check inside the reconciliation.

Quotes:
- "The Ending Amount for amortizing transactions must result in a 0.00 balance; otherwise, an error is displayed." — Oracle docs, Oracle ARCS: Creating Amortizing or Accreting Transactions
- "Ending Amount is calculated as the Original amount minus the Cumulative Amortization amounts for all periods up to and including the period to which the reconciliation pertains." — Oracle docs, Oracle ARCS: Creating Amortizing or Accreting Transactions
- "fractional pennies are carried over to the next period, until they equal one penny." — Oracle docs, Oracle ARCS: Creating Amortizing or Accreting Transactions
- "The sum of the amortization amounts in the summary will always be equal to the original amortization amount." — Oracle docs, Oracle ARCS: Creating Amortizing or Accreting Transactions
