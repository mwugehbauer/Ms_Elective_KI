# 09 — Metacognition

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/09-metacognition.md)

## Concept

Metacognition means an agent (or the system around it) reflects on its own output and improves it, rather than emitting a first draft as final. Two common implementations:
- A **reviewer agent** that critiques another agent's output and sends it back for revision
- A **self-critique loop** where the same agent re-reads and improves its own work

This is different from a guardrail (lecture 06): a guardrail blocks/retries based on a pass/fail check, while metacognition is about *improving quality* through reflection, not gatekeeping.

## Original paper

Linguistic self-reflection — an agent verbally critiquing its own failed attempt and storing that critique to inform the next try — was formalized as a reinforcement signal that doesn't require updating model weights at all:

> Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., & Yao, S. (2023). *Reflexion: Language Agents with Verbal Reinforcement Learning*. NeurIPS 2023. [arXiv:2303.11366](https://arxiv.org/abs/2303.11366)

![Reflexion diagram: an agent's trajectory is evaluated, a self-reflection is generated from the evaluation and added to memory, and the next trajectory is informed by that reflection](../assets/reflexion-shinn2023-fig1.png)
*Figure 1 from Shinn et al. (2023) — Reflexion across decision-making, programming, and reasoning tasks: a trajectory is scored by an evaluator, a verbal self-reflection is generated and stored in memory, and the next attempt's trajectory is conditioned on that stored reflection. Reproduced from the paper for educational use in this course.*

The `reviewer` agent you build in the exercise below plays the role of Reflexion's "Self-reflection" step, and feeding its critique back via a guardrail (the stretch goal) is exactly the "next trajectory informed by reflection" loop in the diagram.

## In this repo

Nothing here does this yet — `analysis_task`'s output goes straight to `output_file='output/report.md'` with no review step ([config/tasks.yaml](../../src/research_crew/config/tasks.yaml)). This is the gap for this exercise.

## Exercise

1. Add a third task, `review_task`, assigned to a new `reviewer` agent (or reuse `analyst`) whose job is to critique the report: does it fully address the topic, is anything vague or unsupported, is the executive summary actually executive-summary-length?
2. Give `review_task` `context: - analysis_task` so it receives the report.
3. Decide on a structure for the critique output: either (a) the reviewer rewrites the report directly with fixes applied, or (b) the reviewer produces a list of issues that a human (you) reads and decides whether to act on. Implement one.
4. Run the full crew and read the reviewer's critique. Was it substantive (caught a real gap) or generic ("looks good!")? If generic, revise the reviewer's `goal`/`backstory` in `agents.yaml` to demand specificity, and compare.

## Stretch goal

Make it an actual loop instead of a one-pass review: if the reviewer's critique contains specific issues, feed those back into a guardrail on `analysis_task` (lecture 06) so the analyst must address them before the crew considers the task done. This combines metacognition (the critique) with guardrails (enforcement) — notice how the two patterns compose.
