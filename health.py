from pico2d import *
import game_framework


class Health:
    health_image = None

    def __init__(self):
        if self.health_image is None:
            self.health_image = load_image('Effect\\health_bar.png')
        self.left_x, self.right_x, self.y = 100, 800, 450
        self.health = 200
        self.a = 0

    def update(self):
        self.health -= game_framework.frame_time * 10
        self.a += game_framework.frame_time * 4
        pass

    def draw(self):
        self.health_image.clip_draw(0, 10, int(self.health), 90, (self.left_x + self.right_x) / 2 - int(self.a), 480,
                                    int(self.health), 20)
