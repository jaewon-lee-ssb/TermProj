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
from health import Health
from jelly import Jelly
from font import Font

name = "MainState"

cookie = None
land = None
font = None
tile = None
health = None
jelly = None
obstacle = None


def enter():
    global cookie
    cookie = Cookie()

    global land
    land = Land()

    global tile
    tile = Tile()

    global obstacle
    obstacle = Obstacle()

    global health
    health = Health()

    global jelly
    jelly = Jelly()

    global font
    font = Font()


def exit():
    global cookie, land, tile, obstacle, health, jelly, font
    del cookie
    del land
    del tile
    del obstacle
    del health
    del jelly
    del font


def get_health():
    return health


def get_obstacle():
    return obstacle


def get_jelly():
    return jelly


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
    jelly.update(cookie)
    obstacle.update(cookie)
    health.update()
    cookie.update()


def draw():
    clear_canvas()
    land.draw()
    tile.draw(cookie)
    jelly.draw(cookie)
    obstacle.draw(cookie)
    health.draw()
    font.draw()
    cookie.draw()
    update_canvas()
