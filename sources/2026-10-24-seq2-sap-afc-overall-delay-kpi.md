# SAP Documentation: Financial Close Overall Delay (Advanced Financial Closing analytical app)

URL: https://help.sap.com/saphelp_ssb/helpdata/en/06/f93a5225ecbb10e10000000a44176d/content.htm
Type: vendor
Read in session: 0009B

Summary: SAP help page for a KPI app on closing task lists. It computes which tasks "cause delay" from buffers between a task's end and its successor's planned start, and the longest delay is the cycle's overall delay. It reports delay and lets users chase the responsible agent by SAP Jam or email; it does not re-date or re-sequence successors. Page is an older SAP help version (URL path saphelp_ssb), so current product behavior may differ.

Quotes:
- "You can also find out about the reasons for the overall delay and follow up through SAP Jam or emails so that the responsible agent can speed up." — SAP Documentation
- "The app compares the end time of all the task lists that have been picked out. The apps defines the end time of whichever task list that ends the latest as the end time of the current closing cycle." — SAP Documentation (the cycle ends when the last task list ends)
- "If the smallest sum is less than the planned duration of the task in question, the app considers that the task will cause delay." — SAP Documentation
- "The app chooses the longest delay among all the task lists that have been picked out as the overall delay in hours of the current closing cycle." — SAP Documentation
- "If a task is in progress, the app does not consider that the task will cause any delay no matter how little time is left till the end time of the closing cycle." — SAP Documentation
