# Beispielprojekt: Einfaches Zahlen-Ratespiel

Dieses vollständige Beispielprojekt zeigt, wie ein Anfänger-Projekt aussehen kann.

## Projektübersicht

**Technologie:** HTML, CSS, JavaScript  
**Schwierigkeit:** Anfänger  
**Entwicklungszeit:** 2-3 Stunden

## Projektdateien

### Dateistruktur

```
zahlen-ratespiel/
├── .copilot/
│   └── project-spec.md
├── index.html
├── style.css
├── script.js
└── README.md
```

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
        <h1>🎯 Zahlen-Ratespiel</h1>
        <p class="anleitung">Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?</p>
        
        <div class="spiel-bereich">
            <input type="number" id="eingabe" min="1" max="100" placeholder="Deine Zahl...">
            <button id="raten-button">Raten!</button>
        </div>
        
        <div id="feedback" class="feedback"></div>
        
        <div class="stats">
            <p>Versuche: <span id="versuche">0</span></p>
            <p>Beste Punktzahl: <span id="beste-punktzahl">-</span></p>
        </div>
        
        <button id="neues-spiel-button" class="versteckt">Neues Spiel</button>
    </div>
    
    <script src="script.js"></script>
</body>
</html>
```

### style.css

```css
/* Grundlegendes Styling */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    max-width: 500px;
    width: 100%;
    text-align: center;
}

h1 {
    color: #667eea;
    margin-bottom: 10px;
    font-size: 2.5em;
}

.anleitung {
    color: #666;
    margin-bottom: 30px;
    line-height: 1.6;
}

.spiel-bereich {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
}

input[type="number"] {
    flex: 1;
    padding: 15px;
    font-size: 18px;
    border: 2px solid #ddd;
    border-radius: 10px;
    outline: none;
    transition: border-color 0.3s;
}

input[type="number"]:focus {
    border-color: #667eea;
}

button {
    padding: 15px 30px;
    font-size: 18px;
    font-weight: bold;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

button:active {
    transform: translateY(0);
}

.feedback {
    min-height: 80px;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
    font-size: 18px;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
}

.feedback.zu-hoch {
    background: #ffe5e5;
    color: #d32f2f;
}

.feedback.zu-niedrig {
    background: #e3f2fd;
    color: #1976d2;
}

.feedback.richtig {
    background: #e8f5e9;
    color: #388e3c;
}

.stats {
    display: flex;
    justify-content: space-around;
    margin-bottom: 20px;
    padding: 20px;
    background: #f5f5f5;
    border-radius: 10px;
}

.stats p {
    color: #666;
    font-size: 16px;
}

.stats span {
    color: #667eea;
    font-weight: bold;
    font-size: 20px;
}

.versteckt {
    display: none;
}

#neues-spiel-button {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
}

/* Animationen */
@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    75% { transform: translateX(10px); }
}

.shake {
    animation: shake 0.5s;
}

@keyframes celebrate {
    0%, 100% { transform: scale(1) rotate(0deg); }
    25% { transform: scale(1.1) rotate(-5deg); }
    75% { transform: scale(1.1) rotate(5deg); }
}

.celebrate {
    animation: celebrate 0.5s;
}
```

### script.js

```javascript
// Spiel-Variablen
let zufallszahl;      // Die zu erratende Zahl
let versuche;         // Anzahl der Versuche
let bestePunktzahl;   // Beste bisherige Punktzahl

// DOM-Elemente
const eingabefeld = document.getElementById('eingabe');
const ratenButton = document.getElementById('raten-button');
const neuesSpielButton = document.getElementById('neues-spiel-button');
const feedbackBereich = document.getElementById('feedback');
const versucheAnzeige = document.getElementById('versuche');
const bestePunktzahlAnzeige = document.getElementById('beste-punktzahl');

