import game_framework
import loading_state
from pico2d import *

from lobby import Lobby


name = "StartGame"
lobby = None
logo_image = None
brave_cookie_head_image = None


def enter():
    global lobby
    lobby = Lobby()

    global logo_image
    logo_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Image\\Cookie_run_logo.png')

    global brave_cookie_head_image
    brave_cookie_head_image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Image\\Brave_cookie_head.png')

    pass


def exit():
    global lobby, logo_image, brave_cookie_head_image
    del lobby
    del logo_image
    del brave_cookie_head_image

    pass


def update():
    pass


def draw():
    global logo_image, brave_cookie_head_image
    clear_canvas()

    lobby.draw()
    logo_image.draw(500, 430)
    brave_cookie_head_image.draw(500, 250, 300, 300)

    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(loading_state)
    pass


def pause():
    pass


def resume():
    pass




