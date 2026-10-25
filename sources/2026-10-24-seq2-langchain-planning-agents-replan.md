# LangChain blog: Plan-and-Execute Agents (LangGraph planning architectures)

URL: https://blog.langchain.com/planning-agents/
Type: vendor
Read in session: 0009B

Summary: LangChain team post (Feb 2024) describing three LangGraph agent architectures. Plan-and-execute re-calls a planner after execution to finish or generate a follow-up plan; LLMCompiler schedules tasks as dependencies are met and has a Joiner that dynamically replans. These are reference patterns/tutorial code that users assemble, not a managed product feature, and replanning is triggered by an LLM judgement, not by a due-date slip.

Quotes:
- "Once execution is completed, the agent is called again with a re-planning prompt, letting it decide whether to finish with a response or whether to generate a follow-up plan (if the first plan didn’t have the desired effect)." — LangChain Team
- "This unit schedules tasks once their dependencies are met." — LangChain Team, on the LLMCompiler task fetching unit
- "dynamically replan or finish based on the entire graph history (including task execution results)" — LangChain Team, on the LLMCompiler Joiner
- "This means it can execute a task list without having to re-plan every time." — LangChain Team, on ReWOO
- "It still is restricted by serial tool calling" — LangChain Team, on plan-and-execute
