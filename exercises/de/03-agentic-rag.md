# 03 — Agentisches RAG

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/03-agentic-rag.md)

RAG (Retrieval-Augmented Generation) gibt einem Agenten Zugriff auf bestimmte Dokumente/Daten, mit denen er nicht trainiert wurde: der Inhalt wird in Chunks zerlegt, jeder Chunk in einen Vektor eingebettet, die Vektoren gespeichert, und die relevantesten Chunks für eine gegebene Anfrage abgerufen, um sie in den Kontext des LLM einzuspeisen. "Agentisches RAG" bedeutet, dass der Agent selbst entscheidet, wann Retrieval nötig ist, statt dass es bei jedem Aufruf bedingungslos passiert. Der Teil, über den Leute stolpern: **Embeddings sind ein separates Modell vom Chat-LLM** — man kann Gemini für den Chat und einen völlig anderen Anbieter für Embeddings nutzen, oder versehentlich auf einen Anbieter zurückfallen, den man nie konfiguriert hat.

RAG wurde eingeführt, um ein vortrainiertes parametrisches LLM mit einem nicht-parametrischen Retriever über einen externen Index zu kombinieren, statt sich rein auf das zu verlassen, was in den Gewichten des Modells steckt:

> Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 2020, 9459–9474. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

![RAG-Architektur: ein Query-Encoder und Retriever (nicht-parametrisch) speisen die Top-k-Dokumente in einen Generator (parametrisch), der über sie marginalisiert, um die finale Antwort zu erzeugen](../assets/rag-lewis2020-fig1.png)
*Abbildung 1 aus Lewis et al. (2020): ein Query Encoder + Retriever speist Dokumente in einen Generator, der seine Vorhersage über sie marginalisiert. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

Die Aufgabe unten baut das CrewAI-Äquivalent dieses Diagramms: `TextFileKnowledgeSource` ist der Retriever/Dokumentenindex, und das LLM des `analyst`-Agenten ist der Generator, in den die abgerufenen Chunks eingespeist werden.

## In diesem Repo

[crew.py:48-60](../../src/research_crew/crew.py#L48-L60) konfiguriert bereits den Embedder, nutzt ihn aber noch nicht:

```python
return Crew(
    agents=self.agents,
    tasks=self.tasks,
    process=Process.sequential,
    verbose=True,
    embedder={
        "provider": "google-generativeai",
        "config": {
            "api_key": os.getenv("GEMINI_API_KEY"),
            "model_name": "gemini-embedding-001",
        },
    },
)
```

Warum das existiert: CrewAIs Knowledge-/RAG-Funktionen nutzen standardmäßig **OpenAI-Embeddings**, unabhängig davon, welches LLM für den Chat konfiguriert ist. Ohne diesen `embedder`-Block würde das Hinzufügen jeder Knowledge-Quelle mit einem fehlenden `OPENAI_API_KEY`-Fehler scheitern — obwohl diese Crew sonst nirgends OpenAI verwendet. Seht in der [Tool-Kategorientabelle](../../README.md#adding-more-tools-or-rag-for-students) des READMEs nach, welche fertigen Tools in dieselbe Falle laufen.

Außerdem liegt bereits eine ungenutzte Datei unter [knowledge/user_preference.txt](../../knowledge/user_preference.txt) — das ist CrewAIs Konvention dafür, wo Knowledge-Quelldateien liegen.

**Fertiger Code zur Wiederverwendung:** [src/research_crew/knowledge_source_example.py](../../src/research_crew/knowledge_source_example.py) ist eine funktionierende, noch nicht eingebundene Vorlage — eine `build_knowledge_sources()`-Funktion, die bereits eine `TextFileKnowledgeSource` zurückgibt, die auf `user_preference.txt` zeigt. Übernehmt sie direkt, oder schreibt die gleichen Zeilen zuerst selbst, um sicherzugehen, dass ihr sie versteht (Schritt 1 unten).

## Aufgabe

Das ist die zentrale praktische Übung der Reihe — echtes RAG verkabeln:

1. Schreibt entweder Import und Quelle selbst:
   ```python
   from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

   preference_knowledge = TextFileKnowledgeSource(file_paths=["user_preference.txt"])
   ```
   oder importiert stattdessen die fertige Hilfsfunktion:
   ```python
   from research_crew.knowledge_source_example import build_knowledge_sources
   ```
2. Übergebt sie an den `Crew`-Konstruktor: `knowledge_sources=[preference_knowledge]` (oder `knowledge_sources=build_knowledge_sources()`, falls ihr die Hilfsfunktion genutzt habt).
3. Fügt einen Task hinzu (oder ändert einen bestehenden), der eine Frage stellt, die nur aus `user_preference.txt` beantwortbar ist (z. B. "Wie heißt der Nutzer und wo ist er ansässig?"). Prüft, dass der Agent korrekt mit abgerufenem Wissen antwortet, nicht mit einer Vermutung.
4. Probiert es mit entfernter Knowledge-Quelle — halluziniert der Agent eine Antwort, verweigert er, oder sagt er, dass er es nicht weiß? Das ist der eigentliche Sinn von RAG: Antworten in realen Daten zu verankern statt in Vermutungen.

## Zusatzaufgabe

Fügt eine zweite Knowledge-Quelle eines anderen Typs hinzu (`StringKnowledgeSource` für eingebetteten Text, oder `PDFKnowledgeSource` für ein eigenes PDF) und prüft, dass beide Quellen abrufbar sind. Falls ihr `knowledge_source_example.py` nutzt, fügt die zweite Quelle einfach als weiteren Eintrag in der von `build_knowledge_sources()` zurückgegebenen Liste hinzu.

---

**Team-Aufgabe:** Diese Übung schaltet [**Meilenstein M2: RAG**](assignment-milestones.md#m2-rag-zwischenabgabe) der [Team-Aufgabe](assignment-overview.md) frei — eure **Zwischenabgabe** ist am Ende dieses Meilensteins fällig.
