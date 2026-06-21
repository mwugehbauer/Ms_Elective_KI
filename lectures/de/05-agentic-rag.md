# 05 — Agentisches RAG

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/05-agentic-rag.md)

## Konzept

RAG (Retrieval-Augmented Generation) gibt einem Agenten Zugriff auf bestimmte Dokumente/Daten, mit denen er nicht trainiert wurde, indem: der Inhalt in Chunks zerlegt wird, jeder Chunk in einen Vektor eingebettet (embedded) wird, die Vektoren in einer Vektordatenbank gespeichert werden, und die relevantesten Chunks für eine gegebene Anfrage abgerufen werden, um sie in den Kontext des LLM einzuspeisen. "Agentisches RAG" bedeutet, dass der Agent selbst entscheidet, wann Retrieval nötig ist, statt dass Retrieval bei jedem einzelnen Aufruf bedingungslos passiert.

Der Teil, über den Leute stolpern: **Embeddings sind ein separates Modell vom Chat-LLM**. Man kann Gemini für den Chat und einen völlig anderen Anbieter für Embeddings nutzen — oder versehentlich auf einen Anbieter zurückfallen, den man nie konfiguriert hat.

## Originalarbeit

RAG wurde eingeführt, um ein vortrainiertes parametrisches LLM mit einem nicht-parametrischen Retriever über einen externen Index zu kombinieren, statt sich rein auf das zu verlassen, was in den Gewichten des Modells steckt:

> Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems 33 (NeurIPS 2020), 9459–9474. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

![RAG-Architektur: ein Query-Encoder und Retriever (nicht-parametrisch) speisen die Top-k-Dokumente in einen Generator (parametrisch), der über sie marginalisiert, um die finale Antwort zu erzeugen](../assets/rag-lewis2020-fig1.png)
*Abbildung 1 aus Lewis et al. (2020) — die RAG-Architektur: ein Query Encoder + Retriever (nicht-parametrisch, der Dokumentenindex) speist abgerufene Dokumente in einen Generator (parametrisch, das seq2seq-Modell), der seine Vorhersage über sie marginalisiert. Aus dem Paper für die Bildungsnutzung in diesem Kurs wiedergegeben.*

Die Übung unten baut das CrewAI-Äquivalent dieses Diagramms: `TextFileKnowledgeSource` ist der Retriever/Dokumentenindex, und das LLM des `analyst`-Agenten ist der Generator, in den die abgerufenen Chunks eingespeist werden.

## In diesem Repo

[crew.py:48-59](../../src/research_crew/crew.py#L48-L59) konfiguriert bereits den Embedder, nutzt ihn aber noch nicht:

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

## Übung

Das ist die zentrale praktische Übung der Reihe — echtes RAG verkabeln:

1. Importiert `TextFileKnowledgeSource`:
   ```python
   from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
   ```
2. Erstellt eine Quelle, die auf die vorhandene Datei zeigt (Pfade sind relativ zu `knowledge/`):
   ```python
   preference_knowledge = TextFileKnowledgeSource(file_paths=["user_preference.txt"])
   ```
3. Übergebt sie an den `Crew`-Konstruktor: `knowledge_sources=[preference_knowledge]`.
4. Fügt einen Task hinzu (oder ändert einen bestehenden), der eine Frage stellt, die nur aus `user_preference.txt` beantwortbar ist (z. B. "Wie heißt der Nutzer und wo ist er ansässig?"). Prüft, dass der Agent korrekt mit abgerufenem Wissen antwortet, nicht mit einer Vermutung.
5. Probiert es mit entfernter Knowledge-Quelle — halluziniert der Agent eine Antwort, verweigert er, oder sagt er, dass er es nicht weiß? Das ist der eigentliche Sinn von RAG: Antworten in realen Daten zu verankern statt in Vermutungen.

## Zusatzaufgabe

Fügt eine zweite Knowledge-Quelle eines anderen Typs hinzu (`StringKnowledgeSource` für eingebetteten Text, oder `PDFKnowledgeSource` für ein eigenes PDF) und prüft, dass beide Quellen abrufbar sind.
