# Pädagogisches Modell: KI-gestütztes Projektbasiertes Lernen

## Überblick

Dieses Dokument beschreibt das didaktische Fundament für KI-gestütztes Programmieren-Lernen basierend auf **workload-orientiertem, iterativem Projektlernen** mit einem KI-Copiloten als aktivem Lernbegleiter.

## Leitidee

> **Programmieren ist Problemlösekunst, nicht Syntax-Training.**

Der KI-Copilot fungiert als **didaktischer Verstärker** im Sinne eines *Cognitive Apprenticeship*:
- Denkt laut mit dem Lernenden
- Stellt klärende Fragen
- Fordert ohne zu überfordern
- Spiegelt Denkprozesse
- Erklärt Konzepte
- **Löst NICHT anstelle des Schülers**

### Ziel

Lernende erwerben ein **"Programmier-Mindset"** (Computational Thinking):
- Denken in Modellen und Abstraktionen
- Verstehen von Zuständen und Prozessen
- Systematisches Problemlösen durch Iteration
- Selbstreguliertes Lernen
- Kritischer Umgang mit KI-Werkzeugen

---

## 🎭 Rollenmodell

### 1. **Der Lernende (Schüler/Student)**

**Kernrollen:**
- **Ideengeber** - Wählt eigenes, motivierendes Projekt
- **Problemlöser** - Entwickelt Lösungsstrategien
- **Implementierer** - Setzt Code um (mit angemessener Unterstützung)
- **Evaluator** - Testet, debuggt, reflektiert
- **Dokumentator** - Hält Lernweg fest

**Verantwortung:**
- Formuliert Projektziel und Anforderungen
- Trifft Design-Entscheidungen
- Übernimmt Kernaufgaben der Implementierung
- Validiert KI-generierte Vorschläge kritisch
- Reflektiert über Lernfortschritt

**Autonomie-Level:** 
- Steigt mit Kompetenz (von geführt → selbstgesteuert)

---

### 2. **Der KI-Copilot ("Kai")**

**Adaptive Rollen je nach Lernphase:**

| Phase | Rolle | Funktion |
|-------|-------|----------|
| **Anforderungen** | Requirements Engineer | Stellt klärende Fragen, konkretisiert vage Ideen |
| **Konzept** | Mentor & Architekt | Hilft bei Strukturierung, schlägt Modelle vor |
| **Implementation** | Pair Programmer | Bietet Code-Support (adaptiv zum Level) |
| **Debugging** | Coach & Reviewer | Führt durch Fehleranalyse, gibt Meta-Hinweise |
| **Reflexion** | Sokratischer Dialog-Partner | Stellt Reflexionsfragen, fördert Transfer |
| **Dokumentation** | Writing Coach | Unterstützt beim Festhalten des Gelernten |

**Kernprinzipien:**
- ✅ Scaffolding & Fading (Hilfe reduzieren bei Fortschritt)
- ✅ Minimale Hilfe (so wenig wie möglich, so viel wie nötig)
- ✅ Guided Discovery (Hinweise in zunehmender Detailtiefe)
- ✅ Formatives Feedback (konstruktiv, zeitnah, spezifisch)
- ❌ NICHT: Fertige Lösungen ohne Anleitung
- ❌ NICHT: Übernehmen von Kernaufgaben des Lernenden

**Technische Umsetzung:**
- System-Prompt definiert pädagogische Rolle
- Prompt-Tuning passt Detailgrad an Wissenstand an
- Context aus `project-spec.yaml` + Chat-Historie

---

### 3. **Der Lehrer/Mentor**

**Rollen:**
- **Moderator** - Begleitet Projektauswahl, hilft bei Scope-Definition
- **Beobachter** - Überwacht Lernfortschritt via Projekt-Logs
- **Evaluator** - Bewertet Prozess UND Produkt
- **Didaktiker** - Kuratiert Lernziele, passt Framework an
- **Technischer Support** - Hilft bei Tool/Setup-Problemen

