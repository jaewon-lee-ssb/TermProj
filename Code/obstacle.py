from pico2d import *
import main_state
import game_framework


class Obstacle:
    obstacle_image1 = None
    obstacle_image2 = None
    obstacle_image3 = None

    def __init__(self):
        if self.obstacle_image1 is None:
            self.obstacle_image1 = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage1_ob.png')
        if self.obstacle_image2 is None:
            self.obstacle_image2 = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage1_ob.png')
        if self.obstacle_image3 is None:
            self.obstacle_image3 = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage1_ob.png')

        self.isCollide = False
        self.timer = 0

        # 천장에 긴 장애물
        self.obstacle_list1 = [[1000, 320], [1500, 320], [1600, 320], [1700, 320], [1800, 320], [2500, 320],
                               [2900, 320], [3900, 320], [4000, 320], [4100, 320], [6900, 320], [7000, 320],
                               [7100, 320], [8300, 320], [8400, 320]]
        # 바닥에 작은 장애물
        self.obstacle_list2 = [[2000, 100], [2200, 100], [2300, 100], [2700, 100], [4550, 100], [4600, 100],
                               [4650, 100], [6000, 100], [6200, 100], [7500, 100], [8000, 100], [8050, 100],
                               [8100, 100], [8550, 100]]
        # 바닥에 긴 장애물
        self.obstacle_list3 = [[1250, 135], [2250, 135], [3100, 135], [3400, 135], [3700, 135], [4300, 135],
                               [4900, 135], [6400, 135], [6700, 135], [7300, 135], [7750, 135]]

    def draw(self, cookie):
        for pos in self.obstacle_list1:
            self.obstacle_image1.clip_draw(0, 0, 85, 260, pos[0] - cookie.x + 200, pos[1], 85, 400)
            # draw_rectangle(pos[0] - cookie.x + 200 - 30, pos[1] - 180, pos[0] - cookie.x + 200 + 30, pos[1] + 160)
            if pos[0] - cookie.x > 1000:
                break

        for pos in self.obstacle_list2:
            self.obstacle_image2.clip_draw(265, 200, 35, 60, pos[0] - cookie.x + 200, pos[1], 50, 70)
            # draw_rectangle(pos[0] - cookie.x + 200 - 20, pos[1] - 20, pos[0] - cookie.x + 200 + 20, pos[1] + 20)
            if pos[0] - cookie.x > 1000:
                break

        for pos in self.obstacle_list3:
            self.obstacle_image3.clip_draw(145, 0, 65, 110, pos[0] - cookie.x + 200, pos[1], 70, 145)
            draw_rectangle(pos[0] - cookie.x + 200 - 20, pos[1] - 60, pos[0] - cookie.x + 200 + 20, pos[1] + 60)
            if pos[0] - cookie.x > 1000:
                break

    def update(self, cookie):
        left, bottom, right, top = cookie.get_bb()
        life = main_state.get_health()
        if self.isCollide:
            self.timer -= game_framework.frame_time
        if self.timer < 0:
            self.isCollide = False

        for pos in self.obstacle_list1:
            if cookie.x - pos[0] > 250:
                self.obstacle_list1.pop(0)
            elif pos[0] - cookie.x < 400 and pos[1] - 180 < top \
                    and (pos[0] - cookie.x + 200 - 30 < left < pos[0] - cookie.x + 200 + 30
                         or pos[0] - cookie.x + 200 - 30 < right < pos[0] - cookie.x + 200 + 30) \
                    and not self.isCollide:
                life.health -= 50
                self.isCollide = True
                self.timer = 3

        for pos in self.obstacle_list2:
            if cookie.x - pos[0] > 250:
                self.obstacle_list2.pop(0)
            elif pos[0] - cookie.x < 400 and pos[1] + 20 > bottom \
                    and (pos[0] - cookie.x + 200 - 20 < left < pos[0] - cookie.x + 200 + 20
                         or pos[0] - cookie.x + 200 - 20 < right < pos[0] - cookie.x + 200 + 20) \
                    and not self.isCollide:
                life.health -= 50
                self.isCollide = True
                self.timer = 3

        for pos in self.obstacle_list3:
            if cookie.x - pos[0] > 250:
                self.obstacle_list3.pop(0)
            elif pos[0] - cookie.x < 400 and pos[1] + 60 > bottom \
                    and (pos[0] - cookie.x + 200 - 20 < left < pos[0] - cookie.x + 200 + 20
                         or pos[0] - cookie.x + 200 - 20 < right < pos[0] - cookie.x + 200 + 20) \
                    and not self.isCollide:
                life.health -= 50
                self.isCollide = True
                self.timer = 3
