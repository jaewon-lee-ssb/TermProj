from pico2d import *
import main_state


class Obstacle:
    obstacle_image1 = None
    obstacle_image2 = None
    obstacle_image3 = None

    def __init__(self):
        if self.obstacle_image1 is None:
            self.obstacle_image1 = load_image('Land\\land1_stage1_ob.png')
        if self.obstacle_image2 is None:
            self.obstacle_image2 = load_image('Land\\land1_stage1_ob.png')
        if self.obstacle_image3 is None:
            self.obstacle_image3 = load_image('Land\\land1_stage1_ob.png')
        self.obstacle_list1 = [[600, 320], [1000, 320], [5000, 320]]
        self.obstacle_list2 = [[800, 100]]
        self.obstacle_list3 = [[1400, 100]]

    def draw(self, cookie):
        for pos in self.obstacle_list1:
            self.obstacle_image1.clip_draw(0, 0, 85, 256, pos[0] - cookie.x + 200, pos[1], 85, 400)
            draw_rectangle(pos[0] - cookie.x + 200 - 30, pos[1] - 180, pos[0] - cookie.x + 200 + 30, pos[1] + 160)
            if pos[0] - cookie.x > 1000:
                break

        for pos in self.obstacle_list2:
            self.obstacle_image2.clip_draw(265, 200, 35, 60, pos[0] - cookie.x + 200, pos[1], 35, 60)
            draw_rectangle(pos[0] - cookie.x + 200 - 20, pos[1] - 20, pos[0] - cookie.x + 200 + 20, pos[1] + 20)
            if pos[0] - cookie.x > 1000:
                break

        for pos in self.obstacle_list3:
            self.obstacle_image3.clip_draw(265, 200, 35, 60, pos[0] - cookie.x + 200, pos[1], 35, 60)
            draw_rectangle(pos[0] - cookie.x + 200 - 20, pos[1] - 20, pos[0] - cookie.x + 200 + 20, pos[1] + 20)
            if pos[0] - cookie.x > 1000:
                break

    def update(self, cookie):
        left, bottom, right, top = cookie.get_bb()
        for pos in self.obstacle_list1:
            if cookie.x - pos[0] > 250:
                self.obstacle_list1.pop(0)
            elif pos[1] - 180 < top and (pos[0] - cookie.x + 200 - 30 < left < pos[0] - cookie.x + 200 + 30
                                         or pos[0] - cookie.x + 200 - 30 < right < pos[0] - cookie.x + 200 + 30):
                self.obstacle_list1.remove(pos)

        for pos in self.obstacle_list2:
            if cookie.x - pos[0] > 250:
                self.obstacle_list2.pop(0)
            elif pos[1] < top and (pos[0] - cookie.x + 200 - 20 < left < pos[0] - cookie.x + 200 + 20
                                   or pos[0] - cookie.x + 200 - 20 < right < pos[0] - cookie.x + 200 + 20):
                self.obstacle_list2.remove(pos)
