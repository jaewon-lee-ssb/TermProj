from pico2d import *
from Position import *

obstacle_image = None


class Obstacle:
    obstacle_list = list()

    def __init__(self):
        global obstacle_image
        if obstacle_image is None:
            obstacle_image = load_image('Land\\land1_stage1_ob.png')
        for i in range(100):
            temp = Position()
            temp.x = 50 + i*500
            temp.y = 320
            self.obstacle_list.append(temp)

    def draw(self, cookie):
        global obstacle_image
        for pos in self.obstacle_list:
            obstacle_image.clip_draw(0, 0, 85, 256, pos.x - cookie.x + 200, pos.y, 85, 400)
            if pos.x - cookie.x > 1000:
                break
        pass

    def update(self):
        for pos in self.obstacle_list:
            if pos.x < -31:
                self.obstacle_list.pop(0)
