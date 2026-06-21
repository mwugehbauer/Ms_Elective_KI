# 07 — Planning-Pattern

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/07-planning-pattern.md)

## Konzept

Statt dass ein Agent Schritt für Schritt improvisiert, erstellt ein **Planner** zunächst einen expliziten Plan — eine Schrittfolge — bevor irgendein Task ausgeführt wird. Das tauscht etwas Latenz/Kosten im Voraus gegen vorhersagbarere, überprüfbare Ausführung: man kann den Plan lesen und einen schlechten Ansatz erkennen, bevor der Agent Tool-Aufrufe und Tokens dafür verbraucht.

## Originalarbeit

Planning-als-Prompting wurde als deliberative Suche über mehrere Reasoning-Pfade formalisiert — statt sich auf eine einzige links-nach-rechts-Gedankenkette festzulegen — in:

> Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., & Narasimhan, K. (2023). *Tree of Thoughts: Deliberate Problem Solving with Large Language Models*. [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)

![Vergleich von Input-Output-Prompting, Chain-of-Thought, Self-Consistency mit CoT und Tree of Thoughts, das einen Baum von Zwischen-"Gedanken" erkundet und zurückverfolgt](../assets/tot-yao2023-fig1.png)
*Abbildung 1 aus Yao et al. (2023) — Vergleich von (a) Standard-Input-Output-Prompting, (b) Chain-of-Thought, (c) Self-Consistency mit CoT (Mehrheitsentscheid über mehrere Ketten) und (d) Tree of Thoughts, das einen Baum von Zwischen-"Gedanken" erkundet und zurückverfolgen kann, bevor es sich auf eine Ausgabe festlegt. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

CrewAIs `planning=True` baut keinen vollständigen Suchbaum wie ToT — es ist näher an (b), ein einziger im Voraus erstellter Plan — aber es löst dasselbe zugrundeliegende Problem: sich nicht auf den ersten Reasoning-Pfad festlegen, den das LLM produziert, ohne ihm die Chance zu geben, zuerst die Struktur der Aufgabe zu berücksichtigen.

## In diesem Repo

CrewAI baut das auf `Crew`-Ebene über zwei Felder ein (`crew.py` nutzt sie noch nicht):

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True,
    planning=True,
    planning_llm="gemini/gemini-2.5-flash",
)
```

Wenn `planning=True` gesetzt ist, führt CrewAI vor Beginn der Ausführung einen internen `AgentPlanner` aus (mit `planning_llm`), der jedem Task-Kontext einen Plan hinzufügt.

## Übung

1. Fügt `planning=True` und `planning_llm="gemini/gemini-2.5-flash"` der `Crew` in [crew.py](../../src/research_crew/crew.py) hinzu.
2. Führt die Crew mit ausführlicher Ausgabe erneut aus und findet den Planning-Schritt in den Logs — er passiert, bevor `research_task` startet. Lest den generierten Plan.
3. Vergleicht zwei Läufe zum selben Thema, einen mit `planning=True` und einen ohne. Verändert der Plan sichtbar *was* der Researcher sucht, oder fügt er nur Overhead ohne Verhaltensänderung hinzu? Schreibt eure Beobachtung auf — es gibt keine einzig richtige Antwort, es geht darum, wirklich hinzusehen.

## Zusatzaufgabe

Planning kostet einen zusätzlichen LLM-Aufruf, bevor überhaupt ein Task läuft. Lohnt sich dieser Overhead für eine Crew mit nur zwei Tasks wie dieser? Argumentiert beide Seiten in ein paar Sätzen, und überlegt dann, ab wann eine Crew genug Tasks/Agenten hat, damit sich Planning erkennbar auszahlt (Tipp: denkt an die Multi-Agenten-Crews aus Lektion 08).
