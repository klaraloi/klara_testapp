# Lernpfad: Web-Entwicklung für Anfänger

**Zielgruppe:** Anfänger (12-16 Jahre)  
**Dauer:** 8-10 Wochen  
**Voraussetzungen:** Keine (Computer-Grundkenntnisse hilfreich)

## Übersicht

Lerne, interaktive Webseiten zu erstellen! Dieser Lernpfad führt dich durch HTML, CSS und JavaScript - die drei Säulen der Web-Entwicklung.

## Lernziele

- [ ] HTML-Struktur verstehen und anwenden
- [ ] Webseiten mit CSS gestalten
- [ ] Interaktivität mit JavaScript hinzufügen
- [ ] Responsive Webseiten erstellen
- [ ] Ein vollständiges Web-Projekt umsetzen

## Module

### Modul 1: HTML Grundlagen (Woche 1-2)

**Konzepte:**
- HTML-Dokument-Struktur
- Wichtigste Tags (h1-h6, p, div, span)
- Links und Bilder
- Listen (ul, ol)
- Formulare (input, button, textarea)

**Mini-Projekt:** Persönliche Vorstellungsseite

**Übungen:**
1. Erstelle eine "Über mich" Seite
2. Baue eine Rezept-Sammlung
3. Erstelle ein einfaches Kontaktformular

### Modul 2: CSS Styling (Woche 3-4)

**Konzepte:**
- CSS-Selektoren (Element, Klasse, ID)
- Farben und Hintergründe
- Textformatierung
- Box-Model (margin, padding, border)
- Flexbox Grundlagen

**Mini-Projekt:** Gestaltete Portfolio-Seite

**Übungen:**
1. Style eine Visitenkarte
2. Erstelle ein Button-Set
3. Gestalte eine Navigationsleiste

### Modul 3: JavaScript Basics (Woche 5-6)

**Konzepte:**
- Variablen und Datentypen
- DOM-Manipulation
- Event-Listener
- Funktionen
- If-Bedingungen

**Mini-Projekt:** Interaktive Quiz-Seite

**Übungen:**
1. Click-Counter
2. Farb-Wechsler
3. Einfacher Taschenrechner

### Modul 4: Fortgeschrittenes JavaScript (Woche 7)

**Konzepte:**
- Arrays und Objekte
- Schleifen
- LocalStorage
- Form-Validation

**Mini-Projekt:** Todo-Liste im Browser

### Modul 5: Responsive Design (Woche 8)

**Konzepte:**
- Media Queries
- Mobile-First Ansatz
- CSS Grid
- Responsive Bilder

**Mini-Projekt:** Responsive Portfolio

### Modul 6: Abschluss-Projekt (Woche 9-10)

**Projekt-Optionen:**
1. Interaktives Quiz-Spiel
2. Persönliches Blog
3. Kleine Web-App (z.B. Wetter-App)
4. Online-Portfolio

## Beispiel-Code Snippets

### HTML Grundgerüst
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine Webseite</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Willkommen!</h1>
    </header>
    <main>
        <!-- Dein Inhalt -->
    </main>
    <footer>
        <p>&copy; 2024 Meine Webseite</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

### CSS Styling
```css
/* Moderne, einfache Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f5f5f5;
}

.container {
    max-width: 800px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

button {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

### JavaScript Interaktivität
```javascript
// Element auswählen
const button = document.getElementById('meinButton');
const anzeige = document.getElementById('anzeige');

// Event Listener
button.addEventListener('click', function() {
    anzeige.textContent = 'Button wurde geklickt!';
});

// Daten in LocalStorage speichern
function datenSpeichern(key, wert) {
    localStorage.setItem(key, wert);
}

// Daten aus LocalStorage laden
function datenLaden(key) {
    return localStorage.getItem(key);
}
```

## Assessment

### Nach Modul 1 (HTML):
- [ ] Kann ich eine HTML-Seite mit Überschriften erstellen?
- [ ] Kann ich Links und Bilder einfügen?
- [ ] Verstehe ich die Struktur eines HTML-Dokuments?

### Nach Modul 2 (CSS):
- [ ] Kann ich Farben und Schriften ändern?
- [ ] Verstehe ich das Box-Model?
- [ ] Kann ich Elemente mit Flexbox anordnen?

### Nach Modul 3 (JavaScript Basics):
- [ ] Kann ich auf Button-Klicks reagieren?
- [ ] Kann ich HTML-Inhalte mit JavaScript ändern?
- [ ] Verstehe ich Variablen und Funktionen?

### Nach Modul 4 (Fortgeschritten):
- [ ] Kann ich Arrays und Objekte verwenden?
- [ ] Kann ich Daten mit LocalStorage speichern?
- [ ] Kann ich Formulare validieren?

### Nach Modul 5 (Responsive):
- [ ] Funktioniert meine Seite auf Mobilgeräten?
- [ ] Verstehe ich Media Queries?
- [ ] Kann ich flexible Layouts erstellen?

## Hilfreiche Ressourcen

- MDN Web Docs: https://developer.mozilla.org/de/
- CSS Tricks: https://css-tricks.com/
- CodePen (Beispiele): https://codepen.io/
- Can I Use (Browser-Support): https://caniuse.com/

## Nächste Schritte

Nach diesem Lernpfad:
- **Frontend-Frameworks:** React, Vue.js
- **Backend-Entwicklung:** Node.js, Express
- **Datenbanken:** MongoDB, SQL
- **Git & GitHub:** Versionskontrolle lernen
