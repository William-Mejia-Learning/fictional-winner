import pygame
from random import randrange
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(20, 50)
dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    grass_surf = pygame.draw.rect(screen, 'Green', pygame.Rect(0,0,500,500))
    sand_turf = pygame.draw.rect(screen, (194, 178, 128), pygame.Rect(500,0,500,500))
    water_surf = pygame.draw.rect(screen, '#00FFFF', pygame.Rect(850,0, 150,500))
    player = pygame.draw.circle(screen, 'White', player_pos, 10)
    
    bush_list = []
    bush_surf = pygame.image.load('assets/PNG/Assets/Bush_simple1_1.png').convert_alpha()
    bush_rect = bush_surf.get_rect(midbottom=(80,300))

    screen.blit(bush_surf, bush_rect)
    
    
    screen.blit(bush_surf, bush_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 40 * dt
    if keys[pygame.K_s]:
        player_pos.y += 40 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 40 * dt
    if keys[pygame.K_d]:
        player_pos.x += 40 * dt

    
    pygame.display.update()
    dt = clock.tick(60) / 1000
