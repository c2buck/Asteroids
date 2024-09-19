import pygame
from constants import *
from circleshape import CircleShape
from circleshape import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.direction = 0
        self.position = pygame.Vector2(640, 360)
        self.shots = pygame.sprite.Group()

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        rotation_amount = PLAYER_TURN_SPEED * dt
        self.rotation += rotation_amount

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS) #create the shot
        direction = pygame.Vector2(0, 1).rotate(self.direction)
        direction = direction.rotate(self.rotation)
        new_shot.velocity = direction * PLAYER_SHOOT_SPEED
        self.shots.add(new_shot)
        print("Current rotation:", self.rotation)
        print("Current shooting direction: ", direction)