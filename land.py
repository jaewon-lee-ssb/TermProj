from pico2d import *
import main_state


class Land:
    land1_image = None
    land2_1_image = None
    land2_2_image = None
    land3_1_image = None
    land3_2_image = None
    land3_3_image = None
    land3_4_image = None

    def __init__(self):
        if self.land1_image is None:
            self.land1_image = load_image('Land\\land1_stage1_bg.png')

        if self.land2_1_image is None:
            self.land2_1_image = load_image('Land\\land1_stage2_bg.png')
        if self.land2_2_image is None:
            self.land2_2_image = load_image('Land\\land1_stage2_bg.png')

        if self.land3_1_image is None:
            self.land3_1_image = load_image('Land\\land1_stage3_bg.png')
        if self.land3_2_image is None:
            self.land3_2_image = load_image('Land\\land1_stage3_bg.png')
        if self.land3_3_image is None:
            self.land3_3_image = load_image('Land\\land1_stage3_bg.png')
        if self.land3_4_image is None:
            self.land3_4_image = load_image('Land\\land1_stage3_bg.png')

        self.land1_sound = load_wav('Sound\\Land11.ogg')
        self.land1_sound.set_volume(10)
        self.land1_sound.repeat_play()

    def update(self):
        pass

    def draw(self):
        cookie = main_state.get_cookie()
        if cookie.x < 5400:
            self.land1_image.clip_draw(0, 0, 1000, 500, 500, 250)
        elif 5400 < cookie.x < 8800:
            self.land2_2_image.clip_draw(1100, 0, 600, 500, 300, 250)
            self.land2_1_image.clip_draw(0, 0, 1000, 500, 499, 250)
        else:
            self.land3_1_image.clip_draw(0, 740, 1100, 370, 500, 315)
            self.land3_2_image.clip_draw(0, 425, 1100, 310, 500, 250)
            self.land3_3_image.clip_draw(0, 190, 1100, 240, 500, 150)
            self.land3_4_image.clip_draw(0, 0, 1100, 190, 500, 80)
