import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_state, log_event
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            vel1 = self.velocity.rotate(new_angle)
            vel2 = self.velocity.rotate(-new_angle)
            new_rad = self.radius -ASTEROID_MIN_RADIUS

            new_ast1 = Asteroid(self.position.x,self.position.y,new_rad)
            new_ast2 = Asteroid(self.position.x,self.position.y,new_rad)

            new_ast1.velocity = vel1 * 1.2
            new_ast2.velocity = vel2 * 1.2