**Bewertungsfokus:**
- Prozessorientiert (nicht nur Endergebnis)
- Chatverläufe analysieren (Prompt-Qualität, Interaktion)
- Übernahmequote messen (was macht Schüler selbst?)
- Reflexionsfähigkeit bewerten
- Metakognitive Entwicklung erkennen

---

## 🔄 4-Phasen-Zyklus (Iterativ)

### **Phase 1: Problemgewinnung & Anforderungsanalyse**

**Ziel:** Von der Vision zur konkreten, spezifizierten Aufgabe

**Aktivitäten:**

| Akteur | Aufgabe | Didaktische Verankerung |
|--------|---------|------------------------|
| **Lernender** | Formuliert Projektidee in Alltagssprache | Intrinsische Motivation, Schülerorientierung |
| **KI-Copilot** | Führt iterative Fragerunde (*Requirement Elicitation*) | Schult Problemformulierung, Spezifikationsdenken |
| | *"Was ist bekannt? Was ist gesucht? Welche Bedingungen?"* | Eingrenzung, Konkretisierung |

**Output:** 
- Anforderungsspezifikation in `project-spec.yaml`
- Funktionale Beschreibung (Input/Output, Bedingungen)
- Erste Testfälle als Akzeptanzkriterien

**Beispiel-Prompts:**
```
"Erzähl mir mehr über dein Projekt: Wer wird es nutzen?"
"Was soll genau passieren, wenn der Nutzer auf den Button klickt?"
"Welche Daten brauchst du dafür?"
```

**Kompetenzfokus:** 
- Problemidentifikation
- Kontextualisierung
- Spezifikationssprache

---

### **Phase 2: Konzeptualisierung & Modellierung**

**Ziel:** Abstraktion - vom Problem zum formalen Lösungsplan

**Aktivitäten:**

| Akteur | Aufgabe | Didaktische Verankerung |
|--------|---------|------------------------|
| **Lernender** | Beschreibt Abläufe, erstellt erste Skizzen | Fähigkeit zur Abstraktion schulen |
| **KI-Copilot** | Unterstützt Strukturierung in Teilprobleme | Modellierung als **Kern informatischer Arbeit** |
| | Schlägt Modellierungstechniken vor (OOP, Algorithmen) | Globale Strategie: Denken in Prozessen/Systemen |
| | Generiert Testfälle als zusätzlichen Kontext | Testgetriebene Entwicklung fördern |

**Output:**
- Lösungsplan (Algorithmus in Pseudocode oder Diagramm)
- Datenmodell (Variablen, Datenstrukturen)
- Kontrollfluss (Sequenz, Verzweigungen, Schleifen)
- OOP-Design (optional: Klassen, Methoden, Beziehungen)

**KI-Einsatz:**
- Fragt nach Beziehungen: *"Was passiert zuerst? Dann?"*
- Schlägt passende Abstraktionen vor
- WICHTIG: Copilot generiert NICHT das fertige Modell, sondern **hilft es zu entwickeln**

**Beispiel-Dialog:**
```
Lernender: "Der Spieler soll raten können und Hinweise bekommen."
Copilot: "Lass uns das strukturieren:
  1. Computer wählt Zufallszahl
  2. Spieler gibt Tipp ein
  3. Vergleich: Zu hoch? Zu niedrig? Richtig?
  4. Wenn falsch: Wiederhole 2-3
  Welche Daten brauchst du dafür zu speichern?"
```

**Kompetenzfokus:**
- Algorithmisches Denken
- Modellbildung
- Strukturierung

---

### **Phase 3: Realisierung & Iterative Umsetzung**

**Ziel:** Implementation des Modells in lauffähigen Code

#### **Differentieller Code-Support** (adaptiv zum Wissensstand)

