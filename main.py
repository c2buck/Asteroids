import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    
#create groups

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    asteroid_field = AsteroidField()
            
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # This will exit the loop and the program
        
        dt = clock.tick(60) / 1000   

        screen.fill((0, 0, 0))

        for obj in updatable:
            obj.update(dt)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    player.shoot()

        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.is_colliding_with(shot):
                    shot.kill()
                    asteroid.kill()  

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
                          
if __name__ == "__main__":
    main()

