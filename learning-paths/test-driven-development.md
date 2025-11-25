# Test-Driven Development (TDD) - Lernpfad

**Quelle:** Test-Driven Development By Example by Kent Beck (Addison Wesley, 2002)

> "Clean code that works - now. This is the seeming contradiction that lies behind much of the pain of programming. Test-driven development replies to this contradiction with a paradox - test the program before you write it."

## Überblick

Test-Driven Development (TDD) ist eine Programmiertechnik, die Tests als treibende Kraft für die Entwicklung nutzt. Statt erst Code zu schreiben und dann zu testen, schreibst du zuerst einen Test, der fehlschlägt, dann gerade genug Code um den Test zu bestehen, und refaktorierst dann den Code.

### Die TDD-Regeln

1. **Write new code only if an automated test has failed** - Schreibe neuen Code nur, wenn ein automatisierter Test fehlgeschlagen ist
2. **Eliminate duplication** - Eliminiere Duplikation

### Der TDD-Rhythmus: Red/Green/Refactor

1. **Red** - Schreibe einen kleinen Test, der nicht funktioniert (und vielleicht nicht mal kompiliert)
2. **Green** - Bringe den Test schnell zum Laufen, egal wie (auch mit "Sünden")
3. **Refactor** - Eliminiere alle Duplikation, die beim Zum-Laufen-Bringen entstanden ist

## Kernkonzepte

### Warum TDD?

**TDD hilft dir, Angst in Vertrauen zu verwandeln:**

- **Angst macht dich zögerlich** - TDD gibt dir konkrete Schritte
- **Angst macht dich verschlossen** - TDD fördert klare Kommunikation durch Tests
- **Angst lässt dich Feedback vermeiden** - TDD gibt dir ständig konkretes Feedback

**Die Tests sind wie eine Ratsche an einem Brunnen:**
- Je schwerer der Eimer (das Problem), desto enger müssen die Zähne sein (kleinere Test-Schritte)
- Einmal arbeitende Tests bleiben arbeiten - für immer
- Jeder Test bringt dich einen Schritt näher ans Ziel

### Die drei Strategien zur Implementierung

1. **Fake It** - Returniere eine Konstante und ersetze schrittweise Konstanten durch Variablen
2. **Obvious Implementation** - Tippe die offensichtliche Implementierung ein
3. **Triangulation** - Generalisiere Code erst, wenn du 2+ Beispiele hast

## Lernziele

Nach diesem Lernpfad kannst du:

### Grundlagen (Anfänger)
- [ ] Die TDD-Regeln erklären und anwenden
- [ ] Den Red/Green/Refactor-Zyklus durchführen
- [ ] Einfache Tests mit xUnit schreiben
- [ ] Die Fake-It-Strategie anwenden
- [ ] Duplikation zwischen Test und Code erkennen
- [ ] Kleine Schritte bei der Entwicklung nehmen

### Fortgeschritten
- [ ] Value Objects zur Vermeidung von Aliasing-Problemen nutzen
- [ ] Tests für Gleichheit (equals) und Hashing implementieren
- [ ] Mit Triangulation arbeiten wenn die Lösung unklar ist
- [ ] Refactorings sicher durchführen mit Test-Unterstützung
- [ ] Factory Methods zur Entkopplung nutzen
- [ ] Objekt-Hierarchien testgetrieben entwickeln

### Experte
- [ ] Komplexe Designs testgetrieben entwickeln
- [ ] Eigene Test-Frameworks bauen (xUnit)
- [ ] Design Patterns testgetrieben einführen
- [ ] Große Systeme mit TDD strukturieren
- [ ] Tests als Spezifikation und Dokumentation nutzen
- [ ] TDD-Praxis im Team etablieren

## Modul 1: Einführung in TDD (Woche 1-2)

### Lernziele
- Den TDD-Rhythmus verstehen und anwenden
- Erste Tests schreiben und zum Laufen bringen
- Fake It vs. Obvious Implementation unterscheiden

### Das Money-Beispiel (Teil 1)

**Aufgabe:** Multi-Currency Geld implementieren

**Schritt 1: Der erste Test**

```java
public void testMultiplication() {
    Dollar five = new Dollar(5);
    five.times(2);
    assertEquals(10, five.amount);
}
```

**Was wir tun:**
1. Stelle dir die **perfekte Schnittstelle** vor (wie soll die Operation aussehen?)
2. Schreibe den Test **bevor** der Code existiert
3. Mache minimale Schritte zum Kompilieren
4. Mache minimale Schritte zum Bestehen
5. Refaktoriere zur Generalisierung

**Schritt 2: Zum Kompilieren bringen**

```java
class Dollar {
    int amount;
    
    Dollar(int amount) {
    }
    
    void times(int multiplier) {
    }
}
```

**Schritt 3: Test bestehen (Fake It)**

```java
class Dollar {
    int amount = 10;  // Hardcoded!
    
    Dollar(int amount) {
    }
    
    void times(int multiplier) {
    }
}
```

**Schritt 4: Refactoring (Duplikation entfernen)**

