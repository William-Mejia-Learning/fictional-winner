import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
