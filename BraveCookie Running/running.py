from pico2d import *

open_canvas()
character = load_image('brave_cookie_running.png')

x = 0
frame = 0
while True:
    clear_canvas()
    character.clip_draw(frame * 80, 0, 80, 100, 100, 90)
    update_canvas()
    frame = (frame + 1) % 4
    delay(0.1)
    get_events()

close_canvas()
