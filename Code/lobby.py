from pico2d import *


class Lobby:
    lobby_image = None

    def __init__(self):
        if self.lobby_image is None:
            self.lobby_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Image\\Lobby.png')

        self.x, self.y = 500, 250
        self.lobby_sound = load_wav('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Sound\\Lobby.ogg')

    def update(self):
        pass

    def draw(self):
        self.lobby_image.draw(self.x, self.y)