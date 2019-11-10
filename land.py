from pico2d import *
from land_tile import Tile


class Land:
    def __init__(self):
        self.x1, self.x2, self.y = 500, 1500, 250
        self.Width, self.Height = 1000, 500
        self.image1_1 = load_image('Land\\land1_stage1_bg.png')
        self.image1_2 = load_image('Land\\land1_stage1_bg.png')

    def update(self):
        self.x1 -= 1
        self.x2 -= 1
        pass

    def draw(self):
        self.image1_1.clip_draw(0, 0, self.Width, self.Height, self.x1, self.y)
        self.image1_2.clip_draw(0, 0, self.Width, self.Height, self.x2, self.y)
