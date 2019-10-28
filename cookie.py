from pico2d import *

s_DOWN, s_UP, SPACE_DOWN, SPACE_UP = range(4)

key_event_table = {
    (SDL_KEYDOWN, SDLK_s): s_DOWN,
    (SDL_KEYUP, SDLK_s): s_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}


class IdleState:
    @staticmethod
    def enter(cookie, event):
        if event == s_DOWN:
            cookie.velocity += 1
        elif event == s_UP:
            cookie.velocity -= 1
        pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 8

    @staticmethod
    def draw(cookie):
        cookie.image1.clip_draw(cookie.frame*80, 0, cookie.Width, cookie.Height, cookie.x, cookie.y)


class SlideState:
    @staticmethod
    def enter(cookie, event):
        if event == s_DOWN:
            cookie.velocity += 1
        elif event == s_UP:
            cookie.velocity -= 1

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 2

    @staticmethod
    def draw(cookie):
        if cookie.velocity == 1:
            cookie.image2.clip_draw(cookie.frame * 110, 0, cookie.Width + 30, cookie.Height,
                                    cookie.x, cookie.y - 20, 130, 90)


next_state_table = {
    IdleState: {s_DOWN: SlideState, s_UP: SlideState},
    SlideState: {s_DOWN: IdleState, s_UP: IdleState}
}


class Cookie:
    def __init__(self):
        self.Width, self.Height = 80, 100
        self.x, self.y = 200, 115
        self.frame = 0
        self.velocity = 0
        self.image1 = load_image('BraveCookie\\brave_cookie_run.png')
        self.image2 = load_image('BraveCookie\\brave_cookie_slide.png')
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def update_state(self):
        if len(self.event_que) > 0 or self.timer == 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def change_state(self, state):
        pass

    def add_event(self, event):
        pass

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass
