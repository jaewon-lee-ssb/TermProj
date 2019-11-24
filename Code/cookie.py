from pico2d import *

import game_framework
import main_state
import start_state

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
            cookie.death_count += 1
            if cookie.death_count == 1:
                cookie.death()
            cookie.death_frame = cookie.death_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time / 3
            if cookie.death_frame > 4:
                cookie.death_frame = 4
                if life.health < -10:
                    game_framework.change_state(start_state)

        if obstacle.isCollide and not cookie.isCollide:
            cookie.isCollide = True
            cookie.collide_sound.play(1)
            cookie.collide_time = 1

        if cookie.isCollide:
            cookie.collide_time -= game_framework.frame_time * 5
            if not obstacle.isCollide:
                cookie.isCollide = False
                cookie.collide_time = 0

    @staticmethod
    def draw(cookie):
        life = main_state.get_health()
        if cookie.collide_time > 0:
            cookie.image.clip_draw(2, 274, 270, 270, 200, cookie.y, 160, 165)
        elif life.health > 0:
            cookie.image.clip_draw(2 + int(cookie.frame) * 272, 1090, 270, 270, 200, cookie.y, 160, 165)
        else:
            cookie.image.clip_draw(1362 + int(cookie.death_frame) * 272, 274, 270, 270, 200, cookie.y, 160, 165)


class SlideState:
    @staticmethod
    def enter(cookie, event):
        if event == s_DOWN:
            cookie.isSlide = True
            cookie.slide_sound.play(1)
        elif event == s_UP:
            cookie.isSlide = False
        cookie.frame = 0

    @staticmethod
    def exit(cookie, event):
        pass

    @staticmethod
    def do(cookie):
        life = main_state.get_health()
        obstacle = main_state.get_obstacle()

        if life.health > 0:
            cookie.x += RUN_SPEED_PPS * game_framework.frame_time

        cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

        if life.health < 0:
            cookie.death_count += 1
            if cookie.death_count == 1:
                cookie.death()
            cookie.death_frame = cookie.death_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time / 3
            if cookie.death_frame > 4:
                cookie.death_frame = 4
                if life.health < -10:
                    game_framework.change_state(start_state)

        if obstacle.isCollide and not cookie.isCollide:
            cookie.isCollide = True
            cookie.collide_sound.play(1)
            cookie.collide_time = 1

        if cookie.isCollide:
            cookie.collide_time -= game_framework.frame_time * 5
            if not obstacle.isCollide:
                cookie.isCollide = False
                cookie.collide_time = 0

    @staticmethod
    def draw(cookie):
        life = main_state.get_health()
        if cookie.collide_time > 0:
            cookie.image.clip_composite_draw(2, 274, 270, 268, 3.141592 / 2, '', 200 - 30, cookie.y - 50, 160, 165)
        elif cookie.isSlide and not cookie.isJump and life.health > 0:
            cookie.image.clip_draw(2450 + int(cookie.frame) * 272, 1362, 270, 270, 200, cookie.y, 160, 165)
        else:
            cookie.image.clip_draw(1362 + int(cookie.death_frame) * 272, 274, 270, 270, 200, cookie.y, 160, 165)


