import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.polygon(screen, "#f8f8ff", self.triangle(), 2)

    def update(self, dt):
        pass

    def collision(self, shape) -> bool:
        distance = self.position.distance_to(shape.position)
        if distance >= self.radius + shape.radius:
            return False
        return True