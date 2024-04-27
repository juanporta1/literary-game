import pygame
from src.player import Player
from src.floors_create import Floors_Create
import src.const as const
import images

pygame.init()
screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT),pygame.FULLSCREEN)
run = True

player = Player(x = 10,
                y = 1080-64-100)

clock = pygame.time.Clock()
FPS = 60
floor1 = Floors_Create(0, 1080 - 64, 31, images.proof_floor, screen)
floor2_1=  Floors_Create(0, 1080 - 64 * 4, 16, images.proof_floor, screen)

while run:
    clock.tick(FPS)
    screen.blit(images.proof_bg, (0,0))
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pressed_keys[pygame.K_ESCAPE]:
            run = False

    player.draw(screen,(255,255,0))
    player.move()
    floor1.draw_floors()
    floor2_1.draw_floors()
    
    
    
    pygame.display.update()

pygame.quit()