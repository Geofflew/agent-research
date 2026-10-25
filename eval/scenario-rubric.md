# Scenario rubric

Fixed. Only the project maintainer edits this. Scenarios are the far view: they are allowed to go beyond the sources. They are judged on how coherent, anchored, bold, and consequential they are, not on whether a source states the conclusion.

You are scoring one scenario from a research program about agentic product experiences in ERP and financial close platforms over the next ten years. The research question, the titles of the defended claims in the thesis, and the scenario text are given.

Score each dimension 0, 1, or 2. Output JSON only: {"coherence":n,"anchoring":n,"clocks":n,"mechanism":n,"reach":n,"consequence":n,"surprise":n,"note":"<=20 words"}

coherence — Does the scenario hold together? 0: contradicts itself or a claim it says it depends on. 1: consistent but vague. 2: every part follows from the others and nothing in it contradicts the claims it names.
anchoring — Does it say which defended claims it depends on and what breaks if each is wrong? 0: no claims named. 1: names claims. 2: names at least three claims and says, for each, what in the scenario fails if that claim is false.
clocks — Are its dates tied to stated clocks (a standard's effective date, a regulation, a product deadline, a licensing cohort, a replacement cycle)? 0: undated or default years. 1: some dates tied. 2: every dated step names its clock.
mechanism — Is there a causal path from today to the scenario? 0: asserts the end state. 1: names causes. 2: a chain where each step is caused by the previous one and the first step is something observable now.
reach — How far from the present does it go? 0: today's products with more automation. 1: changes what a role does. 2: changes who the actors are, what is bought and sold, or what an institution (audit, lending, regulation, the profession) is for.
consequence — Does it say what a named role does differently in that year? 0: no. 1: one role, generally. 2: at least two roles, concretely: what they stop doing, start doing, and decide.
surprise — Would a close practitioner reading it today find it non-obvious and arguable rather than either obvious or absurd? 0: obvious or absurd. 1: somewhat. 2: non-obvious, arguable, and they could say what evidence would settle it.

Be strict. 2 is rare. A scenario that is bold but incoherent scores low on coherence and that is the point; a scenario that is safe scores low on reach and surprise and that is also the point.
