import random
import json
import os

from pico2d import *

import game_framework
import game_world
import land_tile

from cookie import Cookie
from land import Land
from land_tile import Tile

name = "MainState"

cookie = None
land = None
font = None
tile = None
tile_list = list()
tile_list

def enter():
    global cookie, land, tile
    cookie = Cookie()
    land = Land()
    tile = Tile()
    game_world.add_object(land, 0)
    game_world.add_object(cookie, 1)
    game_world.add_object(tile, 1)


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
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
