import sys

import pygame

from paddles import Paddle, Ball
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for player in self.players:
                if self.ball.rect.colliderect(player.rect):
                    self.ball.bounce(player.v)

            self.all_sprites.update()

            self.screen.fill("black")
            self.all_sprites.draw(self.screen)
            self.clock.tick(60)
            pygame.display.update()

    def setup(self):
        self.players = pygame.sprite.Group()
        self.player1 = Paddle(PADDLE_WIDTH * 2, 1, self.players)
        self.player2 = Paddle(SCREEN_WIDTH - PADDLE_WIDTH * 2, 2, self.players)
        self.all_sprites.add(self.players)

        self.ball = Ball(self.all_sprites)

    def reset(self):
        self.ball.kill()
        self.ball = Ball(self.all_sprites)


if __name__ == '__main__':
    game = Game()
    game.run()
