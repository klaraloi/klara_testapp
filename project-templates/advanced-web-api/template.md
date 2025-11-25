# Projekt-Template: REST API mit Datenbank

**Schwierigkeitsgrad:** Fortgeschritten+  
**Dauer:** 8-12 Stunden  
**Technologien:** Node.js, Express, SQLite, REST API Design

## Projektbeschreibung

Erstelle eine vollständige REST API für eine Bibliotheks-Verwaltung mit Büchern, Autoren und Ausleih-Funktionalität.

## Lernziele

### Backend-Konzepte
- [ ] REST API Prinzipien verstehen
- [ ] HTTP-Methoden (GET, POST, PUT, DELETE)
- [ ] Status-Codes korrekt verwenden
- [ ] Request/Response Cycle
- [ ] Middleware-Konzept
- [ ] Routing in Express

### Datenbank
- [ ] SQL-Grundlagen (SELECT, INSERT, UPDATE, DELETE)
- [ ] Datenbank-Design und Normalisierung
- [ ] Relationen zwischen Tabellen
- [ ] Prepared Statements (SQL Injection verhindern)
- [ ] Transaktionen

### Fortgeschrittene Konzepte
- [ ] Asynchrone Programmierung (async/await)
- [ ] Error Handling Strategien
- [ ] Input Validation
- [ ] API-Dokumentation
- [ ] Testen von APIs

## Projektstruktur

```
library-api/
├── .copilot/
│   └── project-spec.md
├── src/
│   ├── routes/
│   │   ├── books.js
│   │   ├── authors.js
│   │   └── loans.js
│   ├── models/
│   │   ├── book.js
│   │   ├── author.js
│   │   └── loan.js
│   ├── middleware/
│   │   ├── validation.js
│   │   └── errorHandler.js
│   ├── database/
│   │   ├── db.js
│   │   └── schema.sql
│   └── app.js
├── tests/
│   └── api.test.js
├── package.json
└── README.md
```

## Datenbank-Schema

```sql
-- Autoren
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_year INTEGER,
    country TEXT
);

-- Bücher
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    isbn TEXT UNIQUE,
    published_year INTEGER,
    available BOOLEAN DEFAULT 1,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Ausleihen
CREATE TABLE loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    borrower_name TEXT NOT NULL,
    loan_date TEXT NOT NULL,
    return_date TEXT,
    FOREIGN KEY (book_id) REFERENCES books(id)
);
```

## API-Endpoints

### Bücher
- `GET /api/books` - Alle Bücher abrufen
- `GET /api/books/:id` - Ein bestimmtes Buch
- `POST /api/books` - Neues Buch erstellen
- `PUT /api/books/:id` - Buch aktualisieren
- `DELETE /api/books/:id` - Buch löschen

### Autoren
- `GET /api/authors` - Alle Autoren
- `GET /api/authors/:id` - Bestimmter Autor
- `GET /api/authors/:id/books` - Bücher eines Autors
- `POST /api/authors` - Neuen Autor erstellen

### Ausleihen
- `POST /api/loans` - Buch ausleihen
- `PUT /api/loans/:id/return` - Buch zurückgeben
- `GET /api/loans/active` - Aktive Ausleihen

## Meilensteine

### 1. Projekt-Setup
- [ ] Node.js Projekt initialisieren
- [ ] Dependencies installieren (express, sqlite3, dotenv)
- [ ] Projektstruktur aufbauen
- [ ] Git-Repository initialisieren

### 2. Datenbank
- [ ] SQLite-Datenbank einrichten
- [ ] Schema erstellen
- [ ] Seed-Daten einfügen
- [ ] Database-Modul implementieren

### 3. Basis-API
- [ ] Express-Server aufsetzen
- [ ] Bücher-Endpoints implementieren
- [ ] Error-Handling Middleware
- [ ] Request-Logging

### 4. Erweiterte Features
- [ ] Autoren-Endpoints
- [ ] Ausleihen-Funktionalität
- [ ] Input-Validation
- [ ] Suche und Filter-Parameter

### 5. Testing & Dokumentation
- [ ] Unit-Tests schreiben
- [ ] API-Dokumentation
- [ ] README mit Beispielen

