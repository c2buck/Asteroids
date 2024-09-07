# player.py
from constants import *

import pygame

# Importing CircleShape from circleshape.py
from circleshape import CircleShape

# Define the Player class that inherits from CircleShape
class Player(CircleShape):
    def __init__(self, x: int, y: int):
        # Call the parent class (CircleShape) constructor
        # Call the parent class's constructor with x and y
        super().__init__(x, y, PLAYER_RADIUS)
        
        # You can add additional attributes or methods for the Player class here
        # Initialize the rotation field
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

        # You can add additional Player-specific behavior here

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]