from pico2d import *


class Land:
    def __init__(self):
        self.x1, self.x2, self.y = 500, 1500, 250
        self.x3 = 35
        self.Width, self.Height = 1000, 500
        self.image1_1 = load_image('Land\\land1_stage1_bg.png')
        self.image1_2 = load_image('Land\\land1_stage1_bg.png')
        self.image1_3 = load_image('Land\\land1_stage1_ob.png')

    def update(self):
        self.x1 -= 2
        self.x2 -= 2

    def draw(self):
        self.image1_1.clip_draw(0, 0, self.Width, self.Height, self.x1, self.y)
        self.image1_2.clip_draw(0, 0, self.Width, self.Height, self.x2, self.y)
        for i in range(100):
            if self.x3 > 0:
                self.image1_3.clip_draw(315, 80, 70, 70, self.x3 + (i * 62), 35)
            self.x3 -= 0.1
