# 05 — Agentic RAG

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/05-agentic-rag.md)

## Concept

RAG (Retrieval-Augmented Generation) gives an agent access to specific documents/data it wasn't trained on, by: chunking the content, embedding each chunk into a vector, storing vectors in a vector DB, and retrieving the most relevant chunks for a given query to feed into the LLM's context. "Agentic RAG" means the agent itself decides when retrieval is needed, rather than retrieval happening on every single call unconditionally.

The part that trips people up: **embeddings are a separate model from the chat LLM**. You can use Gemini for chat and a totally different provider for embeddings — or accidentally default to a provider you never configured.

## Original paper

RAG was introduced as a way to combine a pretrained parametric LLM with a non-parametric retriever over an external index, instead of relying purely on what's baked into the model's weights:

> Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems 33 (NeurIPS 2020), 9459–9474. [arXiv:2005.11401](https://arxiv.org/abs/2005.11401)

![RAG architecture: a query encoder and retriever (non-parametric) feed top-k documents into a generator (parametric), which marginalizes over them to produce the final answer](../assets/rag-lewis2020-fig1.png)
*Figure 1 from Lewis et al. (2020) — the RAG architecture: a Query Encoder + Retriever (non-parametric, the document index) feeds retrieved documents into a Generator (parametric, the seq2seq model), which marginalizes its prediction over them. Reproduced from the paper for educational use in this course.*

The exercise below builds the CrewAI equivalent of this diagram: `TextFileKnowledgeSource` is the retriever/document index, and the `analyst` agent's LLM is the generator that the retrieved chunks get fed into.

## In this repo

[crew.py:48-59](../../src/research_crew/crew.py#L48-L59) already configures the embedder, but doesn't use it yet:

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

Why this exists: CrewAI's knowledge/RAG features default to **OpenAI embeddings** regardless of which LLM you configured for chat. Without this `embedder` block, adding any knowledge source would fail with a missing `OPENAI_API_KEY` error — even though this crew never uses OpenAI for anything else. See the README's [tool category table](../../README.md#adding-more-tools-or-rag-for-students) for which pre-built tools hit this same trap.

There's also an unused file sitting in [knowledge/user_preference.txt](../../knowledge/user_preference.txt) — CrewAI's convention for where knowledge source files live.

## Exercise

This is the main hands-on exercise of the series — wire up real RAG:

1. Import `TextFileKnowledgeSource`:
   ```python
   from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
   ```
2. Create a source pointing at the existing file (paths are relative to `knowledge/`):
   ```python
   preference_knowledge = TextFileKnowledgeSource(file_paths=["user_preference.txt"])
   ```
3. Pass it into the `Crew` constructor: `knowledge_sources=[preference_knowledge]`.
4. Add a task (or modify an existing one) that asks a question only answerable from `user_preference.txt` (e.g. "what is the user's name and where are they based?"). Confirm the agent answers correctly using retrieved knowledge, not a guess.
5. Try it with the knowledge source removed — does the agent hallucinate an answer, refuse, or say it doesn't know? This is the actual point of RAG: grounding answers in real data instead of guesses.

## Stretch goal

Add a second knowledge source of a different type (`StringKnowledgeSource` for inline text, or `PDFKnowledgeSource` for a PDF you provide) and confirm both sources are retrievable.
