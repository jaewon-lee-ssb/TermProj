from pico2d import *


class Jelly:
    jelly_image = None

    def __init__(self):
        if self.jelly_image is None:
            self.jelly_image = load_image('Jelly\\Jelly.png')
        self.jelly_list = [[400, 100], [450, 100], [500, 100], [550, 100], [600, 100], [650, 100], [700, 100],
                           [750, 100], [800, 100], [850, 100], [900, 100], [950, 100], [1000, 100], [1050, 100],
                           [1100, 100], [1130, 150], [1150, 200], [1200, 250], [1250, 100], [1300, 100], [650, 100], [650, 100]]
        # 천장에 긴 장애물
        # self.obstacle_list1 = [[1000, 320], [1500, 320], [1600, 320], [1700, 320], [1800, 320], [2500, 320],
        #                       [2900, 320], [3900, 320], [4000, 320], [4100, 320]]
        # 바닥에 작은 장애물
        # self.obstacle_list2 = [[2000, 100], [2200, 100], [2300, 100], [2700, 100], [4550, 100], [4600, 100],
        #                       [4650, 100]]
        # 바닥에 긴 장애물
        # self.obstacle_list3 = [[1250, 135], [2250, 135], [3100, 135], [3400, 135], [3700, 135], [4300, 135],
        #                       [4900, 135]]

    def draw(self, cookie):
        for pos in self.jelly_list:
            self.jelly_image.clip_draw(242, 668, 55, 50, pos[0] - cookie.x + 200, pos[1], 45, 40)
            draw_rectangle(pos[0] - cookie.x + 200 - 20, pos[1] - 20, pos[0] - cookie.x + 200 + 20, pos[1] + 20)
            if pos[0] - cookie.x > 1000:
                break

    def update(self, cookie):
        left, bottom, right, top = cookie.get_bb()

        for pos in self.jelly_list:
            if cookie.x - pos[0] > 250:
                self.jelly_list.pop(0)
            elif pos[0] - cookie.x < 400 and (bottom < pos[1] - 20 < top or bottom < pos[1] + 20 < top) \
                    and (pos[0] - cookie.x + 200 - 20 < left < pos[0] - cookie.x + 200 + 20
                         or pos[0] - cookie.x + 200 - 20 < right < pos[0] - cookie.x + 200 + 20):
                self.jelly_list.remove(pos)