| Level | Copilot-Unterstützung | Lernender übernimmt | Beispiel |
|-------|----------------------|---------------------|----------|
| **Anfänger** | • Generiert Grundgerüst<br>• Erklärt Syntax detailliert<br>• Zeigt kommentierte Beispiele | • Liest & interpretiert Code<br>• Ändert Werte/Texte<br>• Führt Code aus | Copilot: Template mit Kommentaren<br>Schüler: Variablen benennen |
| **Fortgeschritten** | • Diskutiert Algorithmen<br>• Gibt strukturelle Hinweise<br>• Liefert Boilerplate-Code | • Implementiert Kernlogik<br>• Schreibt Funktionen selbst<br>• Testet eigenständig | Copilot: "Brauchst du eine Schleife"<br>Schüler: Schreibt while-Loop |
| **Erfahren** | • Reviewed Code-Qualität<br>• Diskutiert Architektur<br>• Schlägt Optimierungen vor | • Entwirft & implementiert vollständig<br>• Testet systematisch<br>• Refactored | Copilot: Code-Review<br>Schüler: Eigenständige Entwicklung |

**Lernpsychologische Basis:**
- **Zone of Proximal Development** (Vygotskij): Aufgaben sind herausfordernd aber lösbar mit Unterstützung
- **Cognitive Load Theory**: Komplexität anpassen, nicht überfordern
- **Deliberate Practice**: Wiederholung mit Feedback

**Messung des Lernfortschritts:**
- **Übernahmequote**: Wieviel Code schreibt der Lernende selbst?
- **Prompt-Qualität**: Werden Fragen spezifischer?
- **Debugging-Fähigkeit**: Findet Lernender Fehler selbst?

**Beispiel-Progressionen:**
```
Woche 1: Copilot generiert komplette Funktion
         → Schüler benennt Variablen um

Woche 3: Copilot gibt Pseudocode
         → Schüler implementiert in Python

Woche 6: Copilot gibt nur Hinweis "Du brauchst eine Liste"
         → Schüler schreibt komplette Lösung
```

---

### **Phase 4: Reflexion, Testing & Debugging**

**Ziel:** Analyse, Verbesserung, Meta-Lernen

**Aktivitäten:**

| Akteur | Aufgabe | Didaktische Verankerung |
|--------|---------|------------------------|
| **Lernender** | Führt Tests durch, analysiert Fehler | Fehler als Lernchance normalisieren |
| | Formuliert Hypothesen über Fehlerursachen | Debugging als Problemlösekompetenz |
| **KI-Copilot** | Gibt gezielte Testfälle | Testgetriebenes Denken fördern |
| | Stellt Fragen statt Lösungen zu geben | Guided Discovery, Metakognition |
| | Gibt Feedback auf Prozess- UND Inhaltsebene | Formative Assessment |

**Reflexionsfragen (Copilot):**
```
"Was hast du heute gelernt?"
"Welche Entscheidung war schwierig? Warum?"
"Wie würdest du das Problem jetzt ohne KI lösen?"
"Was hat dich überrascht?"
"Welche Fehler hast du gemacht - und was hast du daraus gelernt?"
```

**Testing-Strategie:**
- Copilot schlägt Edge Cases vor
- Lernender entwickelt eigene Tests
- Gemeinsame Analyse von Fehlverhalten

**Beispiel Debugging-Dialog:**
```
Lernender: "Mein Code gibt immer 'Zu niedrig' aus!"
Copilot: "Interessant! Lass uns systematisch vorgehen:
  1. Was erwartest du bei Eingabe 50?
  2. Was passiert tatsächlich?
  3. Welche Bedingung prüft dein if-Statement?
  → Versuch's mal selbst zu debuggen, ich helfe wenn du stecken bleibst."
```

**Kompetenzfokus:**
- Debugging-Strategien
- Systematisches Testen
- Reflexionsfähigkeit
- Fehlertoleranz

---

### **📝 Phase 5: Dokumentation & Präsentation**

**Ziel:** Lernweg sichtbar machen, Wissen sichern, Transfer fördern

**Ergebnisprodukte:**

1. **Projektjournal** (kontinuierlich)
   - Anforderungen & Spezifikation
   - Modell-Skizzen & Diagramme
   - Code-Versionen mit Kommentaren
   - Wichtige Chat-Ausschnitte mit Copilot
   - Gelöste Probleme & Entscheidungen

2. **Selbstreflexion**
   - "Was habe ich gelernt?"
   - "Wo hat die KI geholfen? Wo war ich selbstständig?"
   - "Was würde ich beim nächsten Mal anders machen?"
   - "Welche Konzepte verstehe ich jetzt besser?"

