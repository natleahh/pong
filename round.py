import pygame
from mobile import Paddle, Ball
from settings import *


class Round:
    SCORE = {1: 0, 2: 0}

    def __init__(self):
        self.display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.all_sprites = pygame.sprite.Group()
        self.active = True
        self.setup()

    def setup(self):
        self.players = pygame.sprite.Group()
        self.player1 = Paddle(PADDLE_WIDTH * 2, 1, self.players)
        self.player2 = Paddle(SCREEN_WIDTH - PADDLE_WIDTH * 2, 2, self.players)
        self.all_sprites.add(self.players)

        self.ball = Ball(self.all_sprites)

    def run(self, dt):

        for player in self.players:
            if self.ball.rect.colliderect(player.rect):
                self.ball.bounce(player.rect)

        self.active = 0 < self.ball.p.x < SCREEN_WIDTH

        self.all_sprites.update(dt)
        self.all_sprites.draw(self.display_surface)
        if not self.active:
            winner = 1 if self.ball.p.x < SCREEN_WIDTH / 2 else 2
            Round.SCORE[winner] += 1
            return winner


