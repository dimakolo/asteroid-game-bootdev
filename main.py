# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

#TODO list:
# - game score display
# - print the score at the end of the game
# - get 1 point for every frame survived
# - get 10 points for killing asteroid
# - once per game, a yellow asteroid spawns that gives you shooting in all directions (8 cardinal directions)
# - add static landmines with duration of 10 seconds (increases by 1 second every 30 seconds of the game)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids,updatable,drawable)
    Shot.containers = (shots, updatable, drawable)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)

        # if player crashed, exit the game
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print(f"Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        # render the updates
        pygame.display.flip()

        # end of the loop - update the frame rate
        dt = game_clock.tick() / 1000


if __name__ == "__main__":
    main()