# Didaktische Methoden & Praxisbeispiele

## Überblick

Diese Datei sammelt **konkrete, erprobte Methoden** und **anschauliche Analogien** für den projektbasierten Programmierunterricht mit KI-Copilot. Sie ergänzt das theoretische Framework mit unmittelbar anwendbaren Werkzeugen.

---

## 🎯 Zielgruppe

- **Lehrer/Dozenten:** Konkrete Unterrichtsmethoden
- **Copilot "Kai":** Methodenrepertoire für adaptive Unterstützung
- **Curriculum-Designer:** Praxisnahe Umsetzungsideen

---

## 📋 Inhaltsverzeichnis

1. [Fragetechniken](#1-fragetechniken)
2. [Didaktische Analogien](#2-didaktische-analogien)
3. [Modellierungsmethoden](#3-modellierungsmethoden)
4. [Code-Verstehensmethoden](#4-code-verstehensmethoden)
5. [Debugging-Strategien](#5-debugging-strategien)
6. [Reflexionsmethoden](#6-reflexionsmethoden)

---

## 1. Fragetechniken

### 1.1 **Prompt-a-thon** (Requirement Elicitation)

**Zweck:** Vage Projektideen in konkrete Anforderungen überführen

**Methode:** Strukturierte Fragestrategie in 3 Ebenen

#### **Ebene 1: Problem verstehen (Polya-Methode)**

```
Fragen des Copiloten:
1. "Was ist BEKANNT?" 
   → Gegenwärtiger Zustand, vorhandene Ressourcen
   
2. "Was ist GESUCHT?"
   → Gewünschtes Ergebnis, Zielzustand
   
3. "Welche BEDINGUNGEN müssen erfüllt sein?"
   → Einschränkungen, Regeln, Anforderungen
```

**Beispiel-Dialog:**

```
Kind: "Ich will ein Programm für meine Hausaufgaben machen."

Copilot: "Cool! Lass uns das genauer anschauen:
1. Was ist BEKANNT? Welche Hausaufgaben hast du? Wie machst du sie jetzt?
2. Was ist GESUCHT? Was soll das Programm können? Was wäre anders/besser?
3. Welche BEDINGUNGEN? Muss es auf dem Handy laufen? Mit Erinnerungen?"
```

#### **Ebene 2: Funktionen konkretisieren**

```
4. "Wer wird das Programm nutzen?" (User Personas)
5. "Was passiert, wenn...?" (Use Cases durchspielen)
6. "Was soll NICHT passieren?" (Fehlerfälle, Grenzen)
7. "Wann ist es fertig?" (Definition of Done)
```

#### **Ebene 3: Technische Details**

```
8. "Welche EINGABEN braucht das Programm?"
9. "Welche AUSGABEN soll es produzieren?"
10. "Müssen Daten gespeichert werden?"
```

**Output:** Strukturierte Anforderungsspezifikation → `project-spec.yaml`

**Didaktischer Wert:**
- ✅ Schult Problemformulierung
- ✅ Fördert systematisches Denken
- ✅ Reduziert Ambiguität
- ✅ Basis für realistische Planung

---

### 1.2 **5-Why-Debugging**

**Zweck:** Fehlerursachen systematisch aufdecken

**Methode:** Fünfmaliges "Warum?" fragen

**Beispiel:**

```
Fehler: "Das Programm stürzt ab."

Warum? → "Weil eine Fehlermeldung kommt."
Warum? → "Weil die Liste leer ist."
Warum? → "Weil keine Daten geladen wurden."
Warum? → "Weil die Datei nicht existiert."
Warum? → "Weil der Dateiname falsch geschrieben ist."

→ ROOT CAUSE: Tippfehler im Dateinamen
```

**Copilot-Prompt:**
```
"Lass uns gemeinsam herausfinden, WARUM das passiert:
1. Was genau passiert? (Symptom)
2. Warum passiert das? (Nächste Ebene)
3. Und warum passiert DAS? (Tiefer graben)
..."
```

---

### 1.3 **Socratic Code Review**

**Zweck:** Verständnis prüfen ohne direkt zu korrigieren

**Methode:** Leitfragen statt Lösungen

**Frage-Templates:**

```
Verständnis prüfen:
• "Was macht diese Zeile?"
• "Warum hast du diesen Datentyp gewählt?"
• "Was passiert, wenn X statt Y eingegeben wird?"

Zum Nachdenken anregen:
• "Gibt es einen kürzeren Weg?"
• "Was würde passieren, wenn wir die Reihenfolge ändern?"
• "Könnte das bei großen Datenmengen zum Problem werden?"

Alternativen erkunden:
• "Welche anderen Ansätze kennst du?"
• "Was wären Vor- und Nachteile von...?"
• "Wie würdest du es machen, wenn...?"
```

**Beispiel:**

```python
# Kind schreibt:
for i in range(len(liste)):
    print(liste[i])

# Copilot fragt (statt zu korrigieren):
"Super, das funktioniert! 
Eine Frage: Was genau macht `range(len(liste))`? 
Und: Brauchst du den Index `i` wirklich, oder nur die Werte?"

# → Kind entdeckt selbst: for item in liste: print(item)
```

---

## 2. Didaktische Analogien

### 2.1 **LEGO-System-Analogie** ⭐

**Zweck:** KI-Koaktivität anschaulich erklären

**Metapher:**

> Programmieren mit KI-Copilot ist wie **LEGO bauen mit einem digitalen Bauleiter**.

| LEGO-Rolle | Programmier-Äquivalent | Wer macht's |
|------------|------------------------|-------------|
| **Architekt** | Projektidee entwickeln | Kind |
| **Bauplan erstellen** | Anforderungen + Modell | Kind mit Copilot-Hilfe |
| **Spezielle Steine sortieren** | Algorithmus entwerfen | Kind |
| **Standard-Verbinder liefern** | Boilerplate-Code | Copilot |
| **Komplexe Mechanik bauen** | Kernlogik implementieren | Kind |
| **Stabilität prüfen** | Testen & Debuggen | Kind + Copilot |
| **Bauanleitung schreiben** | Dokumentation | Kind |

**Kern-Aussage:**
```
"Die KI ist NICHT der Baumeister, der dein LEGO-Modell baut.
Sie ist der Bauleiter, der:
- Fragt: 'Soll es Räder haben? Wie groß?'
- Die Standardteile (Platten, Achsen) bereitstellt
- Prüft: 'Hält das stabil?'

DU entwirfst, was gebaut wird.
DU baust die wichtigen, coolen Teile.
DU entscheidest, ob es gut ist."
```

**Lernfortschritt in der Analogie:**

```
Anfänger: "Wie verbinde ich zwei LEGO-Steine?" 
          → Lernt Grundmechanik

Fortgeschritten: "Ich baue ein Auto mit Lenkung!"
                  → Entwirft komplexe Systeme

Erfahren: "Ich optimiere das Getriebe für Geschwindigkeit."
          → Versteht Trade-offs
```

---

### 2.2 **Koch-Rezept-Analogie**

**Zweck:** Algorithmen und Syntax verständlich machen

**Metapher:**

| Programmier-Konzept | Koch-Äquivalent |
|---------------------|-----------------|
| **Algorithmus** | Rezept (Schritt-für-Schritt-Anleitung) |
| **Variablen** | Zutaten-Behälter |
| **Datentypen** | Zutatensorten (Mehl=String, Anzahl Eier=Integer) |
| **Funktionen** | Zubereitungsschritte (schneiden, rühren, backen) |
| **If-Bedingung** | "Falls Teig zu fest → Milch hinzufügen" |
| **Schleife** | "Rühre, BIS glatt" |
| **Debugging** | Schmeckt's? Fehlt Salz? |

**Beispiel:**

```python
# Algorithmus: Pfannkuchen backen

zutaten = ["Mehl", "Eier", "Milch"]  # Variablen
anzahl_pfannkuchen = 0                # Counter

for zutat in zutaten:                 # Schleife
    if zutat not in kühlschrank:      # Bedingung
        print("Fehlt:", zutat)
        
def backe_pfannkuchen(teig):          # Funktion
    if teig.konsistenz == "zu_fest":  # Bedingung
        teig.add("Milch")
    return pfannkuchen
```

---

### 2.3 **Dirigent-Orchester-Analogie**

**Zweck:** Objektorientierung erklären

**Metapher:**

```
Programm = Symphonie
Objekte = Musiker
Klassen = Instrumentengruppen
Methoden = Spieltechniken
Nachrichten = Dirigenten-Signale
```

**Beispiel:**

```python
# Klasse = Violinen-Sektion
class Violine:
    def __init__(self, name):
        self.name = name
        self.ton = None
    
    def spiele(self, note):  # Methode
        self.ton = note
        print(f"{self.name} spielt {note}")

# Objekte = Einzelne Violinen
violine1 = Violine("Erste Geige")
violine2 = Violine("Zweite Geige")

# Dirigent (Hauptprogramm) gibt Signal
violine1.spiele("A")
violine2.spiele("E")
```

**Didaktischer Wert:**
- ✅ Macht Abstraktion greifbar
- ✅ Erklärt Klassen vs. Objekte
- ✅ Zeigt Kapselung (jede Violine hat eigenen Zustand)

---

## 3. Modellierungsmethoden

### 3.1 **Think-Pair-Program** (für Gruppen)

**Ablauf:**

1. **Think (3 min):** Jedes Kind skizziert Lösungsidee allein
2. **Pair (5 min):** Zu zweit Ideen austauschen, beste wählen
3. **Program (15 min):** Gemeinsam mit Copilot implementieren

**Variante für Einzelarbeit: Think-Ask-Program**
- Think → Ask Copilot → Program

---

### 3.2 **Story-Mapping für Use Cases**

**Methode:** Programm-Funktionen als User-Story erzählen

**Template:**

```
Als [USER]
möchte ich [AKTION]
damit [NUTZEN].

Akzeptanzkriterien:
- Gegeben: [KONTEXT]
- Wenn: [EREIGNIS]
- Dann: [ERWARTETES ERGEBNIS]
```

**Beispiel:**

```
Als Schüler
möchte ich meine erledigten Hausaufgaben abhaken
damit ich den Überblick behalte.

Akzeptanzkriterien:
- Gegeben: Ich habe eine Liste mit Hausaufgaben
- Wenn: Ich klicke auf eine Hausaufgabe
- Dann: Sie wird als "erledigt" markiert und durchgestrichen
```

**Copilot-Rolle:** Hilft, Story in Anforderungen zu übersetzen

---

### 3.3 **CRC-Karten für OOP** (Class-Responsibility-Collaborator)

**Zweck:** Objektorientierte Modelle greifbar machen

**Methode:** Physische Karteikarten (oder digital)

```
┌─────────────────────────────────┐
│ Klasse: Hausaufgabe             │
├─────────────────────────────────┤
│ Verantwortlichkeiten:           │
│ • Titel speichern               │
│ • Fälligkeit merken             │
│ • Status ändern (offen/erledigt)│
├─────────────────────────────────┤
│ Kollaboriert mit:               │
│ • HausaufgabenListe             │
│ • Erinnerung                    │
└─────────────────────────────────┘
```

**Aktivität:** Kind erstellt CRC-Karten für Hauptobjekte → Copilot übersetzt in Klassengerüst

---

### 3.4 **Zustandsdiagramme mit Emojis** 🎨

**Zweck:** Programmzustände visuell darstellen

**Beispiel: Ampel-Programm**

```
     START
       ↓
   🔴 ROT (3 sek)
       ↓
   🟡 GELB (1 sek)
       ↓
   🟢 GRÜN (3 sek)
       ↓
   🟡 GELB (1 sek)
       ↓
   (zurück zu ROT)
```

**Copilot-Unterstützung:** Übersetzt Diagramm in State-Machine-Code

---

## 4. Code-Verstehensmethoden

### 4.1 **Code-Leseprotokoll** (für Anfänger)

**Methode:** Zeile für Zeile den Code "übersetzen"

**Template:**

```python
# CODE:
for i in range(5):
    print(i * 2)

# LESEPROTOKOLL (Kind füllt aus):
Zeile 1: "Starte eine Schleife, die 5 Mal läuft"
         "i startet bei 0 und geht bis 4"
         
Zeile 2: "In jeder Runde:"
         "Nimm die aktuelle Zahl i"
         "Multipliziere sie mit 2"
         "Zeige das Ergebnis an"

Erwartete Ausgabe:
0
2
4
6
8
```

**Didaktischer Wert:**
- ✅ Zwingt zu Zeile-für-Zeile-Analyse
- ✅ Deckt Missverständnisse auf
- ✅ Schult Tracing-Fähigkeit

---

### 4.2 **Rubber-Duck-Debugging** (mit Copilot)

**Methode:** Dem Copilot den Code erklären (als wäre er eine Gummi-Ente)

**Prompt:**

```
"Kai, ich erkläre dir jetzt meinen Code:

[Kind erklärt Zeile für Zeile]

Habe ich etwas vergessen oder falsch erklärt?"
```

**Effekt:** Beim Erklären findet das Kind oft selbst den Fehler

---

### 4.3 **Code-Kommentar-Challenge**

**Methode:** Copilot liefert Code OHNE Kommentare → Kind ergänzt sie

**Beispiel:**

```python
# Copilot liefert:
def mystery(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

# Kind ergänzt Kommentare:
def mystery(n):
    r = 1  # Startwert für das Ergebnis
    for i in range(1, n+1):  # Zähle von 1 bis n
        r *= i  # Multipliziere r mit aktueller Zahl
    return r  # Gib Ergebnis zurück
    
# → Kind erkennt: "Ah, das ist Fakultät!"
```

---

## 5. Debugging-Strategien

### 5.1 **STOP-Methode**

**Akronym:** Systematisch Fehler finden

- **S**ymptom: Was passiert genau?
- **T**heorie: Was könnte die Ursache sein?
- **O**bservation: Beobachte (print, Debugger)
- **P**roven: Teste die Theorie, fixe, validiere

**Copilot-Einsatz:**

```
"Lass uns STOP anwenden:

S - Symptom: Beschreibe genau, was falsch läuft.
T - Theorie: Was glaubst du, woran es liegt?
O - Observation: Fügen wir print() ein, um zu schauen?
P - Proven: Probiere die Lösung aus!"
```

---

### 5.2 **Binary-Search-Debugging**

**Methode:** Code halbieren, um Fehlerbereich einzugrenzen

**Ablauf:**

```
1. Kommentiere HÄLFTE des Codes aus
2. Läuft es jetzt?
   → JA: Fehler war im auskommentierten Teil
   → NEIN: Fehler ist im aktiven Teil
3. Wiederhole mit kleinerer Hälfte
```

**Beispiel:**

```python
# ORIGINAL (Fehler irgendwo):
print("Start")
x = get_input()      # Teil A
y = process(x)       # Teil A
z = calculate(y)     # Teil B
result = output(z)   # Teil B
print("Ende")

# SCHRITT 1: Kommentiere B aus
print("Start")
x = get_input()
y = process(x)
# z = calculate(y)
# result = output(z)
print("Ende")

# Läuft? → JA → Fehler in Teil B
# → Weiter halbieren: calculate oder output?
```

---

### 5.3 **Debug-Print-Strategie**

**Methode:** Strategisch `print()` einsetzen

**Best Practices:**

```python
# ❌ SCHLECHT:
print(x)

# ✅ GUT:
print(f"DEBUG: x nach Berechnung = {x}")
print(f"DEBUG: Liste hat {len(items)} Elemente")
print(f"DEBUG: Schleife Runde {i}, Wert = {value}")
```

**Copilot-Prompt:**
```
"Wo sollte ich print() einbauen, um zu sehen, was passiert?"
```

---

## 6. Reflexionsmethoden

### 6.1 **Dev-Log mit Leitfragen**

**Zweck:** Metakognitive Reflexion strukturieren

**Template (nach jeder Session):**

```markdown
## Dev-Log: [Datum]

### 🎯 Heute geplant:
- [ ] Aufgabe 1
- [ ] Aufgabe 2

### ✅ Heute geschafft:
- [x] Was ich umgesetzt habe...

### 💡 Gelernt:
- Neues Konzept: ...
- Aha-Moment: ...

### 🐛 Probleme & Lösungen:
- Problem: ...
- Gelöst durch: ...

### 🤔 Offene Fragen:
- Was ich noch nicht verstehe: ...

### 🔄 Nächste Schritte:
- Morgen will ich: ...

### 🤖 KI-Nutzung:
- Copilot half bei: ...
- Ich machte selbst: ...
```

---

### 6.2 **Think-Aloud Protocol**

**Methode:** Kind spricht laut, während es programmiert

**Beispiel:**

```
Kind (laut denkend): 
"Okay, ich brauche eine Liste für die Hausaufgaben...
Hmm, wie macht man das nochmal?
Ah ja, eckige Klammern: hausaufgaben = []
Jetzt will ich eine hinzufügen...
.append() war das, glaube ich...
hausaufgaben.append('Mathe')
Mal testen... *führt aus*
Ja! Funktioniert!"
```

**Copilot-Rolle:** Hört zu, fragt bei Unsicherheiten nach

---

### 6.3 **Code-Review-Checkliste**

**Methode:** Systematische Selbstprüfung

**Checkliste:**

```
Code-Qualität:
□ Funktioniert der Code? (Tests bestanden)
□ Sind Variablennamen verständlich?
□ Habe ich Kommentare für komplexe Teile?
□ Gibt es Wiederholungen, die ich vermeiden könnte?

Verständnis:
□ Kann ich jede Zeile erklären?
□ Verstehe ich, warum es funktioniert?
□ Weiß ich, was bei Fehleingaben passiert?

Dokumentation:
□ Gibt es eine Beschreibung, was das Programm macht?
□ Sind die Anforderungen erfüllt?
□ Habe ich meinen Lösungsweg dokumentiert?
```

---

### 6.4 **Peer-Explanation** (für Gruppen)

**Methode:** Einem anderen Kind den Code erklären

**Struktur:**

1. **Erklärer:** Zeigt Code, erklärt Idee
2. **Zuhörer:** Stellt Verständnisfragen
3. **Rollentausch**

**Variante Einzelarbeit:** Erkläre Copilot → Copilot spielt "unwissenden Schüler"

---

## 🎓 Methodeneinsatz nach Lernphase

### Phase 1: Anforderungsanalyse
- ✅ Prompt-a-thon
- ✅ Story-Mapping
- ✅ LEGO-Analogie (Projektidee)

### Phase 2: Modellierung
- ✅ CRC-Karten (OOP)
- ✅ Zustandsdiagramme
- ✅ Think-Pair-Program

### Phase 3: Implementation
- ✅ Code-Leseprotokoll
- ✅ Rubber-Duck-Debugging
- ✅ Code-Kommentar-Challenge

### Phase 4: Debugging
- ✅ STOP-Methode
- ✅ Binary-Search-Debugging
- ✅ 5-Why

### Phase 5: Reflexion
- ✅ Dev-Log
- ✅ Code-Review-Checkliste
- ✅ Think-Aloud Protocol

---

## 🔧 Implementierung in Copilot

### Copilot kann Methoden vorschlagen:

```python
# In system-prompt.md oder phase-prompts.md:

"Wenn das Kind Schwierigkeiten hat, die Anforderungen zu formulieren,
nutze die PROMPT-A-THON-Methode aus teaching-methods.md."

"Wenn das Kind OOP lernt, erkläre mit der ORCHESTER-ANALOGIE 
oder nutze CRC-KARTEN."

"Bei Debugging: Führe durch die STOP-METHODE."
```

### Beispiel-Integration:

```yaml
# In project-spec.yaml:
teaching_methods_used:
  - name: "Prompt-a-thon"
    phase: "Anforderungsanalyse"
    date: "2025-03-15"
    
  - name: "LEGO-Analogie"
    phase: "Kickoff"
    effectiveness: "Sehr hilfreich - Kind verstand Rollenverteilung"
```

---

## 📚 Weitere Ressourcen

**Literatur:**
- Polya, G. (1945): *How to Solve It* (Prompt-a-thon-Basis)
- Beck, K. & Cunningham, W. (1989): CRC-Karten (OOP)
- Hunt, A. & Thomas, D.: *The Pragmatic Programmer* (Rubber Duck)

**Learning Paths:**
- `/learning-paths/computational-thinking-basics.md` (Analogien)
- `/learning-paths/debugging-strategies.md` (Debugging-Methoden)

---

## 🎯 Best Practices für Lehrer

### DO ✅
- Wähle Methode passend zur Lernphase
- Variiere Methoden, um verschiedene Lerntypen zu erreichen
- Erkläre WARUM eine Methode hilft
- Lass Kinder Lieblings-Methoden entwickeln

### DON'T ❌
- Erzwinge nicht ALLE Methoden für JEDES Kind
- Überlade nicht mit zu vielen Methoden auf einmal
- Erwarte nicht, dass Methoden sofort perfekt sitzen
- Vergiss nicht, Methoden selbst vorzuleben

---

**Version:** 1.0  
**Letzte Aktualisierung:** November 2025  
**Maintainer:** Projekt-Team "project-based-learning"

---

*Diese Methoden sind lebendig – füge eigene erfolgreiche Ansätze hinzu!* 🌱
