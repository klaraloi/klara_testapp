# Informatik-Didaktik für den Programmierunterricht

> Basierend auf deutschsprachigen Didaktik-Konzepten und Best Practices

## Übersicht

Dieses Dokument integriert bewährte Konzepte der Informatik-Didaktik in unser Project-Based Learning Framework. Es kombiniert **Angeleitetes Programmieren**, **Agile Methoden** und moderne pädagogische Ansätze.

## 📚 Didaktische Grundprinzipien

### 1. **Programmieren lernt man nur durch Programmieren**

**Kernaussage**: Programmierkompetenz kann nur durch **aktives Üben** erworben werden.

**Problem**:
- ❌ Unmotiviertes Erlernen von Sprachelem

enten
- ❌ "Friss-oder-Stirb"-Aufgaben ohne Anleitung
- ❌ Reine Theorie ohne Praxis

**Lösung**:
- ✅ **Angeleitetes Programmieren**
- ✅ Kurzschrittige, klare Forderungen
- ✅ Konstruktionsanleitungen
- ✅ Sofortiges Feedback

### 2. **Interaktive Arbeitsblätter**

**Konzept**: Multimediale Dokumente mit ausführbarem Code

**Komponenten**:
1. **Code-Boxen** - Programmbausteine zum Experimentieren
2. **Ausführen-Boxen** - "Diagnosestecker" zum Testen
3. **Check-Boxen** - Automatisches Feedback für Testfälle

**Umsetzung in unserem Framework**:
```markdown
# In Jupyter Notebooks oder interaktiven Tutorials

## Schritt 1: Funktion definieren
```python
def berechne_quadrat(zahl):
    # TODO: Vervollständige die Funktion
    return zahl * zahl
```

## Teste deine Funktion:
```python
# Test 1: berechne_quadrat(4) sollte 16 ergeben
assert berechne_quadrat(4) == 16, "Test fehlgeschlagen!"
print("✅ Test bestanden!")
```
```

### 3. **Modularer Aufbau & Test-Driven Development**

**Prinzip**: 
- Entwickle Programmbausteine separat
- Teste sie **bevor** sie ins Gesamtprogramm integriert werden
- Vermeide Seiteneffekte

**Best Practice**:
```python
# ❌ Monolithisches Programm - schwer zu testen
def mache_alles():
    zahl = int(input("Zahl: "))
    if zahl > 0:
        ergebnis = zahl * zahl
        print(f"Quadrat: {ergebnis}")
    else:
        print("Fehler!")

# ✅ Modularer Ansatz - leicht zu testen
def ist_positiv(zahl):
    """Prüft, ob Zahl positiv ist"""
    return zahl > 0

def berechne_quadrat(zahl):
    """Berechnet das Quadrat"""
    return zahl * zahl

def zeige_ergebnis(ergebnis):
    """Gibt Ergebnis aus"""
    print(f"Quadrat: {ergebnis}")

# Tests:
assert ist_positiv(5) == True
assert ist_positiv(-3) == False
assert berechne_quadrat(4) == 16
```

## 🔧 Agile Methoden im Unterricht

### Methode 1: Daily Standup

**Herkunft**: Agile Softwareentwicklung (Scrum)

**Ablauf**:
1. Alle Schüler:innen treffen sich vorne (im Stehen!)
2. **5-10 Minuten** am Stundenbeginn
3. Besprechung: Was passiert heute?
4. Lehrkraft zeigt Demo oder gibt Tipps

**Vorteile**:
- ✅ Schüler:innen können sich nicht hinter Monitoren verstecken
- ✅ Login-Fenster lenken nicht ab
- ✅ Alle sind fokussiert und wissen, was zu tun ist
- ✅ Kurze Meetings (Stehen ist unbequem 😊)

**Umsetzung**:
```markdown
## Daily Standup Routine

### Zu Beginn jeder Stunde:
1. **Sammeln** (1 Min): Alle stehen vorne
2. **Ziel** (2 Min): Was bauen wir heute?
3. **Demo** (3 Min): Zeige Beispiel oder Tipp
4. **Fragen** (2 Min): Kurze Klärungen
5. **Los geht's**: Zurück an die Rechner

### Beispiel-Ablauf:
**Lehrer**: "Heute programmieren wir die Highscore-Funktion. 
Schaut, so soll es aussehen [zeigt Demo]. 
Ihr braucht: Liste für Punkte, sort()-Funktion, und Ausgabe.
Fragen?"
```

### Methode 2: Pair Programming

**Prinzip**: Zwei Personen, ein Computer

**Rollen**:
- **Driver** (Fahrer): Tippt am Computer
- **Navigator** (Navigator): Denkt mit, gibt Anweisungen

