import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
  
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # This will exit the loop and the program
        
        dt = clock.tick(60) / 1000
        keys = pygame.key.get_pressed()
        player.update(keys, dt)
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
                          

if __name__ == "__main__":
    main()

    test 123