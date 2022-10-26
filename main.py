import sys

import pygame
WIDTH, HEIGHT = (800, 400)


class Paddle(pygame.sprite.Sprite):

    PADDLE_DIM = (20, 100)
    MAX_V = 10
    ACCEL = 2
    DECCEL = 4

    def __init__(self, player_pos, bound):
        super().__init__()
        self.image = pygame.Surface(self.PADDLE_DIM).convert_alpha()
        self.image.fill("white")
        self.rect = self.image.get_rect(center=player_pos)
        self.a = 0
        self.v = 0

        self.up = False
        self.down = False
        self.bound = bound

    def update(self):

        # Input Acceleration
        a = (self.ACCEL if self.down else 0) - (self.ACCEL if self.up else 0)

        # Update Acceleration
        if a:
            self.a = a
        # Decay Acceleration
        else:
            self.v -= self.DECCEL * (1 if self.v > 0 else -1) if self.v else self.v
            if abs(self.v) > abs(self.DECCEL) / 2 :
                self.a = 0
                self.v = 0

        # Update Velocity and Position
        self.v += self.a if (-self.MAX_V) < self.v < self.MAX_V else 0
        self.rect.y += self.v

        # Out of Bounds Detection
        if self.rect.midtop[1] <= 0:
            self.rect.y = 0
        elif self.rect.midbottom[1] >= self.bound:
            self.rect.y = self.bound - self.PADDLE_DIM[1]

        print(f"a = {self.a}, v = {self.v}, y = {self.rect.y}")


def main():
    # Setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PONG")
    clock = pygame.time.Clock()

    # Elements Init

    # Player Init
    players = pygame.sprite.Group()
    player_1 = Paddle(
        (20, HEIGHT / 2), HEIGHT
    )
    player_2 = Paddle(
        (WIDTH - 20, HEIGHT / 2), HEIGHT
    )

    players.add(
        player_1,
        player_2
    )

    # Ball Init

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Hold Key Event Checks
            for key_type, bl in ((pygame.KEYUP, False), (pygame.KEYDOWN, True)):
                if event.type != key_type:
                    continue
                if event.key == pygame.K_q:
                    player_1.up = bl
                if event.key == pygame.K_a:
                    player_1.down = bl
                if event.key == pygame.K_p:
                    player_2.up = bl
                if event.key == pygame.K_l:
                    player_2.down = bl

        screen.fill("black")
        players.update()
        players.draw(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
