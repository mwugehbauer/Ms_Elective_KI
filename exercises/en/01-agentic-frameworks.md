# 01 — Agentic Frameworks: CrewAI Basics

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/01-agentic-frameworks.md)

An agentic *framework* gives you reusable building blocks so you don't hand-roll the think-act-observe loop yourself. CrewAI's four core abstractions:

- **Agent** — role, goal, backstory, LLM, tools
- **Task** — a description, expected output, and which agent is assigned to it
- **Crew** — a collection of agents + tasks + a process for running them
- **Process** — the orchestration strategy (we'll cover the two main ones in later exercises)

Other frameworks (LangGraph, AutoGen, Microsoft Agent Framework, OpenAI's Agents SDK) model the same ideas differently — CrewAI's signature choice is the explicit `Agent`/`Task`/`Crew` separation and YAML-driven config. This split is one concrete implementation of a more general pattern from the LLM-agent literature:

> Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2023). *A Survey on Large Language Model based Autonomous Agents*. [arXiv:2308.11432](https://arxiv.org/abs/2308.11432)

![Unified framework for the architecture design of LLM-based autonomous agents: Profile, Memory, Planning, Action modules](../assets/agentsurvey-wang2023-fig2.png)
*Figure 2 from Wang et al. (2023): a unified LLM-agent architecture of Profile, Memory, Planning, and Action modules. Reproduced for educational use in this course.*

Mapped onto CrewAI: an `Agent`'s `role`/`goal`/`backstory` in `agents.yaml` is the **Profile** module; `tools` plus the task loop is the **Action** module.

## In this repo

Open [src/research_crew/crew.py](../../src/research_crew/crew.py) top to bottom — it's short on purpose. Map each part to the concept:

| Concept | Where |
| --- | --- |
| `@CrewBase` class | [crew.py:10](../../src/research_crew/crew.py#L10) — marks `ResearchCrew` as a CrewAI project, auto-loads the YAML configs |
| Agents | `researcher` and `analyst` methods, each decorated `@agent` |
| Tasks | `research_task` and `analysis_task`, each decorated `@task` |
| Crew | the `crew()` method, decorated `@crew`, assembles everything |
| Config-driven roles | [config/agents.yaml](../../src/research_crew/config/agents.yaml) — role/goal/backstory live in YAML, not Python |
| Config-driven tasks | [config/tasks.yaml](../../src/research_crew/config/tasks.yaml) — description/expected_output/agent assignment |

Notice the YAML files use `{topic}` placeholders. [main.py](../../src/research_crew/main.py) passes `inputs = {'topic': '...'}` into `.kickoff(inputs=inputs)`, and CrewAI substitutes it everywhere `{topic}` appears.

## Task

1. In [config/tasks.yaml](../../src/research_crew/config/tasks.yaml), the `analysis_task` has `context: - research_task`. Find what this does by checking the CrewAI docs or experimenting: remove it, re-run the crew, and see how the analyst's report changes. Put it back.
2. Add a brand new field to `agents.yaml` under `researcher` — try `max_iter: 5` — and explain (in a comment or your notes) what you think it controls before checking the docs.

## Stretch goal

Without changing any *logic*, rename the `analyst` agent to `editor` everywhere it's referenced (Python method name, YAML key, `tasks.yaml`'s `agent:` field) and confirm the crew still runs. This is a good test of whether you actually understand how the pieces connect, since CrewAI wires agents to tasks by name.

---

**Team assignment:** this exercise unlocks [**Milestone M0: Baseline**](assignment-milestones.md#m0-baseline) of the [team assignment](assignment-overview.md) — your own two-agent, sequential crew design is due.
