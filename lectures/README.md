# Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](de/README.md)

This series teaches agentic AI concepts using this repository as the running example. It follows the structure of Microsoft's [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) course, adapted to CrewAI and grounded entirely in this project's code instead of abstract examples.

Every lecture has the same shape:
- **Concept** — what the idea is and why it matters
- **Original paper** — the seminal paper (or book/spec) behind the concept, with a reproduced figure where one exists and is openly available
- **In this repo** — exactly where that concept already shows up in `research_crew`, with file/line references
- **Exercise** — something students implement or modify themselves
- **Stretch goal** (optional) — a harder follow-up for students who finish early

Students should have [Run the crew](../README.md#run-the-crew) working (via Codespaces or locally) before lecture 1.

Two companion texts are cited across multiple lectures rather than per-session: Russell & Norvig's *Artificial Intelligence: A Modern Approach* (foundational agent definitions, lectures 01 and 03) and Lakshmanan's *Generative AI Design Patterns* (the pattern catalogue behind lectures 03, 07, 08, 09, 10). All other citations are specific arXiv papers or protocol specs, listed per lecture under "Original paper."

## Sessions

| # | Title | Maps to AI Agents for Beginners |
| --- | --- | --- |
| [00](en/00-course-setup.md) | Course Setup | 00-course-setup |
| [01](en/01-intro-to-ai-agents.md) | Intro to AI Agents | 01-intro-to-ai-agents |
| [02](en/02-agentic-frameworks.md) | Agentic Frameworks: CrewAI Basics | 02-explore-agentic-frameworks |
| [03](en/03-agentic-design-patterns.md) | Agentic Design Patterns | 03-agentic-design-patterns |
| [04](en/04-tool-use.md) | Tool Use | 04-tool-use |
| [05](en/05-agentic-rag.md) | Agentic RAG | 05-agentic-rag |
| [06](en/06-trustworthy-agents.md) | Building Trustworthy Agents | 06-building-trustworthy-agents |
| [07](en/07-planning-pattern.md) | Planning Pattern | 07-planning-design |
| [08](en/08-multi-agent-pattern.md) | Multi-Agent Pattern | 08-multi-agent |
| [09](en/09-metacognition.md) | Metacognition | 09-metacognition |
| [10](en/10-production.md) | AI Agents in Production | 10-ai-agents-production |
| [11](en/11-agentic-protocols.md) | Agentic Protocols (MCP/A2A) | 11-agentic-protocols |
| [12](en/12-context-engineering.md) | Context Engineering | 12-context-engineering |
| [13](en/13-agent-memory.md) | Agent Memory | 13-agent-memory |
| [14](en/14-securing-agents.md) | Securing AI Agents | 18-securing-ai-agents |

Not covered: the source course's "Microsoft Agent Framework" and "Browser-use / Computer Use Agents" modules are framework-specific to tools outside CrewAI's scope and are intentionally omitted.

## For instructors

Each exercise references real files in `src/research_crew/`. Have students work directly in their own Codespace or fork — see the main [README](../README.md) for the two setup options. Solutions aren't included on purpose; if you want a reference implementation for grading, ask students to open a PR against their own fork so you can review the diff.
