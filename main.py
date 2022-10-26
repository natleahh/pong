import sys

import pygame

from round import Round
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.round = Round()
        self.line = pygame.Surface((10, 50))
        self.line.fill("white")

        # Score Board
        self.font = pygame.font.Font("font/PixeloidSans.ttf", 30)
        self.winner = None

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick() / 1000

            # Court
            self.screen.fill("black")
            for i in range(10):
                self.screen.blit(
                    self.line,
                    (SCREEN_WIDTH // 2 - 5, SCREEN_HEIGHT // 10 * i + 5)
                )
            self.screen.blit(
                self.font.render(f"{Round.SCORE[1]}", False, "white"),
                (SCREEN_WIDTH / 2 - 80, 50)
            )
            self.screen.blit(
                self.font.render(f"{Round.SCORE[2]}", False, "white"),
                (SCREEN_WIDTH / 2 + 50, 50)
            )

            # Round
            if self.round.active:
                self.winner = self.round.run(dt)
            else:
                self.pause_display(dt)
                if any(pygame.key.get_pressed()):
                    del self.round
                    self.round = Round()

            pygame.display.update()

    def pause_display(self, dt):
        #
        pass


if __name__ == '__main__':
    game = Game()
    game.run()
