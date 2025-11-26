import sys
import random

try:
    import pygame
except Exception:
    print("Pygame ist nicht installiert. Bitte installiere es mit:\n  .venv\\Scripts\\python.exe -m pip install pygame")
    raise

from game import Character, Monster, CHAR_TEMPLATES, MATERIAL_TYPES, calculate_damage

# Simple Pygame prototype for the 10x10 grid game
TILE = 48
COLS = 10
ROWS = 10
WIDTH = TILE * COLS
HEIGHT = TILE * ROWS + 80  # extra space for HUD
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (80, 180, 80)
BROWN = (150, 100, 50)
RED = (200, 60, 60)
BLUE = (60, 120, 200)
YELLOW = (240, 230, 90)


def make_player(choice_key='1'):
    t = CHAR_TEMPLATES.get(choice_key, CHAR_TEMPLATES['1'])
    return Character('Player', t['role'], t['hp'], t['atk'], t['df'], t['spd'], t['desc'], t.get('symbol', ''), t.get('ability', ''), t.get('ability_desc', ''))


def spawn_monsters(n=5):
    monsters = []
    for i in range(n):
        m = Monster(f'Goblin_{i+1}', 30 + random.randint(0, 10), 6, 2, 4)
        # choose random pos
        mx = random.randint(0, COLS - 1)
        my = random.randint(0, ROWS - 1)
        monsters.append([m, mx, my])
    return monsters


def draw_grid(screen, grid):
    for y in range(ROWS):
        for x in range(COLS):
            rect = pygame.Rect(x * TILE, y * TILE, TILE, TILE)
            pygame.draw.rect(screen, GRAY if (x + y) % 2 == 0 else WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if grid[y][x] == 'B':
                pygame.draw.rect(screen, BROWN, rect.inflate(-6, -6))


def draw_hud(screen, font, player):
    hud_y = ROWS * TILE + 8
    # background
    pygame.draw.rect(screen, BLACK, (0, ROWS * TILE, WIDTH, 80))
    # HP
    hp_text = font.render(f"HP: {player.hp}/{player.max_hp}", True, WHITE)
    screen.blit(hp_text, (8, hud_y))
    # ATK/DEF
    stats_text = font.render(f"ATK:{player.atk} DEF:{player.df}", True, WHITE)
    screen.blit(stats_text, (120, hud_y))
    # Inventory
    inv_text = font.render(' '.join(f"{k}:{v}" for k, v in player.inventory.items()), True, WHITE)
    screen.blit(inv_text, (8, hud_y + 30))
    # Controls
    ctrl_text = font.render('Bewegung: Pfeile/WASD  Leertaste=Angriff  B=Bauen  Esc=Beenden', True, YELLOW)
    screen.blit(ctrl_text, (8, hud_y + 50))


def find_monster_at(monsters, x, y):
    for idx, (m, mx, my) in enumerate(monsters):
        if mx == x and my == y and m.is_alive():
            return idx, m
    return None, None


def main():
    # allow selecting template from argv --player N
    choice = '1'
    for arg in sys.argv[1:]:
        if arg.startswith('--player='):
            choice = arg.split('=', 1)[1]
            break
    player = make_player(choice)
    # give player a little starting materials so they can build
    player.inventory = {m: 3 for m in MATERIAL_TYPES}
    player.placed_blocks = 0

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Klara - Mini GUI')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 18)

    grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
    px, py = COLS // 2, ROWS // 2
    monsters = spawn_monsters(6)

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_w, pygame.K_UP):
                    nx, ny = px, max(0, py - 1)
                    if grid[ny][nx] != 'B':
                        px, py = nx, ny
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    nx, ny = px, min(ROWS - 1, py + 1)
                    if grid[ny][nx] != 'B':
                        px, py = nx, ny
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    nx, ny = max(0, px - 1), py
                    if grid[ny][nx] != 'B':
                        px, py = nx, ny
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    nx, ny = min(COLS - 1, px + 1), py
                    if grid[ny][nx] != 'B':
                        px, py = nx, ny
                elif event.key == pygame.K_SPACE:
                    # attack current tile
                    idx, mon = find_monster_at(monsters, px, py)
                    if mon:
                        dmg = calculate_damage(player.atk, mon.df)
                        mon.take_damage(dmg)
                        print(f"Du greifst {mon.name} an und verursachst {dmg} Schaden.")
                        if not mon.is_alive():
                            print(f"{mon.name} besiegt!")
                            # drops
                            for mtype in MATERIAL_TYPES:
                                player.inventory[mtype] = player.inventory.get(mtype, 0) + random.randint(0, 2)
                    else:
                        print('Kein Monster hier')
                elif event.key == pygame.K_b:
                    # try build 4x4 anchored at player's position
                    cost = 4
                    if player.inventory.get('holz', 0) < cost:
                        print('Nicht genug Holz (bedarf 4)')
                    elif px + 4 > COLS or py + 4 > ROWS:
                        print('Kein Platz hier fuer 4x4 Block')
                    else:
                        for yy in range(py, py + 4):
                            for xx in range(px, px + 4):
                                grid[yy][xx] = 'B'
                        player.inventory['holz'] -= cost
                        player.placed_blocks += 1
                        print('4x4 Block gebaut')

        # Render
        screen.fill(BLACK)
        draw_grid(screen, grid)
        # draw monsters
        for m, mx, my in monsters:
            if m.is_alive():
                rect = pygame.Rect(mx * TILE + 6, my * TILE + 6, TILE - 12, TILE - 12)
                pygame.draw.rect(screen, RED, rect)
        # draw player
        prect = pygame.Rect(px * TILE + 6, py * TILE + 6, TILE - 12, TILE - 12)
        pygame.draw.rect(screen, BLUE, prect)

        draw_hud(screen, font, player)

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
