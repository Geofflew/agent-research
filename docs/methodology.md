# Method: research as a sequence of experiments

The workflow stores research state in ordinary files so a person can inspect the evidence and an agent can continue the work without relying on a long conversation.

## Evidence, claims, and scenarios

A source entry holds a URL, a declared type, a summary, and attributed quotations. A claim names its source entries and explains the reasoning that connects them. A scenario describes a possible future and names the claims, assumptions, clocks, and signposts it depends on.

These layers have different standards. A source quotation must match the source. A claim may infer beyond it but must explain the step. A scenario may imagine a world that does not yet exist, while making its assumptions visible.

## The iteration

Choose an unresolved question, collect evidence, propose one change, check the evidence, evaluate the argument, and decide whether to keep it. Add, strengthen, sharpen, split, merge, retire, and cut are different experiments. An attractive idea that is not yet supported stays in a thread.

The most valuable disagreement is with a documented position: a standard, a study, or a product design. Inventing an easy position to disagree with earns nothing. A new screen also earns little unless it changes what a preparer, reviewer, controller, or buyer actually does.

## Evaluating claims

The thesis evaluator first fetches cited public pages and checks source quotations after whitespace, punctuation, case, and HTML normalization. It then asks a separate model to score grounding, novelty, mechanism, specificity, consequence, tension, evidence, and reach.

The score is the sum of each live claim's grounded contribution, minus a per-claim cost and a word penalty. Source type caps the evidence dimension. Optional reviewer verdicts can cap a weak claim. Repeated model samples are combined by their median; a focused claim receives more samples.

Previously verified quotations can survive a temporary fetch failure if a local verification record exists. Such a record proves only an earlier text match. It does not prove that the source is still current or that the conclusion is correct. The public export starts without those records.

## Evaluating scenarios

Scenarios use a separate rubric: coherence, anchoring, clocks, mechanism, reach, consequence, and surprise. They have no quotation gate because they describe possible futures. Their score includes a length penalty. Passing the rubric does not turn a forecast into evidence.

## Independent review

A reviewer should read the arguments without seeing their scores first. Look for repeated sources, unsupported causal steps, incentives to write longer or bolder, and claims that only look novel because of their phrasing. Freeze the evaluator during an experiment; make rubric changes separately.

## Practical limits

Page extraction is basic and may fail on JavaScript pages, scanned PDFs, or blocked hosts. Source types are declared metadata rather than independently audited classifications. A matching quotation can still be misread. Model judgments can be biased or inconsistent. Small score differences should not determine a keep decision without inspecting the actual change.

The scripts evaluate and render files. They do not schedule agents, manage remote workers, or publish a repository. Those are responsibilities of the operator's runner.
