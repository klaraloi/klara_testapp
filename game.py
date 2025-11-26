import sys
import random


class Character:
    def __init__(self, player_name: str, role: str, hp: int, atk: int, df: int, spd: int, desc: str, symbol: str = "👤", ability: str = "", ability_desc: str = ""):
        self.player_name = player_name
        self.role = role
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spd = spd
        self.desc = desc
        self.symbol = symbol
        self.ability = ability
        self.ability_desc = ability_desc
        self.ability_ready = True  # Track if ability is ready to use

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount: int):
        self.hp = max(0, self.hp - amount)

    def __str__(self):
        return f"{self.symbol} {self.player_name} ({self.role}) HP:{self.hp}/{self.max_hp} ATK:{self.atk} DEF:{self.df} SPD:{self.spd}"


CHAR_TEMPLATES = {
    "1": {
        "role": "Ritter", 
        "desc": "Stark in Verteidigung - Der Waechter des Waldes",
        "lore": "Ein tapferer Ritter mit Schwert und Schild. Bekannt fuer seine Staerke und Ausdauer.",
        "symbol": "[K]",
        "hp": 140, "atk": 11, "df": 12, "spd": 3,
        "ability": "Schildschlag",
        "ability_desc": "Blockiert 50% des naechsten Schadens"
    },
    "2": {
        "role": "Zauberer", 
        "desc": "Starker Zauberschaden - Der mystische Gelehrte",
        "lore": "Ein maechtiger Zauberer mit arcaner Magie. Kann Monster mit Feuerzaubern vernichten.",
        "symbol": "[Z]",
        "hp": 85, "atk": 18, "df": 5, "spd": 6,
        "ability": "Feuerzauber",
        "ability_desc": "Verursacht doppelten Schaden beim naechsten Angriff"
    },
    "3": {
        "role": "Dieb", 
        "desc": "Hohe Geschicklichkeit - Der Schattenlaeufer",
        "lore": "Ein flinker Dieb aus den Schatten. Nutzt Geschwindigkeit und List, um Gegner zu besiegen.",
        "symbol": "[D]",
        "hp": 100, "atk": 13, "df": 7, "spd": 9,
        "ability": "Hinterhalt",
        "ability_desc": "Greift zweimal hintereinander an"
    },
    "4": {
        "role": "Bogenschuetze", 
        "desc": "Gute Reichweite - Der Wildnis-Jaeger",
        "lore": "Ein geschickter Bogenschuetze aus dem Wald. Trifft seine Gegner aus großer Entfernung.",
        "symbol": "[B]",
        "hp": 115, "atk": 14, "df": 8, "spd": 7,
        "ability": "Praezisionsschuss",
        "ability_desc": "Garantiert kritischen Treffer (1,5x Schaden)"
    },
}

MATERIAL_TYPES = ["holz", "stein", "gras"]


# ASCII Art für Charaktere
CHARACTER_ASCII = {
    "Ritter": """
    [RITTER]
      |O_O|
      |=|=|
      |   |
     /| | |\\
      | | |
     /| | |\\
    """,
    "Zauberer": """
    [ZAUBERER]
      (o o)
      /| |\\
      / | \\
       /|\\
      / | \\
    """,
    "Dieb": """
    [DIEB]
     /o_o\\
     |~~~|
    /| | |\\
     | | |
    /| | |\\
    """,
    "Bogenschütze": """
    [BOGENSCHUETZE]
      (o_o)
      >-|-<
      /| |\\
       | |
      /| |\\
    """
}

# ASCII Art für Monster
MONSTER_ASCII = {
    "Goblin": """
    [GOBLIN]
      />_<\\
      |~u~|
     /| | |\\
      | | |
     /| | |\\
    """,
    "Ork_Boss": """
    [ORK BOSS]
      /o^o\\
      |XXX|
     /|XXX|\\
      |XXX|
     /|XXX|\\
    """
}


