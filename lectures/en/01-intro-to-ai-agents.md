# 01 — Intro to AI Agents

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/01-intro-to-ai-agents.md)

## Concept

An **AI agent** is an LLM given three things a plain chatbot doesn't have:
1. A **role/goal** — a specific job, not "answer anything"
2. **Tools** — ways to act on the world (search the web, call an API, read a file) beyond just generating text
3. **Autonomy over a task** — it decides *how* to use its tools to reach its goal, rather than following a fixed script

A single LLM call answers one prompt. An agent can take multiple steps: think, call a tool, look at the result, decide what to do next, repeat until done.

## Original paper

The formal definition of a rational agent (perceives its environment via sensors, acts via actuators, chooses actions to maximize performance) goes back to the standard AI textbook:

> Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.), Chapter 2: Intelligent Agents. Pearson.

The "think, act, observe, repeat" loop CrewAI implements is the exact pattern formalized for LLMs in:

> Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023). *ReAct: Synergizing Reasoning and Acting in Language Models*. ICLR 2023. [arXiv:2210.03629](https://arxiv.org/abs/2210.03629)

![ReAct combines reasoning traces and actions, compared to reasoning-only and acting-only prompting](../assets/react-yao2022-fig1.png)
*Figure 1 from Yao et al. (2023) — comparing standard prompting, reasoning-only (Chain-of-Thought), acting-only, and ReAct's interleaved reasoning+acting on two tasks (HotpotQA, AlfWorld). Reproduced from the paper for educational use in this course.*

This is exactly the loop you'll watch the `researcher` agent execute in the exercise below: a `Thought` (reasoning), an `Act` (tool call), an `Obs` (observation), repeated until the agent decides it's done.

## In this repo

Open [src/research_crew/crew.py](../../src/research_crew/crew.py). The `researcher` agent ([crew.py:17-23](../../src/research_crew/crew.py#L17-L23)) is a complete minimal example:

```python
@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config['researcher'],
        verbose=True,
        tools=[SerperDevTool()]
    )
```

- Its **role/goal/backstory** come from [config/agents.yaml](../../src/research_crew/config/agents.yaml) — read that file. Notice `{topic}` is a placeholder filled in at runtime.
- Its **tool** is `SerperDevTool()` — without it, the agent could only use knowledge baked into the LLM at training time; with it, the agent can search the live web.
- Its **autonomy**: nobody tells it which search queries to run. Given the task description, it decides.

Run the crew with `verbose=True` already set, and watch the terminal (or the Streamlit demo) — you'll see the researcher agent thinking, choosing a search query, reading results, and deciding whether it has enough information yet.

## Exercise

1. Run the crew (`uv run research_crew`) with a topic of your choice (edit `inputs` in [main.py](../../src/research_crew/main.py)).
2. Read the verbose terminal output. Identify the exact moment the agent decides to call its tool, and the moment it decides it's done researching.
3. In your own words (a few sentences, no code), explain: what would be different if `researcher` had no tools at all? Would the agent still "do" anything, or just generate text once?

## Stretch goal

Temporarily remove `tools=[SerperDevTool()]` from the `researcher` agent and re-run. Compare the report quality/specificity to a run with the tool present. Put the tool back afterward.