```java
class Dollar {
    int amount;
    
    Dollar(int amount) {
        this.amount = amount;
    }
    
    void times(int multiplier) {
        amount *= multiplier;  // Generalisiert!
    }
}
```

### Übungen

1. **Einfache Arithmetik**: Implementiere eine `Calculator` Klasse testgetrieben
   - Addition von zwei Zahlen
   - Multiplikation
   - Division (mit Test für Division durch Null)

2. **String-Manipulation**: Baue testgetrieben eine `StringUtils` Klasse
   - `reverse(String)` - dreht einen String um
   - `isPalindrome(String)` - prüft ob String ein Palindrom ist
   - `countVowels(String)` - zählt Vokale

### Checkpoint: Was hast du gelernt?

- Kannst du die drei Phasen von Red/Green/Refactor benennen?
- Verstehst du, warum wir erst einen fehlschlagenden Test brauchen?
- Kannst du Duplikation zwischen Test und Code identifizieren?

## Modul 2: Value Objects und Gleichheit (Woche 3-4)

### Lernziele
- Value Objects verstehen und implementieren
- equals() und hashCode() richtig überschreiben
- Side Effects vermeiden

### Konzept: Value Objects

**Problem: Aliasing**
```java
Dollar d1 = new Dollar(5);
Dollar d2 = d1;
d1.times(2);  // Was passiert mit d2?
```

**Lösung: Value Objects**
- Werte ändern sich **nie** nach Erstellung
- Alle Operationen geben **neue Objekte** zurück
- Ermöglicht sichere Verwendung ohne Aliasing-Sorgen

### Gleichheit implementieren

**Test für Gleichheit:**
```java
public void testEquality() {
    assertTrue(new Dollar(5).equals(new Dollar(5)));
    assertFalse(new Dollar(5).equals(new Dollar(6)));
}
```

**Implementierung mit Triangulation:**

```java
// Erster Test: Fake It
public boolean equals(Object object) {
    return true;  // Sünde!
}

// Zweiter Test erzwingt Generalisierung
public void testEquality() {
    assertTrue(new Dollar(5).equals(new Dollar(5)));
    assertFalse(new Dollar(5).equals(new Dollar(6)));  // Neu!
}

// Jetzt müssen wir generalisieren
public boolean equals(Object object) {
    Dollar dollar = (Dollar) object;
    return amount == dollar.amount;
}
```

### Side Effects eliminieren

**Problem:**
```java
Dollar five = new Dollar(5);
five.times(2);
assertEquals(10, five.amount);
five.times(3);
assertEquals(15, five.amount);  // Aber five ist nicht mehr 5!
```

**Lösung: Neue Objekte zurückgeben**
```java
Dollar times(int multiplier) {
    return new Dollar(amount * multiplier);
}

// Test wird klarer:
Dollar five = new Dollar(5);
Dollar product = five.times(2);
assertEquals(new Dollar(10), product);
product = five.times(3);
assertEquals(new Dollar(15), product);
```

### Übungen

1. **Temperatur Value Object**: Erstelle eine `Temperature` Klasse
   - Unterstütze Celsius und Fahrenheit
   - Implementiere Konvertierung
   - Stelle sicher dass Temperature immutable ist
   - Implementiere equals richtig

2. **Money Value Object**: Erweitere das Dollar-Beispiel
   - Füge Francs hinzu
   - Implementiere equals so dass Dollar ≠ Franc
   - Teste alle Grenzfälle

### Checkpoint

- Kannst du erklären warum Value Objects Aliasing-Probleme vermeiden?
- Verstehst du den Unterschied zwischen Objektidentität und Wert-Gleichheit?
- Kannst du equals() korrekt implementieren?

## Modul 3: Refactoring mit Tests (Woche 5-6)

### Lernziele
- Sichere Refactorings mit Test-Unterstützung durchführen
- Duplikation systematisch eliminieren
- Code-Design schrittweise verbessern

### Refactoring-Strategie

**Die goldene Regel:** Refaktoriere nur wenn alle Tests grün sind!

**Schritte:**
1. Identifiziere Duplikation
2. Mache kleine Änderung
3. Führe alle Tests aus
4. Bei Rot: Rückgängig und kleinere Schritte
5. Bei Grün: Weiter zum nächsten Refactoring

### Factory Methods einführen

**Problem: Tests sind an konkrete Klassen gekoppelt**
```java
public void testMultiplication() {
    Dollar five = new Dollar(5);  // Dollar direkt referenziert
    assertEquals(new Dollar(10), five.times(2));
}
```

**Lösung: Factory Method**
```java
// Schritt 1: Factory einführen
static Dollar dollar(int amount) {
    return new Dollar(amount);
}

// Schritt 2: Im Test verwenden
public void testMultiplication() {
    Money five = Money.dollar(5);  // Jetzt Money!
    assertEquals(Money.dollar(10), five.times(2));
}

// Schritt 3: Rückgabetyp ändern
static Money dollar(int amount) {
    return new Dollar(amount);
}
```

