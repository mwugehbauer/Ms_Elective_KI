# Team-Aufgabe — Entwerft eure eigene Crew

🇩🇪 **Deutsch** (diese Seite) · 🇬🇧 [English](../en/assignment-overview.md)

Dies ist die benotete Aufgabe, die parallel zur Vorlesungsreihe läuft: In Teams entwerft ihr eine CrewAI-Crew zu einem Thema eurer Wahl und baut sie mit wachsender Komplexität aus, während die Vorlesungen neue Fähigkeiten einführen. Das primäre Abgabeprodukt ist in jeder Phase **euer Entwurf plus eure kritische Einschätzung seiner Risiken und Grenzen** — funktionierender Code ist ein optionaler Bonus, nie eine Pflicht.

Siehe [Meilensteine der Aufgabe](assignment-milestones.md) dafür, was in welcher Phase zu bauen ist, und [Vorlagen für die Aufgabe](assignment-templates.md) für die Dokumente, die ihr ausfüllt.

## So funktioniert es: Sprints entlang der Vorlesungen

Behandelt jede Vorlesung als Sprint-Grenze. Jeder Sprint schaltet eine neue Fähigkeit ("Epic") für euren Crew-Entwurf frei — ihr entwerft nicht jedes Mal neu, sondern erweitert, was schon da ist.

| Vorlesung(en) | Schaltet frei | Meilenstein |
| --- | --- | --- |
| [02](02-agentic-frameworks.md)–[03](03-agentic-design-patterns.md) | Agenten, Tasks, sequentieller Prozess | **M0: Baseline** |
| [04](04-tool-use.md) | Tool-Nutzung | **M1: Tools** |
| [05](05-agentic-rag.md) | Knowledge Sources / RAG | **M2: RAG** *(Zwischenabgabe hier fällig)* |
| [06](06-trustworthy-agents.md) + [08](08-multi-agent-pattern.md) | Guardrails, Multi-Agenten-/hierarchischer Prozess | **M3: Multi-Agent und Vertrauen** |
| [10](10-production.md) + [14](14-securing-agents.md) | Produktions-Aspekte, Security-Threat-Modeling | **Abschluss: Produktion und Sicherheit** |

Zwei Abgaben: eine **Zwischenabgabe** bei M2 (formativ, geringeres Gewicht — fängt schwache Grundlagen früh ab) und eine **Abschlussabgabe** nach der letzten Vorlesung (der vollständige Entwurf plus eine Retrospektive darüber, wie sich euer Denken verändert hat).

## Team-Setup: Repos und Accounts

**Ein GitHub-Repository pro Team — nicht eines pro Studierendem.** Nutzt **"Use this template" → Create a new repository**, nicht "Fork": Forken teilt sich einen Netzwerk-Graph über alle Teams hinweg und zwingt Forks eines öffentlichen Repos, öffentlich zu bleiben, während ein aus einer Vorlage erzeugtes Repo vollständig unabhängig ist und privat gemacht werden kann, falls andere Teams euren Entwurf nicht sehen sollen. (Bittet eure Lehrperson, das Kurs-Repo als Template-Repository zu markieren, falls der Button noch fehlt.)

**Jedes Teammitglied braucht trotzdem einen eigenen GitHub-Account**, als Collaborator im Team-Repo hinzugefügt. Zwei Gründe: Eure einzelnen Commits sind die Grundlage, anhand der der individuelle Beitrag im Team bewertet wird, und eine echte Commit-Historie unter eurem eigenen Account ist über diesen Kurs hinaus etwas wert.

### Zusammenarbeiten ohne Git-Erfahrung

Für die tägliche Teamarbeit braucht ihr keine Branches oder Pull Requests — ein einfacher Ablauf reicht:

1. Bearbeitet eine Datei wie gewohnt (in eurem Codespace).
2. Öffnet das **Source-Control-Panel** (das Verzweigungs-Icon in der Seitenleiste).
3. Schreibt eine kurze Commit-Nachricht, klickt auf **✓ Commit**.
4. Klickt auf **Sync Changes** — das holt in einem Schritt die Änderungen eurer Teammitglieder und schiebt eure eigenen hoch.

Kein Terminal, keine `git add`/`commit`/`push`-Befehle. Alle committen direkt auf `main`.

