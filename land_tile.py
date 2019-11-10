from pico2d import *
from Position import *

tile_image = None


class Tile:
    tile_list = list()

    def __init__(self):
        global tile_image
        if tile_image is None:
            tile_image = load_image('Land\\land1_stage1_ob.png')
        for i in range(1000):
            temp = Position()
            temp.x = 20 + i*63
            temp.y = 35
            self.tile_list.append(temp)

    def draw(self, cookie):
        global tile_image
        for pos in self.tile_list:
            tile_image.clip_draw(315, 80, 63, 70, pos.x - cookie.x + 200, pos.y)
        pass

    def update(self):
        for pos in self.tile_list:
            if pos.x < -31:
                self.tile_list.pop(0)
