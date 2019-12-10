from pico2d import *
import game_framework
import main_state


class Health:
    health_image1 = None
    health_image2 = None

    def __init__(self):
        if self.health_image1 is None:
            self.health_image1 = load_image('Effect\\health_bar.png')
        if self.health_image2 is None:
            self.health_image2 = load_image('Jelly\\Jelly.png')
        self.left_x, self.right_x, self.y = 100, 800, 450
        self.health = 200
        self.move1 = 0
        self.move2 = 0
        self.move3 = 0

    def update(self):
        obstacle = main_state.get_obstacle()
        item = main_state.get_item()
        self.health -= game_framework.frame_time * 4
        self.move1 += game_framework.frame_time * 2
        if obstacle.timer == 3:
            self.move2 += 25
        self.move3 = item.count * 100
        pass

    def draw(self):
        obstacle = main_state.get_obstacle()
        self.health_image1.clip_draw(0, 10, int(self.health), 90,
                                     int(self.health) + 55 + self.move1 + self.move2 - self.move3,
                                     450, int(self.health), 20)
        self.health_image2.clip_draw(1475, 960, 140, 140, 120, 450, 95, 100)