Um zu vermeiden, dass zwei Personen dieselbe Datei gleichzeitig bearbeiten, **teilt Dateien zwischen Teammitgliedern auf**, wo es geht — z. B. verwaltet eine Person `agents.yaml`, eine andere `tasks.yaml`. `DESIGN.md` ist eine gemeinsame Datei, zu der alle beitragen — wechselt euch dabei ab, oder committet und synct alle paar Minuten, statt lange parallel in derselben Datei zu arbeiten. Falls trotzdem ein Konflikt auftritt, zeigt VS Code eine Merge-Ansicht mit anklickbaren Buttons ("Accept Current / Incoming / Both") — bittet eure Lehrperson einmal um eine kurze Live-Demo davon, damit es niemanden mitten in einer Deadline überrascht.

Für schnelle Änderungen (z. B. einen `RISK_LOG.md`-Eintrag) könnt ihr Codespaces ganz überspringen: Öffnet die Datei auf github.com, klickt auf das Stift-Icon, bearbeitet sie im Browser und klickt unten auf **"Commit changes"**.

## Abgabepaket

Bei jeder Meilenstein-Deadline ist eure Abgabe der Zustand des `main`-Branchs eures Team-Repos:

| Artefakt | Wo | Was es zeigt |
| --- | --- | --- |
| Lauffähige Crew-Konfiguration | `src/research_crew/config/agents.yaml` + `tasks.yaml` (+ `crew.py`, sobald Tools/RAG/Prozess sich ändern) | Die buchstäbliche, lauffähige Version eures Entwurfs |
| Design-Dokument | `DESIGN.md` — Architektur (Agenten/Tasks/Tools/RAG), Risiken, Grenzen, Sicherheit, Produktions-Aspekte, Design-Historie | Eure vollständige, kritisch geprüfte Entwurfsbegründung, in einem sich entwickelnden Bericht |
| Backlog | GitHub Issues (nach Epic gelabelt) + ein Projects-Board | Eure User Stories und euer Fortschritt — lebt auf GitHub, nichts zu exportieren |
| Team-Notizen | `TEAM.md` | Mitglieder und wer was beigetragen hat |
| Optionaler Bonus | ein funktionierendes `crew.py` + ein erfolgreiches `uv run research_crew` | Nur Zusatzpunkte — nie Pflicht |

Die Abgabe ist einfach **der Zustand des `main`-Branchs eures Team-Repos zur Deadline** — es gibt keinen Pull Request zu öffnen. Teilt eure Repo-URL einmal, am Anfang; eure Lehrperson prüft eure Commit-Historie zu jeder Deadline in genau diesem Repo (und kann dafür einen bestimmten Commit taggen).

## Bewertung

Die Entwurfsdokumente (`agents.yaml`/`tasks.yaml` + `DESIGN.md` + Backlog) tragen den weit überwiegenden Teil der Note. Funktionierender Code gibt Bonuspunkte oben drauf, ersetzt aber nie eine dünne oder fehlende Risikoanalyse. Siehe [Meilensteine der Aufgabe](assignment-milestones.md) für die konkreten, pro Phase bewerteten Risikoanalyse-Fragen.

## Agile Praxis: Backlog und User Stories

Führt euren Entwurfsprozess wie ein echtes Produkt-Backlog:
- Die neue Fähigkeit jedes Meilensteins ist ein **Epic**. Brecht es in 2–4 **User Stories** herunter: *"Als [Stakeholder des Crew-Ergebnisses] möchte ich [Fähigkeit], damit [Nutzen]."*
- Schreibt **Akzeptanzkriterien** für jede Story als testbare Bedingungen — diese sind zugleich ein Entwurf für das `expected_output`-Feld des Tasks, sobald ihr beim YAML angelangt seid, was an sich schon eine nützliche Beobachtung ist.
- Fügt jedem Epic "Risiko identifiziert und dokumentiert" zur Definition of Done hinzu, damit Risikoanalyse eine Gewohnheit wird, kein einmaliger Aufsatz.
- Ist euer Team größer als zwei, rotiert die Facilitator-Rolle jeden Sprint.

Vorlagen dafür findet ihr unter [Vorlagen für die Aufgabe](assignment-templates.md).

## Für Lehrende

Um den Template-Repo-Workflow zu aktivieren: **Settings → "Template repository" anhaken** im Haupt-Kurs-Repo. Für eine Erfahrung näher an GitHub Classroom (Classroom selbst nimmt seit Mai 2026 keine neuen Anmeldungen mehr an) lohnt sich eine GitHub-Organisation für den Kurs mit einem Team pro Gruppe — dann seht ihr Repo und Issues jedes Teams an einer Stelle. Bewertet Abgaben, indem ihr die Commit-Historie jedes Teams auf `main` zu jeder Deadline prüft — taggt selbst einen bestimmten Commit (Releases → "Create a new release"), wenn ihr einen unveränderlichen Stand für die Bewertung wollt. Musterlösungen sind bewusst nicht enthalten, wie im Rest dieser Reihe.
