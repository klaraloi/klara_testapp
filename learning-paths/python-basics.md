# Lernpfad: Python Grundlagen

**Zielgruppe:** Anfänger (10-14 Jahre)  
**Dauer:** 6-8 Wochen  
**Voraussetzungen:** Keine

## Übersicht

Dieser Lernpfad führt dich durch die Grundlagen der Python-Programmierung mit praktischen Projekten. Du lernst durch "Learning by Doing" - jedes Konzept wird sofort in einem kleinen Projekt angewendet.

## Lernziele

Am Ende dieses Lernpfads kannst du:
- [ ] Einfache Python-Programme schreiben
- [ ] Mit Variablen und Datentypen arbeiten
- [ ] Kontrollstrukturen (if, loops) verwenden
- [ ] Funktionen erstellen
- [ ] Listen und Dictionaries nutzen
- [ ] Dateien lesen und schreiben
- [ ] Ein eigenes größeres Projekt umsetzen

## Module

### Modul 1: Erste Schritte (Woche 1)

**Konzepte:**
- Python installieren und erste Programme schreiben
- Variablen und Datentypen (String, Integer, Float, Boolean)
- print() und input() Funktionen
- Einfache Berechnungen

**Mini-Projekt:** Taschenrechner
```python
# Ein einfacher Taschenrechner
zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))
operation = input("Operation (+, -, *, /): ")

if operation == "+":
    print(f"Ergebnis: {zahl1 + zahl2}")
# ... weitere Operationen
```

**Übungen:**
1. Erstelle ein Programm, das deinen Namen und dein Alter abfragt
2. Rechne Celsius in Fahrenheit um
3. Berechne die Fläche eines Rechtecks

### Modul 2: Entscheidungen treffen (Woche 2)

**Konzepte:**
- if, elif, else Bedingungen
- Vergleichsoperatoren (==, !=, <, >, <=, >=)
- Logische Operatoren (and, or, not)
- Verschachtelte Bedingungen

**Mini-Projekt:** Zahlen-Ratespiel
```python
import random
geheime_zahl = random.randint(1, 100)
versuch = int(input("Rate die Zahl (1-100): "))

if versuch == geheime_zahl:
    print("Richtig!")
elif versuch < geheime_zahl:
    print("Zu niedrig!")
else:
    print("Zu hoch!")
```

**Übungen:**
1. Erstelle einen Alterscheck (Kind/Jugendlicher/Erwachsener)
2. Notenrechner (Note basierend auf Punktzahl)
3. Einfacher Quiz mit 5 Fragen

### Modul 3: Wiederholungen (Woche 3)

**Konzepte:**
- while-Schleifen
- for-Schleifen
- range() Funktion
- break und continue
- Verschachtelte Schleifen

**Mini-Projekt:** Einmaleins-Trainer
```python
for zahl in range(1, 11):
    print(f"\n=== {zahl}er Reihe ===")
    for multiplikator in range(1, 11):
        ergebnis = zahl * multiplikator
        print(f"{zahl} x {multiplikator} = {ergebnis}")
```

**Übungen:**
1. Countdown-Programm
2. Alle geraden Zahlen von 1-100 ausgeben
3. Passwort-Checker (3 Versuche)

### Modul 4: Listen und Sammlungen (Woche 4)

**Konzepte:**
- Listen erstellen und verwenden
- List-Methoden (append, remove, sort, etc.)
- Listen-Indizes und Slicing
- Listen durchlaufen
- List Comprehensions (Einführung)

**Mini-Projekt:** Einkaufsliste
```python
einkaufsliste = []

while True:
    print("\n1. Artikel hinzufügen")
    print("2. Liste anzeigen")
    print("3. Artikel löschen")
    print("4. Beenden")
    
    wahl = input("Deine Wahl: ")
    
    if wahl == "1":
        artikel = input("Artikel: ")
        einkaufsliste.append(artikel)
    # ... weitere Optionen
```

**Übungen:**
1. Zahlen-Liste sortieren
2. Größte und kleinste Zahl finden
3. Doppelte Einträge entfernen

### Modul 5: Funktionen (Woche 5)

**Konzepte:**
- Funktionen definieren und aufrufen
- Parameter und Argumente
- Return-Werte
- Default-Parameter
- Dokumentation (Docstrings)

**Mini-Projekt:** Würfel-Spiel
```python
import random

def wuerfeln(anzahl_wuerfel=1):
    """Wirft eine bestimmte Anzahl Würfel"""
    ergebnisse = []
    for _ in range(anzahl_wuerfel):
        ergebnisse.append(random.randint(1, 6))
    return ergebnisse

def zeige_ergebnis(wuerfe):
    """Zeigt die Würfelergebnisse an"""
    print(f"Gewürfelt: {wuerfe}")
    print(f"Summe: {sum(wuerfe)}")

# Spiel starten
wuerfe = wuerfeln(2)
zeige_ergebnis(wuerfe)
```

