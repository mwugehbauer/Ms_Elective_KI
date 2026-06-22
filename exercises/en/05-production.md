# 05 — AI Agents in Production

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/05-production.md)

Moving an agent from "works on my machine" to production means: reproducible environments, observability into what the agent is actually doing (not just the final output), and a way for non-developers to run it. None of this changes agent logic — it's the operational layer around it. There's no single seminal paper for "agent operations" the way there is for RAG or tool use — this is covered as a practitioner topic rather than a research result:

> Lakshmanan, V. (2025). *Generative AI Design Patterns: Solutions to Common Challenges When Building GenAI Agents and Applications*. O'Reilly Media. (See the deployment/observability chapters.)

## In this repo

This project already demonstrates the full stack:

- **Reproducible environments**: [.devcontainer/devcontainer.json](../../.devcontainer/devcontainer.json) + `uv.lock` mean anyone gets an identical environment, locally or in Codespaces, with one command (see exercise 00).
- **Observability**: [streamlit_app.py](../../streamlit_app.py) subscribes to CrewAI's event bus (`crewai_event_bus`) and streams `TaskStartedEvent`, `AgentExecutionStartedEvent`, `ToolUsageStartedEvent`, etc. live, instead of only seeing the final report. This is the same mechanism production monitoring would use — just rendered in a demo UI instead of shipped to a logging backend.
- **Non-developer access**: the Streamlit UI gives anyone a topic input box and a "Run" button, no Python required.

Read [streamlit_app.py](../../streamlit_app.py) end to end — note `crewai_event_bus.scoped_handlers()`, which registers event listeners for the duration of one `kickoff()` call only, so repeated runs in the same process don't stack duplicate handlers.

## Task

1. Run `uv run streamlit run streamlit_app.py` and run a topic while watching the live event log.
2. Add a new event type to the live log: subscribe to `ToolUsageErrorEvent` (already imported) — wait, it's already wired in `run_crew()`. Instead, add `CrewKickoffStartedEvent` and `CrewKickoffCompletedEvent` (from `crewai.events.types.crew_events`) so the log shows the very start and end of the whole crew run, not just individual tasks.
3. Identify one thing this setup is still missing for *real* production use (e.g. persistent logs across restarts, alerting on failures, multi-user concurrency) — you don't need to build it, just name it and explain why the current setup doesn't have it.

## Stretch goal

The Streamlit app runs the crew in a background `threading.Thread` per request. What would break if two users clicked "Run Crew" at the same time in two different browser tabs against the same running Streamlit process? (Hint: think about what `crewai_event_bus.scoped_handlers()` does process-wide, not per-thread.)
