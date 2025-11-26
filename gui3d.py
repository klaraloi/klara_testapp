from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

"""
Minimal 3D prototype using Ursina.

Controls:
- WASD / mouse: move & look (FirstPersonController)
- Left mouse: simple attack (projectile)
- B: place a block 2 units ahead (grid-aligned)
- Esc: quit

Notes:
- Install with `pip install ursina` in your project venv before running.
"""

app = Ursina()

# Ground
ground = Entity(model='plane', scale=(20, 1, 20), texture='white_cube', texture_scale=(10,10), collider='box')

# Player (use FirstPersonController for quick movement/looking)
player = FirstPersonController()
player.cursor = Entity(parent=camera.ui, model='quad', scale=0.01, color=color.white)

# Parent for placed blocks
blocks_parent = Entity()

controls_text = Text(
    text='WASD/mouse: Move  •  Left click: Attack  •  B: Build block',
    position=Vec2(-0.6, 0.45),
    scale=1.25,
    origin=(0,0)
)

def place_block():
    # Compute a grid-aligned position roughly 2 units ahead of the player
    p = player.position + player.forward * 2
    pos = (round(p.x), 0.5, round(p.z))

    # Don't place if a block already exists at that position
    for b in blocks_parent.children:
        if (round(b.x), round(b.y), round(b.z)) == (pos[0], pos[1], pos[2]):
            return

    block = Entity(parent=blocks_parent, model='cube', color=color.rgb(140,100,40), position=pos, scale=Vec3(1,1,1), collider='box')

def fire_projectile():
    # small projectile spawned in front of the player
    proj = Entity(model='sphere', color=color.red, scale=0.15, position=player.position + player.forward * 1.5)
    target_pos = proj.position + player.forward * 6
    proj.animate_position(target_pos, duration=0.45, curve=curve.linear)
    destroy(proj, delay=0.6)

def input(key):
    if key == 'b':
        place_block()
    if key == 'left mouse down':
        fire_projectile()

if __name__ == '__main__':
    app.run()
