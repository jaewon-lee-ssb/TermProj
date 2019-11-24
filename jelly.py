from pico2d import *
import position
import main_state


class Jelly:
    jelly_image = None
    jelly_list = list()

    def __init__(self):
        obstacle = main_state.get_obstacle()
        if self.jelly_image is None:
            self.jelly_image = load_image('Jelly\\Jelly.png')

        self.score = 0

        for i in range(1000):
            temp = position.Position()
            temp.x = 300 + 50 * i
            temp.y = 100
            self.jelly_list.append(temp)

        for pos in obstacle.obstacle_list2:
            for i in self.jelly_list:
                if pos[0] == i.x:
                    i.y += 100

        for pos in obstacle.obstacle_list3:
            for i in self.jelly_list:
                if pos[0] == i.x:
                    i.y += 150

        for i in range(len(self.jelly_list)):
            if self.jelly_list[i].y == 200:
                if i - 1 > 0:
                    self.jelly_list[i - 1].y += 50
                if i + 1 < len(self.jelly_list):
                    self.jelly_list[i + 1].y += 50
            elif self.jelly_list[i].y == 250:
                if i - 1 > 0:
                    self.jelly_list[i - 1].y += 100
                if i + 1 < len(self.jelly_list):
                    self.jelly_list[i + 1].y += 100
        # self.jelly_list = [[400, 100], [450, 100], [500, 100], [550, 100], [600, 100], [650, 100], [700, 100],
        #                   [750, 100], [800, 100], [850, 100], [900, 100], [950, 100], [1000, 100], [1050, 100],
        #                   [1100, 100], [1130, 150], [1150, 200], [1170, 240], [1200, 270], [1240, 300], [1270, 270],
        #                   [1300, 250]]
        # 천장에 긴 장애물
        # self.obstacle_list1 = [[1000, 320], [1500, 320], [1600, 320], [1700, 320], [1800, 320], [2500, 320],
        #                       [2900, 320], [3900, 320], [4000, 320], [4100, 320]]
        # 바닥에 작은 장애물
        # self.obstacle_list2 = [[2000, 100], [2200, 100], [2300, 100], [2700, 100], [4550, 100], [4600, 100],
        #                       [4650, 100]]
        # 바닥에 긴 장애물
        # self.obstacle_list3 = [[1250, 135], [2250, 135], [3100, 135], [3400, 135], [3700, 135], [4300, 135],
        #                       [4900, 135]]

    def jelly_up(self, i):
        (i - 1).y += 50
        (i + 1).y += 50

    def aaaa(self):
        jelly_iter = self.jelly_list.__iter__()



    def draw(self, cookie):
        for pos in self.jelly_list:
            self.jelly_image.clip_draw(242, 668, 55, 50, pos.x - cookie.x + 200, pos.y, 45, 40)
            draw_rectangle(pos.x - cookie.x + 200 - 20, pos.y - 20, pos.x - cookie.x + 200 + 20, pos.y + 20)
            if pos.x - cookie.x > 1000:
                break

    def update(self, cookie):
        left, bottom, right, top = cookie.get_bb()

        for pos in self.jelly_list:
            if cookie.x - pos.x > 250:
                self.jelly_list.pop(0)
            elif pos.x - cookie.x < 400 and (bottom < pos.y - 20 < top or bottom < pos.y + 20 < top) \
                    and (pos.x - cookie.x + 200 - 20 < left < pos.x - cookie.x + 200 + 20
                         or pos.x - cookie.x + 200 - 20 < right < pos.x - cookie.x + 200 + 20):
                self.jelly_list.remove(pos)
                self.score += 246
