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
            temp.x = 50 + i * 100
            temp.y = 320
            self.obstacle_list.append(temp)

    def draw(self, cookie):
        for pos in self.obstacle_list:
            self.obstacle_image.clip_draw(0, 0, 85, 256, pos.x - cookie.x + 200, pos.y, 85, 400)
            draw_rectangle(pos.x - cookie.x + 200 - 30, pos.y - 180, pos.x - cookie.x + 200 + 30, pos.y + 160)
            if pos.x - cookie.x > 1000:
                break

    def update(self, cookie):
        for pos in self.obstacle_list:
            if cookie.x - pos.x > 250:
                self.obstacle_list.pop(0)
            elif not cookie.isSlide and pos.y - 180 < cookie.y + 50\
                    and (pos.x < cookie.x - 40 < pos.x + 40 or pos.x - 30 < cookie.x + 40 < pos.x + 30):
                self.obstacle_list.remove(pos)
                print('삭제')

