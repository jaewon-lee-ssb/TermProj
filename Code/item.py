from pico2d import *
import game_framework
import main_state

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Item:
    hp_item_image = None

    def __init__(self):
        if self.hp_item_image is None:
            self.hp_item_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Jelly\\Jelly.png')
        self.hp_item_sound = load_wav('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Sound\\Hp_item.ogg')
        self.hp_item_sound.set_volume(80)
        self.hp_item_list = [[5500, 200]]
        self.frame = 0
        self.count = 0

    def update(self):
        cookie = main_state.get_cookie()
        left, bottom, right, top = cookie.get_bb()
        health = main_state.get_health()
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        for pos in self.hp_item_list:
            if cookie.x - pos[0] > 250:
                self.hp_item_list.pop(0)
            elif pos[0] - cookie.x < 400 and (bottom < pos[1] - 30 < top or bottom < pos[1] + 30 < top) \
                    and (left < pos[0] - cookie.x + 200 - 30 < right or left < pos[0] - cookie.x + 200 + 30 < right):
                self.hp_item_list.remove(pos)
                self.hp_item_sound.play(1)
                health.health += 200
                self.count += 1

    def draw(self):
        cookie = main_state.get_cookie()
        for pos in self.hp_item_list:
            self.hp_item_image.clip_draw(1474 + int(self.frame) * 146, 958, 144, 144, pos[0] - cookie.x + 200, pos[1], 100, 100)
            draw_rectangle(pos[0] - cookie.x + 200 - 30, pos[1] - 30, pos[0] - cookie.x + 200 + 30, pos[1] + 30)
            if pos[0] - cookie.x > 1000:
                break
