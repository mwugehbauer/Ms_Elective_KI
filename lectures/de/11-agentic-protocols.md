# 11 — Agentische Protokolle (MCP / A2A)

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/11-agentic-protocols.md)

## Konzept

Bisher ist jedes Tool in dieser Crew Python-Code, der in diesem Repo lebt. **MCP (Model Context Protocol)** ist ein Standard dafür, dass Tools in einem separaten Prozess leben (sogar in einer anderen Sprache, sogar auf einer anderen Maschine) und jedem Agenten-Framework zur Verfügung stehen, das MCP spricht — statt eine CrewAI-spezifische `BaseTool`-Unterklasse zu schreiben, richtet man einen Agenten auf einen MCP-Server aus, und dieser entdeckt automatisch die Tools, die der Server anbietet. **A2A (Agent-to-Agent)** ist ein verwandtes, aber anderes Protokoll, damit zwei unabhängige Agenten (potenziell von unterschiedlichen Frameworks/Anbietern) direkt kommunizieren können.

Der Vorteil: ein einmal als MCP-Server gebautes Tool funktioniert mit CrewAI, LangGraph oder jedem anderen MCP-kompatiblen Framework — im Gegensatz zu einer `BaseTool`-Unterklasse, die nur in CrewAI funktioniert.

## Originalquellen

Beide Protokolle sind Industriespezifikationen statt peer-reviewter Papers, daher zitieren wir sie als technische Spezifikationen:

> Anthropic (2024). *Model Context Protocol Specification*. https://modelcontextprotocol.io/specification

> Google (2025). *Agent2Agent (A2A) Protocol Specification*. https://a2a-protocol.org/latest/specification/

Hier keine Abbildung — beides sind lebende Web-Spezifikationen ohne ein einzelnes kanonisches Paper-Diagramm; aktuelle Architekturdiagramme findet ihr auf den jeweiligen Webseiten.

## In diesem Repo

Aktuell nutzt nichts MCP, aber `crewai` (die hier installierte Version) hat native Unterstützung dafür über `Agent(mcps=[...])`:

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

Das verbindet sich über stdio mit einem MCP-Server als Subprozess und stellt automatisch alle vom Server definierten Tools bereit — keine `BaseTool`-Unterklasse nötig.

## Übung

Das ist eine konzeptionelle Lektion mit leichter Erkundung, kein vollständiger Aufbau, da MCP-Server typischerweise externe Prozesse sind:

1. Lest die Docstrings in `crewai/mcp/config.py` (in eurer `.venv`) für `MCPServerStdio`, `MCPServerSSE` (oder die HTTP-Variante) — beachtet die drei Transport-Typen und wann ihr jeweils welchen nutzen würdet (lokaler Subprozess vs. entfernter Server).
2. Vergleicht: Was ist der *minimale* Code, um ein eigenes Python-Tool hinzuzufügen (Lektion 04, `BaseTool`-Unterklasse), im Vergleich zum Minimum, um ein MCP-Server-Tool hinzuzufügen? Was ist über Frameworks hinweg besser wiederverwendbar? Was lässt sich für ein einmaliges, repo-lokales Tool schneller schreiben?
3. Findet einen öffentlich dokumentierten MCP-Server (sucht nach "MCP server list") und schreibt einen Satz dazu, was er bereitstellt.

## Zusatzaufgabe

Falls ihr Node.js verfügbar habt, verkabelt das obige Filesystem-MCP-Server-Beispiel tatsächlich in den `researcher`-Agenten und gebt ihm einen Task, der das Lesen einer lokalen Datei erfordert. Vergleicht das Tool-Aufruf-Verhalten des Agenten mit dem eigenen Tool, das ihr in Lektion 04 gebaut habt.
