import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20,50)
        vec1 = self.velocity.rotate(random_angle)
        vec2 = self.velocity.rotate(-random_angle)
        medium_new_radius = ASTEROID_MAX_RADIUS - ASTEROID_MIN_RADIUS
        small_new_radius = ASTEROID_MAX_RADIUS - 2 * ASTEROID_MIN_RADIUS
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        elif(self.radius == ASTEROID_MAX_RADIUS):
            asteroid1 = Asteroid(self.position.x, self.position.y, medium_new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, medium_new_radius)
            asteroid1.velocity = vec1 * 1.2
            asteroid2.velocity = vec2 * 1.2
        else:
            asteroid1 = Asteroid(self.position.x, self.position.y, small_new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, small_new_radius)
            asteroid1.velocity = vec1 * 1.2
            asteroid2.velocity = vec2 * 1.2