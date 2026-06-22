# Team Assignment — Design Your Own Crew

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-overview.md)

This is the graded assignment that runs alongside the lecture series: in teams, you design a CrewAI crew for a topic of your choice, growing it in complexity as the lectures introduce new capabilities. The primary deliverable at every stage is **your design plus your critical assessment of its risks and constraints** — working code is an optional bonus, never a requirement.

See [Assignment Milestones](assignment-milestones.md) for what to build at each stage, and [Assignment Templates](assignment-templates.md) for the documents you'll fill in.

## How this works: sprints tied to lectures

Treat each lecture as a sprint boundary. Each sprint unlocks one new capability (an "epic") for your crew design — you don't redesign from scratch each time, you extend what you already have.

| Lecture(s) | Unlocks | Milestone |
| --- | --- | --- |
| [02](02-agentic-frameworks.md)–[03](03-agentic-design-patterns.md) | Agents, tasks, sequential process | **M0: Baseline** |
| [04](04-tool-use.md) | Tool use | **M1: Tools** |
| [05](05-agentic-rag.md) | Knowledge sources / RAG | **M2: RAG** *(interim submission due here)* |
| [06](06-trustworthy-agents.md) + [08](08-multi-agent-pattern.md) | Guardrails, multi-agent/hierarchical process | **M3: Multi-agent and trust** |
| [10](10-production.md) + [14](14-securing-agents.md) | Production concerns, security threat modeling | **Final: Production and security** |

Two submissions: an **interim submission** at M2 (formative, lighter weight — catches weak foundations early) and a **final submission** after the last lecture (the full design plus a retrospective on how your thinking changed).

## Team setup: repos and accounts

**One GitHub repository per team — not one per student.** Use **"Use this template" → Create a new repository**, not "Fork": forking shares one network graph across every team and forces forks of a public repo to stay public, while a template-generated repo is fully independent and can be made private if you want other teams unable to see your design. (Ask your instructor to mark the course repo as a template repository if the button isn't there yet.)

**Every team member still needs their own GitHub account**, added as a collaborator on the team's repo. Two reasons: your individual commits are how contribution within the team gets assessed, and a real commit history under your own account is worth having beyond this course.

### Collaborating without git experience

You don't need branches or pull requests for day-to-day team work — one simple loop is enough:

1. Edit a file normally (in your Codespace).
2. Open the **Source Control** panel (the branching-lines icon in the sidebar).
3. Type a one-line commit message, click **✓ Commit**.
4. Click **Sync Changes** — this pulls any teammate's changes and pushes yours, in one step.

No terminal, no `git add`/`commit`/`push` commands. Everyone commits straight to `main`.

To avoid two people editing the same file at once, **divide files between teammates** where you can — e.g. one person owns `agents.yaml`, another `tasks.yaml`. `DESIGN.md` is one shared file everyone contributes to, so for that one specifically: take turns, or commit-and-sync every few minutes rather than both editing it for a long stretch in parallel. If a conflict does happen anyway, VS Code shows a merge view with clickable "Accept Current / Incoming / Both" buttons — ask your instructor for a quick live demo of this once, so it doesn't surprise anyone mid-deadline.

For quick edits (e.g. a `RISK_LOG.md` entry), you can skip Codespaces entirely: open the file on github.com, click the pencil icon, edit in the browser, and click **"Commit changes"** at the bottom.

## Submission package

At each milestone deadline, your submission is the state of your team repo's `main` branch:

| Artifact | Where | What it shows |
| --- | --- | --- |
| Executable crew config | `src/research_crew/config/agents.yaml` + `tasks.yaml` (+ `crew.py` once tools/RAG/process change) | The literal, runnable version of your design |
| Design document | `DESIGN.md` — architecture (agents/tasks/tools/RAG), risks, constraints, security, production considerations, design history | Your full design rationale, critically assessed, in one evolving report |
| Backlog | GitHub Issues (labeled by epic) + a Projects board | Your user stories and progress — lives on GitHub, nothing to export |
| Team notes | `TEAM.md` | Members and who contributed what |
| Optional bonus | a working `crew.py` + a successful `uv run research_crew` | Extra credit only — never required |

Submission is simply **the state of your team repo's `main` branch at the deadline** — there's no pull request to open. Share your repo URL once, at the start; your instructor checks your commit history against each deadline on that same repo (and may tag a specific commit for grading).

## Grading

The design documents (`agents.yaml`/`tasks.yaml` + `DESIGN.md` + backlog) carry the large majority of the grade. Working code is bonus points on top, never a substitute for a thin or missing risk analysis. See [Assignment Milestones](assignment-milestones.md) for the specific risk-analysis prompts graded at each stage.

## Agile practice: backlog and user stories

Run your design process like a real product backlog:
- Each milestone's new capability is an **epic**. Break it into 2–4 **user stories**: *"As a [stakeholder of the crew's output], I want [capability], so that [value]."*
- Write **acceptance criteria** for each story as testable conditions — these double as a draft of the task's `expected_output` field once you get to the YAML, which is a useful thing to notice in itself.
- Add "risks identified and mitigation documented" to every epic's definition of done, so risk analysis is a habit, not a one-off essay.
- If your team is larger than two, rotate a facilitator role each sprint.

Templates for all of this are in [Assignment Templates](assignment-templates.md).

## For instructors

To enable the template-repo workflow: **Settings → check "Template repository"** on the main course repo. For a closer GitHub-Classroom-like experience (Classroom itself stopped taking new sign-ups in May 2026), consider a GitHub Organization for the course with one Team per group — each team's repo and Issues are then visible to you in one place. Review submissions by checking each team's commit history on `main` at each deadline — tag a specific commit yourself (Releases → "Create a new release") if you want an immutable snapshot for grading. Solutions aren't included on purpose, the same as the rest of this series.
