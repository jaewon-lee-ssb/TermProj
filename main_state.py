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
    game_world.add_object(cookie, 1)

    global land
    land = Land()
    game_world.add_object(land, 0)

    global tile
    tile = Tile()
    game_world.add_object(tile, 1)

    global obstacles
    obstacles = [Obstacle(cookie) for i in range(10)]
    game_world.add_objects(obstacles, 1)


def exit():
    game_world.clear()


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
