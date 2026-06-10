import pygame
import random

from car import Car
from obstacle import Obstacle
from road import draw_road
from config import WIDTH, HEIGHT

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

car = Car()
obstacles = []
frame_count = 0

def collision(car, obs):
    return (
        car.x < obs.x + obs.width and
        car.x + car.width > obs.x and
        car.y < obs.y + obs.height and
        car.y + car.height > obs.y
    )

running = True
while running:
    clock.tick(30)
    frame_count += 1

    screen.fill((0, 0, 0))
    draw_road(screen, WIDTH, HEIGHT)

    if frame_count % 40 == 0:
        obstacles.append(Obstacle())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for obs in obstacles:
        if abs(obs.y - car.y) < 120 and obs.lane == car.lane:
            if car.lane > 0:
                car.move_left()
            else:
                car.move_right()

    for obs in obstacles:
        obs.move()
        obs.draw(screen)

    obstacles = [o for o in obstacles if o.y < HEIGHT]

    car.draw(screen)

    pygame.display.update()

pygame.quit()