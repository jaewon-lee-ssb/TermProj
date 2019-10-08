from pico2d import *

open_canvas(1000, 500)
image1 = load_image('land0001_tm001_bg.png')
image2 = load_image('land0001_tm001_bg.png')
character = load_image('brave_cookie_running.png')
character_slide = load_image('brave_cookie_slide.png')

image1Width = 500
image2Width = 1500
frame = 0
running = True
dir = 0


def handle_events():
    global running
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_DOWN:
                dir += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                dir -= 1


while running:
    clear_canvas()
    image1.clip_draw(0, 0, 1000, 500, image1Width, 250)
    image2.clip_draw(0, 0, 1000, 500, image2Width, 250)
    if dir == 0:
        character.clip_draw(frame * 80, 0, 80, 100, 100, 90)
    elif dir == 1:
        character_slide.clip_draw(frame * 80, 0, 80, 100, 100, 90)
    if image1Width == -500:
        image1Width = 500
    if image2Width == 500:
        image2Width = 1500
    frame = (frame + 1) % 4
    update_canvas()
    image1Width -= 2
    image2Width -= 2

    delay(0.01)
    get_events()

close_canvas()
