# Meilensteine der Aufgabe — Die Crew-Entwurfsleiter

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-milestones.md)

Wählt ein Thema für eure Crew vor M0 — alles, was eine zweistufige Recherche-/Analyse-Pipeline plausibel angehen könnte (ein Markt, eine Technologie, eine politische Frage, ein historischer Fall). Ihr behaltet dasselbe Thema über alle Meilensteine hinweg.

Alle zehn Ideen unten brauchen bei M0 **keine strukturellen Änderungen** — nur den `topic`-String (und optional Formulierungen in `agents.yaml`) — weil die Rollen von Researcher/Analyst und die `research_task → analysis_task`-Abhängigkeit über den `{topic}`-Platzhalter bereits themenunabhängig sind. Unterschiedlich ist, wie natürlich sich jede Idee zu M1 (Tools) und M2 (RAG) erweitern lässt:

| # | Anwendungsfall | M0-Themenbeispiel | Naheliegendes M1-Tool | Naheliegende M2-RAG-Quelle |
| --- | --- | --- | --- | --- |
| 1 | Wettbewerbsanalyse | "Wettbewerbslandschaft für [Branche]" | `SerperDevTool` behalten, oder `ScrapeWebsiteTool` für Wettbewerber-Seiten | Eigenes Markt-Positionierungs-Briefing (PDF) |
| 2 | Regulatorisches Wirkungs-Briefing | "Auswirkungen des EU AI Act auf SaaS-Startups" | Websuche nach aktuellen Updates | Der eigentliche Verordnungstext — ein gutes Beispiel für RAG mit langen Dokumenten |
| 3 | Akademischer Literaturüberblick | "Aktuelle Entwicklungen in [CS/KI-Teilgebiet]" | `ArxivPaperTool` (bereits in der Tool-Tabelle des READMEs, keine neue Anmeldung nötig) | Das PDF eines bahnbrechenden Papers für Detail-Fragen |
| 4 | Arbeitsmarkt- & Skills-Trendreport | "Gefragte Skills für [Tech-Feld] 2026" | Websuche, oder `SerplyJobSearchTool` | Ein Curriculum-/Skills-Framework-Dokument |
| 5 | Startup-Due-Diligence-Memo | "Due Diligence für [hypothetisches Startup]" | Websuche | Das eigene Pitch-Deck des Startups (PDF) |
| 6 | Personalisierter Reiseplaner | "Reiseplan für [Reiseziel]" | Websuche | `knowledge/user_preference.txt` unverändert weiterverwenden, umgewidmet für Reisepräferenzen — der reibungsärmste RAG-Einstieg der ganzen Liste |
| 7 | Synthese von Produkt-Stimmungsbildern | "Kundenstimmung zu [Produktkategorie]" | Websuche/Scraping-Tool | Die eigenen FAQ-/Support-Dokumente des Produkts |
| 8 | ESG-/Nachhaltigkeits-Risiko-Briefing | "ESG-Risiken für [Unternehmen/Branche]" | Websuche | Der eigene Nachhaltigkeitsbericht des Unternehmens (PDF) |
| 9 | Erklärstück zu einem Finanzthema | "ETFs vs. Einzelaktien für Einsteiger" | Websuche | Ein Fondsprospekt oder Glossar |
| 10 | News-Digest zu einer laufenden Geschichte | "Wöchentlicher Digest zu [laufendem Thema]" | Websuche / `SerplyNewsSearchTool` | Ein Hintergrunddokument mit Kontext vor dem News-Zeitraum |

## M0: Baseline

**Freigeschaltet durch:** Vorlesungen 02–03

**Hinzufügen:** zwei Agenten, ein sequentieller Prozess, keine Tools über das hinaus, was im Starter-Repo bereits verkabelt ist.

**Aktualisieren:** `agents.yaml`, `tasks.yaml`, und `DESIGN.md` (Überblick + Architektur: Prozess, Agenten, Tasks).

**Risiko- und Grenzenfragen** (beantwortet in den Tabellen "Risiken"/"Grenzen" von `DESIGN.md`):
- Warum genau dieser Rollensplit? Was braucht jeder Agent vom anderen, um seine Aufgabe zu erfüllen?
- Was passiert, wenn die Ausgabe eines Agenten subtil falsch ist — merkt der nächste Agent das überhaupt, oder vertraut er blind?

**Vorschlag für eine User-Story:** *"Als [Leser*in des finalen Reports] möchte ich, dass die Schlussfolgerungen des Analysten auf die Befunde des Researchers zurückverfolgbar sind, damit ich beurteilen kann, ob die Schlussfolgerung tatsächlich belegt ist."*

## M1: Tools

**Freigeschaltet durch:** Vorlesung 04

