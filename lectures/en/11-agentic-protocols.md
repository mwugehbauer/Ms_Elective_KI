# 11 — Agentic Protocols (MCP / A2A)

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/11-agentic-protocols.md)

## Concept

So far, every tool in this crew is Python code living inside this repo. **MCP (Model Context Protocol)** is a standard for tools to live in a separate process (even a separate language, even on a separate machine) and be exposed to any agent framework that speaks MCP — instead of writing a CrewAI-specific `BaseTool` subclass, you point an agent at an MCP server and it auto-discovers the tools that server offers. **A2A (Agent-to-Agent)** is a related but different protocol for two independent agents (potentially from different frameworks/vendors) to communicate directly.

The payoff: a tool built once as an MCP server works with CrewAI, LangGraph, or any other MCP-compatible framework — versus a `BaseTool` subclass that only works in CrewAI.

## Original references

Both protocols are industry specifications rather than peer-reviewed papers, so cite them as technical specs:

> Anthropic (2024). *Model Context Protocol Specification*. https://modelcontextprotocol.io/specification

> Google (2025). *Agent2Agent (A2A) Protocol Specification*. https://a2a-protocol.org/latest/specification/

No figure here — both are living web specifications without a single canonical paper diagram; see their respective sites for current architecture diagrams.

## In this repo

Nothing currently uses MCP, but `crewai` (the version installed here) has native support for it via `Agent(mcps=[...])`:

```python
from crewai.mcp import MCPServerStdio

researcher_with_mcp = Agent(
    config=self.agents_config['researcher'],
    verbose=True,
    mcps=[
        MCPServerStdio(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-filesystem", "."],
        ),
    ],
)
```

This connects to an MCP server as a subprocess over stdio and auto-exposes whatever tools that server defines — no `BaseTool` subclass needed.

## Exercise

This is a conceptual + light-exploration lecture, not a full build, since MCP servers are typically external processes:

1. Read the docstrings in `crewai/mcp/config.py` (in your `.venv`) for `MCPServerStdio`, `MCPServerSSE` (or HTTP variant) — note the three transport types and when you'd use each (local subprocess vs. remote server).
2. Compare: what's the *minimum* code needed to add a custom Python tool (lecture 04, `BaseTool` subclass) vs. the minimum needed to add an MCP server tool? Which has more reusability across frameworks? Which is faster to write for a one-off, repo-local tool?
3. Find one publicly documented MCP server (search "MCP server list") and write one sentence on what it exposes.

## Stretch goal

If you have Node.js available, actually wire up the filesystem MCP server example above into the `researcher` agent and give it a task that requires reading a local file. Compare the agent's tool-call behavior to the custom tool you built in lecture 04.