## Starter-Code

### src/app.js
```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// TODO: Import routes
// const bookRoutes = require('./routes/books');

// TODO: Use routes
// app.use('/api/books', bookRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ 
        error: 'Etwas ist schiefgelaufen!',
        message: err.message 
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server läuft auf Port ${PORT}`);
});

module.exports = app;
```

### src/database/db.js
```javascript
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const dbPath = path.resolve(__dirname, 'library.db');

class Database {
    constructor() {
        this.db = new sqlite3.Database(dbPath, (err) => {
            if (err) {
                console.error('Fehler beim Öffnen der Datenbank:', err);
            } else {
                console.log('Datenbank verbunden');
                this.initialize();
            }
        });
    }

    initialize() {
        // TODO: Erstelle Tabellen falls nicht vorhanden
        // Tipp: Verwende db.run() für SQL-Befehle
    }

    async query(sql, params = []) {
        // TODO: Implementiere eine generische Query-Funktion
        // Tipp: Verwende Promises für async/await
    }

    async get(sql, params = []) {
        // TODO: Für einzelne Zeile
    }

    async all(sql, params = []) {
        // TODO: Für mehrere Zeilen
    }
}

module.exports = new Database();
```

### src/routes/books.js
```javascript
const express = require('express');
const router = express.Router();
const db = require('../database/db');

// GET alle Bücher
router.get('/', async (req, res, next) => {
    try {
        // TODO: Implementiere das Abrufen aller Bücher
        // Tipp: Verwende db.all() mit SQL SELECT
        
        res.json({ books: [] }); // Platzhalter
    } catch (error) {
        next(error);
    }
});

// GET einzelnes Buch
router.get('/:id', async (req, res, next) => {
    try {
        const { id } = req.params;
        // TODO: Implementiere das Abrufen eines Buchs
        
        res.json({ book: {} }); // Platzhalter
    } catch (error) {
        next(error);
    }
});

// POST neues Buch
router.post('/', async (req, res, next) => {
    try {
        const { title, author_id, isbn, published_year } = req.body;
        
        // TODO: Validiere Input
        // TODO: Füge Buch in DB ein
        
        res.status(201).json({ message: 'Buch erstellt' });
    } catch (error) {
        next(error);
    }
});

// TODO: Implementiere PUT und DELETE

module.exports = router;
```

## Best Practices

### 1. Error Handling
```javascript
// Async/Await mit Try-Catch
try {
    const result = await db.query(sql, params);
    res.json(result);
} catch (error) {
    next(error); // An Error-Middleware weitergeben
}
```

### 2. Input Validation
```javascript
function validateBook(book) {
    if (!book.title || book.title.trim() === '') {
        throw new Error('Titel ist erforderlich');
    }
    if (!book.author_id || isNaN(book.author_id)) {
        throw new Error('Gültige Autoren-ID erforderlich');
    }
    return true;
}
```

### 3. HTTP Status Codes
- `200 OK` - Erfolgreiche Anfrage
- `201 Created` - Ressource erstellt
- `400 Bad Request` - Ungültige Eingabe
- `404 Not Found` - Ressource nicht gefunden
- `500 Internal Server Error` - Server-Fehler

## Hilfreiche Fragen für den Copilot

1. "Wie erstelle ich eine REST API mit Express?"
2. "Wie verwende ich async/await mit SQLite?"
3. "Wie implementiere ich Input-Validation?"
4. "Wie teste ich API-Endpoints?"
5. "Wie erstelle ich Relationen zwischen Tabellen?"

## Erweiterungsideen

- [ ] Authentifizierung mit JWT
- [ ] Pagination für große Datensätze
- [ ] Rate Limiting
- [ ] Datei-Upload für Buch-Cover
- [ ] GraphQL statt REST
- [ ] Deployment auf einem Cloud-Service

## Assessment-Fragen

1. Was sind die Prinzipien von REST?
2. Wann verwendest du welchen HTTP-Status-Code?
3. Was ist der Unterschied zwischen PUT und PATCH?
4. Wie verhinderst du SQL Injection?
5. Was ist Middleware in Express?
6. Wie funktioniert async/await in JavaScript?
