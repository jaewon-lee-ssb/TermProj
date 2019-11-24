import game_framework
import main_state
from pico2d import *

name = "LoadingGame"

loading_time = 0.0


def enter():
    global image, loading_time
    image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Image\\Loading.png')
    
    loading_time = 3.0
    
    pass


def exit():
    global image
    del image
    pass


def update():
    global loading_time
    loading_time -= game_framework.frame_time
    if loading_time < 0:
        game_framework.change_state(main_state)
    pass


def draw():
    clear_canvas()

    image.draw(500, 250, 1000, 500)

    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass


def pause():
    pass


def resume():
    pass




