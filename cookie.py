from pico2d import *

import game_framework
import main_state

s_DOWN, s_UP, SPACE_DOWN, JumpToIdle, JumpToSlide, CookieDeath = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_s): s_DOWN,
    (SDL_KEYUP, SDLK_s): s_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
}

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 25.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

JUMP_SPEED_MPM = 25.0
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

GRAVITY_SPEED_MPM = 10.0
GRAVITY_SPEED_MPS = (GRAVITY_SPEED_MPM / 60.0)
GRAVITY_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


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
        life = main_state.get_health()
        obstacle = main_state.get_obstacle()
        if life.health > 0:
            cookie.x += RUN_SPEED_PPS * game_framework.frame_time
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if life.health < 0:
            cookie.death_frame = cookie.death_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time \
                                 / 3
            if cookie.death_frame > 3:
                cookie.death_frame = 3

    @staticmethod
    def draw(cookie):
        life = main_state.get_health()
        if life.health > 0:
            cookie.image1.clip_draw(int(cookie.frame) * 80, 0, cookie.Width, cookie.Height, 200, cookie.y, 80, 90)
        else:
            cookie.image5.clip_draw(int(cookie.death_frame) * 120, 0, cookie.Width + 30, cookie.Height, 200, 100, 150,
                                    130)


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
        life = main_state.get_health()
        if life.health > 0:
            cookie.x += RUN_SPEED_PPS * game_framework.frame_time
        cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
        if life.health < 0:
            cookie.death_frame = cookie.death_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time / 3
            if cookie.death_frame > 3:
                cookie.death_frame = 3


    @staticmethod
    def draw(cookie):
        life = main_state.get_health()
        if cookie.isSlide and not cookie.isJump and life.health > 0:
            cookie.image2.clip_draw(int(cookie.frame) * 110, 0, cookie.Width + 30, cookie.Height,
                                    200, cookie.y - 20, 130, 80)
        else:
            cookie.image5.clip_draw(int(cookie.death_frame) * 120, 0, cookie.Width + 30, cookie.Height, 200, 100, 150,
                                    130)


class JumpState:
    @staticmethod
    def enter(cookie, event):
        if event == SPACE_DOWN and not cookie.isJump:
            cookie.isJump = True
            cookie.velocity = JUMP_SPEED_PPS / 2.5
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
        life = main_state.get_health()
        if life.health > 0:
            cookie.x += RUN_SPEED_PPS * game_framework.frame_time
        cookie.velocity -= GRAVITY_SPEED_PPS * game_framework.frame_time
        cookie.y += cookie.velocity
        if cookie.isJump:
            cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            if cookie.y < 115:
                cookie.y = 115
                cookie.isJump = False
                if not cookie.isSlide:
                    cookie.add_event(JumpToIdle)
                elif cookie.isSlide:
                    cookie.add_event(JumpToSlide)
        if life.health < 0:
            cookie.death_frame = cookie.death_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time / 3
            if cookie.death_frame > 3:
                cookie.death_frame = 3
                if life.health < -10:
                    game_framework.quit()

    @staticmethod
    def draw(cookie):
        life = main_state.get_health()
        if life.health > 0:
            cookie.image3.clip_draw(int(cookie.frame) * 80, 0, cookie.Width, cookie.Height, 200, cookie.y, 100, 120)
        else:
            cookie.image5.clip_draw(int(cookie.death_frame) * 120, 0, cookie.Width + 30, cookie.Height, 200, 100, 150,
                                    130)


class DoubleJumpState:
    @staticmethod
    def enter(cookie, event):
        if event == SPACE_DOWN and not cookie.isDoubleJump:
            cookie.isDoubleJump = True
            cookie.velocity = JUMP_SPEED_PPS / 2.5
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
        life = main_state.get_health()
        if life.health > 0:
            cookie.x += RUN_SPEED_PPS * game_framework.frame_time
        if cookie.isDoubleJump:
            if cookie.frame < 8:
                cookie.frame += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
            cookie.velocity -= GRAVITY_SPEED_PPS * game_framework.frame_time
            cookie.y += cookie.velocity
            if cookie.y < 115:
                cookie.y = 115
                cookie.isJump = False
                cookie.isDoubleJump = False
                if not cookie.isSlide:
                    cookie.add_event(JumpToIdle)
                elif cookie.isSlide:
                    cookie.add_event(JumpToSlide)
        if life.health < 0:
            cookie.death_frame = cookie.death_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time / 3
            if cookie.death_frame > 3:
                cookie.death_frame = 3
                if life.health < -10:
                    game_framework.quit()

    @staticmethod
    def draw(cookie):
        life = main_state.get_health()
        if life.health > 0:
            cookie.image4.clip_draw(int(cookie.frame) * 80, 0, cookie.Width, cookie.Height, 200, cookie.y, 100, 120)
        else:
            cookie.image5.clip_draw(int(cookie.death_frame) * 120, 0, cookie.Width + 30, cookie.Height, 200, 100, 150,
                                    130)


class DeathState:
    @staticmethod
    def enter(cookie, event):
        if event == SPACE_DOWN:
            pass
        elif event == s_UP:
            pass
        elif event == s_DOWN:
            pass
        cookie.frame = 0
        cookie.delay_frame = 5
        pass

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        cookie.delay_frame -= 1
        if cookie.frame < 3 and cookie.delay_frame == 0:
            cookie.frame += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time
            cookie.delay_frame = 5
        pass

    @staticmethod
    def draw(cookie):
        cookie.image5.clip_draw(int(cookie.frame) * 120, 0, cookie.Width + 30, cookie.Height, 200, 100, 150, 130)
        pass


next_state_table = {
    IdleState: {s_DOWN: SlideState, s_UP: SlideState,
                SPACE_DOWN: JumpState, CookieDeath: DeathState},
    SlideState: {s_DOWN: IdleState, s_UP: IdleState,
                 SPACE_DOWN: JumpState, CookieDeath: DeathState },
    JumpState: {SPACE_DOWN: DoubleJumpState,
                JumpToIdle: IdleState, JumpToSlide: SlideState,
                s_DOWN: JumpState, s_UP: JumpState,
                CookieDeath: DeathState},
    DoubleJumpState: {SPACE_DOWN: DoubleJumpState,
                      JumpToIdle: IdleState, JumpToSlide: SlideState,
                      s_DOWN: DoubleJumpState, s_UP: DoubleJumpState,
                      CookieDeath: DeathState}
}


class Cookie:
    def __init__(self):
        self.Width, self.Height = 80, 100
        self.x, self.y = 200, 115
        self.frame = 0
        self.velocity = 0
        self.movement = 0
        self.isSlide = False
        self.isJump = False
        self.isDoubleJump = False
        self.delay_frame = 0
        self.death_frame = 0
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

    def get_bb(self):
        if self.y <= 115 and self.isSlide:
            return 155, self.y - 45, 245, self.y + 5
        else:
            return 170, self.y - 40, 230, self.y + 40

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
        draw_rectangle(*self.get_bb())
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass
