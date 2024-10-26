import pygame
from constants import *
from player import Player
from asteroidfield import *
from asteroid import *
from shot import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for p in updatable:
            p.update(dt)

        for a in asteroids:
            for s in shots:
                if s.collision(a):
                    s.kill()
                    a.split()

            if player.collision(a):
                sys.exit("Game Over!")
        
        screen.fill("black")

        for p in drawable:
            p.draw(screen)

        pygame.display.flip()
        
        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
