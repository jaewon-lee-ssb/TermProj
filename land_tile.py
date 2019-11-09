from pico2d import *
import game_world


class Tile:
    image = None

    def __init__(self, x=350, y=35, velocity=1):
        if Tile.image is None:
            Tile.image = load_image('Land\\land1_stage1_ob.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.clip_draw(315, 80, 70, 70, self.x, self.y)

    def update(self):
        self.x -= self.velocity

        if self.x < 0:
            game_world.remove_object(self)