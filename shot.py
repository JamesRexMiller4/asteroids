import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS) -> None:
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "#f8f8ff", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt