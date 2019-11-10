from pico2d import *
import game_world

tile_image = None


class Position:
    x = 0
    y = 0


class Tile:
    tile_list = list()

    def __init__(self, x=350, y=35, velocity=1):
        global tile_image
        if tile_image is None:
            tile_image = load_image('Land\\land1_stage1_ob.png')
        self.x, self.y, self.velocity = x, y, velocity
        for i in range(20):
            temp = Position()
            temp.x = 20 + i*63
            temp.y = 35
            self.tile_list.append(temp)
            print(temp.x, temp.y)

    def draw(self):
        global tile_image
        for pos in self.tile_list:
            tile_image.clip_draw(315, 80, 63, 70, pos.x, pos.y)
        pass

    def update(self):
        for pos in self.tile_list:
            pos.x -= 1
            if pos.x < -31:
                self.tile_list.pop(0)
                temp = Position()
                temp.x = 1230
                temp.y = 35
                self.tile_list.append(temp)
                print(temp.x, temp.y)
