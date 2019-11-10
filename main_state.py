import random
import json
import os

from pico2d import *

import game_framework

from cookie import Cookie
from land import Land
from land_tile import Tile

name = "MainState"

cookie = None
land = None
font = None
tile = None
tile_list = list()


def enter():
    global cookie, land, tile
    cookie = Cookie()
    land = Land()
    tile = Tile()


def exit():
    global cookie, land, tile
    del cookie
    del land
    del tile


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
    tile.update()


def draw():
    clear_canvas()
    land.draw()
    cookie.draw()
    tile.draw(cookie)
    update_canvas()