class JumpState:
    @staticmethod
    def enter(cookie, event):
        if event == SPACE_DOWN and not cookie.isJump:
            cookie.isJump = True
            cookie.velocity = JUMP_SPEED_PPS / 2.5
            cookie.frame = 0
            cookie.collide_time = 0
            cookie.jump_sound.play(1)
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
        obstacle = main_state.get_obstacle()

        if life.health > 0:
            cookie.x += RUN_SPEED_PPS * game_framework.frame_time

        cookie.velocity -= GRAVITY_SPEED_PPS * game_framework.frame_time
        cookie.y += cookie.velocity

        if cookie.isJump:
            cookie.frame = (cookie.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2
            if cookie.y < 150:
                cookie.y = 150
                cookie.isJump = False
                if not cookie.isSlide:
                    cookie.add_event(JumpToIdle)
                elif cookie.isSlide:
                    cookie.add_event(JumpToSlide)
                    cookie.slide_sound.play(1)

        if life.health < 0:
            cookie.death_count += 1
            if cookie.death_count == 1:
                cookie.death()
            cookie.death_frame = cookie.death_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time / 3
            if cookie.death_frame > 4:
                cookie.death_frame = 4
                if life.health < -10:
                    game_framework.change_state(start_state)

        if obstacle.isCollide and not cookie.isCollide:
            cookie.isCollide = True
            cookie.collide_sound.play(1)
            cookie.collide_time = 1

        if cookie.isCollide:
            cookie.collide_time -= game_framework.frame_time * 5
            if not obstacle.isCollide:
                cookie.isCollide = False
                cookie.collide_time = 0

    @staticmethod
    def draw(cookie):
        life = main_state.get_health()
        if cookie.collide_time > 0:
            cookie.image.clip_draw(2, 274, 270, 270, 200, cookie.y, 160, 165)
        elif life.health > 0:
            cookie.image.clip_draw(1906 + int(cookie.frame) * 272, 1362, 270, 270, 195, cookie.y + 10, 170, 175)
        else:
            cookie.image.clip_draw(1362 + int(cookie.death_frame) * 272, 274, 270, 270, 200, cookie.y, 160, 165)


class DoubleJumpState:
    @staticmethod
    def enter(cookie, event):
        if event == SPACE_DOWN and not cookie.isDoubleJump:
            cookie.isDoubleJump = True
            cookie.velocity = JUMP_SPEED_PPS / 2.5
            cookie.frame = 0
            cookie.count = 1
            cookie.jump_sound.play(1)
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
        obstacle = main_state.get_obstacle()

        if life.health > 0:
            cookie.x += RUN_SPEED_PPS * game_framework.frame_time

        if cookie.isDoubleJump:
            if cookie.frame < 5:
                cookie.frame += FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time / 1.2
                if cookie.frame > 3 and cookie.count == 1:
                    cookie.frame = 1
                    cookie.count -= 1
            cookie.velocity -= GRAVITY_SPEED_PPS * game_framework.frame_time
            cookie.y += cookie.velocity
            if cookie.y < 150:
                cookie.y = 150
                cookie.isJump = False
                cookie.isDoubleJump = False
                if not cookie.isSlide:
                    cookie.add_event(JumpToIdle)
                elif cookie.isSlide:
                    cookie.add_event(JumpToSlide)
                    cookie.slide_sound.play(1)

        if life.health < 0:
            cookie.death_count += 1
            if cookie.death_count == 1:
                cookie.death()
            cookie.death_frame = cookie.death_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time / 3
            if cookie.death_frame > 4:
                cookie.death_frame = 4
                if life.health < -10:
                    game_framework.change_state(start_state)

        if obstacle.isCollide and not cookie.isCollide:
            cookie.isCollide = True
            cookie.collide_sound.play(1)
            cookie.collide_time = 1

        if cookie.isCollide:
            cookie.collide_time -= game_framework.frame_time * 5
            if not obstacle.isCollide:
                cookie.isCollide = False
                cookie.collide_time = 0

    @staticmethod
    def draw(cookie):
        life = main_state.get_health()
        if cookie.collide_time > 0:
            cookie.image.clip_draw(2, 274, 270, 270, 200, cookie.y, 160, 165)
        elif life.health > 0:
            cookie.image.clip_draw(2 + int(cookie.frame) * 272, 1362, 270, 270, 200, cookie.y, 160, 165)
        else:
            cookie.image.clip_draw(1362 + int(cookie.death_frame) * 272, 274, 270, 270, 200, cookie.y, 160, 165)


next_state_table = {
    IdleState: {s_DOWN: SlideState, s_UP: SlideState,
                SPACE_DOWN: JumpState},
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
    image = None

    def __init__(self):
        if self.image is None:
            self.image = load_image('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\BraveCookie\\Brave Cookie.png')
        self.jump_sound = load_wav('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Sound\\Jump.ogg')
        self.slide_sound = load_wav('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Sound\\Slide.ogg')
        self.death_sound = load_wav('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Sound\\Death.ogg')
        self.death_sound.set_volume(120)
        self.collide_sound = load_wav('C:\\Users\\jaewo\\Desktop\\2DGP\\TermProj\\Sound\\Collide.ogg')
        self.collide_sound.set_volume(80)
        self.Width, self.Height = 80, 100
        self.x, self.y = 150, 150
        self.frame = 0
        self.velocity = 0
        self.movement = 0
        self.isSlide = False
        self.isJump = False
        self.isDoubleJump = False
        self.isCollide = False
        self.collide_time = 0
        self.delay_frame = 0
        self.death_frame = 0
        self.count = 0
        self.death_count = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def death(self):
        self.death_sound.play(1)

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
        if self.y <= 150 and self.isSlide:  # 슬라이드 시
            return 155, self.y - 80, 245, self.y - 40
        else:  # 슬라이드 아닐때
            return 180, self.y - 80, 220, self.y

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
        # draw_rectangle(*self.get_bb())
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
        pass
