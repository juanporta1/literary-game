import pygame
from src.player import Player
from src.floors_create import Floors_Create
import src.const as const
import images
from src.ladder import Ladder
import src.levels as levels
from src.menu import Menu


pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT),pygame.FULLSCREEN)
run = True

level1 = levels.Level_1(screen)
initial_menu = Menu(screen)
while run:
    clock.tick(const.FPS)
    key_pressed = pygame.key.get_pressed()
    
    level1.call_level_1()
    
        
    for event in pygame.event.get():
        if key_pressed[pygame.K_ESCAPE]:
            run = False
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

    

pygame.quit()