**Regeln**:
- 🔄 Wechsel alle **15 Minuten**
- 💬 Beide denken aktiv mit
- 🗣️ Kommunikation ist essentiell
- ✅ Höhere Code-Qualität, weniger Fehler

**Umsetzung**:
```markdown
## Pair Programming Setup

### Vorbereitung:
1. 2er-Teams bilden (wechselnde Zusammensetzung!)
2. Ein Computer, ein Monitor
3. Timer auf 15 Minuten stellen

### Während der Arbeit:
**Navigator sagt z.B.:**
- "Lass uns eine Funktion für XY schreiben"
- "Hast du daran gedacht, den Fall zu prüfen?"
- "Vielleicht können wir hier eine Schleife nutzen?"

**Driver**:
- Tippt und führt aus
- Stellt Fragen: "Meinst du so?"
- Macht Vorschläge

### Nach 15 Minuten:
🔔 Timer klingelt → **Rollentausch!**
```

**Vorteile für Schüler:innen**:
- Lernen voneinander
- Können Probleme oft selbst lösen
- Verbesserte Kommunikationsfähigkeit
- Teamarbeit üben

### Methode 3: Review

**Prinzip**: Gemeinsame Ergebnispräsentation und Reflexion

**Ablauf**:
- ⏰ **10 Minuten** am Stundenende
- 🏆 Schüler:innen präsentieren Ergebnisse
- 💭 Erklären Lösungswege
- 🎉 Erfolge feiern

**Review-Struktur**:
```markdown
## Review am Stundenende

### 1. Sammeln (1 Min)
Alle mit ihren Ergebnissen nach vorne

### 2. Präsentationen (6 Min)
- 2-3 Teams stellen vor (rotierend)
- "Was haben wir gebaut?"
- "Wie haben wir es gelöst?"
- "Was war schwierig?"

### 3. Diskussion (2 Min)
- Andere stellen Fragen
- Vergleichen Lösungsansätze

### 4. Ausblick (1 Min)
- "Was machen wir nächstes Mal?"
- "Wer will sein Projekt erweitern?"

### Wichtig:
- Auch wenn etwas **nicht funktioniert** → vorstellen!
- "Bei mir läuft's nicht" gehört dazu
- Gemeinsam Probleme analysieren
```

**Vorteile**:
- Lernen von anderen Lösungswegen
- Präsentationsfähigkeit üben
- Erfolge sichtbar machen
- Gemeinsames Problemlösen

## 🎯 Integration in unser Framework

### Stunden-Struktur

```
┌─────────────────────────────────────────────┐
│ 1. Daily Standup (5-10 Min)                │
│    - Ziel der Stunde                        │
│    - Demo/Tipps                             │
│    - Fragen klären                          │
├─────────────────────────────────────────────┤
│ 2. Arbeitsphase (30-35 Min)                │
│    - Pair Programming (optional)            │
│    - Angeleitetes Programmieren             │
│    - Copilot als Tutor                      │
│    - Lehrkraft zirkuliert und hilft         │
├─────────────────────────────────────────────┤
│ 3. Review (10 Min)                          │
│    - Ergebnisse präsentieren                │
│    - Diskussion                             │
│    - Ausblick                               │
└─────────────────────────────────────────────┘
```

### Kombination mit GitHub Copilot

**Copilot als "virtueller Navigator"**:

```markdown
## Pair Programming mit Copilot

### Variante 1: Schüler + Copilot
- Schüler:in ist Driver
- Copilot ist virtueller Navigator
- Gibt Vorschläge und Erklärungen

### Variante 2: 2 Schüler:innen + Copilot
- Wechselnde Driver/Navigator
- Copilot als zusätzliche Hilfe
- Diskussion über Copilot-Vorschläge

### Wichtig:
Copilot-Vorschläge immer **verstehen**!
- "Warum schlägt Copilot das vor?"
- "Was macht dieser Code?"
- "Gibt es andere Lösungen?"
```

## 📝 Angeleitetes Programmieren - Praktische Umsetzung

### Schritt-für-Schritt Konstruktion

**Beispiel: Zahlen-Ratespiel**

```markdown
# Lektion: Zahlen-Ratespiel

## Meilenstein 1: Zufallszahl generieren

### Aufgabe 1.1: Import
Importiere das random-Modul:
```python
import random
```

### Aufgabe 1.2: Zufallszahl
Erstelle eine Variable für eine Zufallszahl zwischen 1 und 100:
```python
geheime_zahl = random.randint(1, 100)
print(f"Zum Testen: {geheime_zahl}")  # Später entfernen!
```

✅ **Check**: Führe den Code mehrmals aus. Ändert sich die Zahl?

---

## Meilenstein 2: Benutzereingabe

### Aufgabe 2.1: Eingabe abfragen
```python
versuch = int(input("Rate die Zahl (1-100): "))
```

✅ **Check**: Funktioniert die Eingabe? Was passiert bei Buchstaben?

### Aufgabe 2.2: Eingabe validieren
```python
if versuch < 1 or versuch > 100:
    print("Bitte nur Zahlen zwischen 1 und 100!")
