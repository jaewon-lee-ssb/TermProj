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
            self.land1_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage1_bg.png')

        if self.land2_1_image is None:
            self.land2_1_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage2_bg.png')
        if self.land2_2_image is None:
            self.land2_2_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage2_bg.png')

        if self.land3_1_image is None:
            self.land3_1_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage3_bg.png')
        if self.land3_2_image is None:
            self.land3_2_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage3_bg.png')
        if self.land3_3_image is None:
            self.land3_3_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage3_bg.png')
        if self.land3_4_image is None:
            self.land3_4_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Land\\land1_stage3_bg.png')
            
        self.land1_sound = load_wav('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Sound\\Land11.ogg')
        self.land1_sound.set_volume(10)
        self.land1_sound.repeat_play()

    def update(self):
        pass

    def draw(self):
        cookie = main_state.get_cookie()
        if cookie.x < 5400:
            self.land1_image.clip_draw(0, 0, 1000, 500, 500, 250)
        else:
            self.land2_2_image.clip_draw(1100, 0, 600, 500, 300, 250)
            self.land2_1_image.clip_draw(0, 0, 1000, 500, 499, 250)
