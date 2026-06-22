# ResearchCrew Crew

Welcome to the ResearchCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

**Teaching agentic AI?** See the [lecture series](lectures/README.md) (English / [Deutsch](lectures/de/README.md)) — 15 sessions covering agent concepts, tools, RAG, multi-agent patterns, production, and security, each with hands-on exercises grounded in this repo's actual code.

## Getting Started — choose one option

There are two independent ways to get this project running. Pick **one**:

- **Option A — GitHub Codespaces:** run entirely in the browser, nothing installed on your machine.
- **Option B — Run locally:** clone the repo and run it with Python/uv on your own computer.

Both options end up running the exact same code; only the setup step differs. Everything below "Run the crew" applies regardless of which option you picked.

### Option A: GitHub Codespaces (no local install)

No local install needed.

**If you want to edit and save your own changes** (e.g. for an assignment), fork this repo first, then open the Codespace from your fork: **Code → Create codespace on master** on *your fork's* page. You won't have push access if you open a Codespace directly on the original repo.

The container automatically installs `uv` and runs `uv sync`.

**Add your API keys via Codespaces secrets (recommended — do this before opening your first codespace):** go to [github.com/settings/codespaces](https://github.com/settings/codespaces) → Codespaces secrets → add `GROQ_API_KEY` and `SERPER_API_KEY`. They'll be available as environment variables automatically in every codespace you open, on this repo or your fork — no file to create or edit inside the codespace at all. (`GEMINI_API_KEY` is only needed if you do the RAG/memory lectures, which use Gemini for embeddings.)

<details>
<summary>Alternative: local <code>.env</code> file inside the codespace (only if you can't use Codespaces secrets)</summary>

Copy `.env.example` to `.env` inside the codespace and fill in your keys — **edit `.env`, not `.env.example`** (the latter is the committed template and stays empty; real keys belong only in `.env`, which is gitignored).
</details>

Once that's done, skip ahead to [Run the crew](#run-the-crew) below.

### Option B: Run locally

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Clone the repo, then from its root install the dependencies:

```bash
uv sync
```

Copy `.env.example` to `.env` and fill in your `GROQ_API_KEY` and `SERPER_API_KEY` (and `GEMINI_API_KEY` if you'll do the RAG/memory lectures, which use Gemini for embeddings).

Once that's done, continue with [Run the crew](#run-the-crew) below.

### Customizing

**Make sure your `.env` has the right API keys for whichever LLM/tools you use**

- Modify `src/research_crew/config/agents.yaml` to define your agents
- Modify `src/research_crew/config/tasks.yaml` to define your tasks
- Modify `src/research_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/research_crew/main.py` to add custom inputs for your agents and tasks

## Run the crew

This applies whether you set up via Codespaces or locally. From the project root:

```bash
uv run research_crew
```

This initializes the research_crew Crew, assembling the agents and assigning them tasks as defined in your configuration, and saves the report to `output/report.md`.

## Live demo UI (Streamlit)

For a lecture-friendly view of the agents working, run the Streamlit app instead of the plain CLI. It shows each agent/task/tool event live in the browser, then renders the final report.

```bash
uv run streamlit run streamlit_app.py
```

Locally this opens at `http://localhost:8501`. In a Codespace, port `8501` is auto-forwarded and a preview tab opens automatically (configured in `.devcontainer/devcontainer.json`).

## Understanding Your Crew

The research_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Adding more tools or RAG (for students)

`crewai_tools` ships ~90 built-in tools beyond `SerperDevTool`. The setup that matters most is whether a tool calls an external API directly (just needs a key) or does **local embedding-based search** (needs an embedder pointed at Gemini, same as below) — that split is called out per category.

| Category | Needs embedder config? | Tools |
| --- | --- | --- |
| Web search | No — just an API key | `SerperDevTool`, `TavilySearchTool`, `BraveSearchTool`, `EXASearchTool`, `SerpApiGoogleSearchTool`, `SerpApiGoogleShoppingTool`, `SerplyWebSearchTool`, `SerplyNewsSearchTool`, `SerplyJobSearchTool`, `SerplyScholarSearchTool`, `LinkupSearchTool`, `ParallelSearchTool`, `ArxivPaperTool`, `FirecrawlSearchTool` |
| Web scraping & browser automation | No — just an API key | `ScrapeWebsiteTool`, `ScrapeElementFromWebsiteTool`, `SerperScrapeWebsiteTool`, `SerplyWebpageToMarkdownTool`, `FirecrawlScrapeWebsiteTool`, `FirecrawlCrawlWebsiteTool`, `JinaScrapeWebsiteTool`, `ScrapflyScrapeWebsiteTool`, `ScrapegraphScrapeTool`, `SeleniumScrapingTool`, `SpiderTool`, `BrowserbaseLoadTool`, `HyperbrowserLoadTool`, `StagehandTool`, `MultiOnTool`, `TavilyExtractorTool`, `BrightDataSearchTool`, `BrightDataWebUnlockerTool`, `BrightDataDatasetTool`, `OxylabsAmazonProductScraperTool`, `OxylabsAmazonSearchScraperTool`, `OxylabsGoogleSearchScraperTool`, `OxylabsUniversalScraperTool` |
| Local RAG / semantic content search | **Yes** — defaults to OpenAI embeddings | `RagTool` (base class), `WebsiteSearchTool`, `PDFSearchTool`, `CSVSearchTool`, `DOCXSearchTool`, `JSONSearchTool`, `MDXSearchTool`, `TXTSearchTool`, `XMLSearchTool`, `CodeDocsSearchTool`, `GithubSearchTool`, `YoutubeVideoSearchTool`, `YoutubeChannelSearchTool`, `DirectorySearchTool` |
| Vector database connectors | Bring your own embeddings/index | `QdrantVectorSearchTool`, `WeaviateVectorSearchTool`, `MongoDBVectorSearchTool`, `CouchbaseFTSVectorSearchTool` |
| Databases & structured data | No | `MySQLSearchTool`, `SnowflakeSearchTool`, `SingleStoreSearchTool`, `DatabricksQueryTool`, `NL2SQLTool` |
| File & storage I/O | No | `FileReadTool`, `FileWriterTool`, `FileCompressorTool`, `DirectoryReadTool`, `S3ReaderTool`, `S3WriterTool` |
| Code execution | No | `CodeInterpreterTool` |
| Vision, image & OCR | No | `DallETool`, `VisionTool`, `OCRTool` |
| Evaluation & quality | No | `PatronusEvalTool`, `PatronusLocalEvaluatorTool`, `PatronusPredefinedCriteriaEvalTool` |
| Platform & automation integrations | Varies by platform | `ZapierActionTool`, `ComposioTool`, `ApifyActorsTool`, `EnterpriseActionTool`, `MergeAgentHandlerTool`, `GenerateCrewaiAutomationTool`, `InvokeCrewAIAutomationTool`, `BedrockInvokeAgentTool`, `BedrockKBRetrieverTool`, `AIMindTool`, `LlamaIndexTool`, `ContextualAICreateAgentTool`, `ContextualAIParseTool`, `ContextualAIQueryTool`, `ContextualAIRerankTool` |

For any tool marked "Needs embedder config", point it at Gemini the same way (otherwise it fails with a missing `OPENAI_API_KEY` error, even though the crew's chat LLM is Gemini):

```python
WebsiteSearchTool(config={
    "embedding_model": {
        "provider": "google-generativeai",
        "config": {"api_key": os.getenv("GEMINI_API_KEY"), "model_name": "gemini-embedding-001"},
    },
})
```

This crew's `embedder` (see `crew.py`) is already configured the same way at the `Crew` level, so adding a `knowledge_sources=[...]` list there (e.g. a `TextFileKnowledgeSource` pointing at `knowledge/user_preference.txt`) will embed via Gemini automatically — that wiring is left as an exercise.

## Support

For support, questions, or feedback regarding the ResearchCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
