import pygame
from config import LANES

class Car:
    def __init__(self):
        self.lane = 1
        self.x = LANES[self.lane]
        self.y = 500
        self.width = 40
        self.height = 60

    def move_left(self):
        if self.lane > 0:
            self.lane -= 1
        self.x = LANES[self.lane]

    def move_right(self):
        if self.lane < 2:
            self.lane += 1
        self.x = LANES[self.lane]

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0),
                         (self.x, self.y, self.width, self.height))