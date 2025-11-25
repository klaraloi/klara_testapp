# Extreme Programming Installed - Lernpfad

## Überblick

**Titel:** Extreme Programming Installed  
**Autoren:** Ron Jeffries, Ann Anderson, Chet Hendrickson  
**Erscheinungsjahr:** 2001  
**Verlag:** Addison-Wesley  
**Umfang:** 288 Seiten

### Was ist "Extreme Programming Installed"?

Während "Extreme Programming Explained" von Kent Beck die **Philosophie und Prinzipien** von XP beschreibt, ist "Extreme Programming Installed" der praktische **Implementierungsleitfaden**. Die drei Autoren waren Teil des legendären C3-Projekts (Chrysler Comprehensive Compensation System), wo XP geboren wurde.

Das Buch führt dich **chronologisch durch ein XP-Projekt**:
- Von den ersten User Stories bis zum Release
- Mit konkreten Techniken für Customer, Programmer und Manager
- Mit Praxisbeispielen, Kriegsgeschichten und Lessons Learned

### Kernbotschaft

**"Test everything that could possibly break"** und **"Do the simplest thing that could possibly work"** sind nicht nur Slogans – sie sind Arbeitstechniken, die dieses Buch im Detail erklärt.

## Die drei Rollen in XP

### Customer Role
- Definiert Business Value durch User Stories
- Wählt Features nach Priorität
- Spezifiziert Acceptance Tests
- **Recht:** Den größtmöglichen Wert aus jeder Programmierwoche herausholen

### Programmer Role
- Analysiert, designt, testet, programmiert
- Schätzt Story-Schwierigkeit
- Misst Velocity (Liefergeschwindigkeit)
- **Recht:** Qualitätsarbeit zu jeder Zeit produzieren

### Manager Role
- Beseitigt Hindernisse
- Koordiniert Team-Aktivitäten
- Reported Status
- **Recht:** Einen Gesamtplan zu haben und den Fortschritt zu kennen

## Lernziele

### Anfänger (0-2 Jahre Erfahrung)

Nach diesem Lernpfad kannst du:

1. **Circle of Life verstehen**
   - Customer definiert Value → Programmer schätzt Cost → Customer wählt → Programmer baut
   - Den Unterschied zwischen Estimate und Promise erkennen

2. **User Stories schreiben**
   - Stories auf Karteikarten formulieren (1-3 Wochen Aufwand)
   - "Promise for Conversation" Prinzip anwenden
   - Stories splitten, wenn sie zu groß sind

3. **Story Estimation durchführen**
   - In Perfect Engineering Days schätzen
   - Velocity-Faktor (typisch 1/3) verstehen
   - Stories in 1-3 Programmer-Weeks einordnen

4. **Acceptance Tests definieren**
   - Tests automatisieren (kein manuelles Checking!)
   - Test-Daten aus Legacy-Systemen oder Spreadsheets nutzen
   - "Guru Checks Output" Anti-Pattern vermeiden

5. **Iteration Planning machen**
   - 2-3 Wochen Iterationen planen
   - Sign-up für Tasks (nicht Assignment!)
   - Yesterday's Weather zur Velocity-Vorhersage nutzen

### Fortgeschritten (2-5 Jahre Erfahrung)

Du lernst außerdem:

6. **Pair Programming produktiv nutzen**
   - Driver/Navigator Rollen verstehen
   - Pair Rotation organisieren
   - Code Reviews durch kontinuierliche Review ersetzen

7. **Test-First Development praktizieren**
   - Unit Tests VOR dem Code schreiben
   - Test by Intention (erst WHAT, dann HOW)
   - xUnit Framework effektiv einsetzen

8. **Continuous Integration meistern**
   - Mehrmals täglich integrieren
   - Collective Code Ownership leben
   - Keine Code-Branches (außer kurzfristig)

9. **Refactoring als Routine**
   - "Say everything once and only once" (DRY)
   - Simple Design beibehalten
   - Code Quality durch ständige Verbesserung

10. **Release Planning steuern**
    - Scope Management statt Date Management
    - Velocity-basierte Predictions
    - Mit Business Value priorisieren

### Experte (5+ Jahre Erfahrung)

Du vertiefst:

11. **Projektsteuerung durch Metriken**
    - Resources, Scope, Quality, Time tracken
    - Defect Handling (nicht "Bugs"!)
    - Steering durch kontinuierliche Anpassung

