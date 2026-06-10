import pygame

def draw_road(screen, width, height):
    screen.fill((30, 30, 30))

    lane_color = (200, 200, 200)
    for x in [133, 266]:
        pygame.draw.line(screen, lane_color, (x, 0), (x, height), 2)