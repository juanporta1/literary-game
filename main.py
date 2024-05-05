import pygame
from src.player import Player
from src.floors_create import Floors_Create
import src.const as const
import images
from src.ladder import Ladder
import src.levels as levels
from src.menu import Menu


pygame.init()
principal_run = True

clock = pygame.time.Clock()
screen = pygame.display.set_mode((const.SCREEN_WIDTH,const.SCREEN_HEIGHT),pygame.FULLSCREEN)
run = True

actual_level = 1

level1 = levels.Level_1(screen)
level2 = levels.Level_2(screen)
initial_menu = Menu(screen,1,"JUGAR", "SALIR")

while principal_run:
    
    clock.tick(const.FPS)
    key_pressed = pygame.key.get_pressed()
    option = initial_menu.call_inital_menu()
    actual_level = 1
    
    
    if not option:
        principal_run = option
        continue
      
    if actual_level == 1:
        actual_level = level1.call_level_1()
        
    elif actual_level == 2:
        actual_level = level2.call_level_2()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            principal_run = False
        
        
    pygame.display.update()

pygame.quit()