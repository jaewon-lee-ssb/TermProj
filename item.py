from pico2d import *
import game_framework
import main_state

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


class Item:
    heart_item_image = None

    def __init__(self):
        if self.heart_item_image is None:
            self.heart_item_image = load_image('Jelly\\Jelly.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass

    def draw(self):
        cookie = main_state.get_cookie()
        self.heart_item_image.clip_draw(1474 + int(self.frame) * 146, 958, 144, 144, 500 - cookie.x + 200, 300, 100, 100)
