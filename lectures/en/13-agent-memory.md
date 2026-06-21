# 13 — Agent Memory

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/13-agent-memory.md)

## Concept

Memory lets an agent retain information *across* runs (or across tasks within a run) instead of starting from a blank slate every time. CrewAI distinguishes several kinds:
- **Short-term memory** — recent context within the current crew run
- **Long-term memory** — persisted across separate runs (e.g. "we researched this topic last week")
- **Entity memory** — facts about specific entities (people, organizations) the crew has encountered

This is different from RAG (lecture 05): RAG retrieves from documents you provided; memory retrieves from what the *crew itself* has previously said or learned.

## Original paper

The architecture behind "store everything that happens, periodically reflect on it, retrieve relevant pieces to inform future behavior" — which is essentially what CrewAI's short-term/long-term/entity memory implements — was introduced in:

> Park, J. S., O'Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23). [arXiv:2304.03442](https://arxiv.org/abs/2304.03442)

![Generative agent architecture: Perceive feeds a Memory Stream, which supports Retrieve, feeding Retrieved Memories into Plan and Act, with a feedback loop back into the memory stream](../assets/genagents-park2023-fig3.png)
*Figure 3 from Park et al. (2023) — the generative agent architecture: perceived events enter a Memory Stream, relevant memories are retrieved to inform Planning and Acting, and the results feed back into the stream. Reproduced from the paper for educational use in this course.*

CrewAI doesn't implement the "reflection" step (synthesizing many memories into higher-level insights) as explicitly as this paper does, but the core loop — write to memory, retrieve relevant pieces, let them shape the next action — is the same one `memory=True` turns on for this crew.

## In this repo

Memory is currently off — when we printed the crew object earlier in this project's setup, it showed `memory=False`, `short_term_memory=None`, `long_term_memory=None`, `entity_memory=None`. Turning it on is a one-line change to [crew.py](../../src/research_crew/crew.py):

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True,
    memory=True,
)
```

Like knowledge sources (lecture 05), memory also embeds content under the hood — so the same Gemini-embedder gotcha applies. Pass `embedder` (already configured in this crew) and it'll be reused for memory too.

## Exercise

1. Set `memory=True` on the `Crew` and re-run the crew twice in the same process for the *same* topic (e.g. run it from a script that calls `.kickoff()` twice, or run `uv run research_crew` twice without restarting — note CrewAI memory persists to local storage between CLI invocations too, since it's disk-backed).
2. Check `~/.local/share/crewai` or wherever CrewAI's memory storage path resolves (the CLI/verbose logs usually show it) — look for memory files written.
3. Run the crew on a topic that overlaps with a previous one (e.g. "Artificial Intelligence in Healthcare" then "Artificial Intelligence in Drug Discovery") and see if anything in the verbose log shows the agent referencing memory from the earlier run.

## Stretch goal

Memory persists indefinitely by default — for a class where many students share one set of memory storage paths (unlikely with separate Codespaces, but possible locally), this could leak information between runs. Look up how to scope/reset CrewAI memory (hint: `crew.reset_memories()` or deleting the storage directory) and explain when you'd want to do that in a real classroom setting.
