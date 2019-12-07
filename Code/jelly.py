from pico2d import *
import position
import main_state


class Jelly:
    jelly_image = None
    jelly_list = list()

    def __init__(self):
        obstacle = main_state.get_obstacle()
        if self.jelly_image is None:
            self.jelly_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Jelly\\Jelly.png')
        self.jelly_sound = load_wav('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Sound\\Jelly.ogg')
        self.jelly_sound.set_volume(20)

        self.score = 0

        for i in range(500):
            temp = position.Position()
            temp.x = 300 + 50 * i
            temp.y = 100
            self.jelly_list.append(temp)

        for pos in obstacle.land1_obstacle_list2:
            for i in self.jelly_list:
                if pos[0] == i.x:
                    i.y += 100
        for pos in obstacle.land1_obstacle_list3:
            for i in self.jelly_list:
                if pos[0] == i.x:
                    i.y += 150

        for pos in obstacle.land2_obstacle_list2:
            for i in self.jelly_list:
                if pos[0] == i.x:
                    i.y += 100
        for pos in obstacle.land2_obstacle_list3:
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







    def draw(self, cookie):
        for pos in self.jelly_list:
            self.jelly_image.clip_draw(242, 668, 55, 50, pos.x - cookie.x + 200, pos.y, 45, 40)
            # draw_rectangle(pos.x - cookie.x + 200 - 20, pos.y - 20, pos.x - cookie.x + 200 + 20, pos.y + 20)
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
                self.jelly_sound.play(1)
