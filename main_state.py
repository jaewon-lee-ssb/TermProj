import random
import json
import os

from pico2d import *

import game_framework

from cookie import Cookie
from land import Land

name = "MainState"

cookie = None
land = None
font = None


def enter():
    global cookie, land
    boy = Cookie()
    land = Land()


def exit():
    global cookie, land
    del cookie
    del land


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            cookie.handle_event(event)


def update():
    land.update()
    cookie.update()


def draw():
    clear_canvas()
    land.draw()
    cookie.draw()
    update_canvas()
