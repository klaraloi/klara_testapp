from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

"""
Enhanced 3D prototype using Ursina.

New features:
- Grid visual on ground
- HUD showing simple inventory (wood)
- Simple enemies that walk toward the player
- Projectiles that can hit enemies and drop wood
- Block placement that consumes wood

Run after `pip install ursina` in the project venv.
"""

app = Ursina()

# Ground
ground = Entity(model='plane', scale=(20, 1, 20), texture='white_cube', texture_scale=(10,10), collider='box', color=color.light_gray)

# Draw grid lines for visual aid
grid_parent = Entity()
GRID_SIZE = 10
for x in range(-GRID_SIZE, GRID_SIZE+1):
    Entity(parent=grid_parent, model='cube', scale=(0.03, 0.02, GRID_SIZE*2), position=(x, 0.02, 0), color=color.gray)
for z in range(-GRID_SIZE, GRID_SIZE+1):
    Entity(parent=grid_parent, model='cube', scale=(GRID_SIZE*2, 0.02, 0.03), position=(0, 0.02, z), color=color.gray)

# Player (use FirstPersonController for quick movement/looking)
player = FirstPersonController()
player.cursor = Entity(parent=camera.ui, model='quad', scale=0.01, color=color.white)

# Inventory and parents
player_inventory = {'holz': 0}
blocks_parent = Entity()
enemies_parent = Entity()
projectiles_parent = Entity()

# HUD
hud_text = Text(text='', position=Vec2(-0.95, 0.45), scale=1.1, origin=(0,0))
controls_text = Text(text='WASD/mouse: Move  •  Left click: Attack  •  B: Build block (cost 1 Holz)', position=Vec2(-0.6, 0.41), scale=0.9, origin=(0,0))

def update_hud():
    hud_text.text = f'Holz: {player_inventory.get("holz",0)}'

update_hud()

def place_block():
    cost = 1
    if player_inventory.get('holz',0) < cost:
        return
    p = player.position + player.forward * 2
    pos = (round(p.x), 0.5, round(p.z))
    # Don't place if a block exists
    for b in blocks_parent.children:
        if (round(b.x), round(b.y), round(b.z)) == (pos[0], pos[1], pos[2]):
            return
    player_inventory['holz'] -= cost
    Entity(parent=blocks_parent, model='cube', color=color.rgb(140,100,40), position=pos, scale=Vec3(1,1,1), collider='box')
    update_hud()

def spawn_enemy():
    # spawn at random edge
    choices = [(-GRID_SIZE,0,random.randint(-GRID_SIZE,GRID_SIZE)), (GRID_SIZE,0,random.randint(-GRID_SIZE,GRID_SIZE)), (random.randint(-GRID_SIZE,GRID_SIZE),0,-GRID_SIZE), (random.randint(-GRID_SIZE,GRID_SIZE),0,GRID_SIZE)]
    x,y,z = random.choice(choices)
    e = Entity(parent=enemies_parent, model='cube', color=color.green, scale=0.9, position=(x,0.5,z), collider='box')
    e.health = 1

def fire_projectile():
    proj = Entity(parent=projectiles_parent, model='sphere', color=color.red, scale=0.15, position=player.position + player.forward * 1.5)
    proj.direction = player.forward
    proj.speed = 18
    proj.lifetime = 1.0

def handle_projectiles(dt):
    for proj in list(projectiles_parent.children):
        proj.position += proj.direction * proj.speed * dt
        proj.lifetime -= dt
        # collision check with enemies
        for e in list(enemies_parent.children):
            if distance(proj.position, e.position) < 0.9:
                # enemy dies, drop wood
                player_inventory['holz'] = player_inventory.get('holz',0) + 1
                destroy(e)
                destroy(proj)
                update_hud()
                break
        else:
            if proj.lifetime <= 0:
                destroy(proj)

def handle_enemies(dt):
    for e in list(enemies_parent.children):
        # move toward player on XZ plane
        dir = Vec3(player.x - e.x, 0, player.z - e.z)
        if dir.length() > 0.2:
            e.position += dir.normalized() * dt * 1.2
        # optional: if enemy reaches player, we could reduce health (not implemented)

enemy_spawn_timer = 0.0

def update():
    global enemy_spawn_timer
    dt = time.dt
    handle_projectiles(dt)
    handle_enemies(dt)
    enemy_spawn_timer -= dt
    if enemy_spawn_timer <= 0:
        spawn_enemy()
        enemy_spawn_timer = max(1.8, 3.0 + random.uniform(-1,1))

def input(key):
    if key == 'b':
        place_block()
    if key == 'left mouse down':
        fire_projectile()

if __name__ == '__main__':
    # spawn a few enemies to start
    for _ in range(2):
        spawn_enemy()
    app.run()
