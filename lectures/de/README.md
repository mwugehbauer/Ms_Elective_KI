# Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../README.md)

Diese Reihe vermittelt die Konzepte agentischer KI anhand dieses Repositorys als durchgängigem Beispiel. Sie folgt der Struktur des Microsoft-Kurses [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners), angepasst auf CrewAI und vollständig im Code dieses Projekts verankert statt anhand abstrakter Beispiele.

Jede Lektion hat denselben Aufbau:
- **Konzept** — was die Idee ist und warum sie wichtig ist
- **Originalarbeit** — das bahnbrechende Paper (oder Buch/Spezifikation) hinter dem Konzept, mit reproduzierter Abbildung, wo eine existiert und frei verfügbar ist
- **In diesem Repo** — wo genau dieses Konzept bereits in `research_crew` auftaucht, mit Datei-/Zeilenverweisen
- **Übung** — etwas, das Studierende selbst implementieren oder verändern
- **Zusatzaufgabe** (optional) — eine schwerere Anschlussaufgabe für alle, die früher fertig sind

Studierende sollten [Run the crew](../../README.md#getting-started--choose-one-option) (über Codespaces oder lokal) funktionsfähig haben, bevor Lektion 1 beginnt.

Zwei Begleitwerke werden über mehrere Lektionen hinweg zitiert statt pro Sitzung: Russell & Norvigs *Artificial Intelligence: A Modern Approach* (grundlegende Agentendefinitionen, Lektionen 01 und 03) und Lakshmanans *Generative AI Design Patterns* (der Pattern-Katalog hinter den Lektionen 03, 07, 08, 09, 10). Alle anderen Zitate sind spezifische arXiv-Papers oder Protokollspezifikationen, aufgeführt pro Lektion unter "Originalarbeit".

## Lektionen

| # | Titel | Entspricht AI Agents for Beginners |
| --- | --- | --- |
| [00](00-course-setup.md) | Einrichtung des Kurses | 00-course-setup |
| [01](01-intro-to-ai-agents.md) | Einführung in KI-Agenten | 01-intro-to-ai-agents |
| [02](02-agentic-frameworks.md) | Agentische Frameworks: CrewAI-Grundlagen | 02-explore-agentic-frameworks |
| [03](03-agentic-design-patterns.md) | Agentische Design-Patterns | 03-agentic-design-patterns |
| [04](04-tool-use.md) | Tool-Nutzung | 04-tool-use |
| [05](05-agentic-rag.md) | Agentisches RAG | 05-agentic-rag |
| [06](06-trustworthy-agents.md) | Vertrauenswürdige Agenten bauen | 06-building-trustworthy-agents |
| [07](07-planning-pattern.md) | Planning-Pattern | 07-planning-design |
| [08](08-multi-agent-pattern.md) | Multi-Agenten-Pattern | 08-multi-agent |
| [09](09-metacognition.md) | Metakognition | 09-metacognition |
| [10](10-production.md) | KI-Agenten in Produktion | 10-ai-agents-production |
| [11](11-agentic-protocols.md) | Agentische Protokolle (MCP/A2A) | 11-agentic-protocols |
| [12](12-context-engineering.md) | Context Engineering | 12-context-engineering |
| [13](13-agent-memory.md) | Agenten-Gedächtnis | 13-agent-memory |
| [14](14-securing-agents.md) | KI-Agenten absichern | 18-securing-ai-agents |

Nicht abgedeckt: Die Module "Microsoft Agent Framework" und "Browser-use / Computer Use Agents" des Quellkurses sind spezifisch für Tools außerhalb des Anwendungsbereichs von CrewAI und wurden bewusst ausgelassen.

## Für Lehrende

Jede Übung verweist auf reale Dateien in `src/research_crew/`. Lassen Sie Studierende direkt in ihrem eigenen Codespace oder Fork arbeiten — siehe das Haupt-[README](../../README.md) für die beiden Einrichtungsoptionen. Musterlösungen sind bewusst nicht enthalten; falls Sie eine Referenzimplementierung zur Bewertung möchten, lassen Sie Studierende einen PR gegen ihren eigenen Fork öffnen, damit Sie den Diff überprüfen können.