**Hinzufügen:** ein oder zwei Tools aus `crewai_tools` (siehe die [Tool-Tabelle des READMEs](../../README.md#adding-more-tools-or-rag-for-students)), gewählt, weil euer Thema sie wirklich braucht — nicht nur, um ein Kästchen abzuhaken.

**Aktualisieren:** `agents.yaml` (Tools-Liste), Tool-API-Key in `.env`, und `DESIGN.md` (Architektur: Tools-Tabelle).

**Risiko- und Grenzenfragen** (beantwortet in den Tabellen "Risiken"/"Grenzen" von `DESIGN.md`):
- Was passiert, wenn das Tool rate-limitiert ist, nichts Brauchbares zurückgibt, oder die API mitten im Lauf ausfällt? Degradiert eure Crew kontrolliert, oder scheitert sie einfach?
- Macht die Tool-Beschreibung Fehlgebrauch wahrscheinlich (z. B. der Agent ruft es mit falschen Argumenten auf, oder ruft es nicht auf, obwohl er sollte)?

**Vorschlag für eine User-Story:** *"Als [Stakeholder] möchte ich, dass der Researcher aktuelle Informationen abruft statt sich auf die Trainingsdaten des LLM zu verlassen, damit der Report aktuelle Fakten widerspiegelt."*

## M2: RAG (Zwischenabgabe)

**Freigeschaltet durch:** Vorlesung 05

**Hinzufügen:** eine für euer Thema relevante Knowledge Source (`TextFileKnowledgeSource`, `StringKnowledgeSource` oder `PDFKnowledgeSource`), über den bereits in `crew.py` konfigurierten Gemini-Embedder.

**Aktualisieren:** `crew.py` (`knowledge_sources=[...]`), eine neue Datei unter `knowledge/`, und `DESIGN.md` (Architektur: Tabelle Knowledge Sources/RAG).

**Risiko- und Grenzenfragen** (beantwortet in den Tabellen "Risiken"/"Grenzen" von `DESIGN.md`):
- Was fehlt oder ist veraltet in eurer Knowledge Source, und was macht der Agent, wenn das Retrieval nichts Relevantes liefert — rät er, verweigert er, oder sagt er, dass er es nicht weiß?
- Embeddings haben eigene Rate-Limits, getrennt vom Chat-LLM. Würde euer Entwurf noch funktionieren, wenn jemand aus eurem Kurs ein 100-Seiten-Dokument statt eurer wenigen Seiten hochladen würde, oder bräuchte es dann Pacing/Retries?

**Vorschlag für eine User-Story:** *"Als [Stakeholder] möchte ich Antworten, die in [eurer konkreten Quelle] verankert sind, damit der Agent keine Fakten erfindet, die er nie erhalten hat."*

**→ Die Zwischenabgabe ist am Ende dieses Meilensteins fällig.** Einzureichen: `agents.yaml`, `tasks.yaml`, `DESIGN.md` (Abschnitte 1–4 vollständig, mit M0–M2-Zeilen in den Tabellen Risiken/Grenzen/Design-Historie), und euer Backlog (Issues + Project-Board) im aktuellen Stand.

## M3: Multi-Agent und Vertrauen

**Freigeschaltet durch:** Vorlesungen 06 + 08

**Hinzufügen:** einen dritten Agenten, eine begründete Entscheidung zwischen `Process.sequential` und `Process.hierarchical`, und ein `guardrail` auf mindestens einem Task.

**Aktualisieren:** `crew.py`, `agents.yaml`, `tasks.yaml`, und `DESIGN.md` (Architektur: aktualisierter Prozess/Agenten, Guardrails/Vertrauensmechanismen).

**Risiko- und Grenzenfragen** (beantwortet in den Tabellen "Risiken"/"Grenzen" von `DESIGN.md`):
- Falls hierarchisch: Wofür optimiert der Manager beim Delegieren tatsächlich, und könnte das von dem abweichen, was ihr wollt? Falls sequentiell geblieben: Was hätte hierarchisch gebracht, und warum war es den Aufwand nicht wert?
- Was genau fängt euer Guardrail ab, und welches plausible Fehlverhalten würde er übersehen?

**Vorschlag für eine User-Story:** *"Als [Stakeholder] möchte ich eine Prüfung, bevor der finale Report verschickt wird, damit eine offensichtlich kaputte oder themenfremde Ausgabe mich nie erreicht."*

## Abschluss: Produktion und Sicherheit

**Freigeschaltet durch:** Vorlesungen 10 + 14

**Hinzufügen:** einen kurzen Produktionsplan (was würdet ihr überwachen, was würde euch auf einen Ausfall hinweisen) und ein Threat Model (wie realistisch ist das Prompt-Injection- oder Secret-Leak-Risiko für genau euer Thema und eure Tools).

**Aktualisieren:** `DESIGN.md` (Sicherheit & Threat Model, Produktions-Aspekte) — keine zwingenden Code-Änderungen, dieser Meilenstein dreht sich um die schriftliche Ausarbeitung.

**Risiko- und Grenzenfragen** (beantwortet in den Tabellen "Risiken"/"Grenzen" von `DESIGN.md`):
- Würde diese Crew ein Semester lang unbeaufsichtigt zu eurem Thema laufen — was geht als Erstes kaputt, und wie würdet ihr es merken?
- Konstruiert anhand der tatsächlichen Tools/Knowledge Sources eurer Crew ein konkretes (hypothetisches, nicht ausgeführtes) Prompt-Injection-Szenario, das spezifisch zu eurem Entwurf passt — nicht das generische aus Vorlesung 14.

**Abschlussabgabe:** alles oben, plus ein letzter **Design-Historie**-Eintrag in `DESIGN.md` mit der Antwort auf: *Was hat sich zwischen eurer Zwischen- und Abschlussabgabe verändert, und was habt ihr gelernt, das euch zur Änderung bewogen hat?* Diese Frage ist mehr wert, als sie aussieht — sie ist die einzige Stelle, an der ihr zeigen müsst, dass sich euer Denken weiterentwickelt hat, statt sich nur angesammelt zu haben.
