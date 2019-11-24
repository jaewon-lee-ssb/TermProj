import game_framework
import main_state
from pico2d import *


name = "StartGame"
image = None


def enter():
    global image
    image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Image\\Lobby.png')
    pass


def exit():
    global image
    pass


def update():
    pass


def draw():
    global image
    clear_canvas()
    image.draw(500, 250)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_state(main_state)
    pass


def pause():
    pass


def resume():
    pass




