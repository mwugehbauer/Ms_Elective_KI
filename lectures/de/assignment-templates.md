# Vorlagen für die Aufgabe

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-templates.md)

Kopiert diese in euer Team-Repo und füllt sie aus. Siehe [Überblick zur Aufgabe](assignment-overview.md) dafür, wie sie genutzt werden, und [Meilensteine der Aufgabe](assignment-milestones.md) dafür, was in welcher Phase hineingehört.

## `DESIGN.md`

Das ist der Hauptbericht: ein strukturiertes Design-Dokument für die Architektur eurer Crew, das festhält, was ihr gebaut habt, warum, und was schiefgehen könnte. Füllt jeden Abschnitt aus, sobald der jeweilige Meilenstein ihn freischaltet — markiert spätere Abschnitte mit "noch nicht" statt sie zu löschen. Speziell für die Tabellen **Risiken**, **Grenzen** und **Design-Historie**: Das ist append-only — fügt pro Meilenstein neue Zeilen hinzu, bearbeitet oder löscht nie eine vorherige Zeile. Falls ein späterer Meilenstein eure Einschätzung ändert, fügt stattdessen eine neue Zeile hinzu, die das Update vermerkt.

```markdown
# Crew-Design-Dokument

**Team:** [Teamname] · **Thema:** [Thema eurer Crew] · **Zuletzt aktualisiert:** [Meilenstein, JJJJ-MM-TT]

## 1. Überblick
- **Problem / Ziel:** Wofür ist diese Crew, in ein bis zwei Sätzen?
- **Stakeholder:** Wer liest das Ergebnis, und was braucht diese Person davon?

## 2. Architektur

**Prozess:** `Process.sequential` oder `Process.hierarchical` — und warum dieser, nicht der andere.

### Agenten
| Agent | Rolle | Ziel | Verantwortlich für welche(n) Task(s) |
| --- | --- | --- | --- |
| | | | |

### Tasks
| Task | Beschreibung (kurz) | Erwartete Ausgabe | Agent | Abhängig von (`context`) |
| --- | --- | --- | --- | --- |
| | | | | |

### Tools
| Tool | Zweck | Warum dieses Tool für dieses Thema | Braucht API-Key / Embeddings? | Was passiert bei einem Ausfall |
| --- | --- | --- | --- | --- |
| | | | | |

### Knowledge Sources / RAG
*(bis M2 als "noch nicht hinzugefügt" stehen lassen)*

| Quelle | Typ | Warum dieser Inhalt | Embedder | Bekannte Lücken (was NICHT abgedeckt ist) |
| --- | --- | --- | --- | --- |
| | | | | |

### Guardrails / Vertrauensmechanismen
*(bis M3 als "noch keine" stehen lassen)*
-

## 3. Risiken
*(append-only — pro Meilenstein neue Zeilen hinzufügen, alte nie bearbeiten)*

| # | Meilenstein | Risiko | Wo es auftritt (Agent/Task/Tool/RAG) | Mitigation oder akzeptierter Kompromiss |
| --- | --- | --- | --- | --- |
| | | | | |

## 4. Grenzen (Constraints)
*(append-only — pro Meilenstein neue Zeilen hinzufügen, alte nie bearbeiten)*

| # | Meilenstein | Grenze | Typ (Rate-Limit / Kosten / Latenz / Daten / Zeit / Team) | Wie der Entwurf sie berücksichtigt |
| --- | --- | --- | --- | --- |
| | | | | |

## 5. Sicherheit & Threat Model
*(ab M3 ausfüllen, bis zum Abschluss vollständig)*
- Konkretes, zu diesem Entwurf passendes Prompt-Injection-Szenario:
- Umgang mit Secrets:
- Umfang der Tool-Berechtigungen:

## 6. Produktions-Aspekte
*(beim Abschluss ausfüllen)*
- Was ihr überwachen würdet:
- Was euch auf einen Ausfall hinweisen würde:
- Was für echten Produktionseinsatz noch fehlt:

## 7. Betrachtete Alternativen
- Welchen anderen Entwurf habt ihr erwogen (anderer Prozess, anderes Tool, kein RAG, anderer Rollensplit), und warum habt ihr ihn verworfen?

## 8. Design-Historie
*(append-only — ein Eintrag pro Meilenstein, nie einen vorherigen Eintrag bearbeiten)*

### M0 — Baseline (JJJJ-MM-TT)
**Geändert:**
**Warum:**

### M1 — Tools (JJJJ-MM-TT)
**Geändert:**
**Warum:**
```

Bei der Abschlussabgabe sollte der letzte Design-Historie-Eintrag konkret beantworten: *Was hat sich zwischen eurer Zwischen- und Abschlussabgabe verändert, und was habt ihr gelernt, das euch zur Änderung bewogen hat?*

## User Story (pro Epic, als GitHub Issue)

```markdown
**Story:** Als [Stakeholder des Crew-Ergebnisses] möchte ich [Fähigkeit], damit [Nutzen].

**Akzeptanzkriterien:**
- [ ] [testbare Bedingung 1]
- [ ] [testbare Bedingung 2]

**Definition of Done:**
- [ ] Umgesetzt in `agents.yaml`/`tasks.yaml`/`crew.py`
- [ ] Risiko identifiziert und in `RISK_LOG.md` dokumentiert
```

## `TEAM.md`

```markdown
# Team

| Name | GitHub-Handle | Hauptbeitrag |
| --- | --- | --- |
| ... | ... | ... |

Thema: [Thema eurer Crew]
```
