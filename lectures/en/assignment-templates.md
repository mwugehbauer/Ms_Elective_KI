# Assignment Templates

🇬🇧 **English** (this page) · 🇩🇪 [Deutsch](../de/assignment-templates.md)

Copy these into your team repo and fill them in. See [Assignment Overview](assignment-overview.md) for how they're used and [Assignment Milestones](assignment-milestones.md) for what to write at each stage.

## `DESIGN.md`

This is the main report: a structured design document for your crew's architecture, covering what you built, why, and what could go wrong. Fill in each section as the relevant milestone unlocks it — mark later sections "not yet" rather than deleting them. For the **Risks**, **Constraints**, and **Design history** tables specifically: this is append-only — add new rows per milestone, never edit or delete a previous row. If a later milestone changes your assessment, add a new row noting the update instead.

```markdown
# Crew Design Document

**Team:** [team name] · **Topic:** [your crew's topic] · **Last updated:** [milestone, YYYY-MM-DD]

## 1. Overview
- **Problem / goal:** what is this crew for, in one or two sentences?
- **Stakeholders:** who reads the output, and what do they need from it?

## 2. Architecture

**Process:** `Process.sequential` or `Process.hierarchical` — and why this one, not the other.

### Agents
| Agent | Role | Goal | Owns which task(s) |
| --- | --- | --- | --- |
| | | | |

### Tasks
| Task | Description (summary) | Expected output | Agent | Depends on (`context`) |
| --- | --- | --- | --- | --- |
| | | | | |

### Tools
| Tool | Purpose | Why this tool for this topic | Needs API key / embeddings? | What happens if it fails |
| --- | --- | --- | --- | --- |
| | | | | |

### Knowledge sources / RAG
*(leave as "not yet added" until M2)*

| Source | Type | Why this content | Embedder | Known gaps (what's NOT covered) |
| --- | --- | --- | --- | --- |
| | | | | |

### Guardrails / trust mechanisms
*(leave as "none yet" until M3)*
-

## 3. Risks
*(append-only — add new rows per milestone, never edit old ones)*

| # | Milestone | Risk | Where it lives (agent/task/tool/RAG) | Mitigation or accepted tradeoff |
| --- | --- | --- | --- | --- |
| | | | | |

## 4. Constraints
*(append-only — add new rows per milestone, never edit old ones)*

| # | Milestone | Constraint | Type (rate limit / cost / latency / data / time / team) | How the design accounts for it |
| --- | --- | --- | --- | --- |
| | | | | |

## 5. Security & threat model
*(fill in from M3, complete by Final)*
- Concrete prompt-injection scenario specific to this design:
- Secrets handling:
- Tool permission scope:

## 6. Production considerations
*(fill in at Final)*
- What you'd monitor:
- What would alert you to failure:
- What's still missing for real production use:

## 7. Alternatives considered
- What other design did you consider (a different process, a different tool, no RAG, a different role split) and why did you reject it?

## 8. Design history
*(append-only — one entry per milestone, never edit a previous entry)*

### M0 — Baseline (YYYY-MM-DD)
**Changed:**
**Why:**

### M1 — Tools (YYYY-MM-DD)
**Changed:**
**Why:**
```

At the final submission, the last Design History entry should answer specifically: *what changed between your interim and final design, and what did you learn that made you change it?*

## User story (per epic, in a GitHub Issue)

```markdown
**Story:** As a [stakeholder of the crew's output], I want [capability], so that [value].

**Acceptance criteria:**
- [ ] [testable condition 1]
- [ ] [testable condition 2]

**Definition of done:**
- [ ] Implemented in `agents.yaml`/`tasks.yaml`/`crew.py`
- [ ] Risk identified and logged in `RISK_LOG.md`
```

## `TEAM.md`

```markdown
# Team

| Name | GitHub handle | Primary contribution |
| --- | --- | --- |
| ... | ... | ... |

Topic: [your crew's topic]
```
