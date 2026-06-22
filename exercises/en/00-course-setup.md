# 00 — Course Setup

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/00-course-setup.md)

Before writing any agent code, everyone needs an identical, working environment. The two failure modes that waste the most class time are: students stuck on local installs, and students missing API keys. We solve both before exercise 1.

## In this repo

This project supports two setup paths, documented in the main [README](../../README.md#getting-started--choose-one-option):

- **Option A: GitHub Codespaces** — zero local install, runs in the browser. The container automatically runs `uv sync` via [.devcontainer/devcontainer.json](../../.devcontainer/devcontainer.json).
- **Option B: Run locally** — `uv sync` on your own machine.

Either way, you need three API keys before anything will run:
- `GROQ_API_KEY` — powers the LLM behind every agent (`MODEL=groq/llama-3.3-70b-versatile`, set automatically by `main.py` if not already present)
- `SERPER_API_KEY` — powers the researcher agent's web search tool
- `GEMINI_API_KEY` — powers embeddings for knowledge/memory features, not the chat LLM (see exercise 03)

## Task

1. Pick a setup path (Codespaces or local) and get it running, following the README.
2. Get your own free API keys:
   - Groq: https://console.groq.com/keys (free tier)
   - Serper: https://serper.dev (free tier)
   - Gemini: https://ai.google.dev (free tier)
3. Add your keys: if you're on Codespaces, add them as **Codespaces secrets** at [github.com/settings/codespaces](https://github.com/settings/codespaces) *before* opening your codespace — this is the recommended path, since it means you never touch a file containing real keys at all. If you're running locally, copy `.env.example` to `.env` and fill them in there (not into `.env.example` itself — that file is committed and must stay empty).
4. Run the crew once:
   ```bash
   uv run research_crew
   ```
5. Confirm `output/report.md` was created and contains a real report (not an error).

If a key is missing, `main.py` now fails fast with a clear message naming exactly which key is missing and a link to get one — rather than a deep stack trace from inside `crewai`. If you see that message, fix it and rerun; if step 5 still fails after your keys are set, debug it now — every later exercise assumes this works. Other common first-run issues: a model name typo, hitting a free-tier rate limit (wait a minute and retry), or — if you're on a much older clone of this repo without the `MODEL` default in `main.py` — an `OPENAI_API_KEY is required` error, which means `MODEL` itself never reached the environment (Codespaces secrets bypass `.env.example`'s default value entirely; add `MODEL=groq/llama-3.3-70b-versatile` as a Codespaces secret too, or update `main.py`).

## Stretch goal

Run the Streamlit live-view UI instead of the plain CLI:
```bash
uv run streamlit run streamlit_app.py
```
Watch the agent/task/tool events stream in as the crew runs, instead of reading static terminal output.
