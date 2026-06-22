# 04 — Multi-Agenten-Pattern

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/04-multi-agent-pattern.md)

Über eine feste sequentielle Pipeline hinaus bietet CrewAI **hierarchische** Orchestrierung: ein Manager-Agent (oder Manager-LLM) entscheidet, welcher Worker-Agent welchen Task übernimmt und in welcher Reihenfolge, statt dass ihr die Sequenz hartcodiert. Das ist das eigentliche "Multi-Agenten"-Pattern — Agenten, deren Zusammenarbeit selbst dynamisch ist, nicht nur eine feste Leitung. Kompromiss: flexibler, aber weniger vorhersagbar und teurer (der Manager macht zusätzliche LLM-Aufrufe, um zu delegieren).

Die Idee mehrerer zusammenarbeitender LLM-Agenten über strukturierte Konversation — statt einer einzigen festen Pipeline — wurde popularisiert durch:

> Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., & Wang, C. (2023). *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*. [arXiv:2308.08155](https://arxiv.org/abs/2308.08155)

![AutoGen-Architektur: konversationsfähige, anpassbare Agenten, die zur Lösung von Aufgaben kommunizieren, in Joint-Chat- oder hierarchischen Chat-Mustern, gezeigt bei der Lösung einer Datenplot-Aufgabe durch Mehrturn-Konversation](../assets/autogen-wu2023-fig1.png)
*Abbildung 1 aus Wu et al. (2023): AutoGen-Agenten sind konversationsfähig und anpassbar, können in flexiblen Mustern einschließlich hierarchischem Chat kommunizieren und Menschen einbeziehen. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

CrewAIs hierarchischer Prozess mit einem `manager_llm` spielt die Rolle des "hierarchischen Chat"-Patterns: ein koordinierender Agent entscheidet, wer als Nächstes spricht/handelt, statt dass ihr die Reihenfolge selbst festlegt.

## In diesem Repo

Aktuell `process=Process.sequential` mit genau zwei Agenten in fester Reihenfolge ([crew.py:51](../../src/research_crew/crew.py#L51)). Um hierarchisch zu werden, braucht CrewAI entweder `manager_llm` oder `manager_agent`:

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.hierarchical,
    manager_llm="gemini/gemini-2.5-flash",
    verbose=True,
)
```

## Aufgabe

1. Fügt [crew.py](../../src/research_crew/crew.py) und [config/agents.yaml](../../src/research_crew/config/agents.yaml) einen dritten Agenten hinzu — einen `editor`, dessen Aufgabe es ist, den Report des Analysten auf Ton und Klarheit zu prüfen und zu verfeinern.
2. Fügt in [config/tasks.yaml](../../src/research_crew/config/tasks.yaml) einen entsprechenden `editing_task` mit `context: - analysis_task` hinzu.
3. Stellt `process` auf `Process.hierarchical` um und fügt `manager_llm` hinzu. Entfernt das Feld `agent:` aus jedem Task in `tasks.yaml` — im hierarchischen Modus weist der Manager Tasks dynamisch Agenten zu, statt eine feste Zuordnung zu lesen.
4. Führt es aus und beobachtet die ausführlichen Logs: welchen Agenten wählt der Manager für jeden Task, und entspricht das dem, was ihr von der Rolle jedes Agenten erwarten würdet?

## Zusatzaufgabe

Probiert `manager_agent` statt `manager_llm` — definiert euren eigenen dedizierten Manager-`Agent` mit einer Rolle wie "Editorial Director" und übergebt ihn stattdessen. Vergleicht, ob sich die Delegationsentscheidungen ändern.

---

**Team-Aufgabe:** Diese Übung schaltet [**Meilenstein M3: Multi-Agent**](assignment-milestones.md#m3-multi-agent) der [Team-Aufgabe](assignment-overview.md) frei.
