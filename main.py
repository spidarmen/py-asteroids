import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")

    pygame.init()
    
    default_font = pygame.font.Font(None, 72)  # should load data like fonts only once
    text_surface = default_font.render(f"{PLAYER_SPEED}", True, pygame.Color('#FFFFFF'))
    text_position = (0, 0)                 # where the text is going to be drawn

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    game_clock = pygame.time.Clock()

    #create groups
    updatable = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots     = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    BLACK = (0, 0, 0)
    dt    = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for i in updatable:
            i.update(dt)
            
        
        for i in asteroids:
            if i.collides_with(player):
                print("Game over!")
                #sys.exit()

            for shot in shots:
                if i.collides_with(shot):
                    shot.kill()
                    i.split()

        screen.fill(BLACK)
        screen.blit(text_surface, text_position)

        for i in drawable:
            i.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()