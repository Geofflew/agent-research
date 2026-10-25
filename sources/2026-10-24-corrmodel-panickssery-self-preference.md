# LLM Evaluators Recognize and Favor Their Own Generations (Panickssery, Bowman, Feng, 2024)

URL: https://arxiv.org/abs/2404.13076
Type: primary
Read in session: 0001F

Summary: Shows LLM judges score their own outputs higher than others' while humans rate them equal (self-preference). Out of the box, GPT-4 and Llama 2 distinguish their own text from other LLMs and humans with non-trivial accuracy. Fine-tuning shows a linear relation between self-recognition and self-preference strength, with controlled experiments against confounders. Implication: same-model checking is biased.

Quotes:
- "new biases are introduced due to the same LLM acting as both the evaluator and the evaluatee" — Panickssery et al., arXiv abstract
- "an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality" — Panickssery et al., arXiv abstract
- "we discover a linear correlation between self-recognition capability and the strength of self-preference bias" — Panickssery et al., arXiv abstract
