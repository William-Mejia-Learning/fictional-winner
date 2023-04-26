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
    #player = pygame.draw.circle(screen, 'White', player_pos, 10)

    player_surf_dict = {
            'player_surf_down': pygame.image.load('assets/down.png').convert_alpha(),
            'player_surf_up': pygame.image.load('assets/up.png').convert_alpha(),
            'player_surf_left': pygame.image.load('assets/left.png').convert_alpha(),
            'player_surf_right': pygame.image.load('assets/right.png').convert_alpha(),
            }
    player_rect_dict = {
            'player_rect_down': player_surf_dict['player_surf_down'].get_rect(midbottom=(20,20)),
            'player_rect_up': player_surf_dict['player_surf_up'].get_rect(midbottom=(0,0)),
            'player_rect_left': player_surf_dict['player_surf_left'].get_rect(midbottom=(0,0)),
            'player_rect_right': player_surf_dict['player_surf_right'].get_rect(midbottom=(0,0)),
            }

    bush_surf = pygame.image.load('assets/PNG/Assets/Bush_simple1_1.png').convert_alpha()
    bush_2_surf = pygame.image.load('assets/PNG/Assets/Burned_tree1.png').convert_alpha()
    
    assets_dict = {
            'bush_rect': bush_surf.get_rect(midbottom=(80,300)),
            'bush_rect_2': bush_surf.get_rect(midbottom=(100,200)),
            'bush_rect_3':bush_surf.get_rect(midbottom=(100,500)),
            'bush_rect_4': bush_surf.get_rect(midbottom=(200,300)),
            'bush_rect_5': bush_surf.get_rect(midbottom=(300,300)),
            'bush_rect_6': bush_surf.get_rect(midbottom=(50,300))

            }


    bush2_rect = bush_surf.get_rect(midbottom=(100,100)) 

     
    for key, value in assets_dict.items():
        screen.blit(bush_surf, value)
    screen.blit(bush_2_surf, bush2_rect)
    
    
    pygame.draw.rect(screen,
    print(player_surf_dict)
    

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