// Initialisierung beim Laden der Seite
window.addEventListener('load', () => {
    // Lade beste Punktzahl aus LocalStorage
    bestePunktzahl = localStorage.getItem('bestePunktzahl') || Infinity;
    if (bestePunktzahl !== Infinity) {
        bestePunktzahlAnzeige.textContent = bestePunktzahl;
    }
    
    // Starte neues Spiel
    neuesSpiel();
});

// Event Listener für Buttons
ratenButton.addEventListener('click', pruefeRateVersuch);
neuesSpielButton.addEventListener('click', neuesSpiel);

// Enter-Taste zum Raten
eingabefeld.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        pruefeRateVersuch();
    }
});

/**
 * Startet ein neues Spiel
 */
function neuesSpiel() {
    // Generiere neue Zufallszahl zwischen 1 und 100
    zufallszahl = Math.floor(Math.random() * 100) + 1;
    versuche = 0;
    
    // Setze UI zurück
    eingabefeld.value = '';
    eingabefeld.disabled = false;
    eingabefeld.focus();
    feedbackBereich.textContent = '';
    feedbackBereich.className = 'feedback';
    versucheAnzeige.textContent = '0';
    
    // Verstecke "Neues Spiel" Button
    neuesSpielButton.classList.add('versteckt');
    
    // Aktiviere Raten-Button
    ratenButton.disabled = false;
    
    console.log('Neue Zahl generiert:', zufallszahl); // Nur zum Testen!
}

/**
 * Prüft den Rateversuch des Spielers
 */
function pruefeRateVersuch() {
    // Hole die eingegebene Zahl
    const geratenezahl = parseInt(eingabefeld.value);
    
    // Validierung
    if (isNaN(geratenezahl)) {
        zeigeFeedback('Bitte gib eine Zahl ein!', 'zu-hoch');
        eingabefeld.classList.add('shake');
        setTimeout(() => eingabefeld.classList.remove('shake'), 500);
        return;
    }
    
    if (geratenezahl < 1 || geratenezahl > 100) {
        zeigeFeedback('Die Zahl muss zwischen 1 und 100 liegen!', 'zu-hoch');
        eingabefeld.classList.add('shake');
        setTimeout(() => eingabefeld.classList.remove('shake'), 500);
        return;
    }
    
    // Erhöhe Versuchszähler
    versuche++;
    versucheAnzeige.textContent = versuche;
    
    // Vergleiche mit Zufallszahl
    if (geratenezahl === zufallszahl) {
        // Richtig geraten!
        spielGewonnen();
    } else if (geratenezahl < zufallszahl) {
        // Zu niedrig
        zeigeFeedback(`${geratenezahl} ist zu niedrig! 📉 Versuche es höher!`, 'zu-niedrig');
        eingabefeld.value = '';
        eingabefeld.focus();
    } else {
        // Zu hoch
        zeigeFeedback(`${geratenezahl} ist zu hoch! 📈 Versuche es niedriger!`, 'zu-hoch');
        eingabefeld.value = '';
        eingabefeld.focus();
    }
}

/**
 * Zeigt Feedback-Nachricht an
 */
function zeigeFeedback(nachricht, klasse) {
    feedbackBereich.textContent = nachricht;
    feedbackBereich.className = `feedback ${klasse}`;
}

/**
 * Wird aufgerufen, wenn das Spiel gewonnen wurde
 */
function spielGewonnen() {
    // Zeige Erfolgsnachricht
    zeigeFeedback(`🎉 Richtig! Die Zahl war ${zufallszahl}! Du hast ${versuche} Versuche gebraucht!`, 'richtig');
    
    // Feiere mit Animation
    feedbackBereich.classList.add('celebrate');
    
    // Deaktiviere Eingabe
    eingabefeld.disabled = true;
    ratenButton.disabled = true;
    
    // Zeige "Neues Spiel" Button
    neuesSpielButton.classList.remove('versteckt');
    
    // Aktualisiere beste Punktzahl
    if (versuche < bestePunktzahl) {
        bestePunktzahl = versuche;
        bestePunktzahlAnzeige.textContent = bestePunktzahl;
        localStorage.setItem('bestePunktzahl', bestePunktzahl);
        
        // Zeige Extra-Feedback für neuen Rekord
        setTimeout(() => {
            zeigeFeedback(`🏆 Neuer Rekord! Du bist großartig!`, 'richtig');
        }, 2000);
    }
}
```

### .copilot/project-spec.md

```markdown
# Projekt: Zahlen-Ratespiel

