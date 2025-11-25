# KI-gestütztes projektbasiertes Lernen - Prompt Framework

Dieses Framework implementiert ein vollständiges pädagogisches System für KI-gestütztes Programmieren-Lernen mit Kindern und Jugendlichen.

## 📚 Übersicht

Das System kombiniert:
- **Projektbasiertes Lernen** - Schüler lernen durch eigene Projekte
- **Cognitive Apprenticeship** - KI als adaptiver Mentor
- **Spec-driven Development** - Strukturierte Lernreise mit klaren Zielen
- **Zone of Proximal Development** - Dynamische Schwierigkeitsanpassung
- **Polya's Problem-Solving** - Systematischer Problemlösungsansatz

> **✨ NEU (Nov 2025):** Erweitert um wissenschaftlich fundierte [Didaktische Frameworks](#-neue-didaktische-frameworks) mit 4-Phasen-Zyklus, Kompetenz-Tracking und differenziellem Code-Support.

## 🏗️ Architektur

```
.copilot/
├── system-prompt.md              # Master System Prompt für Copilot
├── pedagogical-model.md          # ✨ NEU: Didaktische Grundlagen (4-Phasen-Zyklus)
├── competency-framework.md       # ✨ NEU: Kompetenz-Tracking & Diagnostik
├── integration-guide.md          # ✨ NEU: Wie alles zusammenhängt
├── phase-prompts.md              # Prompts für 6 Lernphasen
├── conversation-patterns.md      # Konversationsmuster & Assessment
├── project-spec-template.yaml    # YAML-Template für Projekte
├── example-project.md            # Vollständiges Beispielprojekt
├── file-overview.md              # Detaillierte Datei-Beschreibungen
└── README.md                     # Diese Datei
```

## 🎯 Die 6 Lernphasen

### Phase 1: Projektinitiierung
**Rolle:** Analyst & Coach  
**Ziel:** Projektziel entwickeln, Motivation aufbauen  
**Prompts:** Offene Fragen, Ideenfindung, Lernziel-Mapping

### Phase 2: Exploration & Anforderungsanalyse
**Rolle:** System Analyst  
**Ziel:** Funktionale Spezifikation erstellen  
**Prompts:** Iterative Verfeinerung, Spec-Generierung

### Phase 3: Konzept & Design
**Rolle:** Mentor  
**Ziel:** Probleme strukturieren, Modelle entwickeln  
**Prompts:** Abstraktion, Visualisierung, Architektur-Diskussion

### Phase 4: Implementation
**Rolle:** Pair Programmer (adaptiv)  
**Ziel:** Code entwickeln mit passender Unterstützung  
**Prompts:** Scaffolded Hints, Code-Vorschläge, Review

### Phase 5: Reflexion & Debugging
**Rolle:** Coach & Reviewer  
**Ziel:** Fehler verstehen, Meta-Lernen fördern  
**Prompts:** Guided Debugging, Reflexionsfragen, Code-Review

### Phase 6: Dokumentation & Präsentation
**Rolle:** Writing Coach  
**Ziel:** Gelerntes festhalten, Projekt präsentieren  
**Prompts:** Dev-Log, README, Präsentationsvorbereitung

## 🎓 Adaptive Scaffolding

Das System passt die Unterstützung dynamisch an den Wissensstand an:

| Level | Scaffolding | Beispiel |
|-------|-------------|----------|
| **Anfänger** | Hoch | Detaillierte Schritt-für-Schritt-Anleitung mit Beispielen |
| **Fortgeschritten** | Mittel | Struktur vorgeben, Schüler implementiert Details |
| **Expert** | Niedrig | Konzeptuelle Hinweise, offene Diskussion |

### Scaffolding-Fading
Die Unterstützung wird schrittweise reduziert:
- ✅ Erfolg → Scaffolding ↓
- 🎯 Transfer zu neuem Kontext → Scaffolding ↓↓
- 🐛 Selbstständiges Debugging → Scaffolding ↓
- 😞 Frustration → Scaffolding ↑

## 📊 Assessment Framework

### Wissensstand-Erkennung

**Automatische Indikatoren:**

```yaml
Anfänger:
  code: Globale Variablen, Wiederholungen, wenig Struktur
  fragen: "Was ist...?", "Wie macht man...?"
  verhalten: Braucht detaillierte Anleitung

Fortgeschritten:
  code: Funktionen, Listen, strukturierter Code
  fragen: "Wie implementiere ich...?"
  verhalten: Experimentiert, stellt "Warum"-Fragen

Expert:
  code: OOP, Design Patterns, Tests
  fragen: "Was sind die Trade-offs...?"
  verhalten: Sehr selbstständig, diskutiert Architektur
```

### Lernfortschritt-Tracking

**Konzept-Mastery (6 Stufen):**
1. Exposure (gesehen)
2. Recognition (erkennt)
3. Reproduction (mit Anleitung)
4. Application (selbstständig)
5. Transfer (neuer Kontext)
6. Mastery (erklärt & optimiert)

**Metriken:**
- Quantitativ: Konzepte gemeistert, Unabhängigkeits-Rate, Code-Qualität
- Qualitativ: Problemlösungsansatz, Reflexionstiefe, Kollaborationsqualität

## 🎮 Engagement-Monitoring

### Positive Signale
- ✅ Stellt Fragen
- ✅ Experimentiert mit Code
- ✅ Macht eigene Vorschläge
- ✅ Reagiert positiv auf Feedback

### Warnsignale
- ⚠️ Lange Inaktivität
- ⚠️ Kopiert ohne zu verstehen
- ⚠️ Frustrations-Signale
- ⚠️ Minimale Antworten

**Auto-Intervention bei niedrigem Engagement:**
- Erfolgserlebnis ermöglichen
- Schwierigkeit reduzieren
- Interesse neu wecken
- Pause vorschlagen

## 💬 Conversation Patterns

### Frage-Typen

**Open-Ended Questions**
```
"Was möchtest du bauen?"
"Wie stellst du dir das vor?"
```
→ Fördert Kreativität und Eigenverantwortung

**Guided Discovery**
```
"Was passiert, wenn du diese Zeile auskommentierst?"
"Welche Werte haben die Variablen hier?"
```
→ Führt zum Verständnis ohne direkte Antwort

**Socratic Questions**
```
"Warum glaubst du, macht der Code das?"
"Was würde passieren, wenn...?"
"Wie hängt das mit [Konzept] zusammen?"
```
→ Vertieft Verständnis durch Hinterfragen

**Checkpoint Questions**
```
"Kannst du in eigenen Worten erklären, was eine Variable ist?"
"Was macht diese Funktion?"
```
→ Prüft Verständnis vor dem Weitermachen

### Feedback-Patterns

**Positive Reinforcement**
```
🎉 "Super! Du hast [spezifische Leistung] gemeistert!"
📚 "Damit hast du [Konzept] verstanden!"
🚀 "Jetzt kannst du [nächster Schritt]!"
```

**Constructive Feedback**
```
1. Acknowledge: "Ich sehe, du versuchst..."
2. Identify: "Dabei ist [Problem] aufgetreten"
3. Explain: "Das passiert, weil..."
4. Guide: "Lass uns [Lösungsweg] versuchen"
5. Encourage: "Du bist auf dem richtigen Weg!"
```

**Scaffolded Hints (4 Stufen)**
```
Level 1: "Du brauchst etwas, das Entscheidungen treffen kann..."
Level 2: "Du brauchst eine if-Bedingung: if [Bedingung]: ..."
Level 3: [Code-Beispiel mit Lücken]
Level 4: [Vollständige Lösung mit Erklärung]
```

## 📝 Project Spec (YAML)

Jedes Projekt hat eine `project-spec.yaml` Datei:

```yaml
project:
  name: "Mein Spiel"
  type: "game"
  technology:
    primary_language: "python"

goals:
  main: "Funktionierendes Jump & Run Spiel"
  success_criteria:
    - "Spieler kann sich bewegen"
    - "Kollisionserkennung funktioniert"

learning_objectives:
  - concept: "variables"
    level: "beginner"
    status: "completed"
  - concept: "loops"
    level: "beginner"
    status: "in-progress"

milestones:
  - title: "Projekt-Setup"
    status: "completed"
  - title: "Grundfunktionalität"
    status: "in-progress"

student_profile:
  level: "beginner"
  known_concepts: ["print", "variables"]
  learning_pace: "normal"
```

Siehe `project-spec-template.yaml` für vollständige Struktur.

## 🚀 Integration in GitHub Copilot

### Schritt 1: Workspace-Konfiguration

Platziere die `.copilot/` Dateien im Root des Projekts:

```
mein-lernprojekt/
├── .copilot/
│   ├── system-prompt.md
│   ├── phase-prompts.md
│   ├── conversation-patterns.md
│   └── project-spec-template.yaml
├── main.py
└── README.md
```

### Schritt 2: Copilot Instruction anpassen

In VS Code Settings → Copilot Instructions:

```markdown
Du bist ein pädagogischer Programmier-Tutor. 
Lies und befolge die Anweisungen in `.copilot/system-prompt.md`.

Verwende:
- `phase-prompts.md` für phasen-spezifische Dialoge
- `conversation-patterns.md` für Konversationsmuster
- `project-spec.yaml` für Projekt-Kontext

Dein Ziel: Schüler durch projektbasiertes Lernen führen, 
Wissen adaptiv vermitteln, Motivation aufrechterhalten.
```

### Schritt 3: Projekt starten

**Für Schüler:**
```
1. Öffne VS Code in deinem Projekt-Ordner
2. Starte Chat mit Copilot
3. Sage: "Ich möchte ein Projekt starten!"
4. Folge den Fragen des Copilots
```

**Copilot erstellt automatisch:**
- `project-spec.yaml` mit deinen Projektzielen
- Lernpfad basierend auf gewähltem Projekt
- Meilensteine und Aufgaben

### Schritt 4: Während der Entwicklung

Copilot passt sich dynamisch an:
- Erkennt deinen Wissensstand
- Gibt passende Hinweise (nicht zu viel, nicht zu wenig)
- Feiert deine Erfolge
- Hilft beim Debuggen
- Dokumentiert deine Lernreise

## 🎨 Beispiel-Interaktion

**Schüler:** "Ich möchte ein Spiel machen!"

**Copilot (Phase 1):**
```
Super Idee! 🎮 Lass uns dein Spiel planen.

Was für ein Spiel möchtest du machen?
- Ein Jump & Run wie Super Mario?
- Ein Ratespiel?
- Ein Quiz?
- Etwas ganz anderes?
```

**Schüler:** "Jump & Run!"

**Copilot (Phase 2):**
```
Toll! 🏃‍♂️ Ein Jump & Run Spiel ist perfekt zum Lernen!

Lass uns die wichtigsten Features planen:
1. Was soll deine Spielfigur können? (Laufen, Springen, ...?)
2. Gibt es Gegner oder Hindernisse?
3. Wie gewinnt man das Spiel?
```

[... Iterative Verfeinerung ...]

**Copilot (Phase 3):**
```
Perfekt! Ich erstelle jetzt einen Bauplan für dein Spiel.

Wir brauchen:
- Variablen für Position (x, y)
- Schleifen für die Hauptspiel-Logik
- Bedingungen für Kollisionserkennung

Kennst du schon Variablen? (ja/nein)
```

**Schüler:** "Ein bisschen"

**Copilot (adaptive Anpassung → Medium Scaffolding):**
```
Okay! Dann machen wir eine kurze Auffrischung:

Eine Variable ist wie eine beschriftete Box 📦
Dort speichern wir Daten, z.B. die Position der Spielfigur.

```python
x = 100  # X-Position (horizontal)
y = 200  # Y-Position (vertikal)
```

Jetzt du: Erstelle eine Variable `speed` für die Geschwindigkeit!
```

[... und so weiter durch alle Phasen ...]

## 📚 Verbindung zu Learning Paths

Die Prompts nutzen die vorhandenen Learning Paths:

```
learning-paths/
├── extreme-programming.md
├── test-driven-development.md
├── object-oriented-software-construction.md
├── software-architecture-in-practice.md
└── ...
```

**Copilot kann:**
- Konzepte aus Learning Paths referenzieren
- Übungen vorschlagen
- Lernpfad-Empfehlungen geben

**Beispiel:**
```
"Super! Du verstehst jetzt Funktionen! 🎉

Wenn du mehr über professionelle Code-Organisation 
lernen möchtest, schau dir später den Learning Path 
'Object-Oriented Programming' an!

Erstmal: Lass uns deine erste Funktion schreiben!"
```

## 🧪 Testing & Evaluation

### A/B Testing Strategies

Test verschiedene Prompt-Varianten:
- **Mehr/Weniger Emojis** - Motiviert oder lenkt ab?
- **Kurze vs. Ausführliche Erklärungen** - Was funktioniert besser?
- **Socratic vs. Direct** - Wann welcher Stil?

### Evaluation-Metriken

**Lern-Erfolg:**
- Anzahl gemeisterter Konzepte
- Zeit bis Konzept-Mastery
- Transfer-Fähigkeit (neue Projekte)

**Engagement:**
- Session-Dauer
- Wiederkehr-Rate
- Selbst-Motivation (arbeitet alleine?)

**Zufriedenheit:**
- Selbst-Assessment (Wie schwer war es?)
- Spaß-Faktor (Hat es Spaß gemacht?)

## 🔧 Anpassung & Erweiterung

### Neue Programmiersprache hinzufügen

1. Passe Code-Beispiele in `phase-prompts.md` an
2. Füge sprachspezifische Patterns zu `conversation-patterns.md` hinzu
3. Aktualisiere `project-spec-template.yaml` (Technology-Section)

### Neue Lernphase hinzufügen

1. Definiere Phase in `phase-prompts.md`
2. Erstelle Prompts für alle Level (Beginner/Intermediate/Advanced)
3. Füge Phase zu Workflow in `system-prompt.md` hinzu

### Prompt-Feintuning

Beobachte Schüler-Interaktionen und justiere:
- Sind Erklärungen zu komplex/zu einfach?
- Sind Scaffolding-Levels gut gewählt?
- Funktioniert Engagement-Monitoring?

Dokumentiere Änderungen im Changelog der jeweiligen Datei.

## 📖 Weitere Ressourcen

### Theoretische Grundlagen

- **Constructivism:** Piaget, Papert (Learning by Making)
- **ZPD:** Vygotsky (Zone of Proximal Development)
- **Cognitive Apprenticeship:** Collins, Brown, Newman (1989)
- **Problem-Solving:** Polya (How to Solve It)
- **Flow:** Csikszentmihalyi (optimal challenge)

### Didaktik-Literatur

- Hubwieser: "Didaktik der Informatik"
- Magenheim/Romeike: "Kompetenzorientierter Informatikunterricht"
- Herper: "Problemorientiertes Lernen"
- Spannagel: "Digitales Lernen"

## 🤝 Contribution

Verbesserungen willkommen! 

**Bereiche für Contributions:**
- Neue Konversationsmuster
- Zusätzliche Assessment-Metriken
- Erweiterungs-Patterns (z.B. Gruppen-Projekte)
- Übersetzungen (Englisch, andere Sprachen)
- Best Practice Beispiele

---

## 🆕 Neue Didaktische Frameworks (Nov 2025)

Das Framework wurde um **wissenschaftlich fundierte pädagogische Konzepte** erweitert:

### 📖 [Pädagogisches Modell](pedagogical-model.md)

**Kernkonzepte:**
- **4-Phasen-Zyklus:** Anforderungsanalyse → Konzeptualisierung → Realisierung → Reflexion
- **Rollenmodell:** Klare Definition von Lernenden, KI-Copilot ("Kai"), und Lehrer
- **Differentieller Code-Support:** Adaptive Unterstützung je nach Level (Anfänger/Fortgeschritten/Erfahren)
- **Didaktische Prinzipien:** Scaffolding & Fading, Zone of Proximal Development, Cognitive Apprenticeship

**Wann nutzen:** 
- Als theoretische Basis für das gesamte Framework verstehen
- Bei Projekt-Design: Welche Phase? Welche Rolle übernimmt die KI?
- Bei Anpassung der Prompts an neue Zielgruppen

### 📊 [Kompetenzframework](competency-framework.md)

**Kernkonzepte:**
- **5 Kernkompetenzen:** Modellieren, Implementieren, Reflektieren, Kommunizieren, KI-Kooperation
- **4 Level pro Kompetenz:** Novize → Fortgeschritten → Kompetent → Expert
- **Automatisierte Diagnostik:**
  - Prompt-Evolution-Analyse (Qualität der Fragen)
  - Code-Übernahmequote (Authorship-Tracking)
  - Debugging-Autonomie-Score
  - Konzept-Mastery-Tracker
  - Metakognitive Reifung
- **Bewertungs-Rubrik** für Lehrer
- **Self-Assessment** für Lernende

**Wann nutzen:**
- Bei Lernfortschritts-Bewertung: Wo steht der Lernende?
- Bei Anpassung der Unterstützung: Welches Level? Welche Kompetenz fördern?
- Bei Portfolio-Reviews: Messindikatoren für objektive Bewertung

### 🔗 [Integration Guide](integration-guide.md)

**Kernkonzepte:**
- Wie die neuen Frameworks mit bestehenden Dateien zusammenarbeiten
- Workflow-Diagramm: Copilot Decision Flow
- Praktische Anwendung für Copilot, Lehrer und Lernende
- Empfohlene Updates und Implementierungs-Checkliste
- Quellenverankerung (Bibliografie der Theorien)

**Wann nutzen:**
- Bei Integration neuer Features: Wie fügt sich das ins System ein?
- Bei Debugging von Copilot-Verhalten: Welche Dateien beeinflussen was?
- Als Onboarding-Material für neue Team-Mitglieder
- Bei Fragen zur Architektur: "Wie hängt alles zusammen?"

### 🎓 [Teaching Methods](teaching-methods.md) ⭐

**Kernkonzepte:**
- **Fragetechniken:**
  - Prompt-a-thon (Requirement Elicitation nach Polya)
  - 5-Why-Debugging (Root-Cause-Analyse)
  - Socratic Code Review (Leitfragen statt Lösungen)
  
- **Didaktische Analogien:**
  - LEGO-System-Analogie (KI-Koaktivität verständlich)
  - Koch-Rezept-Analogie (Algorithmen & Syntax)
  - Dirigent-Orchester-Analogie (OOP)
  
- **Modellierungsmethoden:**
  - Think-Pair-Program
  - Story-Mapping für Use Cases
  - CRC-Karten für OOP
  - Zustandsdiagramme mit Emojis
  
- **Code-Verstehensmethoden:**
  - Code-Leseprotokoll
  - Rubber-Duck-Debugging
  - Code-Kommentar-Challenge
  
- **Debugging-Strategien:**
  - STOP-Methode
  - Binary-Search-Debugging
  - Debug-Print-Strategie
  
- **Reflexionsmethoden:**
  - Dev-Log mit Leitfragen
  - Think-Aloud Protocol
  - Code-Review-Checkliste

**Wann nutzen:**
- Bei Lernschwierigkeiten: Passende Methode wählen
- Für Abwechslung im Unterricht: Verschiedene Lerntypen ansprechen
- Als Copilot-Repertoire: "Nutze LEGO-Analogie zum Erklären"
- Für Lehrer-Training: Konkrete, erprobte Unterrichtsmethoden

---

### 🔄 Zusammenspiel der Frameworks
- Workflow-Integration in den Lernzyklus
- Praktische Anwendung für Copilot, Lehrer, Lernende
- Technische Umsetzung & Datenfluss

**Wann nutzen:**
- Beim Onboarding neuer Nutzer: "Wie funktioniert das System?"
- Bei Implementierung eigener Tools: Welche Daten-Schnittstellen?
- Bei Erweiterung des Frameworks: Wo füge ich neue Konzepte ein?

### 🔄 Zusammenspiel der Frameworks

```
Pedagogical Model (WARUM)
    ↓ definiert
Rollenmodell + 4-Phasen + Prinzipien
    ↓ implementiert in
System-Prompt + Phase-Prompts
    ↓ nutzt
Teaching Methods (WIE konkret)
    ↓ evaluiert mit
Competency Framework (WAS messen)
    ↓ dokumentiert in
Project-Spec + Integration Guide
```

**Kern-Aussage:**
- **Pedagogical Model** = Theoretisches Fundament (WARUM so?)
- **Competency Framework** = Messbare Ziele (WAS erreichen?)
- **Teaching Methods** = Konkrete Werkzeuge (WIE umsetzen?)
- **Phase-Prompts & Conversation-Patterns** = Praktische Anwendung (Copilot-Verhalten)
- **Integration Guide** = Landkarte (Wie hängt alles zusammen?)

---

### 📚 Theoretisches Fundament
Pädagogisches Modell (WARUM)
        ↓
   Definiert Phasen & Rollen
        ↓
Kompetenzframework (WAS)
        ↓
   Definiert Lernziele & Metriken
        ↓
Phase-Prompts & Conversation-Patterns (WIE)
        ↓
   Konkrete Prompts für Copilot
        ↓
Integration Guide (UMSETZUNG)
        ↓
   Praktische Anwendung
```

**Theoretische Fundierung:**
- Polya (1945): Problem Solving
- Vygotsky (1978): Zone of Proximal Development
- Collins et al. (1989): Cognitive Apprenticeship
- Hubwieser (2007): Didaktik der Informatik
- Wing (2006): Computational Thinking
- GI-Bildungsstandards Informatik

---

## �📄 Lizenz

Dieses Framework ist Teil des `project-based-learning` Repositories und steht unter der gleichen Lizenz.

---

**Happy Coding & Teaching! 🚀**

*Erstellt im Rahmen des KI-gestützten projektbasierten Lern-Projekts*  
*Version 2.0 - November 2025 (erweitert mit Didaktischen Frameworks)*
