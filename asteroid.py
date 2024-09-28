import pygame
from circleshape import CircleShape
# from constants import ASTEROID

class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#f8f8ff", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt