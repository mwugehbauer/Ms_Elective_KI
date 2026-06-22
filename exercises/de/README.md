# Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../README.md)

Das sind die praktischen Übungssitzungen zu **Aktuelle Fallstudien der Digitalökonomie und der Künstlichen Intelligenz: Generative und Agentische KI**. Die Vorlesungstheorie wird über Folien im Kurs vermittelt; diese Reihe ist die praktische Begleitung dazu und nutzt dieses Repository als durchgängiges Beispiel — bewusst beschränkt auf die Konzepte, die im Code dieses Projekts tatsächlich gezeigt werden, statt eines umfassenden Überblicks über jedes agentische KI-Thema.

Jede Übung startet direkt mit der praktischen Arbeit statt mit einem eigenen Theorie-Block — sie webt gerade so viel Hintergrund aus dem jeweiligen Paper ein (ein kurzes Zitat und, wo vorhanden, dessen Originalabbildung), um das Konzept einzuordnen, und geht dann direkt in den Code:
- **In diesem Repo** — wo genau das Konzept bereits in `research_crew` auftaucht, mit Datei-/Zeilenverweisen
- **Aufgabe** — etwas, das ihr selbst implementiert oder verändert
- **Zusatzaufgabe** (optional) — eine schwerere Anschlussaufgabe für alle, die früher fertig sind

Diese Reihe wiederholt nicht, was die Vorlesung zu jedem Thema bereits behandelt — sie ist die praktische Begleitung, keine zweite Vorlesung.

Ihr solltet [Run the crew](../../README.md#getting-started--choose-one-option) (über Codespaces oder lokal) funktionsfähig haben, bevor Übung 1 beginnt.

Lakshmanans *Generative AI Design Patterns* wird als Begleitwerk in Übung 05 (Produktion) zitiert; alle anderen Zitate sind spezifische arXiv-Papers, aufgeführt pro Übung unter "Originalarbeit".

## Übungen

| # | Titel |
| --- | --- |
| [00](00-course-setup.md) | Einrichtung des Kurses |
| [01](01-agentic-frameworks.md) | Agentische Frameworks: CrewAI-Grundlagen |
| [02](02-tool-use.md) | Tool-Nutzung |
| [03](03-agentic-rag.md) | Agentisches RAG |
| [04](04-multi-agent-pattern.md) | Multi-Agenten-Pattern |
| [05](05-production.md) | KI-Agenten in Produktion |
| [06](06-securing-agents.md) | KI-Agenten absichern |

## Benotete Team-Aufgabe

Begleitend zu den Übungen entwerfen Teams ihre eigene Crew zu einem Thema ihrer Wahl und bauen sie Meilenstein für Meilenstein aus, sobald neue Übungsinhalte neue Fähigkeiten freischalten — mit einer kritischen Risiko-/Grenzenanalyse als Hauptabgabe und funktionierendem Code als optionalem Bonus. Siehe [Überblick zur Aufgabe](assignment-overview.md), [Meilensteine der Aufgabe](assignment-milestones.md) und [Vorlagen für die Aufgabe](assignment-templates.md).

## Für Lehrende

Jede Übung verweist auf reale Dateien in `src/research_crew/`. Lassen Sie Studierende direkt in ihrem eigenen Codespace oder Fork arbeiten — siehe das Haupt-[README](../../README.md) für die beiden Einrichtungsoptionen. Musterlösungen sind bewusst nicht enthalten; falls Sie eine Referenzimplementierung zur Bewertung möchten, lassen Sie Studierende einen PR gegen ihren eigenen Fork öffnen, damit Sie den Diff überprüfen können. Für die Team-Aufgabe speziell siehe den Abschnitt "Für Lehrende" im [Überblick zur Aufgabe](assignment-overview.md#für-lehrende) für Repo-/Team-Setup.
