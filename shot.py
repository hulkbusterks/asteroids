from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.velocity = PLAYER_SHOOT_SPEED
    
    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt


    