else:
    # Hier später den Vergleich
    print(f"Du hast {versuch} geraten")
```

✅ **Test**: Probiere Werte außerhalb 1-100!

---

## Meilenstein 3: Vergleich

### Aufgabe 3.1: Überprüfung
Füge die Vergleichslogik hinzu:
```python
if versuch == geheime_zahl:
    print("🎉 Richtig!")
elif versuch < geheime_zahl:
    print("📉 Zu niedrig")
else:
    print("📈 Zu hoch")
```

✅ **Check**: Teste alle drei Fälle!
```

### Interaktive Checkpoints

**Automatische Tests in Notebooks**:

```python
# Test-Funktion (versteckt in Template)
def teste_funktion(funktion, testfaelle):
    """Testet eine Funktion mit gegebenen Fällen"""
    erfolge = 0
    for eingabe, erwartet in testfaelle:
        ergebnis = funktion(eingabe)
        if ergebnis == erwartet:
            print(f"✅ Test {eingabe} → {ergebnis}")
            erfolge += 1
        else:
            print(f"❌ Test {eingabe} → {ergebnis}, erwartet: {erwartet}")
    
    print(f"\n{erfolge}/{len(testfaelle)} Tests bestanden")
    return erfolge == len(testfaelle)

# Nutzung durch Schüler:in
def meine_funktion(x):
    return x * 2

# Automatischer Test
teste_funktion(meine_funktion, [
    (2, 4),
    (5, 10),
    (0, 0),
    (-3, -6)
])
```

## 🧩 Mikrowelten & Lernumgebungen

### Bekannte Systeme (Referenz)

**Mikrowelten**:
- 🐹 **Hamster-Modell**: Hamster sammelt Körner
- 🐢 **Turtle Graphics**: Zeichnen mit Schildkröte
- 🤖 **Karel the Robot**: Roboter in Gitterwelt

**Entwicklungsumgebungen**:
- 💙 **BlueJ**: OOP-Lernsystem
- 🍀 **Greenfoot**: Game-basierte Umgebung
- 🎨 **Scratch**: Visuelle Programmierung (Klasse 4-7)
- 📱 **App Inventor**: Android-Apps (Klasse 8-12)

### Integration in unser Framework

**Altersstufen-Empfehlung**:

```
Alter 8-10:  Scratch, Calliope mini
             → Grafische Programmierung
             → Spielerischer Einstieg

Alter 11-13: Scratch, Python (Turtle)
             → Übergang zur Textsprache
             → Einfache Projekte

Alter 14-16: Python, JavaScript, App Inventor
             → Echte Programmiersprachen
             → Web/Mobile Apps

Alter 17+:   Full-Stack Projekte
             → Professional Tools
             → Complex Applications
```

## 📋 Checklisten für Lehrkräfte

### Vorbereitung einer Unterrichtsstunde

```markdown
## Vor der Stunde:

### Inhaltlich:
- [ ] Lernziel klar definiert
- [ ] Meilenstein in überschaubare Schritte zerlegt
- [ ] Beispiel-Code vorbereitet
- [ ] Testfälle überlegt

### Daily Standup:
- [ ] Demo vorbereitet (2-3 Min)
- [ ] Tipps/Tricks notiert
- [ ] Häufige Fehler antizipiert

### Arbeitsphase:
- [ ] Pair-Programming Teams (falls genutzt)
- [ ] Copilot-Instruktionen aktuell
- [ ] Hilfestellung geplant

### Review:
- [ ] 2-3 Teams für Präsentation ausgewählt
- [ ] Diskussionsfragen vorbereitet
```

### Während der Stunde

```markdown
## Beobachtungsbogen:

### Technische Probleme:
- [ ] Alle können Code ausführen?
- [ ] Login-Probleme?
- [ ] Tools funktionieren?

### Lernfortschritt:
- [ ] Verstehen alle das Ziel?
- [ ] Kommen alle mit?
- [ ] Wer braucht Extra-Hilfe?

### Zusammenarbeit:
- [ ] Funktioniert Pair Programming?
- [ ] Kommunizieren die Teams?
- [ ] Hilft man sich gegenseitig?

### Notizen für nächstes Mal:
- Was lief gut?
- Was muss angepasst werden?
- Welche Fehler traten häufig auf?
```

## 🎓 Didaktische Entscheidungen

### Wann welche Methode?

