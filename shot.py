import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, position, rotation):
        super().__init__(position.x,position.y,SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation)
       
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
                
    def update(self, dt):
        self.position += self.velocity*dt*PLAYER_SHOOT_SPEED
    