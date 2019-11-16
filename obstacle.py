from pico2d import *
from Position import *


class Obstacle:
    obstacle_image = None

    def __init__(self, cookie):
        if Obstacle.obstacle_image is None:
            Obstacle.obstacle_image = load_image('Land\\land1_stage1_ob.png')
        self.x, self.y = cookie.x + 1500, 320

    def draw(self, cookie):
        if self.x - cookie.x < 1000:
            Obstacle.obstacle_image.clip_draw(0, 0, 85, 256, self.x - cookie.x + 200, self.y, 85, 400)
            draw_rectangle(*self.get_bb(cookie))
        pass

    def update(self):
        pass

    def get_bb(self, cookie):
        return self.x - cookie.x - 10, self.y - 40, self.x - cookie.x + 10, self.y + 40