**Vorteil:** Tests sind jetzt von der konkreten Implementierung entkoppelt

### Duplikation zwischen Subklassen eliminieren

**Strategie: "Reconcile Differences"**

1. **Mache Methoden identisch:**
```java
// Dollar
Franc times(int multiplier) {
    return new Franc(amount * multiplier);
}

// Franc  
Franc times(int multiplier) {
    return new Franc(amount * multiplier);
}
```

2. **Ändere Rückgabetyp:**
```java
Money times(int multiplier) {
    return new Franc(amount * multiplier);
}
```

3. **Verschiebe zu Superklasse wenn identisch**

### Übungen

1. **Shape Hierarchy**: Refaktoriere testgetrieben
   ```
   Gegeben: Rectangle und Circle mit dupliziertem Code
   Aufgabe: Extrahiere gemeinsame Funktionalität in Shape
   Behalte: Alle Tests grün!
   ```

2. **Report Generator**: Eliminiere Duplikation
   ```
   Gegeben: HTMLReport und XMLReport
   Aufgabe: Nutze Template Method Pattern
   Stelle sicher: Tests dokumentieren das Verhalten
   ```

### Wichtige Refactorings

#### Extract Method
```java
// Vorher: Langer Code
int calculateTotal() {
    int sum = 0;
    for (Item item : items) {
        sum += item.price * item.quantity;
    }
    return sum;
}

// Nachher: Extrahierte Methode
int calculateTotal() {
    return sumItemValues(items);
}

private int sumItemValues(List<Item> items) {
    int sum = 0;
    for (Item item : items) {
        sum += item.price * item.quantity;
    }
    return sum;
}
```

#### Move Method
```java
// Vorher: Methode am falschen Ort
class Invoice {
    double calculateTotal() {
        int width = bounds.right() - bounds.left();
        int height = bounds.bottom() - bounds.top();
        return width * height;  // Das ist Rectangle-Logik!
    }
}

// Nachher: Methode verschoben
class Rectangle {
    int area() {
        int width = right() - left();
        int height = bottom() - top();
        return width * height;
    }
}
```

### Checkpoint

- Kannst du Refactorings in kleine, sichere Schritte aufteilen?
- Erkennst du wann Code für Extract Method/Class bereit ist?
- Führst du Tests nach jedem Refactoring-Schritt aus?

## Modul 4: xUnit - Ein Test-Framework bauen (Woche 7-8)

### Lernziele
- Die Architektur von xUnit verstehen
- Meta-zirkuläres Testen (Tests testen Tests!)
- Reflection und Exceptions testen

### Das xUnit-Muster

**Kern-Konzepte:**
1. **TestCase** - Eine einzelne Test-Methode
2. **TestSuite** - Sammlung von Tests
3. **TestResult** - Sammelt Ergebnisse
4. **Fixture** - Setup und Teardown

### Testgetriebene Entwicklung von xUnit

**Schritt 1: Der erste Test**
```python
# Was wir wollen:
test = WasRun("testMethod")
print(test.wasRun)  # None
test.run()
print(test.wasRun)  # 1

# Der Test für den Test:
def testRunning(self):
    test = WasRun("testMethod")
    assert(not test.wasRun)
    test.run()
    assert(test.wasRun)
```

**Schritt 2: TestCase Klasse**
```python
class TestCase:
    def __init__(self, name):
        self.name = name
    
    def run(self):
        method = getattr(self, self.name)
        method()
```

**Schritt 3: Setup hinzufügen**
```python
def testSetUp(self):
    test = WasRun("testMethod")
    test.run()
    assert(test.wasSetUp)

class TestCase:
    def setUp(self):
        pass
    
    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
```

**Schritt 4: Exceptions handhaben**
```python
def testFailedResult(self):
    test = WasRun("testBrokenMethod")
    result = test.run()
    assert("1 run, 1 failed" == result.summary())

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    
    def testStarted(self):
        self.runCount += 1
    
    def testFailed(self):
        self.errorCount += 1
    
    def summary(self):
        return f"{self.runCount} run, {self.errorCount} failed"
```

### Die Template Method für Tests

```python
class TestCase:
    def run(self, result):
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
```

**Das ist das Herz von xUnit:**
1. Rufe `setUp()` auf
2. Führe Test-Methode aus
3. Bei Fehler: Markiere als fehlgeschlagen
4. Immer: Rufe `tearDown()` auf

### Übungen

1. **Minimal xUnit**: Implementiere in deiner Sprache
   - TestCase Basisklasse
   - Automatisches Finden von test* Methoden
   - setUp/tearDown Support
   - Fehler-Reporting

2. **Erweitere xUnit**:
   - TestSuite für mehrere Tests
   - Assertion-Helper (assertEquals, assertTrue, etc.)
   - Colored Output (Rot für Fehler, Grün für Erfolg)

### Checkpoint

- Verstehst du wie xUnit intern funktioniert?
- Kannst du das Template Method Pattern erkennen?
- Siehst du wie Tests sich selbst testen können?

## Modul 5: Design Patterns mit TDD (Woche 9-10)