3. **README.md** (für Projekt)
   - Was macht das Projekt?
   - Wie nutzt man es?
   - Welche Technologien wurden verwendet?
   - Was war besonders herausfordernd?

4. **Präsentation** (5-10 Min)
   - Live-Demo
   - Erklärung eines interessanten Code-Teils
   - Lessons Learned

**KI-Support:**
- Hilft beim Strukturieren der Dokumentation
- Gibt Feedback zu Erklärungen
- Schlägt Visualisierungen vor

**Bewertungskriterien:**
- Vollständigkeit der Dokumentation
- Tiefe der Reflexion
- Verständlichkeit der Erklärungen
- Kritische Auseinandersetzung mit KI-Hilfen

---

## 🎯 Didaktische Grundprinzipien

| Prinzip | Umsetzung im KI-Setting | Theoriebezug |
|---------|------------------------|--------------|
| **Projektorientierung** | Schüler wählen reale, motivierende Projekte | Konstruktivismus, Situated Learning |
| **Selbststeuerung** | Schüler bestimmen Ziele, Copilot begleitet metakognitiv | Self-Regulated Learning |
| **Scaffolding & Fading** | Copilot gibt anfangs viel Hilfe, zieht sich zurück bei Kompetenz | Zone of Proximal Development |
| **Dialogisches Lernen** | Strukturierte Fragerunden, Prompt-Didaktik | Cognitive Apprenticeship |
| **Reflexion** | Kontinuierliche Reflexion über Code, Konzepte, KI-Interaktion | Metacognition |
| **Kompetenzorientierung** | Bezug zu GI-Bildungsstandards (Modellieren, Implementieren, Bewerten) | Standards der Informatik-Didaktik |
| **Fehlerkultur** | Fehler als Lernchance, nicht als Versagen | Growth Mindset |
| **Differenzierung** | Adaptiver Support je nach Level | Universal Design for Learning |

---

## 📊 Kompetenzentwicklung

### Kernkompetenzen (nach GI-Standards)

| Kompetenzfeld | Beschreibung | Konkrete Aktivitäten |
|---------------|--------------|---------------------|
| **Modellieren** | Strukturen & Abläufe formal darstellen | Diagramme, Pseudocode, Datenmodelle |
| **Implementieren** | Modelle in Code umsetzen | Programmieren, Debugging, Testing |
| **Reflektieren** | Vorgehen & Ergebnis bewerten | Begründen, Alternativen erkennen |
| **Kommunizieren** | Ideen austauschen (mit KI & Menschen) | Präzise Sprache, Prompts, Präsentation |
| **KI-Kooperation** | KI als Werkzeug & Partner nutzen | Konstruktiver Dialog, kritische Validierung |

### Computational Thinking Dimensionen

1. **Decomposition** - Probleme in Teilprobleme zerlegen
2. **Pattern Recognition** - Muster & Ähnlichkeiten erkennen
3. **Abstraction** - Wesentliches vom Unwesentlichen trennen
4. **Algorithm Design** - Schrittweise Lösungen entwickeln
5. **Evaluation** - Lösungen testen & verbessern

---

## 🔍 Lernfortschrittsdiagnostik

### Automatische Indikatoren

**1. Prompt-Analyse**
- **Anfänger**: "Wie macht man...?", vage Fragen
- **Fortgeschritten**: "Wie implementiere ich X mit Y?"
- **Erfahren**: "Was sind Trade-offs zwischen A und B?"

**2. Code-Qualität**
- **Anfänger**: Globale Variablen, Wiederholungen, wenig Struktur
- **Fortgeschritten**: Funktionen, Listen, strukturierter Code
- **Erfahren**: OOP, Design Patterns, Tests

**3. Übernahmequote**
- Anteil selbst geschriebener Code vs. KI-generiert
- Tracking über Code-Versionen + Chat-Logs

**4. Debugging-Autonomie**
- **Level 1**: Braucht vollständige Anleitung
- **Level 2**: Findet Fehler mit Hinweisen
- **Level 3**: Debuggt systematisch selbstständig

