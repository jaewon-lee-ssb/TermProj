from pico2d import *


class Position:
    x = 0
    y = 0


class MyPosition(Position):
    def __init__(self, x, y):
        self.x = x
        self.y = y