**Übungen:**
1. Funktion für Temperatur-Umrechnung
2. Funktion für Primzahl-Check
3. Passwort-Generator-Funktion

### Modul 6: Dictionaries (Woche 6)

**Konzepte:**
- Dictionaries erstellen und verwenden
- Keys und Values
- Dictionary-Methoden
- Durch Dictionaries iterieren
- Verschachtelte Dictionaries

**Mini-Projekt:** Telefon-Buch
```python
telefon_buch = {}

def kontakt_hinzufuegen(name, nummer):
    telefon_buch[name] = nummer
    print(f"Kontakt {name} hinzugefügt!")

def kontakt_suchen(name):
    if name in telefon_buch:
        return telefon_buch[name]
    return "Nicht gefunden"

def alle_kontakte_anzeigen():
    for name, nummer in telefon_buch.items():
        print(f"{name}: {nummer}")
```

**Übungen:**
1. Wörterbuch Deutsch-Englisch
2. Schüler-Noten verwalten
3. Inventar-System

### Modul 7: Dateien (Woche 7)

**Konzepte:**
- Dateien öffnen und schließen
- Dateien lesen (read, readline, readlines)
- Dateien schreiben (write)
- with-Statement
- JSON-Format

**Mini-Projekt:** Tagebuch-App
```python
import datetime

def eintrag_hinzufuegen():
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    eintrag = input("Dein Tagebuch-Eintrag: ")
    
    with open("tagebuch.txt", "a") as datei:
        datei.write(f"\n[{datum}]\n{eintrag}\n")
    
    print("Eintrag gespeichert!")

def eintraege_lesen():
    with open("tagebuch.txt", "r") as datei:
        print(datei.read())
```

**Übungen:**
1. Textdatei zeilenweise lesen
2. Wortanzahl in Datei zählen
3. Highscore-Liste speichern und laden

### Modul 8: Abschluss-Projekt (Woche 8)

**Wähle eines der folgenden Projekte:**

1. **Text-Adventure Spiel**
   - Verschiedene Räume
   - Inventar-System
   - Rätsel und Entscheidungen
   - Speichern/Laden

2. **Vokabeltrainer**
   - Vokabeln hinzufügen/löschen
   - Abfrage-Modus
   - Statistiken
   - Fortschritt speichern

3. **Kontakt-Manager**
   - Kontakte verwalten
   - Suche und Filter
   - Export/Import
   - Kategorien

## Assessment

### Self-Check nach jedem Modul

**Modul 1:**
- [ ] Ich kann Variablen erstellen und verwenden
- [ ] Ich verstehe verschiedene Datentypen
- [ ] Ich kann Benutzereingaben verarbeiten

**Modul 2:**
- [ ] Ich kann if-Bedingungen schreiben
- [ ] Ich verstehe logische Operatoren
- [ ] Ich kann verschachtelte Bedingungen erstellen

**Modul 3:**
- [ ] Ich kann while-Schleifen verwenden
- [ ] Ich kann for-Schleifen verwenden
- [ ] Ich verstehe, wann welche Schleife besser ist

**Modul 4:**
- [ ] Ich kann Listen erstellen und bearbeiten
- [ ] Ich kann durch Listen iterieren
- [ ] Ich verstehe List-Methoden

**Modul 5:**
- [ ] Ich kann eigene Funktionen schreiben
- [ ] Ich verstehe Parameter und Return-Werte
- [ ] Ich kann meine Funktionen dokumentieren

**Modul 6:**
- [ ] Ich kann Dictionaries erstellen und verwenden
- [ ] Ich verstehe den Unterschied zu Listen
- [ ] Ich kann durch Dictionaries iterieren

**Modul 7:**
- [ ] Ich kann Dateien lesen und schreiben
- [ ] Ich verstehe das with-Statement
- [ ] Ich kann Daten persistent speichern

### Finale Projekt-Bewertung

- [ ] Projekt ist funktional und erfüllt Anforderungen
- [ ] Code ist gut strukturiert und lesbar
- [ ] Funktionen werden sinnvoll eingesetzt
- [ ] Fehler werden behandelt
- [ ] Code ist dokumentiert

## Hilfreiche Ressourcen

- Python Dokumentation: https://docs.python.org/de/
- Python Tutor (Visualisierung): https://pythontutor.com/
- Replit (Online-IDE): https://replit.com/

## Nächste Schritte

Nach diesem Lernpfad kannst du weiterlernen mit:
- **Objektorientierte Programmierung** mit Python
- **Web-Entwicklung** mit Flask
- **Datenanalyse** mit Pandas
- **Spiele-Entwicklung** mit Pygame