def choose_char(player_name: str) -> Character:
    print(f"\n{player_name}, wähle deinen Charakter:")
    for k, tmpl in CHAR_TEMPLATES.items():
        print(f"\n{k}. {tmpl['symbol']} {tmpl['role']} - {tmpl['desc']}")
        print(f"   Lore: {tmpl['lore']}")
        print(f"   Fähigkeit: {tmpl['ability']} - {tmpl['ability_desc']}")
        print(f"   Stats: HP {tmpl['hp']}, ATK {tmpl['atk']}, DEF {tmpl['df']}, SPD {tmpl['spd']}")
    while True:
        choice = input("\nNummer eingeben (1-4): ").strip()
        if choice in CHAR_TEMPLATES:
            t = CHAR_TEMPLATES[choice]
            return Character(player_name, t['role'], t['hp'], t['atk'], t['df'], t['spd'], t['desc'], t['symbol'], t['ability'], t['ability_desc'])
        print("Ungültige Wahl. Bitte 1-4 eingeben.")


class Monster:
    def __init__(self, name: str, hp: int, atk: int, df: int, spd: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spd = spd

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount: int):
        self.hp = max(0, self.hp - amount)

    def __str__(self):
        return f"{self.name} HP:{self.hp}/{self.max_hp} ATK:{self.atk} DEF:{self.df} SPD:{self.spd}"


