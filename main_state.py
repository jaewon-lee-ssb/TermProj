from pico2d import *

open_canvas(1000, 500)

direction = 4


class Cookie:
    def __init__(self):
        self.Width, self.Height = 80, 100
        self.x, self.y = 200, 90
        self.frame = 0
        self.image1 = load_image('brave_cookie_run.png')
        self.image2 = load_image('brave_cookie_slide.png')

    def update(self):
        delay(0.05)
        self.frame = (self.frame + 1) % direction

    def draw(self):
        if direction == 4:
            self.image1.clip_draw(self.frame*80, 0, self.Width, self.Height, self.x, self.y)
        elif direction == 2:
            self.image2.clip_draw(self.frame * 110, 0, self.Width + 30, self.Height, self.x, self.y - 20, 130, 90)


class Land1:
    def __init__(self):
        self.x1, self.x2, self.y = 500, 1500, 250
        self.Width, self.Height = 1000, 500
        self.frame = 0
        self.image1 = load_image('land1_stage1_bg.png')
        self.image2 = load_image('land1_stage1_bg.png')

    def update(self):
        self.x1 -= 2
        self.x2 -= 2

    def draw(self):
        self.image1.clip_draw(0, 0, self.Width, self.Height, self.x1, self.y)
        self.image2.clip_draw(0, 0, self.Width, self.Height, self.x2, self.y)


cookie = Cookie()
land1 = Land1()
running = True


def handle_events():
    global running
    global direction
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_s:
                direction = 2
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_s:
                direction = 4


while running:
    handle_events()

    land1.update()
    cookie.update()

    clear_canvas()

    land1.draw()
    cookie.draw()

    update_canvas()

close_canvas()