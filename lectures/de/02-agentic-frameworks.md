# 02 — Agentische Frameworks: CrewAI-Grundlagen

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/02-agentic-frameworks.md)

## Konzept

Ein agentisches *Framework* gibt euch wiederverwendbare Bausteine, damit ihr die Denken-Handeln-Beobachten-Schleife nicht selbst von Hand bauen müsst. Die vier Kern-Abstraktionen von CrewAI:

- **Agent** — Rolle, Ziel, Backstory, LLM, Tools
- **Task** — eine Beschreibung, das erwartete Ergebnis und welcher Agent dafür zuständig ist
- **Crew** — eine Sammlung von Agenten + Tasks + ein Prozess für deren Ausführung
- **Process** — die Orchestrierungsstrategie (die zwei wichtigsten behandeln wir in späteren Lektionen)

Andere Frameworks (LangGraph, AutoGen, Microsoft Agent Framework, OpenAIs Agents SDK) modellieren dieselben Ideen unterschiedlich — CrewAIs charakteristische Entscheidung ist die explizite Trennung von `Agent`/`Task`/`Crew` sowie YAML-gesteuerte Konfiguration.

## Originalarbeit

CrewAIs Aufteilung in `Agent`/`Task`/`Crew` ist eine konkrete Umsetzung eines allgemeineren, vereinheitlichenden Frameworks, das in der LLM-Agenten-Literatur vorgeschlagen wurde:

> Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., & Wen, J. (2023). *A Survey on Large Language Model based Autonomous Agents*. [arXiv:2308.11432](https://arxiv.org/abs/2308.11432)

![Vereinheitlichtes Framework für die Architektur von LLM-basierten autonomen Agenten: Profile, Memory, Planning, Action Module](../assets/agentsurvey-wang2023-fig2.png)
*Abbildung 2 aus Wang et al. (2023) — ein vereinheitlichtes Framework für die Architektur von LLM-Agenten: die Module Profile, Memory, Planning und Action. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

Übertragen auf CrewAI: das `role`/`goal`/`backstory` eines `Agent` in `agents.yaml` ist das **Profile**-Modul; `tools` plus die Task-Schleife ist das **Action**-Modul; spätere Lektionen behandeln **Memory** (13) und **Planning** (07) als eigene CrewAI-Funktionen.

## In diesem Repo

Öffnet [src/research_crew/crew.py](../../src/research_crew/crew.py) von oben bis unten — es ist bewusst kurz gehalten. Ordnet jeden Teil dem Konzept zu:

| Konzept | Wo |
| --- | --- |
| `@CrewBase`-Klasse | [crew.py:10](../../src/research_crew/crew.py#L10) — markiert `ResearchCrew` als CrewAI-Projekt, lädt automatisch die YAML-Konfigurationen |
| Agenten | Methoden `researcher` und `analyst`, jeweils mit `@agent` dekoriert |
| Tasks | `research_task` und `analysis_task`, jeweils mit `@task` dekoriert |
| Crew | die Methode `crew()`, mit `@crew` dekoriert, fügt alles zusammen |
| Konfigurationsgesteuerte Rollen | [config/agents.yaml](../../src/research_crew/config/agents.yaml) — Rolle/Ziel/Backstory leben in YAML, nicht in Python |
| Konfigurationsgesteuerte Tasks | [config/tasks.yaml](../../src/research_crew/config/tasks.yaml) — Beschreibung/erwartetes Ergebnis/Agentenzuweisung |

Beachtet, dass die YAML-Dateien `{topic}`-Platzhalter verwenden. [main.py](../../src/research_crew/main.py) übergibt `inputs = {'topic': '...'}` an `.kickoff(inputs=inputs)`, und CrewAI ersetzt `{topic}` überall, wo es auftaucht.

## Übung

1. In [config/tasks.yaml](../../src/research_crew/config/tasks.yaml) hat `analysis_task` ein `context: - research_task`. Findet heraus, was das bewirkt — in der CrewAI-Dokumentation oder durch Ausprobieren: entfernt es, führt die Crew erneut aus und beobachtet, wie sich der Report des Analysten ändert. Setzt es danach wieder ein.
2. Fügt unter `researcher` in `agents.yaml` ein komplett neues Feld hinzu — probiert `max_iter: 5` — und erklärt (in einem Kommentar oder euren Notizen), was ihr glaubt, dass es steuert, bevor ihr in der Dokumentation nachschaut.

## Zusatzaufgabe

Benennt, ohne irgendeine *Logik* zu ändern, den `analyst`-Agenten überall, wo er referenziert wird, in `editor` um (Python-Methodenname, YAML-Schlüssel, `agent:`-Feld in `tasks.yaml`) und prüft, dass die Crew weiterhin läuft. Das ist ein guter Test, ob ihr wirklich verstanden habt, wie die Teile zusammenhängen, denn CrewAI verknüpft Agenten und Tasks über deren Namen.
