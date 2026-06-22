# Assignment Milestones — The Crew Design Ladder

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-milestones.md)

Pick a use case for your crew before M0 — anything a two-agent pipeline could plausibly tackle (a market, a technology, a policy question, a historical case). You'll keep the same use case through every milestone.

All ten ideas below reuse the same CrewAI mechanics already in this repo (`Agent`/`Task`/`Crew`/`Process`, a sequential pipeline, the same `agents.yaml`/`tasks.yaml` files) — so you're never rewriting code from scratch. What changes is the content: at M0, you design your own agent roles, goals, and backstories suited to the use case, and a task flow to match — **not** the starter repo's `researcher`/`analyst` relabeled with a new topic. The role-split suggestions below are a starting point, not a spec — push back on them if a different split fits your topic better. What differs between use cases is how naturally each one extends into M1 (tools) and M2 (RAG):

| # | Use case | Example topic & suggested role split | Natural M1 tool | Natural M2 RAG source |
| --- | --- | --- | --- | --- |
| 1 | Competitive landscape analysis | "Competitive landscape for [industry]"<br>*Market Scout → Positioning Strategist* | Keep `SerperDevTool`, or add `ScrapeWebsiteTool` for competitor pages | Team's own market-positioning brief (PDF) |
| 2 | Regulatory impact briefing | "EU AI Act impact on SaaS startups"<br>*Policy Tracker → Compliance Strategist* | Web search for recent updates | The actual regulation text itself — a great large-document RAG case |
| 3 | Academic literature review | "Recent advances in [CS/AI subtopic]"<br>*Literature Scout → Synthesis Writer* | `ArxivPaperTool` (already in the README's tool table, no new signup) | One seminal paper's PDF for deep Q&A |
| 4 | Job market & skills trend report | "In-demand skills for [tech field] in 2026"<br>*Labor Market Researcher → Workforce Strategist* | Web search, or `SerplyJobSearchTool` | A curriculum/skills-framework doc |
| 5 | Startup due-diligence memo | "Due diligence on [hypothetical startup]"<br>*Diligence Researcher → Investment Analyst* | Web search | The startup's own pitch deck (PDF) |
| 6 | Personalized travel planner | "Travel plan for [destination]"<br>*Destination Scout → Itinerary Planner* | Web search | Reuse `knowledge/user_preference.txt` as-is, repurposed for travel preferences — the lowest-friction RAG onramp of the whole list |
| 7 | Product sentiment synthesis | "Customer sentiment on [product category]"<br>*Voice-of-Customer Researcher → Product Strategist* | Web search / scraping tool | The product's own FAQ/support docs |
| 8 | ESG/sustainability risk briefing | "ESG risks for [company/sector]"<br>*ESG Researcher → Risk Assessor* | Web search | The company's own sustainability report (PDF) |
| 9 | Personal finance topic explainer | "ETFs vs. individual stocks for beginners"<br>*Finance Researcher → Plain-Language Educator* | Web search | A fund prospectus or glossary doc |
| 10 | News digest on an ongoing story | "Weekly digest on [ongoing news topic]"<br>*News Tracker → Digest Editor* | Web search / `SerplyNewsSearchTool` | A backgrounder doc giving context predating the news window |

## M0: Baseline

**Unlocked by:** exercise 01

**Add:** two agents *you design* — your own roles, goals, and backstories suited to your use case (the table's role-split suggestions are a starting point, not a requirement) — **not** the starter repo's `researcher`/`analyst` relabeled with a new topic. Keep the same mechanics: a sequential process, no tools beyond what's already wired in the starter repo.

**Update:** `agents.yaml`, `tasks.yaml`, and `DESIGN.md` (Overview + Architecture: Process, Agents, Tasks). Same files as the starter repo — you're changing their content, not the surrounding code in `crew.py`.

**Risk & constraint prompts** (answer in `DESIGN.md`'s Risks/Constraints tables):
- Why this specific role split, and why does it fit your use case better than the table's suggestion (or better than the starter repo's `researcher`/`analyst` split)? What does each agent need from the other to do its job?
- What happens if one agent's output is subtly wrong — does the next agent have any way to notice, or does it trust it blindly?

**Suggested user story starter:** *"As a [stakeholder reading the final output], I want the second agent's conclusions to be traceable back to the first agent's findings, so that I can judge whether the conclusion is actually supported."*

## M1: Tools

**Unlocked by:** exercise 02

**Add:** one or two tools from `crewai_tools` (see the [README's tool table](../../README.md#adding-more-tools-or-rag-for-students)), chosen because your topic actually needs them — not just to check a box.

**Update:** `agents.yaml` (tools list), tool API key in `.env`, and `DESIGN.md` (Architecture: Tools table).

**Risk & constraint prompts** (answer in `DESIGN.md`'s Risks/Constraints tables):
- What happens if the tool is rate-limited, returns nothing useful, or the API is down mid-run? Does your crew degrade gracefully or just fail?
- Does the tool's description make misuse likely (e.g. the agent calling it with bad arguments, or not calling it when it should)?

**Suggested user story starter:** *"As a [stakeholder], I want the agent gathering information to pull current information rather than relying on the LLM's training data, so that the output reflects up-to-date facts."*

## M2: RAG (interim submission)

**Unlocked by:** exercise 03

**Add:** a knowledge source (`TextFileKnowledgeSource`, `StringKnowledgeSource`, or `PDFKnowledgeSource`) relevant to your topic, using the Gemini embedder already configured in `crew.py`.

**Update:** `crew.py` (`knowledge_sources=[...]`), a new file under `knowledge/`, and `DESIGN.md` (Architecture: Knowledge sources/RAG table).

**Risk & constraint prompts** (answer in `DESIGN.md`'s Risks/Constraints tables):
- What's missing or stale in your knowledge source, and what does the agent do when retrieval returns nothing relevant — guess, refuse, or say it doesn't know?
- Embeddings have their own rate limits, separate from the chat LLM's. If a classmate uploaded a 100-page document instead of your few pages, would your design still work, or would it need pacing/retries?

**Suggested user story starter:** *"As a [stakeholder], I want answers grounded in [your specific source], so that the agent doesn't fabricate facts it was never given."*

**→ Interim submission is due at the end of this milestone.** Submit: `agents.yaml`, `tasks.yaml`, `DESIGN.md` (sections 1–4 complete, with M0–M2 rows in the Risks/Constraints/Design-history tables), and your backlog (Issues + Project board) as they stand.

## M3: Multi-agent

**Unlocked by:** exercise 04

**Add:** a third agent and a decision between `Process.sequential` and `Process.hierarchical` (justify it). Optional stretch: a `guardrail` on at least one task — not covered in a dedicated exercise this term, but quick to look up in CrewAI's docs (`Task(guardrail=fn)`).

**Update:** `crew.py`, `agents.yaml`, `tasks.yaml`, and `DESIGN.md` (Architecture: updated Process/Agents, Guardrails/trust mechanisms if you added one).

**Risk & constraint prompts** (answer in `DESIGN.md`'s Risks/Constraints tables):
- If you went hierarchical: what is the manager actually optimizing for when it delegates, and could that diverge from what you want? If you stayed sequential: what would hierarchical have bought you, and why wasn't it worth the cost?
- What does the third agent add that the first two couldn't already do between them — is its role truly necessary, or just splitting work that didn't need splitting?

**Suggested user story starter:** *"As a [stakeholder], I want a check before the final report ships, so that an obviously broken or off-topic output never reaches me."*

## Final: Production and security

**Unlocked by:** exercises 05 + 06

**Add:** a short production plan (what you'd monitor, what would alert you to failure) and a threat model (what's the realistic prompt-injection or secret-leak risk for your specific topic and tools).

**Update:** `DESIGN.md` (Security & threat model, Production considerations) — no required code changes, this milestone is about the write-up.

**Risk & constraint prompts** (answer in `DESIGN.md`'s Risks/Constraints tables):
- If this crew ran unattended for a semester on your topic, what's the first thing that breaks, and how would you know?
- Given the actual tools/knowledge sources your crew uses, construct one concrete (hypothetical, not executed) prompt-injection scenario specific to your design — not the generic one from exercise 06.

**Final submission:** everything above, plus a final **Design history** entry in `DESIGN.md` answering: *what changed between your interim and final design, and what did you learn that made you change it?* That question is worth more than it looks — it's the one place you have to show your reasoning evolved, not just accumulated.
