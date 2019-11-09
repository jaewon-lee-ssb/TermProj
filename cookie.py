from pico2d import *
import game_framework

import game_world

s_DOWN, s_UP, SPACE_DOWN, JumpToIdle, JumpToSlide, CookieDeath = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_s): s_DOWN,
    (SDL_KEYUP, SDLK_s): s_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
}


class IdleState:
    @staticmethod
    def enter(cookie, event):
        if event == s_DOWN:
            cookie.isSlide = True
        elif event == s_UP:
            cookie.isSlide = False
        cookie.frame = 0
        pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 4
        cookie.lifetime -= 1
        if cookie.lifetime == 0:
            cookie.add_event(CookieDeath)

    @staticmethod
    def draw(cookie):
        cookie.image1.clip_draw(cookie.frame * 80, 0, cookie.Width, cookie.Height, cookie.x, cookie.y, 80, 90)


class SlideState:
    @staticmethod
    def enter(cookie, event):
        if event == s_DOWN:
            cookie.isSlide = True
        elif event == s_UP:
            cookie.isSlide = False
        cookie.frame = 0

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.frame = (cookie.frame + 1) % 2
        cookie.lifetime -= 1

    @staticmethod
    def draw(cookie):
        if cookie.isSlide and not cookie.isJump:
            cookie.image2.clip_draw(cookie.frame * 110, 0, cookie.Width + 30, cookie.Height,
                                    cookie.x, cookie.y - 20, 130, 80)


class JumpState:
    @staticmethod
    def enter(cookie, event):
        if event == SPACE_DOWN and not cookie.isJump:
            cookie.isJump = True
            cookie.acceleration = 25
            cookie.frame = 0
        elif event == s_UP:
            cookie.isSlide = False
        elif event == s_DOWN:
            cookie.isSlide = True

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.lifetime -= 1
        if cookie.isJump:
            cookie.frame = (cookie.frame + 1) % 2
            cookie.acceleration -= 3
            cookie.y += cookie.acceleration
            if cookie.y < 115:
                cookie.y = 115
                cookie.isJump = False
                if not cookie.isSlide:
                    cookie.add_event(JumpToIdle)
                elif cookie.isSlide:
                    cookie.add_event(JumpToSlide)

    @staticmethod
    def draw(cookie):
        cookie.image3.clip_draw(cookie.frame * 80, 0, cookie.Width, cookie.Height, cookie.x, cookie.y, 100, 120)


class DoubleJumpState:
    @staticmethod
    def enter(cookie, event):
        if event == SPACE_DOWN and not cookie.isDoubleJump:
            cookie.isDoubleJump = True
            cookie.acceleration = 30
            cookie.frame = 0
        elif event == s_UP:
            cookie.isSlide = False
        elif event == s_DOWN:
            cookie.isSlide = True

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.lifetime -= 1
        if cookie.isDoubleJump:
            if cookie.frame < 8:
                cookie.frame += 1
                cookie.delayframe = 1
            cookie.delayframe -= 1
            if 8 < cookie.frame and cookie.delayframe == 0:
                cookie.frame += 1
                cookie.delayframe = 2
            cookie.acceleration -= 3
            cookie.y += cookie.acceleration
            if cookie.y < 115:
                cookie.y = 115
                cookie.isJump = False
                cookie.isDoubleJump = False
                if not cookie.isSlide:
                    cookie.add_event(JumpToIdle)
                elif cookie.isSlide:
                    cookie.add_event(JumpToSlide)

    @staticmethod
    def draw(cookie):
        cookie.image4.clip_draw(cookie.frame * 80, 0, cookie.Width, cookie.Height, cookie.x, cookie.y, 100, 120)


class DeathState:
    @staticmethod
    def enter(cookie, event):
        cookie.frame = 0
        cookie.delayframe = 5
        pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.delayframe -= 1
        if cookie.frame < 3 and cookie.delayframe == 0:
            cookie.frame += 1
            cookie.delayframe = 5
        pass

    @staticmethod
    def draw(cookie):
        cookie.image5.clip_draw(cookie.frame * 120, 0, cookie.Width + 30, cookie.Height, cookie.x, cookie.y, 150, 130)
        pass


next_state_table = {
    IdleState: {s_DOWN: SlideState, s_UP: SlideState,
                SPACE_DOWN: JumpState, CookieDeath: DeathState},
    SlideState: {s_DOWN: IdleState, s_UP: IdleState,
                 SPACE_DOWN: JumpState},
    JumpState: {SPACE_DOWN: DoubleJumpState,
                JumpToIdle: IdleState, JumpToSlide: SlideState,
                s_DOWN: JumpState, s_UP: JumpState},
    DoubleJumpState: {SPACE_DOWN: DoubleJumpState,
                      JumpToIdle: IdleState, JumpToSlide: SlideState,
                      s_DOWN: DoubleJumpState, s_UP: DoubleJumpState}
}


class Cookie:
    def __init__(self):
        self.Width, self.Height = 80, 100
        self.x, self.y = 200, 115
        self.frame = 0
        self.movement = 0
        self.isSlide = False
        self.isJump = False
        self.isDoubleJump = False
        self.lifetime = 200
        self.delayframe = 0
        self.acceleration = 0
        self.image1 = load_image('BraveCookie\\brave_cookie_run.png')
        self.image2 = load_image('BraveCookie\\brave_cookie_slide.png')
        self.image3 = load_image('BraveCookie\\brave_cookie_jump.png')
        self.image4 = load_image('BraveCookie\\brave_cookie_double_jump.png')
        self.image5 = load_image('BraveCookie\\brave_cookie_death.png')
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def update_state(self):
        if len(self.event_que) > 0:
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