### Lernziele
- Design Patterns testgetrieben entdecken
- Patterns aus Refactorings entstehen lassen
- Wissen wann Patterns anzuwenden sind

### Pattern: Command

**Problem:** Methodenaufruf reicht nicht aus (Logging, Undo, Später ausführen)

**TDD-Ansatz:**
```java
// Test: Wir wollen Operation verzögern
@Test
public void testDelayedExecution() {
    List<Runnable> queue = new ArrayList<>();
    queue.add(() -> System.out.println("First"));
    queue.add(() -> System.out.println("Second"));
    
    // Später ausführen
    for (Runnable cmd : queue) {
        cmd.run();
    }
}
```

**Pattern emergiert aus Bedarf!**

### Pattern: Null Object

**Problem:** Ständige null-Checks
```java
SecurityManager guard = System.getSecurityManager();
if (guard != null) {  // Überall!
    guard.canWrite(path);
}
```

**TDD-Lösung:**
```java
// Test ohne null-Checks
@Test
public void testWriteWithSecurity() {
    SecurityManager guard = System.getSecurityManager();
    guard.canWrite(path);  // Kein if!
}

// Implementierung
class LaxSecurity implements SecurityManager {
    public void canWrite(String path) {
        // Does nothing - that's the point!
    }
}

static SecurityManager getSecurityManager() {
    return security == null 
        ? new LaxSecurity()  // Null Object!
        : security;
}
```

### Pattern: Pluggable Selector

**Problem:** Viele ähnliche Subklassen, jede mit nur einer Methode

```java
// Vorher: Viele Subklassen
class HTMLReport extends Report {
    void print() { printHTML(); }
}
class XMLReport extends Report {
    void print() { printXML(); }
}

// Nachher: Eine Klasse mit Pluggable Selector
class Report {
    String printMessage;
    
    Report(String printMessage) {
        this.printMessage = printMessage;
    }
    
    void print() {
        Method method = getClass().getMethod(printMessage, null);
        method.invoke(this, new Class[0]);
    }
}
```

### Pattern: Composite

**Klassisches Beispiel: Account & Transaction**

```java
// Problem: Overall Account braucht eigene Balance-Berechnung
class Account {
    Transaction[] transactions;
    Money balance() {
        Money sum = Money.zero();
        for (Transaction t : transactions) {
            sum = sum.plus(t.value);
        }
        return sum;
    }
}

// Lösung: Beide implementieren Holding
interface Holding {
    Money balance();
}

class Transaction implements Holding {
    Money balance() { return value; }
}

class Account implements Holding {
    Holding[] holdings;  // Kann jetzt Transaction ODER Account sein!
    Money balance() {
        Money sum = Money.zero();
        for (Holding h : holdings) {
            sum = sum.plus(h.balance());
        }
        return sum;
    }
}
```

### Übungen

1. **File System**: Implementiere Composite testgetrieben
   - File und Directory als Holding
   - Beide haben size()
   - Directory kann Files UND Directories enthalten

2. **Graphics Editor**: Strategy Pattern entdecken
   - SelectionTool mit unterschiedlichem Verhalten
   - SingleSelection vs MultipleSelection
   - Lasse Pattern aus Tests entstehen

### Checkpoint

- Kannst du Patterns aus Refactorings entstehen lassen statt sie vorab zu planen?
- Erkennst du wann ein Pattern die Lösung vereinfacht?
- Verstehst du dass Patterns Werkzeuge sind, keine Ziele?

## Modul 6: Test Patterns (Woche 11-12)

### Lernziele
- Effektive Tests schreiben
- Test-Qualität beurteilen
- Test-Organisation verstehen

### Test-Writing Patterns

#### Assert First
**Schreibe den Assert zuerst, arbeite dich rückwärts**

```java
// Start hier:
assertEquals(Money.dollar(10), ????);

// Was brauchen wir?
assertEquals(Money.dollar(10), five.times(2));

// Was brauchen wir für five?
Dollar five = new Dollar(5);
assertEquals(Money.dollar(10), five.times(2));
```

#### Test Data
**Verwende Daten die die Geschichte erzählen**

```java
// Schlecht: Magische Zahlen
@Test public void testSum() {
    Money m1 = new Money(12);
    Money m2 = new Money(14);
    assertEquals(26, m1.plus(m2).amount);
}

// Gut: Verständliche Werte
@Test public void testSum() {
    Money five = Money.dollar(5);
    Money ten = Money.dollar(10);
    Money fifteen = Money.dollar(15);
    assertEquals(fifteen, five.plus(ten));
}
```

#### Test List
**Führe eine Liste aller Tests die du brauchst**

```
To-Do:
- $5 + 10 CHF = $10 if rate is 2:1
- $5 * 2 = $10
- Make "amount" private
- Dollar side effects?
- Money rounding?
```

### Red Bar Patterns

#### One Step Test
**Wähle einen Test der dich ein kleines Stück voranbringt**