**5. Metakognitive Äußerungen**
- "Ich weiß nicht, wie ich anfangen soll" → niedrig
- "Ich probiere erst X, wenn das nicht klappt Y" → mittel
- "Ich plane zuerst die Struktur, dann implementiere ich" → hoch

---

## 🛠️ Technisch-Didaktische Infrastruktur

### Komponenten

| Komponente | Funktion | Implementation |
|------------|----------|----------------|
| **KI-Copilot-Interface** | Chat + IDE Integration | VS Code Extension, Jupyter, Web-IDE |
| **Logging-System** | Speichert Prompts, Antworten, Code-Versionen | Git + JSON-Logs für Evaluation |
| **project-spec.yaml** | Hinterlegt Lernziele, Schwierigkeit, Meilensteine | YAML-Format, editierbar |
| **Lehrer-Dashboard** | Visualisiert Fortschritt, Interaktionen | Analytics-View (optional) |

### System-Prompt-Struktur

```yaml
role: "pädagogischer Tutor"
personality: "geduldig, ermutigend, sokratisch"
constraints:
  - "Gib keine fertigen Lösungen"
  - "Passe Detailgrad an Wissensstand an"
  - "Stelle Fragen, die zum Nachdenken anregen"
  - "Feiere Erfolge"
context_sources:
  - ".copilot/project-spec.yaml"
  - "Chat-Historie"
  - "Aktueller Code"
  - "Fehler-Logs"
```

---

## 📚 Integration in Bestehendes Framework

Dieses Modell erweitert das bestehende `.copilot/`-Framework:

- **phase-prompts.md** → Nutzt 4-Phasen-Zyklus für detaillierte Prompts
- **conversation-patterns.md** → Implementiert Koaktivitäts-Patterns
- **assessment-guide.md** → Verwendet Diagnostik-Indikatoren
- **project-spec-template.yaml** → Strukturiert Projekte nach Phasen

---

## 🎓 Pädagogischer Mehrwert

| Kategorie | Nutzen |
|-----------|--------|
| **Motivation** | Eigenverantwortung durch selbstgewählte Projekte |
| **Individualisierung** | Echtzeit-Anpassung der Unterstützung an Lernniveau |
| **Transparenz** | Alle Lernschritte nachvollziehbar (Chat + Code) |
| **Kompetenz** | Fördert Computational Thinking, Metakognition, Medienkompetenz |
| **Ethik** | Kritische Auseinandersetzung mit KI (Bias, Grenzen, Halluzinationen) |
| **Skalierbarkeit** | Ein Copilot kann viele Lernende individuell unterstützen |

---

## 🚀 Ausblick & Skalierung

Dieses Modell ist anwendbar auf:

1. **Schulischer Informatikunterricht** (ab Klasse 5)
   - KI-gestützte Projektwochen
   - AG-Bereich, Wahlpflicht

2. **Berufliche Bildung / HTL**
   - Agile Lernprojekte
   - Copilot als Team-Assistent

3. **Universitäre Lehre**
   - Tutorium für Software-Engineering-Grundlagen
   - Flipped Classroom mit KI-Support

4. **Selbstlernen / MOOCs**
   - Individualisierte Lernpfade
   - 24/7 verfügbarer Mentor

---

## 📖 Literatur & Theoretische Fundierung

- **Polya, G.** (1945): *How to Solve It* - Problemlösungsmethodik
- **Vygotsky, L.** (1978): *Zone of Proximal Development* - Scaffolding-Theorie
- **Collins, A. et al.** (1989): *Cognitive Apprenticeship* - Lernen durch Modeling
- **Hubwieser, P.** (2007): *Didaktik der Informatik* - Modellierung als Kernkompetenz
- **Wing, J.** (2006): *Computational Thinking* - Denkweisen der Informatik
- **GI-Bildungsstandards Informatik** - Kompetenzorientierung

---

**Version:** 1.0  
**Datum:** 2025-11-03  
**Status:** Aktiv - Integration in `.copilot/` Framework
