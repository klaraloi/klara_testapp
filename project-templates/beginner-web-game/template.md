# Projekt-Template: Einfaches Web-Spiel

**Schwierigkeitsgrad:** Anfänger  
**Dauer:** 2-4 Stunden  
**Technologien:** HTML, CSS, JavaScript (Basics)

## Projektbeschreibung

Erstelle ein einfaches interaktives Spiel im Browser, bei dem der Spieler eine Zahl erraten muss.

## Lernziele

### Programmierkonzepte
- [ ] Variablen deklarieren und verwenden
- [ ] Benutzereingaben verarbeiten
- [ ] If-Else Bedingungen verstehen
- [ ] While-Schleifen verwenden
- [ ] Funktionen definieren und aufrufen

### Web-Technologien
- [ ] HTML-Struktur aufbauen
- [ ] CSS für einfaches Styling
- [ ] JavaScript in HTML einbinden
- [ ] DOM-Manipulation (getElementById)
- [ ] Event-Handler (onclick)

## Projektstruktur

```
mein-ratespiel/
├── .copilot/
│   └── project-spec.md
├── index.html
├── style.css
└── script.js
```

## Meilensteine

### 1. Projekt-Setup
- [ ] Ordner erstellen
- [ ] HTML-Datei mit Grundgerüst
- [ ] CSS und JS Dateien verlinken

### 2. HTML-Struktur
- [ ] Überschrift hinzufügen
- [ ] Eingabefeld für die Zahl
- [ ] Button zum Raten
- [ ] Bereich für Feedback-Nachrichten

### 3. JavaScript-Logik
- [ ] Zufallszahl generieren
- [ ] Benutzereingabe abfragen
- [ ] Eingabe mit Zufallszahl vergleichen
- [ ] Feedback ausgeben (zu hoch/zu niedrig/richtig)

### 4. Verbesserungen
- [ ] Versuchszähler hinzufügen
- [ ] "Neues Spiel"-Button
- [ ] Styling mit CSS verschönern

## Starter-Code

### index.html
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zahlen-Ratespiel</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Zahlen-Ratespiel</h1>
        <p>Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?</p>
        
        <!-- TODO: Füge hier dein Eingabefeld hinzu -->
        <!-- TODO: Füge hier deinen Rate-Button hinzu -->
        <!-- TODO: Füge hier einen Bereich für Feedback hinzu -->
    </div>
    
    <script src="script.js"></script>
</body>
</html>
```

### style.css
```css
/* Grundlegendes Styling - Du kannst das später anpassen! */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    background-color: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    text-align: center;
}

/* TODO: Füge hier weitere Styles hinzu */
```

### script.js
```javascript
// Hier kommt dein JavaScript-Code hin!

// TODO: Erstelle eine Zufallszahl zwischen 1 und 100
// Tipp: Math.random() und Math.floor() könnten helfen

// TODO: Erstelle eine Funktion, die aufgerufen wird, wenn der Spieler rät
```

## Hilfreiche Fragen für den Copilot

Wenn du nicht weiterkommst, frage den Copilot:

1. "Wie erstelle ich eine Zufallszahl in JavaScript?"
2. "Wie bekomme ich den Wert aus einem Eingabefeld?"
3. "Wie vergleiche ich zwei Zahlen mit if-else?"
4. "Wie zeige ich eine Nachricht auf der Webseite an?"

## Erweiterungsideen

Wenn du fertig bist, könntest du:
- Einen Schwierigkeitsgrad hinzufügen (einfach: 1-50, schwer: 1-1000)
- Eine Bestenliste mit den wenigsten Versuchen
- Sound-Effekte für richtige/falsche Antworten
- Eine schönere Animation bei Gewinn

## Assessment-Fragen

Nach dem Projekt solltest du Folgendes beantworten können:
1. Was ist der Unterschied zwischen `let` und `const`?
2. Wann verwendet man eine `if`-Bedingung?
3. Was macht `getElementById()`?
4. Wie ruft man eine Funktion auf?