```java
// Zu groß:
@Test public void testComplexCalculation() {
    // 50 Zeilen Setup...
}

// Besser: Kleine Schritte
@Test public void testAddition() {
    assertEquals(2, 1 + 1);
}

@Test public void testAdditionWithMoney() {
    assertEquals(Money.dollar(2), 
                 Money.dollar(1).plus(Money.dollar(1)));
}
```

#### Starter Test
**Beginne mit einem Test der sicher funktioniert**

```java
// Nicht mit dem schwierigsten anfangen!
@Test public void testCurrencyConversionWithRounding() { ... }

// Sondern mit dem einfachsten:
@Test public void testMultiplication() {
    assertEquals(10, 5 * 2);
}
```

#### Learning Test
**Schreibe Tests um externe APIs zu verstehen**

```java
@Test
public void testArrayList() {
    // Wie funktioniert ArrayList wirklich?
    List<String> list = new ArrayList<>();
    assertEquals(0, list.size());
    list.add("foo");
    assertEquals(1, list.size());
    assertEquals("foo", list.get(0));
}
```

### Green Bar Patterns

#### Fake It
**Return a constant, dann generalisiere**

```java
// Schritt 1: Fake It
int plus(int addend) {
    return 5;
}

// Schritt 2: Triangulate
@Test public void testPlusWithDifferentValues() {
    assertEquals(5, 2 + 3);
    assertEquals(7, 3 + 4);  // Kann nicht mehr 5 returnen!
}

// Schritt 3: Generalize
int plus(int addend) {
    return this.amount + addend;
}
```

#### Obvious Implementation
**Wenn offensichtlich: Einfach tippen!**

```java
// Wenn du weißt wie es geht:
String reverse(String s) {
    return new StringBuilder(s).reverse().toString();
}

// Kein Fake It nötig!
```

### Testing Patterns

#### Mock Object
**Ersetze teure/schwierige Objekte**

```java
// Echte Database ist langsam
interface Database {
    User findUser(int id);
}

// Mock für Tests
class MockDatabase implements Database {
    Map<Integer, User> users = new HashMap<>();
    
    User findUser(int id) {
        return users.get(id);
    }
}

@Test
public void testUserLookup() {
    MockDatabase db = new MockDatabase();
    db.users.put(1, new User("Alice"));
    
    UserService service = new UserService(db);
    assertEquals("Alice", service.getUserName(1));
}
```

#### Self Shunt
**Das Test-Objekt implementiert das Interface selbst**

```java
class TestObserver implements Observer {
    int updateCount = 0;
    
    @Test
    public void testNotification() {
        Subject subject = new Subject();
        subject.addObserver(this);  // Test ist Observer!
        subject.notifyObservers();
        assertEquals(1, updateCount);
    }
    
    public void update() {
        updateCount++;
    }
}
```

### Übungen

1. **Test-Liste erstellen**: Für ein kleines Projekt
   - Schreibe alle Tests auf die du brauchst
   - Sortiere nach Priorität
   - Markiere ab während du sie implementierst

2. **Mock Database**: Baue einen Mock
   - Interface für Database
   - Mock-Implementierung
   - Tests die den Mock nutzen

3. **Test-Qualität**: Verbessere vorhandene Tests
   - Finde magische Zahlen → Benenne sie
   - Finde zu große Tests → Teile sie
   - Finde Test-Duplikation → Extrahiere Helfer

### Checkpoint

- Erkennst du wann Tests zu groß sind?
- Nutzt du Test Lists um den Überblick zu behalten?
- Kannst du Mock Objects effektiv einsetzen?

## Modul 7: Mastering TDD (Woche 13-14)

### Lernziele
- TDD in der Praxis anwenden
- Schrittgröße dynamisch anpassen
- Mit großen Systemen arbeiten

### Wie groß sollen deine Schritte sein?

**Die Antwort: Es kommt darauf an!**

**Wenn alles glatt läuft:**
- Größere Schritte (Obvious Implementation)
- Mehrere Zeilen auf einmal
- Weniger Fake It

**Wenn es schwierig wird:**
- Kleinere Schritte (Fake It)
- Mehr Tests
- Mehr Refactoring-Zwischenschritte

**Die Kunst:** Dynamisch zwischen beiden Modi wechseln!

```java
// Glatt laufend: Obvious Implementation
@Test public void testAddition() {
    assertEquals(5, 2 + 3);
}

int plus(int a, int b) {
    return a + b;  // Direkt richtig!
}

// Schwierig: Fake It
@Test public void testComplexAlgorithm() {
    assertEquals(42, complexCalc(input));
}

int complexCalc(Input i) {
    return 42;  // Erst Fake...
}
// ...dann schrittweise zur richtigen Lösung
```

### Was musst du NICHT testen?

**Teste:**
- Conditionals
- Loops
- Operations
- Polymorphism

**Teste NICHT:**
- Code von anderen (wenn du ihm vertraust)
- Sprach-Features (sie funktionieren)
- Getter/Setter (wenn trivial)

**Aber:** Wenn du dir unsicher bist → Schreibe einen Test!

### Wie erkennst du gute Tests?

**Warnsignale für schlechtes Design:**

