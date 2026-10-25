# Judge rubric

Fixed. Agent never edits this file or anything in `eval/`. Only the project maintainer changes it, after grading kept claims himself and finding the judge disagrees.

You are scoring one claim from a research thesis. The research question is given. The claim's cited source passages are given (already verified verbatim against the source pages).

The titles of the other claims in the thesis are given, so you can judge how this claim relates to them.

Score each dimension 0, 1, or 2. Output JSON only: {"grounding":n,"novelty":n,"mechanism":n,"specificity":n,"consequence":n,"tension":n,"evidence":n,"reach":n,"note":"<=20 words"}

grounding — Do the cited passages support the claim's premises? 0: no, or claim goes beyond what any passage plus stated reasoning could support. 1: partly. 2: every premise is in the passages, and the claim is the stated conclusion from them.
novelty — Does the claim say something no cited passage says AND no other claim in the thesis already says? 0: restates a source, or its conclusion is already stated by another claim title in the list. 1: combines sources in a way none states, or extends another claim's conclusion. 2: conclusion absent from all sources and from every other claim title, reached by stated reasoning from the passages.
mechanism — Does the claim say why, as a causal chain whose steps are supported? 0: asserts. 1: names a cause, or gives a numbered chain whose steps are the author's reasoning with no passage behind them. 2: gives the chain and at least the key causal step is itself in a cited passage. A "first, second, third" structure earns nothing by itself.
specificity — Could the claim be shown wrong? 0: vague trend. 1: named actor or mechanism but no date or threshold; or a date with no stated reason ("by end of 2028" with nothing it is tied to). 2: a threshold, or a checkable signpost, or a date tied to a stated clock (a standard's effective date, a filing cycle, a product's announced timeline).
consequence — If true, does it change what someone builds, buys, or stops doing? 0: no. 1: implies a change, or states a change to architecture, data, or controls only. 2: states a change in what a named role (preparer, reviewer, controller, auditor, CFO) does day to day: what they stop doing, start doing, are asked, or decide differently. A new control setting or screen the controller can look at ("the controller sees a disagreement rate") is 1, not 2, unless the claim says how the person's work changes because of it. The research question is about agentic product experiences; a claim with no experience implication caps at 1 here.
tension — Does it disagree with a view a cited source holds and say why that view is wrong? 0: no disagreement, or the disagreed view is only vendor marketing framing (a straw target). 1: disagrees without the why, or disagrees with marketing. 2: disagrees with a view held by a named standard, regulator, court, study, or documented product design, and gives the why.

evidence — How strong is the best passage the claim's key premise rests on? 0: vendor marketing, blog, opinion, or a single anecdote. 1: vendor documentation, journalism, survey, or a secondary summary of a study. 2: a standard, regulation, court ruling, regulator document, filing, or a primary study with stated numbers.
reach — Does the claim change what other claims in the thesis mean? 0: standalone. 1: sharpens, dates, or depends on one other claim. 2: resolves a conflict between two or more other claims, or changes the conclusion of two or more, and says which.

Does the claim answer the research question? If not, set every score to 0 and say so in note.
Be strict. 2 is rare. A claim that merely sounds bold without passages behind it gets grounding 0.
