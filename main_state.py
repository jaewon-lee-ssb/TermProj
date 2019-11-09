import random
import json
import os

from pico2d import *

import game_framework
import game_world

from cookie import Cookie
from land import Land

name = "MainState"

cookie = None
land = None
font = None


def enter():
    global cookie, land
    cookie = Cookie()
    land = Land()
    game_world.add_object(land, 0)
    game_world.add_object(cookie, 1)


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
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.05)
