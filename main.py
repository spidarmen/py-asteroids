import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pygame.display.set_caption("Asteroids")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    BLACK = (0, 0, 0)
    dt    = 0

    #create groups
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for i in updatable:
            i.update(dt)

        for i in drawable:
            i.draw(screen)

        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()