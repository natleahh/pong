import math
import random

from settings import *
import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, group):
        super(Ball, self).__init__(group)
        self.image = pygame.Surface((BALL_SIZE,) * 2)
        self.image.fill("white")
        self.rect = self.image.get_rect()

        # Movement
        self.p = pygame.math.Vector2(self.rect.center)
        heading = 2 * math.pi / random.randint(1, 18) + 0.5
        self.v = pygame.math.Vector2(
            math.sin(heading),
            math.cos(heading)
        ) * BALL_SPEED

    def bounce(self, spin_v=None):
        if spin_v is None:
            self.v = self.v.reflect([0, 1])
            return
        self.v = self.v.reflect([1, 0])
        self.v = (self.v + spin_v).normalize() * BALL_SPEED

    def update(self):
        if 0 >= self.p.y or SCREEN_HEIGHT <= self.p.y:
            self.bounce()

        self.p += self.v
        self.rect.center = self.p



class Paddle(pygame.sprite.Sprite):
    ACCEL = pygame.math.Vector2(0, 1)
    DECCEL = pygame.math.Vector2(0, 3)
    MAX_V = pygame.math.Vector2(0, 5)
    PLAYER_PARAMS = {
        1: {"up": pygame.K_q, "down": pygame.K_a},
        2: {"up": pygame.K_p, "down": pygame.K_l},

    }

    def __init__(self, start_x, player, group):
        super().__init__(group)
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill("white")
        self.rect = self.image.get_rect(center=(start_x, SCREEN_HEIGHT / 2))

        # Input Info
        self.params = Paddle.PLAYER_PARAMS[player]
        self.up = False
        self.down = False

        # Movement Info
        self.a = pygame.math.Vector2()
        self.v = pygame.math.Vector2()
        self.p = pygame.math.Vector2(self.rect.center)

    def input(self):
        keys = pygame.key.get_pressed()
        self.a = (keys[self.params["down"]] - keys[self.params["up"]]) * Paddle.ACCEL

    def move(self):
        if self.a:
            self.v += self.a if self.v.magnitude() <= Paddle.MAX_V.magnitude() else pygame.math.Vector2()
        elif abs(self.v.magnitude()) > Paddle.DECCEL.magnitude() / 2:
            self.v -= Paddle.DECCEL * (1 if self.v.y > 0 else -1) if self.v else pygame.math.Vector2()

        self.p += self.v
        self.rect.center = self.p

    def update(self):
        self.input()
        self.move()

