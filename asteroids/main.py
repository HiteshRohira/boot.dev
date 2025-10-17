import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot

def main():
    # Pygame init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #Clock init
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Player init
    Player.containers = (updatable, drawable) # pyright: ignore[reportAttributeAccessIssue]
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable) # pyright: ignore[reportAttributeAccessIssue]

    AsteroidField.containers = (updatable) # pyright: ignore[reportAttributeAccessIssue]
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable) # pyright: ignore[reportAttributeAccessIssue]

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        updatable.update(dt)

        for item in asteroids:
            if (player.check_collision(item)):
                print("Game over!")
                exit()

        for asteroid_item in asteroids:
            for shot_item in shots:
                if (asteroid_item.check_collision(shot_item)):
                    asteroid_item.split()
                    shot_item.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
