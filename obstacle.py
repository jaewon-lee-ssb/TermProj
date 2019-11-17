from pico2d import *
from Position import *


class Obstacle:
    obstacle_image = None
    obstacle_list = list()

    def __init__(self):
        global obstacle_image
        if self.obstacle_image is None:
            self.obstacle_image = load_image('Land\\land1_stage1_ob.png')
        for i in range(100):
            temp = Position()
            temp.x = 50 + i * 500
            temp.y = 320
            self.obstacle_list.append(temp)

    def draw(self, cookie):
        for pos in self.obstacle_list:
            self.obstacle_image.clip_draw(0, 0, 85, 256, pos.x - cookie.x + 200, pos.y, 85, 400)

            if pos.x - cookie.x > 1000:
                break

    def update(self):
        for pos in self.obstacle_list:
            if pos.x < -31:
                self.obstacle_list.pop(0)

    def get_bb(self, cookie):
        return self.x - cookie.x - 10, self.y - 40, self.x - cookie.x + 10, self.y + 40
