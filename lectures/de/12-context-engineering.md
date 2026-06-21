# 12 — Context Engineering

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/12-context-engineering.md)

## Konzept

"Context Engineering" ist die Praxis, bewusst zu steuern, welche Informationen im Kontextfenster eines LLM landen: was enthalten ist, was ausgeschlossen wird, und wie es strukturiert ist — im Gegensatz dazu, einfach einen langen Prompt zu schreiben und auf das Beste zu hoffen. Speziell bei Agenten gehört dazu: Task-Beschreibungen, welche vorherigen Task-Ausgaben weitergegeben werden, welches Wissen/Gedächtnis abgerufen wird, und wie viel davon jeweils.

Das ist wichtig, weil Kontextfenster begrenzt und verrauscht sind — irrelevante Informationen kosten nicht nur Tokens, sie können das LLM auch aktiv von den relevanten Teilen ablenken.

## Originalarbeit

Den empirischen Beleg dafür, *warum* es wichtig ist, wo im Kontextfenster etwas steht — nicht nur, ob es überhaupt enthalten ist — liefert:

> Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). *Lost in the Middle: How Language Models Use Long Contexts*. Transactions of the Association for Computational Linguistics, 12, 157–173. [arXiv:2307.03172](https://arxiv.org/abs/2307.03172)

![U-förmige Genauigkeitskurve: die Modellgenauigkeit ist am höchsten, wenn das relevante Dokument am Anfang oder Ende des Kontexts steht, und fällt deutlich ab, wenn es in der Mitte steht, bei 20 abgerufenen Dokumenten insgesamt](../assets/lostinmiddle-liu2023-fig1.png)
*Abbildung 1 aus Liu et al. (2024) — Genauigkeit bei einer Multi-Dokument-QA-Aufgabe als Funktion davon, wo das Dokument mit der Antwort unter 20 abgerufenen Dokumenten steht: am höchsten an erster und letzter Position, am niedrigsten in der Mitte. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

Das ist direkt relevant für Übung 2 unten: Wenn ihr dem Analysten eine riesige, ungefilterte Recherche-Ausgabe übergebt, sind genau die nützlichsten Fakten in der *Mitte* davon am wahrscheinlichsten, ignoriert zu werden — unabhängig davon, wie groß Geminis beworbenes Kontextfenster ist.

## In diesem Repo

Drei Context-Engineering-Mechanismen sind bereits im Einsatz, es lohnt sich, sie explizit zu benennen:

1. **Templating** — `{topic}`-Platzhalter in [config/agents.yaml](../../src/research_crew/config/agents.yaml) und [config/tasks.yaml](../../src/research_crew/config/tasks.yaml), ersetzt durch `inputs` in [main.py](../../src/research_crew/main.py#L13-L15). Das fügt genau die Variable, die wichtig ist (das Thema), in jeden Prompt ein, ohne dass ihr manuell Strings formatieren müsst.
2. **Selektive Kontext-Weitergabe** — das Feld `context: - research_task` von `analysis_task` weist CrewAI an, die vollständige Ausgabe von `research_task` in den Prompt des Analysten aufzunehmen. Das ist eine bewusste Entscheidung: der Analyst erhält *nur* das Recherche-Ergebnis, nicht die Zwischenschritte des Researchers wie Tool-Aufrufe oder Suchanfragen.
3. **Rollenbezogene Anweisungen** — die `backstory` jedes Agenten in `agents.yaml` prägt Ton/Verhalten, ohne dass Anweisungen in jeder Task-Beschreibung wiederholt werden müssen.

## Übung

1. In [config/tasks.yaml](../../src/research_crew/config/tasks.yaml) ist die Beschreibung von `analysis_task` lang und punktweise gegliedert (5 nummerierte Anforderungen). Schreibt sie vage um ("schreibe einen guten Report über {topic}") und führt die Crew erneut aus. Vergleicht Qualität/Struktur des Reports mit dem Original. Das zeigt, wie viel Context-Engineering-Arbeit in dieser Task-Beschreibung steckt, obwohl es "nur Text" ist.
2. `context: - research_task` gibt die *gesamte* Recherche-Ausgabe an den Analysten weiter. Wäre die Ausgabe von `research_task` riesig (z. B. 50 vollständig zusammengefasste Suchergebnisse), welches Problem würde das verursachen? Schlagt eine Lösung vor (ohne sie unbedingt umzusetzen) — z. B. den Researcher um eine knappere Zusammenfassung zu bitten, oder zu kürzen.
3. Stellt die ursprüngliche Task-Beschreibung wieder her.

## Zusatzaufgabe

CrewAI-Tasks unterstützen ein Feld `output_pydantic`, um strukturierte (schema-validierte) Ausgabe statt freien Text zu erzwingen. Definiert ein Pydantic-Modell für die Recherche-Ausgabe (z. B. `key_findings: list[str]`, `sources: list[str]`) und wendet es auf `research_task` an. Ändert das Erzwingen von Struktur, was der Analyst über `context` erhält, und ändert sich dadurch der finale Report?
