from circleshape import *
import pygame
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
                
    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, radius).velocity = pygame.Vector2(self.velocity.rotate(angle)) * 1.2
        Asteroid(self.position.x, self.position.y, radius).velocity = pygame.Vector2(self.velocity.rotate(angle*-1)) * 1.2
        
        