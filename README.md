# Agent Research

A file-based research workflow that turns source excerpts into claims, challenges those claims, and explores competing futures. The worked example asks how agents could change ERP and financial close products over the next ten years.

The interesting part is the separation of evidence, inference, and speculation. Sources have attributed quotations. Claims must explain their reasoning. Scenarios can go further, but must name the assumptions and signposts that would make them plausible.

## Start here

- [Research synthesis](synthesis.md): the readable account of the findings and competing futures.
- [Current themes](themes.md): the main ideas connecting individual claims.
- [Defended claims](thesis.md): claims, supporting sources, and counter-evidence.
- [Future scenarios](scenarios/README.md): alternative outcomes rather than a single forecast.
- [Workflow](docs/methodology.md): roles, iteration rules, and evaluation limits.

This is a research prototype and an example corpus. It contains prompts, evaluation scripts, and report builders. Running the scripts does not start autonomous workers; an operator or agent runner supplies that orchestration.

## Run locally

Python 3.10 or later is sufficient for the offline checks and reports. The Python scripts use only the standard library.

```bash
python3 tools/check_public.py
python3 -m unittest discover -s tests -v
python3 eval/score.py --check
python3 eval/score_scenarios.py --check
python3 tools/progress.py
python3 tools/method.py
```

Open `progress.html` for a snapshot of the current corpus, `method.html` for the workflow, or `synthesis.html` for the research narrative. Reports can be rebuilt from a ZIP download without Git history.

### Optional model evaluation

Live evaluation needs an installed, authenticated Claude CLI and network access to the cited public pages. It sends research text to the CLI and uses the configured account's model usage.

```bash
export JUDGE_MODEL=sonnet
python3 eval/score.py --json
python3 eval/score.py --json --focus C26
python3 eval/score_scenarios.py --json
```

`JUDGE_MODEL` defaults to the CLI's `sonnet` alias; choose a supported model for your account. Judge results and fetched pages are cached locally. `--no-cache` clears the local cache for the thesis evaluator. Missing CLI access and invalid judge output stop evaluation with an error.

## How the loop works

1. Choose one unresolved question and gather public evidence.
2. Save source URLs, source types, and attributed excerpts in `sources/`.
3. Propose one change to a claim, with a causal argument and counter-evidence.
4. Verify the quotations, then evaluate the change with a separate judge.
5. Keep useful changes; move unresolved ideas to a thread.
6. Periodically review the thesis, synthesize themes, and test competing scenarios.

The role prompts in [CLAUDE.md](CLAUDE.md) can be used one at a time or by a separately configured runner. Evaluation criteria are kept apart from the research agent's edits.

## Repository map

| Path | Purpose |
| --- | --- |
| `question.md` | Research question and scope |
| `concepts/` | Definitions and reusable conceptual notes |
| `sources/` | Public source URLs, summaries, and attributed quotations |
| `threads/` | Questions and draft arguments that need more evidence |
| `thesis.md` | Current claims, including retired claims for context |
| `themes.md`, `horizons.md`, `synthesis.md` | Views across claims and scenarios |
| `scenarios/` | Explicitly speculative future scenarios |
| `eval/` | Quote-verification code and model-judge rubrics |
| `tools/` | Offline validation and static report generation |
| `tests/` | Offline evaluator and report checks |

## Reading the example

The research snapshot is dated **24 October 2026**. Forecasts, product descriptions, and regulatory interpretations are research arguments from that snapshot, not continuously maintained facts. Some claims are marked weak or retired; historical references in threads are retained as research context.

The public edition omits run logs, historical score ledgers, verification caches, worker locks, account-specific setup, and selected evidence. Claims affected by omitted evidence have been edited. No historical scores are presented as fresh measurements, and the edited corpus has not been re-evaluated by a live model. Some research threads retain old iteration notes; those record earlier experiments rather than scores for this edition.

A quote match checks wording, not whether a conclusion follows. The model judge is a heuristic: it can reward confident writing, miss errors, and vary between runs. The offline check validates local structure and citations; it does not fetch external pages or establish research accuracy. See [source policy](docs/source-policy.md) for attribution and [publication checks](docs/publication.md) for preparing your own copy.