1. **Langer Setup-Code**
   ```java
   // 100 Zeilen Setup = Objekte sind zu groß
   @Test public void testSomething() {
       // Setup...
       // Setup...
       // Setup...
       // Endlich der eigentliche Test
       assertEquals(expected, actual);
   }
   ```

2. **Setup-Duplikation**
   - Gleicher Setup-Code überall
   - → Objekte sind zu eng gekoppelt

3. **Langsam laufende Tests**
   - Tests die lang laufen werden nicht ausgeführt
   - → Design-Problem, nicht Test-Problem

4. **Fragile Tests**
   - Brechen bei kleinen Änderungen
   - → Zu viel Kopplung

### TDD mit großen Systemen

**Skaliert TDD?**

**Beispiel: 250.000 Zeilen Produktionscode**
- 250.000 Zeilen Test-Code
- 4.000 Tests
- Laufen in < 20 Minuten
- Mehrmals täglich ausgeführt

**Schlüssel:**
- Eliminie Duplikation → Kleine Objekte
- Kleine Objekte → Isoliert testbar
- Funktionalität ≠ Komplexität

### TDD midstream einführen

**Problem:** Du hast alten Code ohne Tests

**Lösung:**

1. **Nicht alles auf einmal refactoren!**
   - Das dauert Monate
   - Keine neue Funktionalität in der Zeit

2. **Scoped Refactoring:**
   - Refaktoriere nur wo du gerade arbeitest
   - Neue Features: Test-first
   - Alter Code der sich nicht ändert: Erstmal lassen

3. **Die Deadlock brechen:**
   - Schreibe grobe Systemtests für Sicherheit
   - Arbeite sehr vorsichtig (Pair Programming!)
   - Mache Bereiche testbar wo du ändern musst

4. **Over time:**
   - Oft geänderte Teile werden test-driven
   - Selten geänderte Teile bleiben wie sie sind
   - Das ist OK!

### TDD und XP-Praktiken

**TDD verstärkt andere XP-Praktiken:**

1. **Pair Programming**
   - Tests sind perfekte Gesprächsthemen
   - Partner übernimmt wenn du müde wirst

2. **Continuous Integration**
   - Tests machen häufigeres Integrieren möglich
   - 15-30 Min statt 1-2 Stunden Zyklen

3. **Simple Design**
   - Nur Code für Tests + Duplikation entfernen
   - = Perfekt für aktuelle Requirements

4. **Refactoring**
   - Tests geben Confidence für große Refactorings
   - Mehr Confidence = Aggressivere Verbesserungen

5. **Continuous Delivery**
   - Weniger Defekte = Häufigere Releases möglich
   - Wie Day Trading: Kein Risiko über Nacht

### Übungen

1. **Legacy Code**: Nimm echten Code ohne Tests
   - Identifiziere einen kleinen Bereich
   - Schreibe Characterization Tests
   - Refaktoriere einen Schritt
   - Wiederhole

2. **Schrittgröße experimentieren**:
   - Nimm ein Problem
   - Löse es mit winzigen Schritten (Fake It immer)
   - Löse es mit großen Schritten (Obvious Always)
   - Vergleiche: Was fühlte sich besser an?

3. **Test-Qualität analysieren**:
   - Nimm deine Tests
   - Miss Setup-Länge
   - Miss Ausführungszeit
   - Identifiziere fragile Tests
   - Refaktoriere die schlechtesten

### Checkpoint

- Kannst du deine Schrittgröße an die Situation anpassen?
- Erkennst du Test-Smells die auf Design-Probleme hinweisen?
- Hast du Strategien um TDD in bestehendem Code einzuführen?

## Modul 8: Das große Ganze (Woche 15-16)

### Lernziele
- TDD als Teil eines Gesamtsystems verstehen
- Feedback-Loops erkennen und nutzen
- TDD-Kultur im Team etablieren

### Warum funktioniert TDD?

**Hypothese 1: Reduzierte Defekte**
- Frühe Fehlerfindung ist billig
- Weniger Stress beim Programmieren
- Bessere Teambeziehungen
- Kunden freuen sich auf neue Releases

**Hypothese 2: Kurze Feedback-Loops**
- Implementierung: Sekunden/Minuten
- Design: Sekunden/Minuten (Test = erstes Beispiel)
- Nicht: Wochen/Monate bis zur Nutzung

**Hypothese 3: Attraktoren in Complex Systems** (Phlip)

> "TDD creates an attractor in state space. Code is more likely to change for the better over time instead of for the worse; the attractor approaches correctness as a limit function."

### Influence Diagrams

**Positive Feedback Loop:**

```
Tests schreiben → Mehr Confidence → Mehr Refactoring
      ↑                                      ↓
      └─────────── Besseres Design ──────────┘
```

**Negative Feedback Loop (vermeiden!):**

```
Zeitdruck → Weniger Tests → Mehr Fehler
     ↑                            ↓
     └─────────────────────────────┘
```

### TDD als Entwicklungsphilosophie

**Naďve Annahme:** Besserer Code = Mehr Erfolg

