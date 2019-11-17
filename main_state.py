import random
import json
import os

from pico2d import *
import game_world
import game_framework

from cookie import Cookie
from land import Land
from land_tile import Tile
from obstacle import Obstacle

name = "MainState"

cookie = None
land = None
font = None
tile = None
obstacles = []


def enter():
    global cookie
    cookie = Cookie()

    global land
    land = Land()

    global tile
    tile = Tile()

    global obstacle
    obstacle = Obstacle()


def exit():
    global cookie, land, tile, obstacle
    del cookie
    del land
    del tile
    del obstacle


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
    tile.update(cookie)
    obstacle.update(cookie)
    cookie.update()


def draw():
    clear_canvas()
    land.draw()
    tile.draw(cookie)
    obstacle.draw(cookie)
    cookie.draw()
    update_canvas()