| Situation | Empfohlene Methode |
|-----------|-------------------|
| Neue Konzepte einführen | Daily Standup + Demo |
| Übungsphase | Pair Programming |
| Komplexe Aufgaben | Angeleitetes Programmieren |
| Fehlersuche | Pair Programming |
| Abschluss Meilenstein | Review |
| Projektarbeit | Einzelarbeit oder 2er-Teams |
| Assessment | Einzelarbeit |

### Schwierigkeitsgrad anpassen

**Differenzierung**:

```markdown
## Aufgabe: Liste sortieren

### Level 1 (Anfänger):
Nutze die sort()-Funktion:
```python
zahlen = [5, 2, 8, 1, 9]
zahlen.sort()
print(zahlen)
```

### Level 2 (Fortgeschritten):
Implementiere Bubble Sort:
```python
def bubble_sort(liste):
    # TODO: Implementiere Bubble Sort
    pass
```

### Level 3 (Expert):
Implementiere Quicksort rekursiv:
```python
def quicksort(liste):
    # TODO: Implementiere Quicksort
    pass
```

**Alle Levels haben dasselbe Lernziel**: Verstehen, wie Sortierung funktioniert
```

## 🔄 Iterativer Lernprozess

### Der Lernzyklus

```
1. Verstehen
   ↓
2. Anwenden (mit Anleitung)
   ↓
3. Üben (mit Variationen)
   ↓
4. Transfer (auf neue Probleme)
   ↓
5. Reflektieren
   ↓
[zurück zu 1 mit neuem Konzept]
```

### Praktisches Beispiel: If-Bedingungen lernen

```markdown
## Phase 1: Verstehen (10 Min)
- Konzept: Entscheidungen im Code
- Alltags-Beispiel: "Wenn Ampel rot, dann stopp"
- Syntax-Erklärung

## Phase 2: Anwenden (15 Min)
- Geführtes Beispiel: Alterscheck
- Schüler:innen ergänzen Lücken
- Sofortiges Feedback

## Phase 3: Üben (20 Min)
- Variationen: Notenberechnung, Rabatt-System
- Pair Programming
- Eigene Ideen willkommen

## Phase 4: Transfer (20 Min)
- Neue Problemstellung: Quiz-Spiel
- Selbstständige Anwendung
- Copilot als Hilfe

## Phase 5: Reflektieren (10 Min)
- Review: Was haben wir gelernt?
- Wo wird es genutzt?
- Was war schwierig?
```

## 📚 Für Informatik-Didaktik Interessierte

### Weiterführende Konzepte

**Konstruktivismus**:
- Lernen als aktiver Konstruktionsprozess
- Vorwissen aktivieren
- Anknüpfungspunkte schaffen

**Scaffolding** (Gerüstbau):
- Temporäre Hilfestellung
- Schrittweise zurückziehen
- Selbstständigkeit fördern

**Cognitive Apprenticeship**:
- Experte demonstriert
- Lernende imitieren
- Schritt für Schritt selbstständiger

**Mastery Learning**:
- Beherrschung vor Fortsetzung
- Individuelles Tempo
- Rückmeldung und Korrektur

### Wie unser Framework diese umsetzt

| Konzept | Umsetzung |
|---------|-----------|
| Konstruktivismus | Projektbasiertes Lernen, eigene Ideen |
| Scaffolding | Copilot's 3-Stufen-Hilfe, Templates |
| Cognitive Apprenticeship | Daily Standup Demos, Pair Programming |
| Mastery Learning | Self-Assessment, individuelles Tempo |

## 🌟 Zusammenfassung

### Die didaktische Formel

```
Angeleitetes Programmieren
    +
Agile Methoden (Daily Standup, Pair Programming, Review)
    +
Projektbasiertes Lernen
    +
AI-Unterstützung (GitHub Copilot)
    =
Effektiver, motivierender Programmierunterricht
```

### Kernelemente

1. ✅ **Aktives Tun** statt passivem Zuhören
2. ✅ **Kleine Schritte** mit Feedback
3. ✅ **Modularer Aufbau** und Tests
4. ✅ **Agile Rituale** für Struktur
5. ✅ **Zusammenarbeit** fördern
6. ✅ **Echte Projekte** als Motivation
7. ✅ **Moderne Tools** nutzen
8. ✅ **Individuelles Tempo** ermöglichen

---

**Quellen**:
- [Angeleitetes Programmieren (ProgrammingWiki)](https://programmingwiki.de/Angeleitetes_Programmieren)
- [Programmieren in der Schule (meinUnterricht.de)](https://www.meinunterricht.de/blog/programmieren-schule-unterricht/)
- Informatik-Didaktik Fachliteratur
- Agile Software Development Praktiken

**Letzte Aktualisierung**: November 2025