**Realität:** 
- Engineering = ~20% vom Projekt-Erfolg
- Aber: Schlechtes Engineering versenkt Projekte definitiv

**TDD für Geeks die:**
- Eleganz schätzen
- Emotionale Bindung zu Code haben
- Projekte lieben die besser werden statt zu verfallen

### TDD im Team etablieren

**1. Starte klein:**
- Du selbst beginnst
- Zeige Erfolge
- Lade andere ein mitzumachen

**2. Pair Programming:**
- TDD lernt sich am besten in Paaren
- Tests sind natürliche Gesprächsthemen
- Pair Reviews Test-Qualität automatisch

**3. Kontinuierliches Lernen:**
- Code Reviews mit Fokus auf Tests
- Retrospektiven: Was haben Tests verhindert?
- Celebrate wenn Tests Bugs fangen

**4. Metriken die helfen:**
- % Code Coverage (aber nicht als Ziel!)
- Anzahl Tests
- Test-Ausführungszeit
- Zeit zwischen Check-ins

### Application-Level TDD?

**Idee:** Tests auf Applikationsebene

```python
# Statt:
def test_dollar_multiplication():
    five = Dollar(5)
    assert Dollar(10) == five.times(2)

# Vielleicht:
def test_checkout_flow():
    user = create_user("test@example.com")
    user.add_to_cart(product)
    user.checkout()
    assert order_was_created()
```

**Herausforderungen:**
- Fixture-Problem (Features existieren noch nicht)
- Sozial (Nutzer müssen lernen Tests zu schreiben)
- Lange Feedback-Loops

**Ansatz:**
- Mache ATDD nur wenn du TDD beherrscht
- Nutze beide Ebenen zusammen
- Kurze Zyklen beibehalten

### Die Zukunft von TDD

**Offene Fragen:**

1. **Optimale Schrittgröße?**
   - Kontext-abhängig
   - Lerne es durch Praxis

2. **TDD für GUIs?**
   - Ja, mit richtigen Tools
   - Modell testbar, View schwieriger

3. **TDD für Concurrency?**
   - Schwieriger aber möglich
   - Tests + Reasoning

4. **TDD für Security?**
   - Tests sind nötig, aber nicht ausreichend
   - Braucht zusätzlich Code Reviews

### Fibonacci Beispiel (Bonus)

**Vollständiges Beispiel von TDD in Aktion:**

```java
@Test public void testFibonacci() {
    // Test-driven table
    int[][] cases = {
        {0, 0},
        {1, 1},
        {2, 1},
        {3, 2},
        {4, 3},
        {5, 5}
    };
    for (int[] c : cases) {
        assertEquals(c[1], fib(c[0]));
    }
}

// Schritt 1: Return 0
int fib(int n) {
    return 0;
}

// Schritt 2: Special case 0
int fib(int n) {
    if (n == 0) return 0;
    return 1;
}

// Schritt 3: Special case <= 2
int fib(int n) {
    if (n == 0) return 0;
    if (n <= 2) return 1;
    return 2;  // Fails on {3,2}
}

// Schritt 4: Generalize 2 = 1 + 1
int fib(int n) {
    if (n == 0) return 0;
    if (n <= 2) return 1;
    return fib(n-1) + fib(n-2);
}

// Schritt 5: Cleanup
int fib(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fib(n-1) + fib(n-2);
}
```

**Vollständig test-driven entwickelt!**

### Finale Übungen

1. **TDD Kata**: Wähle eine
   - FizzBuzz
   - Primzahlen
   - Römische Zahlen
   - String Calculator (von Roy Osherove)

2. **Code Review**: Nimm alten Code
   - Identifiziere fehlende Tests
   - Schätze: Wie schwer wäre Refactoring?
   - Schreibe 3 wichtigste Tests
   - Versuche ein kleines Refactoring

3. **Team Retro**: Falls im Team
   - Was würde TDD bei letztem Bug verhindert haben?
   - Wo hatten wir Angst zu ändern?
   - Wie können wir mehr TDD einführen?

### Checkpoint

- Verstehst du die Philosophie hinter TDD?
- Siehst du TDD als Teil eines größeren Systems?
- Hast du Ideen wie du TDD ausbauen kannst?
- Kannst du andere für TDD begeistern?

## Zusammenfassung & Nächste Schritte

### Was du gelernt hast

**Core Skills:**
- ✅ Red/Green/Refactor Rhythmus
- ✅ Test-First Entwicklung
- ✅ Refactoring mit Test-Safety-Net
- ✅ Design Patterns aus Tests entstehen lassen
- ✅ Test-Qualität beurteilen
- ✅ TDD in verschiedenen Kontexten anwenden

**Mindset:**
- ✅ Tests sind Spezifikation und Dokumentation
- ✅ Kleine Schritte sind schneller als große Sprünge
- ✅ Duplikation ist der Feind
- ✅ Design emergiert, wird nicht vorab geplant
- ✅ Mut kommt aus Tests, nicht aus Hoffnung

### Kent Beck's Wichtigste Lektionen

