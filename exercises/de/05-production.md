# 05 — KI-Agenten in Produktion

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/05-production.md)

Einen Agenten von "läuft auf meinem Rechner" in den Produktionsbetrieb zu bringen bedeutet: reproduzierbare Umgebungen, Observability darüber, was der Agent tatsächlich tut (nicht nur das Endergebnis), und einen Weg für Nicht-Entwickler, ihn zu nutzen. Nichts davon ändert die Agenten-Logik — es ist die operative Schicht darum herum. Für "Agenten-Betrieb" gibt es kein einzelnes bahnbrechendes Paper wie für RAG oder Tool-Nutzung — das wird hier als praxisorientiertes Thema behandelt, nicht als Forschungsergebnis:

> Lakshmanan, V. (2025). *Generative AI Design Patterns: Solutions to Common Challenges When Building GenAI Agents and Applications*. O'Reilly Media. (Siehe die Kapitel zu Deployment/Observability.)

## In diesem Repo

Dieses Projekt zeigt bereits den vollständigen Stack:

- **Reproduzierbare Umgebungen**: [.devcontainer/devcontainer.json](../../.devcontainer/devcontainer.json) + `uv.lock` bedeuten, dass jeder mit einem einzigen Befehl eine identische Umgebung erhält, lokal oder in Codespaces (siehe Übung 00).
- **Observability**: [streamlit_app.py](../../streamlit_app.py) abonniert CrewAIs Event-Bus (`crewai_event_bus`) und streamt `TaskStartedEvent`, `AgentExecutionStartedEvent`, `ToolUsageStartedEvent` usw. live, statt nur den finalen Report zu zeigen. Das ist derselbe Mechanismus, den Produktions-Monitoring nutzen würde — hier nur in einer Demo-UI dargestellt statt an ein Logging-Backend geschickt.
- **Zugang für Nicht-Entwickler**: die Streamlit-UI gibt jedem ein Themen-Eingabefeld und einen "Run"-Button, ohne dass Python-Kenntnisse nötig sind.

Lest [streamlit_app.py](../../streamlit_app.py) von Anfang bis Ende — achtet auf `crewai_event_bus.scoped_handlers()`, das Event-Listener nur für die Dauer eines einzelnen `kickoff()`-Aufrufs registriert, damit wiederholte Läufe im selben Prozess keine doppelten Handler anstapeln.

## Aufgabe

1. Führt `uv run streamlit run streamlit_app.py` aus und startet einen Lauf zu einem Thema, während ihr das Live-Event-Log beobachtet.
2. Fügt dem Live-Log einen neuen Ereignistyp hinzu: abonniert `ToolUsageErrorEvent` (bereits importiert) — Moment, das ist bereits in `run_crew()` verkabelt. Fügt statt­dessen `CrewKickoffStartedEvent` und `CrewKickoffCompletedEvent` hinzu (aus `crewai.events.types.crew_events`), damit das Log auch den Start und das Ende des gesamten Crew-Laufs zeigt, nicht nur einzelne Tasks.
3. Identifiziert eine Sache, die diesem Aufbau für *echten* Produktionseinsatz noch fehlt (z. B. persistente Logs über Neustarts hinweg, Alerting bei Fehlern, Mehrbenutzer-Nebenläufigkeit) — ihr müsst es nicht bauen, nennt es nur und erklärt, warum der aktuelle Aufbau es nicht hat.

## Zusatzaufgabe

Die Streamlit-App führt die Crew pro Anfrage in einem Hintergrund-`threading.Thread` aus. Was würde kaputtgehen, wenn zwei Nutzer gleichzeitig in zwei verschiedenen Browser-Tabs gegen denselben laufenden Streamlit-Prozess auf "Run Crew" klicken würden? (Tipp: denkt daran, dass `crewai_event_bus.scoped_handlers()` prozessweit wirkt, nicht pro Thread.)
