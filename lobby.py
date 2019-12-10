from pico2d import *


class Lobby:
    lobby_image = None

    def __init__(self):
        if self.lobby_image is None:
            self.lobby_image = load_image('Image\\Lobby.png')

        self.x, self.y = 500, 250
        self.lobby_sound = load_wav('Sound\\Lobby.ogg')
        self.lobby_sound.set_volume(10)
        self.lobby_sound.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.lobby_image.draw(self.x, self.y)