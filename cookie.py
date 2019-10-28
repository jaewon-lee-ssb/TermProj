from pico2d import *
import game_framework

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
            cookie.movement += 1
        elif event == s_UP:
            cookie.movement -= 1
        elif event == SPACE_DOWN:
            cookie.movement += 2
        elif event == SPACE_UP:
            cookie.movement -= 2
        pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 4

    @staticmethod
    def draw(cookie):
        cookie.image1.clip_draw(cookie.frame*80, 0, cookie.Width, cookie.Height, cookie.x, cookie.y)


class SlideState:
    @staticmethod
    def enter(cookie, event):
        if event == s_DOWN:
            cookie.movement += 1
        elif event == s_UP:
            cookie.movement -= 1
        cookie.frame = 0

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 2

    @staticmethod
    def draw(cookie):
        if cookie.movement == 1:
            cookie.image2.clip_draw(cookie.frame * 110, 0, cookie.Width + 30, cookie.Height,
                                    cookie.x, cookie.y - 20, 130, 90)


class JumpState:
    @staticmethod
    def enter(cookie, event):
        if event == SPACE_DOWN:
            cookie.movement == 2
        elif event == SPACE_UP:
            cookie.movement == 0
        cookie.frame = 0

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 2
        if cookie.isJump == 0:
            cookie.y += 10
            if cookie.y == 305:
                cookie.isJump = 1
        elif cookie.isJump == 1:
            cookie.y -= 10
            if cookie.y == 115:
                cookie.isJump = 0

    @staticmethod
    def draw(cookie):
        if cookie.movement == 2:
            cookie.image3.clip_draw(cookie.frame * 80, 0, cookie.Width, cookie.Height,
                                    cookie.x, cookie.y)


next_state_table = {
    IdleState: {s_DOWN: SlideState, s_UP: SlideState,
                SPACE_DOWN: JumpState, SPACE_UP: JumpState},
    SlideState: {s_DOWN: IdleState, s_UP: IdleState},
    JumpState: {SPACE_DOWN: IdleState, SPACE_UP: IdleState}
}


class Cookie:
    def __init__(self):
        self.Width, self.Height = 80, 100
        self.x, self.y = 200, 115
        self.frame = 0
        self.movement = 0
        self.isJump = 0
        self.image1 = load_image('BraveCookie\\brave_cookie_run.png')
        self.image2 = load_image('BraveCookie\\brave_cookie_slide.png')
        self.image3 = load_image('BraveCookie\\brave_cookie_jump.png')
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
        self.event_que.insert(0, event)
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