1. **"Clean code that works - now"**
   - Nicht morgen, nicht irgendwann
   - Jetzt, mit Tests als Beweis

2. **Die zwei Regeln:**
   - Code nur wenn Test rot ist
   - Entferne Duplikation

3. **Courage from Tests:**
   - Tests verwandeln Angst in Confidence
   - Confidence führt zu besseren Designs
   - Bessere Designs führen zu mehr Tests

4. **TDD ist kein Test-Technique:**
   - Es ist eine Design-Technik
   - Es ist eine Analyse-Technik
   - Es strukturiert alle Development-Aktivitäten

### Übung: Dein TDD-Manifest

Schreibe auf:

1. **Was ich an TDD schätze:**
   - Was hat dir am meisten geholfen?
   - Was hat dich überrascht?

2. **Wo ich TDD anwenden will:**
   - Welche Projekte?
   - Welche Arten von Code?

3. **Meine TDD-Regeln:**
   - Wann nutze ich Fake It?
   - Wie groß sind meine Schritte?
   - Wann refaktoriere ich?

4. **Nächste Schritte:**
   - Welches Projekt test-drive ich als nächstes?
   - Wen lade ich zum Pair Programming ein?
   - Welches Buch lese ich als nächstes?

### Weiterführende Ressourcen

**Bücher:**
- "Refactoring" by Martin Fowler - Der Klassiker zu Refactorings
- "Working Effectively with Legacy Code" by Michael Feathers - TDD in altem Code
- "Growing Object-Oriented Software, Guided by Tests" by Steve Freeman & Nat Pryce - TDD advanced

**Online:**
- Coding Katas (z.B. auf codewars.com)
- TDD Bowling Game Kata (von Uncle Bob)
- TestDrivenDevelopment.com

**Communities:**
- XP/Agile User Groups
- Software Craftsmanship Communities
- Pair Programming Treffen

### Schlusswort

> "I'm not a great programmer; I'm just a good programmer with great habits." - Kent Beck

TDD ist eine dieser great habits. Es ist nicht leicht, es ist nicht immer angenehm, aber es ist fundamental transformierend. Du wirst Code anders sehen, anders schreiben, anders denken.

**Der Rhythmus bleibt:**
1. Red - Schreibe einen Test der fehlschlägt
2. Green - Bringe ihn zum Laufen
3. Refactor - Mache ihn richtig

**Immer und immer wieder.**

Jetzt bist du dran - schreibe deinen ersten Test! 🚀

---

## Anhang A: TDD Cheat Sheet

### Quick Reference

**Der TDD-Zyklus:**
```
Write Test → Red → Green → Refactor → Repeat
```

**Die drei Strategien:**
- Fake It (til you make it)
- Triangulate (2+ examples)
- Obvious Implementation

**Core Refactorings:**
- Extract Method
- Extract Class
- Move Method
- Inline Method
- Rename

**Test Patterns:**
- Assert First
- Test Data
- Evident Data
- Test List

**Warnsignale:**
- Lange Setup-Zeit
- Setup-Duplikation
- Langsame Tests
- Fragile Tests

### Code-Snippets

**xUnit Basis (Java):**
```java
public class MyTest extends TestCase {
    private Fixture fixture;
    
    @Before
    public void setUp() {
        fixture = new Fixture();
    }
    
    @Test
    public void testSomething() {
        assertEquals(expected, fixture.doSomething());
    }
    
    @After
    public void tearDown() {
        fixture = null;
    }
}
```

**Mock Object:**
```java
class MockDatabase implements Database {
    Map<Integer, User> users = new HashMap<>();
    
    public User find(int id) {
        return users.get(id);
    }
}
```

**Template Method:**
```java
abstract class TestCase {
    public void run() {
        setUp();
        try {
            runTest();
        } finally {
            tearDown();
        }
    }
    
    abstract void runTest();
    void setUp() {}
    void tearDown() {}
}
```

## Anhang B: Glossar

**Attractor:** Punkt im State Space wo Flows konvergieren (aus Complex Systems Theory)

**Bar:** Die Test-Ausgabe - Rot (failed) oder Grün (passed)

**Fake It:** Strategie: Konstante returnen, dann graduell generalisieren

**Fixture:** Setup-Code für Tests (Objekte, Daten, etc.)

**Mock Object:** Test-Double das komplexe Abhängigkeiten ersetzt

**Obvious Implementation:** Strategie: Offensichtliche Lösung direkt tippen

**Ratchet:** Ratsche - Metapher für Tests die einmal bestanden bleiben

**Red/Green/Refactor:** Der TDD-Rhythmus

**Test-First:** Tests vor dem Code schreiben

**Test-Driven:** Entwicklung wird durch Tests getrieben

**Triangulation:** Strategie: Erst mit 2+ Beispielen generalisieren

**Value Object:** Objekt dessen Wert sich nach Erstellung nie ändert

**xUnit:** Familie von Test-Frameworks (JUnit, NUnit, PyTest, etc.)

---

**Viel Erfolg beim Test-Driven Development! May your bars be forever green! 🟢**
