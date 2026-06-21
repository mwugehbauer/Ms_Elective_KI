# 03 — Agentische Design-Patterns

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/03-agentic-design-patterns.md)

## Konzept

"Design-Pattern" bedeutet hier eine wiederkehrende Form, wie Agenten orchestriert werden, unabhängig vom verwendeten Framework. Das Pattern, das dieses Repo zeigt, ist die **sequentielle Pipeline**: Agent A schließt seine Arbeit vollständig ab und gibt sein Ergebnis dann an Agent B weiter. Andere verbreitete Patterns (mehr dazu in späteren Lektionen): hierarchisch/Manager-Worker, Planner-Executor und Reflexions-/Kritik-Schleifen.

Das sequentielle Pattern ist die richtige Standardwahl, wenn Schritte wirklich in einer festen Reihenfolge voneinander abhängen — man kann keine Recherche analysieren, die noch nicht existiert.

## Originalquellen

Das Vokabular dieser Reihe für Design-Patterns (sequentielle Pipeline, hierarchisch/Manager-Worker, Planner-Executor, Reflexions-Schleifen — behandelt über die Lektionen 03, 07, 08, 09) folgt dem Katalog aus:

> Lakshmanan, V. (2025). *Generative AI Design Patterns: Solutions to Common Challenges When Building GenAI Agents and Applications*. O'Reilly Media.

Die zugrundeliegenden Agenten-*Architekturen* (einfacher Reflexagent, modellbasierter Reflexagent, zielbasierter Agent, nutzenbasierter Agent, lernender Agent), auf denen diese Patterns aufbauen, stammen aus der klassischen Taxonomie in:

> Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4. Aufl.), Kapitel 2: Intelligent Agents. Pearson.

Hier keine Abbildung — beides sind Bücher, keine offen lizenzierten Papers, daher zitieren wir, statt ihre Diagramme zu reproduzieren. Falls ihr Zugang zu einem der beiden habt, schaut euch deren jeweilige Agenten-Architektur-Diagramme an und vergleicht sie mit der sequentiellen Pipeline unten.

## In diesem Repo

[crew.py:43-51](../../src/research_crew/crew.py#L43-L51):
```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True,
)
```

`Process.sequential` bedeutet: `research_task` vollständig ausführen (der `researcher`-Agent arbeitet allein), dann `analysis_task` ausführen (der `analyst`-Agent arbeitet allein, erhält aber das Recherche-Ergebnis über `context: - research_task` in [tasks.yaml](../../src/research_crew/config/tasks.yaml)).

Das ist die einfachstmögliche Multi-Agenten-Pipeline: zwei Agenten, keine Verhandlung, keine Verzweigung.

## Übung

1. Zeichnet (auf Papier oder als Markdown-Kommentar) den Datenfluss dieser Crew: was geht hinein, was erhält jeder Agent, was produziert jeder Agent, was ist das Endergebnis.
2. `Process` hat noch eine weitere Option: `Process.hierarchical` (die nutzen wir richtig in Lektion 08). Sucht sie für jetzt einfach im CrewAI-Quellcode (`crewai/process.py` in eurer `.venv`) und lest den Docstring. Schreibt einen Satz dazu, wie sie sich von sequential unterscheidet.
3. Findet eine reale Aufgabe (nicht Recherche/Reporting), die gut zum sequentiellen Pattern passt, und eine, die nicht passen würde (weil die Schritte keine strikte Reihenfolge haben).

## Zusatzaufgabe

Der sequentielle Prozess erzwingt die Task-Reihenfolge über die Listenreihenfolge in `self.tasks`. Versucht, `analysis_task` vor `research_task` im `tasks: List[Task]`-Mechanismus umzustellen (Tipp: die Task-Reihenfolge ergibt sich aus der Reihenfolge der Methodendefinitionen unter `@task`) und sagt voraus, was kaputtgeht, bevor ihr es ausführt.