12. **Infrastructure as Stories**
    - YAGNI (You Ain't Gonna Need It) konsequent anwenden
    - Database-Development inkrementell
    - Technische Tasks mit Business Value verknüpfen

13. **Team-Dynamik optimieren**
    - On-site Customer Vorteile maximieren
    - "It's Chet's Fault" - Team Ownership
    - Balancing Hopes and Fears

14. **XP in verschiedenen Kontexten**
    - Remote Customer Strategien
    - Java vs. Smalltalk Perspektiven
    - XP für Legacy-Integration

15. **Estimates vs. Promises**
    - Die Unmöglichkeit exakter Vorhersagen akzeptieren
    - Transparenz und Tracking über Zusagen
    - Kontinuierliche Re-Estimation

## Modul-Struktur (12-16 Wochen)

### Modul 1: Foundation - XP Rollen und Rechte (Wochen 1-2)

**Theorie:**
- Die drei Rollen (Customer, Programmer, Manager)
- Rights and Responsibilities Framework
- Circle of Life: Define → Estimate → Choose → Build

**Praxis:**
```plaintext
# Customer Rights Exercise
1. Schreibe 5 User Stories für ein fiktives Projekt
2. Priorisiere sie nach Business Value
3. Definiere Acceptance Criteria für Story #1

# Programmer Rights Exercise  
1. Schätze die 5 Stories in Perfect Engineering Days
2. Berechne Velocity mit Faktor 1/3
3. Erstelle einen 3-Iteration Release Plan
```

**Checkpoint:**
- Kannst du erklären, warum XP zwischen Estimate und Promise unterscheidet?
- Verstehst du, wie Circle of Life funktioniert?

### Modul 2: User Stories & Acceptance Tests (Wochen 3-4)

**Theorie:**
- Stories als "Promise for Conversation"
- Story-Größe: 1-3 Wochen pro Programmer
- Acceptance Tests automatisieren
- "Test everything that could possibly break"

**Praxis - Story Writing Workshop:**
```markdown
# User Story Template
Als [Rolle]
möchte ich [Feature]
damit [Business Value]

Akzeptanzkriterien:
- [ ] Kriterium 1
- [ ] Kriterium 2
- [ ] Kriterium 3

Schätzung: ___ Perfect Engineering Days
```

**Code-Beispiel - Automated Acceptance Test (Java):**
```java
// AccountTest.java - Acceptance Test Example
import org.junit.Test;
import static org.junit.Assert.*;

public class AccountAcceptanceTest {
    
    @Test
    public void testDepositIncreasesBalance() {
        // Story: "User can deposit money into account"
        Account account = new Account();
        account.deposit(100.0);
        
        assertEquals("Balance after deposit", 
                     100.0, 
                     account.getBalance(), 
                     0.01);
    }
    
    @Test
    public void testWithdrawalDecreasesBalance() {
        // Story: "User can withdraw money from account"
        Account account = new Account();
        account.deposit(100.0);
        account.withdraw(30.0);
        
        assertEquals("Balance after withdrawal", 
                     70.0, 
                     account.getBalance(), 
                     0.01);
    }
    
    @Test
    public void testOverdraftProtection() {
        // Story: "System transfers from overdraft account"
        Account checking = new Account();
        Account savings = new Account();
        checking.setOverdraftProtection(savings);
        
        savings.deposit(100.0);
        checking.withdraw(50.0); // Checking has 0 balance
        
        assertEquals("Overdraft used", 50.0, savings.getBalance(), 0.01);
    }
}
```

**Praktisches Projekt 1: Story-driven Mini-App (Woche 4)**
Entwickle ein einfaches Todo-System:
- 5-8 User Stories schreiben
- Acceptance Tests für jede Story definieren
- Stories schätzen und priorisieren

### Modul 3: Planning Game - Iterations und Releases (Wochen 5-6)

**Theorie:**
- Small Releases (2-3 Monate)
- Short Iterations (2-3 Wochen)
- Velocity Measurement
- "Yesterday's Weather" Prediction

**Praxis - Iteration Planning Meeting:**
```plaintext
# Iteration Planning Template

Team Velocity: 12 Story Points/Iteration
Available: 3 Programmers × 3 Weeks × 1/3 = 3 Weeks Capacity

Stories für Iteration #1:
[ ] Story A (1.0 weeks) - Sign up: Alice
[ ] Story B (0.5 weeks) - Sign up: Bob  
[ ] Story C (1.5 weeks) - Sign up: Carol

Total: 3.0 weeks ✓

Quick Design Session für Story C:
- CRC Cards session (15 min)
- Identify main classes
- Sketch responsibilities
```

**Code-Beispiel - Velocity Tracker (Python):**
```python
# velocity_tracker.py
from dataclasses import dataclass
from typing import List
from datetime import date

@dataclass
class Story:
    name: str
    estimate: float  # in perfect engineering days
    actual: float = 0.0
    completed: bool = False

class Iteration:
    def __init__(self, number: int, planned_stories: List[Story]):
        self.number = number
        self.stories = planned_stories
        self.start_date = date.today()
        
    def complete_story(self, story_name: str, actual_days: float):
        for story in self.stories:
            if story.name == story_name:
                story.actual = actual_days
                story.completed = True
                break
                
    def get_velocity(self) -> float:
        """Actual velocity in story points per iteration"""
        completed = [s for s in self.stories if s.completed]
        return sum(s.estimate for s in completed)
    
    def get_accuracy(self) -> float:
        """How accurate were our estimates?"""
        completed = [s for s in self.stories if s.completed]
        if not completed:
            return 0.0
        total_estimate = sum(s.estimate for s in completed)
        total_actual = sum(s.actual for s in completed)
        return total_estimate / total_actual if total_actual > 0 else 0.0

class Project:
    def __init__(self, name: str):
        self.name = name
        self.iterations: List[Iteration] = []
        
    def add_iteration(self, iteration: Iteration):
        self.iterations.append(iteration)
        
    def get_average_velocity(self) -> float:
        """Yesterday's Weather prediction"""
        if not self.iterations:
            return 0.0
        velocities = [it.get_velocity() for it in self.iterations]
        return sum(velocities) / len(velocities)
    
    def predict_completion(self, remaining_stories: List[Story]) -> int:
        """How many iterations to complete remaining stories?"""
        avg_velocity = self.get_average_velocity()
        if avg_velocity == 0:
            return -1  # Can't predict yet
        total_points = sum(s.estimate for s in remaining_stories)
        return int(total_points / avg_velocity) + 1

# Usage Example
if __name__ == "__main__":
    project = Project("E-Commerce Platform")
    
    # Iteration 1
    it1 = Iteration(1, [
        Story("User Login", 2.0),
        Story("Product Catalog", 3.0),
        Story("Shopping Cart", 2.5)
    ])
    it1.complete_story("User Login", 2.5)
    it1.complete_story("Product Catalog", 3.5)
    it1.complete_story("Shopping Cart", 2.0)
    project.add_iteration(it1)
    
    print(f"Iteration 1 Velocity: {it1.get_velocity()} points")
    print(f"Iteration 1 Accuracy: {it1.get_accuracy():.2%}")
    
    # Remaining stories
    backlog = [
        Story("Payment Processing", 3.0),
        Story("Order History", 2.0),
        Story("Admin Dashboard", 4.0)
    ]
    
    iterations_needed = project.predict_completion(backlog)
    print(f"Estimated iterations to complete: {iterations_needed}")
```

**Checkpoint:**
- Kannst du eine Iteration planen mit gegebener Velocity?
- Verstehst du, wie "Yesterday's Weather" funktioniert?

### Modul 4: Programming Practices - Pair Programming & TDD (Wochen 7-8)

**Theorie:**
- Pair Programming: Driver & Navigator
- Test-First Development
- Test by Intention (nicht Implementation)
- xUnit Framework

**Praxis - Pair Programming Session:**
```plaintext
# Pair Programming Protocol

Driver: Schreibt den Code
- Denkt laut
- Fokussiert auf Syntax und Details

Navigator: Reviewt den Code  
- Denkt strategisch
- Achtet auf Design und Alternativen

Rotation: Alle 30 Minuten wechseln
```

**Code-Beispiel - Test-First by Intention (Java):**
```java
// Example from Chapter 14: Test-first, by Intention
// We want to implement a simple money calculator

// STEP 1: Write the test FIRST - express intention
@Test
public void testSimpleAddition() {
    // What do we WANT to happen?
    Money sum = Money.dollar(5).plus(Money.dollar(5));
    assertEquals(Money.dollar(10), sum);
}

// STEP 2: Make it compile (stub out classes)
class Money {
    static Money dollar(int amount) {
        return null; // TODO
    }
    Money plus(Money addend) {
        return null; // TODO
    }
}

// STEP 3: Make it run (simplest implementation)
class Money {
    private int amount;
    
    private Money(int amount) {
        this.amount = amount;
    }
    
    static Money dollar(int amount) {
        return new Money(amount);
    }
    
    Money plus(Money addend) {
        return new Money(this.amount + addend.amount);
    }
    
    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Money)) return false;
        Money other = (Money) obj;
        return this.amount == other.amount;
    }
}

// STEP 4: Refactor (only if needed)
// In this case, the code is already simple enough
```

**Unit Test Beispiel - "Test everything that could possibly break":**
```python
# account.py - Implementation
from typing import List

class Transaction:
    def __init__(self, amount: float):
        self.amount = amount
    
    @classmethod
    def deposit(cls, amount: float):
        return cls(amount)
    
    @classmethod  
    def withdraw(cls, amount: float):
        return cls(-amount)
    
    def value(self) -> float:
        return self.amount

class Account:
    def __init__(self):
        self._transactions: List[Transaction] = []
    
    def add(self, transaction: Transaction):
        self._transactions.append(transaction)
    
    def balance(self) -> float:
        return sum(t.value() for t in self._transactions)

# test_account.py - Unit Tests
import unittest

class TestAccount(unittest.TestCase):
    
    def test_empty_account(self):
        """Test simplest case first"""
        account = Account()
        self.assertEqual(0, account.balance())
    
    def test_single_deposit(self):
        """Test single transaction"""
        account = Account()
        account.add(Transaction.deposit(100))
        self.assertEqual(100, account.balance())
    
    def test_multiple_transactions(self):
        """Test the real scenario"""
        account = Account()
        account.add(Transaction.deposit(100))
        account.add(Transaction.withdraw(15))
        account.add(Transaction.withdraw(25))
        self.assertEqual(60, account.balance())
    
    def test_withdrawal_before_deposit(self):
        """Test edge case - negative balance allowed?"""
        account = Account()
        account.add(Transaction.withdraw(50))
        self.assertEqual(-50, account.balance())

if __name__ == '__main__':
    unittest.main()
```

**Praktisches Projekt 2: TDD Kata (Woche 8)**
Implementiere "Bowling Game Scorer" mit TDD:
- Schreibe Tests ZUERST
- Arbeite in Pairs (wenn möglich)
- Refactore nach jedem grünen Test

### Modul 5: Continuous Integration & Collective Ownership (Wochen 9-10)

**Theorie:**
- Continuous Integration (mehrmals täglich!)
- Collective Code Ownership
- No Branches (außer kurzfristig)
- Coding Standards

**Praxis - Integration Rules:**
```plaintext
# Integration Protocol

1. Update from repository
2. Run ALL tests (unit + acceptance)
3. If tests fail, fix immediately
4. Integrate your changes
5. Run ALL tests again
6. If fail, rollback

Integration frequency: Every 2-3 hours
Never leave code unintegrated overnight
```

**Code-Beispiel - Simple Integration Script (Bash):**
```bash
#!/bin/bash
# integrate.sh - Simple CI Script

echo "=== Starting Integration ==="

# Step 1: Update from repository
echo "Pulling latest changes..."
git pull origin main
if [ $? -ne 0 ]; then
    echo "ERROR: Pull failed. Resolve conflicts first."
    exit 1
fi

# Step 2: Run all tests
echo "Running unit tests..."
python -m pytest tests/
if [ $? -ne 0 ]; then
    echo "ERROR: Unit tests failed. Fix before integrating."
    exit 1
fi

echo "Running acceptance tests..."
python -m pytest acceptance_tests/
if [ $? -ne 0 ]; then
    echo "ERROR: Acceptance tests failed."
    exit 1
fi

# Step 3: Integrate changes
echo "Pushing changes..."
git push origin main
if [ $? -ne 0 ]; then
    echo "ERROR: Push failed."
    exit 1
fi

echo "=== Integration Successful ==="
```

**Refactoring Example - Extract Method:**
```python
# BEFORE - Complex method, hard to test
def print_accounts(accounts):
    for account in accounts:
        print(f"Account: {account.number}")
        total = 0
        for transaction in account.transactions:
            total += transaction.amount
            print(f"  {transaction.date}: {transaction.amount}")
        print(f"  Balance: {total}")
        print()

# AFTER - Refactored for testability
def calculate_balance(transactions):
    """Extracted calculation logic - easily testable"""
    return sum(t.amount for t in transactions)

def format_transaction(transaction):
    """Extracted formatting logic"""
    return f"  {transaction.date}: {transaction.amount}"

def print_account(account):
    """Main method now just orchestrates"""
    print(f"Account: {account.number}")
    for transaction in account.transactions:
        print(format_transaction(transaction))
    balance = calculate_balance(account.transactions)
    print(f"  Balance: {balance}")
    print()

def print_accounts(accounts):
    for account in accounts:
        print_account(account)

# Now we can test each piece independently!
def test_calculate_balance():
    transactions = [
        Transaction(date="2024-01-01", amount=100),
        Transaction(date="2024-01-02", amount=-30)
    ]
    assert calculate_balance(transactions) == 70
```

**Checkpoint:**
- Integrierst du mindestens 2-3x täglich?
- Kannst du fremden Code ohne Angst ändern?

### Modul 6: Design & Refactoring (Wochen 11-12)

**Theorie:**
- Simple Design: "Do the simplest thing that could possibly work"
- "Say everything once and only once" (DRY)
- Quick Design Sessions mit CRC Cards
- Emergent Design vs. Big Design Up Front

**Praxis - CRC Card Session:**
```plaintext
# CRC Card Example

Class: Account
------------------------
Responsibilities:
- Track transactions
- Calculate balance
- Apply transaction

Collaborators:
- Transaction
- TransactionRepository
------------------------

Class: Transaction  
------------------------
Responsibilities:
- Store amount
- Store date
- Validate amount

Collaborators:
- (none)
------------------------
```

**Code-Beispiel - Progressive Refactoring:**
```java
// Evolution of a design through refactoring

// VERSION 1: First working version
class PayrollCalculator {
    public double calculatePay(Employee emp) {
        double gross = emp.hoursWorked * emp.hourlyRate;
        double tax = gross * 0.2;
        double unionDues = 0;
        if (emp.union != null) {
            unionDues = emp.union.getDues();
        }
        return gross - tax - unionDues;
    }
}

// VERSION 2: Extract deductions
class PayrollCalculator {
    public double calculatePay(Employee emp) {
        double gross = calculateGross(emp);
        double deductions = calculateDeductions(emp, gross);
        return gross - deductions;
    }
    
    private double calculateGross(Employee emp) {
        return emp.hoursWorked * emp.hourlyRate;
    }
    
    private double calculateDeductions(Employee emp, double gross) {
        double tax = calculateTax(gross);
        double unionDues = calculateUnionDues(emp);
        return tax + unionDues;
    }
    
    private double calculateTax(double gross) {
        return gross * 0.2;
    }
    
    private double calculateUnionDues(Employee emp) {
        return emp.union != null ? emp.union.getDues() : 0;
    }
}

// VERSION 3: Extract classes (Single Responsibility)
class GrossPayCalculator {
    public double calculate(Employee emp) {
        return emp.hoursWorked * emp.hourlyRate;
    }
}

class TaxCalculator {
    private static final double TAX_RATE = 0.2;
    
    public double calculate(double gross) {
        return gross * TAX_RATE;
    }
}

class UnionDuesCalculator {
    public double calculate(Employee emp) {
        return emp.union != null ? emp.union.getDues() : 0;
    }
}

class PayrollCalculator {
    private GrossPayCalculator grossCalc = new GrossPayCalculator();
    private TaxCalculator taxCalc = new TaxCalculator();
    private UnionDuesCalculator duesCalc = new UnionDuesCalculator();
    
    public double calculatePay(Employee emp) {
        double gross = grossCalc.calculate(emp);
        double tax = taxCalc.calculate(gross);
        double dues = duesCalc.calculate(emp);
        return gross - tax - dues;
    }
}

// Each class now has ONE reason to change
// Each class is easily testable
// Design emerged through refactoring, not big design up front
```

**Praktisches Projekt 3: Refactoring Legacy Code (Woche 12)**
Nimm ein kleines Legacy-Projekt und:
- Schreibe Characterization Tests
- Refactore schrittweise
- Behalte Tests grün

### Modul 7: Steering & Metrics (Wochen 13-14)

**Theorie:**
- Resources, Scope, Quality, Time
- Velocity Tracking
- Defect Handling (nicht "Bugs"!)
- Burn-down Charts

**Praxis - Project Dashboard:**
```python
# project_dashboard.py
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class ProjectDashboard:
    def __init__(self, total_story_points: int, 
                 iterations_planned: int,
                 average_velocity: float):
        self.total_points = total_story_points
        self.iterations = iterations_planned
        self.velocity = average_velocity
        self.completed_points = []
        
    def add_iteration_result(self, points_completed: float):
        self.completed_points.append(points_completed)
        
    def plot_burndown(self):
        """Visualize project progress"""
        iterations = list(range(len(self.completed_points) + 1))
        remaining = [self.total_points]
        
        for points in self.completed_points:
            remaining.append(remaining[-1] - points)
        
        # Ideal burndown line
        ideal = [self.total_points - (i * self.velocity) 
                 for i in iterations]
        
        plt.figure(figsize=(10, 6))
        plt.plot(iterations, remaining, 'b-o', label='Actual', linewidth=2)
        plt.plot(iterations, ideal, 'r--', label='Ideal', linewidth=2)
        plt.xlabel('Iteration')
        plt.ylabel('Story Points Remaining')
        plt.title('Project Burn-down Chart')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()
        
    def predict_completion(self) -> int:
        """When will we finish?"""
        if not self.completed_points:
            return self.iterations
        
        actual_velocity = sum(self.completed_points) / len(self.completed_points)
        current_remaining = self.total_points - sum(self.completed_points)
        iterations_needed = int(current_remaining / actual_velocity) + 1
        
        return len(self.completed_points) + iterations_needed
    
    def status_report(self) -> str:
        """Generate status report"""
        completed_iterations = len(self.completed_points)
        completed_total = sum(self.completed_points)
        remaining = self.total_points - completed_total
        
        if completed_iterations > 0:
            actual_velocity = completed_total / completed_iterations
        else:
            actual_velocity = 0
        
        predicted_completion = self.predict_completion()
        
        return f"""
Project Status Report
=====================
Total Story Points: {self.total_points}
Completed: {completed_total} ({completed_total/self.total_points:.1%})
Remaining: {remaining}

Iterations Completed: {completed_iterations}
Planned Velocity: {self.velocity:.1f} pts/iteration
Actual Velocity: {actual_velocity:.1f} pts/iteration

Original Plan: {self.iterations} iterations
Current Prediction: {predicted_completion} iterations
Variance: {predicted_completion - self.iterations:+d} iterations
"""

# Usage
dashboard = ProjectDashboard(
    total_story_points=100,
    iterations_planned=10,
    average_velocity=10.0
)

# After iteration 1: completed 12 points
dashboard.add_iteration_result(12.0)
# After iteration 2: completed 9 points  
dashboard.add_iteration_result(9.0)
# After iteration 3: completed 11 points
dashboard.add_iteration_result(11.0)

print(dashboard.status_report())
dashboard.plot_burndown()
```

**Defect Tracking:**
```python
# defect.py - Not "bugs", but "defects"
from enum import Enum
from dataclasses import dataclass
from datetime import datetime

class DefectPriority(Enum):
    CRITICAL = 1  # System down
    HIGH = 2      # Major feature broken
    MEDIUM = 3    # Minor feature broken  
    LOW = 4       # Cosmetic issue

@dataclass
class Defect:
    id: int
    description: str
    priority: DefectPriority
    story: str
    reported: datetime
    resolved: datetime = None
    
    def as_story(self) -> str:
        """Convert defect to a story for scheduling"""
        return f"Fix: {self.description} (in {self.story})"

class DefectTracker:
    def __init__(self):
        self.defects = []
        self.next_id = 1
        
    def report(self, description: str, priority: DefectPriority, 
               story: str) -> Defect:
        """Report a new defect"""
        defect = Defect(
            id=self.next_id,
            description=description,
            priority=priority,
            story=story,
            reported=datetime.now()
        )
        self.defects.append(defect)
        self.next_id += 1
        
        # Critical defects: write a test immediately
        if priority == DefectPriority.CRITICAL:
            print(f"⚠️  CRITICAL DEFECT #{defect.id}: Write test NOW!")
        
        return defect
    
    def get_open_defects(self):
        """Get unresolved defects"""
        return [d for d in self.defects if d.resolved is None]
    
    def to_stories(self):
        """Convert open defects to stories for iteration planning"""
        return [d.as_story() for d in self.get_open_defects()]
```

**Checkpoint:**
- Kannst du Velocity tracken und Completion vorhersagen?
- Behandelst du Defects als Stories?

### Modul 8: Advanced Topics & War Stories (Wochen 15-16)

**Theorie:**
- Infrastructure as Stories (YAGNI!)
- Estimates vs. Promises
- Remote Customer Strategies
- Balancing Hopes and Fears

**War Stories aus dem Buch:**

1. **"It's Chet's Fault"**
   - Team Ownership statt Blame Game
   - Jeder ist verantwortlich für alles

2. **"A True Story" (Ron Jeffries)**
   - Über-Engineering vermeiden
   - Das einfachste, das funktionieren könnte

3. **"We'll Try"**
   - Realistische Estimates vs. Hoffnungsbasierte Zusagen
   - Velocity und Transparenz

**Code-Beispiel - YAGNI in Practice:**
```python
# Bad: Building infrastructure "just in case"
class DatabaseAbstractionLayer:
    """Support for multiple databases"""
    def __init__(self, db_type='postgres'):
        if db_type == 'postgres':
            self.connection = PostgresConnection()
        elif db_type == 'mysql':
            self.connection = MySQLConnection()
        elif db_type == 'oracle':
            self.connection = OracleConnection()
        # ... 5 more database types we might need someday
    
    # ... complex abstraction layer

# Good: Simple solution for actual need
class DataStore:
    """Simple file-based storage for our current needs"""
    def __init__(self, filename='data.json'):
        self.filename = filename
        
    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)
    
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

# Later, when you ACTUALLY need a database:
# 1. Write the database Story
# 2. Refactor DataStore to use database
# 3. Existing tests ensure nothing breaks
```

**Praktisches Projekt 4: Mini-XP-Projekt (Wochen 15-16)**

Entwickle in einem 2-Wochen-Sprint ein kleines Projekt:

**Tag 1-2: Planning**
- 10-15 User Stories schreiben
- Stories schätzen
- Release Plan erstellen
- Iteration 1 planen (1 Woche)

**Tag 3-7: Iteration 1**
- Pair Programming
- Test-First Development
- Continuous Integration
- Daily Stand-ups

**Tag 8: Iteration Review**
- Demo für "Customer"
- Velocity messen
- Retrospective

**Tag 9-10: Iteration 2 Planning**
- Re-estimate basierend auf Velocity
- Scope anpassen falls nötig
- Neue Stories priorisieren

**Tag 11-14: Iteration 2**
- Weiter entwickeln
- Refactoring
- Acceptance Tests

**Tag 15: Release**
- Final Demo
- Lessons Learned
- Metrics Review

## Code-Beispiele und Patterns

### Pattern 1: Story Card Object

```java
// StoryCard.java - Representing a User Story
public class StoryCard {
    private String title;
    private String description;
    private double estimate; // in perfect engineering days
    private double actual;
    private Priority priority;
    private Status status;
    private List<AcceptanceTest> tests;
    
    public enum Priority {
        CRITICAL, HIGH, MEDIUM, LOW
    }
    
    public enum Status {
        TODO, IN_PROGRESS, DONE
    }
    
    public StoryCard(String title, String description, double estimate) {
        this.title = title;
        this.description = description;
        this.estimate = estimate;
        this.status = Status.TODO;
        this.tests = new ArrayList<>();
    }
    
    public void addAcceptanceTest(AcceptanceTest test) {
        tests.add(test);
    }
    
    public boolean isComplete() {
        return status == Status.DONE && 
               tests.stream().allMatch(AcceptanceTest::passes);
    }
    
    public double velocity() {
        return status == Status.DONE ? estimate : 0;
    }
}
```

### Pattern 2: Velocity Tracker

```javascript
// velocityTracker.js - Track team velocity
class VelocityTracker {
    constructor() {
        this.iterations = [];
    }
    
    addIteration(plannedPoints, completedPoints) {
        this.iterations.push({
            planned: plannedPoints,
            completed: completedPoints,
            date: new Date()
        });
    }
    
    getAverageVelocity(lastN = 3) {
        const recent = this.iterations.slice(-lastN);
        const total = recent.reduce((sum, it) => sum + it.completed, 0);
        return total / recent.length;
    }
    
    predictCompletion(remainingPoints) {
        const velocity = this.getAverageVelocity();
        return Math.ceil(remainingPoints / velocity);
    }
    
    getLoadFactor() {
        // How much work can we really do vs. what we plan?
        const recent = this.iterations.slice(-3);
        const totalPlanned = recent.reduce((sum, it) => sum + it.planned, 0);
        const totalCompleted = recent.reduce((sum, it) => sum + it.completed, 0);
        return totalCompleted / totalPlanned;
    }
}

// Usage
const tracker = new VelocityTracker();
tracker.addIteration(20, 18); // Iteration 1
tracker.addIteration(20, 22); // Iteration 2  
tracker.addIteration(20, 19); // Iteration 3

console.log(`Average Velocity: ${tracker.getAverageVelocity()}`);
console.log(`Load Factor: ${tracker.getLoadFactor()}`);
console.log(`Iterations for 60 points: ${tracker.predictCompletion(60)}`);
```

### Pattern 3: Test-First Template

```python
# test_first_template.py
import unittest

# STEP 1: Write the test FIRST
class TestFeatureX(unittest.TestCase):
    
    def test_basic_behavior(self):
        """Test the simplest case"""
        # Arrange: Set up the test data
        sut = SystemUnderTest()
        
        # Act: Call the method
        result = sut.do_something()
        
        # Assert: Verify the result
        self.assertEqual(expected_value, result)
    
    def test_edge_case(self):
        """Test boundary conditions"""
        pass
    
    def test_error_handling(self):
        """Test exception cases"""
        pass

# STEP 2: Make it compile (stub implementation)
class SystemUnderTest:
    def do_something(self):
        pass  # TODO: Implement

# STEP 3: Make it run (simplest implementation that works)
class SystemUnderTest:
    def do_something(self):
        return expected_value  # Hardcoded!

# STEP 4: Refactor (add real logic, improve design)
class SystemUnderTest:
    def do_something(self):
        # Real implementation here
        return computed_value
```

## XP Practices Cheat Sheet

### Planning
- ✅ User Stories on index cards
- ✅ Acceptance Tests define "done"
- ✅ Estimate in Perfect Engineering Days
- ✅ Use Velocity for planning
- ✅ Small Releases (2-3 months)
- ✅ Short Iterations (2-3 weeks)
- ✅ Customer prioritizes by business value

### Coding
- ✅ Test-First Development
- ✅ Pair Programming (all production code)
- ✅ Simple Design
- ✅ Refactoring constantly
- ✅ Collective Code Ownership
- ✅ Continuous Integration
- ✅ Coding Standards

### Testing
- ✅ Unit Tests for everything that could break
- ✅ Automated Acceptance Tests
- ✅ All tests run 100% before integration
- ✅ Tests as documentation

### Management
- ✅ On-site Customer
- ✅ Daily Stand-up meetings
- ✅ Velocity tracking
- ✅ Honest estimation
- ✅ Scope management (not date management)

## Häufige Fehler und Lösungen

### Fehler 1: "We'll Try"
**Problem:** Management fordert mehr als Velocity erlaubt.
**Lösung:** 
- Zeige die Zahlen (Velocity, Remaining Stories)
- Biete Scope-Reduktion an
- Bleibe ehrlich bei Estimates
- "We'll try" = "We'll fail"

### Fehler 2: Guru Checks Output
**Problem:** Manuelle Überprüfung von Test-Ergebnissen.
**Lösung:**
- Automatisiere ALLE Tests
- Vergleiche mit gespeicherten "guten" Outputs
- Keine visuelle Inspektion von Reports

### Fehler 3: Infrastructure-First
**Problem:** Monate für Framework/Database bevor erste Story.
**Lösung:**
- YAGNI - You Ain't Gonna Need It
- Verknüpfe Infrastructure mit Business Value
- Inkrementell: File → Database wenn wirklich nötig

### Fehler 4: Solo Programming
**Problem:** "Pair Programming ist zu langsam."
**Lösung:**
- Pairing ist schneller (weniger Debugging!)
- Bessere Code-Qualität
- Knowledge Sharing
- Versuch es 2 Wochen ehrlich

### Fehler 5: Late Integration
**Problem:** Code wird tagelang nicht integriert.
**Lösung:**
- Integrate 2-3x täglich
- Alle Tests müssen grün sein
- Kleine Integrationen = weniger Konflikte

## Self-Assessment

### Nach Modul 4 (Woche 8)
- [ ] Ich kann User Stories auf Karteikarten schreiben
- [ ] Ich kann Stories in Perfect Engineering Days schätzen
- [ ] Ich verstehe Velocity und kann sie nutzen
- [ ] Ich schreibe Tests VOR dem Code
- [ ] Ich habe mindestens 8 Stunden Pair Programming gemacht

### Nach Modul 8 (Woche 16)  
- [ ] Ich habe ein komplettes XP-Mini-Projekt durchgeführt
- [ ] Ich tracke Velocity und kann Completion vorhersagen
- [ ] Ich refactore regelmäßig und halte Code einfach
- [ ] Ich integriere mehrmals täglich
- [ ] Ich verstehe "Estimates ≠ Promises"

## Weiterführende Ressourcen

### Bücher
- **"Extreme Programming Explained"** - Kent Beck (die Philosophie)
- **"Test-Driven Development By Example"** - Kent Beck (TDD-Praxis)
- **"Refactoring"** - Martin Fowler (wie man Code verbessert)
- **"The Pragmatic Programmer"** - Hunt & Thomas (Handwerkskunst)

### Online
- **XProgramming.com** - Ron Jeffries' Website mit Artikeln
- **JUnit.org** - Test Framework für Java
- **PyTest** - Test Framework für Python

### Tools
- **JUnit** / **PyTest** / **NUnit** - Unit Testing Frameworks
- **Git** - Version Control für Continuous Integration
- **Physical Index Cards** - Für User Stories (ja, wirklich!)

## Praktische Übungen

### Übung 1: Story Writing Workshop
Schreibe 20 User Stories für ein fiktives Projekt (z.B. Online-Bibliothek):
- Jede Story: 1-3 Wochen Aufwand
- Priorisiere nach Business Value
- Definiere Acceptance Criteria

### Übung 2: Estimation Game
Nimm deine 20 Stories:
- Schätze in Perfect Engineering Days
- Berechne Velocity mit Faktor 1/3
- Erstelle 4-Iteration Release Plan
- Simuliere: Nach Iteration 1 nur 60% Velocity → Re-plan!

### Übung 3: Test-First Kata
Implementiere "Roman Numerals Converter":
- Schreibe JEDEN Test zuerst
- Refactore nach jedem grünen Test
- Stoppe bei allen Tests grün

### Übung 4: Pair Programming Session
Finde einen Partner und implementiert gemeinsam "FizzBuzz":
- Wechselt alle 5 Minuten Driver/Navigator
- Test-First Development
- Refactoring am Ende

### Übung 5: Velocity Simulation
Simuliere 10 Iterationen:
- Plane mit Velocity 10 pts/iteration
- Würfel für tatsächliche Velocity (7-13)
- Update Predictions nach jeder Iteration
- Beobachte Convergence

## Zitate aus dem Buch

> "Test everything that could possibly break. What does this mean? How is it possible?"

> "Do the simplest thing that could possibly work."

> "YAGNI: You Aren't Gonna Need It."

> "It's Chet's Fault." - Team Ownership Card

> "We estimate how long the project will take. We promise to tell the truth about how we're doing."

> "Extreme Programming is a discipline of software development with values of simplicity, communication, feedback and courage."

## Zusammenfassung

**Extreme Programming Installed** ist der praktische Begleiter zu Kent Becks philosophischem Werk. Es zeigt dir:

1. **Wie man ein XP-Projekt startet** - Von ersten Stories bis Release Plan
2. **Wie man XP praktiziert** - Pair Programming, TDD, Continuous Integration
3. **Wie man XP steuert** - Velocity, Metrics, Scope Management
4. **Wie man XP anpasst** - Für verschiedene Kontexte und Teams

Die drei Autoren waren **dabei, als XP erfunden wurde**. Ihre Erfahrungen aus dem C3-Projekt bei Chrysler, ihre Fehler und Erfolge, ihre "War Stories" machen dieses Buch zu einem unverzichtbaren Guide.

**Der Unterschied zu anderen Methodologien:**
- Keine monatelange Planungsphase
- Keine dicken Spezifikationsdokumente
- Keine starren Prozesse
- Stattdessen: Kurze Zyklen, schnelles Feedback, kontinuierliche Anpassung

**Die Kernbotschaft:**
XP funktioniert, weil es die Realität akzeptiert:
- Anforderungen ändern sich
- Schätzungen sind ungenau
- Code wird komplex
- Menschen machen Fehler

XP begegnet dem mit:
- Flexibilität (User Stories, kurze Iterationen)
- Transparenz (Velocity, ehrliche Estimates)
- Qualität (TDD, Refactoring, Pair Programming)
- Mut (Collective Ownership, Simple Design)

Viel Erfolg bei deiner XP-Reise! 🚀
