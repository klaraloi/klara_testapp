# Projekt-Template: Todo-Listen-App (CLI)

**Schwierigkeitsgrad:** Fortgeschritten  
**Dauer:** 4-6 Stunden  
**Technologien:** Python, File I/O, JSON

## Projektbeschreibung

Erstelle eine Kommandozeilen-Anwendung zur Verwaltung von Aufgaben (Todos). Die App soll Todos speichern, anzeigen, bearbeiten und löschen können.

## Lernziele

### Programmierkonzepte
- [ ] Listen und Dictionaries verwenden
- [ ] Funktionen mit Parametern und Rückgabewerten
- [ ] Dateien lesen und schreiben
- [ ] JSON-Format verstehen und nutzen
- [ ] Exception Handling (try-except)
- [ ] While-Schleifen für Menüs
- [ ] String-Methoden (split, strip, format)

### Python-Spezifisch
- [ ] Module importieren
- [ ] Mit dem Dateisystem arbeiten (os/pathlib)
- [ ] Datum und Zeit verwenden (datetime)
- [ ] List Comprehensions
- [ ] f-Strings für Formatierung

## Projektstruktur

```
todo-app/
├── .copilot/
│   └── project-spec.md
├── todo_app.py        # Hauptprogramm
├── todo_manager.py    # Todo-Logik
├── storage.py         # Datei-Operationen
├── todos.json         # Gespeicherte Todos
└── README.md
```

## Meilensteine

### 1. Grundstruktur
- [ ] Projekt-Setup mit Python
- [ ] Hauptmenü mit Optionen erstellen
- [ ] Menü-Loop implementieren

### 2. Todo-Verwaltung
- [ ] Todo hinzufügen (Titel, Beschreibung)
- [ ] Alle Todos anzeigen
- [ ] Todo als erledigt markieren
- [ ] Todo löschen

### 3. Datenspeicherung
- [ ] Todos in JSON-Datei speichern
- [ ] Todos beim Start laden
- [ ] Fehlerbehandlung bei Datei-Operationen

### 4. Erweiterte Features
- [ ] Datum für Todos hinzufügen
- [ ] Todos nach Priorität sortieren
- [ ] Suche nach Todos
- [ ] Statistiken anzeigen

## Starter-Code

### todo_app.py
```python
"""
Todo-Listen-Anwendung
Hauptprogramm mit Menü und Benutzerinteraktion
"""

def zeige_menu():
    """Zeigt das Hauptmenü an"""
    print("\n=== TODO-LISTEN-APP ===")
    print("1. Alle Todos anzeigen")
    print("2. Neues Todo hinzufügen")
    print("3. Todo als erledigt markieren")
    print("4. Todo löschen")
    print("5. Beenden")
    print("=====================")

def main():
    """Hauptfunktion der Anwendung"""
    print("Willkommen zur Todo-Listen-App!")
    
    # TODO: Lade vorhandene Todos
    
    while True:
        zeige_menu()
        auswahl = input("\nDeine Wahl (1-5): ")
        
        # TODO: Implementiere die Menü-Logik
        
        if auswahl == "5":
            print("Auf Wiedersehen!")
            break

if __name__ == "__main__":
    main()
```

### todo_manager.py
```python
"""
Todo-Manager
Enthält die Logik für Todo-Operationen
"""

class TodoManager:
    def __init__(self):
        self.todos = []
    
    def todo_hinzufuegen(self, titel, beschreibung=""):
        """Fügt ein neues Todo hinzu"""
        # TODO: Implementiere diese Funktion
        pass
    
    def todos_anzeigen(self):
        """Zeigt alle Todos an"""
        # TODO: Implementiere diese Funktion
        pass
    
    def todo_erledigen(self, index):
        """Markiert ein Todo als erledigt"""
        # TODO: Implementiere diese Funktion
        pass
    
    def todo_loeschen(self, index):
        """Löscht ein Todo"""
        # TODO: Implementiere diese Funktion
        pass
```

### storage.py
```python
"""
Storage-Modul
Verwaltet das Speichern und Laden von Todos
"""
import json

def todos_speichern(todos, dateiname="todos.json"):
    """Speichert Todos in einer JSON-Datei"""
    # TODO: Implementiere das Speichern
    pass

def todos_laden(dateiname="todos.json"):
    """Lädt Todos aus einer JSON-Datei"""
    # TODO: Implementiere das Laden
    # Tipp: Vergiss nicht die Fehlerbehandlung!
    pass
```

## Hilfreiche Konzepte

### 1. JSON-Format
```python
# Ein Todo als Dictionary
todo = {
    "id": 1,
    "titel": "Hausaufgaben machen",
    "beschreibung": "Mathe Seite 42",
    "erledigt": False,
    "erstellt_am": "2024-03-15"
}

# Liste von Todos
todos = [todo1, todo2, todo3]
```

### 2. Datei-Operationen
```python
# Schreiben
with open("datei.json", "w") as f:
    json.dump(daten, f)

# Lesen
with open("datei.json", "r") as f:
    daten = json.load(f)
```

### 3. Exception Handling
```python
try:
    # Code der fehlschlagen könnte
    datei = open("todos.json", "r")
except FileNotFoundError:
    # Was tun, wenn Datei nicht existiert
    print("Keine gespeicherten Todos gefunden")
```

## Hilfreiche Fragen für den Copilot

1. "Wie erstelle ich ein Dictionary in Python?"
2. "Wie speichere ich eine Liste in einer JSON-Datei?"
3. "Wie behandle ich Fehler beim Öffnen von Dateien?"
4. "Wie formatiere ich Datum und Uhrzeit in Python?"

## Erweiterungsideen

- [ ] Kategorien für Todos (Arbeit, Privat, Schule)
- [ ] Fälligkeitsdatum und Erinnerungen
- [ ] Export als CSV oder TXT
- [ ] Farbige Ausgabe in der Konsole (colorama)
- [ ] Undo-Funktion für gelöschte Todos

## Assessment-Fragen

1. Was ist der Unterschied zwischen einer Liste und einem Dictionary?
2. Warum verwenden wir `with open()` statt nur `open()`?
3. Wann würdest du eine Klasse statt einfache Funktionen verwenden?
4. Wie funktioniert Exception Handling in Python?
