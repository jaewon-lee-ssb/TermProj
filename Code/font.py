from pico2d import *
import main_state


class Font:

    def __init__(self):
        self.font = load_font('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Font\\CookieRun Black.ttf', 20)
        self.x, self.y = 850, 450

    def draw(self):
        jelly = main_state.get_jelly()
        self.font.draw(self.x, self.y, '(Score: %d)' % jelly.score, (255, 255, 0))
