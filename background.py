from pico2d import *

open_canvas(1000, 500)


class Cookie:
    def __init__(self):
        self.Width, self.Height = 80, 100
        self.x, self.y = 200, 90
        self.rframe, self.sframe = 0, 0
        self.rimage = load_image('brave_cookie_run.png')
        self.simage = load_image('brave_cookie_slide.png')

    def update(self):
        self.rframe = (self.rframe + 1) % 4
        self.sframe = (self.sframe + 1) % 2

    def draw(self):
        if dir == 0:
            self.rimage.clip_draw(self.rframe*80, 0, self.Width, self.Height, self.x, self.y)
        elif dir == 1:
            self.simage.clip_draw(self.sframe*80, 0, self.Width, self.Height, self.x, self.y)


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
dir = 0
running = True


def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_DOWN:
                dir += 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                dir -= 1


while running:
    handle_events()

    land1.update()
    cookie.update()

    clear_canvas()

    land1.draw()
    cookie.draw()

    update_canvas()

    delay(0.05)
    get_events()

close_canvas()
