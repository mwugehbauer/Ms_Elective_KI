# 03 — Agentic Design Patterns

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/03-agentic-design-patterns.md)

## Concept

"Design pattern" here means a recurring shape for how agents are orchestrated, independent of which framework you use. The pattern this repo demonstrates is **sequential pipeline**: agent A finishes completely, then hands its output to agent B. Other common patterns (covered more in later lectures): hierarchical/manager-worker, planner-executor, and reflection/critique loops.

The sequential pattern is the right default when steps genuinely depend on each other in order — you can't analyze research that doesn't exist yet.

## Original references

This series' design-pattern vocabulary (sequential pipeline, hierarchical/manager-worker, planner-executor, reflection loops — covered across lectures 03, 07, 08, 09) follows the catalogue laid out in:

> Lakshmanan, V. (2025). *Generative AI Design Patterns: Solutions to Common Challenges When Building GenAI Agents and Applications*. O'Reilly Media.

The underlying agent *architectures* (simple reflex, model-based reflex, goal-based, utility-based, learning agents) that these patterns build on come from the classic taxonomy in:

> Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 2: Intelligent Agents. Pearson.

No figure here — both are books, not openly licensed papers, so we cite rather than reproduce their diagrams. If you have access to either, look up their respective agent-architecture diagrams and compare them to the sequential pipeline below.

## In this repo

[crew.py:43-51](../../src/research_crew/crew.py#L43-L51):
```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True,
)
```

`Process.sequential` means: run `research_task` to completion (the `researcher` agent works alone), then run `analysis_task` (the `analyst` agent works alone, but receives the research output via `context: - research_task` in [tasks.yaml](../../src/research_crew/config/tasks.yaml)).

This is the simplest possible multi-agent pipeline: two agents, zero negotiation, zero branching.

## Exercise

1. Draw (on paper or in a markdown comment) the data flow of this crew: what goes in, what each agent receives, what each agent produces, what the final output is.
2. `Process` has another option: `Process.hierarchical` (we'll use it properly in lecture 08). For now, just find it in the CrewAI source (`crewai/process.py` in your `.venv`) and read its docstring. Write one sentence on how it differs from sequential.
3. Identify one real-world task (not research/reporting) that fits the sequential pattern well, and one that wouldn't (because the steps don't have a strict order).

## Stretch goal

Sequential process forces task order via list order in `self.tasks`. Try reordering `analysis_task` before `research_task` in the `tasks: List[Task]` mechanism (hint: task order comes from method definition order under `@task`) and predict what breaks before running it.
