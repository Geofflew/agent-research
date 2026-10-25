# Preparing a public export

Review the files and source provenance before sharing. Automated scans help find obvious problems; they cannot establish ownership or detect every confidential passage.

```bash
python3 tools/check_public.py
python3 tools/check_public.py --deny-term COMPANY_NAME --deny-term PRIVATE_DOMAIN
python3 -m unittest discover -s tests -v
python3 eval/score.py --check
python3 eval/score_scenarios.py --check
python3 tools/progress.py
python3 tools/method.py
```

The optional deny terms are case-insensitive literal checks across filenames and decoded text. Supply your own terms locally rather than committing private names to the policy.

Export only the reviewed working tree. Exclude Git history, fetched-page caches, model outputs, verification ledgers, run logs, credentials, and local environment files. A new public repository should start with a clean initial commit; copying a sanitized tree into a repository with private history does not remove that history.

The included CI check uses no secrets, external source fetches, or model calls. Live evaluation remains an explicit local action.
