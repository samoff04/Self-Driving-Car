import pygame
import random
from config import LANES, OBSTACLE_SPEED

class Obstacle:
    def __init__(self):
        self.lane = random.randint(0, 2)
        self.x = LANES[self.lane]
        self.y = -50
        self.width = 40
        self.height = 60

    def move(self):
        self.y += OBSTACLE_SPEED

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),
                         (self.x, self.y, self.width, self.height))