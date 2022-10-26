import math
import random

from settings import *
import pygame


class Mobile(pygame.sprite.Sprite):

    def __init__(self, group, size, p):
        from pygame.math import Vector2 as Vector
        super(Mobile, self).__init__(group)
        self.image = pygame.Surface(size)
        self.image.fill("white")
        self.rect = self.image.get_rect(center=p)

        self.p = Vector(self.rect.center)
        self.v = Vector()

    def move(self, dt):
        self.p += self.v * dt
        self.rect.center = self.p


class Ball(Mobile):
    SPEED = 300
    SIZE = 10

    def __init__(self, group):
        super(Ball, self).__init__(
            group=group,
            size=(Ball.SIZE,) * 2,
            p=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )

        # Movement
        heading = 2 * math.pi / random.randint(1, 18) + 0.5
        self.v = pygame.math.Vector2(
            math.sin(heading),
            math.cos(heading)
        ) * Ball.SPEED

    def bounce(self, spin_dist=None):
        if spin_v is None:
            self.v = self.v.reflect([0, 1])
            return
        self.v = self.v.reflect([1, 0])
        self.v = (self.v + spin_v).normalize() * Ball.SPEED

    def update(self, dt):
        if 0 >= self.p.y or SCREEN_HEIGHT <= self.p.y:
            self.bounce()
        self.move(dt)


class Paddle(Mobile):
    ACCEL = pygame.math.Vector2(0, 100)
    DECCEL = pygame.math.Vector2(0, 300)
    MAX_V = pygame.math.Vector2(0, 500)
    LOWER_BOUND, UPPER_BOUND = (PADDLE_HEIGHT / 2, SCREEN_HEIGHT - (PADDLE_HEIGHT / 2))
    PLAYER_PARAMS = {
        1: {"up": pygame.K_q, "down": pygame.K_a},
        2: {"up": pygame.K_p, "down": pygame.K_l},

    }

    def __init__(self, start_x, player, group):
        super(Paddle, self).__init__(
            group=group,
            size=(PADDLE_WIDTH, PADDLE_HEIGHT),
            p=(start_x, SCREEN_HEIGHT / 2)
        )

        # Input Info
        self.params = Paddle.PLAYER_PARAMS[player]
        self.up = False
        self.down = False

        # Movement Info
        self.a = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()
        self.a = (keys[self.params["down"]] - keys[self.params["up"]]) * Paddle.ACCEL

    def update(self, dt):
        if self.a:
            self.v += self.a if self.v.magnitude() <= Paddle.MAX_V.magnitude() else pygame.math.Vector2()
        elif abs(self.v.magnitude()) > Paddle.DECCEL.magnitude() / 2:
            self.v -= Paddle.DECCEL * (1 if self.v.y > 0 else -1) if self.v else pygame.math.Vector2()
        self.input()
        self.move(dt)
        if self.p.y < Paddle.LOWER_BOUND:
            self.p.y = Paddle.LOWER_BOUND
        elif self.p.y > Paddle.UPPER_BOUND:
            self.p.y = Paddle.UPPER_BOUND