def generate_wave(wave_number: int):
    """Generate a list of monsters for the given wave number.
    Waves grow slowly in difficulty. Returns list of Monster objects."""
    monsters = []
    # choose a wave composition: mix of weak mobs and a stronger mob sometimes
    if wave_number == 1:
        monsters = [Monster("Goblin", 40, 6, 2, 5), Monster("Goblin", 40, 6, 2, 5)]
    else:
        count = min(1 + wave_number, 5)
        for i in range(count):
            # scale stats with wave number
            hp = 30 + wave_number * 8 + random.randint(-5, 5)
            atk = 5 + wave_number * 2 + random.randint(-1, 2)
            df = 2 + wave_number // 2
            spd = random.randint(3, 7)
            monsters.append(Monster(f"Goblin_{i+1}", hp, atk, df, spd))
        # sometimes add a stronger mob
        if wave_number % 3 == 0:
            monsters.append(Monster("Ork_Boss", 80 + wave_number * 10, 14 + wave_number * 2, 6 + wave_number // 2, 4))
    return monsters


def calculate_damage(attacker_atk: int, defender_df: int):
    base = max(1, attacker_atk - defender_df)
    # small randomness
    dmg = base + random.randint(0, max(1, base // 2))
    return dmg


def show_character_art(role: str):
    """Display ASCII art for a character"""
    if role in CHARACTER_ASCII:
        print(CHARACTER_ASCII[role])


def show_monster_art(name: str):
    """Display ASCII art for a monster"""
    # Get the base name (e.g. "Goblin_1" -> "Goblin")
    base_name = name.split('_')[0]
    if base_name in MONSTER_ASCII:
        print(MONSTER_ASCII[base_name])
    else:
        print(f"👹 {name} 👹")


def combat_round(players, monsters):
    """Run turns until one side is all dead. Returns True if players won."""
    # create turn order by speed (players and monsters mixed)
    participants = []
    for p in players:
        if p.is_alive():
            participants.append((p.spd, 'player', p))
    for m in monsters:
        if m.is_alive():
            participants.append((m.spd, 'monster', m))

    # sort by speed desc
    participants.sort(key=lambda x: x[0], reverse=True)

    for _, kind, ent in participants:
        if kind == 'player':
            if not ent.is_alive():
                continue
            # simple AI for demo: attack the alive monster with lowest HP
            target = next((mo for mo in sorted(monsters, key=lambda x: x.hp) if mo.is_alive()), None)
            if not target:
                return True
            dmg = calculate_damage(ent.atk, target.df)
            target.take_damage(dmg)
        else:  # monster
            if not ent.is_alive():
                continue
            # monster targets a random alive player
            target = next((pl for pl in sorted(players, key=lambda x: x.hp) if pl.is_alive()), None)
            if not target:
                return False
            dmg = calculate_damage(ent.atk, target.df)
            target.take_damage(dmg)

    # check end conditions
    players_alive = any(p.is_alive() for p in players)
    monsters_alive = any(m.is_alive() for m in monsters)
    return players_alive and not monsters_alive


def run_wave(players, wave_number: int, auto=False):
    monsters = generate_wave(wave_number)
    print(f"\n{'='*60}")
    print(f">>> WELLE {wave_number} GESTARTET! <<<")
    print(f"{'='*60}")
    print(f"\nGegner:")
    for m in monsters:
        print(f"- {m}")
        show_monster_art(m.name)
    print(f"{'='*60}\n")

    # combat loop: we will perform repeated rounds until one side falls
    round_no = 1
    while any(p.is_alive() for p in players) and any(m.is_alive() for m in monsters):
        print(f"\n-- Runde {round_no} --")
        # show brief status
        for p in players:
            print(f"{p.player_name}: HP {p.hp}/{p.max_hp}")
        # run one round (each participant acts once ordered by speed)
        # For demo/auto, we just run the round; for interactive we'd ask players their actions.
        players_won = combat_round(players, monsters)
        # print monster statuses
        for m in monsters:
            if m.is_alive():
                print(f"{m}")
            else:
                print(f"{m.name} besiegt!")
        round_no += 1

    players_alive = any(p.is_alive() for p in players)
    if players_alive:
        print("\nDie Spieler haben die Welle gewonnen!")
        # drop materials by type
        total_drops = {m: sum(random.randint(0, 2) for _ in monsters) for m in MATERIAL_TYPES}
        drops_str = ", ".join(f"{k}: {v}" for k, v in total_drops.items())
        print(f"Die Spieler sammeln Materialien aus der Welle: {drops_str}.")
        # distribute materials evenly among alive players
        alive_players = [pl for pl in players if pl.is_alive()]
        if alive_players:
            for mat, total in total_drops.items():
                per_player = total // len(alive_players)
                for p in alive_players:
                    p.inventory[mat] = p.inventory.get(mat, 0) + per_player
        return True
    else:
        print("\nDie Spieler wurden besiegt...")
        return False


def main(auto=False):
    print("Willkommen zum Klara Abenteuer-Spiel!")
    print(">>> MULTIPLAYER KAMPFSPIEL <<<\n")

    if auto:
        # Demo-Modus: erstelle automatisch 3 Spieler mit templates
        num_players = 3
        player_names = [f"Spieler{i}" for i in range(1, num_players + 1)]
        demo_keys = ["1", "2", "3"]
        players = []
        for n, k in zip(player_names, demo_keys):
            t = CHAR_TEMPLATES[k]
            players.append(Character(n, t['role'], t['hp'], t['atk'], t['df'], t['spd'], t['desc'], t['symbol'], t['ability'], t['ability_desc']))
        print("Demo-Modus: 3 Spieler wurden automatisch erstellt.")
    else:
        # Frage nach Spieleranzahl
        while True:
            try:
                num_players = int(input("Wie viele Spieler? (2-4): ").strip())
                if 2 <= num_players <= 4:
                    break
            except Exception:
                pass
            print("Bitte eine Zahl zwischen 2 und 4 eingeben.")

        # Namen abfragen
        player_names = []
        for i in range(num_players):
            name = input(f"Name von Spieler {i+1}: ").strip()
            if not name:
                name = f"Spieler{i+1}"
            player_names.append(name)

        # Charakterwahl
        players = []
        for name in player_names:
            char = choose_char(name)
            players.append(char)

    # Zeige Zusammenfassung
    print("\n" + "="*60)
    print("=== CHARAKTERE GEWAEHLT ===")
    print("="*60)
    for p in players:
        print(f"\n{p.symbol} {p.player_name} als {p.role}")
        print(f"   {p.desc}")
        print(f"   Faehigkeit: {p.ability} - {p.ability_desc}")
        show_character_art(p.role)
    print("="*60)
    print("\nCharaktere wurden erstellt. Naechster Schritt: Kampfsystem implementieren.")

    # initialize materials for crafting
    for p in players:
        # inventory supports many material types
        p.inventory = {m: getattr(p, 'inventory', {}).get(m, 0) for m in MATERIAL_TYPES}
        p.placed_blocks = getattr(p, 'placed_blocks', 0)  # track 4x4 wooden blocks built

    # simple game loop: run waves until players die or choose to stop
    wave = 1
    while True:
        ok = run_wave(players, wave, auto=auto)
        if not ok:
            print("Spiel beendet. Möchtest du es nochmal versuchen? Starte das Programm neu.")
            break
        # after wave: allow crafting if interactive
        if not auto:
            print("\nZwischenstopp: Ihr könnt jetzt Gegenstände bauen (craft) oder weiter (enter).")
            for p in players:
                if not p.is_alive():
                    continue
                inv = p.inventory
                inv_str = ", ".join(f"{k}:{v}" for k, v in inv.items())
                print(f"{p.player_name} Inventar: {inv_str}")
                choice = input(f"{p.player_name}: craft? (1=Waffe +2ATK kostet holz:2, 2=Heiltrank +30HP kostet gras:1, 3=Schild +2DEF kostet stein:2, 4=Holzblock 4x4 kostet holz:4, enter=weiter): ").strip()
                def can_afford(inv, cost):
                    return all(inv.get(k, 0) >= v for k, v in cost.items())
                def pay_cost(inv, cost):
                    for k, v in cost.items():
                        inv[k] = inv.get(k, 0) - v

                if choice == '1' and can_afford(inv, {'holz': 2}):
                    p.atk += 2
                    pay_cost(inv, {'holz': 2})
                    print(f"{p.player_name} hat eine Waffe gebaut! ATK nun {p.atk}.")
                elif choice == '2' and can_afford(inv, {'gras': 1}):
                    p.hp = min(p.max_hp, p.hp + 30)
                    pay_cost(inv, {'gras': 1})
                    print(f"{p.player_name} nutzt einen Heiltrank. HP nun {p.hp}/{p.max_hp}.")
                elif choice == '3' and can_afford(inv, {'stein': 2}):
                    p.df += 2
                    pay_cost(inv, {'stein': 2})
                    print(f"{p.player_name} hat ein Schild gebaut! DEF nun {p.df}.")
                elif choice == '4' and can_afford(inv, {'holz': 4}):
                    p.placed_blocks += 1
                    pay_cost(inv, {'holz': 4})
                    print(f"{p.player_name} hat einen 4x4 Holzblock gebaut! Blöcke: {p.placed_blocks}.")
                else:
                    if choice:
                        print("Ungültig oder nicht genug Materialien.")
                # show available blocks
                print(f"{p.player_name} hat {p.placed_blocks} 4x4 Holzblöcke gebaut.")
        else:
            # demo auto-crafting: priority Waffe if possible, else Heiltrank, else Holzblock
            for p in players:
                if not p.is_alive():
                    continue
                inv = p.inventory
                if inv.get('holz', 0) >= 4:
                    p.placed_blocks += 1
                    inv['holz'] -= 4
                    print(f"{p.player_name} baut automatisch einen 4x4 Holzblock. Blöcke: {p.placed_blocks}.")
                elif inv.get('holz', 0) >= 2:
                    p.atk += 2
                    inv['holz'] -= 2
                    print(f"{p.player_name} baut automatisch eine Waffe (+2 ATK).")
                elif inv.get('gras', 0) >= 1:
                    p.hp = min(p.max_hp, p.hp + 30)
                    inv['gras'] -= 1
                    print(f"{p.player_name} nutzt automatisch einen Heiltrank (+30 HP).")

        # prepare for next wave
        wave += 1


if __name__ == "__main__":
    auto = "--auto" in sys.argv
    main(auto=auto)