**Erstellt am:** 2024-03-15
**Letzte Aktualisierung:** 2024-03-17

## 1. Projektziel

### Was möchte ich bauen?
Ein interaktives Browser-Spiel, bei dem der Computer eine Zahl zwischen 1 und 100 zufällig auswählt und der Spieler diese Zahl erraten muss. Das Spiel gibt Hinweise (zu hoch/zu niedrig) und zählt die Versuche.

### Für wen ist das Projekt?
Für mich selbst zum Lernen und zum Spielen mit Freunden.

### Warum ist mir dieses Projekt wichtig?
Ich möchte JavaScript lernen und ein echtes, funktionierendes Spiel erstellen, das Spaß macht!

## 2. Mein aktueller Wissensstand

### Programmiererfahrung
- [x] Ich bin Anfänger (erste Schritte)
- [ ] Ich habe Grundkenntnisse (ein paar Projekte gemacht)
- [ ] Ich bin fortgeschritten (mehrere Projekte abgeschlossen)

### Was ich schon kann
- [x] HTML schreiben
- [x] CSS für Styling (Grundlagen)
- [ ] JavaScript Basics
- [ ] Variablen verwenden
- [ ] If-Bedingungen schreiben
- [ ] Funktionen erstellen

### Was ich in diesem Projekt lernen möchte
1. JavaScript Grundlagen (Variablen, Funktionen)
2. Wie man auf Button-Klicks reagiert
3. Zufallszahlen generieren
4. Daten im Browser speichern (LocalStorage)

## Lernziele (vom Copilot ergänzt)

### Programmierkonzepte
- [x] Variablen deklarieren (let, const)
- [x] Funktionen definieren und aufrufen
- [x] If-Else Bedingungen
- [x] Event-Listener verwenden
- [x] DOM-Manipulation (getElementById)

### Technische Skills
- [x] JavaScript in HTML einbinden
- [x] Input-Validierung
- [x] LocalStorage API
- [x] Math.random() für Zufallszahlen
- [x] CSS Animationen

## Fortschritt

### Meilenstein 1: Setup ✅
- [x] HTML-Grundgerüst erstellt
- [x] CSS-Datei verlinkt
- [x] JavaScript-Datei verlinkt

### Meilenstein 2: Grundfunktionalität ✅
- [x] Zufallszahl generieren
- [x] Benutzereingabe verarbeiten
- [x] Vergleich und Feedback

### Meilenstein 3: Verbesserungen ✅
- [x] Versuchszähler
- [x] Beste Punktzahl speichern
- [x] Schönes Design
- [x] Animationen

## Was ich gelernt habe

- Wie man Math.random() verwendet
- Event-Listener sind super praktisch!
- LocalStorage speichert Daten auch nach Schließen des Browsers
- CSS kann man für coole Animationen nutzen
- Funktionen machen den Code übersichtlich
```

## Wie man das Projekt nutzt

1. **Öffnen**: Einfach `index.html` in einem Browser öffnen
2. **Spielen**: Zahl eingeben und auf "Raten!" klicken
3. **Gewinnen**: So wenig Versuche wie möglich verwenden!

## Was man daraus lernen kann

- **Anfänger**: Vollständiges Beispiel für ein erstes JavaScript-Projekt
- **Fortgeschritten**: Kann als Basis für Erweiterungen dienen
- **Lehrer**: Zeigt gute Praktiken und Struktur

## Mögliche Erweiterungen

1. Schwierigkeitsgrade (1-50, 1-100, 1-1000)
2. Timer hinzufügen
3. Sound-Effekte
4. Zwei-Spieler-Modus
5. Highscore-Liste
6. Hinweise nach X Versuchen
